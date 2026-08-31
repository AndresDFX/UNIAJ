# 01 — Alistar un curso: encuentros, Meet y correo de bienvenida

> **Los encuentros ya no invitan a nadie.** Son **bloques de tu calendario personal**: sin
> lista de invitados, sin correos de invitación y sin correos de cancelación al borrar. Cada
> sesión sigue teniendo **su propia sala de Meet**, y **el enlace lo publicas tú** por el canal
> del curso (ExamLab). El archivo conserva su nombre viejo —con «invitaciones»— porque los
> `LEEME` generados apuntan a él por ruta exacta.

Procedimiento **general**: sirve para cualquier periodo y cualquier curso. Donde aparece
`<periodo>` va la etiqueta del semestre (`2026-2`, `2027-1`, …) y donde aparece `<Curso>` la
carpeta del curso. **Se repite igual para cada curso**; al final hay una lista de verificación.

**Todo lo de un curso está en la carpeta de ese curso**, en `Plan curso/<periodo>/`. Lo único
que se corre desde `config/` son los scripts que generan esos archivos.

---

## Orden y por qué

```
0. Regenerar y validar
1. Enviar el correo de bienvenida     → dice el horario y por dónde publicas el enlace
2. Crear los encuentros en Calendar   → tus bloques, cada uno con SU sala de Meet
3. Dejar el archivado de grabaciones  → manual 02
```

**Cada sesión tiene su propio enlace de Meet**, así que no hay un enlace único del curso que
copiar al correo. El estudiante **no recibe invitación de Calendar**: el enlace de la sesión lo
publicas tú antes de cada encuentro (el correo de bienvenida dice que va por **ExamLab**). Por
eso el correo va **primero** — deja claro el horario y dónde buscar el enlace del día.

El paso 2 crea los eventos con la API de Calendar, no importando un archivo, y por eso **cada
sesión tiene su propia sala de Meet** — que es justo lo que la importación de un `.ics` no da.
Después del paso 2, el log te lista sesión por sesión con su enlace: **de ahí sale lo que
publicas**.

---

## Paso 0 — Regenerar y validar

```bash
python config/calendario/generar_semestre_<periodo>.py         # calendario, correo, CSV
python config/calendario/generar_eventos_calendario.py         # nóminas, planillas, .ics
python config/calendario/generar_apps_script_encuentros.py     # los .gs de encuentros
python config/calendario/validar_calendario.py                 # debe terminar en OK
```

Todo sale de `config/calendario/semestre_<periodo>.json`, la **fuente de verdad**: si una
fecha está mal se corrige ahí y se regenera, nunca a mano en los documentos — lo escrito a
mano se pierde en la siguiente corrida.

El tercer script emite **dos cosas**: un `.gs` por curso y **uno consolidado con todos los
cursos del periodo**. Los dos salen de la misma plantilla, así que hacen lo mismo; eliges uno
de los dos caminos (ver *Un proyecto o uno por curso*, más abajo).

El segundo script imprime por curso cuántos estudiantes hay y cuántos traen **correo
institucional**. Eso ya **no** afecta a los encuentros (los eventos no tienen invitados): es
para la **planilla de asistencia** y para saber a quién le puedes escribir el correo de
bienvenida. Si dice `estudiantes: 16 · con correo: 13`, a esas 3 personas no hay por dónde
escribirles (ver *Problemas frecuentes*). Un curso **sin listado** igual queda con su CSV, su
`.ics` y su `.gs`; lo único que le falta es la planilla.

### Lo que queda en la carpeta de cada curso

```
<Curso>/Plan curso/<periodo>/
├── LEEME - Apps Script del curso.md             ← dice dónde está el .gs (visible)
├── CORREO_BIENVENIDA - <Curso> - <periodo>.md   ← paso 1
├── eventos_calendario_<periodo>.csv             ← alternativa manual (camino manual)
├── CALENDARIO_<periodo>.md · Cronograma · PLAN_DE_CURSO
├── LISTA_DE_ALUMNOS_POR_GRUPOS*.xls             ← la nómina que descargas del sistema
└── _privado/                                    ← fuera de git (aquí vive la nómina)
    ├── CrearEncuentros - <Curso>.gs             ← paso 2
    ├── bloques_<curso>.ics                      ← alternativa manual (sin invitados)
    ├── nomina_<curso>.csv                       ← correos para el paso 1 (CCO)
    ├── asistencia_<curso>.csv                   ← planilla de asistencia
    └── correos_manuales.csv                     ← si lo creas tú (ver más abajo)
```

> **Cuando varios grupos comparten la carpeta del curso** (en `2026-2`, los tres grupos de
> `FI300101`), el grupo va **en el nombre** de cada archivo: `CALENDARIO_<periodo> - SB141B.md`,
> `eventos_calendario_<periodo> - SB141B.csv`, `CrearEncuentros - <Curso> - SB141B.gs`,
> `LEEME - Apps Script del curso - SB141B.md`. Si no, el tercer grupo pisaría a los otros dos.

Y, una sola vez para todo el periodo, en la raíz de `Cursos`:

```
LEEME - Apps Script del semestre.md              ← visible: dice qué trae y dónde está
_privado/<periodo>/
└── CrearEncuentros - TODO EL SEMESTRE <periodo>.gs   ← el consolidado
```

---

## Paso 1 — Enviar el correo de bienvenida

Archivo:

```
<Curso>/Plan curso/<periodo>/CORREO_BIENVENIDA - <Curso> - <periodo>.md
```

Se genera solo y ya trae: fechas clave con la **fecha de la primera clase** (que no siempre
coincide con el inicio del periodo), el aviso de que **no va a llegar ninguna invitación de
Google Calendar** y de que el **enlace de Meet lo publicas tú en ExamLab antes de cada
sesión**, qué sesiones son sincrónicas y cuáles autónomas, las carpetas de Drive, el bloque de
ExamLab —con la verificación de acceso y la **encuesta de inicio de semestre**, las dos cosas
que el estudiante tiene que hacer **antes de la primera clase**— y la petición al vocero.

**Antes de enviar completa lo único que el repo no puede saber:**

- [ ] La **contraseña temporal** de ExamLab (el correo deja el espacio en blanco).
- [ ] Que las carpetas de Drive estén **compartidas** con el grupo. El repo publica el
      enlace, no los permisos: si falta compartir, el estudiante ve "Solicitar acceso".

Destinatarios: columna `correo` de `_privado/nomina_<curso>.csv`. Ponlos en **CCO** para no
exponer los correos del grupo entre ellos.

El correo **no publica ningún enlace de Meet**, y por dos razones: no existe uno solo del curso
—publicar uno fijo mandaría al grupo a la sala equivocada en las demás sesiones— y las salas
**todavía no existen** cuando se envía el correo: las crea el paso 2.

> **Compromiso que este correo te deja:** dice que el enlace de cada sesión aparece en ExamLab.
> Nadie lo publica por ti. Después del paso 2, saca los enlaces del log (`verificar` los imprime
> sesión por sesión, cuando ya existen) y déjalos en el curso de ExamLab.

---

## Un proyecto o uno por curso

Hay dos caminos para el paso 2, y **son equivalentes**: los `.gs` salen de la misma plantilla.

| Camino | Archivo | Cuándo conviene |
|---|---|---|
| **Un proyecto por curso** | `<Curso>/Plan curso/<periodo>/_privado/CrearEncuentros - <Curso>.gs` | Cuando alistas los cursos de a uno, en semanas distintas. El desplegable de Apps Script solo muestra las 4 funciones de ese curso, así que no hay dónde equivocarse. |
| **Un proyecto para todo** | `_privado/<periodo>/CrearEncuentros - TODO EL SEMESTRE <periodo>.gs` | Cuando alistas el semestre completo de una sentada, o cuando hay que rehacer varios cursos. Un solo `CALENDAR_ID` que pegar, un solo permiso que aceptar. |

En el consolidado las funciones llevan el nombre del curso —y el **grupo**, cuando varios
comparten código— y además hay cuatro que abarcan todo el periodo. En `2026-2` son **7 cursos**:

| Función | Alcance |
|---|---|
| `verificarProgramacionII` · `crearProgramacionII` · `eliminarProgramacionII` · `recrearProgramacionII` | solo ese curso |
| `verificarSeminario` · `crearSeminario` · `eliminarSeminario` · `recrearSeminario` | solo ese curso |
| `verificarBasesDatosII` · `crearBasesDatosII` · `eliminarBasesDatosII` · `recrearBasesDatosII` | solo ese curso |
| `verificarArquitectura` · `crearArquitectura` · `eliminarArquitectura` · `recrearArquitectura` | solo ese curso |
| `verificarIntroduccionIngenieriaSB141B` · `crear…` · `eliminar…` · `recrear…` | solo ese **grupo** |
| `verificarIntroduccionIngenieriaSB141C` · `crear…` · `eliminar…` · `recrear…` | solo ese **grupo** |
| `verificarIntroduccionIngenieriaLB141F` · `crear…` · `eliminar…` · `recrear…` | solo ese **grupo** |
| `verificarTodosLosCursos` | **los 7** · solo lectura |
| `crearTodosLosCursos` | **los 7** · crea lo que falte y le asegura su sala a cada sesión |
| `eliminarTodosLosCursos` | **los 7** · borra todo |
| `recrearTodosLosCursos` | **los 7** · borra y vuelve a crear |

Las cuatro `*TodosLosCursos` piden **un segundo interruptor** además de `SIMULAR = false`:

```js
var CONFIRMO_SEMESTRE_COMPLETO = false;   // ponlo en true para las funciones de todo el periodo
```

Ya no es por los correos —no se manda ninguno—: existe porque esas cuatro tocan **102 eventos y
96 salas de Meet** de golpe (roza la cuota diaria de Calendar y tarda), y en el desplegable de
Apps Script es fácil elegir `crearTodosLosCursos` cuando querías `crearSeminario`. Si está en
`false`, la función se detiene y te dice qué hacer, sin haber tocado nada. Las funciones de un
curso suelto no lo necesitan.

> **Ojo con los cursos que caen el mismo día:** Bases de Datos II y Arquitectura son los dos
> **lunes**, y los grupos `SB141C` y `LB141F` de Introducción a la Ingeniería son los dos
> **martes** con el mismo código. Cualquier cosa que hagas «para todos los cursos» los toca a
> todos: si solo querías uno, usa su función. Lo que ya **no** pasa es que a un estudiante
> matriculado en dos de tus cursos le llegue nada por duplicado — los eventos no invitan a
> nadie.

El resto del paso 2 es idéntico en los dos caminos: solo cambian los nombres de las funciones.
Donde el manual dice `verificar`, `crearEncuentros`, `eliminarEncuentros` o `recrearTodo`, en
el consolidado usa la del curso (`verificarSeminario`, `crearSeminario`, …) o la de todo el
periodo.

---

## Paso 2 — Crear los encuentros en Calendar

Archivo, según el camino que elegiste arriba:

```
<Curso>/Plan curso/<periodo>/_privado/CrearEncuentros - <Curso>.gs          ← un curso
_privado/<periodo>/CrearEncuentros - TODO EL SEMESTRE <periodo>.gs          ← todos
```

Es un **Google Apps Script**: corre en tu cuenta, no en el repo.

> **Si no lo encuentras:** vive en `_privado/`, que está en `.gitignore` — **existe en tu disco
> y en Drive, pero no en GitHub**. (Ya no lleva ningún dato de estudiante; sigue ahí por
> convención, junto a la nómina.) Al lado, ya visibles,
> quedan los punteros con la ruta exacta: `LEEME - Apps Script del curso.md` en la carpeta del
> curso, y `LEEME - Apps Script del semestre.md` en la raíz de `Cursos`. Si de verdad falta el
> archivo, lo regenera `python config/calendario/generar_apps_script_encuentros.py`, que
> además imprime la ruta absoluta de cada uno.

### 2.1 Pegarlo en tu cuenta

1. **https://script.google.com** con tu cuenta institucional → **Nuevo proyecto**.
2. Nómbralo con el curso, p. ej. `UNIAJC - Encuentros <Curso>` (o `UNIAJC - Encuentros
   <periodo>` si usas el consolidado).
3. Borra `Código.gs` y pega **todo** el `.gs`. Guarda.
4. **⚙ Configuración del proyecto → Zona horaria → `America/Bogota`.**

> **El paso 4 no es cosmético.** Las horas de los eventos las construye Apps Script con la
> zona **del proyecto**, no con la del calendario ni la del curso. Google no siempre pone la
> local: si el proyecto queda en UTC o en `America/New_York`, todas las sesiones entran corridas
> una o cinco horas —y con ellas **las salas de Meet que ya publicaste**—, y reejecutar no lo
> arregla porque el evento existe y se reutiliza. Peor con Nueva York: allí hay horario de verano y en Bogotá no,
> así que el desfase cambia a mitad de semestre y la serie queda inconsistente consigo misma.
>
> El script se defiende: `verificar` imprime la zona y, si no es `America/Bogota`, **crear y
> borrar quedan bloqueados** hasta que la corrijas.

### 2.2 Activar el servicio avanzado de Calendar

**Servicios (+)** en el panel izquierdo → **Google Calendar API** → **Añadir**.

Sin esto los eventos se crean, pero **sin Meet**: las salas se crean con la API avanzada, no
con `CalendarApp`. Y la sala es justo lo que este camino aporta.

### 2.3 Pegar el ID del calendario

En el `.gs`, arriba del todo, hay una constante que **sale vacía a propósito**:

```js
var CALENDAR_ID = '';   // <- pega aquí el ID del calendario
```

Se pide explícito y no se usa el calendario "por omisión" porque ese depende de la cuenta con
la que se abrió Apps Script: si un día se ejecuta con otra sesión, escribiría los eventos en
otro calendario sin avisar — y con ~100 eventos y sus salas ya creados eso no se deshace fácil.

**Cómo obtener el ID, dos caminos:**

1. **Desde el propio script (más rápido):** ejecuta la función **`listarCalendarios`**. El
   registro imprime cada calendario de la cuenta con su ID y marca cuál es el por omisión:

   ```
   Calendarios visibles en esta cuenta (3):
     Julian Castaño [por omision]  ->  julianacastano@profesores.uniajc.edu.co
     Clases UNIAJC                 ->  c_a1b2c3...@group.calendar.google.com
   ```

2. **Desde Google Calendar:** en «Mis calendarios», pasa el mouse sobre el calendario → **⋮**
   → **Configuración y uso compartido** → baja hasta **«Integrar calendario»** → copia
   **«ID de calendario»**.

El del calendario principal es tu propio correo; uno secundario se ve como
`…@group.calendar.google.com`.

Pega el valor entre las comillas y guarda:

```js
var CALENDAR_ID = 'c_a1b2c3...@group.calendar.google.com';
```

> **Usa el MISMO ID en el script de grabaciones** (manual 02). Si los dos miran calendarios
> distintos, el de grabaciones no encontrará los encuentros y dejará todo sin clasificar.

Si de verdad prefieres el calendario por omisión, la línea está en el script comentada dentro
de `_cal_()` (y de `_calId_()`): descoméntala y deja `CALENDAR_ID` vacío.

### 2.4 Verificar (no toca nada)

Ejecuta **`verificar`** y abre **Ver → Registro de ejecución**. Entre otras cosas confirma el **calendario** y el `CALENDAR_ID` que quedó configurado.

La primera vez Google pide permisos y muestra *"Google no ha verificado esta aplicación"* —
es esperado, es tu propio script: **Configuración avanzada → Ir a (proyecto) → Permitir**.

Revisa en el log: que el **calendario** sea el tuyo, que la **zona del proyecto** diga
`America/Bogota (correcta)`, que el **servicio avanzado** diga `activo`, que el tipo diga
`bloque de TU calendario (sin invitados, sin correos)`, el **rango del curso**, y la lista de
sesiones (`se crearía` / `YA EXISTE`). De las que ya existen imprime **su enlace de Meet**: esta
es la función a la que vuelves cuando toca publicar los enlaces.

### 2.5 Crear de verdad

En el `.gs`, cambia:

```js
var SIMULAR = true;    // ponlo en false
```

Guarda y ejecuta **`crearEncuentros`**. Qué hace:

- Crea un evento por sesión **en tu calendario**: sin lista de invitados y **sin enviar ningún
  correo**. Son tus bloques de agenda.
- Le da a **cada sesión sincrónica su propia sala de Meet**: 13 sesiones = 13 enlaces
  distintos. El log los imprime uno por línea, junto a su fecha, y el enlace queda además en
  **Ubicación** y al final de la **descripción** del evento. **De ahí lo copias para publicarlo**
  (paso 1: el correo dice que va en ExamLab).
- Las sesiones **autónomas** también quedan en el calendario (para que vean la fecha de
  cierre) pero **sin Meet**, porque no hay encuentro.
- Si en un hueco ya hay un encuentro del curso **con otro título**, no crea nada ahí y lo dice
  (`OMITIDO(S) por título cambiado`). Pasa cuando el título cambió en el JSON —se marcó un
  parcial, una sesión pasó a autónoma— y evita dejar dos eventos y dos salas el mismo día. La
  salida es `recrear…`, que borra el viejo y crea el nuevo.

**No hay nada que copiar al material del curso**, porque no existe un enlace único: el de cada
sesión vive en su evento. Lo que sí hay que hacer, cada semana o de una vez al arrancar, es
**publicar el enlace de la sesión** en ExamLab; nadie lo hace por ti.

> Volver a ejecutarlo **no duplica**: reutiliza los eventos que ya existen, y si una sesión ya
> tiene sala la respeta. Cada sesión pide la suya con un `requestId` propio y estable
> (`…-s01`, `…-s02`, …), así que Google no crea una segunda sala para la misma sesión.

Si Google acepta la petición pero aún no devuelve el enlace, espera un minuto y ejecuta
`crearEncuentros` otra vez — el propio log lo dice.

**Si se corta a la mitad.** Apps Script mata cualquier ejecución a los 30 minutos (6 en
cuentas gratuitas). El script se corta **solo** antes de eso —la constante `MINUTOS_MAX`— y en
el log te dice **qué función ejecutar para continuar**. No se pierde nada.

Hazle caso al nombre que te dé, porque no siempre es la que se cortó: si lo que se cortó fue
una `recrear…`, hay que continuar con la `crear…` correspondiente. Reejecutar la `recrear…`
volvería a **borrar** lo que acababa de recrear, y con cada evento se va la sala de Meet que
acababa de crear (los enlaces que ya publicaste dejan de servir). El log lo advierte en
mayúsculas.

### 2.6 Borrar todo y volver a crear

Solo cuando de verdad haga falta partir de cero (se movieron las fechas, o quieres rehacer la
serie completa):

| Función | Qué hace |
|---|---|
| `eliminarEncuentros` | Borra los eventos de la serie. **Tres pasadas**, ver abajo. |
| `recrearTodo` | Borra y vuelve a crear en una sola corrida. |

Las tres pasadas del borrado, y qué caza cada una:

| Pasada | Qué encuentra | Cómo se llama en el log |
|---|---|---|
| Título exacto | Los eventos tal como se llaman **ahora** | `Por titulo exacto` |
| Misma fecha **y hora** de cada sesión | Eventos de una corrida anterior cuyo **título** ya no coincide (cambiaron los prefijos, la modalidad, se marcó un parcial) | `Huerfanos del curso` |
| El **rango de ese curso**, a la hora del curso | Eventos en **fechas que ya no están** en el calendario del curso: una sesión que se movió o se quitó del JSON | `Fantasmas` |

Las tres exigen que el título mencione el curso **y** que la hora sea la del curso, así que no
se llevan tus eventos personales que nombren la asignatura a otra hora, ni los del otro curso
que caiga el mismo día (Bases de Datos II y Arquitectura son los dos lunes; `SB141C` y `LB141F`,
los dos martes, se distinguen además por la hora).

> **La tercera pasada barre el rango del curso, no el del periodo.** Cada curso lleva su propio
> `inicio`/`fin` en el `.gs` (`Rango del curso` en el log de `verificar`). Importa porque en
> `2026-2` los grupos de Introducción a la Ingeniería llegan hasta **diciembre**: si el barrido
> usara el rango global, `eliminarBasesDatosII` se metería en diciembre —donde Bases de Datos II
> ya no tiene clases— y se llevaría **tus** apuntes personales que mencionen la asignatura a esa
> hora. Hay una prueba que lo verifica (sección final).

Con `SIMULAR = true` las tres se **listan una por una** antes de borrar nada. Léelas: es la
única oportunidad de ver qué se va.

En el consolidado, lo mismo por curso (`eliminarSeminario` / `recrearSeminario`) o para todo
el periodo (`eliminarTodosLosCursos` / `recrearTodosLosCursos`, con el segundo interruptor).

Con `SIMULAR = true` las dos **solo listan** lo que harían — incluidos los "huérfanos" que
encontró. Corre así primero, siempre.

> **Borrar no notifica a nadie** —los eventos no tienen invitados—, pero **cada evento nuevo trae
> una sala de Meet nueva**: los enlaces cambian. Si ya los habías publicado en ExamLab, hay que
> **volver a publicarlos**, o el grupo entra a una sala que ya no existe.
>
> **Si lo único que cambió es la nómina, no borres nada:** la nómina ya no entra en los eventos.
> Solo afecta a la planilla de asistencia, que la regenera `generar_eventos_calendario.py` (ver
> *Cuando algo cambia*).

---

## Paso 3 — Archivado de grabaciones

Una sola vez por cuenta, sirve para todos los cursos y los periodos siguientes:
**[manual 02](02%20-%20Instalar%20y%20probar%20el%20Apps%20Script%20de%20grabaciones.md)**.

---

## Camino manual (sin Apps Script)

Si prefieres no usar Apps Script, puedes importar los archivos. Los dos dejan **los mismos
bloques en tu agenda**, sin invitados:

| Archivo | Qué logra | Límite |
|---|---|---|
| `eventos_calendario_<periodo>.csv` | Los bloques en **tu** agenda | Formato CSV de Google: título, fecha, hora y descripción, nada más |
| `_privado/bloques_<curso>.ics` | Lo mismo, en formato de calendario (`METHOD:PUBLISH`) | Reimportar **actualiza** los eventos en vez de duplicarlos, porque los `UID` son estables |

Y en ninguno de los dos casos hay enlace de Meet: la sala la crea Google, así que habría que
añadir una a mano en cada evento. Por eso el camino recomendado es el paso 2 — es el único que
le da a **cada sesión su propia sala**.

Importar: Google Calendar → **⚙ Configuración → Importar y exportar → Importar**.

---

## Lista de verificación (por curso)

- [ ] Nómina descargada del sistema en `<Curso>/Plan curso/<periodo>/` (con el **grupo** en el
      nombre si varios grupos comparten el código)
- [ ] Los 4 scripts del paso 0 corridos · validador en `OK`
- [ ] `con correo` = total de estudiantes (si no, ver *Problemas frecuentes*)
- [ ] **Zona horaria del proyecto** de Apps Script en `America/Bogota` (paso 2.1)
- [ ] `CALENDAR_ID` pegado en el `.gs` (el mismo del manual 02)
- [ ] `verificar` revisado: zona `correcta`, servicio avanzado `activo`, rango del curso
- [ ] Carpetas de Drive (**Clases** y **Clases grabadas**) compartidas con el grupo
- [ ] Contraseña temporal de ExamLab escrita en el correo
- [ ] Encuesta de inicio de semestre publicada en el correo (la trae el bloque de
      ExamLab; sale de `semestre_<periodo>.json → encuesta_inicio_semestre`)
- [ ] Correo de bienvenida enviado en CCO
- [ ] `crearEncuentros` ejecutado con `SIMULAR = false`
- [ ] En el log, cada sesión sincrónica con su enlace de Meet
- [ ] **Enlaces de Meet publicados en ExamLab** (es lo que el correo prometió, y el estudiante
      no tiene otra forma de entrar)
- [ ] Archivado de grabaciones instalado (manual 02) · `simulacro` revisado

---

## Cuando algo cambia

| Cambió | Qué hacer |
|---|---|
| Un parcial, una sesión que pasa a autónoma | Cambia el **título** del evento. `crearEncuentros` lo detecta, **no** crea un duplicado y lo dice (`OMITIDO por título cambiado`). Para aplicarlo: `recrearTodo` (o `recrear<Curso>`), que borra el viejo y crea el nuevo. |
| Una fecha o una hora | Editar el JSON, correr el paso 0, volver a pegar el `.gs` y ejecutar `recrearTodo`. El evento viejo queda en una fecha que ya no está en el calendario del curso: lo caza la tercera pasada del borrado (`Fantasmas`, paso 2.6). Con `crearEncuentros` sola te quedarían los dos. Recuerda **volver a publicar** los enlaces: al recrear cambian. |
| Un festivo nuevo | Igual que una fecha: el título pasa a `[AUTONOMO]` y la sesión deja de llevar Meet. `recrearTodo`. |
| Llegó una nómina nueva | Reemplazar el `.xls` y correr `generar_eventos_calendario.py`. **No toca los encuentros**: los eventos no tienen invitados, así que no hay nada que sincronizar en Calendar. Lo que se regenera es la **nómina** y la **planilla de asistencia**. No hace falta volver a pegar el `.gs` ni ejecutar nada en Apps Script. |
| La nómina que dejaste es de otra asignatura | `generar_eventos_calendario.py` lo detecta por el código `FI######` y la **omite**: el curso se queda sin planilla (lo dice en consola), pero el CSV, el `.ics` y el `.gs` se generan igual. Consigue el export correcto y vuelve a correr el paso 0. |
| El listado no dice de qué grupo es, y varios grupos comparten el código | Se **rechaza a propósito** (`no dice <GRUPO> y este codigo lo usan varios grupos`): no hay forma de saber a quién pertenece, y una planilla cruzada es peor que ninguna. Renombra el archivo con el grupo al principio, p. ej. `SB141B - INTRODUCCION A LA INGENIERIA.xls`. |
| Cambió una carpeta de Drive | Actualizar `carpetas_drive` en el JSON; si es la de grabaciones, actualizar también el script del manual 02. El validador avisa si divergen. |
| Arranca un periodo nuevo | Crear `Plan curso/<periodo nuevo>/`; el anterior se queda donde está, no se borra. |

---

## Problemas frecuentes

**«estudiantes: 16 · con correo: 13».**
El export académico no trae correo institucional para algunos. No afecta a los encuentros, pero
sí al correo de bienvenida: a esas personas no hay por dónde escribirles. Dos salidas: pedirlos a
Registro Académico (el script deja `_privado/pendientes_correo_<curso>.csv` con nombre y
documento), o crear `<Curso>/Plan curso/<periodo>/_privado/correos_manuales.csv` con
encabezado `documento,correo,nota` — se cruza por documento y esos correos quedan marcados
como `personal (manual)` en la nómina. Cuando lleguen los institucionales, actualiza el
`.xls` y borra ese archivo.

**«Servicio avanzado: NO ACTIVO».** Falta el paso 2.2. Los eventos se crearían sin Meet.

**Los eventos quedaron sin enlace de Meet.** O falta el servicio avanzado, o Google todavía
no había devuelto el enlace: vuelve a ejecutar `crearEncuentros`, no duplica nada.

**Cada sesión tiene un enlace de Meet distinto.** Es a propósito: una sala por encuentro. Por eso
lo que se publica es **el de la sesión que toca**, no un enlace del curso.

**Un estudiante pregunta cuál es «el link de la clase».** No hay uno solo, y **el estudiante no
ve tus eventos**: los encuentros son bloques de tu calendario, sin invitados. Publica el enlace
de esa sesión en ExamLab (lo saca del log de `verificar`, o de la Ubicación del evento).

**«No me llegó ninguna invitación de Calendar».** Es lo esperado, y el correo de bienvenida ya lo
dice: no se envían invitaciones. El horario está en el correo y el enlace de cada sesión se
publica en ExamLab.

**«BLOQUEADO: crearTodosLosCursos toca los 7 cursos a la vez».** Es la rejilla de seguridad,
no un error. O pones `CONFIRMO_SEMESTRE_COMPLETO = true`, o usas la función del curso que
querías.

**Se creó todo dos veces.** No debería: el script busca el evento por título exacto dentro del
día antes de crearlo. Si pasó, es que los títulos cambiaron entre las dos corridas (se editó
el JSON en medio). Borra los sobrantes a mano o usa `recrear…`, que parte de cero.

**Un estudiante dice que el link de Drive le pide acceso.** La carpeta no está compartida.

**Importé el `.ics` y nadie recibió nada.** Es lo esperado: `bloques_<curso>.ics` no tiene
invitados (`METHOD:PUBLISH`), solo deja los bloques en tu agenda. Ver *Camino manual*.

**El script dice «es de otro periodo -> omitido».** Correcto: ignora una nómina que cuelga de
la carpeta de un periodo anterior.

**El validador falla.** Arréglalo antes de crear eventos o enviar el correo: todo esto es de
cara al estudiante, y corregir aquí es más barato que corregir un horario ya publicado.

---

## Si toca cambiar el generador

Los `.gs` no se editan a mano: se regeneran. Y el generador tiene pruebas que ejecutan el
`.gs` de verdad contra un simulacro de las APIs de Google:

```bash
bash config/calendario/pruebas_apps_script/probar.sh
```

Comprueban lo que este manual promete —que reejecutar no duplica, que hay una sala por sesión,
que el borrado no se lleva nada ajeno **ni se sale del rango del curso**, que ningún evento
lleva invitados ni manda correos, que los interruptores frenan—. Córrelas después de
cualquier cambio en `generar_apps_script_encuentros.py`, **antes** de pegar el `.gs` en Apps
Script. Detalle: `config/calendario/pruebas_apps_script/LEEME.md`.
