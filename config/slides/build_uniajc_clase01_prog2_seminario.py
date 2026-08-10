# -*- coding: utf-8 -*-
"""Guion docente de la Clase 1 para Programacion II y Seminario de Sistemas.

Por que existe
--------------
Los dos cursos tenian `Kit docente/Clase 1/` con SOLO la prueba diagnostica: sin
guion docente. Era la unica clase de todo el semestre sin guion, y justamente la
mas delicada — es el dia en que se aplica el diagnostico y ademas se arranca el
tema, todo en el mismo bloque que la Sesion 0.

Sigue la regla de oro del workspace: el guion asume que el docente NO sabe nada
del tema, asi que trae fundamento teorico desarrollado + plan minuto a minuto que
cubre el bloque completo. Solo el tema de ESTA clase (la logistica del semestre
vive en la Presentacion del Curso).

Salida: `<Curso>/Kit docente/Clase 1/Guion Docente Clase 1 - <tema>.md` (+ .docx
via guion_md_a_docx.py).
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLIDES = Path(__file__).resolve().parent


PROG2 = """# Guion docente · Clase 1 · Introduccion a la POO

- **Curso:** Programacion II (FI303204) · 120 min
- **Tipo:** REGULAR · **presencial** (Clase 1 siempre es presencial)
- **Dia 1:** este bloque comparte espacio con la **Sesion 0** (Presentacion del Curso,
  archivo aparte). Sesion 0 = logistica y encuadre; esta Clase 1 = diagnostico + primer tema.
- **Entregable de hoy:** entorno de desarrollo funcionando + primera clase Java escrita
- **Slides:** `Clases/Clase 1 - Introduccion a POO/Presentacion.pptx`

> Sin mapa completo del curso, sin bio del docente, sin fechas de periodo:
> todo eso ya se cubrio en la Sesion 0.

## Fundamento teorico para el docente

**Que es la Programacion Orientada a Objetos y por que existe.** Antes de la POO, un
programa era una lista de procedimientos que operaban sobre datos sueltos. Cuando el
programa crecia, nadie sabia que funcion tocaba que dato, y un cambio pequeño rompia
cosas en lugares inesperados. La POO propone lo contrario: juntar en una sola unidad
—el objeto— los datos y las operaciones que los manipulan. El programa deja de ser
"una receta" y pasa a ser "un conjunto de piezas que se hablan entre si".

**Clase vs objeto (la distincion que mas cuesta el primer dia).** La clase es el
molde; el objeto es la pieza fabricada con ese molde. `Mascota` es la clase: define
que toda mascota tiene nombre, especie y edad. `luna` es un objeto: una mascota
concreta, con nombre "Luna", especie "Canino", edad 3. De una misma clase se crean
tantos objetos como haga falta, cada uno con sus propios valores. Analogia util en
clase: el plano de una casa (clase) frente a las casas construidas con ese plano
(objetos) — cada casa puede estar pintada de distinto color, pero todas tienen la
misma estructura.

**Los cuatro pilares, en una frase cada uno:**

- **Abstraccion:** quedarse solo con lo que importa del problema. Para una clinica
  veterinaria, de una mascota importa su especie y su historial; no importa su color
  favorito. Modelar es decidir que se ignora.
- **Encapsulamiento:** los datos de un objeto no se tocan directamente desde afuera;
  se accede a traves de metodos. El atributo va `private` y se expone con getters y
  setters. Asi el objeto puede validar (ej.: rechazar una edad negativa) en vez de
  quedar a merced de quien lo use.
- **Herencia:** una clase puede extender a otra y reutilizar lo que ya define.
  `Perro extends Mascota` hereda nombre y edad, y agrega lo suyo (raza). Advertencia
  para el docente: la herencia se sobreusa; solo aplica cuando de verdad hay una
  relacion "es un" (un perro ES una mascota). Si la relacion es "tiene un", no es
  herencia, es composicion.
- **Polimorfismo:** el mismo mensaje produce comportamientos distintos segun el objeto
  que lo recibe. Si `Perro` y `Gato` heredan de `Mascota` y ambos redefinen
  `hacerSonido()`, recorrer una lista de mascotas y llamar ese metodo produce "Guau"
  o "Miau" segun el objeto real. El codigo que recorre la lista no necesita saber de
  que tipo es cada una.

**Error tipico del docente que no domina el tema:** presentar los cuatro pilares como
cuatro definiciones que hay que memorizar. El estudiante los aprende de verdad cuando
ve el problema que cada uno resuelve. Por eso hoy solo se introducen con un ejemplo
concreto; se profundizan en las clases siguientes.

**Constructor y `new`:** el constructor es el metodo que se ejecuta al crear el
objeto y deja sus atributos en un estado valido. `new Mascota("Luna", "Canino", 3)`
reserva memoria y llama al constructor. Si no se escribe ninguno, Java agrega uno
vacio por defecto — y ahi es donde aparecen objetos a medio inicializar.

**Sobre el diagnostico de hoy:** no es una nota. Sirve para saber con que llega el
grupo (si recuerdan Java basico, si distinguen tipos primitivos, si han visto clases
antes). El resultado condiciona el ritmo de las Clases 2 y 3, asi que conviene
revisarlo el mismo dia y registrar el consolidado en `Entregas docente/`.

## Plan minuto a minuto (120 min)

### 0-15 · Enlace con la Sesion 0 y encuadre del tema
**Decir:** «Acabamos de ver como funciona el curso. Ahora empezamos el primer tema:
programacion orientada a objetos. Hoy no van a memorizar definiciones; van a escribir
su primera clase Java y a dejar el entorno listo.»
Aclarar que la Sesion 0 y esta clase son el mismo bloque pero cosas distintas.

### 15-35 · Prueba diagnostica
Aplicar `Kit docente/Clase 1/Prueba Diagnostica…`. Individual, sin nota.
**Decir:** «Esto no se califica. Me sirve para saber a que ritmo vamos.»
Mientras responden, pasar asistencia.

### 35-70 · Teoria Core: clase, objeto y los cuatro pilares
Recorrer las diapositivas 5 y 6 apoyandose en el fundamento de arriba.
Orden sugerido: (1) el problema que resuelve la POO, (2) clase vs objeto con la
analogia del plano y las casas, (3) los cuatro pilares con UN ejemplo del dominio
veterinario cada uno.
Pregunta al aire (2 min): «Si `Mascota` es la clase, ¿que seria un objeto?»
Escribir en el tablero la clase `Mascota` con tres atributos y un constructor.

### 70-85 · Mini-demo en codigo
Proyectar el editor y escribir en vivo, sin copiar-pegar:
- la clase `Mascota` con atributos `private`,
- su constructor,
- un getter,
- un `main` que crea dos objetos distintos y los imprime.
**Decir:** «Fijense que las dos mascotas salen del mismo molde pero tienen datos
distintos. Eso es clase contra objeto.»

### 85-110 · Laboratorio: entorno listo + primera clase propia
Cada estudiante deja funcionando su entorno (JDK + NetBeans o el IDE del curso) y
escribe su propia clase con al menos dos atributos y un constructor.
Circular por los puestos: el objetivo real de este bloque es que **nadie se quede sin
entorno**, porque arrastrar eso a la Clase 2 bloquea todo el curso.
Quien termine antes: agregar un segundo objeto y un metodo que imprima sus datos.

### 110-120 · Cierre y primer contacto con el Proyecto Integrador
**Decir:** «Todo el semestre trabajamos un mismo producto: VetCare, el sistema de la
clinica veterinaria Huellitas. Lo que escribieron hoy es la semilla de ese sistema.»
Señalar donde vive el enunciado (`Clases/Proyecto Integrador/`) y recordar que quien
tambien cursa Seminario de Sistemas hara alla los planos del MISMO producto.

## Cierre docente (despues de clase)

- Revisar el diagnostico y anotar el consolidado en `Entregas docente/<periodo>/DIAGNOSTICO…`.
- Anotar quien quedo sin entorno funcionando: son los que hay que atender en la Clase 2.
"""


SEMINARIO = """# Guion docente · Clase 1 · Conceptos iniciales de ingenieria de software

- **Curso:** Seminario de Sistemas (FI303301) · 120 min
- **Tipo:** REGULAR · **presencial** (Clase 1 siempre es presencial)
- **Dia 1:** este bloque comparte espacio con la **Sesion 0** (Presentacion del Curso,
  archivo aparte). Sesion 0 = logistica y encuadre; esta Clase 1 = diagnostico + primer tema.
- **Entregable de hoy:** equipo conformado + dominio del proyecto elegido y acotado
- **Slides:** `Clases/Clase 1 - Conceptos iniciales/Presentacion.pptx`

> Sin mapa completo del curso, sin bio del docente, sin fechas de periodo:
> todo eso ya se cubrio en la Sesion 0.

## Fundamento teorico para el docente

**Que es la ingenieria de software y por que no es "programar".** Programar es
escribir codigo que funcione. La ingenieria de software es el conjunto de practicas
que hacen que ese codigo siga funcionando cuando el sistema crece, cuando lo mantiene
otra persona y cuando los requisitos cambian. La diferencia se nota en el costo: un
error detectado al analizar requisitos cuesta corregirlo una fraccion de lo que
cuesta corregirlo en produccion. Esa es la justificacion economica de todo lo que se
vera en este curso.

**Producto vs proyecto.** El *producto* es el software (y su documentacion). El
*proyecto* es el esfuerzo acotado en tiempo y recursos para construirlo. Un proyecto
puede terminar y el producto seguir vivo durante años. Confundirlos lleva a creer que
"entregamos, ya terminamos".

**Requisitos funcionales vs no funcionales.** Un requisito funcional dice QUE debe
hacer el sistema ("registrar una mascota con ID, nombre y especie"). Uno no funcional
dice COMO debe comportarse ("la busqueda de un expediente responde en menos de 2
segundos", "la informacion no se pierde ante un corte de energia"). Los no funcionales
son los que mas se olvidan y los que mas arquitectura condicionan. Regla practica para
el estudiante: si no se puede verificar, no es un requisito — es un deseo. «El sistema
debe ser rapido» no es requisito; «responde en menos de 2 s con 50 usuarios» si lo es.

**Interesados (stakeholders).** No solo el que paga. En la clinica veterinaria del
proyecto hay al menos tres: el dueño de la clinica (quiere metricas), la recepcionista
(quiere agendar rapido) y el veterinario (quiere el historial a la mano). Sus intereses
pueden entrar en conflicto, y resolver ese conflicto es trabajo de analisis, no de
programacion.

**Ciclo de vida del software (introduccion).** Todo desarrollo pasa por las mismas
fases —requisitos, diseño, construccion, pruebas, mantenimiento— y lo que cambia entre
metodologias es COMO se recorren: una sola vez y en orden (cascada) o en ciclos cortos
que repiten todas las fases (iterativo/agil). Hoy solo se nombran; se comparan a fondo
en las Clases 2, 3 y 4.

**El rol del estudiante en este curso.** Aqui no se construye el software: se diseñan
los planos. Es la diferencia entre el arquitecto y el maestro de obra. Conviene decirlo
explicitamente el primer dia, porque un estudiante que espera programar se frustra, y
uno que entiende el rol valora el entregable.

**Error tipico del docente que no domina el tema:** empezar por las metodologias
(cascada, Scrum) antes de que el estudiante entienda que problema resuelven. Sin la
nocion de "el costo del error crece con el tiempo", las metodologias suenan a
burocracia arbitraria.

**Sobre el diagnostico de hoy:** no es una nota. Sirve para saber si el grupo llega con
nociones de UML, de requisitos o de trabajo en equipo. El resultado ajusta la
profundidad de las Clases 2 a 4.

## Plan minuto a minuto (120 min)

### 0-15 · Enlace con la Sesion 0 y encuadre del tema
**Decir:** «Ya vimos como funciona el curso. Ahora arrancamos el primer tema. Y algo
importante desde hoy: en esta materia ustedes no van a programar; van a diseñar. Su
producto son los planos que otro equipo podria construir.»

### 15-35 · Prueba diagnostica
Aplicar `Kit docente/Clase 1/Prueba Diagnostica…`. Individual, sin nota.
**Decir:** «No se califica. Me sirve para calibrar el ritmo.»
Mientras responden, pasar asistencia.

### 35-70 · Teoria Core: que es ingenieria de software
Apoyarse en el fundamento de arriba, en este orden:
1. Programar vs hacer ingenieria (el argumento del costo del error).
2. Producto vs proyecto.
3. Requisitos funcionales vs no funcionales, con la regla «si no se puede verificar,
   no es un requisito».
4. Interesados: los tres de la clinica veterinaria y sus intereses en conflicto.
5. Ciclo de vida: nombrar las fases, sin entrar aun en metodologias.

Ejercicio corto en el tablero (5 min): dar la frase cruda «necesito buscar rapido el
expediente de un animal» y convertirla entre todos en un RF y un RNF bien escritos.

### 70-100 · Taller: conformar equipo y acotar el dominio
En equipos de 2-3:
- elegir el dominio del proyecto (por defecto, la clinica veterinaria del PI),
- escribir el problema en 2-3 frases,
- listar 3-5 capacidades del sistema,
- identificar 2-3 actores.

Circular por los equipos con un solo criterio: **bloquear dominios vagos**. Si el
equipo dice «una app para la universidad», no hay problema concreto y todo el semestre
se les vuelve humo. Exigir un actor con un dolor medible.

### 100-115 · Puesta en comun
Dos o tres equipos leen su ficha. El grupo señala que capacidad no se entiende.
**Decir:** «Si nosotros no entendemos su sistema en 30 segundos, un programador
tampoco va a poder construirlo.»

### 115-120 · Cierre y primer contacto con el Proyecto Integrador
Señalar donde vive el enunciado (`Clases/Proyecto Integrador/`) y explicar los tres
casos segun matricula (cursa ambas materias / solo esta / solo Programacion II).
Dejar claro que quien cursa solo Seminario cierra con documento de diseño y prototipo
navegable, **sin escribir codigo**: es una ruta completa, no una version reducida.

## Cierre docente (despues de clase)

- Revisar el diagnostico y anotar el consolidado en `Entregas docente/<periodo>/DIAGNOSTICO…`.
- Anotar que equipos quedaron con el dominio aun sin acotar: hay que cerrarlo en la Clase 2.
"""


DESTINOS = [
    (ROOT / "Programacion II" / "Kit docente" / "Clase 1",
     "Guion Docente Clase 1 - Introduccion a POO.md", PROG2),
    (ROOT / "Seminario de Sistemas" / "Kit docente" / "Clase 1",
     "Guion Docente Clase 1 - Conceptos iniciales.md", SEMINARIO),
]


def main() -> None:
    conv = SLIDES / "guion_md_a_docx.py"
    for carpeta, nombre, texto in DESTINOS:
        carpeta.mkdir(parents=True, exist_ok=True)
        (carpeta / "Capturas").mkdir(exist_ok=True)
        md = carpeta / nombre
        md.write_text(texto, encoding="utf-8")
        print("OK md   ->", md.relative_to(ROOT))
        if conv.exists():
            subprocess.run([sys.executable, str(conv), str(md)], check=False)


if __name__ == "__main__":
    main()
