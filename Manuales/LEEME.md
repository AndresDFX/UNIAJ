# Manuales operativos — docente

Procedimientos que se ejecutan **fuera del repo** (Google Calendar, Drive, Apps Script).
Están escritos de forma **general**: sirven para cualquier periodo y cualquier curso. Donde
aparece `<periodo>` va la etiqueta del semestre (`2026-2`, `2027-1`, …) y donde aparece
`<Curso>` la carpeta del curso.

Aquí no hay material de clase: esto es el "cómo se alista y se opera el semestre".

| Manual | Cuándo se usa |
|---|---|
| [01 — Alistar un curso: encuentros, Meet, correo e invitaciones](01%20-%20Alistar%20un%20curso%20%28encuentros%2C%20Meet%2C%20correo%20e%20invitaciones%29.md) | Al arrancar un periodo, **una vez por curso** |
| [02 — Instalar y probar el Apps Script de grabaciones](02%20-%20Instalar%20y%20probar%20el%20Apps%20Script%20de%20grabaciones.md) | Una vez por cuenta; sirve para todos los cursos y periodos |

## El orden, en corto

```
0. Regenerar y validar          (4 scripts en config/calendario/)
1. Crear los encuentros         → de ahí sale el enlace de Meet y se envían las invitaciones
2. Pegar el enlace de Meet      → y regenerar
3. Enviar el correo             → ya con el enlace adentro
4. Archivado de grabaciones     → manual 02, una sola vez
```

El paso 1 va antes del correo porque **el enlace de Meet lo crea Google, no el repo**: hasta
que no existe la serie de encuentros no hay enlace que publicar.

## Antes de cualquiera de los dos manuales

```bash
python config/calendario/validar_calendario.py
```

Debe terminar en `OK: … sin fallos.` Si falla, arréglalo primero: estos procedimientos
publican cosas de cara al estudiante, y corregir aquí es más barato que retirar invitaciones
ya enviadas o mover grabaciones en una carpeta compartida.

## Qué produce el repo y qué lleva datos personales

Todo lo de un curso vive en la carpeta de ese curso:

| Archivo | Dónde | Datos de estudiantes |
|---|---|---|
| `CORREO_BIENVENIDA - <Curso> - <periodo>.md` | `<Curso>/Plan curso/<periodo>/` | No — se versiona |
| `eventos_calendario_<periodo>.csv` | `<Curso>/Plan curso/<periodo>/` | No — se versiona |
| `CrearEncuentros - <Curso>.gs` | `<Curso>/Plan curso/<periodo>/_privado/` | **Sí** — fuera de git |
| `invitaciones_<curso>.ics` | `<Curso>/Plan curso/<periodo>/_privado/` | **Sí** — fuera de git |
| `nomina_<curso>.csv` | `<Curso>/Plan curso/<periodo>/_privado/` | **Sí** — fuera de git |
| `asistencia_<curso>.csv` | `<Curso>/Plan curso/<periodo>/_privado/` | **Sí** — fuera de git |
| `correos_manuales.csv` | `<Curso>/Plan curso/<periodo>/_privado/` | **Sí** — lo mantienes tú |

Las carpetas `_privado/` están en `.gitignore`. No las compartas ni las subas.

## Fuente de verdad

Fechas, sesiones, parciales, festivos, carpetas de Drive y el enlace de Meet salen de
`config/calendario/semestre_<periodo>.json`. Si algo está mal, **se corrige ahí y se
regenera**, nunca a mano en los documentos: lo escrito a mano se pierde en la siguiente
corrida.
