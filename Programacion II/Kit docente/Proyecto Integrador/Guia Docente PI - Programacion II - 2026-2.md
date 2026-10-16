# Guía docente — Proyecto Integrador · Programación II · 2026-2

**Privado docente** · No compartir en `Clases/`.

## Producto
**VetCare** — aplicación de escritorio en Java para la Clínica Veterinaria «Huellitas».
PI **compartido con Seminario de Sistemas**: mismo producto, distinto entregable
(aquí el software, allá los planos).

## Casos de matrícula
- **A** (ambas materias): aquí se califica el código; los diagramas se califican en Seminario.
- **B** (solo Prog II): el docente entrega los diagramas UML ya hechos; el estudiante programa.
- **C** (solo Seminario): no aplica en este curso.

## Hitos
Semestre acortado a **13 sesiones**; las carpetas de material siguen numeradas 1–15.
Toda entrega intermedia cierra el **domingo siguiente a la sesión, a las 11:59 p. m.**

| Sesión | Fecha | Material | Entrega | Cierre |
|---|---|---|---|---|
| S10 (doble) | 28/10 | Clases 11 + 12 | Avance de código + revisión cruzada e integración de módulos | dom 01/11/2026, 11:59 p. m. |
| S11 | 04/11 | Clase 13 | Excepciones y validaciones | dom 08/11/2026, 11:59 p. m. |
| S12 | 11/11 | Clase 14 | Versión final + ensayo | **paquete final:** dom 15/11/2026, 11:59 p. m. |
| S13 | 18/11 | Clase 15 | Sustentación 15 + 5 min (mismo día del Parcial 3) | — |

## Rúbrica (100 pts → 20% del Corte 3)
POO 20 · Estructuras de datos 15 · GUI 20 · Manejo de errores 15 · Persistencia 15 · Sustentación 15

## Errores frecuentes
- Herencia forzada solo para cumplir el requisito.
- GUI que no persiste: pedir siempre la prueba de cerrar y reabrir.
- `try-catch` vacío que oculta el error.
- Que uno solo del equipo haya programado todo → preguntas al azar a cualquier integrante en la sustentación.

## Entrega y sustentación

- **Plazo único:** domingo 15 de noviembre de 2026, 11:59 p. m., en ExamLab.
- **Un solo .zip** (máx. 50 MB) con esta forma —los estudiantes tienen la carpeta «Plantilla de entrega» ya armada—:

```
Equipo <nombre>.zip
├── LEEME.txt  ← integrantes, caso de matrícula y cómo se ejecuta
├── proyecto/
│   └── src/  ← todos los .java
├── datos/  ← el .csv o .txt con registros de prueba
└── Manual de usuario.docx  ← 1 a 2 páginas con capturas
```

- **Qué debe traer cada pieza:**
  - **LEEME.txt** — Nombre del equipo, integrantes, caso de matrícula (A o B) y los pasos para compilar y ejecutar.
  - **proyecto/src/** — La aplicación completa y que compila: clases del dominio, colecciones, ventanas, manejo de errores y lectura y escritura del archivo de datos. Sin carpetas de compilación (bin, out, target).
  - **datos/** — El archivo que la aplicación lee al arrancar y en el que guarda, con registros de prueba inventados.
  - **Manual de usuario.docx** — 1 a 2 páginas con capturas, en el orden de la plantilla: registrar, agendar, buscar, ver el historial y qué pasa con un dato mal escrito.
- **Enlace obligatorio:** el repositorio de GitHub con el mismo código, o la carpeta de Drive del equipo.
- **Proyecto en equipo de 4 a 5 integrantes (máximo 5)** — solo el proyecto: los demás entregables conservan su modalidad. **Cada integrante sube la entrega del equipo** desde su propia cuenta: el mismo .zip y el mismo enlace; una sola entrega por estudiante.
- **Sustentación:** miércoles 18/11/2026, en la última clase (mismo día del Parcial 3), por Meet: 15 minutos de exposición + 5 minutos de preguntas por equipo (turno de 20 minutos); hablan todos los integrantes.
- **Qué muestran:** la aplicación corriendo en vivo: registrar una mascota, buscarla por su ID, escribir un dato inválido sin que se cierre, y cerrar y volver a abrir para mostrar que los datos siguen ahí.

Enunciado del estudiante en `Clases/Proyecto Integrador/`.
