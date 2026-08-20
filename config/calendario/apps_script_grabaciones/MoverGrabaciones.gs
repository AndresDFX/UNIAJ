/**
 * Mueve automáticamente las grabaciones de Google Meet a la carpeta
 * "Clases grabadas" del curso al que corresponden.
 *
 * Corre en la cuenta de Google del docente (Apps Script), con un disparador por tiempo.
 * No necesita servidor ni credenciales: usa los permisos de la propia cuenta.
 *
 * Cómo decide a qué curso pertenece una grabación (en este orden):
 *   1. Por el evento de calendario que la generó: busca en Calendar un evento que se
 *      solape con la hora de la grabación y cuyo título contenga el nombre del curso.
 *      Es el método fiable, porque los eventos ya se llaman
 *      "[SINCRONICO] Sesión N · <Curso>".
 *   2. Si el paso 1 no encuentra nada (grabación de una reunión sin evento, o evento
 *      borrado), cae al horario fijo del curso: día de la semana + ventana de hora.
 *
 * Qué mueve: el video y también los archivos que Meet crea junto a él
 * (transcripción, chat, notas), que quedan en la misma carpeta.
 *
 * INSTALACIÓN — ver LEEME.md en esta misma carpeta.
 */

// ─────────────────────────────────────────────────────────────── CONFIGURACIÓN

/**
 * Un objeto por curso. Los `carpetaGrabadas` salen de
 * `config/calendario/semestre_2026_2.json` → cursos.<curso>.carpetas_drive.grabadas.id
 *
 * `dia`: 0=domingo, 1=lunes … 6=sábado (Date.getDay()).
 * `desde`/`hasta`: ventana horaria en minutos desde medianoche, con holgura para que
 * una grabación que arranca tarde o termina pasada la hora siga cayendo en el curso.
 * `alias`: variantes con las que el curso puede aparecer escrito en el título del
 * evento o en el nombre del archivo (sin tildes, abreviado, etc.).
 */
const CURSOS = [
  {
    nombre: 'Arquitectura de Sistemas Computacionales',
    codigo: 'FI303380',
    carpetaGrabadas: '1rpmcE6xEUZFNOxPV4bfQ0VqVR6wcN9yg',
    dia: 1,            // lunes
    desde: 9 * 60 + 30,  // 09:30
    hasta: 13 * 60,      // 13:00  (clase 10:00–12:00)
    alias: ['arquitectura', 'arquitectura de sistemas', 'fi303380', 'asc'],
  },
  {
    nombre: 'Bases de Datos II',
    codigo: 'FI303215',
    carpetaGrabadas: '10q7c22SXqsabyVRxpLkQnc9doSZamZo6',
    dia: 1,            // lunes
    desde: 17 * 60 + 30, // 17:30
    hasta: 21 * 60,      // 21:00  (clase 18:00–20:00)
    alias: ['bases de datos', 'base de datos', 'bd ii', 'bd2', 'fi303215'],
  },
  {
    nombre: 'Programación II',
    codigo: 'FI303204',
    carpetaGrabadas: '1oTA2kYgBvNbUfzD784R7AQxsIt_BmGmA',
    dia: 3,            // miércoles
    desde: 17 * 60 + 30,
    hasta: 21 * 60,
    alias: ['programacion', 'programación', 'prog ii', 'prog2', 'fi303204'],
  },
  {
    nombre: 'Seminario de Sistemas',
    codigo: 'FI303301',
    carpetaGrabadas: '10XBX8t7dFrBQhxaQrYWZxWr-nwulo3xi',
    dia: 4,            // jueves
    desde: 17 * 60 + 30,
    hasta: 21 * 60,
    alias: ['seminario', 'seminario de sistemas', 'fi303301'],
  },
];

/**
 * ID del calendario donde estan los encuentros del curso.
 *
 * Sale VACIO a proposito: sin el, el script no sabe donde buscar los eventos con los que
 * identifica cada grabacion. Como obtenerlo: ejecuta `listarCalendarios()` (esta abajo) y
 * copia el ID que te interese; o en Google Calendar, en «Mis calendarios», pasa el mouse
 * sobre el calendario -> ⋮ -> «Configuracion y uso compartido» -> baja hasta «Integrar
 * calendario» -> copia «ID de calendario».
 *
 * El principal tiene el ID de tu correo (p. ej. `julianacastano@profesores.uniajc.edu.co`);
 * uno secundario se ve como `abc123...@group.calendar.google.com`.
 */
const CALENDAR_ID = '';

// Alternativa: usar el calendario por omision de la cuenta en vez de un ID explicito.
// Descomenta la linea de _cal_() marcada mas abajo si prefieres eso.

/** Carpeta donde Meet deja las grabaciones. Se busca por nombre en Mi unidad. */
const NOMBRES_CARPETA_MEET = ['Meet Recordings', 'Grabaciones de Meet'];

/** Cuántos días hacia atrás revisar en cada corrida. */
const DIAS_ATRAS = 7;

/** true = no mueve nada, solo escribe en el log lo que haría. */
const SIMULACRO = false;

// ─────────────────────────────────────────────────────────────── ENTRADA

/** Función a programar con el disparador por tiempo. */
function moverGrabaciones() {
  const origen = carpetaMeet_();
  if (!origen) {
    Logger.log('ERROR: no encontré la carpeta de grabaciones de Meet (%s). ' +
               'Si tu Drive la llama distinto, agrégalo a NOMBRES_CARPETA_MEET.',
               NOMBRES_CARPETA_MEET.join(' / '));
    return;
  }

  const desde = new Date();
  desde.setDate(desde.getDate() - DIAS_ATRAS);

  const archivos = origen.getFiles();
  let vistos = 0, movidos = 0, sinCurso = 0;

  while (archivos.hasNext()) {
    const f = archivos.next();
    if (f.getDateCreated() < desde) continue;
    vistos++;

    const curso = cursoDeArchivo_(f);
    if (!curso) {
      sinCurso++;
      Logger.log('SIN CURSO  %s  (%s) — se queda donde está',
                 f.getName(), f.getDateCreated());
      continue;
    }

    if (SIMULACRO) {
      Logger.log('[SIMULACRO] movería "%s" -> %s', f.getName(), curso.nombre);
      movidos++;
      continue;
    }

    try {
      const destino = DriveApp.getFolderById(curso.carpetaGrabadas);
      f.moveTo(destino);
      movidos++;
      Logger.log('MOVIDO     %s  ->  %s', f.getName(), curso.nombre);
    } catch (e) {
      Logger.log('ERROR moviendo "%s" a %s: %s', f.getName(), curso.nombre, e.message);
    }
  }

  Logger.log('Resumen: %s archivo(s) recientes · %s movido(s) · %s sin curso%s',
             vistos, movidos, sinCurso, SIMULACRO ? ' · SIMULACRO' : '');
}

/** Corre una vez sin mover nada, para revisar el log antes de activarlo de verdad. */
function simulacro() {
  Logger.log('--- SIMULACRO: no se mueve nada ---');
  const origen = carpetaMeet_();
  if (!origen) { Logger.log('No encontré la carpeta de Meet.'); return; }
  const desde = new Date();
  desde.setDate(desde.getDate() - DIAS_ATRAS);
  const it = origen.getFiles();
  while (it.hasNext()) {
    const f = it.next();
    if (f.getDateCreated() < desde) continue;
    const c = cursoDeArchivo_(f);
    Logger.log('%s  ->  %s', f.getName(), c ? c.nombre : '(sin curso)');
  }
}

// ─────────────────────────────────────────────────────────────── LÓGICA

/**
 * El calendario con el que trabaja el script.
 * Preferimos un ID explicito: el «por omision» depende de la cuenta con la que se abrio
 * Apps Script, y si un dia se ejecuta con otra sesion mira un calendario distinto sin avisar.
 */
function _cal_() {
  if (CALENDAR_ID) {
    const c = CalendarApp.getCalendarById(CALENDAR_ID);
    if (!c) throw new Error('CALENDAR_ID no corresponde a un calendario visible: ' + CALENDAR_ID);
    return c;
  }
  // return CalendarApp.getDefaultCalendar();   // <- alternativa: calendario por omision
  throw new Error('Falta CALENDAR_ID. Ejecuta listarCalendarios() y pega el ID arriba, ' +
                  'o descomenta la linea de getDefaultCalendar() en _cal_().');
}

/** Imprime los calendarios de la cuenta con su ID, para copiar el que toque. */
function listarCalendarios() {
  const todos = CalendarApp.getAllCalendars();
  Logger.log('Calendarios visibles en esta cuenta (%s):', todos.length);
  for (const c of todos) {
    Logger.log('  %s%s  ->  %s',
               c.getName(),
               c.getId() === CalendarApp.getDefaultCalendar().getId() ? ' [por omision]' : '',
               c.getId());
  }
  Logger.log('');
  Logger.log('Copia el ID que corresponda y pegalo en CALENDAR_ID, arriba del todo.');
}

function carpetaMeet_() {
  for (const nombre of NOMBRES_CARPETA_MEET) {
    const it = DriveApp.getFoldersByName(nombre);
    if (it.hasNext()) return it.next();
  }
  return null;
}

/** Curso al que pertenece el archivo: primero por evento de calendario, luego por horario. */
function cursoDeArchivo_(file) {
  const creado = file.getDateCreated();
  return cursoPorEvento_(creado) || cursoPorNombre_(file.getName()) || cursoPorHorario_(creado);
}

/**
 * Busca un evento de calendario que se solape con la hora de la grabación y cuyo título
 * mencione el curso. Se amplía la ventana ±3 h porque el archivo se crea al TERMINAR
 * la reunión, no al empezar.
 */
function cursoPorEvento_(creado) {
  const ini = new Date(creado.getTime() - 3 * 60 * 60 * 1000);
  const fin = new Date(creado.getTime() + 1 * 60 * 60 * 1000);
  let eventos;
  try {
    eventos = _cal_().getEvents(ini, fin);
  } catch (e) {
    Logger.log('No pude leer el calendario: %s', e.message);
    return null;
  }
  for (const ev of eventos) {
    const curso = cursoPorNombre_(ev.getTitle());
    if (curso) return curso;
  }
  return null;
}

/** Curso cuyo nombre, código o alias aparece en el texto. */
function cursoPorNombre_(texto) {
  const t = normalizar_(texto);
  for (const c of CURSOS) {
    const candidatos = [c.nombre, c.codigo].concat(c.alias);
    for (const cand of candidatos) {
      if (t.indexOf(normalizar_(cand)) !== -1) return c;
    }
  }
  return null;
}

/** Último recurso: día de la semana + ventana horaria. */
function cursoPorHorario_(creado) {
  const dia = creado.getDay();
  const min = creado.getHours() * 60 + creado.getMinutes();
  const posibles = CURSOS.filter(c => c.dia === dia && min >= c.desde && min <= c.hasta);
  // Si dos cursos comparten día y ventana, no se adivina: mejor dejarlo quieto.
  return posibles.length === 1 ? posibles[0] : null;
}

/** Minúsculas, sin tildes y con espacios colapsados, para comparar sin sorpresas. */
function normalizar_(s) {
  return String(s || '')
    .toLowerCase()
    .normalize('NFD').replace(/[\u0300-\u036f]/g, '')
    .replace(/\s+/g, ' ')
    .trim();
}

// ─────────────────────────────────────────────────────────────── INSTALACIÓN

/** Crea el disparador: revisa cada 6 horas. Ejecutar UNA vez a mano. */
function instalarDisparador() {
  ScriptApp.getProjectTriggers()
    .filter(t => t.getHandlerFunction() === 'moverGrabaciones')
    .forEach(t => ScriptApp.deleteTrigger(t));

  ScriptApp.newTrigger('moverGrabaciones').timeBased().everyHours(6).create();
  Logger.log('Disparador instalado: moverGrabaciones cada 6 horas.');
}

/** Quita el disparador. */
function desinstalarDisparador() {
  ScriptApp.getProjectTriggers()
    .filter(t => t.getHandlerFunction() === 'moverGrabaciones')
    .forEach(t => ScriptApp.deleteTrigger(t));
  Logger.log('Disparador eliminado.');
}

/** Comprueba el calendario y que las carpetas destino existan y sean accesibles. */
function verificarCarpetas() {
  try {
    const c = _cal_();
    Logger.log('OK    calendario -> "%s"  [%s]', c.getName(), c.getId());
  } catch (e) {
    Logger.log('ERROR calendario -> %s', e.message);
    Logger.log('      Ejecuta listarCalendarios() para ver los IDs disponibles.');
  }
  for (const c of CURSOS) {
    try {
      const f = DriveApp.getFolderById(c.carpetaGrabadas);
      Logger.log('OK    %s -> "%s"', c.nombre, f.getName());
    } catch (e) {
      Logger.log('ERROR %s -> id %s no accesible: %s', c.nombre, c.carpetaGrabadas, e.message);
    }
  }
}
