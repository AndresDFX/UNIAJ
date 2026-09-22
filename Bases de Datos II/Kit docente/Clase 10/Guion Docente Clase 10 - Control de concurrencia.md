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

**[Slide 4] La transaccion como unidad de todo o nada (1/2)** — 5 vinetas.

**[Slide 5] La transaccion como unidad de todo o nada (2/2)** — 6 vinetas.

**[Slide 6] Serializar de verdad existe, y cuesta (1/2)** — 3 vinetas.

**[Slide 7] Serializar de verdad existe, y cuesta (2/2)** — 3 vinetas.

**[Slide 8] Los tres fenomenos indeseables, en escenas de la clinica (1/2)** — 6 vinetas.

**[Slide 9] Los tres fenomenos indeseables, en escenas de la clinica (2/2)** — 4 vinetas.

**[Slide 10] Los cuatro niveles de aislamiento se definen por lo que permiten (1/2)** — 6 vinetas.

**[Slide 11] Los cuatro niveles de aislamiento se definen por lo que permiten (2/2)** — 5 vinetas.

**[Slide 12] Control pesimista: SELECT ... FOR UPDATE** — 8 vinetas.
  - Por eso existen variantes que el docente debe conocer: FOR UPDATE NOWAIT falla de inmediato en vez de esperar, y FOR UPDATE WAIT 5 espera cinco segundos y luego falla, lo cual permite devolver un mensaje honesto al usuario en vez de una pantalla congelada.

**[Slide 13] Control optimista: verificar unicamente al escribir (1/2)** — 5 vinetas.

**[Slide 14] Control optimista: verificar unicamente al escribir (2/2)** — 3 vinetas.

**[Slide 15] Deadlock: la escena de VetCare y como se evita (1/2)** — 5 vinetas.

**[Slide 16] Deadlock: la escena de VetCare y como se evita (2/2)** — 5 vinetas.

**[Slide 17] Antes de los niveles: la restriccion que cuesta una linea (1/2)** — 5 vinetas.
  - La leccion general que el docente debe transmitir es que una regla que se puede expresar como restriccion declarativa, es decir UNIQUE, CHECK, FOREIGN KEY o NOT NULL, es mas confiable que la misma regla escrita en codigo, porque el motor la aplica siempre: venga la escritura de la aplicacion, de un script de carga masiva o de alguien conectado con un cliente SQL a corregir un dato a mano.

**[Slide 18] Antes de los niveles: la restriccion que cuesta una linea (2/2)** — 5 vinetas.


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
12. Control pesimista: SELECT ... FOR UPDATE
13. Control optimista: verificar unicamente al escribir (1/2)
14. Control optimista: verificar unicamente al escribir (2/2)
15. Deadlock: la escena de VetCare y como se evita (1/2)
16. Deadlock: la escena de VetCare y como se evita (2/2)
17. Antes de los niveles: la restriccion que cuesta una linea (1/2)
18. Antes de los niveles: la restriccion que cuesta una linea (2/2)
19. Doble reserva sin control de concurrencia
20. La restriccion que hace imposible la doble reserva
21. Demo del dia
22. Herramientas de hoy
23. Actividad autonoma — contexto / por que importa
24. Actividad autonoma — objetivo y criterios
25. Actividad autonoma — escenario / datos de partida
26. Actividad autonoma — pasos guiados
27. Actividad autonoma — pistas (checklist vacio)
28. Criterios de exito / entregable
29. Para el PI esta semana
30. Cierre · Clase 10

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
