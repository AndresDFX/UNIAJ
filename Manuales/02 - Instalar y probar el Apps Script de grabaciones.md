# 02 — Instalar y probar el Apps Script de grabaciones

Procedimiento **general**: se instala una vez por cuenta y sigue sirviendo en los periodos
siguientes. Solo hay que revisarlo si cambian las carpetas de Drive o los horarios.

**Qué logra:** que las grabaciones de Meet dejen de acumularse en `Meet Recordings` y
aparezcan solas en la carpeta **Clases grabadas** del curso correcto.

**Dónde vive el código:** `config/calendario/apps_script_grabaciones/MoverGrabaciones.gs`.
Ese archivo es la **copia versionada**; el que se ejecuta es el que pegues en tu cuenta de
Google. **No se sincronizan entre sí.**

---

## Qué hace, en una frase

Cada pocas horas revisa la carpeta donde Meet deja las grabaciones y mueve lo nuevo (video,
transcripción, chat) a la carpeta de grabaciones del curso al que pertenece.

> **Paso previo:** los encuentros del curso tienen que **existir en tu Calendar**. Es el
> criterio principal con el que este script identifica de qué clase es cada grabación, así
> que hazlo antes: **[manual 01](01%20-%20Alistar%20un%20curso%20%28encuentros%2C%20Meet%2C%20correo%20e%20invitaciones%29.md)**.
> Sin la serie creada, las grabaciones saldrán como *(sin curso)* y se quedarán quietas.

Para decidir el curso usa tres criterios en orden:

1. **El evento de calendario** que se solapa con la hora de la grabación. Es el fiable,
   porque los eventos se llaman `[SINCRONICO] Sesión N · <Curso>`. Busca de −3 h a +1 h,
   porque el archivo se crea **al terminar** la reunión, no al empezar.
2. **El nombre del archivo**, si menciona el curso, su código `FI######` o un alias.
3. **El horario fijo** del curso (día de la semana + ventana de hora), como último recurso.

Si ninguno resuelve, **no mueve nada** y lo anota en el log. Es deliberado: las carpetas de
grabaciones están compartidas con estudiantes, así que dejar un archivo quieto es mejor que
publicarlo en el curso equivocado.

---

## Instalación (una sola vez)

1. Entra a **https://script.google.com** con tu cuenta institucional → **Nuevo proyecto**.
2. Ponle un nombre reconocible, p. ej. `Grabaciones UNIAJC`.
3. Borra el contenido de `Código.gs` y pega **todo** `MoverGrabaciones.gs`.
4. Guarda (💾).

### 5. Pega el ID del calendario

Arriba del `.gs` hay una constante que **sale vacía a propósito**:

```js
const CALENDAR_ID = '';   // <- pega aquí el ID del calendario
```

Tiene que ser **el mismo** que pusiste en el script de encuentros
([manual 01](01%20-%20Alistar%20un%20curso%20%28encuentros%2C%20Meet%2C%20correo%20e%20invitaciones%29.md)):
este script identifica cada grabación buscando el encuentro que había a esa hora, así que si
mira otro calendario no encuentra nada y deja todo sin clasificar.

No se usa el calendario "por omisión" porque depende de la cuenta con la que se abrió Apps
Script. Para obtener el ID: ejecuta **`listarCalendarios`** (imprime cada calendario con su
ID y marca el por omisión), o en Google Calendar → **⋮** sobre el calendario →
**Configuración y uso compartido** → **«Integrar calendario»** → **«ID de calendario»**.

Si prefieres el por omisión, la línea está comentada dentro de `_cal_()`: descoméntala y deja
`CALENDAR_ID` vacío.

### 6. Verifica el calendario y las carpetas

Ejecuta la función **`verificarCarpetas`** y abre el registro (**Ver → Registro de
ejecución**).

La primera ejecución pide permisos: Google mostrará una advertencia de "app no verificada"
porque el script es tuyo y no está publicado. Es esperado — entra en **Configuración
avanzada → Ir a (nombre del proyecto)** y acepta. Los permisos son sobre **tu propio** Drive
y Calendar; el script no accede a nada de nadie más.

Debe salir una línea `OK    calendario -> …` y tantas `OK` como cursos. Si el calendario
dice `ERROR`, revisa el `CALENDAR_ID`; si una carpeta dice `ERROR … no accesible`, ese id está
mal o la carpeta no es tuya.

### 7. Ensaya sin mover nada

Ejecuta **`simulacro`** y revisa el registro. Lista, archivo por archivo, a qué curso iría:

```
Arquitectura … 2026/08/24 … Grabación  ->  Arquitectura de Sistemas Computacionales
Reunión sin título …                   ->  (sin curso)
```

**Este paso es la prueba de verdad.** Que el código esté escrito no garantiza que Meet nombre
los archivos como se espera en tu cuenta. Si hay grabaciones recientes y todas salen
`(sin curso)`, algo no coincide: ver *Si deja de funcionar*.

Si aún no tienes grabaciones, haz una reunión de prueba de un minuto en Meet, grábala, espera
a que Drive la procese (puede tardar) y vuelve a correr `simulacro`.

### 8. Actívalo

Cuando el simulacro se vea bien, ejecuta **`instalarDisparador`** una vez. Desde ahí corre
solo cada 6 horas. Para apagarlo: **`desinstalarDisparador`**.

---

## Ajustes

| Constante | Para qué |
|---|---|
| `CURSOS` | Un objeto por curso: carpeta destino, día, ventana horaria y alias |
| `CALENDAR_ID` | ID del calendario con los encuentros. **El mismo del manual 01** |
| `NOMBRES_CARPETA_MEET` | Nombres posibles de la carpeta de Meet (cambia con el idioma de la cuenta) |
| `DIAS_ATRAS` | Cuántos días atrás revisa en cada corrida |
| `SIMULACRO` | `true` = no mueve nada, solo registra |

Los ids de carpeta salen de `config/calendario/semestre_<periodo>.json` →
`cursos.<curso>.carpetas_drive.grabadas.id`, la misma fuente que usa el correo de bienvenida.
`validar_calendario.py` comprueba que los ids del `.gs` coincidan con el JSON, así que si
cambias una carpeta y actualizas solo uno de los dos, la validación lo avisa.

**Si editas el `.gs` en el repo, hay que volver a pegarlo en tu cuenta.**

---

## Si deja de funcionar

Primero: **abre el registro de ejecuciones** en script.google.com (**Ejecuciones**, en el
menú lateral). Casi siempre lo dice ahí.

| Síntoma | Causa probable | Arreglo |
|---|---|---|
| `no encontré la carpeta de grabaciones de Meet` | Drive la llama distinto en tu idioma, o Meet cambió el nombre | Agrega el nombre exacto a `NOMBRES_CARPETA_MEET` |
| Todo sale `(sin curso)` | El nombre del archivo cambió y no hay evento de calendario que coincida | Revisa que los eventos del curso estén en tu calendario principal; agrega un alias al curso |
| `Falta CALENDAR_ID` / `CALENDAR_ID no corresponde a un calendario visible` | No pegaste el id, o está mal | Ejecuta `listarCalendarios()` y copia el correcto |
| `No pude leer el calendario` | El `CALENDAR_ID` apunta a un calendario que esta cuenta no ve | Verifica con `listarCalendarios()` que el id esté en la lista |
| Mueve al curso equivocado | Dos cursos comparten día y ventana horaria | Ajusta `desde`/`hasta`, o añade un alias más específico |
| Dejó de correr solo | El disparador se borró o falló varias veces seguidas | Ejecuta `instalarDisparador` otra vez |

---

## Limitaciones

- **No se probó de extremo a extremo desde el repo**: requiere tu cuenta de Google y
  grabaciones reales. La lógica está escrita y revisada, pero el primer `simulacro` es la
  validación real. Hazlo antes de activar el disparador.
- **Mueve, no copia**: la grabación deja de estar en `Meet Recordings`.
- Meet cambia de vez en cuando el nombre de la carpeta y el formato del nombre de archivo.
  Cuando pase, el log lo dice y se arregla con un alias o un nombre nuevo en la constante.
- Los dos scripts (encuentros y grabaciones) tienen que apuntar al **mismo**
  `CALENDAR_ID`. Es el error más fácil de cometer y el log lo delata: todo sale
  *(sin curso)*.
- Si el disparador corre cada 6 h, una grabación puede tardar hasta ese tiempo en aparecer
  en la carpeta del curso. Si necesitas que esté ya, ejecuta `moverGrabaciones` a mano.
