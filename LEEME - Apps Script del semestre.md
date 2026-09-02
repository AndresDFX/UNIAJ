# Apps Script del semestre - 2026-2

Un **solo** Apps Script con los cursos del periodo y, para cada uno, sus funciones
de creacion y de borrado. Sirve cuando no quieres pegar 7 proyectos distintos.

Los eventos son **bloques de tu calendario**: reservan tu agenda y guardan el enlace
de Meet de cada sesion. **No llevan invitados y no mandan ningun correo**; el enlace
se comparte a mano por donde de verdad le escribes al grupo.

El script **existe** y esta aqui:

```
_privado/2026-2/CrearEncuentros - TODO EL SEMESTRE 2026-2.gs
```

> **Por que no lo ves en GitHub:** los `.gs` de encuentros viven en `_privado/`, que
> esta en `.gitignore`. Existe en tu disco y en Drive, no en el repositorio remoto.
> Si no aparece, regeneralo:
>
> ```bash
> python config/calendario/generar_apps_script_encuentros.py
> ```

## Que trae

`7` cursos · `102` sesiones · `96` salas de Meet (`6` semanas autonomas por festivo van al calendario sin Meet).

| Curso | Codigo | Grupo | Dia y hora | Sesiones | Meet |
|---|---|---|---|---|---|
| Programación II | `FI303204` | `341C` | Miércoles 18:00 – 20:00 | 13 | 13 |
| Seminario de Sistemas | `FI303301` | `341C` | Jueves 18:00 – 20:00 | 13 | 13 |
| Bases de Datos II | `FI303215` | `641A-2` | Lunes 18:00 – 20:00 | 13 | 11 |
| Arquitectura de Sistemas Computacionales | `FI303380` | `6303C` | Lunes 10:00 – 12:00 | 13 | 11 |
| Introducción a la Ingeniería · SB141B | `FI300101` | `SB141B` | Jueves 14:30 – 16:00 | 16 | 16 |
| Introducción a la Ingeniería · SB141C | `FI300101` | `SB141C` | Martes 14:30 – 16:00 | 17 | 16 |
| Introducción a la Ingeniería · LB141F | `FI300101` | `LB141F` | Martes 18:30 – 20:00 | 17 | 16 |

## Choques en TU horario

**Ninguno.** Se compararon los 7 cursos por pares (mismo dia + horas que
se cruzan) y no hay dos bloques encima. Se revisa en cada regeneracion, porque con
7 grupos en la misma semana es facil que un horario nuevo se pise con otro.

## Aviso del calendario: Las fechas de fin caen en la semana de Navidad

El inicio se corrió una semana a peticion del docente (2026-09-02): los grupos de martes arrancan el 08/09/2026 y el de jueves el 10/09/2026. Con 16 sesiones semanales eso lleva el cierre al 2026-12-24 (jueves, SB141B) y al 2026-12-29 (martes, SB141C y LB141F, ya contando el festivo del 08/12 como semana autónoma). Las dos fechas caen DENTRO del receso de Navidad: el 24/12 es vispera de Navidad y el 29/12 esta entre Navidad y Año Nuevo. Ademas siguen mas de un mes despues del 22/11/2026 en que cierran los otros cuatro cursos del semestre. NINGUNA de las dos es dictable tal cual, y el corte 3 —exposicion final e informe— es justo lo que cae ahi.

**Plan B si el programa exige cerrar antes:** Dos opciones, las dos pendientes de confirmar con el programa. (A) Fusionar los temas 15 y 16 en una sola sesion: quedan 15 sesiones y el cierre pasa al 17/12 (jueves) y al 22/12 (martes), antes de Navidad. Cuesta que la socializacion y la autoevaluacion del tema 16 se hacen en el mismo bloque que las exposiciones. (B) Adelantar la exposicion final y el informe a las sesiones 13 y 14, dejando 15 y 16 como semanas autonomas de cierre. Cuesta que el proyecto se sustenta con dos semanas menos de trabajo. No se ha aplicado ninguna: las fechas de este archivo son las del corrimiento pedido, sin comprimir.

> Mientras no se confirme, el script crea las fechas **tal como estan en el JSON**.
> Ninguna fecha se movio para escribir este aviso.

## Funciones

En el desplegable de Apps Script, **por curso**:

| Funcion | Que hace |
|---|---|
| `verificarProgramacionII` / `crearProgramacionII` / `eliminarProgramacionII` / `recrearProgramacionII` | solo ese curso (Programación II) |
| `verificarSeminario` / `crearSeminario` / `eliminarSeminario` / `recrearSeminario` | solo ese curso (Seminario de Sistemas) |
| `verificarBasesDatosII` / `crearBasesDatosII` / `eliminarBasesDatosII` / `recrearBasesDatosII` | solo ese curso (Bases de Datos II) |
| `verificarArquitectura` / `crearArquitectura` / `eliminarArquitectura` / `recrearArquitectura` | solo ese curso (Arquitectura de Sistemas Computacionales) |
| `verificarIntroduccionIngenieriaSB141B` / `crearIntroduccionIngenieriaSB141B` / `eliminarIntroduccionIngenieriaSB141B` / `recrearIntroduccionIngenieriaSB141B` | solo ese curso (Introducción a la Ingeniería · SB141B) |
| `verificarIntroduccionIngenieriaSB141C` / `crearIntroduccionIngenieriaSB141C` / `eliminarIntroduccionIngenieriaSB141C` / `recrearIntroduccionIngenieriaSB141C` | solo ese curso (Introducción a la Ingeniería · SB141C) |
| `verificarIntroduccionIngenieriaLB141F` / `crearIntroduccionIngenieriaLB141F` / `eliminarIntroduccionIngenieriaLB141F` / `recrearIntroduccionIngenieriaLB141F` | solo ese curso (Introducción a la Ingeniería · LB141F) |

Y **para todo el semestre**:

| Funcion | Que hace |
|---|---|
| `verificarTodosLosCursos` | Solo lectura. Ejecutala primero, siempre. |
| `crearTodosLosCursos` | Crea lo que falte en los 7 cursos. Reejecutable: reutiliza lo que ya existe. |
| `eliminarTodosLosCursos` | Borra los 102 eventos. No notifica a nadie, pero se lleva las 96 salas de Meet. |
| `recrearTodosLosCursos` | Borra y vuelve a crear todo. Lo mas ruidoso: **todos** los enlaces de Meet cambian. |
| `listarCalendarios` | Imprime los IDs de calendario, para llenar `CALENDAR_ID`. |

## Antes que nada: la zona horaria del proyecto

En Apps Script, **Configuracion del proyecto -> Zona horaria -> `America/Bogota`**.

Las horas de los eventos las construye Apps Script con la zona del **proyecto**, no con
la del calendario. Si el proyecto queda en otra (Google no siempre pone la local), los
102 eventos entran corridos y con ellos las 96 salas de Meet. `verificar*`
imprime la zona, y si no es la correcta **crear y borrar quedan bloqueados**.

## Dos interruptores antes de que toque nada

```js
var SIMULAR = true;                        // no crea ni borra: solo dice que haria
var CONFIRMO_SEMESTRE_COMPLETO = false;    // exigido por las funciones *TodosLosCursos*
```

`SIMULAR = true` es el modo de siempre: las funciones listan lo que harian, incluidos
los eventos «huerfanos» (los de una corrida anterior con el titulo viejo) y los
«fantasmas» (los que quedaron en una fecha que ya no esta en el calendario del curso).
Para ejecutar de verdad se pone en `false`.

El segundo interruptor lo piden **solo** las cuatro funciones `*TodosLosCursos`. Ya no
hay correos que enviar, pero sigue teniendo sentido: de un golpe tocan `102` eventos y
crean o destruyen `96` salas de Meet, roza la cuota diaria de Calendar, tarda lo
suyo, y en el desplegable de Apps Script es facil elegir una de esas en vez de la de un
curso. Deshacerlo a mano son 102 borrados. Las funciones por curso no lo necesitan.

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
`LEEME - Apps Script del curso.md` visible en `Plan curso/2026-2/`. Los grupos
que comparten asignatura (y por tanto carpeta) llevan el grupo en el nombre:
`LEEME - Apps Script del curso - <GRUPO>.md`.

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
