# -*- coding: utf-8 -*-
"""Genera material completo BD II 2026-2 centrado en PI VetCare DB.

Salidas:
  Clases/Clase N - <slug>/Presentacion.pptx + Taller PI ....docx
  Kit docente/Clase N/Guion....md|.docx + Quiz + Codigo + Capturas/
  Kit docente/Clase N/Guia aplicacion parcial (dias 5/9/14)
"""
from __future__ import annotations
import os, sys, re, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLIDES = Path(__file__).resolve().parent
sys.path.insert(0, str(SLIDES))

from uniajc_slides_engine import (
    new_prs, content_slide, table_content, box_note_slide, closing_slide,
    class_cover, herramientas_slide, steps_visual_slide, checklist_slide,
    block_timeline_slide, diagram_boxes_slide, pseudo_code_slide,
    before_after_slide, AMARILLO, NAVY, CIAN,
    RED as PPTX_RED,
)
from uniajc_quiz_helpers import clave_text, pptx_chunks, q_abierta, q_om, q_vf, student_lines
from bd2_taller_data import HERRAMIENTAS_DIA, TALLER_BLOQUE, SOLUCION
from docx import Document
from docx.shared import Pt as DocPt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

CURSO = ROOT / "Bases de Datos II"
CLASES_DIR = CURSO / "Clases"
KIT_DIR = CURSO / "Kit docente"
PARCIALES = CURSO / "Parciales"
AZUL = RGBColor(0x09, 0x52, 0x92)
CIAN_D = RGBColor(0x26, 0x9C, 0xCB)
GRIS = RGBColor(0x2B, 0x2B, 0x2B)
BLANCO = RGBColor(0xFF, 0xFF, 0xFF)
FONT = "Calibri"

CLASES = [
  dict(n=1, tipo="regular", slug="Revision BD I y arranque VetCare",
    titulo="Revision BD I · Arranque VetCare DB",
    subtitulo="Diagnostico · dominio PI · primer modelo",
    herramienta="draw.io + DB Fiddle",
    hito_pi="Arranque PI: dominio, alcance y borrador ER de VetCare DB",
    entregable="Ficha de equipo + ER borrador (PNG) + lista de entidades/reglas",
    teoria=["Modelo entidad-relacion: una tabla = conjunto de entidades del mismo tipo; cada fila es una instancia, cada columna un atributo. La clave primaria (PK) identifica sin ambiguedad cada fila: nunca se repite, nunca es nula.",
            "Clave foranea (FK): columna que apunta a la PK de otra tabla y materializa una relacion (1-N o N-N via tabla intermedia). Garantiza integridad referencial: la BD rechaza una Cita con id_mascota que no existe.",
            "Normalizacion 1FN-3FN en una frase cada una: 1FN = nada de listas dentro de una celda (una fila = una mascota, no varias); 2FN = ningun atributo depende solo de una parte de una PK compuesta; 3FN = ningun atributo depende de otro atributo que no sea la PK. Sub-normalizar genera anomalias de insercion/actualizacion/borrado (ej.: cambiar el telefono de un dueno en 5 filas distintas); sobre-normalizar multiplica JOINs sin necesidad real.",
            "Error de docente que no domina el tema: confundir PK con 'el primer campo de la tabla', o asumir que normalizar siempre mejora el rendimiento (en lectura intensiva a veces se denormaliza a proposito, y eso se vera en Clase 6-7).",
            "Dominio VetCare y sus relaciones: Dueno 1-N Mascota, Mascota 1-N Cita, Veterinario 1-N Cita, Consulta 1-1 Cita (una consulta documenta una cita atendida), Factura 1-N DetalleFactura N-1 Insumo.",
            "Reglas de negocio del PI que ya anticipan clases futuras: mascota inactiva no puede tener cita nueva (se validara con un procedimiento en Clase 3), stock de insumo nunca queda negativo (transacciones, Clase 8), cambios sensibles quedan auditados (triggers, Clase 4)."],
    demo="Boceto ER en draw.io (Dueno-Mascota-Cita) + CREATE TABLE minimo en DB Fiddle.",
    taller=["Formar equipo (2-3) y nombrar el proyecto VetCare DB.",
            "Listar entidades minimas + 3 reglas de negocio propias.",
            "Dibujar ER borrador en draw.io/Excalidraw y exportar PNG.",
            "Escribir 5-8 lineas de alcance (que SI / que NO hara el PI)."],
    quiz=True, sql="01_arranque_vetcare.sql"),
  dict(n=2, tipo="autonoma", slug="Administracion de bases de datos",
    titulo="Administracion de BD · Roles VetCare",
    subtitulo="Clase autonoma · privilegios y usuarios del PI",
    herramienta="Oracle Live SQL / DB Fiddle + Google Docs",
    hito_pi="Plan de roles/privilegios de VetCare",
    entregable="Documento Roles_VetCare + script GRANT/REVOKE (o plan equivalente)",
    teoria=["Administracion de BD = gestionar QUIEN puede hacer QUE sobre CADA objeto. Tres piezas: usuario (identidad que se conecta), rol (paquete de privilegios con nombre, ej. RECEPCION), privilegio (permiso atomico: SELECT, INSERT, UPDATE, DELETE, EXECUTE sobre un objeto concreto).",
            "Principio de minimo privilegio: cada rol recibe solo lo que necesita para su funcion, ni un privilegio mas. No es paranoia, es reduccion de superficie de dano: si roban la sesion de un recepcionista, no debe poder borrar el historial clinico ni ver nomina.",
            "Separacion de funciones (segregation of duties): quien disena/modifica el esquema (DDL: CREATE/ALTER/DROP) no deberia ser la misma cuenta que opera datos del dia a dia (DML: INSERT/UPDATE/DELETE), y quien audita solo deberia leer (SELECT), nunca escribir.",
            "GRANT otorga un privilegio a un rol o usuario; REVOKE lo retira. Un rol se puede asignar a varios usuarios (todos los recepcionistas heredan el rol RECEPCION) y modificar en un solo lugar en vez de uno por uno.",
            "Error de docente que no domina el tema: crear un unico usuario 'admin' que todos comparten (rompe la trazabilidad de auditoria) o dar DBA/ALL PRIVILEGES a todo el equipo 'para que no falle nada' — exactamente lo opuesto a minimo privilegio.",
            "En el playground (Live SQL / DB Fiddle) el motor puede restringir CREATE ROLE o GRANT reales: cuando eso pase, el equipo redacta la matriz rol x objeto x privilegio como documento/plan, y ejecuta lo que el playground SI permita como evidencia parcial — no es escusa para omitir el analisis."],
    demo="Matriz rol x objeto x privilegio sobre tablas VetCare.",
    taller=["Definir >=4 roles (ADMIN_BD, RECEPCION, VETERINARIO, AUDITOR).",
            "Matriz SELECT/INSERT/UPDATE/DELETE/EXECUTE por objeto clave.",
            "Justificar privilegio minimo (least privilege).",
            "Redactar 1 pagina: politica de altas/bajas de usuarios."],
    quiz=True, sql="02_roles_vetcare.sql"),
  dict(n=3, tipo="regular", slug="Procedimientos almacenados",
    titulo="Procedimientos almacenados · VetCare",
    subtitulo="Logica de negocio en la BD del PI",
    herramienta="Oracle Live SQL",
    hito_pi=">=1 procedimiento de negocio (agendar cita / registrar consulta)",
    entregable="Script proc + casos de prueba (captura o enlace Live SQL)",
    teoria=["Un procedimiento almacenado (stored procedure) es un bloque de codigo SQL/PLSQL con nombre propio, guardado y compilado DENTRO de la base de datos, que se invoca con CALL o EXECUTE en vez de reescribir la logica cada vez.",
            "Parametros: IN (entra un valor, ej. p_id_mascota), OUT (el proc devuelve un valor al que lo llamo, ej. p_msg con el resultado), IN OUT (ambos). A diferencia de una consulta suelta, un proc puede recibir varios parametros y ejecutar varias sentencias como una sola unidad logica.",
            "Ventaja central para el PI: sin proc, cada pantalla de la futura app (o cada integrante del equipo) reescribiria la regla 'mascota inactiva no agenda' con su propio SQL, y tarde o temprano alguien la escribe distinto o la olvida. Con el proc, la regla vive UNA vez dentro de la BD; toda la app la respeta sin excepcion.",
            "Manejo de errores controlado: en vez de dejar que la insercion falle con un error crudo de motor, el proc valida primero (SELECT activa FROM mascota) y responde con un mensaje de negocio claro ('ERROR: mascota inactiva; no se agenda'), y usa EXCEPTION/TRY-CATCH segun el motor para capturar fallos inesperados sin tumbar la transaccion completa.",
            "Diferencia con una funcion (se vera en Clase 4): el procedimiento se ejecuta como una accion (CALL sp_algo), la funcion se invoca dentro de una expresion SQL y retorna un valor (SELECT fn_algo(x) FROM ...).",
            "Error de docente que no domina el tema: escribir el proc sin validar nada (solo el INSERT) y llamarlo 'logica de negocio' — un proc sin reglas de validacion es solo una consulta con nombre, no resuelve el problema que motiva usar procedimientos."],
    demo="CREATE PROCEDURE sp_agendar_cita(...) con validacion de mascota activa.",
    taller=["Implementar sp_agendar_cita o sp_registrar_consulta en Live SQL.",
            "Incluir validacion de negocio del PI (>=1).",
            "Ejecutar 2 pruebas: caso OK + caso error.",
            "Documentar firma del proc (contrato para la futura app)."],
    quiz=True, sql="03_procs_vetcare.sql"),
  dict(n=4, tipo="regular", slug="Funciones disparadores seguridad respaldo",
    titulo="Funciones · Triggers · Seguridad y respaldo",
    subtitulo="Integridad + RAA1 del PI VetCare",
    herramienta="Oracle Live SQL + Google Docs",
    hito_pi=">=1 funcion + >=1 trigger + borrador plan de respaldo",
    entregable="Scripts funcion/trigger + Plan_Backup_VetCare (1 pag.)",
    teoria=["Funcion (Clase 3 vio procedimiento): retorna un valor y se usa DENTRO de una expresion SQL, ej. SELECT fn_precio_base(especie) FROM mascota. Debe ser determinista y sin efectos secundarios pesados; si necesita modificar datos y ejecutarse como accion independiente, es un procedimiento, no una funcion.",
            "Trigger (disparador): bloque de codigo que el motor ejecuta AUTOMATICAMENTE cuando ocurre un evento (BEFORE/AFTER INSERT, UPDATE o DELETE) sobre una tabla, sin que nadie lo llame explicitamente. Dos usos tipicos aqui: auditoria (guardar quien/cuando cancelo una cita) y validacion de invariantes (que el stock nunca quede negativo tras un UPDATE).",
            "Riesgo real de los triggers: son invisibles en el codigo de la app (un desarrollador que solo mira el INSERT no ve que ademas se dispara una auditoria), y pueden encadenarse (un trigger que dispara otro trigger) generando efectos dificiles de rastrear. Se usan para pocas reglas criticas, no para toda la logica de negocio.",
            "Seguridad y respaldo van juntos: seguridad evita que datos se corrompan o se filtren; respaldo (backup) asume que igual algo saldra mal y prepara la recuperacion. Full backup (copia completa), incremental (solo lo que cambio desde el ultimo backup) y diferencial (todo lo que cambio desde el ultimo FULL) son las tres estrategias base.",
            "RPO (Recovery Point Objective) = cuantos datos se puede permitir perder, medido en tiempo ('maximo 1 hora de citas perdidas'). RTO (Recovery Time Objective) = cuanto tiempo puede estar caida la BD antes de restaurar. Un backup diario sin probar el restore no cumple ningun RPO/RTO real: un plan de respaldo sin prueba de restauracion es solo una promesa.",
            "Error de docente que no domina el tema: presentar el backup como 'copiar el archivo de vez en cuando' sin frecuencia, retencion (cuantas copias se guardan) ni prueba de restore — eso es lo que el taller de esta clase pide explicitamente que el equipo defina."],
    demo="fn_precio_consulta + trg_audit_cancelacion_cita + outline backup.",
    taller=["Crear >=1 funcion util al PI.",
            "Crear >=1 trigger (auditoria o stock no negativo).",
            "Redactar plan de respaldo: frecuencia, retencion, restore de prueba.",
            "Actualizar checklist PI: seguridad/respaldo en progreso."],
    quiz=True, sql="04_func_trigger_backup.sql"),
  dict(n=5, tipo="parcial", slug=None, titulo="Parcial 1", subtitulo="Solo evaluacion — Corte 1",
    herramienta=None, hito_pi="No avanza PI", entregable=None, teoria=[], demo=None, taller=[],
    quiz=False, sql=None, parcial="Parcial 1 - Administracion procedimientos y seguridad.docx"),
  dict(n=6, tipo="regular", slug="Optimizacion de consultas",
    titulo="Optimizacion de consultas · VetCare",
    subtitulo="Antes/despues sobre el DDL del PI",
    herramienta="DB Fiddle / SQLTest.online",
    hito_pi="Primera pareja de consultas antes/despues del PI",
    entregable="2 consultas (antes/despues) + justificacion (media pag.)",
    teoria=["Optimizar consultas parte de entender que el motor NO ejecuta el SQL tal cual se escribe: primero lo transforma en un plan de ejecucion (que tablas leer, en que orden, con o sin indice) y ese plan es lo que realmente determina el tiempo de respuesta.",
            "Tres cuellos de botella clasicos: (1) SELECT * trae columnas que nadie usa y aumenta el trafico/memoria; (2) JOIN sin filtro temprano obliga a cruzar tablas completas antes de descartar filas; (3) aplicar una funcion sobre la columna en el WHERE (ej. WHERE UPPER(nombre)='LUNA') impide que el motor use un indice normal sobre esa columna (esto se llama 'no-sargable').",
            "Reescritura tipica: proyectar solo columnas necesarias (SELECT nombre, fecha en vez de SELECT *), aplicar el filtro mas selectivo primero (WHERE fecha >= hoy antes del JOIN si reduce mucho el conjunto), y mover comparaciones a la forma que el motor pueda usar con indice.",
            "EXPLAIN (o EXPLAIN PLAN segun el motor) muestra COMO el motor piensa ejecutar la consulta: si dice 'Seq Scan'/'Full Table Scan' sobre una tabla grande donde se esperaba usar un indice, esa es la senal de que algo en el WHERE o el tipo de dato esta bloqueando el uso del indice.",
            "Conexion con Clase 7: optimizar consultas y crear indices son las dos caras de la misma moneda — una consulta mal escrita no aprovecha ni el mejor indice, y el mejor indice no compensa una consulta que fuerza un escaneo completo.",
            "Error de docente que no domina el tema: pedir 'la consulta más rápida' sin definir contra que se compara (volumen de datos, indices existentes) — optimizar siempre es relativo a un antes medible, por eso el taller pide guardar la version antes Y despues, no solo la version final."],
    demo="Consulta pesada citas+mascotas+duenos -> version filtrada y proyectada.",
    taller=["Tomar 1 consulta real del PI (citas del dia / historial).",
            "Escribir version antes e ineficiente o real.",
            "Reescribir despues y justificar 3 cambios.",
            "Guardar 06_opt_antes.sql / 06_opt_despues.sql en carpeta del equipo."],
    quiz=True, sql="06_opt_consultas.sql"),
  dict(n=7, tipo="regular", slug="Indices y particionamiento",
    titulo="Indices y particionamiento · VetCare",
    subtitulo="Diseno fisico al servicio del PI",
    herramienta="DB Fiddle + draw.io (opcional)",
    hito_pi=">=2 indices justificados sobre tablas calientes del PI",
    entregable="Script CREATE INDEX + tabla justificacion consulta->indice",
    teoria=["Un indice es una estructura auxiliar (tipicamente un arbol B-Tree) que el motor mantiene ordenada por una o mas columnas, para encontrar filas sin recorrer toda la tabla — como el indice de un libro en vez de leer pagina por pagina.",
            "El costo no es gratis: cada INSERT/UPDATE/DELETE sobre una columna indexada obliga al motor a actualizar tambien el indice, asi que mas indices = lecturas mas rapidas pero escrituras mas lentas. Por eso 'indexar todo' es un error, no una optimizacion.",
            "Buen candidato a indice: columna usada muy frecuentemente en WHERE, JOIN u ORDER BY, con alta cardinalidad (muchos valores distintos, ej. id_dueno) — indexar una columna de baja cardinalidad (ej. un booleano activo S/N con solo 2 valores) rara vez ayuda porque el motor igual debe leer una fraccion enorme de la tabla.",
            "Candidatos reales en VetCare: Cita(fecha_hora) para listar la agenda del dia, Mascota(id_dueno) porque cada consulta de historial parte de un dueno, DetalleFactura(id_factura) para armar el total de una factura sin escanear toda la tabla.",
            "Particionamiento (idea conceptual, no se implementa hoy): dividir fisicamente una tabla muy grande en fragmentos (ej. Cita por mes o por anio) para que las consultas que solo piden 'las citas de este mes' lean unicamente esa porcion, no la tabla historica completa. Es una tecnica de escala, distinta del indice, mientras el indice ordena datos, la particion los separa fisicamente en bloques.",
            "Error de docente que no domina el tema: crear un indice sobre CADA columna 'por si acaso' sin mirar que consultas realmente lo necesitan — el taller exige justificar cada indice con la consulta concreta que lo aprovecha."],
    demo="CREATE INDEX idx_cita_fecha; consulta que lo usaria.",
    taller=["Identificar 2 consultas frecuentes del PI.",
            "Proponer y crear >=2 indices con nombre claro.",
            "Justificar columna, cardinalidad y riesgo de sobre-indexar.",
            "Opcional: diagrama tabla caliente -> indices en Excalidraw."],
    quiz=True, sql="07_indices_vetcare.sql"),
  dict(n=8, tipo="regular", slug="Tuning y transacciones",
    titulo="Tuning · Transacciones · VetCare",
    subtitulo="Atomicidad en facturacion e insumos",
    herramienta="Oracle Live SQL / DB Fiddle",
    hito_pi="Transaccion de negocio (factura + stock) + notas de tuning",
    entregable="Script transaccional + checklist tuning del PI (1 pag.)",
    teoria=["Una transaccion agrupa varias sentencias SQL en una sola unidad de todo-o-nada: si facturar implica INSERT en factura, INSERT en detalle_factura Y UPDATE de stock en insumo, las tres deben aplicarse juntas o ninguna — nunca queda una factura sin descontar stock, ni stock descontado sin factura.",
            "Propiedades ACID en una frase cada una: Atomicidad (todo o nada, ya explicado), Consistencia (la BD pasa de un estado valido a otro, respetando reglas como stock>=0), Aislamiento (transacciones concurrentes no se pisan entre si — se profundiza en Clase 10), Durabilidad (una vez hecho COMMIT, el dato sobrevive aunque el sistema se caiga un segundo despues).",
            "COMMIT confirma la transaccion de forma permanente; ROLLBACK deshace todo lo hecho desde el ultimo COMMIT si algo salio mal (ej. el insumo no tenia stock suficiente). Sin ROLLBACK explicito ante el error, quedaria una factura registrada sin el descuento real de stock: inconsistencia de datos.",
            "Dirty read (lectura sucia): una transaccion lee un dato que otra transaccion modifico pero AUN NO ha confirmado con COMMIT; si esa segunda transaccion hace ROLLBACK despues, la primera trabajo con un dato que nunca existio de verdad. Es uno de los problemas que el nivel de aislamiento intenta evitar.",
            "Tuning en este contexto no es magia, son habitos concretos: mantener estadisticas del optimizador actualizadas (para que EXPLAIN elija bien), apoyarse en los indices ya justificados en Clase 7, y mantener las transacciones lo mas CORTAS posible — una transaccion larga retiene bloqueos (locks) sobre filas y puede frenar a otras transacciones que esperan esas mismas filas.",
            "Error de docente que no domina el tema: envolver TODA la sesion de trabajo en una sola transaccion gigante 'para no perder nada' — eso maximiza el tiempo que otros usuarios quedan bloqueados esperando esas filas, exactamente el problema que Clase 10 (concurrencia) va a diagnosticar."],
    demo="BEGIN... INSERT factura/detalle... UPDATE stock... COMMIT/ROLLBACK.",
    taller=["Implementar bloque/proc que facture y descuente stock atomicamente.",
            "Probar fallo a mitad (stock insuficiente) -> ROLLBACK.",
            "Completar checklist tuning del PI.",
            "Actualizar informe PI: seccion transacciones."],
    quiz=True, sql="08_transacciones_vetcare.sql"),
  dict(n=9, tipo="parcial", slug=None, titulo="Parcial 2", subtitulo="Solo evaluacion — Corte 2",
    herramienta=None, hito_pi="No avanza PI", entregable=None, teoria=[], demo=None, taller=[],
    quiz=False, sql=None, parcial="Parcial 2 - Optimizacion indices y transacciones.docx"),
  dict(n=10, tipo="autonoma", slug="Control de concurrencia",
    titulo="Control de concurrencia · VetCare",
    subtitulo="Clase autonoma · refuerzo sin parcial",
    herramienta="Google Docs + Live SQL",
    hito_pi="Escenarios de concurrencia del PI documentados",
    entregable="Informe corto: 2 escenarios (cita doble / stock) + mitigacion",
    teoria=["Concurrencia = varias transacciones ejecutandose al mismo tiempo sobre los mismos datos. El problema clasico de VetCare: dos recepcionistas, en dos computadores distintos, intentan agendar la MISMA franja horaria para el MISMO veterinario en el mismo instante; sin control, ambas lecturas ven la franja libre y ambas insertan — doble reserva.",
            "Control pesimista: asumir que el conflicto va a ocurrir, asi que se bloquea la fila (o el recurso) apenas se empieza a leer para modificar, y otras transacciones deben esperar a que termine (SELECT ... FOR UPDATE es el ejemplo tipico). Simple y seguro, pero puede generar esperas largas si hay muchas transacciones compitiendo.",
            "Control optimista: asumir que el conflicto es raro, dejar que todos lean libremente, y verificar SOLO al momento de escribir si alguien mas cambio el dato mientras tanto (comparando una version o timestamp); si hubo cambio, se rechaza y se reintenta. Mejor rendimiento cuando los conflictos son poco frecuentes.",
            "Deadlock (mencion breve): dos transacciones se bloquean mutuamente esperando un recurso que la otra tiene — T1 espera la fila que T2 bloqueo, y T2 espera la fila que T1 bloqueo. El motor detecta esto y aborta una de las dos automaticamente.",
            "Mitigaciones concretas y accesibles para el PI: una restriccion UNIQUE sobre (id_veterinario, fecha_hora) hace que el segundo INSERT falle automaticamente en vez de crear la doble reserva; transacciones cortas reducen la ventana de tiempo en la que puede ocurrir un conflicto; centralizar la logica en un procedimiento (Clase 3) evita que cada pantalla de la app implemente su propia validacion de forma inconsistente.",
            "Error de docente que no domina el tema: creer que 'poner una transaccion' ya resuelve la concurrencia — una transaccion garantiza atomicidad, pero sin un mecanismo de bloqueo o una restriccion UNIQUE, dos transacciones concurrentes pueden seguir generando la doble reserva porque ambas leen 'libre' antes de que la otra confirme."],
    demo="Narrativa paso a paso T1/T2 sobre tabla Cita.",
    taller=["Describir escenario doble reserva con tiempos T1/T2.",
            "Describir escenario doble descuento de stock.",
            "Proponer mitigacion SQL.",
            "Anadir seccion al informe PI."],
    quiz=True, sql="10_concurrencia_vetcare.sql"),
  dict(n=11, tipo="regular", slug="Avance del proyecto final",
    titulo="Avance PI · VetCare DB",
    subtitulo="Checklist viva + demo parcial",
    herramienta="Live SQL / DB Fiddle + draw.io + ExamLab",
    hito_pi="Demo parcial + checklist de avance (hito formal PI)",
    entregable="Checklist firmada + enlace/ZIP avance (DDL+procs+ER)",
    teoria=["Hoy no hay tema nuevo: se cierran huecos del PI con rubrica.",
            "Evidencias: ER, DDL, roles, >=2 procs, >=1 fn, >=2 triggers, 1 opt.",
            "Feedback entre pares: 10 min por equipo."],
    demo="Recorrido de checklist + ejemplo demo de 3 min.",
    taller=["Completar checklist de avance (si/no/parcial).",
            "Demo 3-5 min: ER + 1 proc + 1 trigger.",
            "Lista de gaps con responsable.",
            "Subir avance intermedio a ExamLab (Talleres) si se pide."],
    quiz=True, sql="11_checklist_seed.sql"),
  dict(n=12, tipo="regular", slug="Integracion y preparacion final",
    titulo="Integracion app <-> BD · Prep. presentacion",
    subtitulo="Contrato de operaciones + ensayo PI",
    herramienta="Google Docs + Live SQL + Excalidraw",
    hito_pi="Contrato integracion + preparacion de entrega/sustentacion",
    entregable="Contrato app<->BD + outline de slides de sustentacion (5-8 min)",
    teoria=["Integrar app<->BD significa que la aplicacion NUNCA arma SQL dinamico contra las tablas directamente; llama procedimientos y funciones ya construidos (Clases 3-4). Esto evita SQL injection (nadie concatena texto de usuario dentro de una consulta), centraliza la regla de negocio en un solo lugar, y permite cambiar el esquema interno sin romper la app mientras el contrato del proc se mantenga igual.",
            "Un contrato de integracion documenta, por cada operacion: nombre del proc, parametros de entrada con su tipo, que retorna (valor OUT o codigo de resultado), y que errores puede lanzar y con que significado (ej. 'ERROR: mascota inactiva' vs una excepcion no controlada del motor). Sin este contrato, cualquier desarrollador que use la BD debe adivinar el comportamiento leyendo el codigo SQL directamente.",
            "Manejo de errores en la frontera app-BD: la app no deberia mostrar al usuario final un error crudo de base de datos (ej. 'ORA-00001: unique constraint violated'); el proc devuelve un mensaje o codigo de negocio legible, y la app lo traduce a un mensaje humano ('Ya existe una cita en ese horario').",
            "Autenticacion/autorizacion en este punto es conceptual, no de implementacion: la app se conecta con una cuenta de servicio que respeta los roles definidos en Clase 2 (principio de minimo privilegio) — la app de recepcion no deberia poder ejecutar procs reservados a auditoria o administracion.",
            "Preparar la sustentacion no es 'hacer diapositivas bonitas': es organizar la evidencia tecnica en una narrativa logica -> problema real que resuelve VetCare, modelo de datos (ER + normalizacion), seguridad (roles), automatizacion (procs/triggers), rendimiento (indices/optimizacion), y una demo en vivo que conecte todo eso con una operacion real (agendar una cita, facturar).",
            "Error de docente que no domina el tema: dejar que la 'integracion' quede como una idea abstracta sin contrato escrito — el entregable de hoy exige documentar minimo 3 operaciones con su firma completa, no solo mencionarlas de palabra."],
    demo="Plantilla contrato sp_agendar_cita + storyboard 6 slides.",
    taller=["Redactar contrato de >=3 operaciones.",
            "Diagrama flujo app->BD (Excalidraw) opcional.",
            "Outline presentacion 5-8 min + quien habla que.",
            "Empaquetar borrador entrega final."],
    quiz=True, sql="12_contrato_ops.sql"),
  dict(n=13, tipo="autonoma", slug="Analisis de casos reales",
    titulo="Analisis de casos reales · VetCare",
    subtitulo="Clase autonoma · lecciones para el PI",
    herramienta="Google Docs",
    hito_pi="Informe de caso -> mejoras concretas al PI",
    entregable="Informe 1-2 pag.: caso + 3 mejoras aplicables a VetCare",
    teoria=["Caso 1 — falta de backup real: una organizacion que 'hacia backup' copiando el archivo de datos una vez al mes sin probar nunca el restore. Cuando el disco fallo, el archivo copiado estaba corrupto (nunca se verifico) y perdieron meses de informacion. Leccion para VetCare: un backup que nunca se restauro de prueba no cuenta como backup funcional (conecta con Clase 4: RPO/RTO y prueba de restore).",
            "Caso 2 — indices mal disenados: un sistema con un indice sobre CADA columna 'por si acaso', que volvia cada INSERT/UPDATE mas lento de lo aceptable, sin que nadie hubiera medido si esos indices realmente se usaban en consultas reales. Leccion: indexar sin justificar la consulta que lo aprovecha (conecta con Clase 7) desperdicia recursos y no mejora nada.",
            "Caso 3 — inyeccion SQL: una aplicacion que concatenaba directamente el texto escrito por el usuario dentro de una consulta (ej. \"SELECT * FROM usuarios WHERE nombre='\" + input + \"'\"), permitiendo que alguien escribiera un valor que alterara la consulta completa y expusiera o borrara datos ajenos. Leccion: por eso la app llama procedimientos con parametros tipados (Clase 3 y Clase 12) en vez de armar SQL con texto libre.",
            "Estructura para analizar cualquier caso real: (1) contexto — que sistema era y que se suponia que hacia bien; (2) fallo — que paso exactamente y por que la causa raiz no era 'mala suerte' sino una decision tecnica evitable; (3) leccion — que principio general se puede extraer; (4) cambio concreto — que se ajusta HOY en el VetCare del equipo, no en abstracto.",
            "Esta clase es autonoma (sin encuentro sincrono) precisamente porque no introduce tecnica nueva: aplica en modo reflexivo/critico todo lo visto en Clases 1-10 sobre un caso real, cerrando el ciclo antes de entrar a integracion y cierre del PI.",
            "Error de docente que no domina el tema: dejar que el informe describa el caso ajeno sin conectar ninguna leccion con una accion verificable en VetCare — el entregable exige 3 mejoras concretas aplicadas al proyecto propio, no un resumen de noticia."],
    demo="Plantilla: contexto -> fallo -> leccion -> cambio en VetCare.",
    taller=["Elegir 1 caso (backup, rendimiento o seguridad).",
            "Resumir en media pagina que paso.",
            "Proponer 3 mejoras concretas al VetCare del equipo.",
            "Actualizar informe PI con lecciones de casos."],
    quiz=True, sql=None),
  dict(n=14, tipo="parcial", slug=None, titulo="Parcial 3", subtitulo="Solo evaluacion — Corte 3",
    herramienta=None, hito_pi="Prep PI fue Clase 12; cierre en Clase 15", entregable=None,
    teoria=[], demo=None, taller=[], quiz=False, sql=None,
    parcial="Parcial 3 - Integracion casos y cierre de proyecto.docx"),
  dict(n=15, tipo="autonoma", slug="Presentacion del proyecto y cierre",
    titulo="Presentacion PI · Cierre VetCare",
    subtitulo="Clase autonoma · sustentacion y cierre",
    herramienta="ExamLab (Proyectos) + slides del equipo",
    hito_pi="Sustentacion / entrega final del PI (20% Corte 3)",
    entregable="ZIP/PDF final + video o Meet segun indique docente",
    teoria=["Cierre: evidencias completas segun rubrica (100 pts -> 20%).",
            "Sustentacion breve alineada a criterios del enunciado.",
            "Autoevaluacion del proceso del equipo."],
    demo="Checklist final de empaquetado del ZIP.",
    taller=["Entregar paquete final en ExamLab (modulo Proyectos).",
            "Sustentar 5-8 min (sincrono o asincrono).",
            "Autoevaluacion: que harian distinto.",
            "Cierre del curso."],
    quiz=True, sql=None),
]

SQL_BODIES = {
"01_arranque_vetcare.sql": """-- VetCare DB · Clase 1 · DDL minimo demo (DB Fiddle / PostgreSQL o MySQL)
-- Objetivo PI: dejar entidades base para el ER.

CREATE TABLE dueno (
  id_dueno INT PRIMARY KEY,
  nombre VARCHAR(80) NOT NULL,
  telefono VARCHAR(30),
  email VARCHAR(120)
);

CREATE TABLE mascota (
  id_mascota INT PRIMARY KEY,
  id_dueno INT NOT NULL REFERENCES dueno(id_dueno),
  nombre VARCHAR(60) NOT NULL,
  especie VARCHAR(40),
  activa CHAR(1) DEFAULT 'S' CHECK (activa IN ('S','N'))
);

CREATE TABLE cita (
  id_cita INT PRIMARY KEY,
  id_mascota INT NOT NULL REFERENCES mascota(id_mascota),
  fecha_hora TIMESTAMP NOT NULL,
  estado VARCHAR(20) DEFAULT 'PROGRAMADA'
);

INSERT INTO dueno VALUES (1, 'Ana Perez', '3001112233', 'ana@mail.com');
INSERT INTO mascota VALUES (10, 1, 'Luna', 'Canino', 'S');
INSERT INTO cita VALUES (100, 10, '2026-09-01 09:00:00', 'PROGRAMADA');
SELECT m.nombre, d.nombre AS dueno, c.fecha_hora
FROM cita c JOIN mascota m ON m.id_mascota=c.id_mascota
JOIN dueno d ON d.id_dueno=m.id_dueno;
""",
"02_roles_vetcare.sql": """-- VetCare DB · Clase 2 · Roles y privilegios (Oracle Live SQL)
-- Live SQL da UN solo usuario/schema por cuenta: no siempre se puede CREATE ROLE
-- ni GRANT a otro usuario real. Por eso este script trae DOS partes:
--   PARTE A: ejecutable tal cual en cualquier cuenta Live SQL (GRANT/REVOKE sobre
--            las propias tablas hacia PUBLIC, para demostrar la sintaxis real).
--   PARTE B: la version completa multi-usuario (CREATE ROLE + GRANT a rol),
--            documentada como PLAN si el playground no permite crear usuarios/roles.

-- ============ PARTE A — ejecutable en Live SQL (su propio schema) ============
-- Sirve para demostrar que GRANT/REVOKE son sentencias reales, no solo teoria.
GRANT SELECT ON mascota TO PUBLIC;
GRANT SELECT, INSERT, UPDATE ON cita TO PUBLIC;
REVOKE UPDATE ON cita FROM PUBLIC;

-- Verificacion de privilegios otorgados sobre los propios objetos:
SELECT table_name, privilege, grantee
FROM user_tab_privs_made
WHERE table_name IN ('MASCOTA', 'CITA');

-- ============ PARTE B — plan multi-rol (requiere privilegios DBA) ============
-- Roles conceptuales del PI: ADMIN_BD, RECEPCION, VETERINARIO, AUDITOR
CREATE ROLE recepcion;
GRANT SELECT, INSERT, UPDATE ON cita TO recepcion;
GRANT SELECT ON mascota TO recepcion;
GRANT SELECT ON dueno TO recepcion;
REVOKE DELETE ON cita FROM recepcion;

CREATE ROLE veterinario;
GRANT SELECT ON cita TO veterinario;
GRANT SELECT, INSERT, UPDATE ON consulta TO veterinario;

CREATE ROLE auditor;
GRANT SELECT ON cita TO auditor;
GRANT SELECT ON mascota TO auditor;
GRANT SELECT ON dueno TO auditor;

-- Asignar el rol a un usuario real (equivalente conceptual):
-- GRANT recepcion TO usuario_recepcion01;

-- Matriz minima (documentar tal cual en el entregable):
-- RECEPCION:   Cita CRUD limitado (sin DELETE), Dueno/Mascota solo lectura
-- VETERINARIO: Consulta escritura, Cita lectura
-- AUDITOR:     solo SELECT sobre las tablas sensibles
-- ADMIN_BD:    DDL completo + capacidad de otorgar/revocar roles
""",
"03_procs_vetcare.sql": """-- VetCare DB · Clase 3 · Procedimiento agendar cita (Oracle Live SQL)
-- Ajustar tipos segun el schema creado por el equipo.

CREATE OR REPLACE PROCEDURE sp_agendar_cita (
  p_id_cita IN NUMBER,
  p_id_mascota IN NUMBER,
  p_fecha IN TIMESTAMP,
  p_msg OUT VARCHAR2
) AS
  v_activa CHAR(1);
BEGIN
  SELECT activa INTO v_activa FROM mascota WHERE id_mascota = p_id_mascota;
  IF v_activa <> 'S' THEN
    p_msg := 'ERROR: mascota inactiva; no se agenda';
    RETURN;
  END IF;
  INSERT INTO cita(id_cita, id_mascota, fecha_hora, estado)
  VALUES (p_id_cita, p_id_mascota, p_fecha, 'PROGRAMADA');
  p_msg := 'OK: cita agendada';
  COMMIT;
EXCEPTION
  WHEN NO_DATA_FOUND THEN
    p_msg := 'ERROR: mascota no existe';
  WHEN OTHERS THEN
    p_msg := 'ERROR: ' || SQLERRM;
    ROLLBACK;
END;
/
""",
"04_func_trigger_backup.sql": """-- VetCare DB · Clase 4 · Funcion + trigger auditoria (Oracle)

CREATE OR REPLACE FUNCTION fn_precio_base (p_especie VARCHAR2)
RETURN NUMBER IS
BEGIN
  IF UPPER(p_especie) = 'CANINO' THEN RETURN 45000; END IF;
  IF UPPER(p_especie) = 'FELINO' THEN RETURN 40000; END IF;
  RETURN 35000;
END;
/

CREATE TABLE audit_cita (
  id_audit NUMBER PRIMARY KEY,
  id_cita NUMBER,
  accion VARCHAR2(30),
  detalle VARCHAR2(200),
  fecha_evento TIMESTAMP DEFAULT SYSTIMESTAMP
);

CREATE OR REPLACE TRIGGER trg_audit_cancelacion
AFTER UPDATE OF estado ON cita
FOR EACH ROW
WHEN (NEW.estado = 'CANCELADA' AND OLD.estado <> 'CANCELADA')
BEGIN
  INSERT INTO audit_cita(id_audit, id_cita, accion, detalle)
  VALUES (NVL((SELECT MAX(id_audit) FROM audit_cita),0)+1,
          :NEW.id_cita, 'CANCELACION', 'Cita cancelada');
END;
/

-- Plan backup (documentar en Google Docs): diario logico scripts SQL + semanal export playground.
""",
"06_opt_consultas.sql": """-- VetCare DB · Clase 6 · Antes / despues

-- ANTES (anti-patron)
SELECT * FROM cita c, mascota m, dueno d
WHERE c.id_mascota = m.id_mascota AND m.id_dueno = d.id_dueno;

-- DESPUES (proyecto columnas + filtro temprano)
SELECT c.id_cita, c.fecha_hora, m.nombre AS mascota, d.nombre AS dueno
FROM cita c
JOIN mascota m ON m.id_mascota = c.id_mascota
JOIN dueno d ON d.id_dueno = m.id_dueno
WHERE c.fecha_hora >= TIMESTAMP '2026-09-01 00:00:00'
  AND c.fecha_hora <  TIMESTAMP '2026-09-02 00:00:00'
  AND c.estado = 'PROGRAMADA';
""",
"07_indices_vetcare.sql": """-- VetCare DB · Clase 7 · Indices

CREATE INDEX idx_cita_fecha ON cita (fecha_hora);
CREATE INDEX idx_mascota_dueno ON mascota (id_dueno);
CREATE INDEX idx_cita_estado_fecha ON cita (estado, fecha_hora);

-- Justificacion PI:
-- idx_cita_fecha: listado del dia / agenda
-- idx_mascota_dueno: busqueda de mascotas por dueno
-- idx_cita_estado_fecha: filtros combinados recepción
""",
"08_transacciones_vetcare.sql": """-- VetCare DB · Clase 8 · Transaccion facturacion + stock (orientativo)

-- Pseudobloque / proc:
-- BEGIN
--   INSERT INTO factura ...
--   INSERT INTO detalle_factura ...
--   UPDATE insumo SET stock = stock - :cant WHERE id_insumo = :id;
--   IF stock < 0 THEN RAISE; END IF;
--   COMMIT;
-- EXCEPTION WHEN OTHERS THEN ROLLBACK; RAISE;
-- END;

-- Demo minima portable:
-- UPDATE insumo SET stock = stock - 1 WHERE id_insumo = 1 AND stock >= 1;
-- Si SQL%ROWCOUNT = 0 -> no habia stock -> ROLLBACK de la factura.
""",
"10_concurrencia_vetcare.sql": """-- VetCare DB · Clase 10 · Demo ejecutable: doble reserva y su mitigacion
-- Ejecutar EN ORDEN: primero se ve el problema, despues la solucion.

-- Paso 1: tabla de demo SIN restriccion (asi llegaria si nadie penso en concurrencia)
CREATE TABLE cita_demo (
  id_cita INT PRIMARY KEY,
  id_mascota INT NOT NULL,
  id_veterinario INT NOT NULL,
  fecha_hora TIMESTAMP NOT NULL,
  estado VARCHAR(20) DEFAULT 'PROGRAMADA'
);

-- Paso 2: T1 (Recepcion A) agenda la franja - OK
INSERT INTO cita_demo VALUES (1, 10, 5, TIMESTAMP '2026-10-12 09:00:00', 'PROGRAMADA');

-- Paso 3: T2 (Recepcion B) agenda OTRA mascota, MISMO veterinario, MISMA franja.
-- Sin restriccion esto se inserta SIN ERROR -> aqui esta la doble reserva.
INSERT INTO cita_demo VALUES (2, 22, 5, TIMESTAMP '2026-10-12 09:00:00', 'PROGRAMADA');

-- Evidencia del problema: dos citas para el mismo veterinario en la misma franja
SELECT id_veterinario, fecha_hora, COUNT(*) AS citas_en_la_misma_franja
FROM cita_demo
GROUP BY id_veterinario, fecha_hora
HAVING COUNT(*) > 1;

-- Paso 4: la mitigacion real - la restriccion que debio existir desde el diseño
ALTER TABLE cita_demo
  ADD CONSTRAINT uq_cita_demo_vet_fecha UNIQUE (id_veterinario, fecha_hora);

-- Paso 5: repetir el intento de doble reserva - AHORA debe fallar
INSERT INTO cita_demo VALUES (3, 35, 5, TIMESTAMP '2026-10-12 09:00:00', 'PROGRAMADA');
-- Esperado: error de restriccion unica (ORA-00001 en Oracle) -> la BD rechaza la doble reserva.
""",
"11_checklist_seed.sql": """-- VetCare DB · Clase 11 · Seed ejecutable para la demo de checklist
-- Autocontenido: cree estas tablas minimas si el equipo aun no las tiene, o
-- adapte los nombres a su propio DDL (Clases 1-8) antes de correr los INSERT.

CREATE TABLE dueno_demo (id_dueno INT PRIMARY KEY, nombre VARCHAR(80));
CREATE TABLE mascota_demo (
  id_mascota INT PRIMARY KEY, id_dueno INT REFERENCES dueno_demo(id_dueno),
  nombre VARCHAR(60), activa CHAR(1) DEFAULT 'S'
);
CREATE TABLE cita_demo11 (
  id_cita INT PRIMARY KEY, id_mascota INT REFERENCES mascota_demo(id_mascota),
  fecha_hora TIMESTAMP, estado VARCHAR(20)
);
CREATE TABLE insumo_demo (id_insumo INT PRIMARY KEY, nombre VARCHAR(60), stock INT);

-- Datos que permiten mostrar EN VIVO cada punto del checklist:
INSERT INTO dueno_demo VALUES (1, 'Ana Perez');
INSERT INTO dueno_demo VALUES (2, 'Carlos Ruiz');
INSERT INTO mascota_demo VALUES (10, 1, 'Luna', 'S');   -- mascota activa: SI puede agendar
INSERT INTO mascota_demo VALUES (11, 2, 'Rocky', 'N');  -- mascota inactiva: NO debe poder agendar
INSERT INTO cita_demo11 VALUES (100, 10, TIMESTAMP '2026-10-19 09:00:00', 'PROGRAMADA');
INSERT INTO insumo_demo VALUES (50, 'Vacuna antirrabica', 3);  -- stock bajo a proposito

-- Punto del checklist "regla de negocio se cumple": intente agendar la mascota
-- inactiva (id 11) con su sp_agendar_cita y confirme que el proc la rechaza.
-- Punto "stock nunca negativo": intente facturar 5 unidades del insumo 50
-- (solo hay 3) y confirme que su transaccion de Clase 8 hace ROLLBACK.
SELECT m.nombre, m.activa, d.nombre AS dueno FROM mascota_demo m JOIN dueno_demo d ON d.id_dueno = m.id_dueno;
""",
"12_contrato_ops.sql": """-- VetCare DB · Clase 12 · Contrato app<->BD (Oracle PL/SQL, ejecutable)
-- Regla: la app NUNCA hace INSERT directo a cita/consulta/factura; solo llama estos procs.

CREATE OR REPLACE PROCEDURE sp_agendar_cita (
  p_id_cita IN NUMBER, p_id_mascota IN NUMBER, p_fecha IN TIMESTAMP, p_msg OUT VARCHAR2
) AS
BEGIN
  INSERT INTO cita(id_cita, id_mascota, fecha_hora, estado) VALUES (p_id_cita, p_id_mascota, p_fecha, 'PROGRAMADA');
  p_msg := 'OK: cita agendada'; COMMIT;
EXCEPTION WHEN OTHERS THEN p_msg := 'ERROR: ' || SQLERRM; ROLLBACK;
END;
/

CREATE OR REPLACE PROCEDURE sp_registrar_consulta (
  p_id_consulta IN NUMBER, p_id_cita IN NUMBER, p_notas IN VARCHAR2, p_precio IN NUMBER, p_msg OUT VARCHAR2
) AS
BEGIN
  INSERT INTO consulta(id_consulta, id_cita, notas, precio) VALUES (p_id_consulta, p_id_cita, p_notas, p_precio);
  p_msg := 'OK: consulta registrada'; COMMIT;
EXCEPTION WHEN OTHERS THEN p_msg := 'ERROR: ' || SQLERRM; ROLLBACK;
END;
/

-- Contrato para la sustentacion (documentar tal cual en el informe):
-- sp_agendar_cita(id_cita, id_mascota, fecha)      -> p_msg: 'OK: ...' | 'ERROR: ...'
-- sp_registrar_consulta(id_consulta, id_cita, notas, precio) -> p_msg idem
-- sp_facturar(id_factura, id_consulta, lineas...)  -> ver Clase 8 (transaccion factura+stock)
""",
}

QUIZ = {
1: [
    q_om("En el modelo VetCare, ¿qué diferencia PK de FK?",
         ["A) No hay diferencia", "B) PK identifica la fila; FK referencia otra PK",
          "C) FK solo sirve para índices", "D) PK es solo texto"], "B"),
    q_om("¿Cuáles son entidades mínimas típicas del PI VetCare?",
         ["A) Solo Factura", "B) Dueño, Mascota, Cita (y relacionadas)",
          "C) Solo logs de servidor", "D) Solo usuarios LMS"], "B"),
    q_vf("El ER del PI se entrega en draw.io (PNG/SVG) como evidencia visual, no solo como párrafo.", "V"),
    q_vf("Normalización 1–3FN se aplica en el PI solo donde aporta al modelo VetCare (no teoría aislada).", "V"),
    q_om("Regla de negocio típica VetCare:",
         ["A) Mascota inactiva puede agendar sin control", "B) Stock puede ser negativo sin auditar",
          "C) Mascota inactiva no agenda; stock ≥ 0; auditoría sensible", "D) Sin reglas"], "C"),
    q_vf("El diagnóstico de Clase 1 evalúa la plataforma de entrega, no saberes previos de BD I.", "F"),
    q_abierta("Nombre 3 entidades de su ER VetCare y una FK entre dos de ellas.",
              "Ej. Mascota.id_dueno → Dueño.id; Cita.id_mascota → Mascota.id."),
    q_abierta("Escriba en una frase el alcance SI / NO de su PI esta semana.",
              "Respuesta de equipo alineada a ficha (qué sí modelan / qué queda fuera)."),
],
2: [
    q_om("Un rol con privilegios mínimos en VetCare sirve para:",
         ["A) Dar SUPER a todos", "B) Least privilege por perfil (app/lectura/admin)",
          "C) Evitar backups", "D) Eliminar PK"], "B"),
    q_om("¿Qué privilegio NO debería tener el rol de solo lectura de agenda?",
         ["A) SELECT sobre cita", "B) DROP TABLE", "C) SELECT sobre mascota", "D) Consultar veterinario"], "B"),
    q_vf("GRANT y REVOKE forman parte de la administración de privilegios del PI.", "V"),
    q_vf("Usar el usuario root/admin de playground para la app en producción es buena práctica.", "F"),
    q_om("Evidencia típica del taller de roles:",
         ["A) Solo un screenshot del logo", "B) Script de roles + prueba de permiso denegado",
          "C) Factura AWS", "D) Diagrama sin usuarios"], "B"),
    q_vf("Separar rol de aplicación y rol de DBA reduce el impacto de una filtración de credenciales.", "V"),
    q_abierta("Defina 2 roles VetCare (nombre + privilegio clave de cada uno).",
              "Ej. app_vetcare: EXECUTE procs; lector_agenda: SELECT cita/mascota."),
    q_abierta("¿Qué operación debería fallar con el rol de lectura y cómo lo evidencia?",
              "Ej. DELETE/UPDATE stock → error de privilegio; captura del playground."),
],
3: [
    q_om("¿Para qué sirve un procedimiento almacenado en VetCare?",
         ["A) Solo formatear texto", "B) Centralizar regla de negocio invocable desde la app",
          "C) Reemplazar el ER", "D) Dibujar el diagrama"], "B"),
    q_om("Validación mínima de sp_agendar_cita:",
         ["A) Ninguna", "B) Que la mascota exista y esté activa",
          "C) Solo validar el color del logo", "D) Borrar stock"], "B"),
    q_vf("IN entra al procedimiento; OUT/devuelve resultado al llamador.", "V"),
    q_vf("Es correcto duplicar la validación de negocio solo en la UI y nunca en la BD del PI.", "F"),
    q_om("Ventaja de invocar un proc desde la app VetCare:",
         ["A) Oculta reglas y evita SQL suelto inconsistente", "B) Impide transacciones",
          "C) Elimina índices", "D) Obliga a SELECT *"], "A"),
    q_vf("Un procedimiento puede validar reglas y devolver mensaje/código de error controlado.", "V"),
    q_abierta("Escriba la firma (nombre + 2 parámetros) de su sp_agendar_cita.",
              "Ej. sp_agendar_cita(IN id_mascota, IN fecha_hora, OUT msg)."),
    q_abierta("¿Qué pasa si intentan agendar una mascota inactiva? (comportamiento esperado)",
              "Proc rechaza / no inserta cita / mensaje de error; sin fila inválida."),
],
4: [
    q_om("Función vs procedimiento en el PI:",
         ["A) Son idénticos", "B) Función retorna valor usable en SQL; proc orquesta acciones",
          "C) Proc no puede validar", "D) Función borra tablas siempre"], "B"),
    q_om("Un trigger de cancelación/auditoría sirve para:",
         ["A) Decoración", "B) Auditar cambios sensibles sin depender solo de la app",
          "C) Eliminar backups", "D) Quitar FK"], "B"),
    q_vf("RPO = cantidad máxima de dato que se acepta perder (punto de recuperación).", "V"),
    q_vf("RTO mide el tiempo objetivo para volver a operación tras un incidente.", "V"),
    q_om("Evidencia de respaldo mínima razonable en el PI:",
         ["A) «Ya lo hacemos» sin archivo", "B) Plan RPO/RTO + script/export de prueba",
          "C) Solo meme", "D) Apagar el playground"], "B"),
    q_vf("La seguridad del PI termina al crear un usuario; no hace falta auditar cambios sensibles.", "F"),
    q_abierta("Proponga un trigger VetCare (evento + tabla + qué registra).",
              "Ej. AFTER UPDATE cita → auditar cancelación (quién/cuándo/estado)."),
    q_abierta("Indique RPO y RTO objetivo cualitativos para VetCare del equipo.",
              "Ej. RPO ≤ 24h (export diario); RTO ≤ 4h (restaurar playground/script)."),
],
6: [
    q_om("Anti-patrón de consulta en VetCare:",
         ["A) Filtrar por fecha", "B) SELECT * con producto cartesiano / sin filtro",
          "C) Proyectar columnas", "D) Usar índice selectivo"], "B"),
    q_om("Evidencia de optimización pedida en el PI:",
         ["A) Ninguna", "B) ≥2 consultas antes/después con justificación",
          "C) Solo cambiar el color del ER", "D) Borrar la BD"], "B"),
    q_vf("Proyectar solo columnas necesarias reduce I/O y aclara el plan.", "V"),
    q_vf("EXPLAIN/plan de ejecución no aporta nada al entregable de optimización.", "F"),
    q_om("Consulta típica a optimizar en agenda VetCare:",
         ["A) Citas del día con joins necesarios y filtro de fecha", "B) SELECT * FROM todas las tablas",
          "C) Cross join sin WHERE", "D) Actualizar sin WHERE a propósito"], "A"),
    q_vf("«Antes/después» debe mostrar qué cambió (predicado, proyección, índice) y por qué mejora.", "V"),
    q_abierta("Escriba una consulta VetCare «mala» (anti-patrón) en una línea.",
              "Ej. SELECT * FROM cita, mascota; (sin join/filtro)."),
    q_abierta("¿Qué cambio concreto haría en esa consulta y qué evidencia guardaría?",
              "JOIN explícito + filtro fecha + columnas; captura plan/tiempo playground."),
],
7: [
    q_om("¿Cuándo NO conviene crear un índice?",
         ["A) Filtros frecuentes selectivos", "B) Baja selectividad o escritura intensa sin lectura asociada",
          "C) Agenda por fecha_hora", "D) FK muy consultada"], "B"),
    q_om("Índice típico para agenda del día:",
         ["A) Sobre cita.fecha_hora (y opcionalmente estado)", "B) Sobre un comentario libre nunca filtrado",
          "C) Sobre todas las columnas a la vez sin criterio", "D) Ninguno nunca"], "A"),
    q_vf("Particionamiento aquí se trabaja como concepto (p. ej. rango de fecha); no exige SGBD local de pago.", "V"),
    q_vf("Más índices siempre aceleran inserts/updates de stock y facturas.", "F"),
    q_om("Selectividad alta significa:",
         ["A) Casi todas las filas comparten el valor", "B) El predicado discrimina bien (pocas filas)",
          "C) Que no hay PK", "D) Que hay SELECT *"], "B"),
    q_vf("Documentar por qué se creó (o no) un índice es parte de la evidencia del PI.", "V"),
    q_abierta("Proponga un índice VetCare (tabla + columna(s) + consulta que lo usa).",
              "Ej. INDEX cita(fecha_hora) para agenda del día."),
    q_abierta("¿Particionaría citas por mes? Justifique en 1 frase (sí/no + motivo).",
              "Sí si volumen histórico alto por fecha; no si dataset demo pequeño."),
],
8: [
    q_om("COMMIT en la factura VetCare garantiza:",
         ["A) Solo un SELECT", "B) Atomicidad: factura + detalle + stock juntos",
          "C) Borrar auditorías", "D) Ignorar stock"], "B"),
    q_om("Si falta stock, ROLLBACK debe:",
         ["A) Dejar la factura a medias", "B) Deshacer cambios parciales y conservar consistencia",
          "C) Negar el stock a -100", "D) Borrar dueños"], "B"),
    q_vf("Transacciones cortas reducen bloqueos y problemas de concurrencia.", "V"),
    q_vf("Es aceptable hacer la factura en la app con tres commits independientes sin control.", "F"),
    q_om("Propiedad ACID más visible al facturar + descontar insumo:",
         ["A) Atomicidad", "B) Tipografía", "C) Color del ER", "D) Nombre del repo"], "A"),
    q_vf("Un script demo con BEGIN/COMMIT/ROLLBACK es evidencia válida del hito de transacciones.", "V"),
    q_abierta("Liste los 3 pasos atómicos de su caso de facturación VetCare.",
              "Insert factura + detalles + update stock (o equivalente) en una TX."),
    q_abierta("Describa la prueba de fallo (falta stock) y el estado final esperado.",
              "Fuerza stock insuficiente → ROLLBACK → sin factura huérfana ni stock negativo."),
],
10: [
    q_om("Control de concurrencia busca evitar principalmente:",
         ["A) Diagramas bonitos", "B) Anomalías por lecturas/escrituras concurrentes",
          "C) Tener PK", "D) Usar draw.io"], "B"),
    q_om("Escenario VetCare sensible a concurrencia:",
         ["A) Dos cajeros descontando el mismo insumo", "B) Leer el microcurrículo",
          "C) Cambiar el color del logo", "D) Exportar PNG del ER"], "A"),
    q_vf("Aislar transacciones (niveles/locks) es tema de esta clase autónoma.", "V"),
    q_vf("Si «funciona en mi prueba serial», ya está probada la concurrencia.", "F"),
    q_om("Estrategia conceptual frente a doble descuento de stock:",
         ["A) Ignorar", "B) TX + verificación de stock / bloqueo o control optimista",
          "C) SELECT * sin WHERE", "D) Borrar la tabla"], "B"),
    q_vf("Documentar el escenario concurrente (pasos A/B) es parte del entregable autónomo.", "V"),
    q_abierta("Diseñe un caso A/B: dos sesiones tocando el mismo insumo VetCare.",
              "Sesión A y B leen stock=1; ambas intentan vender → una OK, otra falla/rollback."),
    q_abierta("¿Qué evidencia capturaría en el playground para demostrar el control?",
              "Capturas de ambas sesiones + resultado final de stock/factura."),
],
11: [
    q_om("El checkpoint de avance PI VetCare:",
         ["A) Reemplaza el Parcial 3", "B) Es revisión de evidencias, no la sustentación final",
          "C) Cierra el semestre", "D) Elimina la rúbrica"], "B"),
    q_om("Evidencia mínima esperable en el avance:",
         ["A) Solo narrativa", "B) ER + scripts clave + demo parcial + checklist rúbrica",
          "C) Solo el logo", "D) Factura cloud de pago"], "B"),
    q_vf("Si falta el contrato app↔BD, conviene marcarlo como pendiente en el checklist.", "V"),
    q_vf("Seed de datos de prueba no aporta a la demo del PI.", "F"),
    q_om("Durante la viva/demo parcial, lo más útil es:",
         ["A) Improvisar sin script", "B) Mostrar flujo real (agendar/facturar) con datos seed",
          "C) Leer el microcurrículo completo", "D) Ocultar errores siempre"], "B"),
    q_vf("Anti-patrón: SQL suelto en la app que bypasea procs y auditoría.", "V"),
    q_abierta("Liste 3 ítems del checklist PI que YA tienen evidencia en su equipo.",
              "Respuesta concreta: ER PNG, sp_*, trigger, TX, índices, etc."),
    q_abierta("Nombre el mayor hueco actual y la clase/hito donde lo cerrarán.",
              "Ej. contrato ops → Clase 12; concurrencia → ya/ajustes."),
],
12: [
    q_om("El contrato app↔BD es:",
         ["A) Un meme", "B) Lista de operaciones (procs), parámetros, errores y ejemplos",
          "C) Solo el ER sin operaciones", "D) La nota del parcial"], "B"),
    q_om("¿Por qué la app no debe hacer SQL suelto de negocio?",
         ["A) Es más bonito", "B) Duplica reglas y rompe auditoría/seguridad del PI",
          "C) Acelera siempre", "D) Obliga a DROP"], "B"),
    q_vf("La sustentación del PI dura típicamente 5 a 8 minutos.", "V"),
    q_vf("El ensayo de pitch de hoy sustituye el Parcial 3.", "F"),
    q_om("Entrada típica del contrato para agendar:",
         ["A) sp_agendar_cita(params) + errores + ejemplo CALL", "B) Solo «usar la BD»",
          "C) SELECT * sin firma", "D) Token de AWS"], "A"),
    q_vf("El contrato debe alinearse con los procedimientos ya implementados en el PI.", "V"),
    q_abierta("Escriba 2 operaciones de su contrato (nombre + 1 parámetro clave cada una).",
              "Ej. sp_agendar_cita(id_mascota); sp_facturar(id_consulta)."),
    q_abierta("Indique un error de negocio que la app debe manejar (código/mensaje).",
              "Ej. MASCOTA_INACTIVA / STOCK_INSUFICIENTE."),
],
13: [
    q_om("Analizar un caso real sirve en el PI para:",
         ["A) Copiar el logo", "B) Extraer lecciones de modelo, seguridad o operaciones a VetCare",
          "C) Evitar evidencias", "D) Eliminar el ER"], "B"),
    q_om("Lección típica transferable a VetCare:",
         ["A) Ignorar backups", "B) Auditoría, privilegios y consistencia en operaciones críticas",
          "C) SELECT * siempre", "D) Sin transacciones"], "B"),
    q_vf("Esta clase autónoma pide relacionar el caso con decisiones del propio PI.", "V"),
    q_vf("Un caso real «bonito» sin amarre a VetCare cumple el entregable.", "F"),
    q_om("Salida esperada del análisis:",
         ["A) Solo resumen de noticias", "B) 3 lecciones + impacto concreto en su VetCare",
          "C) Solo emojis", "D) Borrar scripts"], "B"),
    q_vf("Incidentes de datos (fugas, inconsistencias) motivan controles que ya vieron en el curso.", "V"),
    q_abierta("Nombre el caso analizado y 1 riesgo que también tiene VetCare.",
              "Respuesta de equipo: caso + riesgo (privilegios, backup, TX…)."),
    q_abierta("¿Qué cambio harán en su PI por esa lección (artefacto concreto)?",
              "Ej. añadir trigger auditoría / endurecer rol / documentar RPO."),
],
15: [
    q_om("En la sustentación VetCare, lo mínimo a demostrar es:",
         ["A) Solo hablar sin demo", "B) Modelo + operaciones clave + evidencias de rúbrica",
          "C) Solo un repositorio de archivos", "D) AWS de pago"], "B"),
    q_om("El PI (20% Corte 3):",
         ["A) Reemplaza el Parcial 3", "B) No sustituye el Parcial 3",
          "C) Elimina asistencia", "D) Es sin rúbrica"], "B"),
    q_vf("Mostrar secretos/credenciales en pantalla durante la demo es aceptable.", "F"),
    q_vf("La demo debe usar el dominio VetCare del equipo (no otro caso improvisado).", "V"),
    q_om("Orden razonable de pitch:",
         ["A) Problema → modelo → ops/demo → decisiones → cierre", "B) Solo memes",
          "C) Leer 40 diapositivas de teoría", "D) Empezar por la factura AWS"], "A"),
    q_vf("Un fallo controlado explicado (rollback/validación) puede reforzar el diseño.", "V"),
    q_abierta("Liste las evidencias que proyectarán (archivos/URLs) en la sustentación.",
              "ER, scripts procs/TX, contrato, capturas playground, checklist."),
    q_abierta("Trade-off principal que defenderán (1–2 frases).",
              "Respuesta alineada a decisiones del equipo (procs vs app, índices, etc.)."),
],
}


def shade(p, fill):
    pPr = p._p.get_or_add_pPr()
    shd = OxmlElement('w:shd'); shd.set(qn('w:val'), 'clear'); shd.set(qn('w:fill'), fill)
    pPr.append(shd)

def run(r, *, size=11, bold=False, color=GRIS):
    r.font.name = FONT
    r._element.rPr.rFonts.set(qn('w:eastAsia'), FONT)
    r.font.size = DocPt(size); r.bold = bold; r.font.color.rgb = color

def para(doc, text, *, size=11, bold=False, color=GRIS, space_after=6, shade_fill=None):
    p = doc.add_paragraph(); p.paragraph_format.space_after = DocPt(space_after)
    if shade_fill: shade(p, shade_fill)
    r = p.add_run(text); run(r, size=size, bold=bold, color=color); return p

def banda(doc, text):
    return para(doc, "  "+text, size=13, bold=True, color=BLANCO, shade_fill="095292", space_after=8)

def add_inline_docx(p, text, *, size=11, color=GRIS):
    """Igual que uniajc_slides_engine._rich pero para runs de docx: soporta @@negrita@@."""
    for part in re.split(r'(@@.*?@@)', text):
        if not part:
            continue
        r = p.add_run()
        if part.startswith('@@') and part.endswith('@@'):
            r.text = part[2:-2]
            run(r, size=size, bold=True, color=color)
        else:
            r.text = part
            run(r, size=size, color=color)

def bullets(doc, items):
    for it in items:
        p = doc.add_paragraph(style='List Bullet'); p.paragraph_format.space_after = DocPt(2)
        add_inline_docx(p, it)

DIAGRAMAS_BD2 = {
    1: {
        "titulo": "ER minimo VetCare (con cardinalidad)",
        "sub": "La FK siempre vive en la tabla del lado “N” de la relacion",
        "boxes": [
            {"id": "dueno", "label": "Dueño\nid_dueno (PK)\nnombre, telefono", "x": 0.6, "y": 2.2, "w": 2.7, "h": 1.6, "color": NAVY},
            {"id": "mascota", "label": "Mascota\nid_mascota (PK)\nid_dueno (FK)\nactiva", "x": 4.1, "y": 2.2, "w": 2.7, "h": 1.6, "color": CIAN},
            {"id": "cita", "label": "Cita\nid_cita (PK)\nid_mascota (FK)\nfecha_hora", "x": 7.6, "y": 2.2, "w": 2.7, "h": 1.6, "color": NAVY},
            {"id": "vet", "label": "Veterinario\nid_veterinario (PK)", "x": 7.6, "y": 4.4, "w": 2.7, "h": 1.1, "color": CIAN},
        ],
        "arrows": [
            {"src": "dueno", "dst": "mascota", "label": "1 : N"},
            {"src": "mascota", "dst": "cita", "label": "1 : N"},
            {"src": "vet", "dst": "cita", "label": "1 : N"},
        ],
        "note": "“Un dueño tiene N mascotas”, “una mascota tiene N citas”. La PK identifica cada fila; la FK materializa la relación y la BD la hace cumplir.",
    },
    10: {
        "titulo": "Doble reserva sin control de concurrencia",
        "sub": "Dos transacciones concurrentes leen “libre” antes de que ninguna confirme",
        "boxes": [
            {"id": "t1a", "label": "T1 (Recepción A)\nlee franja: LIBRE", "x": 0.8, "y": 2.2, "w": 3.1, "h": 1.0, "color": NAVY},
            {"id": "t1b", "label": "T1: INSERT cita\nCOMMIT → OK", "x": 4.6, "y": 2.2, "w": 3.1, "h": 1.0, "color": NAVY},
            {"id": "t2a", "label": "T2 (Recepción B)\nlee franja: LIBRE", "x": 0.8, "y": 3.7, "w": 3.1, "h": 1.0, "color": CIAN},
            {"id": "t2b", "label": "T2: INSERT cita\nCOMMIT → ¡DOBLE RESERVA!", "x": 4.6, "y": 3.7, "w": 3.1, "h": 1.0, "color": PPTX_RED},
        ],
        "arrows": [
            {"src": "t1a", "dst": "t1b", "label": "tiempo →"},
            {"src": "t2a", "dst": "t2b", "label": "tiempo →"},
        ],
        "note": "Mitigación: UNIQUE(id_veterinario, fecha_hora) hace que el segundo INSERT falle automáticamente en vez de crear la doble reserva.",
    },
}


# Codigo PROYECTABLE por clase: el fragmento minimo que el estudiante debe ver en
# pantalla mientras el docente explica (no el script completo — ese va en Codigo/).
CODIGO_SLIDE = {
    1: ("El DDL minimo que sostiene el ER", [
        "CREATE TABLE mascota (",
        "  id_mascota INT PRIMARY KEY,               -- PK: identifica la fila",
        "  id_dueno   INT NOT NULL",
        "             REFERENCES dueno(id_dueno),    -- FK: materializa la relacion",
        "  nombre     VARCHAR(60) NOT NULL,",
        "  activa     CHAR(1) DEFAULT 'S'",
        "             CHECK (activa IN ('S','N'))    -- regla de negocio en la BD",
        ");",
    ], "La FK vive en el lado 'N' de la relacion. El CHECK ya es una regla de negocio."),
    3: ("La validacion que justifica usar un procedimiento", [
        "SELECT activa INTO v_activa FROM mascota",
        " WHERE id_mascota = p_id_mascota;",
        "",
        "IF v_activa <> 'S' THEN",
        "  p_msg := 'ERROR: mascota inactiva; no se agenda';",
        "  RETURN;                       -- sale SIN insertar",
        "END IF;",
        "",
        "INSERT INTO cita(...) VALUES (...);",
    ], "Sin este IF, el proc es solo un INSERT con nombre: no resuelve nada."),
    4: ("Trigger de auditoria: nadie tiene que acordarse de registrarlo", [
        "CREATE OR REPLACE TRIGGER trg_audit_cancelacion_cita",
        "AFTER UPDATE ON cita FOR EACH ROW",
        "WHEN (NEW.estado = 'CANCELADA')",
        "BEGIN",
        "  INSERT INTO auditoria_cita(id_cita, estado_ant, estado_new, usuario, fecha)",
        "  VALUES (:NEW.id_cita, :OLD.estado, :NEW.estado, USER, SYSDATE);",
        "END;",
    ], "Se dispara solo. Riesgo: es invisible para quien solo lee el codigo de la app."),
    7: ("Un indice se justifica con la consulta que lo usa", [
        "-- Consulta frecuente: la agenda del dia",
        "SELECT ... FROM cita WHERE fecha_hora >= :hoy;",
        "",
        "CREATE INDEX idx_cita_fecha ON cita(fecha_hora);",
        "",
        "-- Mal candidato: baja cardinalidad (solo 'S' o 'N')",
        "-- CREATE INDEX idx_mascota_activa ON mascota(activa);",
    ], "Cada indice acelera lecturas y encarece INSERT/UPDATE/DELETE. Indexar todo es un error."),
    8: ("Todo o nada: la transaccion de facturacion", [
        "BEGIN;",
        "  INSERT INTO factura(...)         VALUES (...);",
        "  INSERT INTO detalle_factura(...) VALUES (...);",
        "  UPDATE insumo SET stock = stock - :cant",
        "   WHERE id_insumo = :id AND stock >= :cant;   -- 0 filas si no alcanza",
        "  -- si afecto 0 filas ->",
        "  ROLLBACK;   -- de lo contrario: COMMIT;",
        "END;",
    ], "La condicion stock >= :cant evita el stock negativo; el ROLLBACK evita la factura a medias."),
    10: ("La restriccion que hace imposible la doble reserva", [
        "ALTER TABLE cita",
        "  ADD CONSTRAINT uq_cita_vet_franja",
        "  UNIQUE (id_veterinario, fecha_hora);",
        "",
        "-- T2 intenta la misma franja que T1:",
        "-- ORA-00001: unique constraint violated",
    ], "Poner solo BEGIN/COMMIT no basta: ambas transacciones leen 'libre' antes de confirmar."),
    12: ("El contrato que la app consume (no SQL suelto)", [
        "sp_agendar_cita(",
        "   p_id_cita     IN  NUMBER,",
        "   p_id_mascota  IN  NUMBER,",
        "   p_fecha       IN  TIMESTAMP,",
        "   p_msg         OUT VARCHAR2   -- 'OK: ...' | 'ERROR: ...'",
        ")",
    ], "La app llama el proc con parametros tipados: por eso no hay inyeccion SQL."),
}

# Comparaciones antes/despues (lo que mejor se entiende visualmente).
ANTES_DESPUES = {
    6: {
        "titulo": "Optimizar es un ANTES medible, no una opinion",
        "b_t": "Antes",
        "b": ["`SELECT *` trae columnas que nadie usa",
              "JOIN sin filtro: cruza el historico completo",
              "Funcion sobre la columna del WHERE bloquea el indice",
              "Plan: **TABLE ACCESS FULL** (~120.000 filas)"],
        "a_t": "Despues",
        "a": ["Solo las columnas necesarias",
              "Filtro por fecha ANTES del JOIN",
              "Comparacion directa sobre la columna indexada",
              "Plan: **INDEX RANGE SCAN** (~340 filas)"],
    },
    2: {
        "titulo": "Minimo privilegio, en concreto",
        "b_t": "Lo que suele pasar",
        "b": ["Un solo usuario `admin` que todos comparten",
              "GRANT ALL 'para que no falle nada'",
              "Nadie sabe quien borro que (sin trazabilidad)",
              "Se van del cargo y la cuenta sigue viva"],
        "a_t": "Lo que pide el taller",
        "a": ["4 roles: ADMIN_BD · RECEPCION · VETERINARIO · AUDITOR",
              "Privilegio por objeto y operacion (matriz)",
              "RECEPCION nunca hace DELETE sobre historial",
              "Politica de baja: revocacion inmediata"],
    },
    3: {
        "titulo": "Por que un procedimiento y no SQL en cada pantalla",
        "b_t": "Sin procedimiento",
        "b": ["Cada pantalla reescribe la regla a su manera",
              "Alguien la escribe distinta... o la olvida",
              "La app arma SQL con texto -> inyeccion SQL",
              "Cambiar la regla = buscarla en N lugares"],
        "a_t": "Con procedimiento",
        "a": ["La regla vive UNA vez, dentro de la BD",
              "Toda la app la respeta sin excepcion",
              "Parametros tipados: sin concatenar texto",
              "Cambiar la regla = un solo lugar"],
    },
}


def _slide_summary(bullets_, max_chars=110):
    """Resume cada viñeta de teoria (pensada para el guion, muy detallada) a su
    idea central para que la diapositiva de estudiante no quede sobrecargada de texto.
    El guion docente conserva el texto completo; solo la slide usa esta versión corta."""
    out = []
    for b in bullets_:
        first = re.split(r"(?<=[a-záéíóúü0-9\)])\.\s", b, maxsplit=1)[0].strip()
        if len(first) > max_chars or len(first) < 12:
            # colon-only label (ej. "Control pesimista:") o frase larga: usa un corte por longitud
            base = b if len(first) < 12 else first
            first = base[:max_chars].rsplit(" ", 1)[0].rstrip(":,;") + "…"
        out.append(first)
    return out


def cover_pptx(prs, c):
    """Portada limpia: marca + título + subtítulo. Meta PI/agenda → 2ª slide."""
    class_cover(prs, c['titulo'], subtitulo=c['subtitulo'], clase_n=c['n'], idx=1)

def build_pptx(c):
    if c['tipo'] == 'parcial':
        return None
    prs = new_prs(); cover_pptx(prs, c); idx = 2
    tipo_lbl = "autonoma (festivo)" if c['tipo']=='autonoma' else "regular"
    # 2ª slide: encuadre / objetivos (contenido que salió de la portada)
    content_slide(prs, "Encuadre de hoy · Objetivo PI", [
        f"**Hoy avanzamos el PI en:** {c['hito_pi']}",
        f"Herramienta: **{c['herramienta']}** · Bloque **120 min** · Teoría breve · Taller PI",
        f"**Entregable de hoy:** {c['entregable']}",
        "Gratis + navegador · free tier · sin software de pago obligatorio.",
        "La teoría no es un tema aislado: alimenta evidencias de la rúbrica del PI.",
        "Al salir: avance concreto en el paquete VetCare del equipo.",
    ], idx=idx); idx += 1
    block_timeline_slide(prs, "Mapa del bloque de hoy (120 min)", [
        ("0-10", f"Encuadre · clase {tipo_lbl} · VetCare"),
        ("10-35", "Teoría Core breve (al servicio del PI)"),
        ("35-55", "Demo con la herramienta del día"),
        ("55-105", "Taller guiado = tarea del PI"),
        ("105-120", "Criterios de exito · cierre · dudas del PI"),
    ], idx=idx); idx += 1
    content_slide(prs, "Teoria Core (breve)", _slide_summary(c['teoria']), idx=idx, size=15); idx += 1
    dg = DIAGRAMAS_BD2.get(c['n'])
    if dg:
        diagram_boxes_slide(
            prs, dg["titulo"], dg["boxes"], arrows=dg.get("arrows"),
            sub=dg.get("sub"), note=dg.get("note"), idx=idx,
        )
        idx += 1
    ad = ANTES_DESPUES.get(c['n'])
    if ad:
        before_after_slide(prs, ad["titulo"], ad["b_t"], ad["b"], ad["a_t"], ad["a"], idx=idx)
        idx += 1
    cs = CODIGO_SLIDE.get(c['n'])
    if cs:
        pseudo_code_slide(prs, cs[0], cs[1], caption=cs[2], idx=idx)
        idx += 1
    content_slide(prs, "Demo del dia", [
        f"**Herramienta:** {c['herramienta']}",
        f"**Demo:** {c['demo']}",
        "Sigan el mismo dominio VetCare (no inventen otro caso).",
        "Al final de la demo: dejar enlace/script compartible al equipo.",
    ], idx=idx); idx += 1
    tools = HERRAMIENTAS_DIA.get(c["n"])
    if tools:
        herramientas_slide(prs, tools, title="Herramientas de hoy",
                           sub="Gratis · navegador o free tier", idx=idx)
        idx += 1
    tb = TALLER_BLOQUE.get(c["n"], {})
    label = "Actividad autonoma" if c["tipo"] == "autonoma" else "Taller PI VetCare"
    if tb.get("contexto"):
        content_slide(prs, f"{label} — contexto / por que importa", tb["contexto"], idx=idx, size=16)
        idx += 1
    obj = tb.get("objetivo") or c["hito_pi"]
    crit = [f"@@Exito:@@ {x}" for x in tb.get("criterios", [])] or [
        f"@@Entregable:@@ {c['entregable']}",
        "Evidencia en playground o archivos del equipo.",
    ]
    content_slide(prs, f"{label} — objetivo y criterios", [f"@@Objetivo:@@ {obj}", *crit], idx=idx, size=15)
    idx += 1
    if tb.get("escenario"):
        content_slide(prs, f"{label} — escenario / datos de partida", tb["escenario"], idx=idx, size=16)
        idx += 1
    steps_visual_slide(prs, f"{label} — pasos guiados", [(t, "") for t in c["taller"]], idx=idx)
    idx += 1
    if tb.get("pistas"):
        checklist_slide(prs, f"{label} — pistas (checklist vacio)", tb["pistas"], idx=idx)
        idx += 1
    content_slide(prs, "Criterios de exito / entregable", [
        f"**Entregable:** {c['entregable']}",
        "Evidencia en playground (enlace) o archivo SQL/PNG del equipo.",
        "Actualizar checklist PI (que criterio de rubrica avanzo).",
        "@@Entrega en ExamLab@@ (Talleres) — domingo 23:59 cuando aplique taller.",
    ], idx=idx); idx += 1
    box_note_slide(prs, "Para el PI esta semana", [
        ("info", f"Hito: {c['hito_pi']}"),
        ("aclaracion", "Enunciado completo: Clases/Proyecto Integrador/ (VetCare DB)."),
        ("advertencia", "Taller de la semana en ExamLab: domingo 23:59 (regla del Acuerdo) cuando aplique."),
    ], idx=idx); idx += 1
    # El QUIZ no va en el material del estudiante: ni proyectado ni anunciado.
    # Vive solo en Kit docente/Clase N/ (enunciados + CLAVE DOCENTE aparte), que
    # el docente aplica por el canal que decida. Anticiparlo en la diapositiva le
    # quita sentido como comprobacion.
    closing_slide(prs, f"Clase {c['n']} · VetCare avanza", [
        c['hito_pi'],
        f"Entregable: {c['entregable']}",
        "Siguiente clase: continuar el hilo del PI segun plan",
    ], accent="Teoria breve · practica = PI")
    out_dir = CLASES_DIR / f"Clase {c['n']} - {c['slug']}"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "Presentacion.pptx"
    prs.save(str(out)); print("PPTX", out)
    return out

def build_taller_docx(c):
    if c['tipo']=='parcial': return None
    tb = TALLER_BLOQUE.get(c['n'], {})
    doc = Document(); banda(doc, f"Taller PI · Clase {c['n']} · Bases de Datos II")
    para(doc, c['titulo'], size=14, bold=True, color=AZUL)
    para(doc, "Hilo conductor: Proyecto Integrador VetCare DB (no es un ejercicio desconectado).", size=11, bold=True)
    para(doc, f"Herramienta: {c['herramienta']}")
    para(doc, f"Hoy avanzamos el PI en: {c['hito_pi']}", shade_fill="FFF8D6")
    para(doc, "1. Contexto / por que importa al PI", size=12, bold=True, color=AZUL)
    bullets(doc, tb.get('contexto') or ["Trabaje sobre el dominio VetCare del equipo."])
    para(doc, "2. Objetivo", size=12, bold=True, color=AZUL)
    para(doc, tb.get('objetivo', c['hito_pi']))
    para(doc, "3. Escenario / datos de partida", size=12, bold=True, color=AZUL)
    bullets(doc, tb.get('escenario') or ["Usar el DDL/ER VetCare del equipo."])
    para(doc, "4. Actividades (pasos guiados)", size=12, bold=True, color=AZUL)
    bullets(doc, c['taller'])
    para(doc, "5. Entregable", size=12, bold=True, color=AZUL)
    para(doc, c['entregable'], shade_fill="E8F4FA")
    para(doc, "6. Criterios de exito", size=12, bold=True, color=AZUL)
    bullets(doc, tb.get('criterios') or [
        "Avance real del VetCare del equipo.",
        "Evidencia ejecutable o diagrama exportado.",
        "Criterio de rubrica del PI movido hoy.",
    ])
    para(doc, "7. Pistas (checklist vacio — sin solucion)", size=12, bold=True, color=AZUL)
    bullets(doc, tb.get('pistas') or ["Revisar evidencia antes de subir."])
    para(doc, "8. Entrega", size=12, bold=True, color=AZUL)
    _p_entrega = doc.add_paragraph(); _p_entrega.paragraph_format.space_after = DocPt(6)
    add_inline_docx(_p_entrega, "@@Sube tu taller en ExamLab@@ (examlab.lovable.app/app · módulo Talleres) — domingo 23:59 cuando aplique.")
    out_dir = CLASES_DIR / f"Clase {c['n']} - {c['slug']}"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"Taller PI - Clase {c['n']} - VetCare.docx"
    doc.save(str(out)); print("TALLER", out); return out


def build_solucion_docx(c):
    if c['tipo']=='parcial': return None
    sol = SOLUCION.get(c['n'])
    if not sol: return None
    kit = KIT_DIR / f"Clase {c['n']}"
    kit.mkdir(parents=True, exist_ok=True)
    stem = f"Solucion Taller Clase {c['n']} - VetCare"
    lines = [f"# {sol['titulo']}", "",
             "> DOCUMENTO DOCENTE — PRIVADO. No publicar en Clases/.", "",
             f"**Resumen:** {sol['resumen']}", "",
             "## Alineacion",
             f"- Taller: `Clases/Clase {c['n']} - {c['slug']}/Taller PI - Clase {c['n']} - VetCare.docx`",
             f"- Hito: {c['hito_pi']}", f"- Entregable: {c['entregable']}", "",
             "## Solucion paso a paso"]
    for i, s in enumerate(sol.get('pasos', []), 1):
        lines.append(f"{i}. {s}")
    lines += ["", "## Ejemplo / SQL / artefactos"]
    for e in sol.get('ejemplo', []):
        lines.append(f"- {e}")
    if c.get('sql'):
        lines.append(f"- Script demo: `Kit docente/Clase {c['n']}/Codigo/{c['sql']}`")
    lines += ["", "## Rubrica corta"]
    for r in sol.get('rubrica', []):
        lines.append(f"- [ ] {r}")
    lines += ["", "## Errores frecuentes"]
    for e in sol.get('errores', []):
        lines.append(f"- {e}")
    lines += ["", "Entrega en ExamLab.", ""]
    (kit / f"{stem}.md").write_text("\n".join(lines), encoding="utf-8")
    doc = Document(); banda(doc, sol['titulo'])
    para(doc, "DOCUMENTO DOCENTE — PRIVADO (no va en Clases/)", bold=True, color=RGBColor(0xA0,0x20,0x30), shade_fill="FBE4E4")
    para(doc, sol['resumen'], shade_fill="E8F4FA")
    para(doc, "Alineacion al enunciado", size=12, bold=True, color=AZUL)
    bullets(doc, [
        f"Taller: Clases/Clase {c['n']} - {c['slug']}/Taller PI - Clase {c['n']} - VetCare.docx",
        f"Hito: {c['hito_pi']}",
        f"Entregable: {c['entregable']}",
    ])
    para(doc, "Solucion paso a paso", size=12, bold=True, color=AZUL)
    bullets(doc, sol.get('pasos', []))
    para(doc, "Ejemplo / SQL / artefactos", size=12, bold=True, color=AZUL)
    bullets(doc, sol.get('ejemplo', []) + ([f"Script demo: Codigo/{c['sql']}"] if c.get('sql') else []))
    para(doc, "Rubrica corta", size=12, bold=True, color=AZUL)
    bullets(doc, ["[ ] "+r for r in sol.get('rubrica', [])])
    para(doc, "Errores frecuentes", size=12, bold=True, color=AZUL)
    bullets(doc, sol.get('errores', []))
    out = kit / f"{stem}.docx"
    doc.save(str(out)); print("SOLUCION", out); return out


# Imagenes de SALIDA ESPERADA por clase (generadas por config/slides/mockups.py).
# El guion las embebe con el token [[captura: archivo.png]]; si el archivo no
# existe, guion_md_a_docx.py deja la caja "inserta aqui la captura" y no rompe.
CAPTURAS_CLASE = {
    1: [("Resultado del JOIN de verificacion del ER (lo que debe salir tras los INSERT)",
         "salida-join-vetcare.png")],
    3: [("sp_agendar_cita: caso OK vs caso rechazado por mascota inactiva",
         "salida-proc-ok-y-error.png")],
    6: [("Plan de ejecucion ANTES vs DESPUES (FULL SCAN -> INDEX RANGE SCAN)",
         "salida-explain-antes-despues.png")],
    8: [("Transaccion con stock insuficiente: el ROLLBACK deja todo como estaba",
         "salida-rollback-stock.png")],
    10: [("Evidencia del problema: dos citas en la misma franja (sin restriccion)",
          "salida-doble-reserva.png"),
         ("El MISMO INSERT ya con UNIQUE: la BD lo rechaza sola",
          "salida-unique-rechaza.png")],
}


def _capturas_md(n):
    """Lineas 📸 del guion para la clase n (con token explicito de archivo)."""
    items = CAPTURAS_CLASE.get(n)
    if not items:
        return f"📸 Pantallazo: [CAP: demo VetCare Clase {n}]\n"
    return "".join(f"📸 {cap} [[captura: {fn}]]\n" for cap, fn in items)


def build_guion_md(c):
    kit = KIT_DIR / f"Clase {c['n']}"
    kit.mkdir(parents=True, exist_ok=True)
    (kit/"Capturas").mkdir(exist_ok=True)
    (kit/"Codigo").mkdir(exist_ok=True)
    if c['tipo']=='parcial':
        md = f"""# Guia docente · Clase {c['n']} · {c['titulo']} (solo evaluacion)

> Dia de **parcial = solo evaluacion**. No hay tema nuevo ni avance de PI en clase.
> Enunciado/solucion: Parciales/{c.get('parcial','')}

## Checklist 120 min

| Min | Accion |
|---|---|
| 0-10 | Ingreso, asistencia, normas (sin material abierto no autorizado). |
| 10-15 | Entregar enunciado (impreso / PDF). Aclarar tiempo y canal de dudas de forma. |
| 15-100 | Desarrollo del parcial (silencio de trabajo). |
| 100-110 | Aviso 10 min; revisiones de integridad. |
| 110-120 | Cierre, recoleccion, recordatorio: PI se prepara en clases regulares (no hoy). |

## Notas
- No mezclar «Tema · Parcial».
- Prep PI / sustentacion: Clases 11-12; cierre PI: Clase 15.
- Solucion privada: archivo * SOLUCION.docx en Parciales/.
"""
        path = kit / f"Guia aplicacion {c['titulo']} - Clase {c['n']}.md"
        path.write_text(md, encoding='utf-8')
        # placeholder capturas
        (kit/"Capturas"/".gitkeep").write_text("", encoding='utf-8')
        return path

    slides_ref = [
        "Slide 1 portada (Clase N + titulo VetCare)",
        "Slide Agenda 120 min",
        "Slide Objetivo PI de la clase",
        "Slide Teoria Core",
        "Slide Demo del dia",
        "Slide Herramientas de hoy (logos 3-4)",
        "Bloque Taller ampliado: contexto / objetivo / escenario / pasos / pistas",
        "Slide Criterios de exito / entregable",
        "Slide Para el PI esta semana",
        "Slide Cierre",
        "Solucion PRIVADA: Kit docente/Clase N/Solucion Taller Clase N - VetCare.docx",
    ]
    tipo = "AUTONOMA (festivo)" if c['tipo']=='autonoma' else "REGULAR"
    bloques = ""
    if c['tipo']=='autonoma':
        plan = """## Plan minuto a minuto (120 min equivalentes — trabajo autonomo)

> El estudiante trabaja sin encuentro sincrono. Usted publica este guion resumido + taller en ExamLab.

### Bloque A (0-20) · Encuadre PI
**Decir/publicar:** «Hoy avanzamos el PI en: {hito}. No es un taller suelto.»
Referencia slides: Agenda + Objetivo PI.

### Bloque B (20-45) · Teoria minima
Leer Teoria Core. Tomar notas en el informe del PI.

### Bloque C (45-100) · Practica = entregable PI
Seguir el taller estudiante. Herramienta: {herr}.
Salida esperada de la practica (publiquela junto al enunciado para que el
estudiante autonomo sepa si le quedo bien):
{caps}
### Bloque D (100-120) · Empaquetado y cierre
Subir entregable a ExamLab. Actualizar checklist PI del equipo.
""".format(hito=c['hito_pi'], herr=c['herramienta'], caps=_capturas_md(c['n']))
    else:
        plan = f"""## Plan minuto a minuto (120 min) — texto casi literal

### 0-10 · Encuadre
**Decir:** «Buenas. Hoy el hilo es VetCare DB. Avanzamos el PI en: {c['hito_pi']}.
La teoria sera corta; el peso esta en el taller del proyecto.»
Mostrar slide Agenda + Objetivo PI.
Pasar asistencia. Recordar herramientas gratis+nube.

### 10-35 · Teoria Core (breve)
**Decir:** «Solo lo necesario para el entregable de hoy.»
Cubrir:
""" + "\n".join(f"- {t}" for t in c['teoria']) + f"""
Referencia: slide Teoria Core.
Pregunta al aire (2 min): ¿como se conecta esto con su VetCare?

### 35-55 · Demo paso a paso
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: {c['demo']}
Herramienta: {c['herramienta']}
""" + _capturas_md(c['n']) + f"""Dejar script/enlace en el chat o en ExamLab.

### 55-105 · Taller guiado = tarea del PI
**Decir:** «Equipos: abran su carpeta VetCare. Esto suma a la rubrica del PI. Al final suben el taller en ExamLab.»
Usar bloque Taller ampliado (contexto->pistas). Solucion en Kit docente/Solucion Taller... (no proyectar completa).
Actividades:
""" + "\n".join(f"{i+1}. {t}" for i,t in enumerate(c['taller'])) + f"""
Circular por equipos (o salas). Empujar evidencia, no perfectionismo.
Entregable: {c['entregable']}
📸 Pantallazo: [CAP: avance equipo / playground Clase {c['n']}]

### 105-115 · Criterios de exito + quiz corto
Repasar checklist del dia (slide Criterios).
""" + (
        f"Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). "
        f"Version impresa/proyectable de respaldo: `Quiz Clase {c['n']} - VetCare.docx`. "
        f"Clave para usted: `Quiz Clase {c['n']} - CLAVE DOCENTE.docx` (**no proyectar**)."
        if c['quiz'] else
        "Sin quiz formal: 2 preguntas orales de cierre."
    ) + f"""

### 115-120 · Cierre
**Decir:** «Queda avanzado: {c['hito_pi']}. Suban el taller a ExamLab hoy domingo 23:59 si aplica. Enunciado PI en Clases/Proyecto Integrador.»
Slide cierre. Dudas finales.
"""

    md = f"""# Guion docente · Clase {c['n']} · {c['titulo']}

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** {tipo}
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** {c['hito_pi']}
- **Entregable de hoy:** {c['entregable']}
- **Herramienta:** {c['herramienta']}
- **Slides:** Clases/Clase {c['n']} - {c['slug']}/Presentacion.pptx

> Sin mapa completo del curso, sin bio del docente, sin fechas de periodo.
> Presentacion del Curso / Acuerdo cubren logistica global.

## Fundamento teorico para el docente (al servicio del PI)

El objetivo de la clase no es «cubrir un capitulo» aislado, sino producir evidencia
del PI VetCare. La teoria se limita a desbloquear el taller.

""" + "\n".join(f"- {t}" for t in c['teoria']) + f"""

**Demo que usted debe poder repetir:** {c['demo']}

## Referencias a diapositivas
""" + "\n".join(f"{i+1}. {s}" for i,s in enumerate(slides_ref)) + "\n\n" + plan + f"""

## Codigo / scripts
Carpeta Codigo/ — archivo {c['sql'] or 'N/A'}.

## Capturas
Carpeta Capturas/. Placeholders [CAP: ...] arriba; reemplazar por PNG reales cuando pueda
(Playwright/manual en DB Fiddle, draw.io, Live SQL).

## Criterios de exito del dia
- Equipos tienen el entregable o gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
"""
    path = kit / f"Guion Docente Clase {c['n']} - {c['slug']}.md"
    path.write_text(md, encoding='utf-8')
    # capturas placeholder readme
    (kit/"Capturas"/"README_capturas.txt").write_text(
        f"Placeholders pendientes Clase {c['n']}:\n"
        f"- [CAP: demo {c['herramienta']} VetCare Clase {c['n']}]\n"
        f"- [CAP: avance equipo / playground Clase {c['n']}]\n"
        "Nombre sugerido: cap01_demo.png, cap02_taller.png\n", encoding='utf-8')
    if c['sql'] and c['sql'] in SQL_BODIES:
        (kit/"Codigo"/c['sql']).write_text(SQL_BODIES[c['sql']], encoding='utf-8')
    return path

def build_quiz(c):
    """Quiz estudiante (sin claves) + CLAVE DOCENTE aparte. Nunca claves en Clases/."""
    if not c.get('quiz') or c['n'] not in QUIZ:
        return None
    kit = KIT_DIR / f"Clase {c['n']}"
    kit.mkdir(parents=True, exist_ok=True)
    quiz = QUIZ[c['n']]

    out = kit / f"Quiz Clase {c['n']} - VetCare.docx"
    doc = Document()
    banda(doc, f"Quiz · Clase {c['n']} · VetCare PI")
    para(doc, "Versión para aplicar en clase (sin claves). Corrección: CLAVE DOCENTE.", size=10, bold=True)
    para(doc, "8–10 min · individual · VetCare + tema del día. OM + V/F + abiertas cortas.", size=10)
    for i, item in enumerate(quiz, 1):
        for line in student_lines(item, i):
            text = line.replace("**", "")
            para(doc, text.lstrip(), bold=text.startswith(f"{i}."), size=11)
    doc.save(str(out))
    print("QUIZ", out)

    clave_out = kit / f"Quiz Clase {c['n']} - CLAVE DOCENTE.docx"
    doc_k = Document()
    banda(doc_k, f"CLAVE DOCENTE · Quiz Clase {c['n']} · VetCare")
    para(doc_k, "PRIVADO DOCENTE — no compartir ni proyectar", size=11, bold=True,
         color=RGBColor(0xA0, 0x20, 0x30), shade_fill="FBE4E4")
    para(doc_k, "Usar tras el quiz para retro. No proyectar en Presentacion.pptx.", size=10)
    for i, item in enumerate(quiz, 1):
        para(doc_k, clave_text(item, i), size=10, shade_fill="E8F4FA")
    doc_k.save(str(clave_out))
    print("CLAVE", clave_out)
    return out

def convert_guion(md_path: Path):
    conv = SLIDES / "guion_md_a_docx.py"
    if not conv.exists(): return None
    try:
        subprocess.run([sys.executable, str(conv), str(md_path)], check=False)
    except Exception as e:
        print("WARN convert", e)

def build_readme():
    text = """# Kit docente — Bases de Datos II (2026-2)

Material **privado** del docente. Los estudiantes solo ven Clases/.

## Enfoque
Todo el material de clase esta orientado a avanzar el **Proyecto Integrador VetCare DB**.
Teoria breve; talleres = entregables del PI.

## Por clase
- Guion Docente Clase N - ….md + .docx (via guion_md_a_docx.py)
- Quiz Clase N - VetCare.docx (sin claves) + Quiz Clase N - CLAVE DOCENTE.docx (privado; no proyectar)
- Codigo/*.sql demos VetCare
- Capturas/ placeholders [CAP:…] (pendiente pantallazos reales)
- Dias 5/9/14: Guia aplicacion Parcial N (solo evaluacion)

## Builds
`ash
python .config/slides/build_uniajc_bd2_all.py
python .config/slides/build_uniajc_bd2_curso.py
`

## PI
- Estudiante: Clases/Proyecto Integrador/
- Docente: Kit docente/Proyecto Integrador/
"""
    (KIT_DIR / "README.md").write_text(text, encoding='utf-8')

EXAMLAB_URL = "https://examlab.lovable.app/app"

# Boceto sugerido para la Pizarra (whiteboard) de cada clase — agnostico de
# herramienta: sirve igual en el whiteboard de ExamLab, en una pizarra fisica
# o en draw.io/Excalidraw si el docente prefiere otra.
PIZARRA = {
    1: "ER minimo: Dueño —1:N→ Mascota —1:N→ Cita. Marcar PK subrayada y FK con flecha.",
    2: "Tabla simple 3 columnas: Rol | Objeto | Privilegio (llenar en vivo con los 4 roles del taller).",
    3: "Flujo: App → llama sp_agendar_cita → valida mascota.activa → INSERT o mensaje de error.",
    4: "Mismo ER de Clase 1 + una nota junto a Cita: 'AQUI dispara el trigger de auditoria' y junto a Mascota: 'AQUI vive la fn_precio_base'.",
    6: "Dos columnas: 'Antes' (consulta con SELECT * y JOIN sin filtro) vs 'Despues' (columnas puntuales + filtro temprano) sobre el mismo dibujo de tablas.",
    7: "Tabla caliente (ej. Cita) con una flecha grande hacia un rectangulo 'INDICE idx_cita_fecha' y la palabra 'acelera lectura / cuesta escritura'.",
    8: "Linea de tiempo horizontal: BEGIN → INSERT factura → INSERT detalle → UPDATE stock → COMMIT/ROLLBACK con una bifurcacion visual en el ROLLBACK.",
    10: "La MISMA linea de tiempo T1/T2 de la diapositiva de Clase 10, pero redibujada en vivo con los IDs reales que use el script de demo.",
    11: "Checklist en 2 columnas: Evidencia (ER, DDL, roles, procs, fn, triggers, opt) | Si/No/Parcial — llenar con el equipo en vivo.",
    12: "Caja 'App' — flecha rotulada con el nombre del proc (ej. sp_agendar_cita) — caja 'Base de datos'. Sin flecha directa App→tablas.",
    13: "Tabla 4 columnas: Contexto | Fallo | Leccion | Cambio en VetCare — una fila por caso discutido.",
    15: "Checklist final de empaquetado: ER, DDL, roles, procs, triggers, optimizacion, transacciones, concurrencia, contrato, informe — marcar completos.",
}

# Prompt generico reutilizable: se llena con el tema puntual de la clase.
_PROMPT_TEMPLATE = (
    "Actua como docente de Bases de Datos II. Usando el dominio VetCare (Dueño, "
    "Mascota, Cita, Veterinario, Insumo, Factura), dame un ejemplo minimo en SQL "
    "(Oracle/PostgreSQL) sobre «{tema}»: (1) el DDL de las tablas que necesito, "
    "(2) datos de ejemplo realistas de una clinica veterinaria (INSERT), (3) el "
    "codigo que ilustra «{tema}» paso a paso, (4) en 3 lineas, que debe notar el "
    "estudiante cuando lo vea ejecutar."
)


def build_guia_practica():
    """Guia docente de la PARTE PRACTICA de cada clase: que actividad hacer,
    objetivo, boceto de pizarra + prompt de apoyo + script SQL completo para la
    demo, pasos guiados, entregable y criterios de exito. Agnostica de
    plataforma — ExamLab se menciona solo como el lugar de entrega/quiz, sin
    detalle de configuracion. Reorganiza el mismo contenido de CLASES/
    TALLER_BLOQUE/SOLUCION/SQL_BODIES que ya usan el Guion Docente y el Taller."""
    lines = [
        "# Guia Docente — Parte Practica por Clase (Bases de Datos II, 2026-2)",
        "",
        "> Cada clase = una practica con objetivo propio. La demo se apoya en un",
        "> boceto de pizarra + un script SQL completo (con datos) para que usted lo",
        "> ejecute en vivo en Oracle Live SQL / DB Fiddle. El taller y el quiz se",
        f"> entregan/presentan en ExamLab (`{EXAMLAB_URL}`) — no es la plataforma",
        "> oficial de la UNIAJC, pero es la que usamos para eso en este curso.",
        "",
    ]
    for c in CLASES:
        if c["tipo"] == "parcial":
            continue
        tb = TALLER_BLOQUE.get(c["n"], {})
        sol = SOLUCION.get(c["n"], {})
        lines += [
            f"## Clase {c['n']} — {c['titulo']}",
            "",
            f"**Objetivo practico:** {c['hito_pi']}",
        ]
        contexto = (tb.get("contexto") or [None])[0]
        if contexto:
            contexto = re.sub(r"@@Por qu[eé] importa[^@]*@@\s*", "", contexto).replace("@@", "")
            lines.append(f"**Por que importa:** {contexto}")
        lines += [
            "",
            "**Demo en vivo:**",
            f"- Pizarra: {PIZARRA.get(c['n'], 'Boceto libre del ejemplo de hoy sobre el ER de VetCare.')}",
            f"- Prompt de apoyo (IA, opcional si le falta tiempo de preparar): \"{_PROMPT_TEMPLATE.format(tema=c['titulo'].split('·')[0].strip())}\"",
        ]
        sql_key = c.get("sql")
        if sql_key and sql_key in SQL_BODIES:
            lines.append(f"- Script SQL completo para correr en vivo (con datos de ejemplo):")
            lines.append("```sql")
            lines.append(SQL_BODIES[sql_key].strip())
            lines.append("```")
        else:
            lines.append("- Esta clase no requiere script SQL nuevo: es analisis/discusion sobre lo ya construido.")
        lines += [
            "",
            "**Pasos guiados del taller:**",
        ]
        for i, t in enumerate(c["taller"], 1):
            lines.append(f"{i}. {t}")
        lines += [
            "",
            f"**Entregable:** {c['entregable']}",
            "**Criterios de exito:**",
        ]
        for cr in (tb.get("criterios") or sol.get("rubrica") or ["Avance verificable del PI VetCare."]):
            lines.append(f"- {cr}")
        n_preg = len(QUIZ.get(c["n"], []))
        lines += [
            "",
            f"**Quiz de cierre:** {n_preg} preguntas (banco completo en `Kit docente/Clase {c['n']}/Quiz Clase {c['n']} - VetCare.docx`).",
            f"**Entrega:** taller y quiz en ExamLab · domingo 23:59 cuando aplique el taller.",
            "",
            "---",
            "",
        ]
    lines += [
        "## Parciales (Clase 5 / 9 / 14)",
        "",
        "Solo evaluacion — enunciado + solucion en `Parciales/` (dominio VetCare).",
        "Se presentan en ExamLab con proctoring activado (es evaluacion formal",
        "presencial); duracion 90-100 min dentro del bloque de 120.",
        "",
        "## Proyecto Integrador VetCare DB",
        "",
        "Hilo conductor de todas las clases regulares/autonomas. Avance formal en",
        "Clase 11 (checkpoint) y entrega/sustentacion en Clase 15. Se sube a ExamLab",
        "como Proyecto (grupal); pesa 20% del Corte 3.",
        "",
    ]
    KIT_DIR.mkdir(parents=True, exist_ok=True)
    md_path = KIT_DIR / "Guia Docente - Parte Practica por Clase.md"
    md_path.write_text("\n".join(lines), encoding="utf-8")
    print("OK guia practica (md) ->", md_path)
    convert_guion(md_path)
    return md_path


def main():
    KIT_DIR.mkdir(parents=True, exist_ok=True)
    CLASES_DIR.mkdir(parents=True, exist_ok=True)
    build_readme()
    for c in CLASES:
        print("=== Clase", c['n'], c['tipo'], "===")
        build_pptx(c)
        build_taller_docx(c)
        build_solucion_docx(c)
        md = build_guion_md(c)
        if md: convert_guion(md)
        build_quiz(c)
    build_guia_practica()
    print("DONE")

if __name__ == '__main__':
    main()