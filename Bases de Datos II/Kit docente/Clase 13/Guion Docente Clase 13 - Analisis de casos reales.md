# Guion docente · Clase 13 · Analisis de casos reales · VetCare

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** AUTONOMA (festivo, sin encuentro sincrono)
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** Informe de caso -> mejoras concretas al PI
- **Entregable de hoy:** Informe 1-2 pag.: caso + 3 mejoras aplicables a VetCare
- **Herramienta:** Google Docs
- **Slides:** Clases/Clase 13 - Analisis de casos reales/Presentacion.pptx

> Sin mapa completo del curso, sin bio del docente, sin fechas de periodo.
> Presentacion del Curso / Acuerdo cubren logistica global.

## Fundamento teorico para el docente (al servicio del PI)

El objetivo de la clase no es «cubrir un capitulo» aislado, sino producir evidencia
del PI VetCare. La teoria se limita a desbloquear el taller.

- Caso 1 — falta de backup real: una organizacion que 'hacia backup' copiando el archivo de datos una vez al mes sin probar nunca el restore. Cuando el disco fallo, el archivo copiado estaba corrupto (nunca se verifico) y perdieron meses de informacion. Leccion para VetCare: un backup que nunca se restauro de prueba no cuenta como backup funcional (conecta con Clase 4: RPO/RTO y prueba de restore).
- Caso 2 — indices mal disenados: un sistema con un indice sobre CADA columna 'por si acaso', que volvia cada INSERT/UPDATE mas lento de lo aceptable, sin que nadie hubiera medido si esos indices realmente se usaban en consultas reales. Leccion: indexar sin justificar la consulta que lo aprovecha (conecta con Clase 7) desperdicia recursos y no mejora nada.
- Caso 3 — inyeccion SQL: una aplicacion que concatenaba directamente el texto escrito por el usuario dentro de una consulta (ej. "SELECT * FROM usuarios WHERE nombre='" + input + "'"), permitiendo que alguien escribiera un valor que alterara la consulta completa y expusiera o borrara datos ajenos. Leccion: por eso la app llama procedimientos con parametros tipados (Clase 3 y Clase 12) en vez de armar SQL con texto libre.
- Estructura para analizar cualquier caso real: (1) contexto — que sistema era y que se suponia que hacia bien; (2) fallo — que paso exactamente y por que la causa raiz no era 'mala suerte' sino una decision tecnica evitable; (3) leccion — que principio general se puede extraer; (4) cambio concreto — que se ajusta HOY en su propio VetCare, no en abstracto.
- Esta clase es autonoma (sin encuentro sincrono) precisamente porque no introduce tecnica nueva: aplica en modo reflexivo/critico todo lo visto en Clases 1-10 sobre un caso real, cerrando el ciclo antes de entrar a integracion y cierre del PI.
- Error de docente que no domina el tema: dejar que el informe describa el caso ajeno sin conectar ninguna leccion con una accion verificable en VetCare — el entregable exige 3 mejoras concretas aplicadas al proyecto propio, no un resumen de noticia.

### Desarrollo del tema (para dictar sin consultar otra fuente)

Esta clase es autonoma y cae en festivo, asi que no hay encuentro sincronico: este texto es a la vez el fundamento del docente y la lectura que el estudiante recibe, y por eso debe alcanzar para trabajar solo. El tema es el analisis de casos reales, y el primer punto es que esto no es relleno de fin de semestre sino una practica profesional con nombre propio. Cuando un sistema falla en produccion, los equipos serios escriben un post-mortem, que es un documento breve producido despues del incidente y que responde cuatro preguntas: que paso, cuando y con que impacto medible, por que fue posible, y que se va a cambiar para que no vuelva a ocurrir de la misma manera. La palabra clave del oficio es blameless, sin culpables: la regla es que se analiza el sistema y no la persona. No es cortesia ni buena onda corporativa, es un calculo practico, porque en cuanto el documento sirve para castigar a alguien la gente deja de reportar los errores pequenos y la organizacion pierde la unica fuente de informacion que tiene para evitar los grandes. Un incidente, para nuestros fines, es cualquier evento que degrada el servicio o pone en riesgo los datos, y merece post-mortem tanto el que llego al usuario como el que se detuvo a tiempo. El entregable de hoy es una tabla de cuatro columnas, Contexto, Fallo, Leccion y Cambio en VetCare, con tres casos, y se sube a ExamLab.

Antes de mirar los casos hay que instalar la distincion que separa un buen analisis de una anecdota: causa proxima y causa raiz. La causa proxima es el ultimo evento de la cadena, el que se ve. La causa raiz es la condicion que permitio que ese evento tuviera consecuencias. Un ejemplo con VetCare: el disco del servidor falla un viernes y se pierden tres semanas de historias clinicas. La causa proxima es el disco. La causa raiz es que existia un archivo de respaldo que nadie habia restaurado nunca para comprobar que sirviera, y que nadie vigilaba si el respaldo del dia se habia ejecutado. Los discos fallan siempre, eso no es noticia; lo que se puede cambiar es lo segundo. La tecnica mas simple para llegar ahi es preguntar por que cinco veces seguidas, y hay dos criterios de parada utiles: si la respuesta nombra una persona, todavia no llego a la causa raiz, porque senalar a quien ejecuto el comando equivocado no explica por que el sistema permitia ejecutarlo sin confirmacion ni por que no habia como volver atras; y si la respuesta describe algo que se puede cambiar en un procedimiento, un permiso, una restriccion o una alarma, entonces si llego. Conviene ademas admitir la existencia de factores contribuyentes, que son condiciones que empeoraron el resultado sin haberlo causado, como que el incidente ocurriera de noche, que la documentacion estuviera desactualizada o que el unico que sabia restaurar estuviera de vacaciones.

Caso uno, el respaldo que nunca se restauro, con el ejemplo publico mejor documentado que existe. El 31 de enero de 2017 GitLab sufrio la perdida de datos de su servicio en la nube: durante la atencion de un problema de replicacion, un ingeniero ejecuto un borrado recursivo sobre el directorio de datos del servidor equivocado y elimino cerca de trescientos gigabytes. Eso es la causa proxima. Lo que convirtio un error humano corriente en un incidente historico fue que, al intentar recuperar, la compania descubrio que sus cinco mecanismos de respaldo y replicacion fallaban de una u otra forma: entre otras cosas, la herramienta de volcado logico fallaba en silencio por una diferencia de version entre cliente y servidor, y las copias que debian estar en almacenamiento remoto estaban vacias. Terminaron restaurando desde una copia de trabajo de unas seis horas antes y perdieron de forma definitiva la informacion creada en esa ventana, del orden de miles de proyectos y comentarios. La leccion tecnica es exacta: un respaldo que nunca se restauro de prueba no es un respaldo, es una carpeta con un nombre tranquilizador. Y hay una segunda leccion igual de importante: un proceso de respaldo que puede fallar sin avisar es peor que no tenerlo, porque produce confianza injustificada. Esto conecta con la Clase 4, donde se definieron RPO, la cantidad maxima de datos que la organizacion acepta perder medida en tiempo, y RTO, el tiempo maximo que acepta estar caida. GitLab descubrio su RPO real el dia del incidente, y ese es justo el error que no se debe repetir: el RPO no se declara, se demuestra restaurando.

Caso dos, permisos excesivos. En julio de 2019 Capital One informo un acceso no autorizado que afecto informacion de aproximadamente cien millones de personas en Estados Unidos y varios millones en Canada, incluyendo solicitudes de credito. La cadena tecnica publicada es instructiva porque no hubo ninguna hazana: una configuracion incorrecta en un cortafuegos de aplicaciones permitio que se le hiciera hacer peticiones internas en nombre del servidor, con eso se obtuvieron credenciales temporales de un rol de servicio, y ese rol tenia permiso para listar y leer todos los buckets de almacenamiento, muchos mas de los que necesitaba para su trabajo. El regulador bancario estadounidense impuso una multa de ochenta millones de dolares en 2020. La causa proxima es la mala configuracion del cortafuegos; la causa raiz es que un componente tenia privilegios mucho mayores que su funcion. La leccion, en el vocabulario de la Clase 2, es el principio de privilegio minimo: cada actor recibe exactamente los permisos que necesita para su tarea y nada mas. Y hay que decir la parte incomoda, porque es la que se repite en los proyectos de curso: casi todos los estudiantes hacen que la aplicacion se conecte con un usuario que tiene todo, porque asi nunca aparece un error de permisos y se avanza mas rapido. Ese atajo es exactamente el que convierte una vulnerabilidad menor en una fuga total.

Caso tres, perdida de datos durante una migracion. En marzo de 2019 MySpace reconocio que habia perdido la musica subida a la plataforma entre 2003 y 2015, del orden de cincuenta millones de archivos de unos catorce millones de artistas, durante una migracion de servidores; no hubo ataque ni desastre natural, solo una migracion sin copia verificada de la que ya no se podia volver atras. En la banca hay un caso paralelo y bien documentado con el sistema de TSB en Reino Unido en 2018, donde el paso a una plataforma nueva dejo a millones de clientes sin acceso confiable durante semanas, con costos reportados del orden de cientos de millones de libras y sanciones posteriores del regulador; la causa raiz senalada en los informes no fue un error puntual de programacion sino una migracion probada de forma insuficiente y sin un camino de retorno real. La leccion tecnica es la misma en los dos casos y conecta con la Clase 12: una migracion sin plan de retorno probado es una apuesta, y el plan de retorno se prueba antes, no el dia del cambio. La forma disciplinada de hacerlo es la secuencia de expandir, migrar y contraer, con las dos versiones conviviendo, mas una verificacion de conteos entre origen y destino antes de eliminar nada.

Caso cuatro, concurrencia. Este merece un tratamiento distinto porque su rasgo caracteristico es que no llega a los titulares con nombre propio tan facilmente: son fallos que no producen mensajes de error y por eso se descubren semanas despues, cuando el inventario fisico no coincide con el del sistema o cuando dos clientes reclaman el mismo cupo. El patron es siempre uno de los tres que se estudiaron en la Clase 10. Actualizacion perdida: dos procesos leen el mismo stock de Insumo, digamos cinco unidades, ambos restan tres y ambos escriben dos, con lo cual se despacharon seis unidades y el sistema declara dos existencias que no estan. Doble reserva: dos recepcionistas consultan la franja del martes a las diez del veterinario Ruiz, ambas reciben cero filas, ambas insertan. Bloqueo mutuo o deadlock: dos transacciones se esperan en orden cruzado y el motor mata una. La leccion es que ninguna cantidad de validacion previa en la aplicacion resuelve esto, porque entre la consulta y la escritura hay una ventana de tiempo en la que el mundo cambio; se resuelve en la base con restricciones, con bloqueo explicito al leer lo que se va a modificar o con el nivel de aislamiento adecuado. Y hay una leccion organizacional gratis: estos defectos jamas aparecen probando con un usuario, asi que si el estudiante solo probo VetCare desde una sola maquina, no lo probo.

Lo que decide la calificacion de hoy no es reunir casos sino escribir lecciones accionables, y esa es la habilidad que el estudiante debe practicar sin ayuda. Una leccion es un lugar comun cuando podria haberse escrito antes de conocer el caso: hay que hacer respaldos, hay que cuidar los permisos, hay que probar bien. Una leccion es accionable cuando tiene cuatro elementos verificables: un verbo concreto, el artefacto sobre el cual se actua, una frecuencia o un umbral, y la manera de comprobar que se hizo. Compare las dos versiones. Version inutil: hay que probar los respaldos. Version accionable: el primer lunes de cada mes se restaura el respaldo mas reciente en un esquema temporal de Oracle Live SQL o del entorno de pruebas, se comparan los conteos de filas de Dueno, Mascota, Cita y Factura contra produccion, y se registra fecha y resultado en la bitacora del proyecto; si no hay registro del mes, se declara que no hay respaldo. La segunda se puede auditar, la primera es una intencion. Aplique el mismo molde a los otros casos y ya tiene la cuarta columna de la tabla: del caso de permisos sale crear el rol rol_vetcare_app con GRANT EXECUTE sobre los procedimientos y revocar todo SELECT, INSERT, UPDATE y DELETE directo sobre las tablas, verificado consultando las vistas de privilegios; del caso de concurrencia sale ALTER TABLE Cita ADD CONSTRAINT uq_cita_vet_franja UNIQUE (id_veterinario, fecha_hora) mas SELECT FOR UPDATE al descontar stock, verificado con dos sesiones simultaneas; del caso de migracion sale que todo cambio de esquema tenga script de ida, script de retorno y conteo de verificacion. Sobre las preguntas que llegaran por el canal del curso: si piden inventar un caso, la respuesta es no, cada caso debe ser verificable con una fuente publica o declararse explicitamente como hipotetico; si el caso no tiene detalle tecnico publicado, se escribe solo lo documentado y se marca aparte lo que es inferencia propia, porque separar hecho de suposicion es parte de la nota; y si preguntan cuanto debe medir cada celda, la convencion de este entregable es de tres a cinco lineas.

Error tipico del docente que no domina el tema: el primero es dejar que la actividad se convierta en una coleccion de historias de desastres, con cifras espectaculares y ninguna cadena causal. El estudiante sale creyendo que las bases de datos fallan por mala suerte o por gente descuidada, no por decisiones tecnicas identificables, y en el Parcial 3 de la Clase 14, cuando se le pida diagnosticar por que una operacion de VetCare se degrada o pierde datos, responde con generalidades morales en lugar de senalar el indice que falta, el privilegio que sobra o el bloqueo que no se pidio. El segundo es no exigir la cuarta columna, la del cambio concreto en VetCare, o aceptarla escrita en infinitivo vago del tipo mejorar la seguridad. Sin ese cierre el ejercicio no deja rastro en el proyecto, y en la sustentacion de la Clase 15 el estudiante no puede mostrar ni una linea de DDL, ningun GRANT y ninguna prueba de restauracion que se derive del analisis, con lo cual queda demostrado que la lectura de casos se hizo para entregar y no para decidir.


**Demo que usted debe poder repetir:** Plantilla: contexto -> fallo -> leccion -> cambio en VetCare.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 13 - Analisis de casos reales/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 13 · Analisis de casos reales · VetCare
2. Encuadre de hoy · Objetivo PI
3. Mapa del bloque de hoy (120 min)
4. Teoria Core (breve)
5. Demo del dia
6. Herramientas de hoy
7. Actividad autonoma — contexto / por que importa
8. Actividad autonoma — objetivo y criterios
9. Actividad autonoma — escenario / datos de partida
10. Actividad autonoma — pasos guiados
11. Actividad autonoma — pistas (checklist vacio)
12. Criterios de exito / entregable
13. Para el PI esta semana
14. Cierre · Clase 13

> Privado, no se proyecta: `Kit docente/Clase 13/Solucion Taller Clase 13 - VetCare.docx`

## Plan minuto a minuto (120 min equivalentes — trabajo autonomo)

> El estudiante trabaja sin encuentro sincrono. Usted publica este guion resumido + taller en ExamLab.

### Bloque A (0-20) · Encuadre PI
**Decir/publicar:** «Hoy avanzamos el PI en: Informe de caso -> mejoras concretas al PI. No es un taller suelto.»
Referencia slides: Agenda + Objetivo PI.

### Bloque B (20-45) · Teoria minima
Leer Teoria Core. Tomar notas en el informe del PI.

### Bloque C (45-100) · Practica = entregable PI
Seguir el taller estudiante. Herramienta: Google Docs.
Salida esperada de la practica (publiquela junto al enunciado para que el
estudiante autonomo sepa si le quedo bien):
📸 Salida esperada de la demo de la Clase 13 [[captura: cap01_demo.png | receta: 1) Abra Google Docs y repita la demo de este bloque sobre el dominio VetCare (no otro ejemplo).  2) Capture la ventana en el momento en que se ve el resultado, no el escritorio completo.  3) Recorte a ~1200 px de ancho.  4) Guardela como Kit docente/Clase 13/Capturas/cap01_demo.png.  5) Vuelva a generar el guion: la imagen queda embebida aqui sola.]]

### Bloque D (100-120) · Empaquetado y cierre
Subir entregable a ExamLab. Actualizar el checklist PI del proyecto.


## Codigo / scripts
Carpeta Codigo/ — archivo N/A.

## Capturas
Carpeta `Kit docente/Clase 13/Capturas/`. Cada linea de pantallazo de arriba trae
el nombre exacto del archivo y, si todavia no existe, el paso a paso para producirlo:
tomelo, guardelo con ese nombre y vuelva a generar el guion — la imagen se embebe sola.
Detalle por captura en `Capturas/README_capturas.txt`.

## Criterios de exito del dia
- Cada estudiante tiene el entregable o sus gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
