# Solución Taller Clase 8 — Actions + monitoreo

> DOCUMENTO DOCENTE — PRIVADO. No compartir en Clases/ ni Campus antes del cierre.

**Resumen:** ci.yml build/test + deploy simulado + 4 métricas.

## Alineacion al enunciado estudiante
- Taller: `Clases/Clase 8 - Monitoreo optimizacion y CI-CD/Taller Clase 8 - CloudLite.docx`
- Hito PI: Workflow Actions build/test/simulate + metricas de monitoreo
- Entregable: .github/workflows/ci.yml + seccion Monitoreo/CI del informe

## Solucion paso a paso
1. Repo+stub.
2. ci.yml checkout->build/test->artifact.
3. 4-6 métricas golden signals-lite.
4. Captura o YAML+explicación.

## Ejemplo / artefactos esperados
- name: ci
- on: [push]
- jobs.build.runs-on: ubuntu-latest
- steps: checkout + build-and-test + deploy-simulated

## Rubrica corta / checklist de correccion
- [ ] YAML (3)
- [ ] Build/test serio (2)
- [ ] Métricas (3)
- [ ] Evidencia (2)

## Errores frecuentes
- Solo echo vacío.
- Secrets en claro.

Campus Virtual UNIAJC. Politica: gratis + navegador.
