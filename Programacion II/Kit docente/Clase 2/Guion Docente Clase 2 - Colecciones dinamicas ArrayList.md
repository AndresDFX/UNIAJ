# Guion docente · Clase 2 · Colecciones dinamicas · ArrayList

- **Curso:** Programacion II (FI303204) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** (aplicacion Java de la clinica «Huellitas»)
- **Hoy avanzamos el PI en:** El registro de mascotas de VetCare deja de vivir en un arreglo de tamano fijo y pasa a un ArrayList<Mascota> que crece con la clinica.
- **Entregable de hoy:** Proyecto Java con las clases Mascota y RegistroMascotas y un menu de consola que agrega, lista, busca por ID y elimina mascotas, comprimido y subido a ExamLab.
- **Herramienta:** Visual Studio Code (Java)
- **Slides:** `Clases/Clase 2 - Colecciones dinamicas ArrayList/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**El problema real de Huellitas** — 6 vinetas.

**Un ArrayList es exactamente esa carpeta que se agranda sola, y aqui...** — 5 vinetas.

**La interfaz de trabajo es corta y hay que dominarla de memoria** — 7 vinetas.

**Recorrer la lista tiene dos formas y cada una tiene su momento** — 6 vinetas.

**La ultima idea es de diseno, y es la que hace que este codigo sirva...** — 6 vinetas.


**Demo que usted debe poder repetir:** El docente muestra un Mascota[3] que revienta al intentar guardar la cuarta ficha y luego el mismo caso resuelto con ArrayList, imprimiendo size() despues de cada operacion.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: El registro de mascotas de VetCare deja de vivir en un arreglo de tamano fijo y pasa a un ArrayList<Mascota> que crece con la clinica.. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en la slide «Teoria Core» y en la de codigo
proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente muestra un Mascota[3] que revienta al intentar guardar la cuarta ficha y luego el mismo caso resuelto con ArrayList, imprimiendo size() despues de cada operacion.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 2/Codigo/VetCareRegistroMascotas.java`

### 60-105 · Taller guiado = avance del PI
**Decir:** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. Cree en VS Code el proyecto Java llamado VetCare con paquete vetcare, y dentro de el la clase Mascota con los atributos privados id, nombre, especie, edad y dueno, su constructor completo, sus getters y el metodo toString(); verifique imprimiendo una mascota de prueba y confirmando que en consola sale el texto legible y no vetcare.Mascota@1a2b3c.
2. Cree la clase RegistroMascotas con el atributo private final List<Mascota> mascotas = new ArrayList<>(); y el metodo agregar(Mascota m) que rechace un ID ya existente; verifique agregando dos veces la mascota M-001 y comprobando que la consola muestra el aviso de ID repetido y que cantidad() sigue devolviendo 1.
3. Implemente listar(), que recorra con for indexado e imprima cada ficha numerada, y buscarPorId(String id), que recorra con for-each y devuelva la Mascota o null; verifique que buscarPorId("M-003") imprime la ficha de Rocky y que buscarPorId("M-099") imprime que no existe, sin lanzar NullPointerException.
4. Implemente eliminarPorId(String id) usando remove(objeto) y el metodo pasarAGeriatria(int edadMinima) usando Iterator con it.remove(); verifique que despues de eliminar M-002 y de pasar a geriatria a las mascotas de 9 anios o mas, size() bajo exactamente en la cantidad de fichas retiradas y el programa no lanza ConcurrentModificationException.
5. Arme un menu de consola con Scanner y opciones 1-Agregar, 2-Listar, 3-Buscar por ID, 4-Eliminar, 5-Salir dentro de un ciclo while; ejecute el programa cargando las seis fichas del escenario, tome captura de la consola con el listado final y suba el proyecto comprimido mas la captura a ExamLab.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Proyecto Java con las clases Mascota y RegistroMascotas y un menu de consola que agrega, lista, busca por ID y elimina mascotas, comprimido y subido a ExamLab.

### 105-120 · Criterios de exito y cierre
Repasar el checklist de la slide de criterios.
Aplicar el quiz corto de `Kit docente/Clase 2/Quiz Clase 2 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: El registro de mascotas de VetCare deja de vivir en un arreglo de tamano fijo y pasa a un ArrayList<Mascota> que crece con la clinica.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 2/Solucion Taller Clase 2 - VetCare.docx` — no proyectar completa.
