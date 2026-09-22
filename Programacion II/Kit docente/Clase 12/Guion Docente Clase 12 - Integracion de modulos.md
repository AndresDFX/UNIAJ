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

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**Integrar es lograr que piezas que ya funcionan por separado funcionen... (1/2)** — 4 vinetas.
  - ¿Por qué importa?

**Integrar es lograr que piezas que ya funcionan por separado funcionen... (2/2)** — 3 vinetas.

**El flujo de punta a punta se define antes de integrar, por escrito, y... (1/2)** — 4 vinetas.
  - Eso es lo que tiene que correr sin que nadie toque código en la mitad.

**El flujo de punta a punta se define antes de integrar, por escrito, y... (2/2)** — 2 vinetas.

**Los errores de integración tienen firma propia y conviene reconocerlos...** — 5 vinetas.
  - Los errores de integración tienen firma propia y conviene reconocerlos por el síntoma.
  - Quinto, la unión del código de tres personas que trajeron cada una su propia clase Mascota con constructores distintos.
  - Y sexto, el clásico NullPointerException porque buscarPorId devuelve null cuando el ID no existe y nadie valida antes de usar el resultado.

**El depurador de VS Code es la herramienta de esta clase y hay que... (1/2)** — 4 vinetas.

**El depurador de VS Code es la herramienta de esta clase y hay que... (2/2)** — 4 vinetas.

**La forma de integrar sin sufrir es por goteo y no de un solo golpe (1/2)** — 4 vinetas.
  - Cuando algo se rompe, uno sabe exactamente qué fue lo último que tocó.

**La forma de integrar sin sufrir es por goteo y no de un solo golpe (2/2)** — 3 vinetas.

**VetCareApp.java — class VetCareApp** — 18 vinetas.

**VetCareApp.java — VetCareApp()** — 16 vinetas.

**VetCareApp.java — construirInterfaz() (1/2)** — 20 vinetas.

**VetCareApp.java — construirInterfaz() (2/2)** — 12 vinetas.

**VetCareApp.java — registrarMascota()** — 13 vinetas.

**VetCareApp.java — buscarPorId()** — 11 vinetas.

**VetCareApp.java — refrescarTabla()** — 8 vinetas.

**VetCareApp.java — limpiarFormulario()** — 7 vinetas.

**VetCareApp.java — cerrarGuardando()** — 16 vinetas.

**VetCareApp.java — main()** — 9 vinetas.

**class DatosInvalidosException · DatosInvalidosException() · class Mascota** — 17 vinetas.

**VetCareApp.java — Mascota()** — 8 vinetas.

**VetCareApp.java — ficha()** — 7 vinetas.

**VetCareApp.java — class ServicioVetCare** — 7 vinetas.

**VetCareApp.java — ServicioVetCare()** — 4 vinetas.

**VetCareApp.java — cargarDesdeArchivo()** — 6 vinetas.

**VetCareApp.java — guardarEnArchivo()** — 4 vinetas.

**VetCareApp.java — listar()** — 4 vinetas.

**VetCareApp.java — buscarPorId()** — 12 vinetas.

**VetCareApp.java — registrar() (1/2)** — 20 vinetas.

**VetCareApp.java — registrar() (2/2)** — 6 vinetas.

**VetCareApp.java — siguienteId() (1/2)** — 20 vinetas.

**VetCareApp.java — siguienteId() (2/2)** — 1 vinetas.

**VetCareApp.java — class RepositorioMascotasCSV** — 8 vinetas.

**VetCareApp.java — RepositorioMascotasCSV()** — 4 vinetas.

**VetCareApp.java — rutaAbsoluta()** — 4 vinetas.

**VetCareApp.java — guardar()** — 15 vinetas.

**VetCareApp.java — cargar() (1/2)** — 20 vinetas.

**VetCareApp.java — cargar() (2/2)** — 15 vinetas.

**VetCareApp.java — limpiar()** — 8 vinetas.


**Demo que usted debe poder repetir:** El docente corre el guion de humo completo (abrir, registrar, buscar, cerrar, reabrir) y luego pone un breakpoint en el botón Registrar para mostrar con el debugger por qué una edad vacía estaba entrando como cero.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: VetCare arranca, carga el archivo, registra, busca por ID, lista y guarda al cerrar: el flujo completo del PI corre sin tocar código.. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en la slide «Teoria Core» y en la de codigo
proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente corre el guion de humo completo (abrir, registrar, buscar, cerrar, reabrir) y luego pone un breakpoint en el botón Registrar para mostrar con el debugger por qué una edad vacía estaba entrando como cero.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 12/Codigo/VetCareApp.java`

### 60-105 · Taller guiado = avance del PI
**Decir:** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. Organice el proyecto en los paquetes vetcare.modelo, vetcare.datos, vetcare.logica y vetcare.ui, deje un único método main en la clase de arranque, elimine cualquier otro main que haya quedado de los talleres anteriores y verifique que la aplicación abre desde ese único punto.
2. Asegure una sola instancia: cree el repositorio y el servicio en el main y páselos por constructor a la ventana; ponga un breakpoint en el botón Registrar y otro en el cierre, y compruebe en la ventana Variables que el objeto servicio tiene el mismo identificador en ambos puntos.
3. Corra el guion de humo de cinco pasos (abrir con datos, registrar, buscar por ID, cerrar guardando, reabrir y verificar) y anote en qué paso exacto falla y con qué mensaje; si pasa completo a la primera, dañe una línea de mascotas.csv y vuelva a correrlo.
4. Depure el primer defecto con el debugger: breakpoint en el manejador del botón, registre el valor real de cada campo del formulario antes de llegar al servicio, identifique en qué capa se corrompe el dato y aplique la corrección; deje la evidencia en la bitácora.
5. Repita hasta que el guion de humo corra completo dos veces seguidas y entregue la bitácora de integración con tres defectos documentados con síntoma, causa, corrección y cómo lo verificó.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: El proyecto VetCare ejecutable (carpeta del proyecto o JAR) más la bitácora de integración con tres defectos hallados con el debugger, cada uno con síntoma, causa, corrección y evidencia, subidos a ExamLab.

### 105-120 · Criterios de exito y cierre
Repasar el checklist de la slide de criterios.
Aplicar el quiz corto de `Kit docente/Clase 12/Quiz Clase 12 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: VetCare arranca, carga el archivo, registra, busca por ID, lista y guarda al cerrar: el flujo completo del PI corre sin tocar código.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 12/Solucion Taller Clase 12 - VetCare.docx` — no proyectar completa.
