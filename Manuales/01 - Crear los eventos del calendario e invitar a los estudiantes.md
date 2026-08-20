# 01 — Crear los eventos del calendario e invitar a los estudiantes

Procedimiento **general**: sirve para cualquier periodo y cualquiera de los cursos. Donde
aparece `<periodo>` va la etiqueta del semestre (`2026-2`, `2027-1`, …) y donde aparece
`<Curso>` la carpeta del curso.

**Resultado:** una sesión = un evento en tu calendario, con los estudiantes del curso como
invitados, y el correo de bienvenida listo para enviar.

---

## Paso 0 — Regenerar y validar

```bash
python config/calendario/generar_semestre_<periodo>.py      # calendarios, correos, CSV
python config/calendario/generar_eventos_calendario.py      # .ics con invitados + nóminas
python config/calendario/validar_calendario.py              # debe terminar en OK
```

Todo sale de `config/calendario/semestre_<periodo>.json`, que es la **fuente de verdad**: si
una fecha está mal, se corrige ahí y se vuelve a correr, nunca a mano en los documentos.

El segundo script imprime por curso cuántos estudiantes hay y cuántos son **invitables**.
**Lee esa línea antes de seguir:** si dice `invitables: 13` de 16, esas 3 personas no van a
recibir la invitación (ver *Problemas frecuentes*).

---

## Paso 1 — Los eventos (sin datos de estudiantes)

Cada curso tiene su archivo en su propia carpeta de periodo:

```
<Curso>/Plan curso/<periodo>/eventos_calendario_<periodo>.csv
```

Es formato de importación de Google Calendar, **no lleva invitados** y es el que se
versiona. Sirve para tener los bloques del semestre en tu agenda:

1. Google Calendar → **⚙ Configuración → Importar y exportar → Importar**.
2. Elige el CSV, selecciona el calendario destino y **Importar**.
3. Repite con el archivo de cada curso.

Los títulos llegan con el tipo de encuentro al principio, que es lo primero que el
estudiante lee y lo único que necesita para saber si debe conectarse:

```
[SINCRONICO] Sesión N · <Curso>      → hay encuentro: presencial, virtual, parcial o sustentación
[AUTONOMO]   Sesión N · <Curso>      → no hay encuentro: trabajo guiado con fecha de cierre
```

---

## Paso 2 — Invitar a los estudiantes

Para invitar hace falta el `.ics`, que sí lleva la nómina y por eso vive fuera de git:

```
config/calendario/_privado_<periodo>/invitaciones_<curso>.ics
```

Se importa por el mismo menú del Paso 1. Cada evento queda con sus estudiantes como
invitados, tú como organizador y la zona horaria de Bogotá.

> **Lo que Google no hace:** al **importar**, Google Calendar **no envía** los correos de
> invitación. Los invitados quedan dentro del evento pero nadie recibe nada. Compruébalo:
> abre un evento e verás a los invitados como *"Sin confirmar"* sin que les haya llegado
> nada.

Tres caminos para que efectivamente les llegue:

**A. Abrir y guardar cada evento** — el más fiel al material.
Abre el evento → **Guardar** → Google pregunta *"¿Enviar correos de invitación?"* → **Enviar**.
Hay que hacerlo por evento; conserva el tema de cada sesión en el título.

**B. Un evento recurrente por curso** — el más rápido.
Crea un evento semanal con tantas repeticiones como sesiones tenga el curso, pega los
correos de `_privado_<periodo>/nomina_<curso>.csv` (columna `correo`) en *Invitados* y guarda
una sola vez. Pierdes el tema por sesión en el título; ese detalle queda en el cronograma y
en el correo de bienvenida.

**C. API de Google Calendar** con `sendUpdates=all`, que sí notifica al crear. Vale la pena
solo si vas a repetir el proceso cada semestre.

> Haz **A o B antes** de enviar el correo de bienvenida: así el estudiante ya encuentra las
> invitaciones en su calendario cuando lo lea.

---

## Paso 3 — Enviar el correo de bienvenida

```
<Curso>/Plan curso/<periodo>/CORREO_BIENVENIDA - <Curso> - <periodo>.md
```

Se genera solo y ya trae: fechas clave (incluida la **fecha de la primera clase**, que no
siempre coincide con el inicio del periodo), las carpetas de Drive del curso, el bloque de
ExamLab con acceso y material de apoyo, la explicación de `[SINCRONICO]` / `[AUTONOMO]` y la
petición al vocero de responder con su WhatsApp.

**Antes de enviar, completa lo único que el repo no puede saber:**

- [ ] La **contraseña temporal** de ExamLab (el correo deja el espacio en blanco).
- [ ] Que las carpetas de Drive estén **compartidas** con el grupo. El repo publica el
      enlace, no los permisos: si falta compartir, el estudiante ve "Solicitar acceso".

Destinatarios: columna `correo` de `_privado_<periodo>/nomina_<curso>.csv`. Ponlos en **CCO**
para no exponer los correos del grupo entre ellos.

---

## Cuando algo cambia

| Cambió | Qué hacer |
|---|---|
| Una fecha, un parcial, un festivo | Editar `semestre_<periodo>.json`, correr los 3 scripts del Paso 0 y **reimportar**. Reimportar **crea** eventos, no los reemplaza: borra primero los viejos del calendario. |
| Llegó una nómina nueva | Reemplazar el `.xls` en `<Curso>/Plan curso/<periodo>/`, correr `generar_eventos_calendario.py` y reimportar solo ese `.ics`. |
| Cambió una carpeta de Drive | Actualizar `carpetas_drive` en el JSON; si es la de grabaciones, actualizar también el Apps Script (ver manual 02). El validador avisa si divergen. |
| Arranca un periodo nuevo | Crear `Plan curso/<periodo nuevo>/`; el periodo anterior se queda donde está, no se borra. |

---

## Problemas frecuentes

**«invitables: 13» de 16 estudiantes.**
El export académico no trae correo institucional para algunos. Dos salidas: pedirlos a
Registro Académico (el script deja `pendientes_correo_<curso>.csv` con nombre y documento),
o agregar un correo alterno en `config/calendario/_correos_manuales.csv` con
`curso,documento,correo,nota` — el generador lo cruza por documento. Ese archivo es entrada
tuya, tiene datos personales y está fuera de git.

**Los estudiantes no recibieron nada.** Es lo esperado si solo importaste: ver Paso 2.

**Un estudiante dice que el link de Drive le pide acceso.** La carpeta no está compartida
con él.

**Importé dos veces y hay eventos duplicados.** Google no deduplica al importar. Borra el
rango en el calendario y vuelve a importar una vez.

**El script dice «es de otro periodo -> omitido».** Correcto: está ignorando una nómina que
cuelga de la carpeta de un periodo anterior.

**El validador falla.** Arréglalo antes de importar o enviar: los dos pasos publican cosas
de cara al estudiante, y corregir aquí es más barato que retirar invitaciones ya enviadas.
