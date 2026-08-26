# Apps Script del semestre - 2026-2

Un **solo** Apps Script con los cursos del periodo y, para cada uno, sus funciones
de creacion y de borrado. Sirve cuando no quieres pegar cuatro proyectos distintos.

El script **existe** y esta aqui:

```
_privado/2026-2/CrearEncuentros - TODO EL SEMESTRE 2026-2.gs
```

> **Por que no lo ves en GitHub:** lleva los correos de los 59 estudiantes
> matriculados en los 4 cursos, asi que `_privado/` esta en `.gitignore`.
> Existe en tu disco y en Drive, no en el repositorio remoto. Si no aparece,
> regeneralo:
>
> ```bash
> python config/calendario/generar_apps_script_encuentros.py
> ```

## Que trae

`4` cursos · `52` sesiones · `80` matriculas (`59` personas distintas).

| Curso | Codigo | Grupo | Dia y hora | Sesiones | Invitados |
|---|---|---|---|---|---|
| Programación II | `FI303204` | `341C` | Miércoles 18:00 – 20:00 | 13 | 22 |
| Seminario de Sistemas | `FI303301` | `341C` | Jueves 18:00 – 20:00 | 13 | 22 |
| Bases de Datos II | `FI303215` | `641A-2` | Lunes 18:00 – 20:00 | 13 | 18 |
| Arquitectura de Sistemas Computacionales | `FI303380` | `6303C` | Lunes 10:00 – 12:00 | 13 | 18 |

## Ojo: hay estudiantes en mas de un curso

Las 80 matriculas son **59 personas**: hay quien esta en dos cursos.

| Cursos | Estudiantes en comun |
|---|---|
| Programación II + Seminario de Sistemas | **21** |

A esas personas, **cada operacion «de los 4 cursos» les llega por duplicado**: dos
invitaciones por semana, y dos cancelaciones si se borra todo. Cuando solo hay que
arreglar un curso, usa la funcion de ese curso.

## Funciones

En el desplegable de Apps Script, **por curso**:

| Funcion | Que hace |
|---|---|
| `verificarProgramacionII` / `crearProgramacionII` / `eliminarProgramacionII` / `recrearProgramacionII` | solo ese curso (Programación II) |
| `verificarSeminario` / `crearSeminario` / `eliminarSeminario` / `recrearSeminario` | solo ese curso (Seminario de Sistemas) |
| `verificarBasesDatosII` / `crearBasesDatosII` / `eliminarBasesDatosII` / `recrearBasesDatosII` | solo ese curso (Bases de Datos II) |
| `verificarArquitectura` / `crearArquitectura` / `eliminarArquitectura` / `recrearArquitectura` | solo ese curso (Arquitectura de Sistemas Computacionales) |

Y **para todo el semestre**:

| Funcion | Que hace |
|---|---|
| `verificarTodosLosCursos` | Solo lectura. Ejecutala primero, siempre. |
| `crearTodosLosCursos` | Crea lo que falte en los 4 cursos y sincroniza invitados. Reejecutable. |
| `eliminarTodosLosCursos` | Borra los 52 eventos. **Manda ~1040 cancelaciones.** |
| `recrearTodosLosCursos` | Borra y vuelve a crear todo. Lo mas ruidoso. |
| `listarCalendarios` | Imprime los IDs de calendario, para llenar `CALENDAR_ID`. |

## Antes que nada: la zona horaria del proyecto

En Apps Script, **Configuracion del proyecto -> Zona horaria -> `America/Bogota`**.

Las horas de los eventos las construye Apps Script con la zona del **proyecto**, no con
la del calendario. Si el proyecto queda en otra (Google no siempre pone la local), los
52 eventos entran corridos y las invitaciones ya salieron. `verificar*` imprime la
zona, y si no es la correcta **crear y borrar quedan bloqueados**.

## Dos interruptores antes de que toque nada

```js
var SIMULAR = true;                        // no crea ni borra: solo dice que haria
var CONFIRMO_SEMESTRE_COMPLETO = false;    // exigido por las funciones *TodosLosCursos*
```

`SIMULAR = true` es el modo de siempre: las funciones listan lo que harian, incluidos
los eventos «huerfanos» (los de una corrida anterior con el titulo viejo) y los
«fantasmas» (los que quedaron en una fecha que ya no esta en el calendario del curso).
Para ejecutar de verdad se pone en `false`.

El segundo interruptor lo piden **solo** las cuatro funciones `*TodosLosCursos`, porque tocan `52` eventos y mas de mil correos de golpe, y en el desplegable es
facil elegir esa en vez de la de un curso. Las funciones por curso no lo necesitan.

## Si se corta a la mitad

Apps Script mata cualquier ejecucion a los 30 minutos (6 en cuentas gratuitas). El
script se corta **solo** antes de eso (`MINUTOS_MAX`) y lo dice en el log. No se
pierde nada: vuelve a ejecutar la misma funcion y retoma donde quedo, porque reutiliza
los eventos y las salas de Meet que ya existen.

## Lo mismo, pero por curso

Si prefieres un proyecto por curso, cada uno tiene el suyo:

```
<Curso>/Plan curso/2026-2/_privado/CrearEncuentros - <Curso>.gs
```

Salen de la **misma plantilla** que este, asi que hacen exactamente lo mismo; solo
cambian los nombres de las funciones (`verificar`, `crearEncuentros`,
`eliminarEncuentros`, `recrearTodo`). Cada curso tiene su
`LEEME - Apps Script del curso.md` visible en `Plan curso/2026-2/`.

**Paso a paso:** `Manuales/01 - Alistar un curso (encuentros, Meet, correo e
invitaciones).md`.

## Si tocaste el generador

Los `.gs` no se editan a mano. Y el generador tiene pruebas que ejecutan el `.gs` de
verdad contra un simulacro de las APIs de Google:

```bash
bash config/calendario/pruebas_apps_script/probar.sh
```

Comprueban que reejecutar no duplica, que cada sesion tiene su sala, que el borrado no
se lleva nada ajeno y que los dos interruptores frenan. Detalle:
`config/calendario/pruebas_apps_script/LEEME.md`.

---

*Archivo generado por `config/calendario/generar_apps_script_encuentros.py`.*
