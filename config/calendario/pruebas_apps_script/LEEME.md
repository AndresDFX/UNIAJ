# Pruebas de los Apps Script de encuentros

Los `.gs` que genera `generar_apps_script_encuentros.py` corren en Google, contra el
calendario de verdad. Los eventos son bloques del calendario del docente: **no llevan
invitados y no envían correos**. Un error ahí sigue costando caro: 102 eventos creados o
borrados de golpe, y con ellos las salas de Meet cuyos enlaces ya se habían compartido.

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
| `google-mock.js` | Simulacro de `CalendarApp`, `Calendar` (servicio avanzado), `Logger`, `Utilities`. Cuenta invitaciones, cancelaciones, llamadas a `addGuest` y escrituras (todas deben quedar en cero), y permite torcer cosas a propósito. |
| `probar.js` | 121 comprobaciones sobre el `.gs` consolidado. Las cifras (cursos, sesiones, salas) las lee del `.gs`, no están cableadas — salvo el bloque 24, que las contrasta con los JSON. |
| `probar_curso.js` | 22 comprobaciones sobre un `.gs` de un solo curso — 24 cuando el rango del curso es más estrecho que el del periodo por **los dos** extremos (hoy solo SB141B: arranca el 03/09 y cierra el 17/12). Corre sobre los 7. |
| `probar.sh` | Corre todo. |

## Qué comprueba, y por qué eso

Lo que se prueba son las promesas que el manual le hace al docente:

- **«Volver a ejecutar no duplica».** Se crea la serie, se vuelve a crear, y se cuenta:
  mismos eventos, mismos enlaces de Meet.
- **«Una sala por sesión».** 96 salas distintas para las 96 sesiones sincrónicas; las 6
  autónomas quedan en el calendario sin Meet ni enlace en Ubicación.
- **«No invita a nadie y no manda correos».** Es la promesa central. Se comprueba en las tres
  rutas (crear, reejecutar, borrar) que ningún evento acaba con invitados, que el contador de
  invitaciones y de cancelaciones del simulacro se queda en cero, y que el `.gs` **nunca llama
  a `addGuest`** (el simulacro cuenta las llamadas, así que no se supone: se mide).
- **Están los 7 cursos, ni uno menos.** El resto de las pruebas deriva sus cifras del propio
  `.gs`, que es lo correcto para no cablear números que cambian cada semestre — pero eso deja un
  hueco: si el generador dejara de emitir un curso, los totales bajarían con él y todo seguiría
  en verde. El bloque 24 cuenta contra los **dos JSON** (`semestre_2026_2.json` +
  `introduccion_ingenieria_2026_2.json`): 7 cursos, 102 sesiones, 6 autónomas, y curso por curso
  con su grupo y su número de sesiones, para que el fallo diga *cuál* falta.
- **Ni un dato de estudiante en el `.gs`.** El bloque 25 mira el texto del archivo —que es lo
  que de verdad se pega en el editor de Apps Script— y exige que no haya ni un
  `@estudiante.uniajc.edu.co`, ni `ATTENDEE`, ni `addGuest`, ni `sendUpdates: 'all'`. Los únicos
  correos admitidos son el del docente y el del calendario. El `.gs` sigue en `_privado/` por
  historia, no porque le quede PII.
- **Los tres grupos de FI300101 no se pisan.** Comparten código y asignatura; lo que los
  distingue es el grupo dentro del título más el flag `codigoCompartido`. Se crean los 7 cursos,
  se borra un grupo y se comprueba que los otros dos siguen enteros.
- **Un evento ajeno del docente CON invitados no se toca.** Una reunión con gente invitada, el
  mismo día del encuentro y a otra hora, sobrevive al barrido y no pierde ni gana invitados.
- **El borrado no se lleva nada ajeno.** Bases de Datos II y Arquitectura caen los dos en
  lunes: se borra uno y se comprueba que el otro sigue entero. Y un evento personal del
  docente que mencione el curso a otra hora sobrevive.
- **El barrido de fantasmas no se sale del rango DEL CURSO.** `INICIO`/`FIN` son la **unión** de
  los rangos del periodo (llegan a diciembre por FI300101), pero los otros cuatro cursos cierran
  el 22/11 y los grupos de FI300101 arrancan el 03/09. El bloque 26 de `probar.js` y su gemelo en
  `probar_curso.js` plantan un **apunte personal del docente** fuera del rango del curso pero
  dentro del global, con el nombre de la asignatura y **a la hora del curso** —el evento exacto
  que un barrido global se llevaría— y exigen que `eliminar*` no lo liste ni lo borre. Se prueba
  por comportamiento a propósito: que el objeto del curso traiga `inicio`/`fin` no dice nada
  sobre si `_fantasmas_` los usa.
- **Los dos interruptores frenan.** `SIMULAR = true` no toca nada; `CONFIRMO_SEMESTRE_COMPLETO`
  bloquea las funciones que abarcan los 7 cursos, y las de un curso suelto no lo necesitan.
- **Cortarse por tiempo no pierde nada.** Con el plazo vencido no crea nada y avisa; al
  reejecutar completa las 102.
- **Los caminos que fallan.** Sin servicio avanzado de Calendar (crea eventos, sin Meet), sala
  de Meet que viene «pending», `deleteEvent` que falla (reporta `Eliminados=0`, no éxito
  falso), `CALENDAR_ID` vacío o inexistente.

## Los defectos que salieron de aquí

Vale la pena dejarlos escritos, porque todos parecían inofensivos leyendo el código. Los dos
primeros los encontró este arnés; los cuatro siguientes, una auditoría por lectura estática, y
cada uno tiene ya su prueba aquí para que no vuelva.

1. **`_buscarEvento_` dependía de `search`.** Usaba el parámetro `search` de
   `getEvents(...)`, que es la búsqueda de texto de Google. Los títulos llevan
   `[SINCRONICO]`, `·` y tildes; si esa búsqueda no casa, la función devuelve `null` con el
   evento delante, el script lo considera inexistente y **crea un duplicado**, con una segunda
   sala de Meet. Ahora enumera el día y compara el título exacto.
2. **El barrido de huérfanos alcanzaba los eventos personales del docente.** Borraba cualquier
   evento del día cuyo título mencionara el curso — «Preparar quiz de Bases de Datos II»
   incluido. Ahora exige además que empiece **a la hora de la sesión**, que es donde está un
   evento de una corrida anterior (lo que le cambió fue el título, no el horario).
3. **`TZ` se declaraba y nunca se usaba.** La hora de los eventos la construye Apps Script con
   la zona del **proyecto**; `var TZ = 'America/Bogota'` era una línea muerta. Un proyecto en
   UTC o en `America/New_York` metía los 102 eventos corridos, y con ellos las salas de Meet
   ya compartidas, sin forma de arreglarlo reejecutando. Y era indetectable con las herramientas del propio
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
   muertos en el calendario. Ahora barre siempre; el filtro de hora y de
   nombre del curso ya garantizan que no alcanza nada ajeno.
6. **El aviso de corte daba un consejo destructivo.** Decía «vuelve a ejecutar la misma
   función», que sirve para `crear*` pero no para `recrear*`: reejecutarla borra otra vez lo que
   acababa de recrear, y con ello las salas de Meet que acababa de pedir. Ahora el aviso **nombra**
   la función con la que continuar y, si la que se cortó era destructiva, advierte de no
   repetirla.

Y una más, de la misma auditoría: **`_eliminar_` solo miraba las fechas del `.gs` actual**, así
que una sesión movida o quitada del JSON dejaba un evento que ninguna función podía encontrar
—y el manual mandaba usar `recrearTodo`, que tampoco lo veía—. Ahora hay una tercera pasada
(`Fantasmas`) por el rango de fechas **del curso**, acotada a la hora del curso.

## Lo que estas pruebas NO cubren

El simulacro es fiel a lo que el script necesita, no a Google. Queda sin verificar y solo se
comprueba ejecutando de verdad con `SIMULAR = true`:

- Si `Calendar.Events.patch` con `conferenceData.createRequest` devuelve la **misma** sala para
  un `requestId` repetido (el simulacro asume que sí, que es lo documentado).
- Los tiempos reales y las cuotas de Calendar y de Meet con 102 eventos y 96 salas en una sola
  corrida: en el simulacro no hay cuota.
- Que Google, de verdad, **no notifique a nadie** al crear un evento sin `guests`. Es lo
  documentado y aquí se comprueba que el script no pasa invitados ni llama a `addGuest`; el
  comportamiento del servidor no se ha observado.
- **Qué zona horaria asigna Google a un proyecto nuevo** con esta cuenta institucional, y
  cuánto se desplazan los eventos en la práctica. Que `new Date(y,m,d,h,min)` use la zona del
  proyecto es lo documentado, y el guardia se prueba aquí torciendo `Session`; el desfase real
  no se ha medido.
- El estado del calendario **de verdad**: si hoy ya hay eventos previos, duplicados o
  fantasmas. Eso solo se ve con `verificar*` en `SIMULAR = true`, o abriendo Calendar.

Por eso el manual insiste en correr `verificar` con `SIMULAR = true` antes de nada.
