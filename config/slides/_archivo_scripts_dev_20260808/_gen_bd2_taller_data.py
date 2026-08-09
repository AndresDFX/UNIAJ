# -*- coding: utf-8 -*-
from pathlib import Path

def emit(obj, indent=0):
    sp = " " * indent
    if isinstance(obj, dict):
        lines = ["{\n"]
        for k, v in obj.items():
            lines.append(f"{sp}    {k!r}: {emit(v, indent+4)},\n")
        lines.append(f"{sp}}}")
        return "".join(lines)
    if isinstance(obj, list):
        lines = ["[\n"]
        for item in obj:
            lines.append(f"{sp}    {emit(item, indent+4)},\n")
        lines.append(f"{sp}]")
        return "".join(lines)
    return repr(obj)

H = {
1: [("draw.io","drawio.png","ER VetCare"),("DB Fiddle","dbfiddle.png","DDL demo"),("Oracle Live SQL","oracle_livesql.png","Playground"),("Google Docs","google_docs.png","Ficha equipo")],
2: [("Oracle Live SQL","oracle_livesql.png","GRANT/roles"),("DB Fiddle","dbfiddle.png","SQL demo"),("Google Docs","google_docs.png","Matriz roles")],
3: [("Oracle Live SQL","oracle_livesql.png","Procedimientos"),("DB Fiddle","dbfiddle.png","Pruebas"),("Google Docs","google_docs.png","Contrato proc")],
4: [("Oracle Live SQL","oracle_livesql.png","Fn/trigger"),("DB Fiddle","dbfiddle.png","Pruebas"),("Google Docs","google_docs.png","Plan backup")],
6: [("DB Fiddle","dbfiddle.png","Antes/despues"),("SQLTest.online","sqltest.png","Multi-motor"),("Google Docs","google_docs.png","Justificacion")],
7: [("DB Fiddle","dbfiddle.png","CREATE INDEX"),("draw.io","drawio.png","Tabla caliente"),("Google Docs","google_docs.png","Justificacion")],
8: [("Oracle Live SQL","oracle_livesql.png","Transacciones"),("DB Fiddle","dbfiddle.png","ROLLBACK"),("Google Docs","google_docs.png","Checklist tuning")],
10:[("Google Docs","google_docs.png","Escenarios T1/T2"),("Oracle Live SQL","oracle_livesql.png","Demo SQL"),("DB Fiddle","dbfiddle.png","Pruebas")],
11:[("Oracle Live SQL","oracle_livesql.png","Demo procs"),("draw.io","drawio.png","ER"),("DB Fiddle","dbfiddle.png","DDL"),("Google Docs","google_docs.png","Checklist")],
12:[("Google Docs","google_docs.png","Contrato app-BD"),("Oracle Live SQL","oracle_livesql.png","Ops"),("draw.io","drawio.png","Flujo")],
13:[("Google Docs","google_docs.png","Caso real"),("draw.io","drawio.png","Leccion"),("DB Fiddle","dbfiddle.png","Opcional SQL")],
15:[("Google Docs","google_docs.png","Informe final"),("draw.io","drawio.png","ER final"),("Oracle Live SQL","oracle_livesql.png","Demo SQL")],
}
HERRAMIENTAS_DIA = {n:[{"name":a,"logo":b,"note":c} for a,b,c in items] for n,items in H.items()}

# Compact META: n -> (objetivo, contexto_list, criterios, escenario, pistas, sol_titulo, sol_resumen, sol_pasos, sol_ej, sol_rub, sol_err)
META = {
1: ("Arrancar VetCare: ficha + ER borrador + entidades/reglas.",
    ["@@Por que importa al PI VetCare:@@ sin ER/alcance no hay base para procs ni seguridad.",
     "Hoy cierran dominio + entidades minimas + reglas de negocio del equipo.",
     "El DDL demo (Codigo/) es semilla; el ER del equipo manda."],
    ["Equipo 2-3 nombrado.","ER PNG con entidades minimas.","3 reglas de negocio propias.","Alcance SI/NO 5-8 lineas.","Entrega domingo 23:59."],
    ["Dominio: clinica veterinaria VetCare.","Herramientas: draw.io + DB Fiddle.","Reutilizar nombres del enunciado PI."],
    ["Hay PK/FK visibles en el ER?","Mascota inactiva / stock aparecen como regla?","El alcance evita scope infinito?"],
    "Solucion Taller Clase 1 — Arranque VetCare","ER minimo Dueno-Mascota-Cita + 3 reglas + alcance.",
    ["Equipo 2-3; nombre VetCare-<apellido>.","Entidades: Dueno, Mascota, Veterinario, Cita.","Reglas: mascota inactiva no cita; stock>=0; auditoria.","ER PNG.","Alcance SI/NO."],
    ["DDL: Kit docente/Clase 1/Codigo/01_arranque_vetcare.sql","ER: Dueno 1-N Mascota; Mascota 1-N Cita."],
    ["Equipo (1)","ER (3)","Reglas (2)","Alcance (2)","Entrega (2)"],
    ["ER generico.","Sin FK.","Scope infinito."]),
2: ("Plan de roles/privilegios VetCare (>=4 roles).",
    ["@@Por que importa al PI:@@ roles son evidencia de administracion.",
     "Least privilege evita que Recepcion borre historial.",
     "Autonoma: documentar matriz aunque el playground no persista usuarios."],
    [">=4 roles.","Matriz privilegio x objeto.","Justificacion least privilege.","1 pagina politica.","Domingo 23:59."],
    ["Roles: ADMIN_BD, RECEPCION, VETERINARIO, AUDITOR.","Live SQL / Docs."],
    ["Recepcion con DELETE historial? (no)","Auditor solo SELECT?","DDL separado?"],
    "Solucion Taller Clase 2 — Roles VetCare","4 roles + matriz least privilege.",
    ["Definir 4 roles.","Matriz privilegios.","Recepcion: citas; no DELETE historial.","Auditor SELECT.","Politica altas/bajas."],
    ["Codigo/02_roles_vetcare.sql"],
    ["4 roles (2)","Matriz (3)","Least privilege (3)","Politica (2)"],
    ["Todos DBA.","Sin justificar."]),
3: (">=1 procedimiento con validacion + 2 pruebas.",
    ["@@Por que importa al PI:@@ la regla vive en un proc reutilizable.",
     "La app futura llama al proc."],
    ["Proc en Live SQL.","Validacion negocio.","Prueba OK + error.","Contrato documentado."],
    ["DDL VetCare del equipo.","Validacion tipica: mascota activa."],
    ["Error controlado?","Captura/enlace?","Firma clara?"],
    "Solucion Taller Clase 3 — Procedimientos","sp_agendar_cita con validacion mascota activa.",
    ["Crear proc.","Validar activa='S'.","Insertar o error.","Probar OK+error.","Documentar firma."],
    ["Codigo/03_procs_vetcare.sql"],
    ["Proc (3)","Validacion (3)","Pruebas (2)","Contrato (2)"],
    ["Sin validacion.","Solo captura."]),
4: (">=1 funcion + >=1 trigger + plan backup.",
    ["@@Por que importa al PI:@@ integridad + RAA1.",
     "Trigger evita inconsistencias silenciosas."],
    ["Funcion util.","Trigger auditoria/stock.","Plan backup 1 pag.","Checklist PI."],
    ["Ej: fn_precio_consulta; trg_audit_cancelacion."],
    ["Trigger con proposito?","Backup con restore?","Evidencia SQL?"],
    "Solucion Taller Clase 4 — Fn/trigger/backup","Funcion + trigger + plan respaldo.",
    ["fn util.","trigger auditoria/stock.","Plan frecuencia/retencion/restore.","Checklist."],
    ["Codigo/04_func_trigger_backup.sql"],
    ["Funcion (2)","Trigger (3)","Backup (3)","Checklist (2)"],
    ["Trigger vacio.","Backup sin restore."]),
6: ("Pareja consultas antes/despues + justificacion.",
    ["@@Por que importa al PI:@@ optimizar el propio DDL.",
     "Reescribir y justificar, no solo decir lento."],
    ["Consulta real PI.","Version despues.","3 cambios.","Archivos SQL."],
    ["Citas del dia / historial mascota."],
    ["Sin SELECT *?","Filtro temprano?","Cuello de botella nombrado?"],
    "Solucion Taller Clase 6 — Optimizacion","Pareja antes/despues VetCare.",
    ["Elegir consulta.","Escribir antes.","Reescribir despues.","Justificar 3 cambios.","Guardar SQL."],
    ["Codigo/06_opt_consultas.sql"],
    ["Consulta PI (2)","Pareja (3)","Justificacion (3)","Archivos (2)"],
    ["Caso generico.","Sin diferencia real."]),
7: (">=2 indices justificados en tablas calientes.",
    ["@@Por que importa al PI:@@ indices aceleran lecturas frecuentes.",
     "Sobre-indexar castiga escrituras."],
    ["2 CREATE INDEX.","Justificacion.","Riesgo sobre-indexar.","Diagrama opcional."],
    ["Candidatos: Cita(fecha), Mascota(id_dueno)."],
    ["Nombre legible?","Atado a consulta?","Indexar todo? (no)"],
    "Solucion Taller Clase 7 — Indices","2 indices justificados.",
    ["2 consultas frecuentes.","CREATE INDEX ejemplos.","Tabla consulta->indice.","Riesgo sobre-indexar."],
    ["Codigo/07_indices_vetcare.sql"],
    ["Indices (4)","Justificacion (3)","Riesgo (2)","Evidencia (1)"],
    ["Sin consulta.","Indexar todo."]),
8: ("Transaccion factura+stock + checklist tuning.",
    ["@@Por que importa al PI:@@ factura+stock atomicos.",
     "ROLLBACK ante stock insuficiente."],
    ["Transaccion completa.","Prueba ROLLBACK.","Checklist tuning.","Seccion informe."],
    ["BEGIN/COMMIT/ROLLBACK del playground."],
    ["Prueba de fallo?","Locks/indices en checklist?","En informe?"],
    "Solucion Taller Clase 8 — Transacciones","Factura+stock con ROLLBACK.",
    ["Bloque/proc atomico.","Forzar fallo->ROLLBACK.","Checklist tuning.","Informe."],
    ["Codigo/08_transacciones_vetcare.sql"],
    ["Transaccion (4)","ROLLBACK (3)","Checklist (2)","Informe (1)"],
    ["Sin prueba fallo.","Updates sueltos."]),
10:("2 escenarios concurrencia T1/T2 + mitigacion.",
    ["@@Por que importa al PI:@@ doble reserva y stock negativo.",
     "Autonoma: escenarios + mitigacion SQL."],
    ["Doble reserva.","Doble stock.","Mitigacion SQL.","Seccion informe.","Domingo 23:59."],
    ["Narrar T1/T2 sobre Cita/Insumo."],
    ["Tiempos claros?","Mitigacion SQL concreta?","Conecta con procs?"],
    "Solucion Taller Clase 10 — Concurrencia","2 escenarios + mitigacion.",
    ["Narrar doble reserva.","Narrar doble stock.","UNIQUE/tx/procs.","Informe."],
    ["Codigo/10_concurrencia_vetcare.sql"],
    ["Cita (3)","Stock (3)","Mitigacion (3)","Informe (1)"],
    ["Sin T1/T2.","Mitigacion vaga."]),
11:("Checklist avance + demo 3-5 min.",
    ["@@Por que importa al PI:@@ checkpoint vs rubrica.",
     "Demo + gaps con responsable."],
    ["Checklist evidenciada.","Demo ER+proc+trigger.","Gaps.","Avance subido si aplica."],
    ["Evidencias: ER, DDL, roles, procs, fn, triggers, opt."],
    ["Si con evidencia?","Gaps con dueno?","Demo <=5 min?"],
    "Solucion Taller Clase 11 — Checkpoint","Checklist + demo.",
    ["Completar checklist.","Demo 3-5 min.","Gaps.","Subir avance."],
    ["Codigo/11_checklist_seed.sql"],
    ["Checklist (4)","Demo (3)","Gaps (2)","Paquete (1)"],
    ["Si sin enlaces.","Demo sin artefactos."]),
12:("Contrato >=3 ops + outline pitch 5-8 min.",
    ["@@Por que importa al PI:@@ app llama contrato, no SQL suelto.",
     "Preparar sustentacion."],
    ["Contrato 3 ops.","Parametros/errores/ejemplo.","Outline pitch.","Borrador final."],
    ["Plantilla sp_agendar_cita / consulta / facturar."],
    [">=3 ops?","Errores esperados?","Outline completo?"],
    "Solucion Taller Clase 12 — Contrato + pitch","Contrato 3 ops + outline.",
    ["Contrato 3 ops.","Errores+ejemplo.","Outline 5-8 min.","Empaquetar."],
    ["Codigo/12_contrato_ops.sql"],
    ["Contratos (4)","Errores (2)","Outline (3)","Paquete (1)"],
    ["Sin errores.","Outline logos."]),
13:("Caso real -> 3 mejoras VetCare.",
    ["@@Por que importa al PI:@@ lecciones accionables.",
     "Autonoma: 1 caso -> 3 mejoras."],
    ["Caso elegido.","Resumen.","3 mejoras.","Informe.","Domingo 23:59."],
    ["Plantilla: contexto->fallo->leccion->cambio."],
    ["Mejoras accionables?","Conectan al PI?","Evidencia de lectura?"],
    "Solucion Taller Clase 13 — Casos reales","1 caso -> 3 mejoras.",
    ["Elegir caso.","Resumir.","3 mejoras.","Actualizar informe."],
    ["Plantilla contexto->fallo->leccion->cambio VetCare."],
    ["Caso (2)","Resumen (2)","Mejoras (4)","Informe (2)"],
    ["Mejoras genericas.","Sin conexion PI."]),
15:("Paquete final + sustentacion 5-8 min.",
    ["@@Por que importa al PI:@@ cierre segun rubrica 20% Corte 3.",
     "No confundir con Parcial 3 (Clase 14)."],
    ["ZIP/PDF Campus.","Sustentacion 5-8 min.","Autoevaluacion.","Cierre."],
    ["Checklist empaquetado del enunciado PI."],
    ["Falta evidencia?","Todos hablan?","PI != P3?"],
    "Solucion Taller Clase 15 — Entrega final","Checklist empaquetado + pitch.",
    ["Verificar ZIP vs rubrica.","Sustentacion.","Autoevaluacion.","Cierre."],
    ["Estructura: ER, DDL, roles, procs, fn/triggers, opt, indices, tx, concurrencia, contrato, informe."],
    ["Paquete (4)","Sustentacion (3)","Autoevaluacion (2)","Rubrica (1)"],
    ["Faltan evidencias.","Confundir con P3."]),
}

def accent(s):
    for a,b in [
        ("Por que","Por qué"),("seccion","sección"),("Seccion","Sección"),
        ("Solucion","Solución"),("autonoma","autónoma"),("Autonoma","Autónoma"),
        ("minimas","mínimas"),("clinica","clínica"),("dueno","dueño"),("Dueno","Dueño"),
        ("pagina","página"),("Justificacion","Justificación"),("justificacion","justificación"),
        ("Leccion","Lección"),("leccion","lección"),("rubrica","rúbrica"),
        ("validacion","validación"),("Validacion","Validación"),("tipica","típica"),
        ("proposito","propósito"),("optmizacion","optimización"),("Optimizacion","Optimización"),
        ("despues","después"),("Antes/despues","Antes/después"),("generico","genérico"),
        ("conexion","conexión"),("Politica","Política"),("politica","política"),
        ("Administracion","Administración"),("administracion","administración"),
        ("recepcion","recepción"),("Recepcion","Recepción"),
    ]:
        s = s.replace(a,b)
    return s

TALLER_BLOQUE = {}
SOLUCION = {}
for n, row in META.items():
    obj, ctx, crit, esc, pistas, st, sr, sp, se, sru, serr = row
    TALLER_BLOQUE[n] = {
        "contexto":[accent(x) for x in ctx],
        "objetivo":accent(obj),
        "criterios":[accent(x) for x in crit],
        "escenario":[accent(x) for x in esc],
        "pistas":["□ "+accent(x) for x in pistas],
    }
    SOLUCION[n] = {
        "titulo":accent(st), "resumen":accent(sr),
        "pasos":[accent(x) for x in sp], "ejemplo":[accent(x) for x in se],
        "rubrica":[accent(x) for x in sru], "errores":[accent(x) for x in serr],
    }

out = Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos\.config\slides\bd2_taller_data.py")
body = '# -*- coding: utf-8 -*-\n"""Taller ampliado + soluciones BD II / VetCare (PRIVADO)."""\n\n'
body += "HERRAMIENTAS_DIA = " + emit(HERRAMIENTAS_DIA) + "\n\n"
body += "TALLER_BLOQUE = " + emit(TALLER_BLOQUE) + "\n\n"
body += "SOLUCION = " + emit(SOLUCION) + "\n"
out.write_text(body, encoding="utf-8")
print("OK", out, out.stat().st_size)
