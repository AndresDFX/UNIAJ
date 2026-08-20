# Apps Script — mover grabaciones de Meet

`MoverGrabaciones.gs` es un **Google Apps Script**: corre dentro de la cuenta de Google del
docente, no en este repo ni en un servidor. Este archivo es la **copia versionada**; el que
se ejecuta es el que se pegue en la cuenta. **No se sincronizan.**

## Instalación y pruebas

→ **[Manuales/02 - Instalar y probar el Apps Script de grabaciones.md](../../../Manuales/02%20-%20Instalar%20y%20probar%20el%20Apps%20Script%20de%20grabaciones.md)**

Ahí está el paso a paso (permisos, `verificarCarpetas`, `simulacro`, `instalarDisparador`),
qué hacer si deja de funcionar y las limitaciones conocidas.

## Notas técnicas

Funciones que se ejecutan a mano:

| Función | Qué hace |
|---|---|
| `verificarCarpetas` | Comprueba que las carpetas destino existan y sean accesibles |
| `simulacro` | Lista a qué curso iría cada grabación, **sin mover nada** |
| `instalarDisparador` | Activa la ejecución automática cada 6 h |
| `desinstalarDisparador` | La desactiva |
| `moverGrabaciones` | La que corre el disparador; también sirve para forzar una pasada |

Los ids de `carpetaGrabadas` salen de `config/calendario/semestre_<periodo>.json` →
`cursos.<curso>.carpetas_drive.grabadas.id`. Están duplicados aquí a propósito, porque Apps
Script no puede leer el repo; `validar_calendario.py` comprueba que coincidan con el JSON y
que no se haya usado por error el id de la carpeta de *clases*, que es la del material
compartido.

Si no puede determinar el curso de un archivo, **no lo mueve**. Las carpetas de grabaciones
están compartidas con estudiantes: dejar un archivo quieto es mejor que publicarlo en el
curso equivocado.
