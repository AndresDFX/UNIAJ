# Definición de terminado · material de una clase

Criterios de aceptación **vinculantes** para el material de cualquier clase de UNIAJC.
No son una guía de estilo: una clase que no los cumpla no está terminada, aunque el build
pase y los archivos existan. Clases de referencia: **ARQ Clase 1** y **BD II Clase 2**.

## Orientación mínima del repo

Los `.pptx` y `.docx` son **generados** desde `config/slides/*.py`. Nunca se editan a mano:
se cambia el dato o el generador y se regenera. Los conflictos de merge en material generado
se resuelven regenerando, nunca eligiendo un lado.

## 0. Criterio rector

**Nada se evalúa que no se haya enseñado, y nada se enseña que no se use.**

Es el defecto que ha aparecido tres veces, y siempre valía puntos:

| Caso | Puntos evaluados | Enseñanza previa |
|---|---|---|
| ARQ C1 · nube vs on-premise | 35 de 100 | 2 menciones, ninguna diapositiva |
| BD II C2 · vistas y privilegio por columna | 20 de 100 | ninguna |
| BD II C1 · la clínica Huellitas | dominio de todo el PI | 1 mención antes de abrir ExamLab |

Prueba concreta: por **cada** pregunta de la actividad debe existir la diapositiva donde se
proyectó el mecanismo que la resuelve. Si no existe, **falta la diapositiva** — no sobra la
pregunta.

## 1. Inventario de archivos

Ocho artefactos en dos carpetas con audiencia distinta.

`Clases/Clase N/` — lo que ve el estudiante:
- `Presentacion.pptx`
- `Taller ... .docx`

`Kit docente/Clase N/`:
- `Guion Docente ... .md` + `.docx`
- `Quiz ... .docx` (estudiante) y `Quiz ... - CLAVE DOCENTE.docx`
- `Solucion Taller ... .md` + `.docx`
- `Taller en ExamLab - Clase N (configuracion).md`
- `Capturas/` con la imagen de la demo · en BD II además `Codigo/` con el script ejecutable

Solo la Clase 1 lleva `Prueba Diagnostica`. En `config/slides/`, la clase debe tener entrada
en los cuatro módulos de datos: `*_examlab_data.py`, `*_fundamentos.py`, `*_solucion_data.py`,
`*_taller_data.py`.

## 2. Guion docente

- **Teoría dividida por diapositiva**: cada sección `###` anclada con `{{slide:Fragmento}}`.
  No «ver la presentación», sino *qué se dice mientras esa diapositiva está en pantalla*. Es lo
  que hace que el guion sirva a un docente que no domina el tema.
- Los tokens **resuelven a números reales**; si el fragmento desaparece el build aborta, así que
  no puede publicarse un guion mal numerado.
- Cubre el **bloque completo** minuto a minuto, y el reparto de minutos coincide con los
  conceptos del deck.
- Cierra con **«Errores típicos del docente que no domina el tema»** y **preguntas frecuentes
  del grupo**.
- El fuente del fundamento va **sin acentos** (convención del archivo; `«»` sí). Cero
  marcadores crudos en la salida.

Referencia de tamaño: BD II C2 quedó en 15 secciones ancladas a las diapositivas 4–15, de
11.9k a 23.9k caracteres.

## 3. Solución docente

- **Resuelve los entregables en el mismo archivo**, no los describe: SQL que corre tal cual,
  matriz completa, diagrama, veredicto redactado.
- **Salida esperada** del motor, para comparar contra la captura del estudiante sin ejecutar
  nada.
- **Desglose de puntos** por pregunta, que suma el total de la propuesta del curso (100 por
  actividad, 25 % de peso por clase) — **no** lo que muestra ExamLab.
- **Errores frecuentes y qué hacer con ellos**: decisiones de calificación tomadas de antemano.
- En preguntas cerradas, **justificación de todas las opciones**, y la clave **leída del banco**,
  nunca copiada — así la solución no puede quedar marcando una opción que en la plataforma ya
  cambió.
- `nota_actividad` cuando hay una trampa que le cuesta puntos al docente.
- Marcada como **privada**, no publicada en `Clases/`.

## 4. Taller del estudiante (ficha del PI)

El `Taller ... .docx` de `Clases/Clase N/` no describe la actividad: **la deja lista para
llenar.**

- **Plantilla en blanco de cada entregable**, con su estructura real. Si se pide una matriz, va
  la tabla con sus encabezados y sus filas vacías. Si se pide una ficha, van sus bloques como
  campos. Si se pide un documento de una página, van sus secciones. Enumerar la estructura en una
  línea de prosa («Plantilla ficha (5 bloques): DOMINIO · PROBLEMA · …») **no** es una plantilla.
- **Es el corolario del criterio rector aplicado al formato:** si el formato del entregable se
  califica —«matriz de 10 objetos × 4 roles»— entonces el formato se entrega, no se adivina. Un
  estudiante que pierde puntos por la forma de la tabla perdió puntos por algo que nunca se le dio.
- **Los nombres de la plantilla son los exactos de la actividad y de la solución**, mayúsculas
  incluidas. Un `VETERINARIO` en el taller y un `veterinario_rol` en la pregunta son dos
  entregables distintos.
- **El checklist de pistas cubre todas las preguntas**, no las primeras. Sigue siendo checklist
  vacío: sin solución.
- **Nada obsoleto sobrevive aquí.** Es el documento que más se olvida al corregir la clase: si se
  cambió el motor, la herramienta o un nombre de rol, este archivo también cambió.

## 5. Actividad de ExamLab

- **Máximo 5 preguntas**, 100 puntos, tipos que el motor sabe calificar.
- **Consistente consigo misma.** Fue el defecto de BD II C2: la P1 daba privilegios sobre 5
  tablas y la P4 exigía una matriz de 10 objetos coherente con ellos. Ningún error del motor
  lo delataba.
- **Salida determinista.** Si una consulta de verificación puede devolver distinto número de
  filas, se acota; si depende de la versión del motor, se declara el rango con su razón y se
  instruye no descontar.
- **Nada técnicamente falso**, ni siquiera al justificar un nombre.
- Espejada en `*_examlab_data.py`: la plataforma no es alcanzable desde aquí.
- Al cerrar la clase, **reportar qué pregunta cambió, cuál se añadió y cuál se retiró**. Es un
  checklist accionable para el docente, porque ExamLab no importa preguntas desde archivo.

## 6. Coherencia transversal

- **La herramienta anunciada es la que se usa y donde se califica.** ExamLab corre PostgreSQL
  (PGlite en el navegador) y no puede correr Oracle. Las menciones a Oracle que enseñan algo
  (niveles de aislamiento, portabilidad) se quedan como contraste explícito.
- Nomenclatura estable: **Huellitas** es el cliente, **VetCare DB** la base de datos.
- Modalidad correcta: **virtual síncrona (Meet)**, incluidos los parciales. Nunca «presencial».
- El amarre con el Proyecto Integrador y con las clases vecinas, dicho explícitamente.
- El build pasa: `_verificar_mapa()`, el resolutor de `{{slide:…}}` y
  `config/calendario/validar_calendario.py`.
- **Cero marcadores crudos** (`@@`, `**`, `{{slide`, `[CAP:`, `[[captura:`) en lo que ve el
  estudiante.

## 7. Cierre

Reporte de cambios de preguntas, y commit con mensaje de **una línea**.

---

## Lo que ningún script cubre

El verificador comprueba la mecánica (guion vs deck, rango de `[Slide N]`, marcadores crudos,
imagen de demo, contextualización del cliente, modalidad, anexo del caso). **El criterio rector
y la consistencia entre preguntas se revisan leyendo pregunta por pregunta** — ahí salieron los
tres defectos de la tabla.

## Límite declarado

«Completa» **no** incluye *SQL ejecutado*: no hay PostgreSQL ni Docker disponibles en este
entorno. Las salidas esperadas se calculan a mano contra los datos sembrados. Es verificable por
lectura, no por ejecución, y así debe declararse al entregar.
