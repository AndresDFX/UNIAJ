# Apps Script del curso - Bases de Datos II - 2026-2

## ATENCION: este curso NO tiene Apps Script al dia

La ultima regeneracion **no encontro la nomina** del grupo `FI303215` / `641A-2`, asi que no se pudo generar el `.gs`.

> **Hay un `.gs` viejo en `_privado/`. NO lo uses:** trae la nomina de la
> corrida anterior, asi que invitaria a los estudiantes equivocados.

### Como arreglarlo

1. Exporta de Academusoft la **Lista de Alumnos por Grupo** de `FI303215` (grupo `641A-2`).
2. Dejala en `Bases de Datos II/Plan curso/2026-2/`.
3. Vuelve a correr, desde la raiz de `Cursos`:

```
python config/calendario/generar_eventos_calendario.py
python config/calendario/generar_apps_script_encuentros.py
```

Si el listado que dejaste es de OTRA asignatura, el generador lo dice y lo omite:
compara el codigo `FI######` del archivo con el del curso.

---

*Archivo generado por `config/calendario/generar_apps_script_encuentros.py`.*
