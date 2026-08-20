# 01 — Alistar un curso: encuentros, Meet, correo e invitaciones

Procedimiento **general**: sirve para cualquier periodo y cualquier curso. Donde aparece
`<periodo>` va la etiqueta del semestre (`2026-2`, `2027-1`, …) y donde aparece `<Curso>` la
carpeta del curso. **Se repite igual para cada curso**; al final hay una lista de verificación.

**Todo lo de un curso está en la carpeta de ese curso**, en `Plan curso/<periodo>/`. Lo único
que se corre desde `config/` son los scripts que generan esos archivos.

---

## Orden y por qué

```
0. Regenerar y validar
1. Crear los encuentros en Calendar   → de aquí sale el enlace de Meet y se envían las invitaciones
2. Pegar el enlace de Meet y regenerar
3. Enviar el correo de bienvenida     → ya con el enlace adentro
4. Dejar el archivado de grabaciones  → manual 02
```

El paso 1 va **antes** del correo porque el enlace de Meet **lo crea Google, no el repo**:
hasta que no existe la serie de encuentros no hay enlace que publicar. Y como el script crea
los eventos con la API (no importando un archivo), **sí envía las invitaciones** — que es
justo lo que la importación de un `.ics` no hace.

---

## Paso 0 — Regenerar y validar

```bash
python config/calendario/generar_semestre_<periodo>.py         # calendario, correo, CSV
python config/calendario/generar_eventos_calendario.py         # nóminas, planillas, .ics
python config/calendario/generar_apps_script_encuentros.py     # el .gs de encuentros por curso
python config/calendario/validar_calendario.py                 # debe terminar en OK
```

Todo sale de `config/calendario/semestre_<periodo>.json`, la **fuente de verdad**: si una
fecha está mal se corrige ahí y se regenera, nunca a mano en los documentos — lo escrito a
mano se pierde en la siguiente corrida.

El segundo script imprime por curso cuántos estudiantes hay y cuántos son **invitables**.
**Lee esa línea:** si dice `invitables: 13` de 16, esas 3 personas no recibirán la invitación
(ver *Problemas frecuentes*).

### Lo que queda en la carpeta de cada curso

```
<Curso>/Plan curso/<periodo>/
├── CORREO_BIENVENIDA - <Curso> - <periodo>.md   ← paso 3
├── eventos_calendario_<periodo>.csv             ← alternativa manual (sin invitados)
├── CALENDARIO_<periodo>.md · Cronograma · PLAN_DE_CURSO
├── LISTA_DE_ALUMNOS_POR_GRUPOS*.xls             ← la nómina que descargas del sistema
└── _privado/                                    ← datos personales · fuera de git
    ├── CrearEncuentros - <Curso>.gs             ← paso 1
    ├── invitaciones_<curso>.ics                 ← alternativa manual
    ├── nomina_<curso>.csv                       ← correos para el paso 3
    ├── asistencia_<curso>.csv                   ← planilla de asistencia
    └── correos_manuales.csv                     ← si lo creas tú (ver más abajo)
```

---

## Paso 1 — Crear los encuentros en Calendar (una vez por curso)

Archivo: `<Curso>/Plan curso/<periodo>/_privado/CrearEncuentros - <Curso>.gs`

Es un **Google Apps Script**: corre en tu cuenta, no en el repo. Contiene los correos de los
estudiantes, por eso vive en `_privado/`.

### 1.1 Pegarlo en tu cuenta

1. **https://script.google.com** con tu cuenta institucional → **Nuevo proyecto**.
2. Nómbralo con el curso, p. ej. `UNIAJC - Encuentros <Curso>`.
3. Borra `Código.gs` y pega **todo** el `.gs` del curso. Guarda.

### 1.2 Activar el servicio avanzado de Calendar

**Servicios (+)** en el panel izquierdo → **Google Calendar API** → **Añadir**.

Sin esto los eventos se crean con invitados pero **sin Meet**: el enlace único de Meet se
crea con la API avanzada, no con `CalendarApp`.

### 1.3 Verificar (no toca nada)

Ejecuta **`verificar`** y abre **Ver → Registro de ejecución**.

La primera vez Google pide permisos y muestra *"Google no ha verificado esta aplicación"* —
es esperado, es tu propio script: **Configuración avanzada → Ir a (proyecto) → Permitir**.

Revisa en el log: que el **calendario** sea el tuyo, que el **servicio avanzado** diga
`activo`, el número de **invitados**, y la lista de sesiones (`se crearía` / `YA EXISTE`).

### 1.4 Crear de verdad

En el `.gs`, cambia:

```js
var SIMULAR = true;    // ponlo en false
```

Guarda y ejecuta **`crearEncuentros`**. Qué hace:

- Crea un evento por sesión, con los estudiantes como invitados y **enviándoles la
  invitación** (`SEND_INVITES = true`).
- Crea **una sola sala de Meet** y la deja en **todas** las sesiones sincrónicas, para que el
  estudiante entre siempre por el mismo enlace.
- Las sesiones **autónomas** también quedan en el calendario (para que vean la fecha de
  cierre) pero **sin Meet**, porque no hay encuentro.
- Al final imprime el **enlace de Meet**. Cópialo: es el del paso 2.

> Volver a ejecutarlo **no duplica**: reutiliza los eventos que ya existen y la sala ya
> creada (el `requestId` es determinista, así que Google no crea una segunda sala).

Si Google acepta la petición pero aún no devuelve el enlace, espera un minuto y ejecuta
`crearEncuentros` otra vez — el propio log lo dice.

---

## Paso 2 — Pegar el enlace de Meet y regenerar

En `config/calendario/semestre_<periodo>.json`:

```json
"cursos": { "<curso>": { "meet": "https://meet.google.com/xxx-xxxx-xxx" } }
```

Y regenera:

```bash
python config/calendario/generar_semestre_<periodo>.py
```

Ahora el correo de bienvenida **publica el enlace**. Si lo dejas vacío el correo no miente:
dice que el enlace llega dentro de la invitación de Calendar.

---

## Paso 3 — Enviar el correo de bienvenida

```
<Curso>/Plan curso/<periodo>/CORREO_BIENVENIDA - <Curso> - <periodo>.md
```

Se genera solo y ya trae: fechas clave con la **fecha de la primera clase** (que no siempre
coincide con el inicio del periodo), el **enlace de Meet**, el aviso de la invitación de
Calendar, la explicación de `[SINCRONICO]` / `[AUTONOMO]`, las carpetas de Drive, el bloque
de ExamLab y la petición al vocero.

**Antes de enviar completa lo único que el repo no puede saber:**

- [ ] La **contraseña temporal** de ExamLab (el correo deja el espacio en blanco).
- [ ] Que las carpetas de Drive estén **compartidas** con el grupo. El repo publica el
      enlace, no los permisos: si falta compartir, el estudiante ve "Solicitar acceso".

Destinatarios: columna `correo` de `_privado/nomina_<curso>.csv`. Ponlos en **CCO** para no
exponer los correos del grupo entre ellos.

---

## Paso 4 — Archivado de grabaciones

Una sola vez por cuenta, sirve para los 4 cursos y los periodos siguientes:
**[manual 02](02%20-%20Instalar%20y%20probar%20el%20Apps%20Script%20de%20grabaciones.md)**.

---

## Camino manual (sin Apps Script)

Si prefieres no usar Apps Script, puedes importar los archivos, con dos límites que conviene
saber de antemano:

| Archivo | Qué logra | Límite |
|---|---|---|
| `eventos_calendario_<periodo>.csv` | Los bloques en **tu** agenda | Sin invitados |
| `_privado/invitaciones_<curso>.ics` | Eventos **con** invitados | **Google no envía las invitaciones al importar**: hay que abrir y guardar cada evento para que pregunte *"¿Enviar correos de invitación?"* |

Y en ninguno de los dos casos hay enlace de Meet: el enlace lo crea Google, así que habría
que añadirlo a mano en cada evento. Por eso el camino recomendado es el paso 1.

Importar: Google Calendar → **⚙ Configuración → Importar y exportar → Importar**.

---

## Lista de verificación (por curso)

- [ ] Nómina descargada del sistema en `<Curso>/Plan curso/<periodo>/`
- [ ] Los 4 scripts del paso 0 corridos · validador en `OK`
- [ ] `invitables` = total de estudiantes (si no, ver *Problemas frecuentes*)
- [ ] `verificar` revisado en el Apps Script del curso
- [ ] `crearEncuentros` ejecutado con `SIMULAR = false` → invitaciones enviadas
- [ ] Enlace de Meet pegado en el JSON y material regenerado
- [ ] Carpetas de Drive (**Clases** y **Clases grabadas**) compartidas con el grupo
- [ ] Contraseña temporal de ExamLab escrita en el correo
- [ ] Correo de bienvenida enviado en CCO
- [ ] Archivado de grabaciones instalado (manual 02) · `simulacro` revisado

---

## Cuando algo cambia

| Cambió | Qué hacer |
|---|---|
| Una fecha, un parcial, un festivo | Editar el JSON, correr los scripts del paso 0, volver a pegar el `.gs` del curso y ejecutar `crearEncuentros` (reutiliza lo que ya existe; los cambios de hora sí hay que ajustarlos en Calendar o borrar y recrear con `eliminarEncuentros`). |
| Llegó una nómina nueva | Reemplazar el `.xls`, correr los scripts del paso 0 y volver a pegar el `.gs`: los invitados nuevos entran al ejecutar `crearEncuentros`. |
| Cambió una carpeta de Drive | Actualizar `carpetas_drive` en el JSON; si es la de grabaciones, actualizar también el script del manual 02. El validador avisa si divergen. |
| Arranca un periodo nuevo | Crear `Plan curso/<periodo nuevo>/`; el anterior se queda donde está, no se borra. |

---

## Problemas frecuentes

**«invitables: 13» de 16 estudiantes.**
El export académico no trae correo institucional para algunos. Dos salidas: pedirlos a
Registro Académico (el script deja `_privado/pendientes_correo_<curso>.csv` con nombre y
documento), o crear `<Curso>/Plan curso/<periodo>/_privado/correos_manuales.csv` con
encabezado `documento,correo,nota` — se cruza por documento y esos correos quedan marcados
como `personal (manual)` en la nómina. Cuando lleguen los institucionales, actualiza el
`.xls` y borra ese archivo.

**«Servicio avanzado: NO ACTIVO».** Falta el paso 1.2. Los eventos se crearían sin Meet.

**Los eventos quedaron sin enlace de Meet.** O falta el servicio avanzado, o Google todavía
no había devuelto el enlace: vuelve a ejecutar `crearEncuentros`, no duplica nada.

**Creé dos salas de Meet distintas.** Pasa si borraste la sala guardada (`olvidarSalaMeet`) o
si pegaste el `.gs` en dos proyectos distintos. Deja una, pégala en `MEET_URL` del `.gs` y
ejecuta `crearEncuentros`: aplicará esa a toda la serie.

**Un estudiante dice que el link de Drive le pide acceso.** La carpeta no está compartida.

**Importé el `.ics` y nadie recibió nada.** Es lo esperado: ver *Camino manual*.

**El script dice «es de otro periodo -> omitido».** Correcto: ignora una nómina que cuelga de
la carpeta de un periodo anterior.

**El validador falla.** Arréglalo antes de crear eventos o enviar correos: todo esto es de
cara al estudiante, y corregir aquí es más barato que retirar invitaciones ya enviadas.
