# Plantilla del correo de bienvenida

`correo_bienvenida.py` es **el texto** del correo de bienvenida, para cualquier curso y
cualquier periodo. El curso solo aporta **los datos**.

Existe porque el correo es el mismo cinco veces: cuándo nos vemos, qué fechas anotar, cómo
entrar a la plataforma y qué necesito del grupo. Escribirlo por curso garantiza que a los seis
meses cinco correos digan cinco cosas distintas del mismo ExamLab — y ya pasó: el de
Introducción a la Ingeniería llegó a 1255 palabras contra las ~860 de los otros cuatro, con
media clase de pedagogía dentro.

## Usarla para un curso nuevo

```python
import sys, os
sys.path.insert(0, os.path.join(RAIZ, "config", "correos"))
import correo_bienvenida as cb

cb.escribir({
    "curso": "Estructuras de Datos",
    "codigo": "FI303210",
    "grupo": "341A",
    "periodo": "2027-1",
    "dia": "Lunes",
    "horario": "18:00 – 20:00",
    "inicio_efectivo": "18:10",
    "primera": "01/02/2027",
    "ultima": "10/05/2027",
    "linea_calendario": "15 sesiones de lunes, una por semana, de 120 min.",
    "plataforma_encuentro": "Google Meet",
    "fechas_clave": [
        ("**Primera sesión** (Lunes)", "**01/02/2027**", "Sesión 1 · presentación y diagnóstico"),
        ("Parcial 1", "08/03/2027", "Sesión 6 · en ExamLab"),
        ("Última sesión (Lunes)", "**10/05/2027**", "Sesión 15 · sustentación"),
    ],
}, ruta_del_md)
```

Obligatorios: `curso`, `codigo`, `periodo`, `dia`, `horario`, `primera`, `ultima`. El resto
tiene valor por omisión o se **omite del correo** si no se pasa — un curso sin carpetas de
Drive no lleva esa sección, uno sin encuesta no la menciona. La lista completa de campos está
en la constante `CAMPOS` del módulo.

Para ver la forma sin cablear nada:

```bash
python config/correos/correo_bienvenida.py     # imprime un correo de ejemplo
```

**Las fechas se pasan ya formateadas** (`"01/02/2027"`), y **no se escriben a mano**: salen
del JSON del curso. Ver `build_uniajc_intro_ing_curso.py → build_correo()`, que las lee del
desglose de cortes de cada grupo, incluida la sesión en que cae cada evaluación.

## Qué NO va en este correo

Esto no es un descuido, es la decisión que hizo el correo utilizable:

| Fuera | Dónde vive |
|---|---|
| La dinámica de la sesión (minuto a minuto, cómo se arman los equipos) | Acuerdo Pedagógico · `LEEME - Dinamica de sesion y plataformas.md` del curso |
| El stack de herramientas con su uso una por una | Plan de curso · el LEEME del curso |
| Las reglas de aula | Acuerdo Pedagógico |
| El desglose de porcentajes por corte | Acuerdo Pedagógico · Plan de curso |

El correo tiene un solo trabajo: que el estudiante sepa **cuándo** es la clase y **entre a la
plataforma antes** del primer encuentro. Todo lo demás compite con eso.

Dos cosas que tampoco van, por regla:

- **Un enlace fijo de la sala.** Cada sesión tiene el suyo y se publica en ExamLab. Publicar
  uno mandaría al grupo a la sala equivocada las otras semanas.
- **Que la universidad no tiene campus virtual propio.** Al estudiante se le dice que ExamLab
  «no es una plataforma oficial de la UNIAJC» y ahí se para. El dato del LMS inexistente puede
  quedar en el kit docente, marcado como contexto interno.

## Quién la usa hoy

| Curso | Generador | Vía |
|---|---|---|
| Introducción a la Ingeniería (3 grupos) | `config/slides/build_uniajc_intro_ing_curso.py` | **esta plantilla** |
| Programación II · Seminario · Bases de Datos II · Arquitectura | `config/calendario/generar_semestre_2026_2.py` | bloques gestionados propios |

Los cuatro de 2026-2 **no** usan la plantilla, a propósito: su generador actualiza los correos
**en sitio** mediante marcas HTML (`<!-- examlab: generado -->`, `<!-- vocero: generado -->`,
…), lo que permite reescribir un bloque sin tocar lo que el docente haya editado a mano —
empezando por la contraseña temporal, que en esos cuatro se escribe a mano. Pasarlos a la
plantilla significaría perder eso a cambio de nada, porque sus correos ya están enviados.

**El riesgo de tener dos caminos es real**, así que está acotado: las URLs de ExamLab
(dirección, manual, video) viven **solo aquí** y `generar_semestre_2026_2.py` las importa de
este módulo. Si cambia la dirección de la plataforma, cambia en un sitio. Lo que sí puede
divergir es la **redacción** de los bloques; si se reescribe el texto de ExamLab, hay que
mirar los dos archivos. Para un curso nuevo, siempre esta plantilla.

## Si hay varios grupos del mismo curso

Un correo por grupo, porque lo que cambia es justo lo que el estudiante necesita: el día, la
hora y las fechas. Se pasa `nota_grupos` para que el encabezado lo diga, y `grupo` entra en el
título, en el asunto, en el «Para:» y en la nota de que ya están matriculados.
