# Calendario de eventos CSV 2026-2

Archivos `eventos_*_2026-1.csv` / `eventos_*_2026-2.csv` (copia en `.config/calendario/`) y `<Curso>/Plan curso/2026-1|2026-2/calendario_eventos_….csv`: 15 filas/clase por curso, UTF-8 con BOM. Notas: `[PENDIENTE listado]` hasta tener nómina.

Cuando tengas el listado de estudiantes, importa el CSV a Excel/Google Sheets o genera invitaciones (una fila = una clase; `es_parcial=si` marca parciales síncronos; `tipo_clase` = `presencial` | `virtual` | `autonoma`).

## Modalidad por curso (fuente CSV / semestre_2026_2.json)

| Curso | Oferta | Por sesión |
|---|---|---|
| **Programación II** (mié 18:00–20:00) | Presencialidad asistida | Clase 1 + parciales 5/10/15 **presencial**; resto **virtual**; festivos **autónoma** |
| **Seminario** (jue 18:00–20:00) | Presencialidad asistida | Regulares (incl. Clase 1) **virtual**; parciales 5/10/15 **presencial**; festivos **autónoma** |
| **Arquitectura** (lun 10:00–12:00 · 6303C) | Presencialidad asistida | Clase 1 + parciales 5/9/14 **presencial**; resto **virtual**; festivos **autónoma** |
| **BD II** (lun 18:00–20:00 · 641A-2) | Presencialidad asistida | Ver tipo por sesión en CSV; parciales 5/9/14 **presencial**; festivos **autónoma** |

## Reglas transversales

- **Sesión 0** = Presentación del Curso (logística); **Clase 1** = diagnóstico + tema intro. Día 1 puede combinar ambas. Se mantienen **15** clases temáticas.
- **Día de parcial = solo evaluación** (sin tema técnico mezclado).
- Parciales **nunca** en festivo/autónoma; si el cierre del corte es autónoma → última regular anterior.
- Fuente de cortes/fechas: `.config/calendario/semestre_2026_2.json`.
