# Guion docente · Clase 10 · Control de concurrencia · VetCare

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** AUTONOMA (festivo)
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** Escenarios de concurrencia del PI documentados
- **Entregable de hoy:** Informe corto: 2 escenarios (cita doble / stock) + mitigacion
- **Herramienta:** Google Docs + Live SQL
- **Slides:** Clases/Clase 10 - Control de concurrencia/Presentacion.pptx

> Sin mapa completo del curso, sin bio del docente, sin fechas de periodo.
> Presentacion del Curso / Acuerdo cubren logistica global.

## Fundamento teorico para el docente (al servicio del PI)

El objetivo de la clase no es «cubrir un capitulo» aislado, sino producir evidencia
del PI VetCare. La teoria se limita a desbloquear el taller.

- Concurrencia = varias transacciones ejecutandose al mismo tiempo sobre los mismos datos. El problema clasico de VetCare: dos recepcionistas, en dos computadores distintos, intentan agendar la MISMA franja horaria para el MISMO veterinario en el mismo instante; sin control, ambas lecturas ven la franja libre y ambas insertan — doble reserva.
- Control pesimista: asumir que el conflicto va a ocurrir, asi que se bloquea la fila (o el recurso) apenas se empieza a leer para modificar, y otras transacciones deben esperar a que termine (SELECT ... FOR UPDATE es el ejemplo tipico). Simple y seguro, pero puede generar esperas largas si hay muchas transacciones compitiendo.
- Control optimista: asumir que el conflicto es raro, dejar que todos lean libremente, y verificar SOLO al momento de escribir si alguien mas cambio el dato mientras tanto (comparando una version o timestamp); si hubo cambio, se rechaza y se reintenta. Mejor rendimiento cuando los conflictos son poco frecuentes.
- Deadlock (mencion breve): dos transacciones se bloquean mutuamente esperando un recurso que la otra tiene — T1 espera la fila que T2 bloqueo, y T2 espera la fila que T1 bloqueo. El motor detecta esto y aborta una de las dos automaticamente.
- Mitigaciones concretas y accesibles para el PI: una restriccion UNIQUE sobre (id_veterinario, fecha_hora) hace que el segundo INSERT falle automaticamente en vez de crear la doble reserva; transacciones cortas reducen la ventana de tiempo en la que puede ocurrir un conflicto; centralizar la logica en un procedimiento (Clase 3) evita que cada pantalla de la app implemente su propia validacion de forma inconsistente.
- Error de docente que no domina el tema: creer que 'poner una transaccion' ya resuelve la concurrencia — una transaccion garantiza atomicidad, pero sin un mecanismo de bloqueo o una restriccion UNIQUE, dos transacciones concurrentes pueden seguir generando la doble reserva porque ambas leen 'libre' antes de que la otra confirme.

**Demo que usted debe poder repetir:** Narrativa paso a paso T1/T2 sobre tabla Cita.

## Referencias a diapositivas
1. Slide 1 portada (Clase N + titulo VetCare)
2. Slide Agenda 120 min
3. Slide Objetivo PI de la clase
4. Slide Teoria Core
5. Slide Demo del dia
6. Slide Herramientas de hoy (logos 3-4)
7. Bloque Taller ampliado: contexto / objetivo / escenario / pasos / pistas
8. Slide Criterios de exito / entregable
9. Slide Para el PI esta semana
10. Slide Cierre
11. Solucion PRIVADA: Kit docente/Clase N/Solucion Taller Clase N - VetCare.docx

## Plan minuto a minuto (120 min equivalentes — trabajo autonomo)

> El estudiante trabaja sin encuentro sincrono. Usted publica este guion resumido + taller en ExamLab.

### Bloque A (0-20) · Encuadre PI
**Decir/publicar:** «Hoy avanzamos el PI en: Escenarios de concurrencia del PI documentados. No es un taller suelto.»
Referencia slides: Agenda + Objetivo PI.

### Bloque B (20-45) · Teoria minima
Leer Teoria Core. Tomar notas en el informe del PI.

### Bloque C (45-100) · Practica = entregable PI
Seguir el taller estudiante. Herramienta: Google Docs + Live SQL.
Salida esperada de la practica (publiquela junto al enunciado para que el
estudiante autonomo sepa si le quedo bien):
📸 Evidencia del problema: dos citas en la misma franja (sin restriccion) [[captura: salida-doble-reserva.png]]
📸 El MISMO INSERT ya con UNIQUE: la BD lo rechaza sola [[captura: salida-unique-rechaza.png]]

### Bloque D (100-120) · Empaquetado y cierre
Subir entregable a ExamLab. Actualizar checklist PI del equipo.


## Codigo / scripts
Carpeta Codigo/ — archivo 10_concurrencia_vetcare.sql.

## Capturas
Carpeta Capturas/. Placeholders [CAP: ...] arriba; reemplazar por PNG reales cuando pueda
(Playwright/manual en DB Fiddle, draw.io, Live SQL).

## Criterios de exito del dia
- Equipos tienen el entregable o gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
