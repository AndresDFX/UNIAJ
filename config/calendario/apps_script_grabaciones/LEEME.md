# Mover grabaciones de Meet a la carpeta del curso

`MoverGrabaciones.gs` es un **Google Apps Script**: corre dentro de tu cuenta de Google
(la institucional `@profesores.uniajc.edu.co`), no en este repo ni en un servidor. Este
archivo es la copia versionada; **hay que pegarlo en tu cuenta una vez**.

## Qué hace

Cada 6 horas revisa la carpeta donde Meet deja las grabaciones (`Meet Recordings` /
`Grabaciones de Meet` en Mi unidad) y mueve lo nuevo a la carpeta **Clases grabadas** del
curso que corresponde. Mueve el video y también lo que Meet crea al lado
(transcripción, chat, notas).

Para decidir el curso usa tres criterios, en orden:

1. **El evento del calendario** que se solapa con la hora de la grabación. Es el método
   fiable, porque los eventos del semestre ya se llaman `[SINCRONICO] Sesión N · <Curso>`.
   Busca en una ventana de −3 h a +1 h, porque el archivo se crea **al terminar** la
   reunión, no al empezar.
2. **El nombre del archivo**, si menciona el curso, su código `FI######` o un alias.
3. **El horario fijo** del curso (día de la semana + ventana de hora). Último recurso, para
   grabaciones de reuniones sin evento.

Si ninguno resuelve, **no mueve nada** y lo anota en el log. Preferible a adivinar y
mandar una grabación al curso equivocado, que además es una carpeta compartida con
estudiantes.

## Instalación (una vez)

1. Entra a https://script.google.com con tu cuenta institucional → **Nuevo proyecto**.
2. Ponle nombre, p. ej. `Grabaciones UNIAJC`.
3. Borra el contenido de `Código.gs` y pega **todo** `MoverGrabaciones.gs`.
4. Guarda (💾).
5. Ejecuta la función **`verificarCarpetas`** y mira el log (`Ver → Registro`). Google
   pedirá permisos la primera vez: acéptalos (Drive y Calendar de tu propia cuenta).
   Las 4 líneas deben decir `OK`. Si alguna dice `ERROR ... no accesible`, revisa el id.
6. Ejecuta **`simulacro`**. No mueve nada: solo lista qué archivo iría a qué curso.
   Revisa que la asignación tenga sentido.
7. Cuando el simulacro se vea bien, ejecuta **`instalarDisparador`** una vez. Desde ahí
   corre solo cada 6 horas.

Para apagarlo: ejecuta `desinstalarDisparador`.

## Ajustes

| Constante | Para qué |
|---|---|
| `CURSOS` | Un objeto por curso: carpeta destino, día, ventana horaria y alias |
| `NOMBRES_CARPETA_MEET` | Si tu Drive llama distinto a la carpeta de grabaciones, agrégalo |
| `DIAS_ATRAS` | Cuántos días atrás revisar en cada corrida (por defecto 7) |
| `SIMULACRO` | `true` = no mueve nada, solo registra. Útil para depurar |

## Los ids de carpeta

Salen de `config/calendario/semestre_2026_2.json` →
`cursos.<curso>.carpetas_drive.grabadas.id`, que es la misma fuente que usa el correo de
bienvenida. `validar_calendario.py` comprueba que los ids del `.gs` coincidan con el JSON,
así que si cambias una carpeta y actualizas solo uno de los dos, la validación lo avisa.

**Ojo:** si cambias el `.gs` aquí, hay que **volver a pegarlo** en tu cuenta. Este archivo
no se sincroniza con Apps Script.

## Limitaciones honestas

- No pude probarlo end-to-end: requiere tu cuenta de Google y grabaciones reales. La lógica
  está escrita y revisada, pero **el primer `simulacro` es la prueba de verdad** — hazlo
  antes de instalar el disparador.
- Meet cambia de vez en cuando el nombre de la carpeta y el formato del nombre de archivo.
  Si un día deja de mover, revisa el log: casi siempre es eso, y se arregla agregando el
  nombre nuevo a `NOMBRES_CARPETA_MEET` o un alias en el curso.
- El script usa `CalendarApp.getDefaultCalendar()`. Si los eventos del curso los pones en
  un calendario secundario, hay que cambiarlo por `CalendarApp.getCalendarById('...')`.
- Mueve, no copia: la grabación deja de estar en `Meet Recordings`.
