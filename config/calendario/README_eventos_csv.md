# Calendario de eventos CSV 2026-2

Archivos `eventos_*_2026-1.csv` / `eventos_*_2026-2.csv` (copia en `config/calendario/`) y
`<Curso>/Plan curso/2026-2/calendario_eventos_2026-2.csv`: **13 filas (una por sesión) por curso**,
UTF-8 con BOM, 14 columnas. La columna de notas NO lleva nómina de estudiantes (información privada).

> **Semestre acortado 2026-2:** inicio **24/08/2026** (la fecha fin **22/11/2026** no se movió) =
> **13 sesiones** por curso. Se conservan los **15 temas** del microcurrículo porque **2 sesiones
> son dobles**. Las carpetas de material (`Clases/Clase N - …`, `Kit docente/Clase N/`) **no se
> renumeraron**: la columna `sesion_etiqueta` dice qué "Clase N" de material se dicta en cada sesión.

Una fila = una sesión; `es_parcial=si` marca parciales síncronos;
`tipo_clase` = `presencial` | `virtual` | `autonoma` | `sustentacion`.

## Eventos de calendario a partir de la nómina real

```bash
python config/calendario/generar_eventos_calendario.py
```

Lee `semestre_2026_2.json` + el **listado real de estudiantes** de cada curso (lo detecta solo;
acepta el export Academusoft `LISTA_DE_ALUMNOS_POR_GRUPOS*.xls` y el formato
`<grupo> - <MATERIA>.xls[x]`, y valida que el código `FI######` del archivo coincida con el del
curso para no cruzar nóminas). Requiere `xlrd` y `openpyxl`.

Produce dos clases de salida, deliberadamente separadas:

| Salida | Contiene nómina | Ruta | Para qué |
|---|---|---|---|
| `eventos_calendario_2026-2.csv` | **No** | `<Curso>/Plan curso/2026-2/` | Importación directa a Google Calendar (13 eventos) |
| `invitaciones_<curso>.ics` | **Sí** | `config/calendario/_privado_2026-2/` | 13 eventos con los estudiantes como `ATTENDEE` → invitaciones reales |
| `nomina_<curso>.csv` | **Sí** | idem | Nómina normalizada (documento, nombre, correo, repitente) |
| `asistencia_<curso>.csv` | **Sí** | idem | Planilla estudiantes × 13 sesiones (el 10% de asistencia de cada corte) |
| `pendientes_correo_<curso>.csv` | **Sí** | idem (solo si aplica) | Estudiantes sin correo institucional, para pedirlo a Registro Académico |

> `config/calendario/_privado_2026-2/` está en `.gitignore`: son datos personales de estudiantes
> (nombre, documento, correo) y **no se versionan ni se comparten**. El CSV de eventos que sí se
> versiona no lleva nómina. El script tampoco imprime nombres ni correos en consola, solo conteos.

Cómo usarlo: importa el `.csv` si solo quieres los bloques en tu calendario; importa el `.ics` si
además quieres **invitar** a los estudiantes (el cliente de calendario pedirá confirmar el envío).
Las sesiones autónomas van como `TRANSP:TRANSPARENT` porque no hay encuentro sincrónico.

Si cambia el calendario o llega un listado actualizado: vuelve a correr el script; es idempotente.

Todo se regenera con `python config/calendario/generar_semestre_2026_2.py`, que **lee**
`config/calendario/semestre_2026_2.json` (fuente de verdad; el script ya no lo reescribe).

## Modalidad y parciales por curso (fuente: `semestre_2026_2.json`)

| Curso | Oferta | Por sesión |
|---|---|---|
| **Programación II** (mié 18:00–20:00) | Presencialidad asistida | Sesión 1 + parciales **5/9/13** presencial; resto virtual; sin festivos; sesiones dobles **8 y 10** |
| **Seminario** (jue 18:00–20:00) | Presencialidad asistida | Sesión 1 + parciales **5/9/13** presencial; resto virtual; sin festivos; sesiones dobles **8 y 10** |
| **Arquitectura** (lun 10:00–12:00 · 6303C) | Presencialidad asistida | Sesión 1 + parciales **5/9/12** presencial; sesiones **8 y 11 autónomas** (festivos 12/10 y 02/11); **sesión 13 = sustentaciones del PI** (16/11); sesiones dobles **7 y 10** |
| **BD II** (lun 18:00–20:00 · 641A-2) | Presencialidad asistida | Igual que Arquitectura: parciales **5/9/12**; autónomas **8 y 11**; **sesión 13 = sustentaciones del PI**; sesiones dobles **7 y 10** |

## Nombres de archivo (inconsistencia conocida)

`eventos_programacion_ii_2026-1.csv` y `eventos_seminario_2026-1.csv` están etiquetados **2026-1**
aunque su contenido es del periodo **2026-2**. Se mantiene el nombre para no romper referencias;
el contenido sí está actualizado.

## Reglas transversales

- **Sesión 0** = Presentación del Curso (logística + socialización del PI); **Sesión 1** = diagnóstico
  + tema intro. El día 1 combina ambas en el bloque de 120 min.
- **Día de parcial = solo evaluación** (sin tema técnico mezclado).
- Parciales **nunca** en festivo/autónoma.
- Cortes: 30% (sesiones 1–5 · 24/08–27/09) · 30% (6–9 · 28/09–25/10) · 40% (10–13 · 26/10–22/11).
- Fuente de cortes/fechas: `config/calendario/semestre_2026_2.json`.
