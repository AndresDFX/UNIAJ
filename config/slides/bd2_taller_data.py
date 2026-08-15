# -*- coding: utf-8 -*-
"""Taller ampliado + soluciones BD II / VetCare (PRIVADO)."""

HERRAMIENTAS_DIA = {
    1: [
        {
            'name': 'draw.io',
            'logo': 'drawio.png',
            'note': 'ER VetCare',
        },
        {
            'name': 'DB Fiddle',
            'logo': 'dbfiddle.png',
            'note': 'DDL demo',
        },
        {
            'name': 'Oracle Live SQL',
            'logo': 'oracle_livesql.png',
            'note': 'Playground',
        },
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'Ficha del PI',
        },
    ],
    2: [
        {
            'name': 'Oracle Live SQL',
            'logo': 'oracle_livesql.png',
            'note': 'GRANT/roles',
        },
        {
            'name': 'DB Fiddle',
            'logo': 'dbfiddle.png',
            'note': 'SQL demo',
        },
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'Matriz roles',
        },
    ],
    3: [
        {
            'name': 'Oracle Live SQL',
            'logo': 'oracle_livesql.png',
            'note': 'Procedimientos',
        },
        {
            'name': 'DB Fiddle',
            'logo': 'dbfiddle.png',
            'note': 'Pruebas',
        },
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'Contrato proc',
        },
    ],
    4: [
        {
            'name': 'Oracle Live SQL',
            'logo': 'oracle_livesql.png',
            'note': 'Fn/trigger',
        },
        {
            'name': 'DB Fiddle',
            'logo': 'dbfiddle.png',
            'note': 'Pruebas',
        },
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'Plan backup',
        },
    ],
    6: [
        {
            'name': 'DB Fiddle',
            'logo': 'dbfiddle.png',
            'note': 'Antes/despues',
        },
        {
            'name': 'SQLTest.online',
            'logo': 'sqltest.png',
            'note': 'Multi-motor',
        },
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'Justificacion',
        },
    ],
    7: [
        {
            'name': 'DB Fiddle',
            'logo': 'dbfiddle.png',
            'note': 'CREATE INDEX',
        },
        {
            'name': 'draw.io',
            'logo': 'drawio.png',
            'note': 'Tabla caliente',
        },
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'Justificacion',
        },
    ],
    8: [
        {
            'name': 'Oracle Live SQL',
            'logo': 'oracle_livesql.png',
            'note': 'Transacciones',
        },
        {
            'name': 'DB Fiddle',
            'logo': 'dbfiddle.png',
            'note': 'ROLLBACK',
        },
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'Checklist tuning',
        },
    ],
    10: [
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'Escenarios T1/T2',
        },
        {
            'name': 'Oracle Live SQL',
            'logo': 'oracle_livesql.png',
            'note': 'Demo SQL',
        },
        {
            'name': 'DB Fiddle',
            'logo': 'dbfiddle.png',
            'note': 'Pruebas',
        },
    ],
    11: [
        {
            'name': 'Oracle Live SQL',
            'logo': 'oracle_livesql.png',
            'note': 'Demo procs',
        },
        {
            'name': 'draw.io',
            'logo': 'drawio.png',
            'note': 'ER',
        },
        {
            'name': 'DB Fiddle',
            'logo': 'dbfiddle.png',
            'note': 'DDL',
        },
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'Checklist',
        },
    ],
    12: [
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'Contrato app-BD',
        },
        {
            'name': 'Oracle Live SQL',
            'logo': 'oracle_livesql.png',
            'note': 'Ops',
        },
        {
            'name': 'draw.io',
            'logo': 'drawio.png',
            'note': 'Flujo',
        },
    ],
    13: [
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'Caso real',
        },
        {
            'name': 'draw.io',
            'logo': 'drawio.png',
            'note': 'Leccion',
        },
        {
            'name': 'DB Fiddle',
            'logo': 'dbfiddle.png',
            'note': 'Opcional SQL',
        },
    ],
    15: [
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'Informe final',
        },
        {
            'name': 'draw.io',
            'logo': 'drawio.png',
            'note': 'ER final',
        },
        {
            'name': 'Oracle Live SQL',
            'logo': 'oracle_livesql.png',
            'note': 'Demo SQL',
        },
    ],
}

TALLER_BLOQUE = {
    1: {
        'contexto': [
            '@@Por qué importa al PI VetCare:@@ sin ER/alcance no hay base para procs ni seguridad.',
            'Hoy cierras dominio + entidades mínimas + reglas de negocio propias.',
            'El DDL demo (Codigo/) es semilla; tu ER manda.',
        ],
        'objetivo': 'Arrancar VetCare: ficha + ER borrador + entidades/reglas.',
        'criterios': [
            'Proyecto nombrado y registrado.',
            'ER PNG con entidades mínimas.',
            '3 reglas de negocio propias.',
            'Alcance SI/NO 5-8 lineas.',
            'Entrega domingo 23:59.',
        ],
        'escenario': [
            'Dominio: clínica veterinaria VetCare.',
            'Herramientas: draw.io + DB Fiddle.',
            'Reutilizar nombres del enunciado PI.',
        ],
        'pistas': [
            '□ Hay PK/FK visibles en el ER?',
            '□ Mascota inactiva / stock aparecen como regla?',
            '□ El alcance evita scope infinito?',
        ],
    },
    2: {
        'contexto': [
            '@@Por qué importa al PI:@@ roles son evidencia de administración.',
            'Least privilege evita que Recepción borre historial.',
            'Autónoma: documentar matriz aunque el playground no persista usuarios.',
        ],
        'objetivo': 'Plan de roles/privilegios VetCare (>=4 roles).',
        'criterios': [
            '>=4 roles.',
            'Matriz privilegio x objeto.',
            'Justificación least privilege.',
            '1 página política.',
            'Domingo 23:59.',
        ],
        'escenario': [
            'Roles: ADMIN_BD, RECEPCION, VETERINARIO, AUDITOR.',
            'Live SQL / Docs.',
        ],
        'pistas': [
            '□ Recepción con DELETE historial? (no)',
            '□ Auditor solo SELECT?',
            '□ DDL separado?',
        ],
    },
    3: {
        'contexto': [
            '@@Por qué importa al PI:@@ la regla vive en un proc reutilizable.',
            'La app futura llama al proc.',
        ],
        'objetivo': '>=1 procedimiento con validación + 2 pruebas.',
        'criterios': [
            'Proc en Live SQL.',
            'Validación negocio.',
            'Prueba OK + error.',
            'Contrato documentado.',
        ],
        'escenario': [
            'Tu DDL de VetCare.',
            'Validación típica: mascota activa.',
        ],
        'pistas': [
            '□ Error controlado?',
            '□ Captura/enlace?',
            '□ Firma clara?',
        ],
    },
    4: {
        'contexto': [
            '@@Por qué importa al PI:@@ integridad + RAA1.',
            'Trigger evita inconsistencias silenciosas.',
        ],
        'objetivo': '>=1 funcion + >=1 trigger + plan backup.',
        'criterios': [
            'Funcion util.',
            'Trigger auditoria/stock.',
            'Plan backup 1 pag.',
            'Checklist PI.',
        ],
        'escenario': [
            'Ej: fn_precio_consulta; trg_audit_cancelacion.',
        ],
        'pistas': [
            '□ Trigger con propósito?',
            '□ Backup con restore?',
            '□ Evidencia SQL?',
        ],
    },
    6: {
        'contexto': [
            '@@Por qué importa al PI:@@ optimizar el propio DDL.',
            'Reescribir y justificar, no solo decir lento.',
        ],
        'objetivo': 'Pareja consultas antes/después + justificación.',
        'criterios': [
            'Consulta real PI.',
            'Version después.',
            '3 cambios.',
            'Archivos SQL.',
        ],
        'escenario': [
            'Citas del dia / historial mascota.',
        ],
        'pistas': [
            '□ Sin SELECT *?',
            '□ Filtro temprano?',
            '□ Cuello de botella nombrado?',
        ],
    },
    7: {
        'contexto': [
            '@@Por qué importa al PI:@@ indices aceleran lecturas frecuentes.',
            'Sobre-indexar castiga escrituras.',
        ],
        'objetivo': '>=2 indices justificados en tablas calientes.',
        'criterios': [
            '2 CREATE INDEX.',
            'Justificación.',
            'Riesgo sobre-indexar.',
            'Diagrama opcional.',
        ],
        'escenario': [
            'Candidatos: Cita(fecha), Mascota(id_dueño).',
        ],
        'pistas': [
            '□ Nombre legible?',
            '□ Atado a consulta?',
            '□ Indexar todo? (no)',
        ],
    },
    8: {
        'contexto': [
            '@@Por qué importa al PI:@@ factura+stock atomicos.',
            'ROLLBACK ante stock insuficiente.',
        ],
        'objetivo': 'Transaccion factura+stock + checklist tuning.',
        'criterios': [
            'Transaccion completa.',
            'Prueba ROLLBACK.',
            'Checklist tuning.',
            'Sección informe.',
        ],
        'escenario': [
            'BEGIN/COMMIT/ROLLBACK del playground.',
        ],
        'pistas': [
            '□ Prueba de fallo?',
            '□ Locks/indices en checklist?',
            '□ En informe?',
        ],
    },
    10: {
        'contexto': [
            '@@Por qué importa al PI:@@ doble reserva y stock negativo.',
            'Autónoma: escenarios + mitigacion SQL.',
        ],
        'objetivo': '2 escenarios concurrencia T1/T2 + mitigacion.',
        'criterios': [
            'Doble reserva.',
            'Doble stock.',
            'Mitigacion SQL.',
            'Sección informe.',
            'Domingo 23:59.',
        ],
        'escenario': [
            'Narrar T1/T2 sobre Cita/Insumo.',
        ],
        'pistas': [
            '□ Tiempos claros?',
            '□ Mitigacion SQL concreta?',
            '□ Conecta con procs?',
        ],
    },
    11: {
        'contexto': [
            '@@Por qué importa al PI:@@ checkpoint vs rúbrica.',
            'Demo + gaps con responsable.',
        ],
        'objetivo': 'Checklist avance + demo 3-5 min.',
        'criterios': [
            'Checklist evidenciada.',
            'Demo ER+proc+trigger.',
            'Gaps.',
            'Avance subido si aplica.',
        ],
        'escenario': [
            'Evidencias: ER, DDL, roles, procs, fn, triggers, opt.',
        ],
        'pistas': [
            '□ Si con evidencia?',
            '□ Gaps con dueño?',
            '□ Demo <=5 min?',
        ],
    },
    12: {
        'contexto': [
            '@@Por qué importa al PI:@@ app llama contrato, no SQL suelto.',
            'Preparar sustentacion.',
        ],
        'objetivo': 'Contrato >=3 ops + outline pitch 5-8 min.',
        'criterios': [
            'Contrato 3 ops.',
            'Parametros/errores/ejemplo.',
            'Outline pitch.',
            'Borrador final.',
        ],
        'escenario': [
            'Plantilla sp_agendar_cita / consulta / facturar.',
        ],
        'pistas': [
            '□ >=3 ops?',
            '□ Errores esperados?',
            '□ Outline completo?',
        ],
    },
    13: {
        'contexto': [
            '@@Por qué importa al PI:@@ lecciónes accionables.',
            'Autónoma: 1 caso -> 3 mejoras.',
        ],
        'objetivo': 'Caso real -> 3 mejoras VetCare.',
        'criterios': [
            'Caso elegido.',
            'Resumen.',
            '3 mejoras.',
            'Informe.',
            'Domingo 23:59.',
        ],
        'escenario': [
            'Plantilla: contexto->fallo->lección->cambio.',
        ],
        'pistas': [
            '□ Mejoras accionables?',
            '□ Conectan al PI?',
            '□ Evidencia de lectura?',
        ],
    },
    15: {
        'contexto': [
            '@@Por qué importa al PI:@@ cierre segun rúbrica 20% Corte 3.',
            'No confundir con Parcial 3 (Clase 14).',
        ],
        'objetivo': 'Paquete final + sustentacion 5-8 min.',
        'criterios': [
            'ZIP/PDF en ExamLab.',
            'Sustentacion 5-8 min.',
            'Autoevaluacion.',
            'Cierre.',
        ],
        'escenario': [
            'Checklist empaquetado del enunciado PI.',
        ],
        'pistas': [
            '□ Falta evidencia?',
            '□ Cubre todos los bloques (y todos hablan, si hay equipo)?',
            '□ PI != P3?',
        ],
    },
}

SOLUCION = {
    1: {
        'titulo': 'Solución Taller Clase 1 — Arranque VetCare',
        'resumen': 'ER minimo Dueño-Mascota-Cita + 3 reglas + alcance.',
        'pasos': [
            'Trabajo individual por defecto: nombra tu proyecto VetCare-<tu apellido> y registralo para identificarlo en todas las entregas del semestre. Si el docente autoriza equipo de 2 o 3, el artefacto puede ser compartido pero la entrega en ExamLab sigue siendo individual.',
            'Listar las entidades minimas del dominio: Dueño (persona que trae la mascota), Mascota (paciente), Veterinario (quien atiende), Cita (agenda de una atencion). Consulta, Insumo y DetalleFactura se agregan en clases posteriores.',
            'Redactar como reglas de negocio explicitas (no solo mencionarlas): "una mascota con activa=N no puede tener una cita nueva", "el stock de un insumo nunca puede quedar en negativo", "toda cancelacion de cita queda registrada con usuario y fecha".',
            'Dibujar el ER borrador marcando cardinalidad en cada relacion (Dueño 1-N Mascota, Mascota 1-N Cita) y exportarlo como PNG legible, no un boceto a mano ilegible.',
            'Escribir el alcance en dos listas explicitas: que SI cubre el PI este semestre (agenda, facturacion basica, roles) y que NO cubre (ej. pagos en linea, historial clinico completo) para evitar scope creep en clases futuras.',
        ],
        'ejemplo': [
            'DDL: Kit docente/Clase 1/Codigo/01_arranque_vetcare.sql',
            'ER: Dueño 1-N Mascota; Mascota 1-N Cita.',
        ],
        'rubrica': [
            'Registro del proyecto (1)',
            'ER (3)',
            'Reglas (2)',
            'Alcance (2)',
            'Entrega (2)',
        ],
        'errores': [
            'ER genérico.',
            'Sin FK.',
            'Scope infinito.',
        ],
    },
    2: {
        'titulo': 'Solución Taller Clase 2 — Roles VetCare',
        'resumen': '4 roles + matriz least privilege.',
        'pasos': [
            'Definir los 4 roles minimos: ADMIN_BD (DDL + gestion de roles), RECEPCION (opera citas y datos de contacto), VETERINARIO (registra consultas), AUDITOR (solo lectura sobre todo lo sensible).',
            'Construir la matriz rol x objeto x privilegio: por cada rol, listar exactamente que tabla y que operacion (SELECT/INSERT/UPDATE/DELETE/EXECUTE) tiene permitida — no "acceso general", sino privilegio por objeto.',
            'RECEPCION puede SELECT/INSERT/UPDATE sobre cita y SELECT sobre mascota/dueno, pero NUNCA DELETE sobre historial clinico ni sobre consulta — solo un veterinario o admin puede borrar ese tipo de registro.',
            'AUDITOR recibe unicamente SELECT sobre las tablas sensibles (cita, consulta, factura); ningun privilegio de escritura, ni siquiera sobre datos "poco importantes", porque su funcion es verificar, no operar.',
            'Redactar la politica de altas/bajas de usuarios en media pagina: quien autoriza crear un usuario nuevo, que rol se le asigna por defecto, y que pasa con sus privilegios el dia que deja de trabajar en la clinica (revocacion inmediata, no "despues").',
        ],
        'ejemplo': [
            'Codigo/02_roles_vetcare.sql',
        ],
        'rubrica': [
            '4 roles (2)',
            'Matriz (3)',
            'Least privilege (3)',
            'Política (2)',
        ],
        'errores': [
            'Todos DBA.',
            'Sin justificar.',
        ],
    },
    3: {
        'titulo': 'Solución Taller Clase 3 — Procedimientos',
        'resumen': 'sp_agendar_cita con validación mascota activa.',
        'pasos': [
            'Crear sp_agendar_cita con parametros IN (id_cita, id_mascota, fecha) y un parametro OUT (p_msg) para devolver el resultado a quien lo llame.',
            "Antes de insertar, hacer SELECT activa FROM mascota WHERE id_mascota = p_id_mascota; si activa <> 'S', asignar p_msg := 'ERROR: mascota inactiva; no se agenda' y salir con RETURN sin tocar la tabla cita.",
            'Si la validacion pasa, ejecutar el INSERT INTO cita y confirmar con COMMIT; asignar p_msg := \'OK: cita agendada\' para que quien llamo el proc sepa que la operacion tuvo exito.',
            'Ejecutar dos pruebas obligatorias: (1) caso OK con una mascota activa=S — debe insertar y devolver mensaje de exito; (2) caso error con una mascota activa=N o inexistente — debe rechazar sin insertar nada y devolver el mensaje de error correspondiente (usar EXCEPTION WHEN NO_DATA_FOUND para el caso de mascota inexistente).',
            'Documentar la firma del proc como si fuera el contrato que usara la futura app: nombre, cada parametro con su tipo y direccion (IN/OUT), y el listado de mensajes de p_msg posibles — esto es exactamente lo que se reutiliza en el contrato de integracion de Clase 12.',
        ],
        'ejemplo': [
            'Codigo/03_procs_vetcare.sql',
        ],
        'rubrica': [
            'Proc (3)',
            'Validación (3)',
            'Pruebas (2)',
            'Contrato (2)',
        ],
        'errores': [
            'Sin validación.',
            'Solo captura.',
        ],
    },
    4: {
        'titulo': 'Solución Taller Clase 4 — Fn/trigger/backup',
        'resumen': 'Funcion + trigger + plan respaldo.',
        'pasos': [
            'Crear fn_precio_base(p_especie) que RETURN un valor NUMBER util al PI (ej. tarifa base segun especie), verificable con SELECT fn_precio_base(\'CANINO\') FROM dual — una funcion se prueba dentro de un SELECT, no con CALL.',
            'Crear trg_audit_cancelacion_cita (AFTER UPDATE ON cita WHEN estado cambia a CANCELADA) que inserte una fila en una tabla de auditoria con usuario, fecha y el id de la cita cancelada — sin que la app tenga que acordarse de registrar nada explicitamente.',
            'Redactar el plan de respaldo con las 3 variables que lo hacen verificable: frecuencia (ej. diaria a las 2am), retencion (ej. 7 copias diarias + 4 semanales), y prueba de restore (ej. una vez al mes se restaura en un ambiente de prueba y se valida que los datos coinciden).',
            'Actualizar el checklist del PI marcando explicitamente: funcion creada y probada, trigger creado y disparado al menos una vez en pruebas, plan de respaldo redactado con las 3 variables — no basta con "en progreso" sin evidencia.',
        ],
        'ejemplo': [
            'Codigo/04_func_trigger_backup.sql',
        ],
        'rubrica': [
            'Funcion (2)',
            'Trigger (3)',
            'Backup (3)',
            'Checklist (2)',
        ],
        'errores': [
            'Trigger vacio.',
            'Backup sin restore.',
        ],
    },
    6: {
        'titulo': 'Solución Taller Clase 6 — Optimización',
        'resumen': 'Pareja antes/después VetCare.',
        'pasos': [
            'Elegir una consulta real y frecuente del PI (ej. listar las citas del dia con nombre de mascota y dueno) — no un ejemplo inventado sin uso real.',
            'Escribir la version "antes" tal como la escribiria alguien sin entrenamiento: SELECT * ... con JOIN sin filtro de fecha, trayendo todo el historico.',
            'Reescribir la version "despues": proyectar solo las columnas necesarias, filtrar por fecha_hora >= hoy ANTES del JOIN cuando el motor lo permita, y evitar funciones sobre la columna de fecha en el WHERE.',
            'Justificar por escrito minimo 3 cambios concretos (ej. "se elimino SELECT * porque solo se usan 4 columnas", "el filtro de fecha reduce el conjunto antes del JOIN", "se evito CAST sobre fecha_hora en el WHERE porque bloqueaba el uso de indice").',
            'Guardar ambas versiones como 06_opt_antes.sql y 06_opt_despues.sql en tu carpeta del PI, y si el playground lo permite, adjuntar el resultado de EXPLAIN de cada una como evidencia de la mejora.',
        ],
        'ejemplo': [
            'Codigo/06_opt_consultas.sql',
        ],
        'rubrica': [
            'Consulta PI (2)',
            'Pareja (3)',
            'Justificación (3)',
            'Archivos (2)',
        ],
        'errores': [
            'Caso genérico.',
            'Sin diferencia real.',
        ],
    },
    7: {
        'titulo': 'Solución Taller Clase 7 — Indices',
        'resumen': '2 indices justificados.',
        'pasos': [
            'Identificar 2 consultas frecuentes del PI que filtran o unen por una columna especifica (ej. "citas de un dia" filtra por fecha_hora; "historial de un dueno" filtra por id_dueno via mascota).',
            'Crear los indices correspondientes, ej. CREATE INDEX idx_cita_fecha ON cita(fecha_hora); CREATE INDEX idx_mascota_dueno ON mascota(id_dueno) — con nombres que dejen claro que tabla/columna indexan.',
            'Construir una tabla de dos columnas: consulta frecuente -> indice que la acelera, explicando en una frase por que esa columna tiene suficiente cardinalidad para justificar el indice.',
            'Explicar por escrito el riesgo de sobre-indexar: cada indice adicional ralentiza INSERT/UPDATE/DELETE sobre esa tabla, asi que un indice sin una consulta real que lo use es costo puro sin beneficio — por eso el entregable exige justificar cada indice con su consulta.',
        ],
        'ejemplo': [
            'Codigo/07_indices_vetcare.sql',
        ],
        'rubrica': [
            'Indices (4)',
            'Justificación (3)',
            'Riesgo (2)',
            'Evidencia (1)',
        ],
        'errores': [
            'Sin consulta.',
            'Indexar todo.',
        ],
    },
    8: {
        'titulo': 'Solución Taller Clase 8 — Transacciones',
        'resumen': 'Factura+stock con ROLLBACK.',
        'pasos': [
            'Implementar un procedimiento (o bloque transaccional explicito) que inserte la factura, inserte el detalle_factura y descuente el stock del insumo en una sola transaccion: BEGIN...INSERT...INSERT...UPDATE stock...COMMIT.',
            'Forzar deliberadamente un caso de fallo (ej. intentar descontar mas stock del disponible) y verificar que el ROLLBACK deshace TODO: ni la factura ni el detalle quedan registrados a medias — esa es la prueba real de atomicidad, no solo el caso feliz.',
            'Completar el checklist de tuning: estadisticas actualizadas, existencia de indice sobre las columnas usadas en el JOIN/WHERE de esta transaccion, y verificar que la transaccion no queda abierta mas tiempo del necesario (sin operaciones manuales del usuario en medio del BEGIN/COMMIT).',
            'Actualizar el informe del PI con la seccion de transacciones: que operacion se protegio, que prueba de fallo se ejecuto, y que se verifico despues del ROLLBACK (que el stock e historial quedaron exactamente como antes del intento fallido).',
        ],
        'ejemplo': [
            'Codigo/08_transacciones_vetcare.sql',
        ],
        'rubrica': [
            'Transaccion (4)',
            'ROLLBACK (3)',
            'Checklist (2)',
            'Informe (1)',
        ],
        'errores': [
            'Sin prueba fallo.',
            'Updates sueltos.',
        ],
    },
    10: {
        'titulo': 'Solución Taller Clase 10 — Concurrencia',
        'resumen': '2 escenarios + mitigacion.',
        'pasos': [
            'Narrar el escenario de doble reserva con linea de tiempo explicita: T1 lee la franja como libre en el segundo 0, T2 lee la misma franja como libre en el segundo 1 (antes de que T1 confirme), ambas insertan y quedan dos citas para el mismo veterinario/franja.',
            'Narrar el escenario de doble descuento de stock con la misma logica T1/T2: dos facturas leen el mismo stock disponible antes de que ninguna confirme su UPDATE, y el stock final queda incorrecto (mayor de lo que debería haberse descontado, o incluso negativo).',
            'Proponer la mitigacion SQL concreta para cada escenario: UNIQUE(id_veterinario, fecha_hora) para que el segundo INSERT de cita falle automaticamente; y para el stock, un UPDATE con condicion (UPDATE insumo SET stock = stock - x WHERE id_insumo = y AND stock >= x) que falla/no afecta filas si ya no alcanza, en vez de restar a ciegas.',
            'Agregar la seccion de concurrencia al informe del PI explicando, en lenguaje simple, por que un simple "usar transacciones" no basta sin la restriccion UNIQUE o la condicion en el UPDATE, y que mecanismo especifico elegiste para VetCare.',
        ],
        'ejemplo': [
            'Codigo/10_concurrencia_vetcare.sql',
        ],
        'rubrica': [
            'Cita (3)',
            'Stock (3)',
            'Mitigacion (3)',
            'Informe (1)',
        ],
        'errores': [
            'Sin T1/T2.',
            'Mitigacion vaga.',
        ],
    },
    11: {
        'titulo': 'Solución Taller Clase 11 — Checkpoint',
        'resumen': 'Checklist + demo.',
        'pasos': [
            'Completar el checklist marcando SI/NO/PARCIAL en cada evidencia exigida: ER actualizado, DDL ejecutable, roles definidos, minimo 2 procedimientos, minimo 1 funcion, minimo 2 triggers, minimo 1 optimizacion documentada.',
            'Preparar y ejecutar una demo de 3-5 minutos que muestre en vivo: el ER, un procedimiento ejecutandose con un caso real, y un trigger disparandose (ej. cancelar una cita y mostrar la fila de auditoria creada).',
            'Listar explicitamente los gaps (huecos) que quedan pendientes, cada uno con un responsable con nombre (tu mismo si trabajas solo; repartido si hay equipo autorizado) — no dejar gaps sin dueño.',
            'Subir el avance intermedio (enlace o ZIP con DDL + procs + ER) a ExamLab si el docente lo solicita, como respaldo verificable del progreso a mitad de corte.',
        ],
        'ejemplo': [
            'Codigo/11_checklist_seed.sql',
        ],
        'rubrica': [
            'Checklist (4)',
            'Demo (3)',
            'Gaps (2)',
            'Paquete (1)',
        ],
        'errores': [
            'Si sin enlaces.',
            'Demo sin artefactos.',
        ],
    },
    12: {
        'titulo': 'Solución Taller Clase 12 — Contrato + pitch',
        'resumen': 'Contrato 3 ops + outline.',
        'pasos': [
            'Redactar el contrato de al menos 3 operaciones (ej. agendar_cita, registrar_consulta, facturar) especificando nombre del proc, cada parametro con tipo y direccion IN/OUT, y que retorna en caso de exito.',
            'Para cada operacion, documentar los posibles errores de negocio (ej. "mascota inactiva", "stock insuficiente") con el mensaje exacto que devuelve el proc, y un ejemplo de llamada con valores concretos.',
            'Construir el outline de la sustentacion de 5-8 minutos con la secuencia problema -> modelo -> seguridad -> procs/triggers -> optimizacion -> demo en vivo, dejando claro que dices en cada seccion (y quien la presenta, si hay equipo autorizado: todos deben hablar).',
            'Empaquetar el borrador de entrega final (DDL, procs, contrato, outline) en una carpeta o ZIP organizado, listo para completarse en las Clases 13-15 sin tener que reconstruirlo desde cero.',
        ],
        'ejemplo': [
            'Codigo/12_contrato_ops.sql',
        ],
        'rubrica': [
            'Contratos (4)',
            'Errores (2)',
            'Outline (3)',
            'Paquete (1)',
        ],
        'errores': [
            'Sin errores.',
            'Outline logos.',
        ],
    },
    13: {
        'titulo': 'Solución Taller Clase 13 — Casos reales',
        'resumen': '1 caso -> 3 mejoras.',
        'pasos': [
            'Elegir uno de los 3 casos trabajados en teoria (falta de backup, indices mal disenados, o inyeccion SQL) segun el que mas riesgo represente para el estado actual de tu VetCare.',
            'Resumir el caso en media pagina con la estructura contexto -> fallo -> causa raiz tecnica (no "mala suerte") -> leccion general.',
            'Proponer 3 mejoras concretas y verificables aplicadas al VetCare propio (ej. "agregar prueba de restore mensual", "revisar y eliminar 2 indices sin uso real", "confirmar que todos los procs usan parametros tipados, ninguno concatena texto de usuario").',
            'Actualizar el informe del PI incorporando estas lecciones como una seccion nueva, citando en que clase/entregable anterior se relaciona cada mejora (Clase 4 para backup, Clase 7 para indices, Clase 3/12 para inyeccion SQL).',
        ],
        'ejemplo': [
            'Plantilla contexto->fallo->lección->cambio VetCare.',
        ],
        'rubrica': [
            'Caso (2)',
            'Resumen (2)',
            'Mejoras (4)',
            'Informe (2)',
        ],
        'errores': [
            'Mejoras genericas.',
            'Sin conexión PI.',
        ],
    },
    15: {
        'titulo': 'Solución Taller Clase 15 — Entrega final',
        'resumen': 'Checklist empaquetado + pitch.',
        'pasos': [
            'Verificar el ZIP/paquete final linea por linea contra la rubrica de 100 pts (ER, DDL, roles, procs, funciones/triggers, optimizacion, indices, transacciones, concurrencia, contrato de integracion, informe) antes de subirlo, no despues.',
            'Sustentar 5-8 minutos siguiendo el outline preparado en Clase 12, con evidencia en vivo (no solo diapositivas) de al menos un procedimiento y un trigger ejecutandose.',
            'Completar la autoevaluacion de tu propio trabajo respondiendo con honestidad que harias distinto si empezaras de nuevo (si hubo equipo autorizado, agrega una linea por integrante) — esto pesa en la nota y demuestra criterio, no solo ejecucion.',
            'Cerrar formalmente el curso confirmando que la entrega quedo registrada en ExamLab dentro del plazo, con el enlace o archivo accesible para el docente.',
        ],
        'ejemplo': [
            'Estructura: ER, DDL, roles, procs, fn/triggers, opt, indices, tx, concurrencia, contrato, informe.',
        ],
        'rubrica': [
            'Paquete (4)',
            'Sustentacion (3)',
            'Autoevaluacion (2)',
            'Rubrica (1)',
        ],
        'errores': [
            'Faltan evidencias.',
            'Confundir con P3.',
        ],
    },
}
