# Solucion Taller · Clase 2 · Ciclos de vida del software

> DOCUMENTO DOCENTE — PRIVADO. No publicar en Clases/.

## Solucion paso a paso
1. Tabla resuelta: Requisitos responde QUE debe hacer VetCare y produce la lista RF-01 registrar paciente, RF-02 registrar consulta, RF-03 buscar historial, RNF-01 tiempo de respuesta menor a 3 segundos, aprobada por la administradora de Huellitas. Diseño responde COMO y produce el diagrama de casos de uso, el diagrama de clases, el modelo entidad-relacion y los mockups de la ficha, aprobados por el docente en rol de arquitecto. Construccion produce el codigo del modulo de pacientes y se aprueba en Programacion II. Pruebas produce los casos de prueba de aceptacion y sus evidencias, aprobados por la veterinaria. Mantenimiento produce las solicitudes de cambio y las versiones 1.1 y 1.2, aprobadas por la clinica.
2. Fase actual resuelta: el equipo esta cerrando REQUISITOS. Evidencia 1: existe la entrevista con Huellitas transcrita y una lista cruda de necesidades. Evidencia 2: no existe ningun diagrama UML ni mockup aprobado, luego la fase de diseño no ha empezado formalmente. Conclusion escrita: no se puede diseñar la pantalla de busqueda mientras no este claro por cuales campos se busca.
3. Diagrama lineal resuelto en draw.io: Requisitos -> Diseño con la flecha rotulada 'Documento RF/RNF aprobado'; Diseño -> Construccion rotulada 'Casos de uso, clases, modelo de datos y mockups'; Construccion -> Pruebas rotulada 'Modulo de pacientes ejecutable'; Pruebas -> Mantenimiento rotulada 'Acta de aceptacion firmada'. Una nota al pie aclara que si la clinica cambia de opinion en la ultima flecha, hay que devolverse hasta requisitos y rehacer todo lo intermedio.
4. Diagrama en vueltas resuelto: tres ciclos con las mismas cinco cajas. Vuelta 1 Incremento 1 'Ficha del paciente' entrega el mockup navegable de la ficha; Vuelta 2 Incremento 2 'Historia clinica y busqueda' entrega el caso de uso y el prototipo de busqueda; Vuelta 3 Incremento 3 'Reportes y metricas' entrega el tablero de indicadores. Desde la caja de pruebas de cada vuelta sale una flecha punteada rotulada 'Retroalimentacion de Huellitas' que regresa a requisitos de la vuelta siguiente.
5. Parrafo resuelto: 'El proyecto VetCare termina cuando se entregan y aprueban los planos, el prototipo navegable y el documento de diseño al cierre del semestre. El producto VetCare no termina ahi: sigue vivo mientras Huellitas lo use, con su version 1.0 en operacion. Ejemplo de mantenimiento: tres meses despues la clinica pide registrar vacunacion a domicilio con la direccion del cliente, lo cual obliga a volver a requisitos, ajustar el modelo de datos y liberar la version 1.1.'

## Rubrica corta
- [ ] Tabla de fases con artefactos propios de VetCare y responsable de aprobacion (3)
- [ ] Diagrama lineal en draw.io con artefacto rotulado en cada flecha (2)
- [ ] Diagrama en tres vueltas con incrementos nombrados y flecha de retroalimentacion (3)
- [ ] Parrafo producto vs proyecto con ejemplo concreto de mantenimiento (2)

## Errores frecuentes
- Copiar la definicion de las fases de internet y dejar la columna del artefacto en abstracto ('documentacion', 'analisis'), sin nombrar un solo entregable real de Huellitas.
- Dibujar el diagrama iterativo con cajas distintas a las del lineal, como si iterar cambiara las fases; iterar cambia el recorrido, no las fases.
- Confundir incremento con iteracion: entregar modulo tras modulo sin volver nunca sobre lo ya entregado, y llamar a eso 'trabajo iterativo'.

Plantilla de apoyo: `Kit docente/Clase 2/Plantillas/Mapa-Ciclo-de-Vida-VetCare.md`