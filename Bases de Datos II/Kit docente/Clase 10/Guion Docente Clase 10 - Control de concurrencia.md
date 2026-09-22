# Guion docente · Clase 10 · Control de concurrencia · VetCare

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** AUTONOMA (festivo, sin encuentro sincrono)
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** Escenarios de concurrencia del PI documentados
- **Entregable de hoy:** Informe corto: 2 escenarios (cita doble / stock) + mitigacion
- **Herramienta:** Google Docs + Live SQL
- **Slides:** Clases/Clase 10 - Control de concurrencia/Presentacion.pptx
- **Caso de estudio (anexo del estudiante):** `Clases/Proyecto Integrador/Anexo - Caso de estudio Clinica Huellitas - Bases de Datos II.docx`
  — perfil de la clinica, las 8 entidades, las 3 reglas, el elenco de nombres y la escala por clase.
  Remita a este anexo cada vez que alguien pregunte «que datos guarda» o «de que tamano es esto».

> Sin mapa completo del curso, sin bio del docente, sin fechas de periodo.
> Presentacion del Curso / Acuerdo cubren logistica global.

## Fundamento teorico para el docente (al servicio del PI)

El objetivo de la clase no es «cubrir un capitulo» aislado, sino producir evidencia
del PI VetCare. La teoria se limita a desbloquear el taller.


## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**[Slide 4] La transaccion como unidad de todo o nada (1/2)** — 3 vinetas.
  - Se abre de forma explicita o implicita y se cierra con COMMIT, que hace permanentes los cambios, o con ROLLBACK, que los deshace.
  - Concurrencia significa que dos o mas transacciones estan abiertas al mismo tiempo sobre los mismos datos.
  - Ambas consultan si la franja esta libre.
  - Ambas reciben cero filas.
  - Ambas insertan una cita.

**[Slide 5] La transaccion como unidad de todo o nada (2/2)** — 3 vinetas.

**[Slide 6] Serializar de verdad existe, y cuesta (1/2)** — 3 vinetas.
  - Por eso el estandar SQL no impone una sola forma de trabajar: ofrece una perilla llamada nivel de aislamiento, que permite negociar cuanta anomalia se tolera a cambio de cuanto rendimiento.

**[Slide 7] Serializar de verdad existe, y cuesta (2/2)** — 2 vinetas.

**[Slide 8] Los tres fenomenos indeseables, en escenas de la clinica (1/2)** — 5 vinetas.
  - El estandar define tres fenomenos indeseables, y cada uno se entiende mejor con una escena de la clinica.
  - La misma consulta, en la misma transaccion, devolvio dos valores distintos.

**[Slide 9] Los tres fenomenos indeseables, en escenas de la clinica (2/2)** — 3 vinetas.

**[Slide 10] Los cuatro niveles de aislamiento se definen por lo que permiten (1/2)** — 5 vinetas.
  - READ COMMITTED impide la lectura sucia, porque solo se ve lo que ya fue confirmado, pero permite lectura no repetible y fantasma.
  - SERIALIZABLE impide los tres y equivale logicamente a ejecutar las transacciones una tras otra.

**[Slide 11] Los cuatro niveles de aislamiento se definen por lo que permiten (2/2)** — 4 vinetas.

**[Slide 12] Control pesimista: SELECT... FOR UPDATE (1/2)** — 4 vinetas.
  - El control pesimista asume que el conflicto va a ocurrir, asi que bloquea el recurso antes de tocarlo.
  - Por eso existen variantes que el docente debe conocer: FOR UPDATE NOWAIT falla de inmediato en vez de esperar, y FOR UPDATE WAIT 5 espera cinco segundos y luego falla, lo cual permite devolver un mensaje honesto al usuario en vez de una pantalla congelada.

**[Slide 13] Control pesimista: SELECT... FOR UPDATE (2/2)** — 3 vinetas.

**[Slide 14] Control optimista: verificar unicamente al escribir (1/2)** — 5 vinetas.

**[Slide 15] Control optimista: verificar unicamente al escribir (2/2)** — 3 vinetas.

**[Slide 16] Control optimista: verificar unicamente al... — sintaxis** — 3 vinetas.

**[Slide 17] Deadlock: la escena de VetCare y como se evita (1/2)** — 4 vinetas.
  - Un deadlock, o interbloqueo, ocurre cuando dos transacciones se esperan mutuamente y ninguna puede avanzar.
  - Si los dos arrancan al mismo tiempo, cada uno tiene exactamente lo que el otro necesita, nadie cede y ninguna espera termina sola.
  - La transaccion sobreviviente termina normal.

**[Slide 18] Deadlock: la escena de VetCare y como se evita (2/2)** — 3 vinetas.

**[Slide 19] Antes de los niveles: la restriccion que cuesta una linea** — 3 vinetas.
  - Con esa restriccion, cuando las dos recepcionistas insertan, el motor deja pasar la primera y rechaza la segunda con una violacion de unicidad, sin que nadie haya razonado sobre aislamiento; el procedimiento captura esa excepcion y devuelve «ese horario acaba de ser tomado, elija otro».
  - La leccion general que el docente debe transmitir es que una regla que se puede expresar como restriccion declarativa, es decir UNIQUE, CHECK, FOREIGN KEY o NOT NULL, es mas confiable que la misma regla escrita en codigo, porque el motor la aplica siempre: venga la escritura de la aplicacion, de un script de carga masiva o de alguien conectado con un cliente SQL a corregir un dato a mano.
  - La respuesta honesta es que no se puede: los playgrounds gratuitos ejecutan un script en una unica sesion, normalmente con autocommit activo, y no permiten abrir dos conexiones para intercalarlas.
  - Lo que si se demuestra con evidencia ejecutable son tres cosas: la restriccion UNIQUE rechazando el segundo INSERT, el patron optimista completo con la columna version y el UPDATE que afecta cero filas, y la sintaxis de SELECT FOR UPDATE ejecutandose sin error.
  - Lo que no se demuestra se documenta en una tabla de linea de tiempo con columnas T1, T2 y estado de la fila, paso por paso; esa tabla es un artefacto profesional legitimo, no un premio de consolacion, y es exactamente como se comunican estos escenarios en un documento de diseno real.

**[Slide 20] Antes de los niveles: la restriccion que... — sintaxis** — 1 vinetas.

**[Slide 21] La doble reserva, y la restriccion que la cierra de raiz** — 10 vinetas.

**[Slide 22] El bloqueo explicito y la actualizacion condicional** — 10 vinetas.

**[Slide 23] Niveles de aislamiento: que anomalia tapa cada uno** — 13 vinetas.


**Demo que usted debe poder repetir:** Narrativa paso a paso T1/T2 sobre tabla Cita.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 10 - Control de concurrencia/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 10 · Control de concurrencia · VetCare
2. Encuadre de hoy · Objetivo PI
3. Mapa del bloque de hoy (120 min)
4. La transaccion como unidad de todo o nada (1/2)
5. La transaccion como unidad de todo o nada (2/2)
6. Serializar de verdad existe, y cuesta (1/2)
7. Serializar de verdad existe, y cuesta (2/2)
8. Los tres fenomenos indeseables, en escenas de la clinica (1/2)
9. Los tres fenomenos indeseables, en escenas de la clinica (2/2)
10. Los cuatro niveles de aislamiento se definen por lo que permiten (1/2)
11. Los cuatro niveles de aislamiento se definen por lo que permiten (2/2)
12. Control pesimista: SELECT... FOR UPDATE (1/2)
13. Control pesimista: SELECT... FOR UPDATE (2/2)
14. Control optimista: verificar unicamente al escribir (1/2)
15. Control optimista: verificar unicamente al escribir (2/2)
16. Control optimista: verificar unicamente al... — sintaxis
17. Deadlock: la escena de VetCare y como se evita (1/2)
18. Deadlock: la escena de VetCare y como se evita (2/2)
19. Antes de los niveles: la restriccion que cuesta una linea
20. Antes de los niveles: la restriccion que... — sintaxis
21. La doble reserva, y la restriccion que la cierra de raiz
22. El bloqueo explicito y la actualizacion condicional
23. Niveles de aislamiento: que anomalia tapa cada uno
24. Doble reserva sin control de concurrencia
25. La restriccion que hace imposible la doble reserva
26. Demo del dia
27. Herramientas de hoy
28. Actividad autonoma — contexto / por que importa
29. Actividad autonoma — objetivo y criterios
30. Actividad autonoma — escenario / datos de partida
31. Actividad autonoma — pasos guiados
32. Actividad autonoma — pistas (checklist vacio)
33. Criterios de exito / entregable
34. Para el PI esta semana
35. Cierre · Clase 10

> Privado, no se proyecta: `Kit docente/Clase 10/Solucion Taller Clase 10 - VetCare.docx`

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
Subir entregable a ExamLab. Actualizar el checklist PI del proyecto.


## Codigo / scripts
Carpeta Codigo/ — archivo 10_concurrencia_vetcare.sql.

## Capturas
Carpeta `Kit docente/Clase 10/Capturas/`. Cada linea de pantallazo de arriba trae
el nombre exacto del archivo y, si todavia no existe, el paso a paso para producirlo:
tomelo, guardelo con ese nombre y vuelva a generar el guion — la imagen se embebe sola.
Detalle por captura en `Capturas/README_capturas.txt`.

## Criterios de exito del dia
- Cada estudiante tiene el entregable o sus gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
