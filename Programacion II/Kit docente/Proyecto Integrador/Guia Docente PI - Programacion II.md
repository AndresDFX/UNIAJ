# Guía docente — Proyecto Integrador · Programación II

**Privado docente** · No compartir en `Clases/`.

## Producto
**VetCare** — aplicación de escritorio en Java para la Clínica Veterinaria «Huellitas».
PI **compartido con Seminario de Sistemas**: mismo producto, distinto entregable
(aquí el software, allá los planos).

## Casos de matrícula
- **A** (ambas materias): aquí se califica el código; los diagramas se califican en Seminario.
- **B** (solo Prog II): el docente entrega los diagramas UML ya hechos; el estudiante programa.
- **C** (solo Seminario): no aplica en este curso.

## Hitos (por clase del material)
Sin sesiones ni fechas: cambian cada semestre y están en el calendario (`config/calendario/`).

| Material | Foco |
|---|---|
| Clases 11 + 12 | Avance de código + revisión cruzada e integración de módulos |
| Clase 13 | Excepciones y validaciones |
| Clase 14 | Versión final + ensayo |
| Antes de la última clase | **Paquete final** en ExamLab, en la fecha y la hora que publique el docente |
| Clase 15 (la última) | Sustentación 15 + 5 min |

## Rúbrica (100 pts)
POO 20 · Estructuras de datos 15 · GUI 20 · Manejo de errores 15 · Persistencia 15 · Sustentación 15

## Errores frecuentes
- Herencia forzada solo para cumplir el requisito.
- GUI que no persiste: pedir siempre la prueba de cerrar y reabrir.
- `try-catch` vacío que oculta el error.
- Que uno solo del equipo haya programado todo → preguntas al azar a cualquier integrante en la sustentación.

## Entrega y sustentación

- **Plazo único:** el que publique el docente en ExamLab, el mismo para todos los grupos.
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
- **Proyecto en equipo** (el número de integrantes lo indica el docente cada semestre) — solo el proyecto: los demás entregables conservan su modalidad. **Cada integrante sube la entrega del equipo** desde su propia cuenta: el mismo .zip y el mismo enlace; una sola entrega por estudiante.
- **Sustentación:** en la última clase del curso, 15 minutos de exposición + 5 minutos de preguntas por equipo (turno de 20 minutos); hablan todos los integrantes.
- **Qué muestran:** la aplicación corriendo en vivo: registrar una mascota, buscarla por su ID, escribir un dato inválido sin que se cierre, y cerrar y volver a abrir para mostrar que los datos siguen ahí.

Enunciado del estudiante en `Clases/Proyecto Integrador/`.
