# Calendario 2026-2 — cómo se mantiene

## Fuente de verdad

`semestre_2026_2.json` es la **única** fuente de verdad del calendario.

Contiene, por curso, el array `clases` con las **13 sesiones** del semestre acortado
(inicio **2026-08-24** · fin fijo **2026-11-22**) y, en cada sesión:

| campo | significado |
|---|---|
| `n` | número de **sesión** (1-13) |
| `fecha`, `tipo`, `festivo` | fecha ISO · `presencial` / `virtual` / `autonoma` / `sustentacion` · nombre del festivo |
| `parcial`, `parcial_n` | si esa sesión es parcial y cuál |
| `clases_material` | los **"Clase N"** del material ya construido que se dictan en esa sesión |
| `tema` | título del tema (o temas, si es sesión doble) |
| `sesion_doble` | `true` si cubre dos clases de material en un bloque de 120 min |

> **Sesión ≠ Clase.** Se conservan los **15 temas** del microcurrículo en 13 sesiones:
> 2 sesiones por curso son **dobles**. Las carpetas `Clases/Clase N - …` y
> `Kit docente/Clase N/` **no se renumeraron**; lo que cambió es el mapeo
> Sesión → Clase(s) de material.

## Cómo regenerar

```bash
python3 config/calendario/generar_semestre_2026_2.py
```

Ese script **lee** el JSON (no lo reescribe) y regenera, por curso:
`Plan curso/2026-2/{CALENDARIO_2026-2.md, calendario_eventos_2026-2.csv, Cronograma 2026-2.md, PLAN_DE_CURSO_2026-2.md, CORREO_BIENVENIDA - <Curso> - 2026-2.md}`,
el `ACUERDO PEDAGOGICO …docx` en `Entregas docente/2026-2/` y las copias `eventos_*.csv` de esta carpeta.
Es **idempotente**: dos corridas seguidas producen archivos idénticos.

> **Ubicación del correo de bienvenida:** va en `Plan curso/<periodo>/`, no en
> `Entregas docente/`. Esa última carpeta guarda **solo lo que el docente le entrega a la
> universidad** (acuerdo, diagnóstico). El correo es planeación y comunicación con el
> grupo. Si el script encuentra un correo en la ubicación vieja, lo **migra** solo.

Para cambiar el calendario: **edita el JSON y vuelve a correr el generador.** Nada más.

Los otros dos generadores vivos de esta carpeta:

| Script | Qué produce |
|---|---|
| `generar_eventos_calendario.py` | Por curso: CSV de eventos, `.ics` con invitados, nómina y planilla de asistencia (los tres últimos en `<Curso>/Plan curso/<periodo>/_privado/`) |
| `generar_apps_script_encuentros.py` | Por curso: el Apps Script que **crea** los encuentros en Calendar con una sola sala de Meet y **envía** las invitaciones |
| `validar_calendario.py` | Comprueba invariantes y coherencia; sale con código 1 si algo falla |

Procedimiento operativo: carpeta `Manuales/` en la raíz de `Cursos`.

Las diapositivas y los parciales leen el mismo JSON a través de
`config/slides/calendario_2026_2.py` y `config/parciales/contenido_parciales_2026_2.py`.

## ⚠️ NO re-ejecutar los scripts `_fix_*.py` / `_patch_*.py` de esta carpeta

Los archivos `_fix_parciales_2026_2.py`, `_fix_modalidad_2026_2.py`,
`_patch_modalidad_prog_sem_2026_2.py`, `_reorg_y_cronograma.py`,
`_gen_eventos_y_builds.py`, `_fix_parcial_solo_eval.py`, `_finish_csv_bd2.py`,
`_fix_bd2_horario.py`, `_patch_arq_horario_120.py`, `_patch_generador*.py`,
`_patch_dudas.py`, `_finish_padlet.py`, `_padlet_pptx_fix.py`,
`_verify_arq_horario.py`, `_apply_all.py`, `_gen_all.py`
son **parches one-shot ya aplicados**, de antes del cambio de calendario.

Tienen hardcodeadas las fechas viejas (inicio **10/08/2026**, ventanas de corte
`10/08 → 13/09`, `14/09 → 18/10`, `19/10 → 22/11`) y la estructura de **15 clases**
con parciales en 5/10/15 y 5/9/14.

**Re-ejecutarlos revertiría el calendario al esquema anterior** o fallaría con
`WARN skip` al no encontrar los strings literales que esperaban. Algunos además
apuntan a rutas que ya no existen (`Plan curso/2026-1/`, `.config\calendario`).

Se conservan solo como historial. Si necesitas un cambio, hazlo en el JSON + el
generador, no resucitando estos scripts.
