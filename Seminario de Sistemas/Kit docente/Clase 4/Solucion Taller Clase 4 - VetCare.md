# Solucion Taller · Clase 4 · Metodologias agiles

> DOCUMENTO DOCENTE — PRIVADO. No publicar en Clases/.

## Solucion paso a paso
1. Backlog priorizado resuelto (primeros cinco): 1) Registrar paciente con sus datos basicos y su propietario, prioridad Alta, porque sin ficha digital se siguen extraviando las fichas de papel. 2) Buscar historial por nombre o documento, Alta, porque ataca directo el dolor de la busqueda lenta. 3) Registrar consulta con motivo, diagnostico y tratamiento, Alta. 4) Ver historia clinica completa del paciente, Media. 5) Reporte de consultas por mes y por especie, Media, porque es el dolor de las metricas pero solo tiene sentido cuando ya hay datos. Justificacion del primer item: sin registro de pacientes ninguna otra historia se puede usar, es la base de todo el flujo.
2. Historia resuelta con criterios: 'Como veterinaria de Huellitas quiero buscar la historia clinica de una mascota por nombre o por documento del dueño para atender la consulta sin ir al archivador'. Escenario feliz: Dado que Rocky esta registrado con el dueño CC 1.144.556, Cuando escribo Rocky y presiono Enter, Entonces veo la ficha con nombre, especie, edad y las ultimas tres consultas en menos de 3 segundos. Escenario alternativo: Dado que escribo un nombre que no existe, Cuando presiono Enter, Entonces veo el mensaje 'No se encontro el paciente' y el boton 'Registrar nuevo'. Escenario de ambiguedad: Dado que hay tres mascotas llamadas Rocky, Cuando busco por ese nombre, Entonces veo una lista con nombre del propietario para poder distinguirlas.
3. Definicion de Terminado resuelta para artefactos de diseño: 1) El diagrama esta hecho en draw.io y exportado a PDF. 2) Existe el mockup de la pantalla asociada en Figma o Penpot. 3) Los nombres de campos coinciden con el diccionario de datos. 4) Un compañero distinto al autor lo reviso y dejo comentario. 5) El cliente (docente en rol de Huellitas) dio visto bueno en la revision de sprint. Si falta uno solo de los cinco, la tarjeta NO pasa a Aprobado.
4. Plan de sprints resuelto: Sprint 1 (tres semanas) objetivo 'que la clinica pueda ver como se registra y se consulta una ficha', entregable: casos de uso de registro y consulta mas mockup navegable de la ficha del paciente. Sprint 2 objetivo 'que la busqueda quede resuelta de punta a punta', entregable: historias con criterios, diagrama de clases del modulo de historia clinica y prototipo de busqueda. Sprint 3 objetivo 'que la clinica vea sus numeros', entregable: diccionario de datos completo, modelo entidad-relacion y mockup del tablero de metricas. Cada sprint cierra con revision frente al cliente y retrospectiva escrita de tres lineas.
5. Tablero resuelto: columnas Por hacer / Modelando (limite 2) / En revision del cliente (limite 2) / Aprobado, con la Definicion de Terminado escrita en la cabecera. Al arrastrar la tercera tarjeta a Modelando el tablero queda en rojo y la politica dice: nadie empieza algo nuevo, se ayuda a terminar lo que esta atascado. En la retrospectiva del sprint 1 el equipo anota: 'las tarjetas se acumulan en revision del cliente porque solo pedimos retroalimentacion el ultimo dia; en el sprint 2 pedimos revision a mitad de sprint'.

## Rubrica corta
- [ ] Product Backlog priorizado con justificacion de valor por item (2)
- [ ] Tres historias con estructura completa y escenarios Dado/Cuando/Entonces incluyendo casos alternativos (3)
- [ ] Plan de tres sprints con objetivo e incremento visible para el cliente en cada uno (3)
- [ ] Tablero con Definicion de Terminado explicita y limite de trabajo en curso respetado (2)

## Errores frecuentes
- Organizar los sprints por fases (sprint 1 analisis, sprint 2 diseño, sprint 3 construccion), con lo cual ningun sprint termina en algo que la clinica pueda ver: es cascada con nombre nuevo.
- Escribir historias que en realidad son tareas tecnicas ('crear la tabla paciente', 'instalar la herramienta'), sin decir quien las necesita ni para que sirven al negocio.
- Dejar criterios de aceptacion solo con el camino feliz, sin definir que pasa cuando el paciente no existe, cuando hay nombres repetidos o cuando falta un dato obligatorio.

Plantilla de apoyo: `Kit docente/Clase 4/Plantillas/Backlog-y-Sprints-VetCare.md`