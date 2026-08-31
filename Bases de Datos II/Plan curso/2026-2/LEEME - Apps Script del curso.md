# Apps Script del curso - Bases de Datos II - 2026-2

## Bloquear los encuentros en TU calendario (cada sesion con su propio Meet)

El script **existe** y esta aqui:

```
_privado/CrearEncuentros - Bases de Datos II.gs
```

Ruta completa desde la raiz de `Cursos`:

```
Bases de Datos II/Plan curso/2026-2/_privado/CrearEncuentros - Bases de Datos II.gs
```

> **Por que no lo ves en GitHub:** los `.gs` de encuentros viven en `_privado/`, que
> esta en `.gitignore`. Existe en tu disco y en Drive, no en el repositorio remoto.
> Si no aparece, regeneralo:
>
> ```bash
> python config/calendario/generar_apps_script_encuentros.py
> ```

Crea **13 eventos** (uno por sesion) en **tu** calendario. **No invita a nadie y
no manda ningun correo:** son bloques tuyos, para que la agenda quede reservada y cada
sesion traiga su enlace a mano.

11 eventos llevan **su propia sala de Meet**; 2 son semanas autonomas por festivo, que quedan en el calendario **sin Meet**.

El enlace de cada sesion queda en **Ubicacion** y al final de la descripcion del
evento: de ahi lo copias para compartirlo con el grupo por donde de verdad les
escribes.

Funciones: `verificar` · `crearEncuentros` · `eliminarEncuentros` · `recrearTodo`.

**Paso a paso:** `Manuales/01 - Alistar un curso (encuentros, Meet, correo e
invitaciones).md` en la raiz de `Cursos`. Incluye como sacar el `CALENDAR_ID` y por
que se ejecuta `verificar` antes de `crearEncuentros`.

## Si prefieres un solo script para los 7 cursos

Hay uno consolidado, con las funciones de creacion y borrado **de cada curso** mas
las de todo el semestre. Sale de la misma plantilla que este, asi que hacen lo mismo:

```
_privado/2026-2/CrearEncuentros - TODO EL SEMESTRE 2026-2.gs
```

Puntero visible: `LEEME - Apps Script del semestre.md` en la raiz de `Cursos`.

## Archivar las grabaciones de Meet

Ese script es **uno solo** y vive en
`config/calendario/apps_script_grabaciones/MoverGrabaciones.gs`.
Paso a paso: `Manuales/02 - Instalar y probar el Apps Script de grabaciones.md`.

---

*Archivo generado por `config/calendario/generar_apps_script_encuentros.py`.*
