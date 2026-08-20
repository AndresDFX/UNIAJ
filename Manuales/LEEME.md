# Manuales operativos — docente

Procedimientos que se ejecutan **fuera del repo** (Google Calendar, Drive, Apps Script).
Están escritos de forma **general**: sirven para cualquier periodo y cualquier curso. Donde
aparece `<periodo>` va la etiqueta del semestre (`2026-2`, `2027-1`, …) y donde aparece
`<Curso>` la carpeta del curso.

Aquí no hay material de clase: esto es el "cómo se opera el semestre".

| Manual | Cuándo se usa |
|---|---|
| [01 — Crear los eventos del calendario e invitar a los estudiantes](01%20-%20Crear%20los%20eventos%20del%20calendario%20e%20invitar%20a%20los%20estudiantes.md) | Al arrancar un periodo, y cada vez que cambie el calendario o llegue una nómina nueva |
| [02 — Instalar y probar el Apps Script de grabaciones](02%20-%20Instalar%20y%20probar%20el%20Apps%20Script%20de%20grabaciones.md) | Una vez por cuenta, antes de la primera sesión virtual |

## Antes de cualquiera de los dos

```bash
python config/calendario/validar_calendario.py
```

Debe terminar en `OK: … sin fallos.` Si falla, arréglalo primero: los dos procedimientos
publican cosas de cara al estudiante, y corregir aquí es más barato que retirar invitaciones
ya enviadas o mover grabaciones de una carpeta compartida.

## Qué produce el repo y qué lleva datos personales

| Archivo | Dónde | Datos de estudiantes |
|---|---|---|
| `eventos_calendario_<periodo>.csv` | `<Curso>/Plan curso/<periodo>/` | No — se versiona |
| `CORREO_BIENVENIDA - <Curso> - <periodo>.md` | `<Curso>/Plan curso/<periodo>/` | No — se versiona |
| `invitaciones_<curso>.ics` | `config/calendario/_privado_<periodo>/` | **Sí** — fuera de git |
| `nomina_<curso>.csv` | `config/calendario/_privado_<periodo>/` | **Sí** — fuera de git |
| `asistencia_<curso>.csv` | `config/calendario/_privado_<periodo>/` | **Sí** — fuera de git |
| `_correos_manuales.csv` | `config/calendario/` | **Sí** — fuera de git · entrada que mantienes tú |

La carpeta `_privado_<periodo>/` está en `.gitignore`. No la compartas ni la subas.

## Fuente de verdad

Fechas, sesiones, parciales, festivos y carpetas de Drive salen de
`config/calendario/semestre_<periodo>.json`. Si algo está mal, **se corrige ahí y se
regenera**, nunca a mano en los documentos: lo escrito a mano se pierde en la siguiente
corrida.
