# Solución Taller Clase 6 — Optimización

> DOCUMENTO DOCENTE — PRIVADO. No publicar en Clases/.

**Resumen:** Pareja antes/después VetCare.

## Alineacion
- Taller: `Clases/Clase 6 - Optimizacion de consultas/Taller PI - Clase 6 - VetCare.docx`
- Hito: Primera pareja de consultas antes/despues del PI
- Entregable: 2 consultas (antes/despues) + justificacion (media pag.)

## Solucion paso a paso
1. Elegir una consulta real y frecuente del PI (ej. listar las citas del dia con nombre de mascota y dueno) — no un ejemplo inventado sin uso real.
2. Escribir la version "antes" tal como la escribiria alguien sin entrenamiento: SELECT * ... con JOIN sin filtro de fecha, trayendo todo el historico.
3. Reescribir la version "despues": proyectar solo las columnas necesarias, filtrar por fecha_hora >= hoy ANTES del JOIN cuando el motor lo permita, y evitar funciones sobre la columna de fecha en el WHERE.
4. Justificar por escrito minimo 3 cambios concretos (ej. "se elimino SELECT * porque solo se usan 4 columnas", "el filtro de fecha reduce el conjunto antes del JOIN", "se evito CAST sobre fecha_hora en el WHERE porque bloqueaba el uso de indice").
5. Guardar ambas versiones como 06_opt_antes.sql y 06_opt_despues.sql en la carpeta del equipo, y si el playground lo permite, adjuntar el resultado de EXPLAIN de cada una como evidencia de la mejora.

## Ejemplo / SQL / artefactos
- Codigo/06_opt_consultas.sql
- Script demo: `Kit docente/Clase 6/Codigo/06_opt_consultas.sql`

## Rubrica corta
- [ ] Consulta PI (2)
- [ ] Pareja (3)
- [ ] Justificación (3)
- [ ] Archivos (2)

## Errores frecuentes
- Caso genérico.
- Sin diferencia real.

Campus Virtual UNIAJC.
