# Ajustes puntuales del calendario ya creado

Scripts de Apps Script que **corrigen eventos que ya existen**, sin recrearlos.

## Por qué no se usa `recrearTodo()`

`recrearTodo()` del script de encuentros borra y vuelve a crear cada evento, y con el
evento **se va su sala de Meet**. Cada sesión tiene su propio enlace, así que recrear
significa enlaces nuevos: los que ya se compartieron con el grupo dejan de servir. Para
un cambio pequeño —correr media hora la entrada— eso es un precio absurdo.

Cambiar la hora de un evento existente con `setTime()` **conserva la sala**: es la misma
reunión, media hora más tarde. Eso es lo que hacen estos scripts.

## `AjustarHoraInicio.gs`

Mueve el **inicio** de los encuentros de **Programación II** y **Seminario de Sistemas**
de las **18:00 a las 18:30**. El fin (20:00) no se toca.

### Procedimiento

| | Función | Qué hace |
|---|---|---|
| 1 | `listarCalendarios()` | imprime los calendarios con su ID. Copia el del calendario donde creaste los encuentros y pégalo en `CALENDAR_ID`, arriba del archivo. |
| 2 | `verificar()` | **no cambia nada.** Dice cuántos eventos encontró, cuántos movería, cuántos ya están y cuáles tienen otro horario. |
| 3 | `ajustarHoraInicio()` | con `SIMULAR = true` primero (solo escribe en el registro lo que haría). Cuando el registro diga lo que esperas, `SIMULAR = false` y vuelve a ejecutar. |
| 4 | `verificar()` | confirma que quedaron en 18:30. |
| — | `revertir()` | deshace: devuelve el inicio a las 18:00. |

### Lo que el script no hace

- **No crea ni borra** ningún evento. Los enlaces de Meet se conservan.
- **No toca invitados ni manda correos.** Los eventos son bloques del calendario personal
  del docente y no tienen invitados; `setTime` sobre un evento sin invitados no notifica a
  nadie.
- **No toca Bases de Datos II ni Arquitectura**, aunque BD II también esté a las 18:00.
  Solo mueve eventos cuyo título menciona uno de los dos cursos de `CURSOS`.
- **No toca un evento con otro horario.** Si una sesión se reprogramó a otra hora, la
  reporta y la deja quieta: moverla a 18:30 sería inventarse una decisión.
- **Se bloquea** si la zona horaria del proyecto Apps Script no es `America/Bogota`. No es
  paranoia: el script construye la hora nueva con `new Date(...)`, que usa la zona del
  **proyecto**. Con el proyecto en UTC, «18:30» serían las 13:30 en Bogotá y los 26 eventos
  quedarían corridos cinco horas.

### Pruebas

```bash
node config/calendario/pruebas_apps_script/probar_ajuste_hora.js
```

34 comprobaciones contra un simulacro de las APIs de Google: que mueva solo los dos cursos,
que no toque los eventos ajenos de la misma hora, que conserve el enlace de Meet, que
`SIMULAR` no escriba, que `revertir()` deje el calendario como estaba, que sea idempotente,
que se bloquee con la zona mal, y que si Google falla en un evento lo reporte en vez de
dejar la serie a medias.

## Ojo: la fuente de verdad sigue diciendo 18:00

`config/calendario/semestre_2026_2.json` declara los dos cursos como **18:00 – 20:00, 120
min**. Este script cambia el calendario, **no el JSON**. Consecuencias:

- Si alguien corre `generar_apps_script_encuentros.py` y luego `recrearTodo()`, los eventos
  vuelven a las 18:00.
- Un bloque de 18:30 a 20:00 son **90 minutos**, no 120, y el material de esos dos cursos
  está escrito para 120: los planes minuto a minuto de los guiones van de 0 a 120 y los
  decks lo dicen 102 veces.

Cambiar el JSON obliga a decidir qué pasa con esos 30 minutos de material, así que se dejó
sin tocar a propósito.

## Introducción a la Ingeniería: por qué NO hay un script de ajuste aquí

Hasta el 2026-09-04 hubo un `AjustarFechaIntroIng.gs` que corría una semana las 50 fechas
de los tres grupos (16-17 sesiones cada uno, terminando en diciembre). Se **borró** ese
mismo día: el curso pasó de 16 a **11 sesiones de calendario** (5 sesiones dobles, dos
Clases del microcurrículo en un mismo bloque de 90 min) para cerrar dentro de la ventana
institucional, y el mapeo sesión-a-fecha que ese script conocía quedó completamente
obsoleto — no es que las fechas se corrieran otra semana, es que la mitad de las sesiones
que existían ya no existen como tales (ahora cubren dos Clases cada una) y las fechas de
diciembre desaparecieron del todo.

Intentar escribir un mapeo fino evento-por-evento entre el calendario viejo (16-17
sesiones hasta diciembre) y el nuevo (11 sesiones hasta el 17-19/11) es la clase de
ejercicio donde un error de un día se nota tarde. La instrucción correcta, dado el tamaño
del cambio, es la más simple y la más segura: **borrar los tres grupos y crearlos de
nuevo** con el `.gs` consolidado ya regenerado.

```
eliminarIntroduccionIngenieriaSB141B()
eliminarIntroduccionIngenieriaSB141C()
eliminarIntroduccionIngenieriaLB141F()

crearIntroduccionIngenieriaSB141B()
crearIntroduccionIngenieriaSB141C()
crearIntroduccionIngenieriaLB141F()
```

Esto **sí genera salas de Meet nuevas** para las 33 sesiones de los tres grupos —es
inevitable: el calendario cambió de forma, no de posición—, así que los enlaces que ya se
hubieran compartido con los tres grupos dejan de servir y hay que volver a compartirlos.
Sigue sin invitar a nadie ni mandar ningún correo: son bloques del calendario personal del
docente, igual que siempre.
