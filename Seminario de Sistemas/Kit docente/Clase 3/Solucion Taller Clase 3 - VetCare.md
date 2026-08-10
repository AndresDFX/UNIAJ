# Solucion Taller · Clase 3 · Metodologias tradicionales

> DOCUMENTO DOCENTE — PRIVADO. No publicar en Clases/.

## Solucion paso a paso
1. Indice del ERS resuelto: 1. Proposito y alcance (VetCare digitaliza el registro de pacientes, consultas e historia clinica de la clinica Huellitas; queda fuera del alcance la facturacion y el inventario de medicamentos). 2. Glosario (paciente = animal atendido; propietario = persona responsable; ficha = historia clinica del paciente; consulta = atencion medica registrada). 3. Requisitos funcionales RF-01 a RF-12. 4. Requisitos no funcionales RNF-01 a RNF-05. 5. Reglas de negocio (RN-01 un paciente pertenece a un unico propietario; RN-02 no se elimina una consulta, se anula con motivo). 6. Matriz de trazabilidad. 7. Control de versiones y aprobaciones.
2. Requisitos resueltos en ficha: RF-01 Registrar paciente, fuente auxiliar de recepcion, prioridad alta, estabilidad alta, criterio de aceptacion: se guarda con nombre, especie, raza, fecha de nacimiento y propietario, y el sistema rechaza el registro si falta el propietario. RF-03 Buscar historial, fuente Dra. Rios, criterio: con 5.000 fichas el resultado aparece en menos de 3 segundos y en maximo 3 clics. RF-08 Anular consulta con motivo, depende de RF-02. RNF-02 Disponibilidad: el sistema opera en horario de atencion de 7:00 a 19:00 con caida maxima de 30 minutos al mes. Todos en version 1.0, estado Aprobado, linea base con fecha.
3. Matriz en V resuelta: Requisitos / ERS aprobado / Pruebas de aceptacion / CP-ACEP-07 verifica RF-03 y CP-ACEP-02 verifica RF-01. Diseño de arquitectura / Diagrama de componentes y modelo de datos / Pruebas de integracion / CP-INT-03 verifica que el modulo de consultas guarde contra la ficha correcta. Diseño detallado / Diagrama de clases y contratos de metodos / Pruebas unitarias / CP-UNI-11 verifica la regla RN-01. Construccion (Programacion II) / Modulo ejecutable / se prueba de abajo hacia arriba.
4. Diagrama en V resuelto en draw.io: rama izquierda descendente con Requisitos, Diseño de arquitectura, Diseño detallado y en el vertice Construccion; rama derecha ascendente con Pruebas unitarias, Pruebas de integracion y Pruebas de aceptacion. Lineas punteadas horizontales: Requisitos <--> Pruebas de aceptacion rotulada 'RF-03 <-> CP-ACEP-07'; Diseño detallado <--> Pruebas unitarias rotulada 'RN-01 <-> CP-UNI-11'. Nota al margen: la prueba se escribe cuando se escribe el requisito, no al final.
5. Solicitud de cambio resuelta: SC-004, solicitada por la administradora, descripcion 'buscar tambien por numero de microchip'. Requisito afectado RF-03 (pasa a version 1.1). Impacto: el modelo de datos requiere el campo microchip en la entidad Paciente, el mockup de busqueda necesita un filtro adicional, y CP-ACEP-07 debe ampliarse con un tercer escenario. Estimacion: 6 horas de rediseño de planos. Decision: aprobada con nueva linea base fechada, porque el cambio se detecto antes de construir; si hubiera llegado despues de la construccion, se habria aplazado a la version 1.1 del producto.

## Rubrica corta
- [ ] Indice del ERS completo y con glosario del dominio veterinario (2)
- [ ] Cuatro requisitos en ficha con ID, version, estado y criterio de aceptacion medible (3)
- [ ] Matriz en V con todos los requisitos emparejados a su nivel de prueba y codigo de caso (3)
- [ ] Solicitud de cambio con impacto y decision justificada (2)

## Errores frecuentes
- Escribir criterios de aceptacion no medibles como 'la busqueda debe ser rapida' o 'la pantalla debe ser amigable', que nadie puede aprobar ni rechazar objetivamente.
- Dibujar la V con las mismas fases en los dos lados (requisitos abajo y requisitos arriba), perdiendo el sentido del modelo, que es emparejar cada fase con su NIVEL de prueba.
- Poner requisitos sin fuente ni version y luego cambiarlos en el documento sin dejar rastro, con lo cual la linea base deja de existir y ya no se puede demostrar que fue lo acordado.

Plantilla de apoyo: `Kit docente/Clase 3/Plantillas/ERS-y-Matriz-en-V-VetCare.md`