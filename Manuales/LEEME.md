# Manuales operativos — docente

Procedimientos que se ejecutan **fuera del repo** (Google Calendar, Drive, Apps Script).
Están escritos de forma **general**: sirven para cualquier periodo y cualquier curso. Donde
aparece `<periodo>` va la etiqueta del semestre (`2026-2`, `2027-1`, …) y donde aparece
`<Curso>` la carpeta del curso.

Aquí no hay material de clase: esto es el "cómo se alista y se opera el semestre".

| Manual | Cuándo se usa |
|---|---|
| [01 — Alistar un curso: encuentros, Meet y correo](01%20-%20Alistar%20un%20curso%20%28encuentros%2C%20Meet%2C%20correo%20e%20invitaciones%29.md) | Al arrancar un periodo. Hay dos caminos: un proyecto de Apps Script por curso, o **uno solo con todos los cursos** |
| [02 — Instalar y probar el Apps Script de grabaciones](02%20-%20Instalar%20y%20probar%20el%20Apps%20Script%20de%20grabaciones.md) | Una vez por cuenta; sirve para todos los cursos y periodos |

## El orden, en corto

```
0. Regenerar y validar          (4 scripts en config/calendario/)
1. Enviar el correo             → dice el horario y por dónde se publica el enlace
2. Crear los encuentros         → bloques de TU calendario, cada uno con SU enlace de Meet
3. Publicar los enlaces         → en ExamLab: el estudiante no recibe invitación
4. Archivado de grabaciones     → manual 02, una sola vez
```

**Cada sesión tiene su propio enlace de Meet**, así que el correo no publica ninguno y no
depende de que la serie exista: va primero. Los eventos son **bloques del calendario personal
del docente** —sin invitados y sin correos—, así que el paso 3 no es opcional: es la única forma
en que el grupo llega a la sala.

El paso 2 se puede hacer curso por curso o de una vez para todo el periodo, con el script
consolidado (`LEEME - Apps Script del semestre.md`, en la raíz de `Cursos`). Los dos salen de
la misma plantilla; el manual 01 explica cuándo conviene cada uno.

## Antes de cualquiera de los dos manuales

```bash
python config/calendario/validar_calendario.py
```

Debe terminar en `OK: … sin fallos.` Si falla, arréglalo primero: estos procedimientos
publican cosas de cara al estudiante, y corregir aquí es más barato que corregir un horario ya
enviado al grupo, unos enlaces ya publicados o unas grabaciones ya movidas en una carpeta
compartida.

## Qué produce el repo y qué lleva datos personales

Todo lo de un curso vive en la carpeta de ese curso:

| Archivo | Dónde | Datos de estudiantes |
|---|---|---|
| `CORREO_BIENVENIDA - <Curso> - <periodo>.md` | `<Curso>/Plan curso/<periodo>/` | No — se versiona |
| `eventos_calendario_<periodo>.csv` | `<Curso>/Plan curso/<periodo>/` | No — se versiona |
| `CrearEncuentros - <Curso>.gs` | `<Curso>/Plan curso/<periodo>/_privado/` | No (ya no lleva invitados) — sigue fuera de git |
| `bloques_<curso>.ics` | `<Curso>/Plan curso/<periodo>/_privado/` | No (`METHOD:PUBLISH`, sin `ATTENDEE`) — sigue fuera de git |
| `nomina_<curso>.csv` | `<Curso>/Plan curso/<periodo>/_privado/` | **Sí** — fuera de git |
| `asistencia_<curso>.csv` | `<Curso>/Plan curso/<periodo>/_privado/` | **Sí** — fuera de git |
| `correos_manuales.csv` | `<Curso>/Plan curso/<periodo>/_privado/` | **Sí** — lo mantienes tú |

Las carpetas `_privado/` están en `.gitignore`. No las compartas ni las subas. Los dos primeros
archivos de `_privado/` dejaron de llevar datos personales cuando los encuentros pasaron a ser
bloques del calendario del docente; se quedan ahí por convención, junto a la nómina.

> Cuando varios grupos comparten la carpeta del curso, el **grupo** va en el nombre del archivo
> (`CrearEncuentros - <Curso> - SB141B.gs`, `eventos_calendario_<periodo> - SB141B.csv`,
> `bloques_<curso>_sb141b.ics`).

## Fuente de verdad

Fechas, sesiones, parciales, festivos y carpetas de Drive salen de
`config/calendario/semestre_<periodo>.json`. Si algo está mal, **se corrige ahí y se
regenera**, nunca a mano en los documentos: lo escrito a mano se pierde en la siguiente
corrida.

En `2026-2` hay un **segundo** archivo: `config/calendario/introduccion_ingenieria_2026_2.json`,
con los **3 grupos** de Introducción a la Ingeniería (FI300101). Está aparte porque no cabe en
las reglas del otro (16 sesiones de 90 min, dos días distintos, fechas que llegan a diciembre).
Los generadores leen **los dos**: 4 + 3 = **7 cursos**.
