# Guion docente · Clase 9 · Casos de uso

- **Curso:** Seminario de Sistemas (FI303301) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** — planos del sistema de la clinica «Huellitas»
- **Hoy avanzamos el PI en:** Queda listo el diagrama de casos de uso de VetCare con su limite de sistema y la especificacion textual completa de Registrar mascota y Buscar expediente.
- **Entregable de hoy:** Un PDF con el diagrama de casos de uso, la matriz de trazabilidad RF a CU y las dos especificaciones textuales completas (precondiciones, postcondiciones, flujo principal y minimo dos flujos alternos cada una), subido a ExamLab.
- **Herramienta:** draw.io · Google Docs
- **Slides:** `Clases/Clase 9 - Casos de uso/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**Un caso de uso es la descripcion de una interaccion completa entre un...** — 4 vinetas.
  - En VetCare, Registrar mascota pasa la prueba, porque la recepcionista de Huellitas termina con la ficha creada y el codigo asignado; en cambio Validar la fecha de nacimiento no la pasa, porque nadie llega a la clinica con el objetivo de validar una fecha.
  - Esa distincion parece un detalle de nombres, pero define el tamaño de todo el modelo: si se confunde, un sistema pequeño como VetCare termina con cuarenta casos de uso inutiles en vez de seis u ocho casos de uso reales.

**El actor es un rol, no una persona ni un cargo del organigrama** — 5 vinetas.
  - Si en VetCare dibujamos adentro del rectangulo un caso de uso llamado Enviar mensaje de WhatsApp, estamos diciendo que nosotros construimos la mensajeria, y eso probablemente sea falso y encarezca el proyecto por escrito.

**Las relaciones entre casos de uso son tres y se abusa de ellas (1/2)** — 5 vinetas.

**Las relaciones entre casos de uso son tres y se abusa de ellas (2/2)** — 3 vinetas.

**La especificacion textual es donde vive el noventa por ciento del valor... (1/2)** — 4 vinetas.
  - Un caso de uso especificado tiene ficha de identificacion (ID, nombre, actor primario, requisitos que cubre, prioridad y frecuencia), precondiciones, postcondiciones, flujo principal y flujos alternos, y las reglas de negocio asociadas.

**La especificacion textual es donde vive el noventa por ciento del valor... (2/2)** — 2 vinetas.

**Precondiciones y postcondiciones son un contrato, no un adorno (1/2)** — 4 vinetas.
  - Escribirlas asi tiene dos consecuencias practicas enormes.
  - Primero, cada postcondicion se convierte casi automaticamente en un caso de prueba, porque describe algo que se puede ir a comprobar.

**Precondiciones y postcondiciones son un contrato, no un adorno (2/2)** — 2 vinetas.


**Demo que usted debe poder repetir:** El docente proyecta como un caso de uso mal escrito (Dar clic en guardar) se transforma en uno correcto (Registrar mascota) y luego llena en vivo, delante del grupo, la plantilla de especificacion de Buscar expediente.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: Queda listo el diagrama de casos de uso de VetCare con su limite de sistema y la especificacion textual completa de Registrar mascota y Buscar expediente. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en la slide «Teoria Core» y en la de codigo
proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente proyecta como un caso de uso mal escrito (Dar clic en guardar) se transforma en uno correcto (Registrar mascota) y luego llena en vivo, delante del grupo, la plantilla de especificacion de Buscar expediente.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 9/Plantillas/CU-VetCare-Especificacion.md`

### 60-105 · Taller guiado = avance del PI
**Decir:** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. En draw.io, dibujar el limite del sistema rotulado VetCare y ubicar afuera los actores como roles (Recepcionista, Veterinario, Administrador y el servicio externo de mensajeria como actor secundario candidato, que hoy todavia no se conecta a ningun caso de uso); ningun actor puede llamarse con nombre propio ni con cargo inventado.
2. Colocar dentro del limite entre seis y ocho casos de uso derivados del catalogo de RF ya construido, todos redactados como verbo en infinitivo mas objeto del dominio, y borrar de inmediato cualquier elipse que se llame Guardar, Validar, Mostrar o Iniciar pantalla.
3. Construir en Google Docs la matriz de trazabilidad RF a CU: cada requisito funcional debe apuntar al menos a un caso de uso y cada caso de uso debe nacer de al menos un requisito; marcar en rojo los huerfanos que aparezcan y anotar por escrito la decision que se tomara con cada uno.
4. Modelar exactamente una relacion include y una relacion extend en el diagrama, y escribir al lado, en una nota de draw.io, una frase que justifique por que una es obligatoria y la otra condicional; si no se puede justificar, se elimina la flecha.
5. Diligenciar la plantilla completa de especificacion para CU-01 Registrar mascota y CU-02 Buscar expediente, con precondiciones, postcondiciones de exito y de fracaso, flujo principal en pares actor-sistema y minimo dos flujos alternos cada uno; exportar todo a PDF y subirlo a ExamLab.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Un PDF con el diagrama de casos de uso, la matriz de trazabilidad RF a CU y las dos especificaciones textuales completas (precondiciones, postcondiciones, flujo principal y minimo dos flujos alternos cada una), subido a ExamLab.

### 105-120 · Criterios de exito y cierre
Repasar el checklist de la slide de criterios.
Aplicar el quiz corto de `Kit docente/Clase 9/Quiz Clase 9 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: Queda listo el diagrama de casos de uso de VetCare con su limite de sistema y la especificacion textual completa de Registrar mascota y Buscar expediente.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 9/Solucion Taller Clase 9 - VetCare.docx` — no proyectar completa.
