# Solución Taller Clase 1 — Arranque VetCare

> DOCUMENTO DOCENTE — PRIVADO. No publicar en Clases/.

**Resumen:** ER minimo Dueño-Mascota-Cita + 3 reglas + alcance.

## Alineacion
- Taller: `Clases/Clase 1 - Revision BD I y arranque VetCare/Taller PI - Clase 1 - VetCare.docx`
- Hito: Arranque PI: dominio, alcance y borrador ER de VetCare DB
- Entregable: Ficha del PI (plantilla) + ER en Mermaid renderizado en ExamLab (PNG para tu carpeta) + 3 reglas Condicion -> Accion

## Solucion paso a paso
1. Trabajo individual por defecto: nombra tu proyecto VetCare - [Apellido] y registralo para identificarlo en todas las entregas del semestre. Si el docente autoriza equipo de 2 o 3, el artefacto puede ser compartido pero la entrega en ExamLab sigue siendo individual.
2. Listar las entidades minimas del dominio: Dueño (persona que trae la mascota), Mascota (paciente), Veterinario (quien atiende), Cita (agenda de una atencion). Consulta, Insumo y DetalleFactura se agregan en clases posteriores.
3. Redactar 3 reglas de negocio propias en formato Condicion -> Accion, cada una con el mecanismo con que se implementara (CHECK, UNIQUE, FK, procedimiento o trigger): "una mascota con activa=N no puede tener una cita nueva", "el stock de un insumo nunca puede quedar en negativo", "toda cancelacion de cita queda registrada con usuario y fecha".
4. Dibujar el ER borrador marcando cardinalidad en cada relacion (Dueño 1-N Mascota, Mascota 1-N Cita) en Excalidraw o draw.io, pasarlo a Mermaid (erDiagram) con ayuda de una IA y pegarlo en la pregunta 2 de ExamLab verificando que renderice; el PNG exportado va a la carpeta del PI, pero lo que califica es el Mermaid renderizado.
5. Escribir el alcance en dos listas explicitas: que SI cubre el PI este semestre (agenda, facturacion basica, roles) y que NO cubre (ej. pagos en linea, historial clinico completo) para evitar scope creep en clases futuras.

## Ejemplo / SQL / artefactos
- DDL: Kit docente/Clase 1/Codigo/01_arranque_vetcare.sql
- ER: Dueño 1-N Mascota; Mascota 1-N Cita.
- Script demo: `Kit docente/Clase 1/Codigo/01_arranque_vetcare.sql`

## Rubrica corta
- [ ] Registro del proyecto (1)
- [ ] ER (3)
- [ ] Reglas (2)
- [ ] Alcance (2)
- [ ] Entrega (2)

## Errores frecuentes
- ER genérico.
- Sin FK.
- Scope infinito.
- Entregar el PNG y dejar vacía la pregunta de diagrama: ExamLab califica el Mermaid renderizado, no la imagen.
- Reglas escritas como deseos («el sistema debe ser seguro») en vez de Condición → Acción verificable.
- Nombres en mayúscula, plural o con tilde: el DDL falla en el PostgreSQL de ExamLab y se pierde la clase depurándolo.

Entrega en ExamLab.
