# Guion docente · Clase 13 · Analisis de casos reales · VetCare

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** AUTONOMA (festivo, sin encuentro sincrono)
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** Informe de caso -> mejoras concretas al PI
- **Entregable de hoy:** Informe 1-2 pag.: caso + 3 mejoras aplicables a VetCare
- **Herramienta:** Google Docs
- **Slides:** Clases/Clase 13 - Analisis de casos reales/Presentacion.pptx
- **Caso de estudio (anexo del estudiante):** `Clases/Proyecto Integrador/Anexo - Caso de estudio Clinica Huellitas - Bases de Datos II.docx`
  — perfil de la clinica, las 8 entidades, las 3 reglas, el elenco de nombres y la escala por clase.
  Remita a este anexo cada vez que alguien pregunte «que datos guarda» o «de que tamano es esto».

> Sin mapa completo del curso, sin bio del docente, sin fechas de periodo.
> Presentacion del Curso / Acuerdo cubren logistica global.

## Fundamento teorico para el docente (al servicio del PI)

El objetivo de la clase no es «cubrir un capitulo» aislado, sino producir evidencia
del PI VetCare. La teoria se limita a desbloquear el taller.


## Guion por diapositiva

Es el mismo texto que llevan las **notas del presentador** de cada lámina: qué decir al entrar y en cada clic, el ejemplo, las preguntas típicas y el puente a la siguiente.

### [Slide 2] Encuadre de hoy · Tema y objetivo

QUÉ ES (dilo así): Hoy no hay técnica nueva: se usa lo del semestre para entender fallos reales. La pregunta de la clase es una sola: cuando una base falla en producción, ¿qué falló de verdad y qué se cambia para que no vuelva a pasar?

CÓMO DARLA (≈3 min):
- Al entrar: La clase cae en festivo (2 de noviembre) y no hay encuentro en vivo. Si grabas una explicación corta, abre con la pregunta de la clase y avisa que las láminas se leen en orden y que cada una se entiende sola.
- Antes de empezar: Recuerda al grupo que el Parcial 3 (Clase 14, 9 de noviembre) incluye esta clase autónoma: es la que más se olvida al estudiar.

CUIDADO: No la presentes como «clase de relleno»: el análisis de incidentes es una práctica profesional con nombre propio, el post-mortem.

PASA A LA SIGUIENTE: Empezamos por ese documento: el post-mortem.

### [Slide 3] Mapa del bloque de hoy (120 min)

QUÉ ES (dilo así): El reparto orientativo de las dos horas de trabajo autónomo: teoría con una lámina por concepto, un análisis guiado completo y la práctica opcional de la carpeta.

CÓMO DARLA (≈1 min):
- Al entrar: Señala los tramos sin detenerte. La teoría, leída con calma, toma unos 50 minutos (más que el tramo 10-35); el «demo» de hoy es el análisis guiado de la lámina «Demo del día», y la práctica empieza hacia el minuto 65.

PASA A LA SIGUIENTE: Primer concepto: qué es un post-mortem.

### [Slide 4] El post-mortem analiza el fallo, no a la persona

QUÉ ES (dilo así): Cuando un sistema falla en producción, los equipos serios no se quedan en «se cayó»: escriben un post-mortem, un documento corto que reconstruye el fallo y decide qué cambiar. La regla del oficio es que no se buscan culpables: se busca la condición del sistema que dejó que un error común se volviera un problema grande.

CÓMO DARLA (≈4 min):
- Al entrar: La falla en producción y, a la derecha, el documento que se escribe después. «Post-mortem» es literalmente «después de la muerte» del servicio; es breve, no un libro.
- Clic 1: Las cuatro preguntas, en orden. Subraya la 3, en otro color: «por qué fue posible» es la causa raíz, el tema de la lámina siguiente. El impacto se mide: datos, horas, dinero o personas afectadas.
- Clic 2: La banda verde: sin culpables. Explica el porqué práctico: si el documento sirve para castigar, la gente esconde los errores pequeños y la organización se queda sin aviso de los grandes.

EJEMPLO: Un post-mortem de cuatro líneas en la clínica: «A las 9:10 se borraron las citas del día; a las 9:40 se restauraron desde el respaldo de la noche y se perdieron las creadas en esa media hora; fue posible porque el usuario de la aplicación podía hacer DELETE sin WHERE; se cambia: la aplicación pierde el permiso DELETE sobre cita».

SI PREGUNTAN:
- «¿Y si alguien lo hizo mal a propósito?» → Eso ya no es un incidente sino un asunto de seguridad o disciplinario, y va por otro camino. El post-mortem trata los errores honestos, que son casi todos.
- «¿Hace falta post-mortem si el fallo no llegó al usuario?» → Sí: el que se detuvo a tiempo es el más barato de estudiar. Incidente es todo evento que degrada el servicio o pone en riesgo los datos.

CUIDADO: «Sin culpables» no es «sin responsables»: cada acción de mejora tiene un responsable y una fecha. Lo que no hay es castigo por el error honesto.

PASA A LA SIGUIENTE: Para responder la tercera pregunta hay que separar dos causas: la próxima y la raíz.

### [Slide 5] Causa proxima y causa raiz: la distincion que separa el analisis de la anecdota

QUÉ ES (dilo así): Todo fallo tiene una causa que se ve y otra que lo permitió. La que se ve, la próxima, casi nunca se puede eliminar: los discos fallan y la gente se equivoca. La raíz sí se cambia, y se encuentra preguntando por qué hasta llegar a un procedimiento, un permiso, una restricción o una alarma.

CÓMO DARLA (≈4 min):
- Al entrar: Arriba, lo que se ve: el disco falla un viernes y se pierden tres semanas de historias clínicas. La etiqueta roja dice «causa próxima». Pregunta: «¿la solución es comprar discos que no fallen?».
- Clic 1: Tres «¿por qué?» bajan a la caja azul: había un respaldo que nadie había restaurado nunca, y nadie vigilaba si el del día se ejecutaba. Esa es la causa raíz, y esa sí se puede cambiar.
- Clic 2: La regla para saber cuándo parar: si la respuesta nombra a una persona («Pedro borró»), sigue preguntando; si nombra algo que se cambia (un permiso, una restricción, una alarma), llegaste.

EJEMPLO: «Se borró la agenda» → ¿por qué? «Alguien corrió DELETE sin WHERE» (nombra una persona: seguir) → ¿por qué pudo? «El usuario de la aplicación tiene DELETE sobre cita» (un permiso: raíz). La mejora es quitar ese permiso.

SI PREGUNTAN:
- «¿Siempre son cinco «por qué»?» → No: cinco es una guía. Se para cuando la respuesta es algo que se puede cambiar; a veces son tres y a veces seis.
- «¿Y que fuera de noche o que quien sabía restaurar estuviera de vacaciones?» → Son factores contribuyentes: empeoraron el resultado sin causarlo. Se anotan aparte; no son la raíz.

CUIDADO: No aceptes «error humano» como causa raíz: es la causa próxima de casi todo. La pregunta correcta es por qué el sistema dejó que ese error tuviera consecuencias.

PASA A LA SIGUIENTE: Con esta herramienta vamos al primer caso real, el mejor documentado.

### [Slide 6] Caso uno: el respaldo que nunca se restauro (GitLab, 2017)

QUÉ ES (dilo así): GitLab, un servicio en la nube para guardar código, perdió datos en 2017. El error humano fue corriente; lo que lo volvió histórico fue descubrir, en plena emergencia, que ninguno de sus respaldos servía como se creía.

CÓMO DARLA (≈4 min):
- Al entrar: La causa próxima: atendiendo un problema de replicación, un ingeniero ejecutó un borrado recursivo del directorio de datos en el servidor equivocado. Unos 300 GB.
- Clic 1: La causa raíz: al intentar recuperar, los cinco mecanismos de respaldo y replicación fallaban. Dos ejemplos: el volcado lógico fallaba en silencio por una diferencia de versión entre cliente y servidor, y las copias remotas estaban vacías.
- Clic 2: El desenlace: se restauró una copia de unas seis horas antes; lo creado en esa ventana se perdió para siempre (miles de proyectos y comentarios).
- Clic 3: Las dos lecciones: un respaldo nunca restaurado no es un respaldo, y el RPO (Clase 4: cuántos datos se acepta perder, medido en tiempo) no se declara: se demuestra restaurando.

EJEMPLO: En la clínica: si el respaldo de la noche nunca se ha restaurado en una base de prueba, nadie sabe si el RPO real es de 24 horas o de tres semanas.

SI PREGUNTAN:
- «¿Por qué el volcado fallaba en silencio?» → Por una diferencia de versión entre el programa que hacía la copia y el servidor: daba error y nadie revisaba ese error. Un proceso que puede fallar sin avisar da una confianza que no existe.
- «¿Qué es el RPO?» → Recovery Point Objective: cuántos datos acepta perder la organización, medido en tiempo. Si el último respaldo bueno era de seis horas antes, el RPO real fue de seis horas.

CUIDADO: No lo cuentes como «un ingeniero borró la base»: esa es la causa próxima, justo el error de análisis de la lámina anterior. El caso enseña que cinco respaldos sin probar equivalen a ninguno.

PASA A LA SIGUIENTE: Segundo caso: no se perdió nada; se leyó lo que no se debía, por un permiso de más.

### [Slide 7] Caso dos: permisos excesivos (Capital One, 2019)

QUÉ ES (dilo así): Capital One, un banco de Estados Unidos, tuvo en 2019 una fuga de datos sin ninguna hazaña técnica: una configuración incorrecta abrió la puerta, y un permiso de más hizo que detrás de esa puerta estuviera todo.

CÓMO DARLA (≈3 min):
- Al entrar: La cadena, de arriba abajo: cortafuegos mal configurado (causa próxima) → el servidor hace peticiones internas a pedido del atacante → entrega credenciales temporales de un rol de servicio.
- Clic 1: Lo que ese rol podía leer. Los 12 recuadros son un esquema, no a escala: verde, lo que su función necesitaba; rojo, todo lo demás que también podía listar y leer.
- Clic 2: La causa raíz: un privilegio mucho mayor que su función. La lección, con el vocabulario de la Clase 2: privilegio mínimo.

EJEMPLO: En la clínica, una aplicación que entra con el usuario dueño de todas las tablas repite el error: si alguien abusa de ella, tiene todo. Con un rol que solo puede ejecutar los procedimientos, el daño queda acotado.

SI PREGUNTAN:
- «¿El problema no fue el cortafuegos?» → Esa es la causa próxima. Con un rol de privilegio mínimo, la misma falla habría expuesto una fracción de los datos.
- «¿Por qué los proyectos de curso repiten este error?» → Porque conectarse con un usuario que tiene todo hace que nunca aparezca un error de permisos: es más rápido hoy y es la puerta abierta mañana.

CUIDADO: Usa las cifras publicadas: unos 100 millones de personas en EE. UU. y varios millones en Canadá, y una multa de 80 millones de dólares en 2020. No las redondees hacia arriba para dramatizar.

PASA A LA SIGUIENTE: Tercer caso: ni ataque ni comando equivocado; una migración sin camino de vuelta.

### [Slide 8] Caso tres: perdida de datos en una migracion (MySpace, 2019)

QUÉ ES (dilo así): Migrar es mover datos de un sistema a otro. MySpace lo hizo sin una copia verificada y sin poder volver atrás, y perdió doce años de música de sus usuarios. El mismo patrón aparece en la banca.

CÓMO DARLA (≈3 min):
- Al entrar: Los archivos viajan de los servidores viejos a los nuevos; los rojos se pierden en el camino. No había copia verificada: la franja roja son doce años de música, del orden de 50 millones de archivos.
- Clic 1: Lo que faltaba, en tres cajas: expandir, migrar y contraer (las dos versiones conviven mientras se migra), conteos que coincidan entre origen y destino antes de borrar nada, y un plan de retorno probado antes del día del cambio.
- Clic 2: La lección y el caso paralelo: TSB, un banco del Reino Unido, dejó en 2018 a millones de clientes sin acceso confiable durante semanas por una migración probada de forma insuficiente.

EJEMPLO: En la clínica, al mover las citas antiguas a una tabla histórica: se crea la tabla nueva, se copian las filas, se compara SELECT COUNT(*) en las dos y solo entonces se borran del origen.

SI PREGUNTAN:
- «¿Qué es expandir, migrar y contraer?» → Primero se agrega lo nuevo sin quitar lo viejo (expandir), luego se mueven los datos y la aplicación (migrar) y solo al final se retira lo viejo (contraer). Mientras tanto siempre hay a dónde volver.

CUIDADO: La causa raíz no es «el servidor nuevo falló»: es que se dio por terminada la migración sin haber comprobado el destino.

PASA A LA SIGUIENTE: Cuarto caso: el fallo que no da ningún mensaje de error.

### [Slide 9] Caso cuatro: concurrencia, el que no llega a los titulares

QUÉ ES (dilo así): La concurrencia es lo que pasa cuando dos usuarios trabajan sobre el mismo dato al mismo tiempo. Sus fallos no producen errores: el sistema queda mal en silencio y se descubre semanas después, cuando el inventario físico no cuadra o dos personas reclaman el mismo cupo.

CÓMO DARLA (≈4 min):
- Al entrar: El stock del insumo vale 5. Los dos procesos lo leen y los dos ven 5.
- Clic 1: Cada uno resta 3 y escribe 2. El número del centro pasa a 2 en rojo: la segunda escritura pisó a la primera.
- Clic 2: El resultado: salieron 6 unidades y el sistema dice 2, sin mensaje de error. Nombra los otros dos patrones de la Clase 10: la doble reserva de la misma franja y el bloqueo mutuo, en el que el motor aborta una de las dos transacciones.
- Clic 3: La defensa vive en la base: UPDATE condicional (stock = stock - 3 WHERE stock >= 3) o SELECT … FOR UPDATE al leer, y UNIQUE para la doble reserva. Validar antes en la aplicación no basta: entre leer y escribir hay una ventana.

EJEMPLO: UPDATE insumo SET stock = stock - 3 WHERE id_insumo = 2 AND stock >= 3; — si otro proceso ya descontó, esta sentencia actualiza 0 filas en vez de dejar un dato falso.

SI PREGUNTAN:
- «¿Por qué no lo vi al probar?» → Porque estos defectos solo aparecen con dos sesiones a la vez. Si se probó desde una sola máquina, no se probó.
- «¿Qué hace exactamente FOR UPDATE?» → Bloquea la fila leída hasta el COMMIT: la segunda sesión espera en vez de decidir con un dato que ya cambió.

CUIDADO: El título dice que este caso no llega a los titulares: no le inventes un nombre propio. Es un patrón, no una noticia.

PASA A LA SIGUIENTE: Quinto caso: el fallo de seguridad más documentado de la web.

### [Slide 10] Caso cinco: inyeccion de SQL, cuando el dato se vuelve codigo

QUÉ ES (dilo así): Inyectar SQL es colar código dentro de un dato. Pasa cuando la aplicación arma la consulta pegando lo que el usuario escribió: el texto deja de ser un dato y pasa a ser parte de la sentencia. La defensa es que el dato viaje aparte, como parámetro.

CÓMO DARLA (≈4 min):
- Al entrar: Recorre la ilustración de arriba abajo. Primero, lo que escribe el usuario: x' OR '1'='1.
- Camino 1: Pegado dentro de la sentencia: la comilla del texto cierra la cadena y el OR queda como código. La condición es siempre verdadera y salen todos los dueños.
- Camino 2: Ligado como parámetro: la sentencia lleva $1 y USING entrega el valor aparte. El texto completo se compara como un nombre y salen 0 filas: nadie se llama así.
- Banda final: Escapar comillas a mano no equivale: basta olvidarlo en un sitio. La regla: el dato nunca viaja como código.

EJEMPLO: TalkTalk, Reino Unido, octubre de 2015: una inyección de SQL en páginas web heredadas que nadie había actualizado expuso datos personales de unos 157.000 clientes; el regulador de protección de datos la multó con 400.000 libras en 2016.

SI PREGUNTAN:
- «¿Y si le quito las comillas a lo que escribe el usuario?» → Rompe nombres legítimos como O'Brien y basta olvidarlo en un solo sitio. El parámetro ligado lo resuelve siempre, porque el dato nunca se interpreta.
- «¿El PREPARE de la Clase 12 es lo mismo?» → Es el mismo principio: la sentencia con huecos y los valores aparte. EXECUTE … USING es su forma dentro de PL/pgSQL.

CUIDADO: No digas que la inyección «borra la base» siempre: el ataque típico lee datos, como aquí. Lo que puede hacer depende del rol con que entra la aplicación: otra vez, privilegio mínimo.

PASA A LA SIGUIENTE: Veámoslo en código: la misma búsqueda, insegura y segura.

### [Slide 11] SQL dinamico: concatenar el texto o ligar el parametro

QUÉ ES (dilo así): Dos funciones que buscan un dueño por nombre con SQL dinámico: la sentencia se arma como texto y se ejecuta con EXECUTE. La única diferencia es cómo entra el nombre: pegado al texto o ligado como parámetro.

CÓMO DARLA (≈4 min):
- Al entrar: Presenta la lámina como «la misma función dos veces»; señala las dos cabeceras, MAL y BIEN.
- Líneas 1-7: La versión insegura: RETURN QUERY EXECUTE ejecuta un texto armado con || (concatenar). Cada '' dentro de la cadena es UNA comilla escrita: el nombre queda entre comillas dentro de la sentencia.
- Líneas 9-15: La versión segura: el texto lleva $1 donde va el dato y USING p_nombre entrega el valor por separado. El motor nunca lo lee como SQL.
- Líneas 17-18: La prueba: el mismo texto de ataque contra las dos. La insegura devuelve todos los dueños; la segura, 0.

EJEMPLO: Con los 6 dueños de ejemplo: el COUNT(*) del ataque contra buscar_dueno_inseguro da 6 y contra buscar_dueno_seguro da 0; buscar_dueno_inseguro('Ana Gomez') devuelve una fila (id 1), así que el uso normal funciona igual en las dos.

SI PREGUNTAN:
- «¿Por qué no WHERE nombre = p_nombre, sin EXECUTE?» → Es todavía mejor cuando la consulta es fija: una consulta estática usa el parámetro siempre como valor. EXECUTE solo hace falta si la sentencia cambia, por ejemplo la tabla o la columna.
- «¿Qué pasa si alguien busca O'Brien en la insegura?» → Falla con «syntax error at or near "Brien"»: la comilla del nombre cierra la cadena. Es la misma grieta por la que entra el ataque.

CUIDADO: Las dos comillas seguidas ('') dentro de una cadena SQL son una sola comilla escrita, no una cadena vacía; si las confundes al dictar, nadie entiende por qué funciona el ataque.

PASA A LA SIGUIENTE: Sexto caso: no es de seguridad ni de pérdida, sino de rendimiento.

### [Slide 12] Caso seis: el reporte que tumba el servicio (rendimiento)

QUÉ ES (dilo así): No todos los incidentes son pérdidas o ataques: muchos son una consulta lenta que se ejecuta demasiado seguido. Ninguna ejecución falla; el servicio cae porque se queda sin recursos. Es el caso que más se repite y menos se cuenta.

CÓMO DARLA (≈4 min):
- Al entrar: Recorre la ilustración en tres franjas, de arriba abajo.
- Arriba: Un reporte programado cada minuto (min 0 a 5) en el que cada ejecución tarda más que un minuto y más que la anterior, porque compiten entre sí: la siguiente empieza antes de que termine la anterior y se apilan.
- Centro: En el minuto 5 hay tres reportes a la vez y, en hora pico, la aplicación usa el resto: las 10 conexiones del esquema quedan ocupadas y la siguiente petición de recepción no consigue ninguna.
- Abajo: Lo que dice el plan: Seq Scan sobre la tabla grande, que recorre todo para quedarse con pocas filas, es la firma de un índice que falta. La lección accionable: solo las columnas que se muestran e índice en el filtro, medido con EXPLAIN ANALYZE antes y después.

EJEMPLO: En la clínica: un tablero que cada minuto cuenta las citas del día leyendo toda la tabla de citas, con años de historia, en lugar de usar un índice por fecha.

SI PREGUNTAN:
- «¿Por qué el SELECT * es parte del problema?» → Trae columnas que nadie mira: más datos leídos, más memoria y más red por ejecución. El reporte pide solo lo que muestra.
- «¿Cómo sé que el índice sirvió?» → Con EXPLAIN ANALYZE antes y después: el Seq Scan cambia por un Index Scan y el tiempo real baja. Si no se midió, no se sabe.

CUIDADO: No afirmes que un índice lo arregla siempre: si el filtro devuelve casi toda la tabla, el planeador hace bien en recorrerla. El índice ayuda cuando el filtro deja pocas filas.

PASA A LA SIGUIENTE: Cómo se lee el plan de una consulta que no escribiste tú.

### [Slide 13] Leer un plan de ejecucion ajeno

QUÉ ES (dilo así): EXPLAIN (ANALYZE, BUFFERS) ejecuta la consulta y muestra el plan que eligió el motor, con filas y tiempos reales. Los cuatro comentarios son el orden en que se lee un plan ajeno, el de un sistema que falla.

CÓMO DARLA (≈3 min):
- Al entrar: Primero la consulta y después los comentarios: son una lista de revisión.
- Líneas 1-8: La consulta: dueños con más de 5 citas desde el 1 de enero de 2026. EXPLAIN (ANALYZE, BUFFERS) delante la ejecuta de verdad y añade tiempos y páginas leídas.
- Comentario 1: Se busca el nodo con el costo más alto, no el primero de arriba: el plan es un árbol y se lee de adentro hacia afuera.
- Comentarios 2 y 3: Seq Scan sobre tabla grande con un filtro que deja pocas filas: falta un índice. Filas estimadas contra reales diez veces distintas: estadísticas viejas, ANALYZE.
- Comentario 4: Un Nested Loop con muchas filas suele indicar estimaciones malas; con estadísticas al día el planeador tiende a elegir Hash Join.

EJEMPLO: Con los datos de ejemplo (10 citas) el plan muestra Seq Scan on cita c con Filter: (fecha_hora >= '2026-01-01'::date), dos Hash Join y un HashAggregate que descarta a los 4 dueños con citas porque ninguno pasa de 5: devuelve 0 filas.

SI PREGUNTAN:
- «¿EXPLAIN ANALYZE es seguro en producción?» → Ejecuta la sentencia de verdad: con un SELECT solo cuesta su tiempo, pero con un UPDATE o un DELETE los cambios se aplican. A esos se les envuelve en BEGIN … ROLLBACK.
- «¿Qué agrega BUFFERS?» → Cuántas páginas se leyeron de memoria (shared hit) y cuántas de disco (read). Muchas lecturas de disco son la señal de una consulta cara.

CUIDADO: Con tablas pequeñas el Seq Scan es la decisión correcta: no lo presentes como error en la base de ejemplo de 10 citas. La alarma es con millones de filas.

PASA A LA SIGUIENTE: Ya hay seis casos. ¿Cómo se convierte un caso en una lección que sirva?

### [Slide 14] Lecciones accionables: los cuatro elementos verificables

QUÉ ES (dilo así): La parte difícil del análisis no es contar el caso sino sacar una lección que alguien pueda cumplir y otro pueda verificar. La prueba es simple: si la lección se pudo escribir antes de conocer el caso, es un lugar común.

CÓMO DARLA (≈4 min):
- Al entrar: La versión inútil, tachada: «hay que probar los respaldos». Pregunta: ¿quién la cumple, cuándo, y cómo sabemos que la cumplió? Nadie puede responder.
- Clic 1: La misma lección con sus cuatro partes: verbo (se restaura), artefacto (el respaldo más reciente, en una base de prueba), frecuencia (el primer lunes de cada mes) y comprobación (conteos de filas contra producción y bitácora con fecha y resultado).
- Clic 2: Por qué vale: se puede auditar. Si no hay registro del mes, se declara que no hay respaldo.

EJEMPLO: Del caso de permisos: crear rol_clinica_app con GRANT EXECUTE sobre los procedimientos y sin SELECT, INSERT, UPDATE ni DELETE directos, verificado consultando las vistas de privilegios. Del de concurrencia: ALTER TABLE cita ADD CONSTRAINT uq_cita_vet_franja UNIQUE (id_veterinario, fecha_hora).

SI PREGUNTAN:
- «¿Puedo inventar un caso?» → No. Cada caso tiene que poder verificarse con una fuente pública o declararse expresamente como hipotético.
- «¿Y si el caso no tiene detalle técnico publicado?» → Se escribe solo lo documentado y se marca aparte lo que es inferencia propia: separar hecho de suposición es parte del análisis.

CUIDADO: No aceptes lecciones en infinitivo vago («mejorar la seguridad», «optimizar»): sin artefacto y sin comprobación no son lecciones.

PASA A LA SIGUIENTE: Ahora, la lección del caso del respaldo convertida en dos objetos de la base.

### [Slide 15] Del caso a la mejora: el borrado con rastro y la restauracion comprobada

QUÉ ES (dilo así): Del caso GitLab salen dos mejoras que se confunden pero hacen cosas distintas. El archivo de borrados permite recuperar lo que se borró por error; la verificación demuestra que lo recuperado está completo. Sin la segunda, nadie sabe si la primera funcionó.

CÓMO DARLA (≈3 min):
- Al entrar: Presenta las dos columnas como dos controles distintos.
- Columna izquierda: El DELETE sigue siendo posible (el error humano no desaparece); el trigger BEFORE DELETE copia OLD a tarifa_borrada y devuelve OLD para que el borrado siga. Resultado: se puede volver.
- Columna derecha: El registro del respaldo guarda cuántas filas había (3); después de restaurar se cuenta otra vez y el CASE compara: 3 = 3, RESTAURACION OK. Resultado: se demuestra que se volvió completo.
- Abajo: Lo que le faltó a GitLab: tenía respaldos, pero ninguno se había comprobado restaurando.

EJEMPLO: Con la tabla tarifa de tres especies (CANINO 45000, FELINO 40000, OTRA 35000), un DELETE FROM tarifa sin WHERE deja 3 filas en tarifa_borrada; tras restaurar, registro 3, conteo 3, RESTAURACION OK. Si solo volvieran 2, el veredicto sería REVISAR.

SI PREGUNTAN:
- «¿El trigger no impide el borrado?» → No: devuelve OLD y el borrado sigue. Impedirlo sería otra decisión (quitar el permiso o un BEFORE con RAISE EXCEPTION). Este control acepta el error y prepara la vuelta.
- «¿Por qué no basta con el respaldo de la noche?» → Porque no tiene lo creado durante el día; el archivo guarda la fila exacta en el momento en que se borró.

CUIDADO: El conteo esperado se calcula con COUNT(*) al respaldar, no se escribe a mano: un número escrito a mano verifica contra lo que alguien creyó, no contra lo que había.

PASA A LA SIGUIENTE: Primero, el trigger en código.

### [Slide 16] El borrado con rastro: BEFORE DELETE y RETURN OLD

QUÉ ES (dilo así): Un trigger de archivo completo sobre una tabla pequeña y sin dependencias, la de tarifas por especie: la tabla donde se guarda lo borrado, la función que copia la fila y la asociación que la dispara antes de cada DELETE.

CÓMO DARLA (≈3 min):
- Al entrar: Recorre las piezas de arriba abajo.
- Líneas 1-2: La tabla de ejemplo, tarifa, con tres especies. Nadie apunta a ella con una clave foránea, así que se puede borrar sin tropezar con otras tablas.
- Líneas 4-9: La tabla tarifa_borrada: las columnas de tarifa más dos que se llenan solas, borrado_en (DEFAULT now()) y usuario_bd (DEFAULT current_user).
- Líneas 11-17: La función RETURNS TRIGGER: inserta los valores de OLD, que en un DELETE es la fila que se va, y termina en RETURN OLD.
- Líneas 19-21: La asociación: BEFORE DELETE ON tarifa, FOR EACH ROW. Corre una vez por cada fila borrada.

EJEMPLO: DELETE FROM tarifa WHERE especie = 'OTRA'; deja en tarifa_borrada la fila OTRA · 35000.00, con la fecha y el usuario de la base.

SI PREGUNTAN:
- «¿Por qué RETURN OLD y no RETURN NEW?» → En un DELETE no hay fila nueva: NEW es NULL. En un BEFORE, devolver NULL cancela la operación en silencio; devolver OLD la deja seguir.
- «¿Y si el borrado falla por una clave foránea?» → Se deshace toda la sentencia, incluida la copia que hizo el trigger: el archivo no queda con filas que en realidad no se borraron.

CUIDADO: Haz el ejemplo sobre tarifa y no sobre una tabla con dependencias: borrar un veterinario que tiene citas falla por la clave foránea («update or delete on table "veterinario" violates foreign key constraint»), y la tabla cita es la de la práctica.

PASA A LA SIGUIENTE: La segunda mejora: comprobar que la restauración quedó completa.

### [Slide 17] La restauracion comprobada: una consulta, un veredicto

QUÉ ES (dilo así): El ciclo completo en tres bloques: respaldar y anotar cuántas filas había, sufrir el accidente y volver desde el archivo, y una consulta que compara y dicta un veredicto.

CÓMO DARLA (≈3 min):
- Al entrar: Señala los tres comentarios numerados: son los tres momentos.
- Líneas 1-6: CREATE TABLE … AS SELECT copia la tabla tarifa; registro_respaldo guarda el conteo calculado con COUNT(*), no escrito a mano.
- Líneas 8-11: El accidente: DELETE sin WHERE. El trigger de la lámina anterior ya archivó cada fila; el INSERT … SELECT con columnas explícitas las devuelve.
- Líneas 13-20: La comprobación: una fila con las filas esperadas, las actuales y el veredicto del CASE. ORDER BY hecho_en DESC LIMIT 1 toma el respaldo más reciente si hubo varios.

EJEMPLO: Ejecutada después de la lámina anterior, la consulta final devuelve esperadas 3 · actuales 3 · RESTAURACION OK, y la tabla cita de la base sigue intacta. Si faltara una fila, devolvería 3 · 2 · REVISAR.

SI PREGUNTAN:
- «¿Por qué columnas explícitas en el INSERT?» → Porque tarifa_borrada tiene dos columnas más (borrado_en y usuario_bd): con SELECT * no coincidirían. Nombrarlas además protege si cambia el orden de las columnas.
- «¿Basta con comparar el conteo?» → Es el mínimo. Una verificación más fuerte compara también rangos o sumas, por ejemplo el MIN y el MAX de una fecha o la suma de los valores.

CUIDADO: Si una tabla con SERIAL se restaura con su id explícito en una tabla recién creada, la secuencia no avanza y el siguiente INSERT sin id choca con la llave primaria; se ajusta con setval. Aquí no pasa: la llave de tarifa es la especie.

PASA A LA SIGUIENTE: Con todo esto, el análisis guiado de un caso completo.

### [Slide 18] Demo del dia

QUÉ ES (dilo así): Como hoy no hay encuentro en vivo, la «demo» es un análisis completo hecho sobre un caso que no es el de la práctica: Capital One. Muestra la forma que debe tener cualquier análisis, de punta a punta.

CÓMO DARLA (≈15 min):
- Al entrar: Recorre las seis filas de la ilustración de arriba abajo, leyendo cada una en voz alta como una frase del informe.
- Filas 2 y 3: Qué falló y causa raíz por separado: el cortafuegos es la causa próxima; la raíz es el rol que podía leerlo todo.
- Filas 5 y 6: La lección tiene comprobación (revisión mensual contra la matriz) y el cambio nombra un objeto de la base: la aplicación entra con su propio rol, con GRANT EXECUTE y sin SELECT directo.
- Si tienes una base a mano: Ejecuta en orden las tres láminas de código (SQL dinámico, trigger de archivo y restauración comprobada) y muestra cada salida: 6 contra 0, las 3 filas en tarifa_borrada y el RESTAURACION OK.

EJEMPLO: Cambio en la base, escrito para la clínica: «la aplicación se conecta como rol_clinica_app, que tiene GRANT EXECUTE sobre los procedimientos y ningún privilegio directo sobre las tablas; se verifica en las vistas de privilegios».

SI PREGUNTAN:
- «¿Cuánto debe medir el análisis?» → Media página: lo que cabe en seis secciones breves.
- «¿Puedo usar uno de los casos de las láminas?» → Sí, o uno propio documentado con su fuente. Lo que no vale es inventarlo.

CUIDADO: Que el análisis no se quede en la noticia: la fila 6, el cambio en la base propia, es la que conecta el caso con el proyecto y la que más se olvida.

PASA A LA SIGUIENTE: Cierre de la clase.


**Demo que usted debe poder repetir:** Plantilla: contexto -> fallo -> leccion -> cambio en VetCare.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 13 - Analisis de casos reales/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 13 · Analisis de casos reales · la clínica
2. Encuadre de hoy · Tema y objetivo
3. Mapa del bloque de hoy (120 min)
4. El post-mortem analiza el fallo, no a la persona
5. Causa proxima y causa raiz: la distincion que separa el analisis de la anecdota
6. Caso uno: el respaldo que nunca se restauro (GitLab, 2017)
7. Caso dos: permisos excesivos (Capital One, 2019)
8. Caso tres: perdida de datos en una migracion (MySpace, 2019)
9. Caso cuatro: concurrencia, el que no llega a los titulares
10. Caso cinco: inyeccion de SQL, cuando el dato se vuelve codigo
11. SQL dinamico: concatenar el texto o ligar el parametro
12. Caso seis: el reporte que tumba el servicio (rendimiento)
13. Leer un plan de ejecucion ajeno
14. Lecciones accionables: los cuatro elementos verificables
15. Del caso a la mejora: el borrado con rastro y la restauracion comprobada
16. El borrado con rastro: BEFORE DELETE y RETURN OLD
17. La restauracion comprobada: una consulta, un veredicto
18. Demo del dia
19. Cierre · Clase 13

> Privado, no se proyecta: `Kit docente/Clase 13/Solucion Taller Clase 13 - VetCare.docx`

## Plan minuto a minuto (120 min equivalentes — trabajo autonomo)

> El estudiante trabaja sin encuentro sincrono. Usted publica este guion resumido + taller en ExamLab.

### Bloque A (0-20) · Encuadre PI
**Decir/publicar:** «Hoy avanzamos el PI en: Informe de caso -> mejoras concretas al PI. No es un taller suelto.»
Referencia slides: Encuadre + Mapa del bloque.

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
