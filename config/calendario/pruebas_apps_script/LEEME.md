# Pruebas de los Apps Script de encuentros

Los `.gs` que genera `generar_apps_script_encuentros.py` corren en Google, contra el
calendario de verdad, invitando a estudiantes de verdad. Un error ahí no se deshace: las
invitaciones y las cancelaciones ya salieron.

Estas pruebas ejecutan el `.gs` **de verdad** (en Node, con `vm`) contra un simulacro de las
APIs de Google. No es un análisis del texto del script: se llaman las funciones y se mira qué
quedó en el calendario simulado.

## Correrlas

```bash
python config/calendario/generar_apps_script_encuentros.py   # primero, que existan los .gs
bash config/calendario/pruebas_apps_script/probar.sh          # o: ... probar.sh 2027-1
```

Prueba el consolidado del periodo y todos los `.gs` por curso que encuentre. Termina en
`TODO OK` o en `HUBO FALLOS` con la lista.

## Archivos

| Archivo | Qué es |
|---|---|
| `google-mock.js` | Simulacro de `CalendarApp`, `Calendar` (servicio avanzado), `Logger`, `Utilities`. Cuenta invitaciones, cancelaciones y escrituras, y permite torcer cosas a propósito. |
| `probar.js` | 94 comprobaciones sobre el `.gs` consolidado. |
| `probar_curso.js` | 12 comprobaciones sobre un `.gs` de un solo curso. |
| `probar.sh` | Corre todo. |

## Qué comprueba, y por qué eso

Lo que se prueba son las promesas que el manual le hace al docente:

- **«Volver a ejecutar no duplica».** Se crea la serie, se vuelve a crear, y se cuenta:
  mismos eventos, cero invitaciones nuevas, mismos enlaces de Meet.
- **«Una sala por sesión».** 48 salas distintas para las 48 sesiones sincrónicas; las 4
  autónomas quedan en el calendario sin Meet ni enlace en Ubicación.
- **«Si llegó una nómina nueva, `crear` invita a quien falta».** Se agrega un estudiante y se
  verifica que entra en las 13 sesiones de su curso y que reejecutar no lo invita dos veces.
- **Un estudiante retirado NO se va solo.** Es una limitación real: el script solo agrega
  invitados. Está probada para que quede constancia, y el manual dice que hay que quitarlo a
  mano.
- **El borrado no se lleva nada ajeno.** Bases de Datos II y Arquitectura caen los dos en
  lunes: se borra uno y se comprueba que el otro sigue entero. Y un evento personal del
  docente que mencione el curso a otra hora sobrevive.
- **Los dos interruptores frenan.** `SIMULAR = true` no toca nada; `CONFIRMO_SEMESTRE_COMPLETO`
  bloquea las funciones que abarcan los 4 cursos, y las de un curso suelto no lo necesitan.
- **Cortarse por tiempo no pierde nada.** Con el plazo vencido no crea nada y avisa; al
  reejecutar completa las 52.
- **Los caminos que fallan.** Sin servicio avanzado de Calendar (crea eventos, sin Meet), sala
  de Meet que viene «pending», `deleteEvent` que falla (reporta `Eliminados=0`, no éxito
  falso), `addGuest` sin cuota, `CALENDAR_ID` vacío o inexistente.

## Los defectos que salieron de aquí

Vale la pena dejarlos escritos, porque todos parecían inofensivos leyendo el código. Los dos
primeros los encontró este arnés; los cuatro siguientes, una auditoría por lectura estática, y
cada uno tiene ya su prueba aquí para que no vuelva.

1. **`_buscarEvento_` dependía de `search`.** Usaba el parámetro `search` de
   `getEvents(...)`, que es la búsqueda de texto de Google. Los títulos llevan
   `[SINCRONICO]`, `·` y tildes; si esa búsqueda no casa, la función devuelve `null` con el
   evento delante, el script lo considera inexistente y **crea un duplicado**, con una
   segunda invitación para todo el grupo. Ahora enumera el día y compara el título exacto.
2. **El barrido de huérfanos alcanzaba los eventos personales del docente.** Borraba cualquier
   evento del día cuyo título mencionara el curso — «Preparar quiz de Bases de Datos II»
   incluido. Ahora exige además que empiece **a la hora de la sesión**, que es donde está un
   evento de una corrida anterior (lo que le cambió fue el título, no el horario).
3. **`TZ` se declaraba y nunca se usaba.** La hora de los eventos la construye Apps Script con
   la zona del **proyecto**; `var TZ = 'America/Bogota'` era una línea muerta. Un proyecto en
   UTC o en `America/New_York` metía los 52 eventos corridos, con las invitaciones enviadas y
   sin forma de arreglarlo reejecutando. Y era indetectable con las herramientas del propio
   script: `verificar` imprimía `s.ini` (la cadena `'18:00'` del array), no la hora real del
   evento. Ahora `verificar` compara con `Session.getScriptTimeZone()` y **crear y borrar se
   bloquean** si no coincide.
4. **Un título cambiado generaba una serie entera al lado de la vieja.** La única llave de
   identidad es el título exacto, y el título codifica lo que el JSON cambia (prefijo
   `[SINCRONICO]`/`[AUTONOMO]`, `Sesión N` vs `Parcial N`). Lo grave era que el manual
   prescribía justo eso —«marca el parcial en el JSON y ejecuta `crearEncuentros`»—, y el log
   decía «1 creado · 12 ya existían» sin una línea de alerta. Ahora `crear` mira si ya hay un
   encuentro del curso en ese hueco con otro título, **no crea** y lo cuenta como omitido.
5. **El `continue` de `_eliminar_` apagaba el barrido justo cuando hacía falta.** El barrido de
   huérfanos solo corría si la pasada por título exacto no había encontrado nada ese día —
   pero el caso para el que existe es precisamente el contrario: el evento con el título
   **nuevo** ya está, y el viejo sigue al lado. El log afirmaba «Huerfanos: 0» con 13 eventos
   muertos en el calendario de los estudiantes. Ahora barre siempre; el filtro de hora y de
   nombre del curso ya garantizan que no alcanza nada ajeno.
6. **El aviso de corte daba un consejo destructivo.** Decía «vuelve a ejecutar la misma
   función», que sirve para `crear*` pero no para `recrear*`: reejecutarla borra otra vez lo que
   acababa de recrear, con una cancelación por invitado y por evento. Ahora el aviso **nombra**
   la función con la que continuar y, si la que se cortó era destructiva, advierte de no
   repetirla.

Y una más, de la misma auditoría: **`_eliminar_` solo miraba las fechas del `.gs` actual**, así
que una sesión movida o quitada del JSON dejaba un evento que ninguna función podía encontrar
—y el manual mandaba usar `recrearTodo`, que tampoco lo veía—. Ahora hay una tercera pasada
por todo el periodo (`Fantasmas`), acotada a la hora del curso.

## Lo que estas pruebas NO cubren

El simulacro es fiel a lo que el script necesita, no a Google. Queda sin verificar y solo se
comprueba ejecutando de verdad con `SIMULAR = true`:

- Si `Calendar.Events.patch` con `conferenceData.createRequest` devuelve la **misma** sala para
  un `requestId` repetido (el simulacro asume que sí, que es lo documentado).
- Los tiempos reales y las cuotas de Calendar: los volúmenes de correos que cita el manual son
  aritmética (eventos × invitados), no envíos observados.
- Si `CalendarApp.createEvent` con `sendInvites: true` manda exactamente una invitación.
- **Qué zona horaria asigna Google a un proyecto nuevo** con esta cuenta institucional, y
  cuánto se desplazan los eventos en la práctica. Que `new Date(y,m,d,h,min)` use la zona del
  proyecto es lo documentado, y el guardia se prueba aquí torciendo `Session`; el desfase real
  no se ha medido.
- El estado del calendario **de verdad**: si hoy ya hay eventos previos, duplicados o
  fantasmas. Eso solo se ve con `verificar*` en `SIMULAR = true`, o abriendo Calendar.

Por eso el manual insiste en correr `verificar` con `SIMULAR = true` antes de nada.
