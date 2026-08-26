# Calendario de eventos CSV 2026-2

Archivos `eventos_<curso>_2026-2.csv` (copia consolidada en `config/calendario/`) y
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

Produce dos clases de salida, deliberadamente separadas. **Todo lo de un curso vive en la
carpeta del curso**; en `config/` quedan solo los scripts.

| Salida | Nómina | Ruta | Para qué |
|---|---|---|---|
| `eventos_calendario_<periodo>.csv` | **No** | `<Curso>/Plan curso/<periodo>/` | Importar los bloques a tu calendario |
| `invitaciones_<curso>.ics` | **Sí** | `<Curso>/Plan curso/<periodo>/_privado/` | Eventos con los estudiantes como `ATTENDEE` |
| `nomina_<curso>.csv` | **Sí** | idem | documento, nombre, correo, `origen_correo`, repitente |
| `asistencia_<curso>.csv` | **Sí** | idem | Planilla estudiantes × sesiones (nota de asistencia) |
| `pendientes_correo_<curso>.csv` | **Sí** | idem (solo si aplica) | Quién no trae correo institucional |

La regla `_privado/` está en `.gitignore`: son datos personales de estudiantes (nombre,
documento, correo) y **no se versionan ni se comparten**. El CSV de eventos que sí se versiona
no lleva nómina, y el script no imprime nombres ni correos en consola, solo conteos.

### El camino recomendado no es el .ics

**Importar un `.ics` no envía las invitaciones**: Google deja a los invitados dentro del
evento pero no les manda nada. Para que lleguen, y para que cada sesión tenga **su propia
sala de Meet**, se usa el Apps Script que genera:

```bash
python config/calendario/generar_apps_script_encuentros.py
```

Emite `<Curso>/Plan curso/<periodo>/_privado/CrearEncuentros - <Curso>.gs`, que crea la serie
con la API de Calendar (`sendUpdates: 'all'`) y le pone a cada sesión sincrónica una sala de
Meet distinta (`requestId` propio por sesión, así reejecutar no duplica). Las autónomas por
festivo van al calendario pero **sin Meet**, porque no hay encuentro.

No hay ningún enlace que pegar de vuelta en el material: al estudiante le llega el de cada
sesión dentro de su invitación de Calendar. El mismo `.gs` trae `eliminarEncuentros()` y
`recrearTodo()` para rehacer la serie desde cero.

El `.ics` y el CSV quedan como camino manual alternativo. Las sesiones autónomas van en el
`.ics` como `TRANSP:TRANSPARENT` porque no bloquean agenda.

**Procedimiento completo:** carpeta `Manuales/` en la raíz de `Cursos`.

### Correos que faltan en el export académico

Cuando el sistema no trae el correo institucional de alguien, **no se edita el `.xls`**: se
agrega en `<Curso>/Plan curso/<periodo>/_privado/correos_manuales.csv`
(`documento,correo,nota`), que el generador cruza por documento. Es entrada del docente, tiene
datos personales y está fuera de git. En la nómina esos estudiantes salen con
`origen_correo = personal (manual)`.

### Validación

`python config/calendario/validar_calendario.py` comprueba los invariantes del calendario
(semana de inicio, sesiones numeradas sin huecos, día de la semana correcto, una sesión por
semana, los 15 temas cubiertos sin duplicados, sesiones dobles coherentes, ningún parcial en
festivo o sesión autónoma, cortes que cubren todas las sesiones), que los CSV y el
`CALENDARIO_<periodo>.md` derivados coincidan con el JSON, y que las carpetas de Drive del
JSON coincidan con las del Apps Script de grabaciones. Devuelve código 1 si algo falla.

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

## Nombres de archivo y periodos

Los 4 CSV por curso llevan el periodo vigente: `eventos_<curso>_2026-2.csv`.

Antes, los de Programación II y Seminario se llamaban `*_2026-1.csv` aunque su contenido ya era
2026-2. Se renombraron porque **2026-1 sí es un periodo real** de esos dos cursos: tienen una
oferta anterior archivada en `<Curso>/Plan curso/2026-1/` (ver su `LEEME - periodo 2026-1.md`),
así que un archivo con 2026-1 en el nombre y contenido de 2026-2 era engañoso.

Bases de Datos II y Arquitectura no tienen periodo anterior en este repo: arrancan en 2026-2.

## Reglas transversales

- **Sesión 0** = Presentación del Curso (logística + socialización del PI); **Sesión 1** = diagnóstico
  + tema intro. El día 1 combina ambas en el bloque de 120 min.
- **Día de parcial = solo evaluación** (sin tema técnico mezclado).
- Parciales **nunca** en festivo/autónoma.
- Cortes: 30% (sesiones 1–5 · 24/08–27/09) · 30% (6–9 · 28/09–25/10) · 40% (10–13 · 26/10–22/11).
- Fuente de cortes/fechas: `config/calendario/semestre_2026_2.json`.
