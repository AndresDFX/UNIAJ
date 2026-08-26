# Apps Script del curso - Seminario de Sistemas - 2026-2

## Crear los encuentros en Calendar (cada sesión con su propio Meet)

El script **existe** y esta aqui:

```
_privado/CrearEncuentros - Seminario de Sistemas.gs
```

Ruta completa desde la raiz de `Cursos`:

```
Seminario de Sistemas/Plan curso/2026-2/_privado/CrearEncuentros - Seminario de Sistemas.gs
```

> **Por que no lo ves en GitHub:** el `.gs` incluye los correos de los 22
> estudiantes del grupo, asi que la carpeta `_privado/` esta en `.gitignore`.
> Existe en tu disco y en Drive, no en el repositorio remoto. Si no aparece,
> regeneralo:
>
> ```bash
> python config/calendario/generar_apps_script_encuentros.py
> ```

Crea **13 eventos** (uno por sesion) e invita a los **22 estudiantes**,
enviandoles la invitacion de verdad. Deja **la misma sala de Meet** en todas las
sesiones sincronicas; las autonomas por festivo quedan en el calendario pero sin Meet.

**Paso a paso:** `Manuales/01 - Alistar un curso (encuentros, Meet, correo e
invitaciones).md` en la raiz de `Cursos`. Incluye como sacar el `CALENDAR_ID` y por
que se ejecuta `verificar` antes de `crearEncuentros`.

## Archivar las grabaciones de Meet

Ese script es **uno solo para los 4 cursos** y vive en
`config/calendario/apps_script_grabaciones/MoverGrabaciones.gs`.
Paso a paso: `Manuales/02 - Instalar y probar el Apps Script de grabaciones.md`.

---

*Archivo generado por `config/calendario/generar_apps_script_encuentros.py`.*
