# Solucion Taller · Clase 1 · Conceptos iniciales de ingenieria de software

> DOCUMENTO DOCENTE — PRIVADO. No publicar en Clases/.

## Solucion paso a paso
1. Paso 1 resuelto. Equipos de 2-3: mas de tres personas hace que alguien quede sin trabajo real y se note en la sustentacion, donde se pregunta al azar. El vocero tecnico no es el que mas sabe, es el que centraliza la comunicacion con el docente.
2. Paso 2 resuelto. Un problema bien escrito para VetCare: «La clinica Huellitas atiende un alto volumen de pacientes y lleva su gestion en carpetas de papel. Se extravian fichas de pacientes y buscar un historial durante la consulta toma varios minutos, lo que genera filas en la sala de espera. Ademas la administracion no sabe cuantas especies distintas atiende al mes». Note que hay actor, dolor y consecuencia observable.
3. Paso 3 resuelto. Capacidades como verbos de negocio: registrar dueños y sus mascotas; agendar citas medicas; consultar el historial clinico de una mascota; buscar un expediente por identificador; generar un conteo de atenciones por especie. Lo que NO es una capacidad: «tener una pantalla azul con botones», porque eso es una decision de interfaz, no una capacidad del sistema.
4. Paso 4 resuelto. Actores con interes explicito: Recepcionista, que necesita registrar y agendar rapido porque tiene fila esperando; Veterinario, que necesita ver el historial completo durante la consulta; Administrador de la clinica, que necesita metricas mensuales para decidir compras e horarios. Escribir el interes al lado del actor es lo que despues permite priorizar requisitos en conflicto.
5. Paso 5 resuelto. Fuera de alcance, escrito para que nadie lo discuta despues: no habra cobro ni facturacion electronica; no habra aplicacion movil; no habra acceso desde internet (el sistema es de escritorio, en la clinica); no habra historia clinica con imagenes ni radiografias. Cada linea de esta lista es una discusion que el equipo se ahorra en la Clase 11.

## Rubrica corta
- [ ] Problema con actor y dolor observable (3)
- [ ] 3-5 capacidades como verbos de negocio (3)
- [ ] Actores con interes explicito (2)
- [ ] Fuera de alcance especifico (2)

## Errores frecuentes
- Dominio vago tipo «una app para la universidad»: sin problema concreto, todo el semestre se vuelve humo.
- Confundir capacidad con pantalla: «tener un formulario» no es una capacidad, «registrar una mascota» si.
- Omitir el fuera de alcance: el proyecto crece cada semana y el equipo no alcanza a cerrar nada.

Plantilla de apoyo: `Kit docente/Clase 1/Plantillas/Ficha de dominio - VetCare.md`