# Guion docente · Clase 12 · Integración de módulos

- **Curso:** Programacion II (FI303204) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** (aplicacion Java de la clinica «Huellitas»)
- **Hoy avanzamos el PI en:** VetCare arranca, carga el archivo, registra, busca por ID, lista y guarda al cerrar: el flujo completo del PI corre sin tocar código.
- **Entregable de hoy:** El proyecto VetCare ejecutable (carpeta del proyecto o JAR) más la bitácora de integración con tres defectos hallados con el debugger, cada uno con síntoma, causa, corrección y evidencia, subidos a ExamLab.
- **Herramienta:** Visual Studio Code (Java)
- **Slides:** `Clases/Clase 12 - Integracion de modulos/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

## Apoyo por diapositiva

Las ideas de cada concepto estan proyectadas y el desarrollo completo esta en las notas del presentador de su lamina. Aqui va, por lamina y en su orden, lo que hay que subrayar.

**[Slide 4] Integrar: piezas que funcionan juntas** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: ¿Por qué importa?

**[Slide 5] main(): una sola instancia de cada capa** — codigo (6 lineas). Leerlo de arriba abajo y ejecutarlo en la demo.

**[Slide 6] El guion de humo** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: Eso es lo que tiene que correr sin que nadie toque código en la mitad.

**[Slide 7] El constructor registra el cierre** — codigo (15 lineas). Leerlo de arriba abajo y ejecutarlo en la demo.

**[Slide 8] cerrarGuardando(): guardar antes de salir** — codigo (15 lineas). Leerlo de arriba abajo y ejecutarlo en la demo.

**[Slide 9] Errores de integración y su síntoma** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: Los errores de integración tienen firma propia y conviene reconocerlos por el síntoma.
  - Subrayar: Quinto, la unión del código de tres personas que trajeron cada una su propia clase Mascota con constructores distintos.
  - Subrayar: Y sexto, el clásico NullPointerException porque buscarPorId devuelve null cuando el ID no existe y nadie valida antes de usar el resultado.

**[Slide 10] ServicioClinica: dueño de la lista** — codigo (12 lineas). Leerlo de arriba abajo y ejecutarlo en la demo.

**[Slide 11] El depurador de VS Code** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.

**[Slide 12] Integrar por goteo** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: Cuando algo se rompe, uno sabe exactamente qué fue lo último que tocó.

**[Slide 13] registrar(): la regla vive en el servicio** — codigo (17 lineas). Leerlo de arriba abajo y ejecutarlo en la demo.

**[Slide 14] registrarMascota(): la frontera con la interfaz** — codigo (13 lineas). Leerlo de arriba abajo y ejecutarlo en la demo.

## Errores tipicos del docente que no domina el tema

Material de preparacion: no se proyecta.

- Error tipico del docente que no domina el tema: junta todos los módulos la noche anterior, en clase la aplicación no arranca, y termina explicando el flujo en el tablero mientras los estudiantes nunca ven correr el producto; después culpa al editor, al JDK o al computador del salón. El segundo error es no abrir jamás el debugger: llena el código de System.out.println, y como imprime solo lo que se le ocurrió imprimir, no logra distinguir entre 'el dato llegó mal desde el formulario' y 'el dato se guardó mal en el archivo', que son dos defectos completamente distintos con el mismo síntoma. El tercero es no fijar el contrato del CSV: cada estudiante escribe su propio orden de campos, y al integrar el módulo del compañero el archivo se lee corrido, con lo que el docente concluye que 'el CSV es frágil' cuando lo frágil fue el acuerdo. La disciplina que se enseña hoy y que el docente debe haber practicado antes de entrar al salón es: integrar temprano, integrar por partes, tener un guion de humo de dos minutos que se corre después de cada cambio, y llegar a clase con VetCare ya corriendo para poder romperlo a propósito delante del grupo y arreglarlo con el debugger en vivo, que es la única forma de que el estudiante crea que la herramienta sirve.


**Demo que usted debe poder repetir:** El docente corre el guion de humo completo (abrir, registrar, buscar, cerrar, reabrir) y luego pone un breakpoint en el botón Registrar para mostrar con el debugger por qué una edad vacía estaba entrando como cero.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: VetCare arranca, carga el archivo, registra, busca por ID, lista y guarda al cerrar: el flujo completo del PI corre sin tocar código.. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en las laminas de concepto y en las de codigo
(lo que hay que subrayar esta tambien en las notas del presentador de cada lamina). Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente corre el guion de humo completo (abrir, registrar, buscar, cerrar, reabrir) y luego pone un breakpoint en el botón Registrar para mostrar con el debugger por qué una edad vacía estaba entrando como cero.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 12/Codigo/ClinicaApp.java`

### 60-105 · Taller guiado (opcional) = avance del PI
Opcional: no tiene lamina en el deck. La guia esta en
`Clases/Clase 12 - Integracion de modulos/Taller PI - Clase 12 - VetCare.docx`; si hoy no se hace, se extiende la demo y la practica libre.
**Decir:** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. Organice el proyecto en los paquetes clinica.modelo, clinica.datos, clinica.logica y clinica.ui, deje un único método main en la clase de arranque, elimine cualquier otro main que haya quedado de los talleres anteriores y verifique que la aplicación abre desde ese único punto.
2. Asegure una sola instancia: cree el repositorio y el servicio en el main y páselos por constructor a la ventana; ponga un breakpoint en el botón Registrar y otro en el cierre, y compruebe en la ventana Variables que el objeto servicio tiene el mismo identificador en ambos puntos.
3. Corra el guion de humo de cinco pasos (abrir con datos, registrar, buscar por ID, cerrar guardando, reabrir y verificar) y anote en qué paso exacto falla y con qué mensaje; si pasa completo a la primera, dañe una línea de mascotas.csv y vuelva a correrlo.
4. Depure el primer defecto con el debugger: breakpoint en el manejador del botón, registre el valor real de cada campo del formulario antes de llegar al servicio, identifique en qué capa se corrompe el dato y aplique la corrección; deje la evidencia en la bitácora.
5. Repita hasta que el guion de humo corra completo dos veces seguidas y entregue la bitácora de integración con tres defectos documentados con síntoma, causa, corrección y cómo lo verificó.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: El proyecto VetCare ejecutable (carpeta del proyecto o JAR) más la bitácora de integración con tres defectos hallados con el debugger, cada uno con síntoma, causa, corrección y evidencia, subidos a ExamLab.

### 105-120 · Criterios de exito y cierre
Si hubo taller, repasar los criterios de exito del `Taller PI - Clase 12 - VetCare.docx` (no estan en el deck).
Aplicar el quiz corto de `Kit docente/Clase 12/Quiz Clase 12 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: VetCare arranca, carga el archivo, registra, busca por ID, lista y guarda al cerrar: el flujo completo del PI corre sin tocar código.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 12/Solucion Taller Clase 12 - VetCare.docx` — no proyectar completa.
