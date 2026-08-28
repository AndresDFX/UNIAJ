# -*- coding: utf-8 -*-
"""Soluciones del taller por clase — Bases de Datos II (PRIVADO docente).

Por que existe
--------------
`bd2_taller_data.SOLUCION` daba tres o cuatro vinetas por clase: unos pasos, un
ejemplo y una rubrica corta. Con eso el docente no puede calificar una entrega ni
responderle a un estudiante por que su consulta esta mal, porque no hay respuesta
resuelta contra la que comparar ni desglose de puntos por pregunta.

Aqui la solucion se declara pregunta por pregunta, alineada con la rubrica de
`bd2_examlab_data`, y el render lo hace `solucion_taller` (compartido con
Arquitectura). Las clases que todavia no esten aqui conservan su solucion vieja:
la migracion es clase por clase y el build no se rompe por las que falten.

Cada pregunta trae tres bloques que no se mezclan:

  - `sql` / `respuesta` / `respuesta_mermaid` / `salida`  -> lo que se espera
  - `como_calificar`  -> el desglose de puntos de la rubrica de la plataforma
  - `errores`         -> lo que llega mal y que hacer con ello

El SQL esta escrito para **PostgreSQL**, que es el motor que ExamLab corre en el
navegador (PGlite), y para pegarse y ejecutarse tal cual al revisar una entrega
dudosa. No es Oracle: no hay `NUMBER`, `VARCHAR2` ni `DUAL`.
"""
from __future__ import annotations

from bd2_examlab_data import EXAMLAB


def opciones(n: int, i_pregunta: int):
    """(opciones, indices correctos) de una pregunta cerrada, leidas de ExamLab.

    Se lee del banco que ve el estudiante para que la clave de la solucion no
    pueda quedar marcando una opcion que en la plataforma ya cambio.
    """
    preguntas = (EXAMLAB.get(n) or {}).get("preguntas", [])
    if 1 <= i_pregunta <= len(preguntas):
        p = preguntas[i_pregunta - 1]
        return p.get("opciones") or [], set(p.get("correctas") or [])
    return [], set()


def mermaid_referencia(n: int) -> str:
    """Mermaid de referencia de la pregunta de diagrama, leido de ExamLab."""
    for p in (EXAMLAB.get(n) or {}).get("preguntas", []):
        if p.get("tipo") == "diagrama" and p.get("mermaid_esperado"):
            return p["mermaid_esperado"]
    return ""


SOLUCION = {
    1: {
        "titulo": "Solucion Taller Clase 1 — Arranque de VetCare DB",
        "resumen": (
            "Las 5 preguntas resueltas: el DDL de las tres tablas base con su integridad "
            "declarativa, el modelo ER completo en Mermaid, las cuatro consultas de repaso "
            "sobre los datos sembrados de la clinica Huellitas, la clave razonada de lo que "
            "el DDL puede y no puede garantizar, y la ficha de alcance del PI."
        ),
        "total": 100,
        "nota_actividad": (
            "El SQL de esta solucion esta en **PostgreSQL** y se puede pegar tal cual en la "
            "consola de ExamLab para comparar contra la entrega de un estudiante. El motor de "
            "la plataforma es PGlite en el navegador, no Oracle."
        ),
        "preguntas": [
            {
                "n": 1,
                "titulo": "DDL base de VetCare DB",
                "tipo": "bd_sql",
                "puntos": 30,
                "sql": """-- 1. Registro del proyecto en la bitacora que ya existe
INSERT INTO proyecto_pi (estudiante, codigo, proyecto)
VALUES ('Laura Restrepo Gomez', '202512345', 'VetCare - Restrepo');

-- 2. Las tres tablas base, con la integridad declarativa exigida
CREATE TABLE dueno (
  id_dueno  SERIAL PRIMARY KEY,
  nombre    TEXT NOT NULL,
  telefono  TEXT,
  email     TEXT,
  ciudad    TEXT DEFAULT 'Cali'
);

CREATE TABLE mascota (
  id_mascota SERIAL PRIMARY KEY,
  id_dueno   INT  NOT NULL REFERENCES dueno(id_dueno),
  nombre     TEXT NOT NULL,
  especie    TEXT NOT NULL,
  fecha_nac  DATE,
  activa     CHAR(1) NOT NULL DEFAULT 'S' CHECK (activa IN ('S','N'))
);

CREATE TABLE cita (
  id_cita    SERIAL PRIMARY KEY,
  id_mascota INT NOT NULL REFERENCES mascota(id_mascota),
  fecha_hora TIMESTAMP NOT NULL,
  estado     TEXT NOT NULL DEFAULT 'PROGRAMADA'
             CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))
);

-- 3. Datos de prueba: 3 duenos, 4 mascotas (una inactiva), 3 citas
INSERT INTO dueno (nombre, telefono, email) VALUES
  ('Ana Gomez',    '3001112233', 'ana.gomez@mail.com'),
  ('Carlos Ruiz',  '3014445566', 'carlos.ruiz@mail.com'),
  ('Marcela Diaz', '3027778899', 'marcela.diaz@mail.com');

INSERT INTO mascota (id_dueno, nombre, especie, fecha_nac, activa) VALUES
  (1, 'Firulais', 'Canino', DATE '2019-04-12', 'S'),
  (1, 'Luna',     'Felino', DATE '2021-08-30', 'S'),
  (2, 'Rocky',    'Canino', DATE '2016-01-20', 'N'),
  (3, 'Mishi',    'Felino', DATE '2022-11-05', 'S');

INSERT INTO cita (id_mascota, fecha_hora, estado) VALUES
  (1, TIMESTAMP '2026-09-01 09:00:00', 'PROGRAMADA'),
  (2, TIMESTAMP '2026-09-01 10:30:00', 'PROGRAMADA'),
  (4, TIMESTAMP '2026-09-02 08:15:00', 'ATENDIDA');

-- 4. Verificacion con JOIN explicito
SELECT m.nombre AS mascota, d.nombre AS dueno, c.fecha_hora
FROM cita c
JOIN mascota m ON m.id_mascota = c.id_mascota
JOIN dueno   d ON d.id_dueno   = m.id_dueno
ORDER BY c.fecha_hora;""",
                "salida": """ mascota  |    dueno     |     fecha_hora
----------+--------------+---------------------
 Firulais | Ana Gomez    | 2026-09-01 09:00:00
 Luna     | Ana Gomez    | 2026-09-01 10:30:00
 Mishi    | Marcela Diaz | 2026-09-02 08:15:00
(3 filas)""",
                "como_calificar": [
                    "12 pts las tres tablas creadas sin error, con su PK, las **2 FK**, el "
                    "`DEFAULT 'Cali'` de ciudad y los **2 CHECK** exigidos (`activa` y "
                    "`estado`). Se prorratea: cada restriccion que falte descuenta.",
                    "8 pts los datos: al menos 3 duenos, 4 mascotas con **>=1 inactiva** y 3 "
                    "citas coherentes con las FK. Si un INSERT viola una FK y el script no "
                    "corre, esta parte vale cero.",
                    "5 pts el `SELECT` final: devuelve filas y usa **JOIN explicito**. Un "
                    "producto cartesiano (`FROM cita, mascota`) no suma aunque el resultado "
                    "parezca correcto.",
                    "3 pts sintaxis 100 % PostgreSQL: `SERIAL` o `GENERATED ALWAYS AS "
                    "IDENTITY`, `TEXT`/`VARCHAR`. Se penaliza `NUMBER`, `VARCHAR2` y las "
                    "comillas dobles mal usadas.",
                    "2 pts las convenciones de nombres: minusculas, tabla en singular sin "
                    "tildes, e `id_<entidad>` con el **mismo nombre a ambos lados de la FK**.",
                    "El registro en `proyecto_pi` es obligatorio; la columna `integrantes` "
                    "solo se llena si hubo equipo autorizado y su ausencia **no descuenta**.",
                ],
                "errores": [
                    "`activa BOOLEAN` en vez de `CHAR(1)` con CHECK. Funciona, pero rompe el "
                    "contrato del curso: los procedimientos de la Clase 3 y los disparadores "
                    "de la Clase 4 asumen `'S'`/`'N'`. Corrijalo hoy, no en la Clase 3.",
                    "`telefono INT`. Se pierden los ceros iniciales y no cabe el prefijo. Es "
                    "el ejemplo canonico de que un telefono no es un numero.",
                    "`fecha_hora TEXT`. El `ORDER BY` sale alfabetico y el indice de la Clase 7 "
                    "no sirve de nada. Debe ser `TIMESTAMP`.",
                    "Nombres en plural o con mayuscula (`Mascotas`, `Dueño`). PostgreSQL pliega "
                    "a minuscula lo que no va entrecomillado, asi que quien despues consulte "
                    "con comillas dobles obtiene «tabla inexistente» y pierde media clase.",
                    "Olvidar el `DEFAULT 'Cali'`. Es el criterio que comprueba que leyo la "
                    "tabla de requisitos y no solo copio un CREATE TABLE de memoria.",
                ],
            },
            {
                "n": 2,
                "titulo": "Modelo ER de VetCare DB en Mermaid",
                "tipo": "diagrama",
                "puntos": 20,
                "respuesta_mermaid": """erDiagram
    dueno ||--o{ mascota : "posee"
    mascota ||--o{ cita : "tiene agendada"
    veterinario ||--o{ cita : "atiende"
    cita ||--|| consulta : "documenta"
    consulta ||--o{ factura : "genera"
    factura ||--o{ detalle_factura : "se desglosa en"
    insumo ||--o{ detalle_factura : "se factura en"

    dueno {
        int id_dueno PK
        text nombre
        text telefono
    }
    mascota {
        int id_mascota PK
        int id_dueno FK
        char activa
    }
    veterinario {
        int id_veterinario PK
        text nombre
        text especialidad
    }
    cita {
        int id_cita PK
        int id_mascota FK
        timestamp fecha_hora
    }
    consulta {
        int id_consulta PK
        int id_cita FK
        text diagnostico
    }
    insumo {
        int id_insumo PK
        text nombre
        int stock
    }
    factura {
        int id_factura PK
        int id_consulta FK
        decimal total
    }
    detalle_factura {
        int id_factura PK
        int id_insumo PK
        decimal precio_unitario
    }""",
                "como_calificar": [
                    "8 pts las **8 entidades** con los nombres exactos del curso: `dueno`, "
                    "`mascota`, `veterinario`, `cita`, `consulta`, `insumo`, `factura`, "
                    "`detalle_factura`. 1 pt cada una.",
                    "7 pts las **7 relaciones** con la cardinalidad correcta: `||--o{` para "
                    "1‑N y `||--||` para 1‑1. Una cardinalidad invertida no suma, aunque la "
                    "relacion exista.",
                    "3 pts que cada entidad declare **al menos su PK y 2 atributos**, con `PK` "
                    "y `FK` marcados.",
                    "2 pts que renderice sin error de sintaxis dentro de la plataforma.",
                    "Los nombres tienen que coincidir con el DDL de la pregunta 1. Si el ER "
                    "dice `Mascotas` y el DDL `mascota`, no son el mismo modelo: se descuenta "
                    "de los 8 pts de entidades.",
                ],
                "errores": [
                    "Poner `cita ||--o{ consulta`. La relacion es **1‑1**: una cita atendida "
                    "produce una consulta y solo una. Es el error de cardinalidad mas comun y "
                    "se corrige preguntando «¿puede una cita tener dos consultas?».",
                    "Olvidar que `detalle_factura` tiene **clave compuesta** "
                    "(`id_factura` + `id_insumo`). Si le pone un `id_detalle` suelto no es "
                    "incorrecto, pero pidale que justifique por que necesita una clave "
                    "sustituta ahi.",
                    "Meter `precio_unitario` en `insumo` y no en `detalle_factura`. Es el "
                    "matiz que separa a quien entendio: en el detalle es el **precio "
                    "historico** del dia de la venta; si se toma del insumo, reimprimir una "
                    "factura de hace seis meses da otra cifra.",
                    "Entregar solo el PNG y dejar la pregunta vacia. Es de tipo `diagrama`: "
                    "recibe texto Mermaid, y si no renderiza no se puede calificar.",
                    "Inventar relaciones que no estan en el enunciado (por ejemplo "
                    "`dueno ||--o{ factura`). Se descuenta: el modelo es el del caso de "
                    "estudio, no el que al estudiante le parezca.",
                ],
            },
            {
                "n": 3,
                "titulo": "Consultas de repaso sobre los datos de Huellitas",
                "tipo": "bd_sql",
                "puntos": 25,
                "sql": """-- 1. Agenda del 1 de septiembre de 2026 (filtro por RANGO, no por funcion)
SELECT c.id_cita, c.fecha_hora,
       m.nombre AS mascota, d.nombre AS dueno, v.nombre AS veterinario
FROM cita c
JOIN mascota     m ON m.id_mascota     = c.id_mascota
JOIN dueno       d ON d.id_dueno       = m.id_dueno
JOIN veterinario v ON v.id_veterinario = c.id_veterinario
WHERE c.estado = 'PROGRAMADA'
  AND c.fecha_hora >= TIMESTAMP '2026-09-01 00:00:00'
  AND c.fecha_hora <  TIMESTAMP '2026-09-02 00:00:00'
ORDER BY c.fecha_hora;

-- 2. Mascotas sin ninguna cita registrada
SELECT m.nombre AS mascota, d.nombre AS dueno
FROM mascota m
JOIN dueno d ON d.id_dueno = m.id_dueno
LEFT JOIN cita c ON c.id_mascota = m.id_mascota
WHERE c.id_cita IS NULL
ORDER BY m.nombre;

-- 3. Citas por veterinario y estado, incluyendo veterinarios sin citas
SELECT v.nombre AS veterinario, c.estado, COUNT(c.id_cita) AS total
FROM veterinario v
LEFT JOIN cita c ON c.id_veterinario = v.id_veterinario
GROUP BY v.nombre, c.estado
ORDER BY v.nombre, c.estado;

-- 4. Riesgo de negocio: citas vivas de mascotas inactivas
SELECT c.id_cita, m.nombre AS mascota, c.estado
FROM cita c
JOIN mascota m ON m.id_mascota = c.id_mascota
WHERE m.activa = 'N'
  AND c.estado <> 'CANCELADA'
ORDER BY c.id_cita;""",
                "como_calificar": [
                    "6 pts la consulta 1: los cinco campos pedidos, `estado = 'PROGRAMADA'`, "
                    "**filtro por rango** con `>=` y `<`, y `ORDER BY` por hora. **Se pierden "
                    "3 pts si filtra con `to_char`, `EXTRACT` o `CAST` sobre `fecha_hora`**: "
                    "esa forma impide usar el indice de la Clase 7 y es el punto de la "
                    "pregunta.",
                    "6 pts la consulta 2: detecta las mascotas huerfanas con "
                    "`LEFT JOIN ... IS NULL` o `NOT EXISTS`. Un `INNER JOIN` devuelve lo "
                    "contrario de lo pedido y vale cero.",
                    "7 pts la consulta 3: `COUNT` con `GROUP BY` y **`LEFT JOIN`** para que "
                    "los veterinarios sin citas aparezcan. Con `INNER JOIN` desaparecen y se "
                    "pierden 4 de los 7.",
                    "6 pts la consulta 4: cruza `cita` con `mascota` inactiva y **excluye** "
                    "`CANCELADA`. Si el resultado sale vacio con los datos sembrados, la "
                    "consulta puede estar bien: pidale que lo interprete en una frase.",
                    "Se descuenta transversalmente por `SELECT *`, por joins implicitos con "
                    "comas y por resultados que no correspondan a los datos entregados.",
                ],
                "errores": [
                    "`WHERE to_char(c.fecha_hora,'YYYY-MM-DD') = '2026-09-01'`. Devuelve lo "
                    "correcto y por eso el estudiante lo defiende, pero aplica una funcion "
                    "sobre la columna e inutiliza el indice. Es exactamente el «antes» de la "
                    "Clase 6.",
                    "Usar `COUNT(*)` en la consulta 3 con `LEFT JOIN`: cuenta 1 para los "
                    "veterinarios sin citas en vez de 0. Debe ser `COUNT(c.id_cita)`.",
                    "Interpretar la consulta 4 al reves: creer que un resultado vacio es un "
                    "error de la consulta. Vacio significa que hoy nadie agendo una mascota "
                    "inactiva, y es la evidencia de por que en la Clase 3 hace falta un "
                    "procedimiento: la FK no lo impide, simplemente todavia no paso.",
                    "Joins implicitos (`FROM cita c, mascota m WHERE ...`). Funciona, pero el "
                    "curso exige `JOIN` explicito porque hace visible la condicion de union.",
                ],
            },
            {
                "n": 4,
                "titulo": "Que puede garantizar el DDL por si solo",
                "tipo": "cerrada_multi",
                "puntos": 10,
                "justificacion": {
                    0: ("CORRECTA. `CHECK (stock >= 0)` mira solo columnas de la fila que se "
                        "esta modificando, y eso es exactamente lo que un CHECK puede hacer. "
                        "Ojo con el matiz que conviene comentar: el CHECK impide guardar un "
                        "stock negativo, pero no evita que la factura quede a medias — eso "
                        "necesita una transaccion, y es el tema de la Clase 8."),
                    1: ("FALSA, y es la trampa principal. Un `CHECK` **no puede consultar otra "
                        "tabla**: solo ve columnas de la fila que se inserta o actualiza. Para "
                        "mirar `mascota.activa` desde `cita` hace falta logica programada."),
                    2: ("CORRECTA. Es la consecuencia de lo anterior: la regla necesita leer "
                        "una fila de OTRA tabla en el momento de la insercion, asi que se "
                        "resuelve con un procedimiento (Clase 3) o un disparador (Clase 4)."),
                    3: ("CORRECTA. El DDL declarativo describe el estado valido, no la "
                        "historia de los cambios. Para registrar quien cambio que y cuando "
                        "hace falta un `AFTER UPDATE` que escriba en una tabla de auditoria."),
                    4: ("FALSA. La FK garantiza que el identificador **exista**, no que el "
                        "negocio lo quiera. La mascota inactiva tiene un id valido y la FK la "
                        "acepta sin chistar. Es la frase que hay que dejar dicha hoy porque "
                        "sostiene toda la Clase 3."),
                    5: ("CORRECTA. Un dominio cerrado y conocido de antemano es el caso de uso "
                        "ideal del CHECK: valida sin mirar otras tablas y el motor lo hace "
                        "cumplir en cada INSERT y UPDATE, aunque alguien entre por fuera de la "
                        "aplicacion."),
                },
                "como_calificar": [
                    "10 pts con las **4 opciones correctas** marcadas y ninguna incorrecta.",
                    "Puntaje **proporcional** por acierto parcial: 2.5 pts por correcta "
                    "marcada, descontando por cada incorrecta marcada.",
                    "Las correctas son los indices **0, 2, 3 y 5**; la clave se lee del banco "
                    "de la plataforma, no de esta lista.",
                ],
                "errores": [
                    "Marcar la opcion del `CHECK` que consulta otra tabla. Si aparece en mas "
                    "de un tercio del grupo, conviene dedicarle dos minutos al abrir la Clase "
                    "3, porque es el cimiento de por que existen los procedimientos.",
                    "Marcar que la FK alcanza para impedir agendar mascotas inactivas. Es la "
                    "confusion mas costosa del semestre: el estudiante que la sostiene escribe "
                    "`sp_agendar_cita` sin validacion en la Clase 3.",
                    "Marcar las seis por seguridad. El puntaje proporcional lo castiga; digalo "
                    "antes de que abran la pregunta.",
                ],
            },
            {
                "n": 5,
                "titulo": "Ficha de alcance del Proyecto Integrador",
                "tipo": "abierta",
                "puntos": 15,
                "respuesta": """**Nombre del proyecto:** VetCare - Restrepo
**Autor:** Laura Restrepo Gomez · **Codigo:** 202512345
**Integrantes:** individual
**Descripcion:** VetCare DB es la base de datos que soporta la operacion diaria de la
Clinica Veterinaria «Huellitas»: agenda, historia clinica, insumos y facturacion.

**1) QUE SI HARA EL PI**
Registrara duenos y sus mascotas con baja logica, para no perder historial clinico.
Agendara citas por veterinario y franja, con estado (programada, atendida, cancelada).
Guardara la consulta de cada cita atendida con motivo, diagnostico y tratamiento.
Descontara insumos al facturar y dejara el detalle con el precio del dia de la venta.
Controlara quien puede hacer que mediante roles (recepcion, veterinario, auditor).
Auditara los cambios sensibles: precios de insumo y cancelaciones de cita.

**2) QUE NO HARA EL PI**
No cobrara en linea ni se integrara con ninguna pasarela de pagos.
No tendra aplicacion de escritorio ni movil: solo la capa de datos.
No manejara nomina ni contabilidad de la clinica.
No guardara imagenes ni resultados de laboratorio adjuntos.

**3) TRES REGLAS DE NEGOCIO PROPIAS (Condicion -> Accion)**
R1. Si un veterinario ya tiene una cita en la misma franja -> entonces no se puede
    crear otra cita para el a esa misma hora.
    Se implementa con: UNIQUE (id_veterinario, fecha_hora)
R2. Si una cita se cancela con menos de 2 horas de anticipacion -> entonces queda
    marcada como cancelacion tardia para el reporte del mes.
    Se implementa con: trigger BEFORE UPDATE sobre cita
R3. Si el precio de un insumo cambia -> entonces las facturas ya emitidas conservan
    el precio con el que se vendieron.
    Se implementa con: precio_unitario almacenado en detalle_factura

**4) RIESGO PRINCIPAL Y MITIGACION**
Riesgo: llegar a la Clase 8 con el esquema a medias y tener que rehacer tablas que ya
tienen procedimientos y disparadores escritos encima.
Mitigacion: cerrar el DDL completo en la Clase 2 y no cambiar nombres de columnas
despues; si algo falta, se agrega con ALTER TABLE en vez de recrear.""",
                "como_calificar": [
                    "3 pts las **5 secciones** de la plantilla presentes, y el proyecto llamado "
                    "**VetCare - [Apellido]**.",
                    "4 pts el SI/NO: delimita el alcance de forma **concreta y realista para "
                    "un semestre**. Promesas vagas («hara todo lo necesario») no suman.",
                    "6 pts las **3 reglas propias** en formato `Condicion -> Accion`, "
                    "verificables, **cada una con su mecanismo** de implementacion: 2 pts cada "
                    "una. Se pierde la mitad de una regla si no dice con que se implementa.",
                    "2 pts el riesgo principal con su mitigacion.",
                    "Se descuenta si las reglas **repiten literalmente** las tres del "
                    "enunciado general (mascota inactiva, stock, auditoria): se piden reglas "
                    "**propias**, distintas o adicionales.",
                    "Se descuenta si las reglas estan redactadas como deseos («el sistema debe "
                    "ser seguro») en vez de como condicion y accion.",
                ],
                "errores": [
                    "Copiar las tres reglas del enunciado. Es lo mas frecuente. Devuelvala "
                    "pidiendo una regla que se le haya ocurrido a el mirando el caso: la "
                    "doble reserva del veterinario suele salir sola si se le pregunta que "
                    "pasa si dos recepcionistas agendan a la vez.",
                    "Reglas sin mecanismo. Son 3 de los 15 puntos. Basta con nombrar el "
                    "instrumento (`CHECK`, `UNIQUE`, `FK`, procedimiento, trigger); no hace "
                    "falta el codigo todavia.",
                    "Alcance SI que promete la aplicacion y las pantallas. Recuerdele que en "
                    "esta asignatura el entregable es la capa de datos, y que la aplicacion "
                    "es el alcance de Programacion II sobre el mismo cliente.",
                    "Riesgo escrito como excusa anticipada («no tengo tiempo»). El riesgo debe "
                    "ser tecnico y con mitigacion accionable.",
                ],
            },
        ],
        "preguntas_frecuentes": [
            ("¿Puedo usar Oracle en vez de PostgreSQL?",
             "No para la entrega: la consola de ExamLab corre PostgreSQL (PGlite) en el "
             "navegador, asi que `NUMBER`, `VARCHAR2` y `DUAL` fallan. Oracle Live SQL se usa "
             "desde la Clase 3, cuando haga falta PL/SQL, y eso se dice ahi."),
            ("¿Por que `activa CHAR(1)` y no un booleano?",
             "Porque es el contrato del curso: los procedimientos de la Clase 3 y los "
             "disparadores de la Clase 4 asumen `'S'`/`'N'`. Un booleano funciona hoy y rompe "
             "el material de las clases siguientes."),
            ("¿Las 8 entidades hay que crearlas todas hoy?",
             "No. Hoy se crean **tres** tablas (`dueno`, `mascota`, `cita`) en la pregunta 1, y "
             "el diagrama de la pregunta 2 muestra las **ocho** del modelo completo. El "
             "diagrama es el plano; el DDL avanza clase por clase."),
            ("En la consulta 4, ¿esta mal si no devuelve filas?",
             "No necesariamente. Vacio significa que con los datos sembrados nadie agendo una "
             "mascota inactiva. Pidale que lo interprete: es la evidencia de que la regla se "
             "cumple hoy por casualidad y no porque la base la haga cumplir, que es el motivo "
             "de la Clase 3."),
            ("¿Las reglas de negocio pueden ser las tres del enunciado?",
             "No. Se piden **propias**, distintas o adicionales. Las del enunciado son el "
             "ejemplo de la forma esperada, no la respuesta."),
            ("¿Donde encuentro los nombres de los datos de prueba?",
             "En el anexo del caso de estudio, en `Clases/Proyecto Integrador/`. El elenco "
             "esta fijo y sin tildes, tal como esta sembrado en la base: usarlo evita que cada "
             "entrega hable de personas distintas."),
        ],
        "cierre": [
            "Al terminar, cada estudiante debe tener: el proyecto registrado en `proyecto_pi`, "
            "las tres tablas creadas con sus restricciones, el ER de 8 entidades renderizado y "
            "la ficha de alcance con sus 3 reglas propias.",
            "Lo que hay que verificar antes de cerrar la sesion es la **coherencia de nombres** "
            "entre el DDL de la pregunta 1 y el ER de la pregunta 2: si no coinciden, se "
            "arrastra a la Clase 2 y a todas las siguientes.",
            "Quien salga sin dominio ni alcance escritos no tiene sobre que trabajar en la "
            "Clase 2 (roles y privilegios): no deje el tema abierto para la semana siguiente.",
        ],
    },
    2: {
        "titulo": "Solucion del taller · Clase 2 · Administracion de BD y roles de VetCare",
        "resumen": (
            "Los 4 roles de VetCare creados y verificados con SQL que corre, la superficie "
            "recortada con una vista y con privilegios por columna, la matriz de 10 objetos x 4 "
            "roles consistente con esos GRANT, y la politica de altas y bajas con el limite del "
            "entorno reconocido."
        ),
        "nota_actividad": (
            "**El motor es PostgreSQL, no Oracle.** Las preguntas 1 y 3 son SQL que corre en "
            "ExamLab: `CREATE ROLE`, `GRANT`, `REVOKE`, `CREATE VIEW`, privilegios por columna e "
            "`information_schema` funcionan todos. Lo unico que el entorno no permite es una "
            "segunda sesion, asi que no se puede conectar como `recepcion` para ver el "
            "*permission denied*: eso es lo que la pregunta 5 pide reconocer. No repita en clase "
            "que «el playground no deja crear roles»: es falso aqui y cuesta los 50 puntos de las "
            "preguntas 1 y 3."
        ),
        "total": 100,
        "preguntas": [
            {
                "n": 1, "titulo": "Crear los roles de VetCare y otorgar privilegios",
                "tipo": "bd_sql", "puntos": 30,
                "sql": """-- =====================================================================
    -- 1) Los cuatro roles. NOLOGIN porque son bolsas de privilegios, no
    --    identidades: la persona se crea aparte, con LOGIN, y recibe el rol.
    -- =====================================================================
    CREATE ROLE admin_bd        NOLOGIN;
    CREATE ROLE recepcion       NOLOGIN;
    CREATE ROLE veterinario_rol NOLOGIN;
    CREATE ROLE auditor         NOLOGIN;

    -- =====================================================================
    -- 2) Privilegios. Un rol recien creado no tiene NINGUNO sobre tablas
    --    ajenas, asi que lo que no se escriba aqui queda negado por omision.
    -- =====================================================================

    -- recepcion: agenda y reprograma citas; identifica al cliente y su mascota.
    -- Sin DELETE: cancelar es UPDATE de estado a 'CANCELADA'.
    GRANT SELECT, INSERT, UPDATE ON cita TO recepcion;
    GRANT SELECT ON dueno, mascota, veterinario TO recepcion;

    -- veterinario_rol: lee la agenda y el paciente; documenta la atencion.
    GRANT SELECT ON cita, mascota TO veterinario_rol;
    GRANT SELECT, INSERT, UPDATE ON consulta TO veterinario_rol;

    -- auditor: solo lectura, y nunca una escritura.
    GRANT SELECT ON dueno, mascota, cita, consulta, factura TO auditor;

    -- admin_bd: el unico rol con privilegios amplios, sobre las 8 tablas.
    GRANT ALL PRIVILEGES ON dueno, mascota, veterinario, cita,
                            consulta, insumo, factura, detalle_factura
      TO admin_bd;

    -- =====================================================================
    -- 3) REVOKE explicito y documentado. Es redundante -- recepcion nunca
    --    recibio DELETE -- y se escribe precisamente por eso: deja por
    --    escrito que la ausencia de DELETE es una decision, no un olvido.
    --    Quien audite el script manana no tiene que adivinarlo.
    -- =====================================================================
    REVOKE DELETE ON cita FROM recepcion;

    -- =====================================================================
    -- 4) Verificacion: la matriz sale del motor, no de un documento.
    -- =====================================================================
    SELECT grantee, table_name, privilege_type
      FROM information_schema.role_table_grants
     WHERE grantee IN ('admin_bd','recepcion','veterinario_rol','auditor')
     ORDER BY grantee, table_name, privilege_type;""",
                "salida": """Filas por rol (el orden es grantee, table_name, privilege_type):

      auditor          -> 5 filas   : cita, consulta, dueno, factura, mascota (SELECT en cada una)
      recepcion        ->  6 filas   : cita x 3 (INSERT, SELECT, UPDATE) + dueno, mascota, veterinario (SELECT)
      veterinario_rol  ->  5 filas   : cita (SELECT), consulta x 3 (INSERT, SELECT, UPDATE), mascota (SELECT)
      admin_bd         -> 56 o 64 filas : las 8 tablas x los privilegios que ALL PRIVILEGES expande

    Las tres primeras cifras son exactas y son las que hay que contar. La de admin_bd
    depende de la version del motor: ALL PRIVILEGES sobre una tabla expande a INSERT,
    SELECT, UPDATE, DELETE, TRUNCATE, REFERENCES y TRIGGER (7 x 8 = 56), y desde
    PostgreSQL 17 se agrega MAINTAIN (8 x 8 = 64). No descuente por esa diferencia:
    lo que se califica es que aparezcan las 8 tablas.

    Para revisar rapido una entrega, sin leer 60 filas, esta variante agrupa la matriz
    en una fila por rol y objeto (no se pide en el enunciado, es para el docente):

      SELECT grantee, table_name,
             string_agg(privilege_type, ', ' ORDER BY privilege_type) AS privilegios
        FROM information_schema.role_table_grants
       WHERE grantee IN ('admin_bd','recepcion','veterinario_rol','auditor')
       GROUP BY grantee, table_name
       ORDER BY grantee, table_name;

      grantee          | table_name  | privilegios
      -----------------+-------------+-----------------------
      auditor          | cita        | SELECT
      auditor          | consulta    | SELECT
      auditor          | dueno       | SELECT
      auditor          | factura     | SELECT
      auditor          | mascota     | SELECT
      recepcion        | cita        | INSERT, SELECT, UPDATE
      recepcion        | dueno       | SELECT
      recepcion        | mascota     | SELECT
      recepcion        | veterinario | SELECT
      veterinario_rol  | cita        | SELECT
      veterinario_rol  | consulta    | INSERT, SELECT, UPDATE
      veterinario_rol  | mascota     | SELECT""",
                "como_calificar": [
                    "**10 pts — los 4 roles.** Los cuatro `CREATE ROLE` corren sin error y con "
                    "`NOLOGIN`. 2,5 por rol. Si usa `CREATE USER`, medio punto menos por rol: no "
                    "es un error de sintaxis (es un alias de `CREATE ROLE ... LOGIN`) pero "
                    "contradice la decision de que estos cuatro son bolsas de permisos.",
                    "**14 pts — los GRANT reproducen la matriz exactamente.** Se cuenta por rol: "
                    "4 pts `recepcion`, 3 pts `veterinario_rol`, 3 pts `auditor`, 4 pts "
                    "`admin_bd`. Se descuenta tanto por privilegio de mas como de menos, y la "
                    "verificacion es la salida de arriba: si `recepcion` no da 6 filas o "
                    "`auditor` no da 5, hay una diferencia y hay que localizarla.",
                    "**3 pts — el REVOKE explicito** de `DELETE ON cita FROM recepcion` esta "
                    "presente. Se dan los 3 puntos completos aunque el estudiante escriba al lado "
                    "que es redundante; de hecho, decirlo demuestra que entendio el punto de "
                    "partida en cero.",
                    "**3 pts — la consulta de verificacion** sobre "
                    "`information_schema.role_table_grants` con las tres columnas pedidas y el "
                    "`ORDER BY grantee, table_name, privilege_type`, y devuelve filas de los 4 "
                    "roles.",
                    "**Piso de sintaxis.** Si el script no corre, no hay puntos de los 14 de la "
                    "matriz: la pregunta es `bd_sql` y la evidencia es que el motor lo acepte. Si "
                    "corre pero la matriz esta incompleta, se califica lo que si quedo.",
                ],
                "errores": [
                    "**`GRANT CREATE SESSION TO recepcion`.** Es sintaxis de Oracle y en "
                    "PostgreSQL no existe. El equivalente no es un privilegio sino un atributo "
                    "del rol: `LOGIN`, que se escribe en el `CREATE ROLE`. Aparece en quien busco "
                    "en internet sin filtrar por motor.",
                    "**`CREATE USER recepcion IDENTIFIED BY '...'`.** Tambien Oracle. En "
                    "PostgreSQL es `CREATE ROLE recepcion LOGIN PASSWORD '...'`, y hoy no hace "
                    "falta ninguna clave porque no se conecta nadie.",
                    "**Otorgar `DELETE` a `recepcion` «para que pueda cancelar».** Es justo lo "
                    "que la pregunta 2 evalua. Cancelar es `UPDATE cita SET estado = 'CANCELADA'`: "
                    "conserva la historia y basta el `UPDATE` que ya tiene.",
                    "**Darle `ALL PRIVILEGES` a `admin_bd` sobre 5 tablas y no 8.** Deja al "
                    "administrador sin acceso a `dueno`, `mascota` y `veterinario`, y entonces la "
                    "matriz de la pregunta 4 queda con guiones en la columna del administrador, "
                    "que es indefendible. Es el error mas facil de arrastrar porque no produce "
                    "ningun mensaje de error.",
                    "**Escribir el rol en mayusculas y creerlo distinto.** PostgreSQL pasa los "
                    "identificadores sin comillas a minusculas, asi que `RECEPCION` y `recepcion` "
                    "son el mismo rol. `\"Recepcion\"` entre comillas dobles si es otro, y ese si "
                    "produce un error de rol inexistente que cuesta encontrar.",
                    "**Entregar solo la matriz en un documento** porque «el playground no deja». "
                    "Aqui si deja. Si alguien llega con eso, es probable que lo haya leido en una "
                    "version anterior de la guia: corrijalo en voz alta al grupo entero.",
                ],
            },
            {
                "n": 2, "titulo": "Privilegio minimo en la matriz de VetCare",
                "tipo": "cerrada_multi", "puntos": 10,
                "justificacion": {
                    0: "**Incorrecta.** Confunde la accion del negocio con la sentencia SQL. "
                       "Cancelar es un cambio de estado, no una desaparicion: la cita cancelada "
                       "hay que poder contarla, cobrarla si aplica y explicarla. Con `DELETE` se "
                       "pierde la evidencia de que existio, y ademas se abre la puerta a un "
                       "`DELETE` sin `WHERE` que borre la agenda completa.",
                    1: "**Correcta.** Es el borrado logico de la Clase 1 aplicado a permisos: "
                       "`UPDATE cita SET estado = 'CANCELADA' WHERE id_cita = ...`. Se conserva la "
                       "historia y el rol no necesita ningun privilegio nuevo, porque `UPDATE` ya "
                       "lo tiene para reprogramar.",
                    2: "**Incorrecta.** Es exactamente lo contrario de privilegio minimo: se "
                       "otorga por comodidad futura y no por necesidad presente. `ALL PRIVILEGES` "
                       "sobre `cita` incluye `DELETE` y `TRUNCATE`, asi que un error de copiar y "
                       "pegar vacia la tabla. El argumento de «no tener que ajustar permisos» es "
                       "justamente lo que resuelve el rol: se ajusta en un solo lugar.",
                    3: "**Correcta.** El alta de una mascota la hace otro rol, asi que recepcion "
                       "no necesita escribir en `dueno` ni en `mascota`; le basta leer para "
                       "identificar a quien llama. Cada privilegio que no se otorga es una "
                       "superficie de dano que no existe.",
                    4: "**Correcta.** Es el mecanismo de la pregunta 3. Si solo necesita nombre y "
                       "telefono, darle la tabla `dueno` completa le entrega tambien el correo y "
                       "la ciudad. La vista o el privilegio por columna entregan el dato sin el "
                       "resto.",
                    5: "**Incorrecta.** Y es la mas importante de descartar. Quien puede corregir "
                       "el registro de lo que hizo puede borrar la evidencia de lo que hizo: una "
                       "tabla de auditoria con `UPDATE` para el auditor no prueba nada. Un "
                       "registro erroneo se corrige con un registro nuevo que deja fecha y autor, "
                       "no editando el anterior.",
                },
                "como_calificar": [
                    "10 pts con las tres correctas (indices 1, 3 y 4) y ninguna incorrecta "
                    "marcada.",
                    "Parcial proporcional: 10/3 ≈ 3,33 por correcta marcada, menos 3,33 por cada "
                    "incorrecta marcada, con piso en 0. Quien marque las 6 saca 0, y eso es "
                    "deliberado: marcar todo no es responder.",
                    "Si alguien marca 0 y 1 a la vez, senale la contradiccion en voz alta: son "
                    "afirmaciones opuestas sobre la misma decision, y no se puede estar de acuerdo "
                    "con las dos.",
                ],
                "errores": [
                    "**Marcar la 5 «porque el auditor tiene que poder corregir errores».** Es la "
                    "trampa de la pregunta y la que mas cae. La respuesta es que corregir un "
                    "registro de auditoria destruye su valor como prueba.",
                    "**Marcar la 2 «porque asi no toca volver a tocar permisos».** Confunde "
                    "comodidad del administrador con necesidad del usuario. Es el argumento con el "
                    "que en la practica se llega a que todo el mundo sea administrador.",
                    "**Dudar entre 3 y 4 y marcar solo una.** No son alternativas: la 3 dice que "
                    "sobre `dueno` basta `SELECT`, y la 4 dice que incluso ese `SELECT` puede "
                    "recortarse a dos columnas. Son dos pasos del mismo razonamiento.",
                ],
            },
            {
                "n": 3, "titulo": "Reducir la superficie: vista de agenda y privilegios por columna",
                "tipo": "bd_sql", "puntos": 20,
                "sql": """-- =====================================================================
    -- 1) La vista recorta las dos dimensiones a la vez:
    --    filas  -> WHERE c.estado <> 'CANCELADA'
    --    columnas -> el email del dueno simplemente no esta en el SELECT
    -- =====================================================================
    CREATE VIEW v_agenda_recepcion AS
    SELECT c.id_cita,
           c.fecha_hora,
           c.estado,
           m.nombre  AS mascota,
           d.nombre  AS dueno,
           d.telefono,
           v.nombre  AS veterinario
      FROM cita c
      JOIN mascota     m ON m.id_mascota     = c.id_mascota
      JOIN dueno       d ON d.id_dueno       = m.id_dueno
      JOIN veterinario v ON v.id_veterinario = c.id_veterinario
     WHERE c.estado <> 'CANCELADA';

    GRANT SELECT ON v_agenda_recepcion TO recepcion;

    -- Y se le cierra la puerta directa: a partir de aqui recepcion llega al
    -- telefono del dueno UNICAMENTE a traves de la vista. Funciona porque la
    -- vista se ejecuta con los privilegios de su propietario, no de quien la
    -- consulta.
    REVOKE SELECT ON dueno FROM recepcion;

    -- =====================================================================
    -- 2) Privilegio por columna: mismo objetivo, sin crear objeto nuevo.
    -- =====================================================================
    GRANT SELECT (id_dueno, nombre) ON dueno TO veterinario_rol;

    -- =====================================================================
    -- 3) Verificacion
    -- =====================================================================
    SELECT * FROM v_agenda_recepcion ORDER BY fecha_hora;

    SELECT grantee, table_name, column_name, privilege_type
      FROM information_schema.column_privileges
     WHERE grantee = 'veterinario_rol'
       AND table_name = 'dueno'
     ORDER BY column_name;""",
                "salida": """SELECT * FROM v_agenda_recepcion ORDER BY fecha_hora;  -- 9 filas

     id_cita |     fecha_hora      |   estado   | mascota  |     dueno      |  telefono  |  veterinario
    ---------+---------------------+------------+----------+----------------+------------+----------------
           1 | 2026-09-01 08:00:00 | PROGRAMADA | Firulais | Ana Gomez      | 3001112233 | Laura Restrepo
           2 | 2026-09-01 09:00:00 | ATENDIDA   | Luna     | Ana Gomez      | 3001112233 | Laura Restrepo
           3 | 2026-09-01 10:00:00 | PROGRAMADA | Mishi    | Marcela Diaz   | 3027778899 | Diego Moreno
           5 | 2026-09-02 11:00:00 | ATENDIDA   | Nube     | Jorge Pineda   | 3105551212 | Diego Moreno
           6 | 2026-09-03 07:45:00 | PROGRAMADA | Toby     | Luisa Cardona  | 3123334455 | Ivan Ortiz
           7 | 2026-09-05 15:00:00 | ATENDIDA   | Firulais | Ana Gomez      | 3001112233 | Laura Restrepo
           8 | 2026-09-08 16:00:00 | PROGRAMADA | Luna     | Ana Gomez      | 3001112233 | Paula Salazar
           9 | 2026-09-10 08:00:00 | PROGRAMADA | Mishi    | Marcela Diaz   | 3027778899 | Ivan Ortiz
          10 | 2026-09-10 09:00:00 | ATENDIDA   | Nube     | Jorge Pineda   | 3105551212 | Laura Restrepo

    Son 9 de las 10 citas sembradas: falta la id_cita 4, que esta CANCELADA. Ese
    "9 y no 10" es la comprobacion de un solo golpe de que el WHERE quedo puesto.
    Notese tambien que no hay columna de email: la vista no lo expone.


    SELECT ... FROM information_schema.column_privileges ...  -- exactamente 2 filas

        grantee      | table_name | column_name | privilege_type
    -----------------+------------+-------------+----------------
     veterinario_rol | dueno      | id_dueno    | SELECT
     veterinario_rol | dueno      | nombre      | SELECT

    Si aparecen 4 o 6 filas, con telefono, email o ciudad, es que se otorgo la
    tabla completa y el recorte por columna no se hizo.""",
                "como_calificar": [
                    "**8 pts — la vista.** 4 pts por las 7 columnas con los alias pedidos "
                    "(`mascota`, `dueno`, `telefono`, `veterinario`), 2 pts por excluir el email y "
                    "2 pts por el `WHERE` que deja fuera las canceladas. El `SELECT` sobre la "
                    "vista devuelve 9 filas: si devuelve 10, falta el filtro; si devuelve mas de "
                    "10, hay un JOIN mal cerrado y se multiplicaron filas.",
                    "**4 pts — el traslado del acceso.** 2 pts por `GRANT SELECT ON "
                    "v_agenda_recepcion TO recepcion` y 2 pts por el `REVOKE SELECT ON dueno FROM "
                    "recepcion`. Los dos: dar la vista sin cerrar la tabla no reduce nada, porque "
                    "el rol sigue pudiendo leer el email por la puerta de al lado.",
                    "**5 pts — el privilegio por columna.** La forma exacta `GRANT SELECT "
                    "(id_dueno, nombre) ON dueno TO veterinario_rol`. Se descuenta todo si otorgo "
                    "la tabla completa, aunque despues escriba que «idealmente serian dos "
                    "columnas»: la pregunta es de implementacion.",
                    "**3 pts — las dos consultas de verificacion**, y que la segunda devuelva "
                    "exactamente las dos filas de arriba.",
                    "**Bono conceptual, sin puntos.** Si el estudiante escribe en un comentario "
                    "por que la vista funciona despues del `REVOKE` (se ejecuta con los "
                    "privilegios del propietario), tomelo como senal de que entendio el mecanismo "
                    "y no solo copio la sintaxis. Es el concepto central de la pregunta.",
                ],
                "errores": [
                    "**`WHERE c.estado != 'cancelada'` en minusculas.** No falla ni avisa: "
                    "devuelve las 10 filas porque ninguna coincide con el literal en minusculas, "
                    "y el estudiante cree que su filtro funciona. El `CHECK` de la tabla guarda "
                    "`'CANCELADA'` en mayusculas.",
                    "**`SELECT *` dentro de la vista.** Trae el email y la ciudad, que es "
                    "exactamente lo que la pregunta pide dejar fuera. Ademas la vista queda "
                    "amarrada a la forma de las tablas: si manana se agrega una columna sensible a "
                    "`dueno`, la vista la expone sola.",
                    "**Dar la vista y olvidar el `REVOKE`.** Es el error mas comun y el mas "
                    "invisible: todo corre, la vista se ve bien, y la superficie no se redujo ni "
                    "un poco.",
                    "**`GRANT SELECT ON dueno(id_dueno, nombre) TO veterinario_rol`.** Las "
                    "columnas van despues del privilegio, no despues de la tabla: `GRANT SELECT "
                    "(id_dueno, nombre) ON dueno`. Es un error de sintaxis, asi que al menos avisa.",
                    "**Esperar que `veterinario_rol` pueda hacer `SELECT * FROM dueno`.** No "
                    "puede, y esa es la consecuencia correcta del privilegio por columna: el "
                    "asterisco pide todas las columnas y dos de ellas le estan negadas. Tiene que "
                    "nombrarlas. Vale advertirlo antes de que alguien lo reporte como fallo.",
                    "**Crear la vista sin `veterinario` en el JOIN** y poner el `id_veterinario` "
                    "en bruto. La pregunta pide el nombre del veterinario: quien lee la agenda es "
                    "una persona en el mostrador, no un programa.",
                ],
            },
            {
                "n": 4, "titulo": "Matriz rol x objeto x privilegio de VetCare",
                "tipo": "abierta", "puntos": 25,
                "tabla": {
                    "headers": ["Objeto", "admin_bd", "recepcion", "veterinario_rol", "auditor"],
                    "rows": [
                        ["`dueno`", "S I U D", "- (vista)", "S (2 col.)", "S"],
                        ["`mascota`", "S I U D", "S", "S", "S"],
                        ["`veterinario`", "S I U D", "S", "-", "-"],
                        ["`cita`", "S I U D", "S I U", "S", "S"],
                        ["`consulta`", "S I U D", "-", "S I U", "S"],
                        ["`insumo`", "S I U D", "-", "-", "-"],
                        ["`factura`", "S I U D", "-", "-", "S"],
                        ["`detalle_factura`", "S I U D", "-", "-", "-"],
                        ["`sp_agendar_cita`", "E", "E", "-", "-"],
                        ["`sp_facturar`", "E", "-", "-", "-"],
                    ],
                },
                "respuesta": (
                    "La celda de `dueno` x `recepcion` es la unica que necesita nota al pie, y es "
                    "la que separa una matriz copiada de una razonada: **no es `-` a secas ni `S` "
                    "a secas**. Despues de la pregunta 3, `recepcion` no tiene `SELECT` sobre la "
                    "tabla `dueno` — se le revoco — pero si tiene `SELECT` sobre "
                    "`v_agenda_recepcion`, y por ahi llega al nombre y al telefono. Se acepta "
                    "escribirlo como `-` con la nota «solo via `v_agenda_recepcion`», o agregar la "
                    "vista como fila 11 de la matriz. Lo que no se acepta es `S`, porque "
                    "contradice el `REVOKE` que el propio estudiante ejecuto.\n\n"
                    "Las tres justificaciones que la pregunta pide (4 a 6 lineas en total):\n\n"
                    "1. **Ningun rol operativo tiene `D`.** En VetCare nada se borra: una cita "
                    "cancelada lleva `estado = 'CANCELADA'` y una mascota que ya no se atiende "
                    "lleva `activa = 'N'`. Como el borrado es logico, `DELETE` no le hace falta a "
                    "nadie que opere el dia a dia, y no otorgarlo elimina de raiz la perdida "
                    "accidental de informacion. Solo `admin_bd` lo conserva, y para tareas de "
                    "mantenimiento, no de operacion.\n"
                    "2. **`auditor` es de solo lectura, incluida la tabla de auditoria** que "
                    "llegara en la Clase 4. Quien puede corregir el registro de lo que hizo puede "
                    "borrar la evidencia de lo que hizo; un registro equivocado se corrige con uno "
                    "nuevo que deja fecha y autor.\n"
                    "3. **La aplicacion llegara por `E` y no por `I`.** `recepcion` tiene `E` "
                    "sobre `sp_agendar_cita` porque agendar no es «insertar una fila en `cita`»: "
                    "es insertarla *si* la mascota esta activa y *si* el veterinario tiene la "
                    "franja libre. Con `EXECUTE`, la regla vive una sola vez dentro de la base y "
                    "ninguna pantalla puede saltarsela. Ese es el patron que construye la Clase 3 "
                    "y que consume la Clase 12."
                ),
                "como_calificar": [
                    "**14 pts — la matriz completa.** Los 10 objetos x 4 roles, sin celdas "
                    "vacias, a razon de 1,4 pts por fila. El `-` cuenta como respuesta; la celda "
                    "en blanco, no.",
                    "**5 pts — consistencia con la pregunta 1.** Es el criterio duro y se revisa "
                    "comparando contra el script del estudiante, no contra esta tabla: si su "
                    "script no otorgo `DELETE` a nadie, en su matriz no puede haber una `D`; si le "
                    "dio `ALL PRIVILEGES` a `admin_bd` sobre 8 tablas, las 8 filas de esa columna "
                    "tienen que estar servidas. Una matriz internamente coherente con un script "
                    "distinto del de arriba se califica completa.",
                    "**3 pts — los procedimientos con `E`.** `sp_agendar_cita` y `sp_facturar` "
                    "aparecen con `E` y nunca con `S`, `I`, `U` o `D`. Es el error conceptual que "
                    "esta pregunta busca: un procedimiento no se consulta, se ejecuta.",
                    "**3 pts — la justificacion.** Tres decisiones concretas, cada una nombrando "
                    "privilegio minimo y el dano que evita. 1 pt por decision. No se dan puntos "
                    "por repetir la definicion del principio sin aplicarla a una celda de la "
                    "matriz.",
                    "**Descuentos.** −2 por cada rol con `ALL PRIVILEGES` sin justificar (aparte "
                    "de `admin_bd`, que si esta justificado). −1,4 por objeto omitido.",
                ],
                "errores": [
                    "**`admin_bd` con guiones en `dueno`, `mascota` y `veterinario`.** Es el "
                    "arrastre del error de la pregunta 1 y produce una matriz donde el "
                    "administrador de la base no puede leer a los clientes. Si aparece, la "
                    "correccion es en la pregunta 1 y la matriz se recalifica coherente.",
                    "**Poner `S` en `dueno` x `recepcion`.** Contradice el `REVOKE` de la pregunta "
                    "3. Es la celda que revela si el estudiante armo la matriz mirando su propio "
                    "script o copiandola de la teoria.",
                    "**`sp_agendar_cita` con `I` «porque inserta una cita».** Confunde lo que el "
                    "procedimiento hace por dentro con el privilegio que necesita quien lo llama. "
                    "El rol solo necesita `EXECUTE`; el `INSERT` lo hace el procedimiento con los "
                    "privilegios de su propietario, que es precisamente la gracia.",
                    "**Dar `S` sobre `insumo` y `detalle_factura` a `auditor` «porque audita "
                    "todo».** Aqui hay que ser justo: es una decision defendible y no un error, "
                    "siempre que su script de la pregunta 1 lo haya otorgado. Si la matriz dice "
                    "`S` y el script no lo otorgo, el problema es la inconsistencia, no la "
                    "decision.",
                    "**Justificar con la definicion en vez de con el caso.** «Aplicamos "
                    "privilegio minimo porque cada rol debe tener solo lo necesario» no dice nada "
                    "sobre VetCare. Se pide nombrar la celda y el dano que evita.",
                ],
            },
            {
                "n": 5, "titulo": "Politica de altas y bajas de usuarios (y la prueba negativa)",
                "tipo": "abierta", "puntos": 15,
                "respuesta": (
                    "Version de referencia, en una pagina. Lo que se califica no es la redaccion "
                    "sino que **haya responsables y plazos concretos**: «el administrador» y «lo "
                    "antes posible» no son respuestas.\n\n"
                    "**1. Alta.** La solicita el jefe del area donde entra la persona (recepcion, "
                    "clinica o administracion) por correo a la coordinacion. La aprueba la "
                    "administradora de la clinica, que es la unica que decide quien entra a la "
                    "base. La ejecuta el `admin_bd` creando un rol con `LOGIN` y otorgandole "
                    "**exactamente uno** de los cuatro roles del negocio segun el cargo; por "
                    "omision, `recepcion` para el personal de mostrador. La credencial inicial se "
                    "entrega en persona o por un canal distinto del correo con el que se pidio, es "
                    "temporal, y el sistema exige cambiarla en el primer ingreso. Caduca a las 72 "
                    "horas si no se usa, y en ese caso hay que volver a solicitarla.\n\n"
                    "**2. Cambio de rol.** Una recepcionista que pasa a auxiliar veterinaria "
                    "recibe `GRANT veterinario_rol TO ana_gomez` y — esto es lo que se califica — "
                    "**pierde el anterior** con `REVOKE recepcion FROM ana_gomez`, el mismo dia y "
                    "en la misma solicitud. Los permisos no se acumulan: quien conserva los dos "
                    "roles termina pudiendo hacer las dos mitades de un proceso que se separo a "
                    "proposito. La solicitud la firma el jefe que la recibe y la nota el jefe que "
                    "la entrega, para que ninguno de los dos asuma que el otro pidio la "
                    "revocacion.\n\n"
                    "**3. Baja.** El mismo dia de la desvinculacion, y antes de que la persona "
                    "salga del edificio: (a) `REVOKE` de todos los roles del negocio; (b) "
                    "`ALTER ROLE ana_gomez NOLOGIN` para cerrar el acceso sin destruir nada; (c) "
                    "los objetos que la persona era dueno se reasignan con `REASSIGN OWNED BY "
                    "ana_gomez TO admin_bd`, porque PostgreSQL no permite `DROP ROLE` de un rol "
                    "que todavia posee objetos, y porque una vista o un procedimiento que "
                    "desaparece con su autor rompe la aplicacion; (d) el rol se conserva "
                    "deshabilitado, **no se borra**, durante los cinco anos de retencion de la "
                    "traza clinica, para que los registros de auditoria sigan apuntando a un "
                    "nombre y no a un identificador huerfano.\n\n"
                    "**4. Revision periodica.** Cada tres meses, el primer lunes del trimestre. La "
                    "evidencia es la salida de `SELECT grantee, table_name, privilege_type FROM "
                    "information_schema.role_table_grants WHERE grantee IN "
                    "('admin_bd','recepcion','veterinario_rol','auditor') ORDER BY 1,2,3`, mas "
                    "`information_schema.column_privileges` para los recortes por columna, y se "
                    "compara contra la matriz aprobada. Firma la administradora de la clinica; el "
                    "`admin_bd` prepara la evidencia pero no se autoaprueba, porque eso rompe la "
                    "separacion de funciones que la matriz defiende. Toda diferencia se corrige o "
                    "se documenta como excepcion con fecha de vencimiento.\n\n"
                    "**5. Prueba negativa y limite del entorno.** En ExamLab la base es PostgreSQL "
                    "corriendo en el navegador (PGlite), con **una sola sesion y un solo usuario "
                    "de conexion**. Eso no impide la prueba negativa, y aqui esta corrida: `SET "
                    "ROLE recepcion;` cambia el rol efectivo de la sesion, y desde esa linea el "
                    "motor evalua los permisos como `recepcion`. Entonces `DELETE FROM cita WHERE "
                    "id_cita = 1;` responde `ERROR: permission denied for table cita`, y `RESET "
                    "ROLE;` devuelve la sesion al rol propietario. El limite real es otro, y "
                    "conviene decirlo con precision: `SET ROLE` cambia el rol **dentro** de la "
                    "sesion ya abierta, no abre una sesion nueva; los cuatro roles se crearon "
                    "`NOLOGIN` justamente porque son paquetes de permisos y no identidades de "
                    "conexion, asi que lo que ExamLab no permite probar es el **login** de "
                    "`recepcion` ni la concurrencia entre dos personas. Lo que si quedo demostrado "
                    "es lo que importa de la pregunta 1: que el motor **hace cumplir** la matriz, "
                    "no solo que esta escrita. Y si en la maquina de alguien el `SET ROLE` "
                    "fallara, ese mensaje se pega tal cual y ahi si aparece la brecha de "
                    "verificacion: se habria comprobado la configuracion y no el cumplimiento."
                ),
                "como_calificar": [
                    "**8 pts — las cinco secciones, con responsable y plazo.** 1,6 por seccion. "
                    "Se descuenta la mitad de la seccion cuando dice que hay que hacer algo pero "
                    "no dice quien ni cuando: una politica sin responsable no es ejecutable.",
                    "**2 pts — el cambio de rol incluye la revocacion del anterior.** Es el punto "
                    "que separa una politica pensada de una lista de buenas intenciones. Si solo "
                    "dice que se otorga el nuevo, no se dan.",
                    "**2 pts — la baja resuelve el destino de los objetos** (`REASSIGN OWNED` o "
                    "equivalente razonado) y dice cuanto se conserva la traza.",
                    "**3 pts — la seccion 5.** 1 pt por la prueba negativa corrida (`SET ROLE`, la "
                    "sentencia que fallo, `RESET ROLE`), 1 pt por el mensaje del motor pegado "
                    "literal — `permission denied for table cita` — y no parafraseado, y 1 pt por "
                    "distinguir `SET ROLE` de conectarse como otro usuario y nombrar el limite "
                    "verdadero del entorno: un solo usuario de conexion, sin login de `recepcion` "
                    "ni concurrencia. Si el `SET ROLE` le fallo y pego el mensaje mas la brecha de "
                    "verificacion, se dan los 3 igual: lo que se califica es que haya intentado "
                    "comprobar y haya reportado lo que vio.",
                    "**Extension.** Una pagina es el techo, no la meta. Tres parrafos que "
                    "resuelven las cinco secciones valen mas que dos paginas de generalidades, y "
                    "no se descuenta por brevedad si esta todo.",
                ],
                "errores": [
                    "**«El administrador revisa los permisos periodicamente».** No tiene "
                    "responsable con nombre de cargo, no tiene periodo y no tiene evidencia. Es la "
                    "forma mas comun de entregar esta pregunta y no vale los puntos de la seccion "
                    "4.",
                    "**Decir que en la baja se hace `DROP ROLE` y listo.** Falla en el motor si el "
                    "rol posee objetos, y destruye la trazabilidad de la auditoria. La respuesta "
                    "correcta es deshabilitar, reasignar y conservar.",
                    "**Escribir en la seccion 5 que «en ExamLab no se pueden crear roles ni "
                    "otorgar privilegios».** Es la limitacion equivocada, y ademas contradice las "
                    "preguntas 1 y 3, que el propio estudiante acaba de ejecutar. Casi siempre "
                    "viene de leer material de otro motor.",
                    "**Proponer como prueba negativa «abrir otra pestana y entrar como "
                    "recepcion».** No sirve: no hay segundo usuario ni segunda sesion. Lo que se "
                    "pide es el comando concreto de PostgreSQL, y es `SET ROLE`.",
                    "**Afirmar que «en ExamLab no se puede hacer la prueba negativa» sin haberla "
                    "intentado.** Es falso, y hay que saberlo antes de calificar: PGlite conecta "
                    "como el superusuario `postgres`, asi que `SET ROLE recepcion;` funciona y el "
                    "`DELETE` rebota de verdad. Si la entrega lo afirma, se le pide la corrida; "
                    "sin evidencia no hay seccion 5.",
                    "**Correr el `SET ROLE` y olvidar el `RESET ROLE;`.** Todo lo que el "
                    "estudiante escriba despues se sigue ejecutando como `recepcion` y falla por "
                    "una razon que no es la del ejercicio. Cuando alguien reporta que «se le "
                    "rompio el resto del taller», es esto casi siempre.",
                    "**Permitir cuentas compartidas** («la cuenta recepcion1 la usan las tres "
                    "recepcionistas»). Rompe toda la auditoria de la Clase 4 antes de escribirla: "
                    "el disparador registrara siempre el mismo nombre y ninguna investigacion "
                    "posterior podra atribuir un cambio a una persona.",
                ],
            },
        ],
        "preguntas_frecuentes": [
            ("Ejecute el GRANT y no surtio efecto. ¿Por que?",
             "Casi siempre es una de cuatro cosas, en este orden de frecuencia: (1) se otorgo el "
             "privilegio al rol pero no se otorgo el rol a la persona, y falta el `GRANT recepcion "
             "TO ana_gomez`; (2) se esta «comprobando» en la misma sesion del propietario, que pasa "
             "por encima de todos los permisos y por lo tanto nunca vera un error; (3) el rol no "
             "tiene `USAGE` sobre el esquema — en `public` viene por omision, asi que hoy no "
             "estorba, pero en un servidor real es la causa numero uno; (4) el nombre se escribio "
             "entre comillas dobles, y `\"Recepcion\"` no es `recepcion`."),
            ("¿ExamLab me va a dejar hacer CREATE ROLE?",
             "Si. Es PostgreSQL real en el navegador y el DDL de permisos funciona completo. Lo "
             "unico que no hay es una segunda sesion. Si un estudiante llega diciendo que no puede, "
             "revise el mensaje de error real antes de aceptar la premisa: normalmente es un rol "
             "que ya existia de un intento anterior, y se resuelve con `DROP ROLE` o volviendo a "
             "cargar el ejercicio."),
            ("Si le doy SELECT solo a la vista, ¿no necesita tambien SELECT sobre dueno?",
             "No, y es el concepto central de la clase: la consulta de la vista se ejecuta con los "
             "privilegios de su **propietario**, no con los de quien la consulta. Por eso se puede "
             "dar la vista y revocar la tabla en el mismo script, y el rol sigue viendo el telefono "
             "pero ya no el correo."),
            ("¿Puedo demostrar que a recepcion le rebota el DELETE?",
             "Si, y sin abrir otra conexion: `SET ROLE recepcion;` y luego `DELETE FROM cita WHERE "
             "id_cita = 1;`, que debe responder `permission denied for table cita`; se vuelve con "
             "`RESET ROLE;`. Funciona en ExamLab porque PGlite conecta como superusuario y `SET "
             "ROLE` cambia el rol efectivo de la sesion, no la conexion. Lo que no se puede es "
             "conectarse *como* `recepcion`: hay un solo usuario de conexion y, de hecho, los "
             "cuatro roles se crearon `NOLOGIN`. Esa es la respuesta que vale puntos en la "
             "pregunta 5."),
            ("¿Rol y usuario son lo mismo?",
             "En PostgreSQL si: un usuario es un rol con el atributo `LOGIN`, y `CREATE USER` es "
             "literalmente un alias de `CREATE ROLE ... LOGIN`. Por eso los cuatro roles del taller "
             "se crean con `NOLOGIN`: son paquetes de permisos, no identidades con las que alguien "
             "se conecte."),
            ("¿Por que el rol se llama veterinario_rol y no veterinario?",
             "Por legibilidad, no por obligacion del motor. En PostgreSQL los roles son globales al "
             "cluster y las tablas viven en un esquema, asi que un rol `veterinario` y una tabla "
             "`veterinario` pueden coexistir sin problema. Pero en la linea `GRANT SELECT ON cita "
             "TO veterinario` nadie puede saber a simple vista si eso es un rol o un error, y el "
             "sufijo lo resuelve. Conviene dar esta respuesta completa: un estudiante despierto va "
             "a preguntar y merece la razon verdadera."),
            ("¿El REVOKE de DELETE no es inutil si nunca se otorgo?",
             "Tecnicamente si es redundante, y decirlo esta bien. Se escribe porque es la evidencia "
             "documental de la decision: quien lea el script en seis meses tiene que poder "
             "distinguir «aqui se decidio que recepcion no borra» de «aqui se olvidaron de darle "
             "DELETE». Vale los 3 puntos igual."),
            ("¿La matriz va en el mismo ExamLab o en un documento aparte?",
             "En ExamLab, en la respuesta de la pregunta 4, como tabla markdown. El documento "
             "`Roles_VetCare` de la carpeta del PI es la misma matriz mas la politica, y sirve para "
             "que el estudiante conserve su trabajo; lo que se califica es lo que esta en la "
             "plataforma."),
        ],
        "cierre": [
            "Al terminar, cada estudiante debe tener: el script de los 4 roles corriendo con su "
            "consulta de verificacion, la vista `v_agenda_recepcion` con el `REVOKE` que la hace "
            "necesaria, el privilegio por columna evidenciado en `column_privileges`, la matriz de "
            "10 objetos x 4 roles consistente con su propio script, y la politica de una pagina.",
            "Lo que hay que verificar antes de cerrar la sesion es la **consistencia entre la "
            "pregunta 1 y la pregunta 4**: son la misma decision escrita dos veces, en SQL y en "
            "tabla, y la mitad de las entregas flojas se detecta comparandolas. Proyecte una "
            "entrega voluntaria y haga esa comparacion en vivo.",
            "Dejar dicho en voz alta lo que sigue: en la Clase 3 el rol `recepcion` va a perder el "
            "`INSERT` directo sobre `cita` y va a recibir `EXECUTE` sobre `sp_agendar_cita`. La "
            "matriz de hoy no es definitiva, es la primera version de un documento que el PI va a "
            "revisar dos veces mas.",
        ],
    },

    3: {
        "titulo": "Solucion del taller · Clase 3 · Procedimientos almacenados de VetCare en PL/pgSQL",
        "resumen": (
            "Los dos procedimientos de negocio del PI escritos en PL/pgSQL y corriendo: "
            "`sp_agendar_cita` con sus tres validaciones y `sp_registrar_consulta` con sus cuatro, "
            "la bateria de pruebas que demuestra que las validaciones no dejan basura en la tabla, "
            "la distincion entre PROCEDURE y FUNCTION resuelta con el criterio correcto, y el "
            "contrato de los dos procedimientos documentado tal como lo consumira la aplicacion "
            "de Huellitas."
        ),
        "total": 100,
        "nota_actividad": (
            "**El motor es PostgreSQL, no Oracle,** y en esta clase la diferencia se paga caro: "
            "tres de las cinco preguntas son SQL que corre. La sintaxis es "
            "`CREATE PROCEDURE ... LANGUAGE plpgsql AS $proc$ ... $proc$;` y no lleva `IS`, ni "
            "`VARCHAR2`, ni `NUMBER`, ni `RAISE_APPLICATION_ERROR`, ni la barra `/` final. "
            "`RAISE EXCEPTION 'texto %', variable;` es el equivalente exacto de "
            "`RAISE_APPLICATION_ERROR`. Un detalle del entorno que conviene anunciar antes de "
            "arrancar: en ExamLab **cada pregunta arranca con su propia base sembrada**, asi que "
            "la pregunta 2 ya trae `sp_agendar_cita` creado —la version de referencia— y el "
            "estudiante no depende de que su pregunta 1 haya quedado bien. Y una recomendacion "
            "que ahorra la mitad de los reportes de error: escribir "
            "`CREATE OR REPLACE PROCEDURE`, para que el segundo intento no choque con «ya "
            "existe»."
        ),
        "preguntas": [
            {
                "n": 1,
                "titulo": "Implementar sp_agendar_cita en PL/pgSQL",
                "tipo": "bd_sql",
                "puntos": 35,
                "sql": """-- =====================================================================
    -- sp_agendar_cita: la regla de negocio del PI, escrita una sola vez y
    -- dentro de la base. OR REPLACE para poder corregir y volver a ejecutar
    -- sin borrar antes.
    -- =====================================================================
    CREATE OR REPLACE PROCEDURE sp_agendar_cita(
      p_id_mascota     INT,
      p_id_veterinario INT,
      p_fecha_hora     TIMESTAMP
    )
    LANGUAGE plpgsql
    AS $proc$
    DECLARE
      v_activa  CHAR(1);
      v_ocupado INT;
    BEGIN
      -- 1) ¿Existe la mascota? El SELECT ... INTO deja FOUND en falso cuando no
      --    devolvio ninguna fila, y es la unica forma limpia de distinguir
      --    "no existe" de "existe y esta inactiva". Ojo: esto solo funciona
      --    porque el SELECT trae una columna, no un COUNT.
      SELECT activa INTO v_activa
        FROM mascota
       WHERE id_mascota = p_id_mascota;

      IF NOT FOUND THEN
        RAISE EXCEPTION 'ERROR: la mascota % no existe', p_id_mascota;
      END IF;

      -- 2) La regla de negocio del PI: una mascota inactiva no agenda. Se
      --    escribe <> 'S' y no = 'N' a proposito: si manana el CHECK admite
      --    un tercer estado, la regla sigue siendo correcta sin tocarla.
      IF v_activa <> 'S' THEN
        RAISE EXCEPTION 'ERROR: la mascota % esta inactiva; no se agenda cita',
                        p_id_mascota;
      END IF;

      -- 3) ¿El veterinario tiene la franja libre? Una cita CANCELADA libera la
      --    franja, por eso se excluye del conteo. Aqui NO se puede usar
      --    IF NOT FOUND: un COUNT(*) siempre devuelve una fila, asi que FOUND
      --    seria verdadero incluso con cero citas. Se compara el numero.
      SELECT COUNT(*) INTO v_ocupado
        FROM cita
       WHERE id_veterinario = p_id_veterinario
         AND fecha_hora     = p_fecha_hora
         AND estado        <> 'CANCELADA';

      IF v_ocupado > 0 THEN
        RAISE EXCEPTION 'ERROR: el veterinario % ya tiene cita en %',
                        p_id_veterinario, p_fecha_hora;
      END IF;

      -- 4) Caso valido. El estado se escribe explicito aunque la tabla lo
      --    tenga por omision: el procedimiento es el contrato y no debe
      --    depender de un DEFAULT que alguien puede cambiar manana.
      INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, estado)
      VALUES (p_id_mascota, p_id_veterinario, p_fecha_hora, 'PROGRAMADA');
    END;
    $proc$;

    -- =====================================================================
    -- Demostracion pedida por el enunciado: el caso valido.
    -- =====================================================================
    CALL sp_agendar_cita(1, 2, TIMESTAMP '2026-09-15 10:00:00');

    SELECT id_cita, id_mascota, id_veterinario, fecha_hora, estado
      FROM cita
     ORDER BY id_cita DESC
     LIMIT 3;""",
                "salida": """CALL sp_agendar_cita(1, 2, TIMESTAMP '2026-09-15 10:00:00');   -- CALL, sin filas devueltas

    SELECT id_cita, id_mascota, id_veterinario, fecha_hora, estado ...   -- 3 filas

     id_cita | id_mascota | id_veterinario |     fecha_hora      |   estado
    ---------+------------+----------------+---------------------+-------------
          11 |          1 |              2 | 2026-09-15 10:00:00 | PROGRAMADA
          10 |          6 |              1 | 2026-09-10 09:00:00 | ATENDIDA
           9 |          4 |              4 | 2026-09-10 08:00:00 | PROGRAMADA

    La comprobacion de un golpe es el 11: la base venia con 10 citas sembradas,
    asi que el id 11 y el estado PROGRAMADA en la primera fila demuestran que el
    procedimiento inserto y que lo hizo con el estado correcto. Si la primera fila
    dice 10, el CALL no inserto nada y hay que revisar si alguna validacion esta
    disparando de mas.

    Las tres excepciones, para pegarlas al revisar una entrega dudosa (cada una
    aborta el script, por eso van de a una):

      CALL sp_agendar_cita(99, 2, TIMESTAMP '2026-09-16 10:00:00');
      -- ERROR:  ERROR: la mascota 99 no existe

      CALL sp_agendar_cita(3, 2, TIMESTAMP '2026-09-16 10:00:00');
      -- ERROR:  ERROR: la mascota 3 esta inactiva; no se agenda cita

      CALL sp_agendar_cita(2, 1, TIMESTAMP '2026-09-01 08:00:00');
      -- ERROR:  ERROR: el veterinario 1 ya tiene cita en 2026-09-01 08:00:00

    Y la que confirma que CANCELADA libera la franja: el veterinario 3 tiene la cita
    4 CANCELADA el 2026-09-02 08:30:00, asi que esta debe funcionar.

      CALL sp_agendar_cita(1, 3, TIMESTAMP '2026-09-02 08:30:00');
      -- CALL (sin error): inserta la cita 12""",
                "como_calificar": [
                    "**6 pts — el procedimiento se crea sin error.** `CREATE PROCEDURE` (o "
                    "`CREATE OR REPLACE PROCEDURE`) con `LANGUAGE plpgsql`, dollar-quoting y los "
                    "**3 parametros en el orden y con los tipos pedidos**: `INT`, `INT`, "
                    "`TIMESTAMP`. Es el piso de la pregunta: si el motor no lo acepta, los 21 pts "
                    "de las validaciones no se pueden evaluar.",
                    "**21 pts — las tres validaciones, 7 pts cada una.** Por validacion: 4 pts "
                    "que la condicion sea la correcta, 2 pts el `RAISE EXCEPTION` y 1 pt que el "
                    "mensaje sea informativo, es decir que incluya el valor con `%`. La tercera "
                    "es la que mas se pierde: tiene que excluir `'CANCELADA'`, porque una cita "
                    "cancelada **libera** la franja.",
                    "**5 pts — el `INSERT` del caso valido** con estado `'PROGRAMADA'` y en las 4 "
                    "columnas. Se descuentan 2 si el estado se deja al `DEFAULT` de la tabla en "
                    "vez de escribirlo: funciona, pero el procedimiento deja de ser "
                    "autocontenido.",
                    "**3 pts — la demostracion.** El `CALL` corre y el `SELECT` final evidencia "
                    "la fila nueva. La verificacion es la de la salida de arriba: `id_cita = 11` "
                    "en la primera fila. Un `SELECT` que no muestre la cita nueva no evidencia "
                    "nada.",
                    "**Cero sintaxis Oracle.** Es explicito en la rubrica y se aplica sobre los "
                    "6 pts del primer renglon: `IS` en vez de `AS`, `VARCHAR2`, `NUMBER`, "
                    "`RAISE_APPLICATION_ERROR` o `/` final impiden que el motor cree el "
                    "procedimiento, asi que el efecto es automatico. No hace falta un descuento "
                    "aparte.",
                    "**Bono conceptual, sin puntos, y vale la pena buscarlo:** si el estudiante "
                    "escribe en un comentario que la validacion 3 **no** garantiza la unicidad "
                    "con dos sesiones simultaneas —dos llamadas pueden contar cero al mismo "
                    "tiempo y las dos insertar—, entendio el limite real de validar leyendo antes "
                    "de escribir. Es el problema que abre la Clase 10 y se resuelve con una "
                    "restriccion unica, no con mas `IF`.",
                ],
                "errores": [
                    "**`IF NOT FOUND` despues de un `SELECT COUNT(*) INTO`.** No falla, no avisa, "
                    "y la validacion queda muerta: un `COUNT` siempre devuelve una fila, asi que "
                    "`FOUND` es verdadero incluso cuando el conteo es cero. Es el error mas fino "
                    "de la pregunta y el que hay que explicar en voz alta al grupo entero: "
                    "`FOUND` sirve con `SELECT columna INTO`, no con agregados.",
                    "**Olvidar `AND estado <> 'CANCELADA'`** en la validacion del veterinario. La "
                    "consecuencia es que una franja cancelada queda bloqueada para siempre y la "
                    "clinica pierde una hora de agenda por cada cancelacion. Se detecta con el "
                    "`CALL` del veterinario 3 el `2026-09-02 08:30:00`, que debe funcionar.",
                    "**`RAISE EXCEPTION 'ERROR: la mascota ' || p_id_mascota || ' no existe';`** "
                    "Concatenar en vez de usar `%`. Funciona, pero se descuenta el punto del "
                    "mensaje informativo si la concatenacion falla con `NULL`: cualquier "
                    "concatenacion con `NULL` da `NULL` y el mensaje sale vacio. Con `%` el motor "
                    "imprime `<NULL>` y el mensaje sigue siendo legible.",
                    "**Validar el veterinario antes que la mascota** o mezclar las tres "
                    "condiciones en un solo `IF ... OR ...`. Corre, pero el mensaje ya no dice "
                    "cual regla se violo, y la aplicacion de la Clase 12 no puede decidir que "
                    "hacer. El orden del enunciado es el orden en que la recepcionista necesita "
                    "las respuestas.",
                    "**Comprobar la existencia con `SELECT COUNT(*) INTO v_existe` y luego el "
                    "estado con un segundo `SELECT`.** No esta mal y no se descuenta, pero son dos "
                    "viajes a la tabla para una sola pregunta. Vale senalar la version de arriba: "
                    "un `SELECT activa INTO` resuelve existencia y estado a la vez.",
                    "**Terminar el bloque con `/`** o abrirlo con `AS $$ DECLARE ... BEGIN ... "
                    "END; $$` sin etiqueta. La barra es de la consola de Oracle y aqui es un error "
                    "de sintaxis; `$$` sin etiqueta funciona, pero `$proc$` es mas seguro cuando "
                    "el cuerpo contiene a su vez cadenas con `$`.",
                ],
            },
            {
                "n": 2,
                "titulo": "Bateria de pruebas del procedimiento (caso OK + casos de error)",
                "tipo": "bd_sql",
                "puntos": 25,
                "sql": """-- =====================================================================
    -- P1 - CASO VALIDO: mascota 1 (Firulais, activa), vet 2, franja libre.
    -- Aqui el exito es que NO haya excepcion.
    -- =====================================================================
    DO $$
    BEGIN
      CALL sp_agendar_cita(1, 2, TIMESTAMP '2026-09-20 08:00:00');
      INSERT INTO resultado_prueba (caso, esperado, obtenido, paso)
      VALUES ('P1 mascota activa', 'OK: cita creada', 'OK: cita creada', TRUE);
    EXCEPTION WHEN OTHERS THEN
      INSERT INTO resultado_prueba (caso, esperado, obtenido, paso)
      VALUES ('P1 mascota activa', 'OK: cita creada', SQLERRM, FALSE);
    END $$;

    -- =====================================================================
    -- P2 - MASCOTA INACTIVA: mascota 3 (Rocky). Aqui el exito es que SI haya
    -- excepcion, y ademas que sea LA excepcion esperada. Por eso no basta
    -- WHEN OTHERS: se verifica el texto. Si el procedimiento fallara por
    -- cualquier otra razon -- un typo en el nombre de una columna -- un
    -- WHEN OTHERS a secas lo reportaria como prueba superada.
    -- =====================================================================
    DO $$
    BEGIN
      CALL sp_agendar_cita(3, 2, TIMESTAMP '2026-09-21 08:00:00');
      INSERT INTO resultado_prueba (caso, esperado, obtenido, paso)
      VALUES ('P2 mascota inactiva', 'EXCEPCION: mascota inactiva',
              'NO lanzo excepcion: la cita se creo', FALSE);
    EXCEPTION WHEN OTHERS THEN
      INSERT INTO resultado_prueba (caso, esperado, obtenido, paso)
      VALUES ('P2 mascota inactiva', 'EXCEPCION: mascota inactiva',
              SQLERRM, SQLERRM ILIKE '%inactiva%');
    END $$;

    -- =====================================================================
    -- P3 - MASCOTA INEXISTENTE: id 99.
    -- =====================================================================
    DO $$
    BEGIN
      CALL sp_agendar_cita(99, 2, TIMESTAMP '2026-09-22 08:00:00');
      INSERT INTO resultado_prueba (caso, esperado, obtenido, paso)
      VALUES ('P3 mascota inexistente', 'EXCEPCION: mascota no existe',
              'NO lanzo excepcion: la cita se creo', FALSE);
    EXCEPTION WHEN OTHERS THEN
      INSERT INTO resultado_prueba (caso, esperado, obtenido, paso)
      VALUES ('P3 mascota inexistente', 'EXCEPCION: mascota no existe',
              SQLERRM, SQLERRM ILIKE '%no existe%');
    END $$;

    -- =====================================================================
    -- P4 - VETERINARIO OCUPADO: vet 1 el 2026-09-01 08:00:00, franja que la
    -- cita 1 ya tiene PROGRAMADA.
    -- =====================================================================
    DO $$
    BEGIN
      CALL sp_agendar_cita(2, 1, TIMESTAMP '2026-09-01 08:00:00');
      INSERT INTO resultado_prueba (caso, esperado, obtenido, paso)
      VALUES ('P4 veterinario ocupado', 'EXCEPCION: veterinario ocupado',
              'NO lanzo excepcion: la cita se creo', FALSE);
    EXCEPTION WHEN OTHERS THEN
      INSERT INTO resultado_prueba (caso, esperado, obtenido, paso)
      VALUES ('P4 veterinario ocupado', 'EXCEPCION: veterinario ocupado',
              SQLERRM, SQLERRM ILIKE '%ya tiene cita%');
    END $$;

    -- =====================================================================
    -- CIERRE 1: el tablero de la bateria.
    -- =====================================================================
    SELECT caso, esperado, obtenido, paso
      FROM resultado_prueba
     ORDER BY id_prueba;

    -- =====================================================================
    -- CIERRE 2: la prueba de que las validaciones no dejaron basura. Se mira
    -- el total y, sobre todo, los tres conteos que deben dar cero.
    -- =====================================================================
    SELECT (SELECT COUNT(*) FROM cita)                                AS citas_totales,
           (SELECT COUNT(*) FROM cita
             WHERE fecha_hora = TIMESTAMP '2026-09-20 08:00:00')      AS de_p1_debe_ser_1,
           (SELECT COUNT(*) FROM cita WHERE id_mascota = 3)           AS de_p2_debe_ser_0,
           (SELECT COUNT(*) FROM cita
             WHERE fecha_hora = TIMESTAMP '2026-09-22 08:00:00')      AS de_p3_debe_ser_0,
           (SELECT COUNT(*) FROM cita
             WHERE id_veterinario = 1
               AND fecha_hora = TIMESTAMP '2026-09-01 08:00:00')      AS de_p4_debe_ser_1;""",
                "salida": """SELECT caso, esperado, obtenido, paso FROM resultado_prueba ORDER BY id_prueba;  -- 4 filas

              caso          |           esperado            |                        obtenido                         | paso
    ------------------------+-------------------------------+---------------------------------------------------------+------
     P1 mascota activa      | OK: cita creada               | OK: cita creada                                         | t
     P2 mascota inactiva    | EXCEPCION: mascota inactiva   | ERROR: la mascota 3 esta inactiva; no se agenda cita     | t
     P3 mascota inexistente | EXCEPCION: mascota no existe  | ERROR: la mascota 99 no existe                          | t
     P4 veterinario ocupado | EXCEPCION: veterinario ocupado| ERROR: el veterinario 1 ya tiene cita en 2026-09-01 ...  | t

    SELECT ... conteos ...  -- 1 fila

     citas_totales | de_p1_debe_ser_1 | de_p2_debe_ser_0 | de_p3_debe_ser_0 | de_p4_debe_ser_1
    ---------------+------------------+------------------+------------------+------------------
                11 |                1 |                0 |                0 |                1

    Los cuatro numeros de la derecha son la respuesta a la pregunta del enunciado
    -- "las 3 pruebas negativas no dejaron basura" -- y son mas fuertes que el
    total: 11 = 10 sembradas + 1 de P1; cero citas de Rocky (P2 no inserto); cero
    citas el 22 de septiembre (P3 no inserto); y 1, no 2, en la franja del
    veterinario 1 el 1 de septiembre, que es lo que demuestra que P4 no duplico.

    Sobre la columna `paso`: aqui las 4 filas quedan en «t» porque `paso` se
    definio como "el resultado coincidio con lo esperado", y en las pruebas
    negativas lo esperado ES la excepcion. Es la semantica que usa cualquier
    framework de pruebas. La plantilla del enunciado deja las negativas en `f`,
    leyendo `paso` como "la operacion se completo": tambien es correcta y vale los
    mismos puntos, siempre que el estudiante escriba cual de las dos usa. Lo
    que no se acepta es que las cuatro filas digan `t` sin haber verificado el
    texto de la excepcion, porque entonces `paso` no significa nada.""",
                "como_calificar": [
                    "**16 pts — los cuatro bloques `DO`, 4 pts cada uno.** Por bloque: 2 pts que "
                    "el `CALL` sea el del caso pedido (mascota, veterinario y franja exactos), "
                    "1 pt el manejador `EXCEPTION` que evita que el script aborte, y 1 pt la fila "
                    "registrada en `resultado_prueba` con `SQLERRM` en los negativos. **El "
                    "criterio duro es que el script llegue hasta el final:** si se cae en el "
                    "segundo bloque, los bloques que no corrieron no se califican.",
                    "**4 pts — la semantica de `paso` es coherente y esta declarada.** Se acepta "
                    "cualquiera de las dos lecturas —«coincidio con lo esperado» o «la operacion "
                    "se completo»—; lo que se exige es que la misma regla valga para las 4 filas y "
                    "que el estudiante diga cual eligio, en un comentario o en la columna "
                    "`esperado`.",
                    "**3 pts — la primera consulta de cierre** devuelve las 4 filas con las 4 "
                    "columnas y `ORDER BY id_prueba`. Es la pregunta mas facil de la bateria y se "
                    "pierde por olvido.",
                    "**2 pts — la segunda consulta de cierre** demuestra que `cita` paso de 10 a "
                    "11 filas. Se dan los 2 pts con un `COUNT(*)` simple; la version con los "
                    "cuatro conteos por caso es mejor y vale la pena senalarla como referencia, "
                    "porque un total de 11 tambien saldria si P1 hubiera fallado y P2 hubiera "
                    "insertado.",
                    "**Se descuenta si el script se cae** por no capturar la excepcion, tal como "
                    "dice la rubrica. El sintoma es inconfundible: `resultado_prueba` queda con "
                    "menos de 4 filas y el error del motor aparece en pantalla.",
                    "**Bono conceptual, sin puntos:** quien verifique el **texto** de la excepcion "
                    "(`SQLERRM ILIKE '%inactiva%'`) en vez de aceptar cualquier fallo entendio "
                    "para que sirve una prueba negativa. Es la diferencia entre probar y "
                    "aparentar que se probo.",
                ],
                "errores": [
                    "**Escribir los cuatro `CALL` seguidos, sin bloques `DO`.** El script se cae "
                    "en el segundo y las pruebas 3 y 4 nunca corren. Es el error que la rubrica "
                    "castiga explicitamente, y el sintoma es que `resultado_prueba` tiene una sola "
                    "fila.",
                    "**Un solo bloque `DO` con los cuatro `CALL` dentro.** Parece mas elegante y "
                    "es peor: la primera excepcion salta al manejador y las llamadas siguientes se "
                    "saltan. Cada prueba necesita su propio bloque justamente para poder fallar "
                    "sola.",
                    "**`EXCEPTION WHEN OTHERS THEN NULL;`** —capturar y no registrar nada—. El "
                    "script no se cae, pero la bateria no prueba nada: no queda evidencia de que "
                    "la excepcion ocurrio ni de cual fue. Es la version silenciosa del error "
                    "anterior.",
                    "**Poner el texto de la excepcion a mano** en la columna `obtenido` en vez de "
                    "`SQLERRM`. Entonces la prueba dice lo que el estudiante espera, no lo que el "
                    "motor respondio, y deja de ser una prueba. Se detecta porque el texto es "
                    "sospechosamente limpio.",
                    "**Creer que las pruebas negativas dejan filas a medias.** No las dejan, y "
                    "vale explicar por que: el bloque `DO` con manejador abre una subtransaccion "
                    "implicita, asi que cuando la excepcion se captura se deshace lo que el `CALL` "
                    "hubiera alcanzado a hacer, y el `INSERT` en `resultado_prueba` que viene "
                    "despues si queda. Ese mecanismo es el tema completo de la Clase 8.",
                    "**Reportar «el procedimiento no existe».** En esta pregunta el procedimiento "
                    "viene creado en el `setup_sql`. Si aparece el error, casi siempre el "
                    "estudiante esta ejecutando en la base de la pregunta 1 con su propia version "
                    "a medio hacer, o escribio el nombre con una letra distinta. Revisar el "
                    "mensaje real antes de aceptar la premisa.",
                ],
            },
            {
                "n": 3,
                "titulo": "PROCEDURE o FUNCTION en PostgreSQL",
                "tipo": "cerrada",
                "puntos": 10,
                "justificacion": {
                    0: "**Incorrecta.** Es justamente lo que un `PROCEDURE` no puede hacer. En "
                       "PostgreSQL un procedimiento se invoca con `CALL` como **sentencia "
                       "independiente**; escribirlo en la lista de columnas de un `SELECT` da "
                       "`ERROR: sp_x(...) is a procedure` y sugiere usar `CALL`. La frontera es "
                       "clara: lo que se usa dentro de una consulta es una funcion.",
                    1: "**Correcta.** El criterio de decision no es «cual es mas moderno» sino "
                       "**donde se necesita invocarlo**. Como el precio sugerido se va a usar "
                       "dentro de un `SELECT` sobre `consulta`, tiene que ser "
                       "`CREATE FUNCTION fn_precio_sugerido(p_especie TEXT) RETURNS NUMERIC`, y "
                       "entonces se escribe `SELECT ..., fn_precio_sugerido(m.especie) FROM ...`. "
                       "Un procedimiento no cabe ahi.",
                    2: "**Incorrecta.** Un `PROCEDURE` con parametro `OUT` **si** existe en "
                       "PostgreSQL y devuelve valores —`CALL sp_x(1, NULL)` los entrega—, pero "
                       "sigue siendo una sentencia independiente: no se puede poner dentro de un "
                       "`SELECT`, que es lo que la pregunta necesita. Y el «es la unica forma de "
                       "retornar un valor» es falso de plano: para eso estan las funciones.",
                    3: "**Incorrecta, y es la mas importante de descartar** porque es el residuo "
                       "de otros motores. En PostgreSQL son objetos distintos desde la version 11: "
                       "la funcion se invoca dentro de una consulta y **no puede** controlar "
                       "transacciones; el procedimiento se invoca con `CALL` y **si** puede hacer "
                       "`COMMIT` y `ROLLBACK` en su interior. Esa capacidad transaccional es la "
                       "verdadera razon por la que existen los dos.",
                    4: "**Incorrecta.** Al reves de la realidad. `LANGUAGE plpgsql` es "
                       "precisamente el lenguaje con `DECLARE`, `IF`, bucles y `RETURN`, y las "
                       "funciones plpgsql retornan valores todo el tiempo —el `sp_agendar_cita` de "
                       "la pregunta 1 esta escrito en plpgsql—. `LANGUAGE sql` sirve para cuerpos "
                       "de una sola expresion y es mas rapido cuando alcanza, pero no es una "
                       "condicion para retornar.",
                },
                "como_calificar": [
                    "**10 pts si marca la opcion 2 tal como aparece numerada en la plataforma** "
                    "(indice 1: la funcion que devuelve `NUMERIC`). Cualquier otra respuesta, 0. "
                    "Es pregunta de opcion unica, sin parcial: la clave se lee del banco.",
                    "El criterio que se evalua no es memoria de sintaxis sino **la regla de "
                    "decision**: se usa funcion cuando hay que invocarla dentro de una consulta, y "
                    "procedimiento cuando es una accion que se ejecuta sola y puede necesitar "
                    "controlar la transaccion. Conviene decirla asi en la devolucion, porque es lo "
                    "que se aplica en el PI: `sp_agendar_cita` es procedimiento; el precio "
                    "sugerido es funcion.",
                    "Si mas de un tercio del grupo marca la opcion 4 —«son sinonimos»—, vale "
                    "abrir la Clase 4 con dos minutos de demostracion en vivo: un `SELECT` con la "
                    "funcion adentro y un `SELECT` con el procedimiento adentro, para que vean el "
                    "mensaje del motor. Es mas eficaz que repetir la definicion.",
                ],
                "errores": [
                    "**Marcar la opcion 4 («da lo mismo»).** Casi siempre viene de material de "
                    "otros motores, donde la distincion es mas borrosa. En PostgreSQL son objetos "
                    "distintos y el motor lo dice con un mensaje de error explicito.",
                    "**Marcar la del `PROCEDURE` con `OUT`.** El razonamiento va por buen camino "
                    "—reconoce que hay que devolver algo— pero no atiende la condicion del "
                    "enunciado, que es **usarlo dentro de un `SELECT`**. Vale la pena senalarlo "
                    "asi: la respuesta no es incorrecta por el `OUT`, es incorrecta por donde se "
                    "necesita invocar.",
                    "**Marcar la ultima («solo si es `LANGUAGE sql`»).** Contradice el propio "
                    "trabajo del estudiante: acaba de escribir plpgsql en las preguntas 1 y 4. "
                    "Devolver con esa observacion es mas util que explicar la teoria.",
                    "**Responder bien aqui y despues escribir `CREATE FUNCTION` en la pregunta 4.** "
                    "Pasa mas de lo que parece. El taller pide un **procedimiento** en las "
                    "preguntas 1 y 4 porque son acciones que modifican datos; la funcion es para "
                    "el precio sugerido de esta pregunta, que no se implementa hoy.",
                ],
            },
            {
                "n": 4,
                "titulo": "sp_registrar_consulta: el segundo procedimiento de negocio",
                "tipo": "bd_sql",
                "puntos": 15,
                "sql": """-- =====================================================================
    -- sp_registrar_consulta: cierra el ciclo de la atencion. Inserta la
    -- consulta y mueve la cita a ATENDIDA en la misma operacion, para que no
    -- pueda existir una consulta cuya cita siga PROGRAMADA.
    -- =====================================================================
    CREATE OR REPLACE PROCEDURE sp_registrar_consulta(
      p_id_cita     INT,
      p_diagnostico TEXT,
      p_precio      NUMERIC
    )
    LANGUAGE plpgsql
    AS $proc$
    DECLARE
      v_estado TEXT;
    BEGIN
      -- 1) ¿Existe la cita? Igual que en sp_agendar_cita: SELECT ... INTO de
      --    una columna, para que FOUND signifique algo.
      SELECT estado INTO v_estado
        FROM cita
       WHERE id_cita = p_id_cita;

      IF NOT FOUND THEN
        RAISE EXCEPTION 'ERROR: la cita % no existe', p_id_cita;
      END IF;

      -- 2) Una cita CANCELADA no genera consulta. Se permite registrar sobre
      --    una PROGRAMADA (el caso normal) y tambien sobre una ATENDIDA que
      --    todavia no tenga consulta, porque la validacion 3 es la que decide
      --    eso: aqui solo se cierra la puerta a la cancelada.
      IF v_estado = 'CANCELADA' THEN
        RAISE EXCEPTION
          'ERROR: la cita % esta CANCELADA; una cita cancelada no genera consulta',
          p_id_cita;
      END IF;

      -- 3) ¿Ya tiene consulta? Se pregunta con EXISTS ANTES de intentar el
      --    INSERT. La restriccion UNIQUE de consulta.id_cita ya lo impediria,
      --    pero su mensaje seria "duplicate key value violates unique
      --    constraint consulta_id_cita_key", que no le sirve a nadie en el
      --    mostrador. La restriccion es la garantia; el EXISTS es la
      --    explicacion. Se necesitan las dos.
      IF EXISTS (SELECT 1 FROM consulta WHERE id_cita = p_id_cita) THEN
        RAISE EXCEPTION 'ERROR: la cita % ya tiene una consulta registrada',
                        p_id_cita;
      END IF;

      -- 4) Precio estrictamente positivo. Es MAS estricto que el CHECK de la
      --    tabla, que admite precio >= 0: una consulta gratis se registra con
      --    otro procedimiento y con autorizacion, no colandole un cero aqui.
      IF p_precio IS NULL OR p_precio <= 0 THEN
        RAISE EXCEPTION 'ERROR: el precio debe ser mayor que cero; llego %',
                        p_precio;
      END IF;

      -- 5) Las dos escrituras, en la misma operacion. Un PROCEDURE llamado con
      --    CALL corre dentro de la transaccion de quien lo llama: si el UPDATE
      --    fallara, el INSERT tambien se deshace. Eso es lo que hace que no
      --    exista una consulta con su cita sin atender.
      INSERT INTO consulta (id_cita, diagnostico, precio)
      VALUES (p_id_cita, p_diagnostico, p_precio);

      UPDATE cita
         SET estado = 'ATENDIDA'
       WHERE id_cita = p_id_cita;
    END;
    $proc$;

    -- =====================================================================
    -- Demostracion: una valida y dos que deben fallar sin detener el script.
    -- =====================================================================
    CALL sp_registrar_consulta(1, 'Vacunacion anual antirrabica', 45000);

    DO $$
    BEGIN
      CALL sp_registrar_consulta(4, 'Revision', 30000);   -- cita 4: CANCELADA
    EXCEPTION WHEN OTHERS THEN
      RAISE NOTICE '%', SQLERRM;
    END $$;

    DO $$
    BEGIN
      CALL sp_registrar_consulta(2, 'Duplicada', 40000);  -- cita 2: ya tiene
    EXCEPTION WHEN OTHERS THEN
      RAISE NOTICE '%', SQLERRM;
    END $$;

    -- =====================================================================
    -- Cierre pedido por el enunciado.
    -- =====================================================================
    SELECT c.id_cita, c.estado, co.diagnostico, co.precio
      FROM cita c
      LEFT JOIN consulta co ON co.id_cita = c.id_cita
     ORDER BY c.id_cita;""",
                "salida": """Los dos avisos de los bloques DO (van al panel de mensajes, no a la grilla):

      NOTICE:  ERROR: la cita 4 esta CANCELADA; una cita cancelada no genera consulta
      NOTICE:  ERROR: la cita 2 ya tiene una consulta registrada

    SELECT c.id_cita, c.estado, co.diagnostico, co.precio ...   -- 10 filas

     id_cita |   estado   |         diagnostico          |  precio
    ---------+------------+------------------------------+----------
           1 | ATENDIDA   | Vacunacion anual antirrabica | 45000.00
           2 | ATENDIDA   | Vacunacion triple felina     | 40000.00
           3 | PROGRAMADA |                              |
           4 | CANCELADA  |                              |
           5 | ATENDIDA   | Control de peso              | 38000.00
           6 | PROGRAMADA |                              |
           7 | ATENDIDA   | Otitis externa               | 55000.00
           8 | PROGRAMADA |                              |
           9 | PROGRAMADA |                              |
          10 | ATENDIDA   | Desparasitacion              | 35000.00

    Las tres comprobaciones que hay que buscar en esta salida, en este orden:

    1. La fila 1 paso de PROGRAMADA a ATENDIDA y trae diagnostico y precio: el
       procedimiento hizo sus dos escrituras.
    2. La fila 4 sigue en CANCELADA y con las dos columnas vacias: la validacion
       2 impidio la consulta y, muy importante, no cambio el estado. Si la fila 4
       apareciera en ATENDIDA, el UPDATE se hizo antes de validar.
    3. La fila 2 conserva su diagnostico original, `Vacunacion triple felina`, no
       `Duplicada`: la validacion 3 rechazo el segundo registro sin sobrescribir el
       primero.

    El precio sale con dos decimales porque la columna es `NUMERIC(12,2)`, aunque el
    `CALL` recibio `45000` sin decimales. No es un error del estudiante.""",
                "como_calificar": [
                    "**8 pts — las cuatro validaciones, 2 pts cada una.** Cita inexistente, cita "
                    "cancelada, consulta duplicada **detectada con `EXISTS`** y precio positivo. "
                    "La tercera es la que la rubrica subraya: si el estudiante deja que reviente "
                    "la restriccion `UNIQUE` en vez de preguntar antes, esos 2 pts no se dan "
                    "aunque el resultado final sea el mismo, porque el mensaje que llega a la "
                    "aplicacion es inservible.",
                    "**4 pts — las dos escrituras.** 2 pts el `INSERT` en `consulta` y 2 pts el "
                    "`UPDATE` de la cita a `'ATENDIDA'`, **despues** de las cuatro validaciones. "
                    "Se verifica en la salida: la fila 4 debe seguir en `CANCELADA`.",
                    "**2 pts — la demostracion completa.** La llamada valida corre, y las dos "
                    "invalidas van envueltas en `DO ... EXCEPTION WHEN OTHERS THEN RAISE NOTICE` "
                    "de modo que el script llega hasta el `SELECT` final. Si el script se detiene, "
                    "estos 2 pts no se dan.",
                    "**1 pt — el `SELECT` final** con el `LEFT JOIN` y el `ORDER BY` pedidos, "
                    "devolviendo las 10 filas. Con `JOIN` en vez de `LEFT JOIN` devuelve 5 y se "
                    "pierde el punto: el `LEFT` esta ahi precisamente para ver las citas **sin** "
                    "consulta.",
                    "**Piso de sintaxis.** Si el procedimiento no se crea, no hay puntos de "
                    "validaciones ni de escrituras. Y una advertencia de correccion: quien haya "
                    "resuelto bien la pregunta 1 y mal esta casi siempre fallo en el "
                    "`RAISE EXCEPTION` de varias lineas, que necesita la coma antes de los "
                    "argumentos.",
                    "**Bono conceptual, sin puntos:** quien escriba en un comentario que el "
                    "`EXISTS` **no reemplaza** a la restriccion `UNIQUE` sino que la acompana "
                    "—porque entre el `EXISTS` y el `INSERT` cabe otra sesion— ya entendio el tema "
                    "de la Clase 10 tres semanas antes. Vale mencionarlo al grupo.",
                ],
                "errores": [
                    "**Confiar en el `UNIQUE` y no validar con `EXISTS`.** Funciona en el sentido "
                    "de que no se duplica, pero el mensaje que sale es "
                    "`duplicate key value violates unique constraint`, que la aplicacion no puede "
                    "traducir a nada util. Es el error que la rubrica senala de forma explicita.",
                    "**Hacer el `UPDATE` de la cita antes del `INSERT` de la consulta, o antes de "
                    "validar.** El sintoma esta en la salida: la cita 4 aparece `ATENDIDA` aunque "
                    "no tenga consulta. Deja la base en un estado que ninguna regla del negocio "
                    "admite y es exactamente el tipo de inconsistencia que la Clase 8 formaliza.",
                    "**Validar `p_precio >= 0` en vez de `> 0`.** El enunciado pide "
                    "estrictamente positivo. Ademas hay una razon para no copiar el `CHECK` de la "
                    "tabla: el `CHECK` protege la integridad del dato, el procedimiento protege la "
                    "regla del negocio, y aqui la regla es mas estricta que el dato.",
                    "**Olvidar el caso `NULL` en el precio.** `NULL <= 0` no es falso, es "
                    "**desconocido**, asi que el `IF` no entra y el `INSERT` termina fallando por "
                    "el `NOT NULL` de la columna, con un mensaje del motor en vez del propio. Es "
                    "el error de logica de tres valores mas comun y vale explicarlo en voz alta: "
                    "por eso la condicion empieza con `p_precio IS NULL OR`.",
                    "**Poner los tres `CALL` sin bloque `DO`.** El script se detiene en el "
                    "segundo, el `SELECT` final nunca corre y no hay evidencia de nada. El "
                    "enunciado da la plantilla, asi que este error es de lectura.",
                    "**`JOIN` en vez de `LEFT JOIN`** en el cierre. Devuelve 5 filas y desaparecen "
                    "justo las que interesan —las citas sin consulta, entre ellas la 4—. Cuesta el "
                    "punto y, peor, esconde la comprobacion mas importante de la pregunta.",
                ],
            },
            {
                "n": 5,
                "titulo": "Contrato de los procedimientos para la futura aplicacion",
                "tipo": "abierta",
                "puntos": 15,
                "tabla": {
                    "headers": ["Procedimiento", "Excepcion", "Texto del mensaje",
                                "Que debe hacer la aplicacion"],
                    "rows": [
                        ["`sp_agendar_cita`", "Mascota inexistente",
                         "`ERROR: la mascota 99 no existe`",
                         "**No** mostrar el error al usuario: es un defecto del cliente, que "
                         "envio un id que no esta en el catalogo. Registrar en el log con el id "
                         "recibido y mostrar «seleccione una mascota de la lista». El selector "
                         "debe cargarse de la base, no escribirse a mano."],
                        ["`sp_agendar_cita`", "Mascota inactiva",
                         "`ERROR: la mascota 3 esta inactiva; no se agenda cita`",
                         "Aviso al usuario con el motivo, en su idioma: «Rocky esta inactivo y no "
                         "puede agendar. Reactivelo desde la ficha de la mascota o consulte con "
                         "la coordinacion». Deshabilitar el boton de agendar mientras la mascota "
                         "elegida este inactiva."],
                        ["`sp_agendar_cita`", "Veterinario ocupado",
                         "`ERROR: el veterinario 1 ya tiene cita en 2026-09-01 08:00:00`",
                         "No es un error del usuario, es una carrera perdida: alguien tomo la "
                         "franja primero. Refrescar la agenda del veterinario y **ofrecer las "
                         "tres franjas libres mas cercanas**, sin perder el resto del formulario."],
                        ["`sp_registrar_consulta`", "Cita inexistente",
                         "`ERROR: la cita 99 no existe`",
                         "Defecto del cliente. Log con el id, mensaje generico y volver a cargar "
                         "la lista de citas del dia: casi siempre la pantalla quedo abierta con "
                         "datos viejos."],
                        ["`sp_registrar_consulta`", "Cita cancelada",
                         "`ERROR: la cita 4 esta CANCELADA; una cita cancelada no genera "
                         "consulta`",
                         "Aviso con el motivo y bloqueo del formulario de consulta para esa cita. "
                         "Ofrecer la accion correcta: agendar una cita nueva, que es "
                         "`sp_agendar_cita`."],
                        ["`sp_registrar_consulta`", "Consulta duplicada",
                         "`ERROR: la cita 2 ya tiene una consulta registrada`",
                         "Casi siempre es un doble clic o un reenvio del formulario. **No** "
                         "insistir: mostrar la consulta que ya existe y ofrecer «editar» en vez "
                         "de «registrar». La aplicacion deberia ademas deshabilitar el boton "
                         "despues del primer envio."],
                        ["`sp_registrar_consulta`", "Precio no valido",
                         "`ERROR: el precio debe ser mayor que cero; llego 0`",
                         "Validacion de formulario que **tambien** debe estar en el cliente, para "
                         "no gastar un viaje a la base. Marcar el campo en rojo con el texto «el "
                         "precio debe ser mayor que cero» y no habilitar el envio hasta que lo "
                         "sea."],
                    ],
                },
                "respuesta": (
                    "**Contrato de `sp_agendar_cita`**\n\n"
                    "1. **Firma exacta:** "
                    "`sp_agendar_cita(p_id_mascota INT, p_id_veterinario INT, "
                    "p_fecha_hora TIMESTAMP)`. Tres parametros de entrada, en ese orden, sin "
                    "valores por omision y sin parametros `OUT`.\n"
                    "2. **Como se invoca:** "
                    "`CALL sp_agendar_cita(1, 2, TIMESTAMP '2026-09-15 10:00:00');`\n"
                    "3. **Precondiciones:** la mascota existe y tiene `activa = 'S'`; el "
                    "veterinario existe; el veterinario no tiene otra cita no cancelada en esa "
                    "misma `fecha_hora`. Quien llama **no** tiene que comprobar nada de esto: "
                    "puede llamar y atender la excepcion. Esa es la gracia del contrato.\n"
                    "4. **Postcondiciones:** exactamente **una** fila nueva en `cita`, con "
                    "`estado = 'PROGRAMADA'` y el `id_cita` que asigna la secuencia. Ninguna otra "
                    "tabla cambia. Si la llamada falla, **ninguna** fila cambia: no hay estados "
                    "intermedios visibles.\n"
                    "5. **Tabla de errores:** las tres primeras filas de la tabla de arriba.\n"
                    "6. **Decision de diseno:** la validacion vive en la base porque la regla "
                    "«una mascota inactiva no agenda» es del negocio, no de la pantalla. "
                    "Manana habra una app web, un script de carga masiva y una consola de "
                    "soporte tocando la misma base; si la regla estuviera en la app, los otros "
                    "dos caminos la esquivarian sin enterarse. Escrita una sola vez dentro del "
                    "motor, vale para **cualquier** cliente que llegue.\n\n"
                    "**Contrato de `sp_registrar_consulta`**\n\n"
                    "1. **Firma exacta:** "
                    "`sp_registrar_consulta(p_id_cita INT, p_diagnostico TEXT, "
                    "p_precio NUMERIC)`.\n"
                    "2. **Como se invoca:** "
                    "`CALL sp_registrar_consulta(1, 'Vacunacion anual antirrabica', 45000);`\n"
                    "3. **Precondiciones:** la cita existe; su estado **no** es `'CANCELADA'`; no "
                    "tiene todavia una consulta registrada; el precio es mayor que cero.\n"
                    "4. **Postcondiciones:** una fila nueva en `consulta` con `id_cita` unico, y "
                    "la fila correspondiente de `cita` con `estado = 'ATENDIDA'`. **Las dos cosas "
                    "o ninguna:** el procedimiento corre dentro de la transaccion de quien lo "
                    "llama, asi que no puede quedar una consulta cuya cita siga `PROGRAMADA`. "
                    "Esta es la postcondicion mas importante del contrato y es la que la Clase 8 "
                    "formaliza con la palabra atomicidad.\n"
                    "5. **Tabla de errores:** las cuatro ultimas filas de la tabla de arriba.\n"
                    "6. **Decision de diseno:** ademas del argumento anterior, aqui hay uno "
                    "propio: el paso «insertar la consulta» y el paso «marcar la cita como "
                    "atendida» **tienen que ocurrir juntos**. Si la aplicacion hiciera dos "
                    "llamadas —un `INSERT` y luego un `UPDATE`— una caida de red entre las dos "
                    "dejaria la base en un estado que ninguna regla del negocio admite. Dentro "
                    "del procedimiento eso es imposible por construccion.\n\n"
                    "**Regla del PI, la frase de cierre:**\n\n"
                    "> La aplicacion de Huellitas **nunca** hara `INSERT` ni `UPDATE` directo "
                    "sobre `cita` ni sobre `consulta`. Su unico acceso de escritura a esas dos "
                    "tablas es `EXECUTE` sobre `sp_agendar_cita` y `sp_registrar_consulta`. Lo "
                    "que la matriz de la Clase 2 escribio como intencion, aqui queda "
                    "implementado: en la Clase 12 el rol `recepcion` pierde el `INSERT` sobre "
                    "`cita` y conserva unicamente el `EXECUTE`."
                ),
                "como_calificar": [
                    "**8 pts — los 6 puntos documentados para los dos procedimientos.** 4 pts por "
                    "procedimiento, a razon de aproximadamente 0,67 por punto. Se descuenta el "
                    "punto completo cuando la seccion existe pero esta vacia de contenido "
                    "verificable («precondiciones: que los datos sean correctos»).",
                    "**3 pts — las firmas coinciden exactamente con el codigo entregado** en las "
                    "preguntas 1 y 4: nombre, orden y tipos. Es el criterio duro de la rubrica y "
                    "se revisa comparando contra **el script del estudiante**, no contra esta "
                    "solucion. Si su procedimiento recibe `(p_id_veterinario, p_id_mascota, ...)` "
                    "en otro orden, su contrato tiene que decir ese orden.",
                    "**3 pts — la tabla de errores.** Debe listar **todas** las excepciones que su "
                    "propio codigo implementa —normalmente 3 + 4 = 7—, con el **texto real** del "
                    "mensaje y una **accion concreta** de la aplicacion para cada una. 0,4 pts por "
                    "fila. Una accion como «mostrar el error» no cuenta: hay que decir que ve el "
                    "usuario y que hace el sistema.",
                    "**1 pt — la justificacion** menciona explicitamente que la regla debe valer "
                    "para **cualquier cliente** que toque la base, no solo para la app web. Es la "
                    "frase que la rubrica pide y es el argumento central de la clase.",
                    "**Se valora, sin puntos adicionales:** distinguir los errores que el usuario "
                    "debe ver (mascota inactiva, precio invalido) de los que son defectos del "
                    "cliente y solo van al log (id inexistente). Esa distincion es la que hace un "
                    "contrato utilizable, y es lo que la Clase 12 va a exigir por escrito.",
                    "**Extension.** Dos paginas es de sobra. Se califica que esten los 6 puntos y "
                    "la tabla completa; no se descuenta por brevedad si nada falta.",
                ],
                "errores": [
                    "**Firmas que no coinciden con el codigo entregado.** Es el descuento mas "
                    "frecuente y el mas facil de evitar: casi siempre el estudiante escribe el "
                    "contrato de memoria en vez de copiar la cabecera de su propio "
                    "`CREATE PROCEDURE`. La correccion es literal: copiar y pegar.",
                    "**Tabla de errores con la excepcion pero sin el texto del mensaje.** El "
                    "mensaje **es** el contrato: es lo unico que la aplicacion recibe y sobre lo "
                    "que puede decidir. Sin el texto, la tabla no sirve para programar nada.",
                    "**«Que debe hacer la aplicacion: mostrar un mensaje de error».** No es una "
                    "accion, es la ausencia de una decision. Se pide el comportamiento concreto: "
                    "que texto ve el usuario, que control se bloquea, que alternativa se ofrece.",
                    "**Mostrar el `SQLERRM` crudo al usuario final.** «ERROR: la mascota 3 esta "
                    "inactiva» esta bien para el log; en pantalla el usuario necesita el nombre "
                    "(«Rocky») y la salida («reactivelo desde la ficha»). Vale la pena senalarlo "
                    "aunque el enunciado no lo exija: es la diferencia entre un mensaje tecnico y "
                    "un mensaje util.",
                    "**Postcondiciones que no dicen que pasa si falla.** «Se inserta la cita» esta "
                    "a medias. La otra mitad —«y si falla, no cambia nada»— es la que le permite a "
                    "la aplicacion no tener que limpiar despues de un error, y es la razon de ser "
                    "del procedimiento.",
                    "**Justificar con la definicion.** «La validacion va en la base porque es mas "
                    "seguro» no dice nada. Se pide el argumento del caso: tres clientes distintos "
                    "tocando la misma base y una sola regla que ninguno puede esquivar.",
                    "**Omitir la frase de cierre del PI.** Es una linea y es la que conecta esta "
                    "clase con la matriz de la Clase 2 y con el contrato de la Clase 12. Si falta, "
                    "pedirla: no es decoracion, es la decision de arquitectura del proyecto.",
                ],
            },
        ],
        "preguntas_frecuentes": [
            ("¿Puedo escribir `CREATE PROCEDURE` como en Oracle, con `IS` y `/` al final?",
             "No, y el motor lo rechaza de entrada. La forma de PostgreSQL es "
             "`CREATE OR REPLACE PROCEDURE nombre(params) LANGUAGE plpgsql AS $proc$ DECLARE ... "
             "BEGIN ... END; $proc$;`. Cuatro traducciones que resuelven el 90 % de los errores: "
             "`AS` en vez de `IS`, `TEXT` o `VARCHAR` en vez de `VARCHAR2`, `NUMERIC` en vez de "
             "`NUMBER`, y `RAISE EXCEPTION 'texto %', var;` en vez de `RAISE_APPLICATION_ERROR`. "
             "La barra final simplemente no existe."),
            ("Mi validacion de «no existe» nunca dispara. ¿Que pasa?",
             "Casi con seguridad esta usando `IF NOT FOUND` despues de un `SELECT COUNT(*) INTO`. "
             "Un `COUNT` **siempre** devuelve una fila, asi que `FOUND` es verdadero incluso "
             "cuando el conteo da cero. `NOT FOUND` funciona despues de un `SELECT columna INTO`, "
             "que puede no traer fila. Con agregados hay que comparar el numero: "
             "`IF v_ocupado > 0 THEN`."),
            ("¿Por que el procedimiento valida si la tabla ya tiene un `CHECK` y un `UNIQUE`?",
             "Porque hacen dos cosas distintas y se necesitan las dos. La restriccion es la "
             "**garantia**: no hay forma de meter el dato malo, venga de donde venga. El `IF` del "
             "procedimiento es la **explicacion**: convierte "
             "`duplicate key value violates unique constraint consulta_id_cita_key` en «la cita 2 "
             "ya tiene una consulta registrada», que es lo que la aplicacion puede mostrar. "
             "Quitar la restriccion y quedarse con el `IF` es el error grave; quitar el `IF` y "
             "quedarse con la restriccion solo deja mensajes inservibles."),
            ("Corri mi script dos veces y me dice que el procedimiento ya existe.",
             "Es normal: `CREATE PROCEDURE` falla si el nombre esta tomado. Use "
             "`CREATE OR REPLACE PROCEDURE` desde el principio y el problema desaparece. Si ya "
             "quedo creado y quiere cambiar los parametros, hay que borrarlo primero con "
             "`DROP PROCEDURE sp_agendar_cita(INT, INT, TIMESTAMP);` —con los tipos, porque el "
             "nombre solo no identifica la rutina—. Recargar el ejercicio en ExamLab tambien "
             "devuelve la base al estado sembrado."),
            ("Si valido con un `IF` que la franja esta libre, ¿ya no hay forma de duplicar?",
             "Con una sola sesion, no. Con dos personas agendando al mismo tiempo, si: las dos "
             "pueden contar cero antes de que ninguna haya insertado, y las dos insertar. La "
             "validacion leyendo antes de escribir no es una garantia, es una comodidad. La "
             "garantia es una restriccion unica sobre `(id_veterinario, fecha_hora)` para las "
             "citas no canceladas, y ese es exactamente el tema de la Clase 10. Quien lo escriba "
             "hoy en un comentario va tres semanas adelantado."),
            ("¿Cual es la diferencia real entre PROCEDURE y FUNCTION, mas alla de la sintaxis?",
             "Dos, y las dos importan. Una: la funcion se puede invocar **dentro** de una "
             "consulta (`SELECT fn_precio(m.especie) FROM mascota m`) y el procedimiento no; el "
             "procedimiento se invoca con `CALL` como sentencia suelta. Dos: el procedimiento "
             "puede hacer `COMMIT` y `ROLLBACK` en su interior y la funcion no, porque la funcion "
             "corre dentro de la consulta que la llamo. Para el PI la regla practica es simple: "
             "si modifica datos y es una accion del negocio, procedimiento; si calcula y "
             "devuelve un valor para usarlo en una consulta, funcion."),
            ("En las pruebas negativas, ¿`paso` debe quedar en TRUE o en FALSE?",
             "Las dos se aceptan, siempre que diga cual usa y la aplique a las cuatro filas. Si "
             "`paso` significa «el resultado coincidio con lo esperado», las negativas quedan en "
             "TRUE, porque lo esperado era la excepcion: es la semantica de cualquier framework "
             "de pruebas. Si significa «la operacion se completo», quedan en FALSE, que es lo que "
             "hace la plantilla del enunciado. Lo que no vale es que las cuatro digan TRUE sin "
             "haber verificado el texto de la excepcion, porque entonces cualquier fallo —incluso "
             "un nombre mal escrito— se reportaria como prueba superada."),
            ("¿Las pruebas que fallan dejan filas a medias en `cita`?",
             "No, y el mecanismo vale la pena entenderlo porque es el tema de la Clase 8: un "
             "bloque `DO` con manejador `EXCEPTION` abre una subtransaccion, asi que al capturar "
             "la excepcion se deshace todo lo que el `CALL` alcanzo a hacer. El `INSERT` en "
             "`resultado_prueba` que viene **despues** del manejador si queda. Por eso la bateria "
             "puede registrar cuatro resultados y dejar una sola cita nueva, y por eso la segunda "
             "consulta de cierre debe dar 11 y no 14."),
        ],
        "cierre": [
            "Al terminar, cada estudiante debe tener: `sp_agendar_cita` creado con sus tres "
            "validaciones y el `CALL` que agrega la cita 11, la bateria de cuatro pruebas con las "
            "cuatro filas en `resultado_prueba` y los conteos que demuestran que nada quedo a "
            "medias, `sp_registrar_consulta` con sus cuatro validaciones y la cita 1 en "
            "`ATENDIDA`, y el contrato de los dos procedimientos con la tabla de las siete "
            "excepciones.",
            "Lo que hay que verificar antes de cerrar la sesion es la **consistencia entre las "
            "preguntas 1 y 4 y la pregunta 5**: el contrato tiene que describir el codigo que el "
            "estudiante entrego, no el de la solucion. Proyecte una entrega voluntaria y compare "
            "la cabecera del `CREATE PROCEDURE` con la firma escrita en el contrato: es el "
            "chequeo de treinta segundos que detecta la mitad de las entregas flojas.",
            "Dejar dicho en voz alta lo que sigue. En la Clase 4 aparece el disparador, que es el "
            "unico objeto que nadie invoca, y con el la tabla de auditoria que la matriz de la "
            "Clase 2 ya reservo para el `auditor` en solo lectura. Y en la Clase 10 se vera por "
            "que la validacion de la franja libre que hoy quedo escrita con un `IF` **no** "
            "garantiza nada con dos personas agendando al mismo tiempo: la garantia sera una "
            "restriccion, no un `IF` mas.",
        ],
    },

    4: {
        "titulo": "Solucion del taller · Clase 4 · Funciones, triggers y plan de respaldo de VetCare",
        "resumen": (
            "La funcion de tarifas `fn_precio_consulta` corriendo dentro de dos consultas, el "
            "trigger de auditoria que registra 2 filas y no 3, el trigger que impide el stock "
            "negativo despues de haber visto el -7 en pantalla, el criterio para decidir si una "
            "validacion va en `CHECK`, en trigger o en la aplicacion, y el "
            "`Plan_Backup_VetCare` con RPO, RTO y una consulta de validacion post-restauracion "
            "que si detecta un respaldo incompleto."
        ),
        "total": 100,
        "nota_actividad": (
            "**El motor es PostgreSQL, no Oracle,** y esta clase es la que mas se paga en "
            "sintaxis: en PostgreSQL el trigger **no lleva codigo adentro**. Se escriben dos "
            "objetos —una funcion `RETURNS TRIGGER` y luego "
            "`CREATE TRIGGER ... EXECUTE FUNCTION nombre_de_la_funcion()`— y dentro de la funcion "
            "se usan `NEW` y `OLD` **sin los dos puntos**: `NEW.estado`, no `:NEW.estado`. "
            "Anunciarlo antes de arrancar ahorra la mitad de los reportes de error. Un detalle "
            "del entorno: la pregunta 3 corre sobre una base donde la tabla `insumo` fue creada "
            "**a proposito sin** su `CHECK (stock >= 0)`, para que el estudiante pueda ver el "
            "stock en -7 antes de arreglarlo; en las demas preguntas el `CHECK` si esta. Y la "
            "pregunta 5 es un **documento**: no hay que contratar ningun servicio, ni abrir "
            "cuenta, ni poner tarjeta."
        ),
        "preguntas": [
            {
                "n": 1,
                "titulo": "Funcion de tarifas fn_precio_consulta",
                "tipo": "bd_sql",
                "puntos": 20,
                "sql": """-- =====================================================================
    -- fn_precio_consulta: la tarifa base de Huellitas, en un solo lugar.
    -- Es FUNCTION y no PROCEDURE porque hay que invocarla DENTRO de un
    -- SELECT, que es justo lo que un procedimiento no puede hacer.
    -- IMMUTABLE es correcto aqui porque el resultado depende unicamente de
    -- los dos parametros: no lee ninguna tabla ni la hora del sistema.
    -- =====================================================================
    CREATE OR REPLACE FUNCTION fn_precio_consulta(
      p_especie  TEXT,
      p_urgencia BOOLEAN
    )
    RETURNS NUMERIC
    LANGUAGE plpgsql
    IMMUTABLE
    AS $fn$
    DECLARE
      v_base NUMERIC;
      v_urg  BOOLEAN;
    BEGIN
      -- COALESCE convierte el NULL en falso. Sin esto, IF p_urgencia THEN con
      -- NULL no entra por ninguna rama (NULL no es verdadero NI falso) y la
      -- funcion terminaria sin RETURN, lanzando
      -- "control reached end of function without RETURN".
      v_urg := COALESCE(p_urgencia, FALSE);

      -- UPPER() en los dos lados de la comparacion: asi 'CANINO', 'canino' y
      -- 'Canino' entran por la misma rama. Comparar contra 'Canino' a secas
      -- es el error mas frecuente de la pregunta.
      CASE UPPER(TRIM(COALESCE(p_especie, '')))
        WHEN 'CANINO' THEN v_base := 45000;
        WHEN 'FELINO' THEN v_base := 40000;
        ELSE               v_base := 35000;   -- cualquier otra especie
      END CASE;

      -- El recargo del 35 %. Se escribe * 1.35 y no + 35 % de nada: el
      -- ROUND(..., 2) esta para que las dos columnas salgan con la misma
      -- escala que la columna precio de consulta, NUMERIC(12,2).
      IF v_urg THEN
        RETURN ROUND(v_base * 1.35, 2);
      END IF;

      RETURN ROUND(v_base, 2);
    END;
    $fn$;

    -- =====================================================================
    -- Consulta 1: la tarifa de las 8 mascotas, normal y de urgencia.
    -- =====================================================================
    SELECT nombre,
           especie,
           fn_precio_consulta(especie, FALSE) AS tarifa_normal,
           fn_precio_consulta(especie, TRUE)  AS tarifa_urgencia
      FROM mascota
     ORDER BY id_mascota;

    -- =====================================================================
    -- Consulta 2: lo cobrado contra la tarifa. Este es el uso que justifica
    -- que sea funcion: va dentro del SELECT, en la misma fila que el precio
    -- real, y la resta la hace el motor.
    -- =====================================================================
    SELECT co.id_consulta,
           c.id_cita,
           m.nombre                                  AS mascota,
           m.especie,
           co.precio                                 AS precio_cobrado,
           fn_precio_consulta(m.especie, FALSE)      AS tarifa_base,
           co.precio - fn_precio_consulta(m.especie, FALSE) AS diferencia
      FROM consulta co
      JOIN cita    c ON c.id_cita    = co.id_cita
      JOIN mascota m ON m.id_mascota = c.id_mascota
     ORDER BY co.id_consulta;

    -- =====================================================================
    -- Comprobacion de las tres reglas del enunciado, en una sola fila.
    -- =====================================================================
    SELECT fn_precio_consulta('canino',  FALSE) AS minusculas_45000,
           fn_precio_consulta('CANINO',  TRUE)  AS urgencia_60750,
           fn_precio_consulta('Conejo',  FALSE) AS otra_especie_35000,
           fn_precio_consulta('Felino',  NULL)  AS null_como_falso_40000;""",
                "salida": """Consulta 1 -- 8 filas

      nombre  | especie | tarifa_normal | tarifa_urgencia
    ----------+---------+---------------+-----------------
     Firulais | Canino  |      45000.00 |        60750.00
     Luna     | Felino  |      40000.00 |        54000.00
     Rocky    | Canino  |      45000.00 |        60750.00
     Mishi    | Felino  |      40000.00 |        54000.00
     Bobby    | Canino  |      45000.00 |        60750.00
     Nube     | Felino  |      40000.00 |        54000.00
     Toby     | Canino  |      45000.00 |        60750.00
     Kiara    | Canino  |      45000.00 |        60750.00

    Las 8 mascotas, incluidas Rocky y Kiara que estan inactivas: la funcion no
    filtra por `activa` y esta bien que no lo haga. Una funcion IMMUTABLE no puede
    leer tablas; quien quiera excluirlas pone el `WHERE m.activa = 'S'` en la
    consulta, no dentro de la funcion. El numero que confirma el recargo es el
    60750.00 (45000 x 1.35).

    Consulta 2 -- 4 filas

     id_consulta | id_cita | mascota  | especie | precio_cobrado | tarifa_base | diferencia
    -------------+---------+----------+---------+----------------+-------------+------------
               1 |       2 | Luna     | Felino  |       40000.00 |    40000.00 |       0.00
               2 |       5 | Nube     | Felino  |       38000.00 |    40000.00 |   -2000.00
               3 |       7 | Firulais | Canino  |       55000.00 |    45000.00 |   10000.00
               4 |      10 | Nube     | Felino  |       35000.00 |    40000.00 |   -5000.00

    Solo una de las cuatro consultas cobro exactamente la tarifa. Dos cobraron
    por debajo y una por encima, y la suma de las diferencias es +3000. La lectura
    que hay que dejar dicha: la funcion es la tarifa de referencia, no lo
    facturado; el negocio ajusta caso por caso. Ese hueco entre lo esperado y lo
    cobrado es lo que la Clase 6 va a convertir en una vista de control.

    Comprobacion de las reglas -- 1 fila

     minusculas_45000 | urgencia_60750 | otra_especie_35000 | null_como_falso_40000
    ------------------+----------------+--------------------+-----------------------
             45000.00 |       60750.00 |           35000.00 |              40000.00

    Los cuatro nombres de columna dicen el valor esperado, asi que la fila se
    corrige de un vistazo. Si la ultima columna sale vacia o el script falla con
    "control reached end of function without RETURN", falta el COALESCE.""",
                "como_calificar": [
                    "**5 pts — la funcion se crea con la firma exacta.** "
                    "`fn_precio_consulta(TEXT, BOOLEAN)`, `RETURNS NUMERIC`, `LANGUAGE plpgsql` "
                    "y **`IMMUTABLE`**. 1 pt es de `IMMUTABLE`: es facil de olvidar y el "
                    "enunciado lo pide de forma explicita. Si el motor no acepta la funcion, no "
                    "hay puntos de logica.",
                    "**8 pts — las cuatro reglas, 2 pts cada una.** Las tres tarifas "
                    "45000/40000/35000 con `ELSE` para «cualquier otra»; la insensibilidad a "
                    "mayusculas con `UPPER()` o `lower()`; el recargo del 35 %; y `NULL` tratado "
                    "como falso con `COALESCE`. La ultima es la que mas se pierde y la que mas "
                    "vale explicar.",
                    "**5 pts — las dos consultas pedidas.** 2 pts la de las 8 mascotas con las "
                    "cuatro columnas y `ORDER BY id_mascota`; 3 pts la de la diferencia, que "
                    "exige los **dos** `JOIN` (`consulta -> cita -> mascota`) y una columna "
                    "`diferencia` calculada por el motor. Escribir la diferencia a mano no vale.",
                    "**2 pts — los valores son coherentes con los datos.** La rubrica nombra el "
                    "caso: Firulais canino en 45000 y 60750 en urgencia. Se verifica contra la "
                    "salida de arriba, sin ejecutar nada.",
                    "**Piso de sintaxis.** `RETURN NUMBER IS`, `VARCHAR2` o la barra `/` final "
                    "impiden que el motor cree la funcion, asi que el efecto ya esta en el primer "
                    "renglon: no se descuenta aparte.",
                    "**Bono conceptual, sin puntos:** quien explique por que la funcion **puede** "
                    "ser `IMMUTABLE` —porque no lee ninguna tabla, solo sus dos parametros— y "
                    "senale que si manana las tarifas se guardaran en una tabla habria que "
                    "bajarla a `STABLE`, entendio para que sirve la etiqueta. No es decoracion: "
                    "una funcion `IMMUTABLE` que si lee tablas devuelve resultados viejos y es un "
                    "error muy dificil de encontrar.",
                ],
                "errores": [
                    "**`WHEN 'Canino' THEN`** sin normalizar. Funciona con los datos sembrados "
                    "—que estan capitalizados asi— y falla en cuanto alguien escribe `CANINO` "
                    "desde otra pantalla. Se detecta con la consulta de comprobacion: "
                    "`fn_precio_consulta('canino', FALSE)` debe dar 45000, no 35000. Es el error "
                    "que mas puntos cuesta porque **la salida de la consulta 1 se ve bien**.",
                    "**Olvidar el `COALESCE` del `NULL`.** El sintoma es inconfundible: "
                    "`ERROR: control reached end of function without RETURN`. La razon merece "
                    "medio minuto en voz alta: `IF p_urgencia THEN ... ELSE ... END IF` con "
                    "`p_urgencia` en `NULL` **no entra por ninguna de las dos ramas**, porque "
                    "`NULL` no es verdadero ni falso. Es la logica de tres valores de SQL "
                    "apareciendo dentro de un `IF`.",
                    "**Aplicar el recargo como `v_base + 35`** o como `v_base * 0.35`. El primero "
                    "suma 35 pesos y el segundo devuelve **solo** el recargo. Se detecta en un "
                    "golpe: la columna de urgencia de Firulais tiene que decir 60750, y cualquier "
                    "otro numero es este error.",
                    "**Escribir un `PROCEDURE` en vez de una `FUNCTION`.** Se crea sin problema y "
                    "revienta en la consulta 1 con `ERROR: fn_precio_consulta(...) is a procedure` "
                    "y la sugerencia de usar `CALL`. Es exactamente la frontera de la pregunta 3 "
                    "de la Clase 3, ahora en la practica: lo que se invoca dentro de un `SELECT` "
                    "es una funcion.",
                    "**Un solo `JOIN` en la consulta 2.** De `consulta` a `mascota` no hay camino "
                    "directo: la especie esta en `mascota`, y `consulta` solo conoce `id_cita`. "
                    "Hay que pasar por `cita`. Quien intente `JOIN mascota ON ...` desde "
                    "`consulta` recibe `column co.id_mascota does not exist`, que es el motor "
                    "diciendo justamente eso.",
                    "**Meter el `WHERE m.activa = 'S'` dentro de la funcion.** Ademas de no poder "
                    "—una funcion `IMMUTABLE` no debe leer tablas—, mezcla dos cosas: cuanto vale "
                    "atender un canino, y a quien se le puede atender. La segunda ya la resuelve "
                    "`sp_agendar_cita` de la Clase 3.",
                ],
            },
            {
                "n": 2,
                "titulo": "Trigger de auditoria de cambios de estado de cita",
                "tipo": "bd_sql",
                "puntos": 20,
                "sql": """-- =====================================================================
    -- 1) La tabla de auditoria. usuario_bd y fecha_evento con DEFAULT: los
    --    pone el motor, no el trigger, para que nadie pueda falsearlos desde
    --    la aplicacion. Es el mismo criterio de la matriz de la Clase 2: el
    --    rol auditor lee esta tabla y no escribe en ella.
    -- =====================================================================
    CREATE TABLE audit_cita (
      id_audit       SERIAL PRIMARY KEY,
      id_cita        INT       NOT NULL,
      accion         TEXT      NOT NULL,
      valor_anterior TEXT,
      valor_nuevo    TEXT,
      usuario_bd     TEXT      DEFAULT current_user,
      fecha_evento   TIMESTAMP DEFAULT now()
    );

    -- =====================================================================
    -- 2) La funcion de trigger. En PostgreSQL el codigo NO va dentro del
    --    CREATE TRIGGER: va aqui, en una funcion aparte que devuelve TRIGGER
    --    y que puede ser reutilizada por varios triggers.
    --    NEW y OLD se escriben SIN los dos puntos: NEW.estado, no :NEW.estado.
    -- =====================================================================
    CREATE OR REPLACE FUNCTION fn_trg_audit_cita()
    RETURNS TRIGGER
    LANGUAGE plpgsql
    AS $fn$
    BEGIN
      INSERT INTO audit_cita (id_cita, accion, valor_anterior, valor_nuevo)
      VALUES (NEW.id_cita, 'CAMBIO_ESTADO', OLD.estado, NEW.estado);

      -- En un trigger AFTER ... FOR EACH ROW el valor de retorno se ignora,
      -- asi que RETURN NULL y RETURN NEW dan lo mismo. Se pone RETURN NULL
      -- para dejar claro que esta funcion NO pretende modificar la fila.
      RETURN NULL;
    END;
    $fn$;

    -- =====================================================================
    -- 3) El trigger. Tres decisiones, las tres pedidas por el enunciado:
    --    AFTER  -> auditar lo que YA quedo guardado, no lo que se intento;
    --    UPDATE OF estado -> solo interesa esa columna;
    --    WHEN (OLD.estado IS DISTINCT FROM NEW.estado) -> y solo cuando de
    --    verdad cambio. Esto ultimo no es un lujo: UPDATE OF estado se
    --    dispara cuando la columna aparece en el SET, aunque el valor sea el
    --    mismo. Sin el WHEN habria 3 filas auditadas y no 2.
    --    IS DISTINCT FROM y no <>: con <>, un cambio de NULL a 'ATENDIDA'
    --    daria NULL, el WHEN no se cumpliria y ese cambio no se auditaria.
    -- =====================================================================
    CREATE TRIGGER trg_audit_cita
    AFTER UPDATE OF estado ON cita
    FOR EACH ROW
    WHEN (OLD.estado IS DISTINCT FROM NEW.estado)
    EXECUTE FUNCTION fn_trg_audit_cita();

    -- =====================================================================
    -- 4) Las tres pruebas del enunciado, en orden. La tercera es la que
    --    demuestra que el filtro funciona: la cita 6 ya esta PROGRAMADA.
    -- =====================================================================
    UPDATE cita SET estado = 'CANCELADA'  WHERE id_cita = 1;   -- se audita
    UPDATE cita SET estado = 'ATENDIDA'   WHERE id_cita = 3;   -- se audita
    UPDATE cita SET estado = 'PROGRAMADA' WHERE id_cita = 6;   -- NO se audita

    -- =====================================================================
    -- 5) El cierre pedido.
    -- =====================================================================
    SELECT id_audit, id_cita, accion, valor_anterior, valor_nuevo, usuario_bd
      FROM audit_cita
     ORDER BY id_audit;

    -- =====================================================================
    -- Prueba adicional que conviene mostrar al grupo: el UPDATE de la cita 6
    -- SI se ejecuto -- devolvio "UPDATE 1" -- y aun asi no dejo rastro. Es la
    -- diferencia entre "el UPDATE corrio" y "el estado cambio".
    -- =====================================================================
    SELECT (SELECT COUNT(*) FROM audit_cita)                        AS filas_auditadas,
           (SELECT estado FROM cita WHERE id_cita = 1)              AS cita_1,
           (SELECT estado FROM cita WHERE id_cita = 3)              AS cita_3,
           (SELECT estado FROM cita WHERE id_cita = 6)              AS cita_6,
           (SELECT COUNT(*) FROM audit_cita WHERE id_cita = 6)       AS auditorias_de_la_6;""",
                "salida": """UPDATE cita SET estado = 'CANCELADA'  WHERE id_cita = 1;   -- UPDATE 1
    UPDATE cita SET estado = 'ATENDIDA'   WHERE id_cita = 3;   -- UPDATE 1
    UPDATE cita SET estado = 'PROGRAMADA' WHERE id_cita = 6;   -- UPDATE 1  <-- corrio igual

    SELECT id_audit, id_cita, accion, valor_anterior, valor_nuevo, usuario_bd ...  -- 2 filas

     id_audit | id_cita |    accion     | valor_anterior | valor_nuevo | usuario_bd
    ----------+---------+---------------+----------------+-------------+------------
            1 |       1 | CAMBIO_ESTADO | PROGRAMADA     | CANCELADA   | postgres
            2 |       3 | CAMBIO_ESTADO | PROGRAMADA     | ATENDIDA    | postgres

    Dos filas, no tres. Es el resultado que la pregunta pide demostrar. Y el
    detalle que hay que subrayar en la devolucion: el tercer `UPDATE` si se
    ejecuto -- el motor respondio `UPDATE 1`, no `UPDATE 0` -- y aun asi no dejo
    rastro, porque la clausula `WHEN` se evalua por fila y descarto ese disparo.

    El valor de `usuario_bd` depende de con que usuario se conecte el entorno; en
    ExamLab sale `postgres`. No se califica el nombre, se califica que la columna
    tenga `DEFAULT current_user` y que el trigger no lo escriba a mano.

    Prueba adicional -- 1 fila

     filas_auditadas | cita_1    | cita_3   | cita_6     | auditorias_de_la_6
    -----------------+-----------+----------+------------+--------------------
                   2 | CANCELADA | ATENDIDA | PROGRAMADA |                  0

    Ese 0 de la derecha es la prueba mas limpia de que el filtro es el que
    trabaja, y no la casualidad.""",
                "como_calificar": [
                    "**5 pts — `audit_cita` con las 7 columnas** y los dos `DEFAULT`: "
                    "`current_user` y `now()`. 2 de los 5 pts son de los `DEFAULT`, porque son "
                    "la razon de ser de la tabla: si el usuario y la hora los pone quien escribe, "
                    "la auditoria no prueba nada.",
                    "**5 pts — la funcion `RETURNS TRIGGER`** inserta `NEW.id_cita`, la accion "
                    "`'CAMBIO_ESTADO'`, `OLD.estado` en `valor_anterior` y `NEW.estado` en "
                    "`valor_nuevo`. Invertir `OLD` y `NEW` cuesta 2 pts: la salida sale con las "
                    "columnas cruzadas y se detecta sin ejecutar nada.",
                    "**6 pts — el trigger, 2 pts por decision.** `AFTER UPDATE` **`OF estado`**, "
                    "`FOR EACH ROW`, y la clausula "
                    "`WHEN (OLD.estado IS DISTINCT FROM NEW.estado)`. Los 2 pts del `WHEN` no se "
                    "dan si se resuelve con un `IF` dentro de la funcion: funciona, pero el "
                    "enunciado pide la clausula y hay una razon —abajo, en errores frecuentes—.",
                    "**4 pts — la demostracion de las 2 filas.** 2 pts las tres sentencias en el "
                    "orden pedido y 2 pts el `SELECT` final mostrando exactamente 2 filas. La "
                    "rubrica exige ademas que **el estudiante explique por que la tercera no se "
                    "audito**: si el script muestra 2 filas pero no hay una linea que lo explique, "
                    "se descuenta 1 de estos 4.",
                    "**Cero sintaxis Oracle.** `:NEW` / `:OLD`, el bloque `BEGIN ... END` dentro "
                    "del `CREATE TRIGGER`, u omitir `EXECUTE FUNCTION`: la rubrica lo penaliza y "
                    "en la practica el motor ni crea el objeto, asi que el efecto es automatico "
                    "sobre los 6 pts del trigger.",
                    "**Bono conceptual, sin puntos:** quien explique por que se usa "
                    "`IS DISTINCT FROM` y no `<>` —con `<>`, un cambio desde `NULL` daria `NULL`, "
                    "el `WHEN` no se cumpliria y **ese** cambio se perderia de la auditoria— "
                    "entendio el unico detalle fino de la pregunta. Aqui `estado` es `NOT NULL` y "
                    "da lo mismo, pero la costumbre correcta se construye ahora.",
                ],
                "errores": [
                    "**Poner el codigo dentro del `CREATE TRIGGER`,** como en Oracle. Es el error "
                    "numero uno de la clase. En PostgreSQL son **dos** objetos: una funcion "
                    "`RETURNS TRIGGER` con el cuerpo, y un `CREATE TRIGGER` que solo dice cuando "
                    "dispararla y termina en `EXECUTE FUNCTION nombre()`.",
                    "**`:NEW.estado` en vez de `NEW.estado`.** Los dos puntos son de PL/SQL. El "
                    "mensaje del motor —`syntax error at or near \":\"`— apunta al lugar correcto, "
                    "asi que este error se corrige solo si el estudiante lee el error.",
                    "**Omitir la clausula `WHEN` y filtrar con un `IF` dentro de la funcion.** El "
                    "resultado visible es el mismo —2 filas— y por eso hay que explicar la "
                    "diferencia: con el `WHEN`, el motor **ni siquiera llama** a la funcion; con "
                    "el `IF`, la llama, entra, evalua y sale. En una carga masiva de 50 000 citas "
                    "esa diferencia es medible. Se descuentan los 2 pts del `WHEN` pero se "
                    "reconoce que la logica es correcta.",
                    "**Omitir el filtro por completo y no notarlo.** El `SELECT` final devuelve 3 "
                    "filas, y una de ellas tiene `valor_anterior` y `valor_nuevo` **iguales**: "
                    "`PROGRAMADA -> PROGRAMADA`. Esa fila es basura de auditoria, y en un ano son "
                    "miles. Es el sintoma que hay que ensenar a reconocer.",
                    "**`AFTER UPDATE ON cita` sin `OF estado`.** Funciona, porque el `WHEN` "
                    "atrapa lo demas, pero hace que el trigger se evalue en cada cambio de "
                    "`fecha_hora` tambien. Se descuentan los 2 pts de esa decision: el enunciado "
                    "es explicito y la intencion —auditar **una** columna— debe quedar escrita en "
                    "el objeto.",
                    "**Escribir `usuario_bd` y `fecha_evento` desde el `INSERT` de la funcion.** "
                    "Quita el sentido a los `DEFAULT` y abre la puerta a que un dia alguien ponga "
                    "otro nombre. La regla es la de la Clase 2: el dato de la auditoria lo pone el "
                    "motor, no el codigo que se audita.",
                ],
            },
            {
                "n": 3,
                "titulo": "Trigger que impide stock negativo",
                "tipo": "bd_sql",
                "puntos": 20,
                "sql": """-- =====================================================================
    -- 1) PRIMERO EL PROBLEMA. En esta base insumo NO tiene CHECK (stock >= 0),
    --    asi que el motor acepta encantado un stock imposible. Hay que verlo
    --    antes de arreglarlo: es la mitad del valor didactico de la pregunta.
    -- =====================================================================
    UPDATE insumo SET stock = stock - 10 WHERE id_insumo = 2;   -- habia 3

    SELECT id_insumo, nombre, stock AS stock_imposible
      FROM insumo
     WHERE id_insumo = 2;
    -- Vacuna triple felina | -7   <-- ninguna bodega del mundo tiene -7 vacunas

    -- Se restaura el dato antes de seguir. Se escribe el valor absoluto y no
    -- stock + 10, para no arrastrar el error si el UPDATE anterior corrio dos
    -- veces.
    UPDATE insumo SET stock = 3 WHERE id_insumo = 2;

    -- =====================================================================
    -- 2) La funcion de trigger. RETURN NEW al final es OBLIGATORIO en un
    --    trigger BEFORE ... FOR EACH ROW: si devolviera NULL, el motor
    --    cancelaria la fila EN SILENCIO -- el UPDATE diria "UPDATE 0" y nadie
    --    sabria por que. Devolver NEW es decir "sigue adelante con este
    --    valor".
    -- =====================================================================
    CREATE OR REPLACE FUNCTION fn_trg_stock_no_negativo()
    RETURNS TRIGGER
    LANGUAGE plpgsql
    AS $fn$
    BEGIN
      IF NEW.stock < 0 THEN
        RAISE EXCEPTION
          'ERROR: el stock de % no puede quedar negativo (resultado: %)',
          OLD.nombre, NEW.stock;
      END IF;

      RETURN NEW;
    END;
    $fn$;

    -- =====================================================================
    -- 3) El trigger. BEFORE, no AFTER: se revisa el valor ANTES de escribirlo,
    --    que es el unico momento en que todavia se puede vetar o corregir la
    --    fila con un RETURN. Un AFTER llega cuando el dato ya se escribio y su
    --    unico recurso es hacer estallar toda la sentencia.
    -- =====================================================================
    CREATE TRIGGER trg_stock_no_negativo
    BEFORE UPDATE OF stock ON insumo
    FOR EACH ROW
    EXECUTE FUNCTION fn_trg_stock_no_negativo();

    -- =====================================================================
    -- 4) Las dos pruebas, cada una en su propio bloque DO para que la primera
    --    no tumbe el script y la segunda alcance a correr.
    -- =====================================================================
    DO $$
    BEGIN
      -- Intento invalido: descontar 10 de un insumo que tiene 3.
      UPDATE insumo SET stock = stock - 10 WHERE id_insumo = 2;
      RAISE NOTICE 'PRUEBA 1 FALLIDA: el trigger dejo pasar un stock negativo';
    EXCEPTION WHEN OTHERS THEN
      RAISE NOTICE 'PRUEBA 1 OK, el trigger bloqueo: %', SQLERRM;
    END $$;

    DO $$
    BEGIN
      -- Intento valido: descontar 2. Debe pasar y dejar el stock en 1.
      UPDATE insumo SET stock = stock - 2 WHERE id_insumo = 2;
      RAISE NOTICE 'PRUEBA 2 OK, el descuento valido paso';
    EXCEPTION WHEN OTHERS THEN
      RAISE NOTICE 'PRUEBA 2 FALLIDA: %', SQLERRM;
    END $$;

    -- =====================================================================
    -- 5) Estado final: ningun stock negativo y el insumo 2 en 1.
    -- =====================================================================
    SELECT id_insumo, nombre, stock
      FROM insumo
     ORDER BY id_insumo;

    -- Y la comprobacion de una sola linea, para no tener que leer las 6 filas.
    SELECT COUNT(*) FILTER (WHERE stock < 0) AS negativos_debe_ser_0,
           (SELECT stock FROM insumo WHERE id_insumo = 2) AS insumo_2_debe_ser_1
      FROM insumo;""",
                "salida": """Paso 1 -- el problema, antes del trigger

     id_insumo |        nombre        | stock_imposible
    -----------+----------------------+-----------------
             2 | Vacuna triple felina |              -7

    Avisos de los dos bloques DO (van al panel de mensajes):

      NOTICE:  PRUEBA 1 OK, el trigger bloqueo: ERROR: el stock de Vacuna triple felina
               no puede quedar negativo (resultado: -7)
      NOTICE:  PRUEBA 2 OK, el descuento valido paso

    Estado final -- 6 filas

     id_insumo |          nombre          | stock
    -----------+--------------------------+-------
             1 | Vacuna antirrabica       |    12
             2 | Vacuna triple felina     |     1
             3 | Antiparasitario oral     |    40
             4 | Suero fisiologico 500ml  |    25
             5 | Gasa esteril             |     8
             6 | Jeringa 5ml              |    60

    Comprobacion de una linea -- 1 fila

     negativos_debe_ser_0 | insumo_2_debe_ser_1
    ----------------------+---------------------
                        0 |                   1

    Las tres cosas que hay que ver, en este orden: el -7 existio (el problema es
    real, no una advertencia teorica), el aviso de la prueba 1 trae el nombre del
    insumo y el valor rechazado (el mensaje sirve para actuar, no solo para
    saber que algo fallo), y el insumo 2 quedo en 1 y no en 3 -- si quedara en 3,
    el trigger esta bloqueando tambien los descuentos validos, casi siempre por
    haber escrito `NEW.stock <= 0`.""",
                "como_calificar": [
                    "**4 pts — se evidencia el problema y se restaura el dato.** 3 pts el `UPDATE` "
                    "mas el `SELECT` que muestra el **-7**, y 1 pt devolver el insumo 2 a 3 antes "
                    "de continuar. Sin la evidencia del -7 la pregunta pierde su sentido: el "
                    "estudiante estaria arreglando un problema que no vio.",
                    "**6 pts — la funcion.** 3 pts la condicion `NEW.stock < 0` con "
                    "`RAISE EXCEPTION` que incluya `OLD.nombre` y `NEW.stock` en el mensaje; "
                    "3 pts el **`RETURN NEW`** en el camino valido. Este ultimo no es un detalle: "
                    "sin el, un trigger `BEFORE` cancela la fila en silencio.",
                    "**4 pts — el trigger es `BEFORE UPDATE OF stock ... FOR EACH ROW`.** La "
                    "rubrica penaliza `AFTER`; se descuentan 2 de estos 4 si se usa `AFTER` "
                    "—porque la eleccion de momento es lo que se esta evaluando— y los 4 completos "
                    "si falta `FOR EACH ROW`, porque entonces el trigger es de sentencia y "
                    "`NEW`/`OLD` ni existen.",
                    "**4 pts — las dos pruebas en bloques `DO` separados,** con la excepcion "
                    "capturada y el script llegando hasta el final. 2 pts cada una.",
                    "**2 pts — el estado final** demuestra que ningun stock quedo negativo y que "
                    "el insumo 2 esta en **1**. El 1 es el numero que se busca: en 3 significa que "
                    "el trigger tambien bloqueo el descuento valido.",
                    "**Bono conceptual, sin puntos, y es el mejor de la clase:** quien escriba que "
                    "este trigger **sobra** —que la solucion correcta era el "
                    "`CHECK (stock >= 0)` que la tabla tenia en las otras preguntas, y que el "
                    "trigger esta aqui solo como ejercicio— acaba de responder por su cuenta la "
                    "pregunta 4. Vale la pena leerlo en voz alta.",
                ],
                "errores": [
                    "**Olvidar `RETURN NEW`.** El sintoma es raro y desconcierta: el `UPDATE` "
                    "valido responde `UPDATE 0`, no da ningun error y el stock no cambia. Un "
                    "trigger `BEFORE ... FOR EACH ROW` que devuelve `NULL` le dice al motor "
                    "«descarta esta fila», y lo hace **en silencio**. Es el error mas costoso de "
                    "depurar de toda la clase.",
                    "**`NEW.stock <= 0`** en vez de `< 0`. Bloquea el caso legitimo de quedarse "
                    "en cero, que es lo que pasa cuando se gasta la ultima unidad. Se detecta en "
                    "el estado final: si el insumo 2 quedo en 3, el descuento valido tambien fue "
                    "rechazado.",
                    "**Usar `AFTER` en lugar de `BEFORE`.** Se descuenta segun la rubrica, y "
                    "conviene dar la razon exacta porque la de «no impide el cambio» es "
                    "imprecisa: en PostgreSQL una excepcion en un trigger `AFTER` **si** aborta la "
                    "sentencia y deshace la escritura. Lo que pierde es todo lo demas: la fila ya "
                    "se escribio y se indexo para nada, no queda forma de **corregir** el valor "
                    "con un `RETURN NEW` ajustado, y si hay varios `AFTER` el orden alfabetico "
                    "decide quien ve que. La validacion va donde todavia se puede decidir.",
                    "**`RAISE_APPLICATION_ERROR(-20001, '...')`.** Es de Oracle y aqui es un error "
                    "de sintaxis. El equivalente es "
                    "`RAISE EXCEPTION 'texto % y %', var1, var2;`, y el `%` se sustituye en orden.",
                    "**Usar `NEW.nombre` en el mensaje** en vez de `OLD.nombre`. Funciona, porque "
                    "el `UPDATE` no toca el nombre y los dos valen lo mismo, y no se descuenta. "
                    "Pero el enunciado pide `OLD.nombre` y hay una razon: el mensaje describe el "
                    "insumo **tal como esta**, no como quedaria si el cambio pasara.",
                    "**Poner los dos `UPDATE` de prueba sin bloque `DO`.** El primero lanza la "
                    "excepcion, el script se detiene, la prueba valida nunca corre y el estado "
                    "final no aparece. El enunciado da la plantilla del bloque, asi que este es un "
                    "error de lectura.",
                ],
            },
            {
                "n": 4,
                "titulo": "Donde vive cada validacion: CHECK, trigger o aplicacion",
                "tipo": "cerrada_multi",
                "puntos": 15,
                "justificacion": {
                    0: "**Correcta, y es la moraleja de la pregunta 3.** La regla «el stock no es "
                       "negativo» mira una sola columna de la propia fila, asi que un "
                       "`CHECK (stock >= 0)` la resuelve mejor que el trigger: es una linea, el "
                       "motor la aplica venga el cambio de donde venga, no hay codigo que "
                       "mantener y **no se puede desactivar por descuido**. El trigger de la "
                       "pregunta 3 existe como ejercicio; en el PI real esa regla va en el "
                       "`CHECK` que la tabla ya trae en las demas preguntas.",
                    1: "**Incorrecta**, aunque no por la razon que suele darse. Es cierto que una "
                       "excepcion lanzada desde un trigger `AFTER` aborta la sentencia y deshace "
                       "la escritura; lo falso es el «igual que un `BEFORE`». Un `BEFORE` puede "
                       "**vetar** la fila o incluso **corregirla** devolviendo un `NEW` "
                       "modificado, y actua antes de gastar la escritura y los indices. Un "
                       "`AFTER` llega cuando el dato ya esta puesto y su unica herramienta es "
                       "hacer estallar todo. Se parecen en el resultado y no en lo que permiten: "
                       "la validacion va donde todavia se puede decidir.",
                    2: "**Correcta, y es la razon de ser de la pregunta 2.** Ninguna restriccion "
                       "declarativa guarda el valor **anterior**: un `CHECK` mira la fila nueva, "
                       "una clave ajena mira otra tabla, un `UNIQUE` mira el conjunto. Ninguna "
                       "recuerda que la cita 1 estuvo `PROGRAMADA` antes de quedar `CANCELADA`. "
                       "Para tener historia hace falta alguien que escriba la fila de auditoria, y "
                       "ese alguien es un trigger o codigo de la aplicacion. El trigger gana "
                       "porque no se puede esquivar.",
                    3: "**Incorrecta,** y es la que hay que desmontar con mas cuidado porque suena "
                       "razonable. El compromiso de una persona no es un control: el mismo "
                       "semestre del PI ya hay tres caminos hacia la misma base —la aplicacion "
                       "web, los scripts de carga y la consola de soporte— y ninguno de los tres "
                       "pasa por los otros. Ademas el compromiso caduca: la persona rota, entra "
                       "otra, y la regla no esta escrita en ninguna parte que el motor lea. "
                       "Validar en la aplicacion **tambien** es buena idea, por la experiencia de "
                       "uso; lo que no es, es suficiente.",
                    4: "**Correcta, y es el argumento central de la clase.** La validacion en la "
                       "base es la unica que cubre lo que nadie planeo: la carga masiva de fin de "
                       "mes, el script de mantenimiento que se corre a mano una vez, el "
                       "`UPDATE` de urgencia que alguien escribe en la consola a las 7 de la "
                       "tarde, y la aplicacion movil que se contrate el ano entrante. Es la misma "
                       "frase de cierre del contrato de la Clase 3, ahora aplicada a las reglas y "
                       "no solo a los procedimientos.",
                    5: "**Correcta, y es la contraparte honesta de todo lo anterior.** El trigger "
                       "es potente justamente porque es invisible: nadie lo invoca y nadie lo ve "
                       "en el codigo de la aplicacion. Eso mismo lo vuelve dificil de depurar "
                       "—«¿de donde salio esta fila?»—, el orden entre varios triggers de la misma "
                       "tabla lo decide el nombre en orden alfabetico y no la intencion del "
                       "autor, y en un `UPDATE` de 200 000 filas un trigger `FOR EACH ROW` se "
                       "ejecuta 200 000 veces. De ahi la regla practica: `CHECK` cuando alcance, "
                       "trigger cuando haga falta, y siempre documentado.",
                },
                "como_calificar": [
                    "**15 pts con las 4 correctas marcadas y ninguna incorrecta**, con puntaje "
                    "proporcional por acierto parcial, tal como dice la rubrica. La plataforma "
                    "calcula el parcial; la clave se lee del banco y es la que se califica.",
                    "El criterio que se esta evaluando es **una regla de decision de tres "
                    "escalones**, y conviene decirla asi en la devolucion: si la regla mira solo "
                    "la propia fila, `CHECK`; si necesita el valor anterior, otra fila u otra "
                    "tabla, trigger; si es experiencia de uso —un mensaje bonito, un boton "
                    "deshabilitado—, aplicacion, **ademas** de lo que ya este en la base.",
                    "**El par 0 / 5 es el que mide comprension real.** Marcar solo el 0 es «la "
                    "base siempre gana»; marcar solo el 5 es «los triggers son peligrosos». "
                    "Marcar los dos es haber entendido que la eleccion tiene costo en las dos "
                    "direcciones. Vale la pena mirar cuantos marcaron los dos.",
                    "Si mas de un tercio del grupo marca la opcion 4 —«basta con la aplicacion si "
                    "hay compromiso»—, es senal para abrir la Clase 6 con el ejemplo concreto: la "
                    "carga masiva de insumos que nadie va a pasar por la pantalla.",
                ],
                "errores": [
                    "**Marcar la del trigger `AFTER` como correcta.** No es un disparate: "
                    "efectivamente la excepcion aborta la sentencia. Lo que falla es el «igual "
                    "que»: un `BEFORE` puede corregir el valor y evita la escritura; un `AFTER` "
                    "solo puede volar la sentencia entera. Devolver con esa precision, no con un "
                    "«esta mal».",
                    "**Marcar la de «basta con la aplicacion».** Casi siempre viene de haber "
                    "trabajado en proyectos con un solo cliente. Basta con nombrar los tres "
                    "caminos que el propio PI ya tiene abiertos hacia la misma base.",
                    "**No marcar la opcion 5, la de los inconvenientes del trigger.** Suele ser "
                    "por lealtad: acaban de escribir dos triggers y les parece que reconocerles un "
                    "costo es contradecirse. Es lo contrario: la decision de diseno solo existe si "
                    "se conocen los dos precios.",
                    "**No marcar la opcion 0 despues de haber hecho la pregunta 3.** Es la senal "
                    "de que el trigger de stock se resolvio como receta y no como decision. Aqui "
                    "la devolucion es directa: la tabla `insumo` de las otras preguntas del taller "
                    "ya tiene ese `CHECK`, y por eso alli el problema del -7 no existe.",
                ],
            },
            {
                "n": 5,
                "titulo": "Plan de respaldo de VetCare DB",
                "tipo": "abierta",
                "puntos": 25,
                "tabla": {
                    "headers": ["Que se respalda", "Herramienta", "Frecuencia y ventana",
                                "Retencion y ubicacion"],
                    "rows": [
                        ["Datos + esquema + rutinas, todo junto",
                         "`pg_dump -Fc -d vetcare -f vetcare_AAAAMMDD.dump` (formato "
                         "comprimido, restaurable con `pg_restore`)",
                         "**Diario, 20:30.** La clinica cierra a las 19:00 y la facturacion del "
                         "ultimo turno se cierra hacia las 19:45; 20:30 da hora y media de "
                         "margen y aun deja la noche libre.",
                         "14 copias diarias + la del domingo durante 8 semanas. "
                         "**Ubicacion 1:** disco externo del consultorio. "
                         "**Ubicacion 2:** carpeta cifrada sincronizada fuera de la clinica el "
                         "mismo dia."],
                        ["Roles, contrasenas y permisos (la matriz de la Clase 2)",
                         "`pg_dumpall --globals-only -f roles_AAAAMMDD.sql`",
                         "**Diario, 20:25,** justo antes del dump, y **ademas cada vez que se "
                         "ejecuta un `GRANT` o `REVOKE`**. Se separa porque `pg_dump` de una base "
                         "**no** incluye los roles: restaurar solo el dump deja una base con "
                         "datos y sin usuarios.",
                         "30 dias, las dos ubicaciones. Es un archivo de pocos kilobytes: no hay "
                         "razon para guardar menos."],
                        ["DDL y rutinas como codigo fuente versionado",
                         "El repositorio Git del PI: `/db/01_schema.sql`, "
                         "`/db/02_procedimientos.sql`, `/db/03_triggers.sql`, "
                         "`/db/migraciones/NNN_*.sql`",
                         "**En cada cambio,** con el `commit` correspondiente. El respaldo del "
                         "esquema no es un archivo que se genera de noche: es el historial del "
                         "repositorio.",
                         "Indefinida. **Ubicacion 1:** repositorio remoto. **Ubicacion 2:** clon "
                         "local del docente. Se complementa con "
                         "`pg_dump --schema-only` diario, para poder comparar lo que hay en "
                         "produccion contra lo que dice el repositorio."],
                        ["Copia fisica para recuperacion rapida",
                         "`pg_basebackup -D /respaldos/base_AAAAMMDD -Ft -z`",
                         "**Semanal, domingo 02:00,** con la clinica cerrada. Es la que permite "
                         "un RTO corto: restaurar una copia fisica es copiar un directorio, no "
                         "reconstruir la base sentencia por sentencia.",
                         "4 copias semanales, solo en la ubicacion 1 por tamano. La primera del "
                         "mes se conserva 12 meses en la ubicacion 2."],
                        ["Registro continuo de transacciones (WAL)",
                         "Archivado de WAL: `archive_mode = on` mas un `archive_command` que "
                         "copie cada segmento a `/respaldos/wal/`",
                         "**Continuo.** Es lo unico que permite recuperar el trabajo hecho "
                         "**despues** del ultimo dump: sin esto, una caida a las 18:50 pierde el "
                         "dia completo de atencion.",
                         "7 dias, o el tiempo que cubra hasta la copia fisica mas antigua que se "
                         "conserve. Ubicacion 1, con copia diaria a la 2."],
                    ],
                },
                "respuesta": (
                    "**2. Por que esas horas.** La clinica atiende de lunes a sabado de 7:00 a "
                    "19:00. Todo lo que bloquea o pesa se corre **fuera** de esa franja: el dump "
                    "diario a las 20:30 y la copia fisica el domingo a las 2:00, el unico dia sin "
                    "atencion. El unico proceso que corre en horario de atencion es el archivado "
                    "de WAL, y corre porque no compite: copia segmentos ya cerrados. La ventana "
                    "no se pone «en la madrugada» por costumbre: se pone a las 20:30 porque la "
                    "facturacion del ultimo turno se cierra hacia las 19:45 y un respaldo tomado "
                    "a las 19:10 dejaria fuera las facturas del final del dia, que son "
                    "precisamente las que no se pueden reconstruir.\n\n"
                    "**4. RPO y RTO.**\n\n"
                    "- **RPO objetivo: 15 minutos.** Es lo que da el archivado de WAL, y se elige "
                    "mirando que se pierde en cada caso. Quince minutos son, como maximo, una "
                    "consulta y su factura: la agenda del dia esta impresa en recepcion y las dos "
                    "se pueden volver a capturar en cinco minutos. Sin archivado de WAL el RPO "
                    "seria de **hasta 12 horas de atencion** —una caida a las 18:50 volveria al "
                    "dump de la noche anterior— y eso significa perder unas 25 citas atendidas y "
                    "toda la facturacion del dia. Las citas se recuperan del papel; **las "
                    "facturas y los diagnosticos no**, y son las que tienen consecuencia legal y "
                    "contable. Por eso el archivado de WAL no es un lujo del plan: es lo que "
                    "convierte un RPO inaceptable en uno aceptable.\n"
                    "- **RTO objetivo: 4 horas en horario de atencion, 12 horas si la falla "
                    "ocurre fuera.** Cuatro horas es un tercio de la jornada: la clinica puede "
                    "operar ese tiempo con la agenda impresa y capturar despues, pero no un dia "
                    "entero. El presupuesto de las 4 horas se reparte asi: 30 min para detectar y "
                    "decidir, 60 min para restaurar la copia fisica del domingo, 90 min para "
                    "aplicar los WAL hasta el ultimo minuto disponible, 30 min para la consulta de "
                    "validacion de abajo, y 30 min de margen. La copia fisica esta en el plan "
                    "**por este numero**: restaurar desde el dump logico tomaria mas, porque hay "
                    "que volver a crear indices y restricciones.\n\n"
                    "**5. Restore de prueba.** Un respaldo no verificado no es un respaldo, es un "
                    "archivo. El ensayo es **mensual, el primer domingo, a las 3:00**, despues de "
                    "la copia fisica, y son cinco pasos concretos:\n\n"
                    "1. `createdb vetcare_restore_AAAAMMDD` — nunca sobre la base de produccion.\n"
                    "2. `psql -d vetcare_restore_AAAAMMDD -f roles_AAAAMMDD.sql` — los roles "
                    "primero, o el `pg_restore` fallara al asignar propietarios.\n"
                    "3. `pg_restore -d vetcare_restore_AAAAMMDD vetcare_AAAAMMDD.dump` y se "
                    "**guarda la salida completa**, incluidos los avisos.\n"
                    "4. Se corre la consulta de validacion y se compara contra los valores "
                    "esperados del dia del respaldo.\n"
                    "5. `dropdb vetcare_restore_AAAAMMDD` y se archiva la evidencia.\n\n"
                    "La consulta de validacion, con los valores que deben salir para el respaldo "
                    "de la base sembrada de este taller:\n\n"
                    "```sql\n"
                    "SELECT (SELECT COUNT(*) FROM cita)          AS citas,          -- 10\n"
                    "       (SELECT COUNT(*) FROM consulta)      AS consultas,      --  4\n"
                    "       (SELECT COUNT(*) FROM factura)       AS facturas,       --  3\n"
                    "       (SELECT SUM(total) FROM factura)     AS suma_facturado, -- 178200.00\n"
                    "       (SELECT MAX(fecha_hora) FROM cita)   AS ultima_cita,\n"
                    "                                       -- 2026-09-10 09:00:00\n"
                    "       (SELECT COUNT(*) FROM pg_proc p\n"
                    "          JOIN pg_namespace n ON n.oid = p.pronamespace\n"
                    "         WHERE n.nspname = 'public')        AS rutinas,\n"
                    "       (SELECT COUNT(*) FROM pg_trigger\n"
                    "         WHERE NOT tgisinternal)            AS triggers;\n"
                    "```\n\n"
                    "Las dos ultimas columnas son las que hacen que esta consulta sirva de algo. "
                    "Contar filas detecta un respaldo **truncado**; no detecta el fallo mas comun "
                    "y mas silencioso, que es un respaldo con **todos los datos y sin las "
                    "rutinas**: la base restaurada responde perfectamente a los `SELECT`, y el "
                    "dia que alguien llama a `sp_agendar_cita` no existe, o el trigger de "
                    "auditoria dejo de registrar sin que nadie se enterara. Se compara contra el "
                    "numero del dia: al cerrar este taller son **3 rutinas** —"
                    "`sp_agendar_cita`, `fn_precio_consulta`, `fn_trg_audit_cita`— y **1 "
                    "trigger**.\n\n"
                    "**Quien firma:** el ensayo lo ejecuta quien administre la base y la "
                    "evidencia —salida del `pg_restore` mas la fila de la consulta— queda en "
                    "`/informe/respaldos/restore-AAAA-MM.md` firmada por el responsable del PI. "
                    "Si un mes no se ensayo, se escribe que no se ensayo: un renglon vacio en la "
                    "bitacora es informacion, un renglon inventado es un riesgo.\n\n"
                    "**6. Que NO cubre este plan, y el riesgo residual.**\n\n"
                    "- **No cubre el borrado correcto pero indeseado.** Si alguien cancela 40 "
                    "citas por error y lo hace bien, el respaldo lo copia fielmente. Eso se "
                    "recupera con la auditoria de la pregunta 2, no con el respaldo.\n"
                    "- **No cubre lo que no esta en la base:** radiografias, consentimientos "
                    "escaneados, hojas de calculo en el escritorio de recepcion.\n"
                    "- **No cubre la infraestructura.** Restaurar datos en un servidor que no "
                    "existe no sirve; el plan asume que hay una maquina donde restaurar.\n"
                    "- **Riesgo residual asumido, escrito y firmado:** la copia remota se verifica "
                    "una vez al mes, no todos los dias. Entre dos ensayos puede haber hasta 30 "
                    "dias de copias que nadie probo. Se acepta porque la copia local si se "
                    "verifica con el ensayo mensual y porque el costo de un ensayo diario no se "
                    "justifica para una clinica de este tamano. **Queda por escrito para que sea "
                    "una decision y no un olvido.**\n\n"
                    "**Cierre — checklist del PI**\n\n"
                    "- **Listo:** matriz de roles y permisos (Clase 2). "
                    "**Listo:** procedimientos de negocio con sus validaciones y su contrato "
                    "(Clase 3). **Listo:** validaciones en la base para stock y estados "
                    "(Clase 4). **Listo:** `Plan_Backup_VetCare` como documento.\n"
                    "- **En progreso:** auditoria de cambios sensibles. Esta la de `cita`; faltan "
                    "`consulta` y `factura`, que son las dos que tienen consecuencia contable.\n"
                    "- **Falta:** el **primer ensayo de restore ejecutado**. El plan escrito vale "
                    "cero hasta que exista una fila de evidencia en "
                    "`/informe/respaldos/`, y ese es el gap principal que se declara hoy.\n"
                    "- **Falta:** los permisos de la matriz **aplicados** con `GRANT` sobre la "
                    "base real, con el rol `recepcion` sin `INSERT` directo sobre `cita`. Es lo "
                    "que cierra la Clase 12."
                ),
                "como_calificar": [
                    "**12 pts — las 6 secciones, 2 pts cada una.** Se dan los 2 pts cuando la "
                    "seccion trae **decisiones con numeros**, y 1 solo si esta presente pero es "
                    "generica. El criterio para distinguirlas: «respaldo diario en la noche» es "
                    "generico; «`pg_dump -Fc` a las 20:30 porque la facturacion cierra a las "
                    "19:45» es una decision.",
                    "**4 pts — RPO y RTO justificados con el impacto para la clinica,** no "
                    "definidos. Se pide un numero y la consecuencia de ese numero: cuantas citas y "
                    "cuantas facturas se pierden, y cuales de las dos se pueden reconstruir del "
                    "papel. Un RPO sin esa frase vale 1 de los 4.",
                    "**4 pts — herramientas reales de PostgreSQL y bien asignadas.** `pg_dump`, "
                    "`pg_dumpall --globals-only`, `pg_basebackup`, archivado de WAL, "
                    "`pg_restore`. Se descuentan 2 si aparece herramienta de Oracle "
                    "(`exp`/`imp`, `RMAN`, Data Pump) y 2 mas si `pg_dump` figura como si "
                    "respaldara tambien los roles: es el error tecnico mas comun de esta "
                    "pregunta.",
                    "**3 pts — la consulta de validacion post-restauracion.** 2 pts que sea "
                    "verificable, es decir que compare contra valores esperados concretos y no "
                    "«revisar que los datos esten»; 1 pt la periodicidad del ensayo y quien firma. "
                    "**Se reconoce como excelente** —sin puntos extra, pero se anota— si la "
                    "consulta verifica ademas que volvieron las **rutinas y los triggers**: es el "
                    "fallo silencioso que contar filas no detecta.",
                    "**2 pts — el cierre del checklist del PI** con los items en «listo» / «en "
                    "progreso» y **al menos un gap declarado explicitamente**. Un checklist con "
                    "todo en verde no vale los 2 pts: en la Clase 4 es imposible que todo este "
                    "listo, y la rubrica pide el gap pendiente.",
                    "**Extension.** El enunciado pide una pagina. Se califica que las 6 secciones "
                    "esten con decisiones concretas; no se premia la longitud y no se descuenta "
                    "por brevedad si nada falta.",
                ],
                "errores": [
                    "**Creer que `pg_dump` respalda los roles y los permisos.** No los respalda: "
                    "`pg_dump` es de **una** base y los roles son del **cluster**. Restaurar solo "
                    "el dump da una base con todos los datos y sin un solo usuario, y el "
                    "`pg_restore` empieza a fallar al asignar propietarios. La matriz de la "
                    "Clase 2 se respalda con `pg_dumpall --globals-only`. Es el error que hay que "
                    "corregir aunque el resto del plan este bien.",
                    "**Copiar el plan de otro motor.** `RMAN`, `exp`/`imp` o «Data Pump» "
                    "descalifican la seccion 1: la rubrica exige herramientas reales de "
                    "PostgreSQL. Se detecta rapido porque suele venir con una redaccion muy "
                    "distinta del resto del documento.",
                    "**RPO y RTO como definiciones.** «RPO es la cantidad de datos que se puede "
                    "perder» no responde nada. La pregunta es **cuanta**, en minutos u horas, y "
                    "**por que esa** y no el doble. Sin la justificacion de impacto son 1 punto "
                    "de 4.",
                    "**Un RPO de 15 minutos sin nada que lo sustente.** Si el plan solo tiene un "
                    "dump diario, el RPO **es** de hasta 24 horas, digalo o no el documento. El "
                    "numero tiene que estar respaldado por un mecanismo —archivado de WAL, o un "
                    "segundo dump al mediodia para bajarlo a 6 horas—. Escribir un RPO que el "
                    "plan no puede cumplir es peor que escribir uno honesto y grande.",
                    "**Retencion en una sola ubicacion,** o dos ubicaciones que en realidad son la "
                    "misma maquina: «disco C y disco D» no son dos ubicaciones. El enunciado pide "
                    "**dos distintas** y la razon es concreta: un robo, un incendio o un cifrado "
                    "por rescate se lleva las dos copias que estan en el mismo sitio.",
                    "**Validar el restore «revisando que los datos esten».** No es verificable y no "
                    "se puede automatizar. La seccion 5 pide una consulta con valores esperados; "
                    "sin ella, el ensayo depende de la impresion de quien mira la pantalla.",
                    "**El checklist del PI con todos los items en «listo».** Es la senal mas clara "
                    "de que la seccion se lleno por cumplir. En la Clase 4 hay al menos dos cosas "
                    "que no pueden estar hechas: el primer ensayo de restore y los `GRANT` "
                    "aplicados. Pedir la correccion nombrando esas dos.",
                ],
            },
        ],
        "preguntas_frecuentes": [
            ("¿Por que mi `CREATE TRIGGER` no acepta el codigo adentro?",
             "Porque en PostgreSQL el trigger **no tiene cuerpo**. Son dos objetos y en este "
             "orden: primero `CREATE FUNCTION fn_x() RETURNS TRIGGER LANGUAGE plpgsql AS $fn$ "
             "BEGIN ... END; $fn$;` con toda la logica, y despues "
             "`CREATE TRIGGER trg_x BEFORE UPDATE ON tabla FOR EACH ROW EXECUTE FUNCTION fn_x();` "
             "que solo dice cuando dispararla. La ventaja de esta separacion es que una misma "
             "funcion puede servir a varios triggers de varias tablas; la desventaja es que hay "
             "que acordarse de crear los dos."),
            ("¿`NEW` y `OLD` se escriben con dos puntos?",
             "No. En PostgreSQL son `NEW.columna` y `OLD.columna`, sin `:`. Los dos puntos son de "
             "PL/SQL de Oracle. Y hay una regla de disponibilidad que conviene tener presente: en "
             "un `INSERT` existe `NEW` y `OLD` es nulo; en un `DELETE` existe `OLD` y `NEW` es "
             "nulo; en un `UPDATE` existen los dos. Un trigger que use `OLD.nombre` en un "
             "`INSERT` fallara."),
            ("¿`BEFORE` o `AFTER`? Me dijeron que un `AFTER` no puede impedir el cambio.",
             "La regla practica es correcta —**validar en `BEFORE`, auditar en `AFTER`**— pero esa "
             "explicacion es imprecisa y vale corregirla: en PostgreSQL una excepcion lanzada "
             "desde un trigger `AFTER` **si** aborta la sentencia y deshace la escritura. La razon "
             "real para validar en `BEFORE` es otra y es mejor: es el unico momento en que "
             "todavia se puede decidir. Ahi se puede vetar la fila, o incluso **corregirla** "
             "devolviendo un `NEW` modificado, y se evita el trabajo de escribir e indexar un dato "
             "que se va a rechazar. El `AFTER` llega cuando ya no hay nada que decidir, y por eso "
             "es el lugar de la auditoria: audita lo que **quedo**, no lo que se intento."),
            ("¿Por que mi `UPDATE` responde «UPDATE 0» y no da ningun error?",
             "A la funcion del trigger `BEFORE` le falta el `RETURN NEW`. En un trigger "
             "`BEFORE ... FOR EACH ROW`, devolver `NULL` significa «descarta esta fila», y el "
             "motor lo hace **en silencio**: sin error, sin aviso, sin cambio. Es el error mas "
             "desconcertante de la clase. Regla: todo trigger `BEFORE` de fila termina en "
             "`RETURN NEW` en el camino valido. En un trigger `AFTER` el retorno se ignora y da "
             "igual devolver `NEW` o `NULL`."),
            ("¿Para que sirve la clausula `WHEN` si puedo poner el mismo `IF` dentro de la "
             "funcion?",
             "El resultado visible es el mismo y las dos son correctas; la diferencia es donde se "
             "toma la decision. Con la clausula `WHEN`, el motor evalua la condicion y **ni "
             "siquiera llama** a la funcion; con el `IF` adentro, la llama, entra, evalua y sale. "
             "En un `UPDATE` de una fila no se nota; en una carga de 50 000 citas son 50 000 "
             "llamadas a una funcion que no va a hacer nada. Ademas la condicion queda visible en "
             "la definicion del trigger, que es donde alguien la va a buscar."),
            ("¿Y por que `IS DISTINCT FROM` y no `<>`?",
             "Por los nulos. `'A' <> NULL` no da verdadero ni falso: da `NULL`, y un `WHEN` que "
             "evalua a `NULL` no se cumple, asi que ese cambio **no se auditaria**. "
             "`IS DISTINCT FROM` trata el nulo como un valor mas y devuelve verdadero o falso "
             "siempre. En esta tabla `estado` es `NOT NULL` y da lo mismo, pero la costumbre se "
             "construye ahora: en cuanto se audite una columna que admita nulos, `<>` empieza a "
             "perder cambios sin avisar."),
            ("Si el `CHECK` es mejor, ¿por que el taller me hace escribir el trigger de stock?",
             "Para que veas los dos y puedas elegir. La pregunta 3 corre sobre una base a la que "
             "**le quitamos el `CHECK` a proposito**, para que primero veas el stock en -7 y "
             "despues lo resuelvas con la herramienta que la clase esta ensenando. Pero la "
             "respuesta correcta de diseno es la de la pregunta 4: esa regla mira una sola columna "
             "de la propia fila, asi que en el PI real va en un `CHECK (stock >= 0)`, que es una "
             "linea, no se puede olvidar y el motor aplica sin llamar a ningun codigo. El trigger "
             "se reserva para lo que el `CHECK` no puede: mirar el valor anterior, mirar otra "
             "tabla o dejar historia."),
            ("En el plan de respaldo, ¿`pg_dump` no basta? Es lo unico que hemos visto.",
             "Le faltan dos cosas y las dos duelen. Una: `pg_dump` respalda **una base**, no los "
             "roles ni las contrasenas, que son del cluster; si restauras solo el dump te queda "
             "una base con todos los datos y sin un usuario que la pueda usar, y el "
             "`pg_restore` empieza a fallar al asignar propietarios. Para eso esta "
             "`pg_dumpall --globals-only`. Dos: un dump es una foto de un instante, asi que tu "
             "RPO es «desde el ultimo dump», y con un dump diario eso puede ser un dia entero de "
             "atencion. Bajarlo requiere archivar los WAL o, como minimo, un segundo dump al "
             "mediodia. Escribir «RPO de 15 minutos» con un solo dump diario es escribir un "
             "numero que el plan no puede cumplir."),
        ],
        "cierre": [
            "Al terminar, cada estudiante debe tener: `fn_precio_consulta` creada, `IMMUTABLE` y "
            "usada dentro de dos consultas —con Firulais en 45000 y 60750—; la tabla "
            "`audit_cita` con **2 filas y no 3**; el stock en -7 capturado **antes** del trigger y "
            "el insumo 2 en 1 despues; las cuatro afirmaciones correctas de la pregunta 4; y el "
            "`Plan_Backup_VetCare` con RPO, RTO y la consulta de validacion.",
            "Lo que hay que verificar antes de cerrar la sesion son **dos numeros y una "
            "coherencia**. Los numeros: que la auditoria tenga 2 filas —si tiene 3, falta el "
            "filtro y hay una fila con `PROGRAMADA -> PROGRAMADA`— y que el insumo 2 haya quedado "
            "en 1 y no en 3 —si quedo en 3, el trigger esta bloqueando tambien el descuento "
            "valido, casi siempre por `<= 0`—. La coherencia: que quien marco bien la pregunta 4 "
            "no haya escrito en la 3 que el trigger era la unica forma de proteger el stock. "
            "Proyectar una entrega voluntaria y leer esas tres cosas toma dos minutos y separa a "
            "quien entendio de quien copio la sintaxis.",
            "Dejar dicho en voz alta lo que sigue. El Corte 1 se cierra con el parcial de la "
            "Clase 5, y lo que se evalua de estas cuatro clases es exactamente lo que quedo "
            "escrito: la matriz de roles, el contrato de los procedimientos, la decision entre "
            "`CHECK`, trigger y aplicacion, y el plan de respaldo con su gap declarado. Y la "
            "Clase 6 arranca donde termino hoy la pregunta 1: la diferencia entre lo cobrado y la "
            "tarifa de referencia, que ahi se convierte en una consulta de control y en el primer "
            "problema de rendimiento del semestre.",
        ],
    },

    6: {
        "titulo": "Solucion del taller · Clase 6 · Optimizacion de consultas de VetCare (antes / despues)",
        "resumen": (
            "Las dos consultas del PI reescritas y medidas sobre las 30.010 citas reales de la "
            "base: la agenda del dia con sus cuatro antipatrones corregidos y las **91 filas** "
            "que las dos versiones tienen que devolver, la evidencia del `EXPLAIN ANALYZE` leida "
            "e interpretada —incluida la parte incomoda, que sin indice las dos versiones siguen "
            "leyendo las 30.010 filas—, la subconsulta correlacionada de 2.006 ejecuciones "
            "convertida en una sola pasada con la prueba de equivalencia por `EXCEPT`, y la "
            "justificacion tecnica que va al informe."
        ),
        "total": 100,
        "nota_actividad": (
            "**El motor es PostgreSQL, no Oracle:** aqui se lee `EXPLAIN (ANALYZE, BUFFERS)` con "
            "sus nodos `Seq Scan`, `Hash Join` y `Nested Loop`, no un `AUTOTRACE` ni un "
            "`TKPROF`. Tres avisos operativos que conviene dar antes de arrancar. Primero: la "
            "base de este taller **si tiene volumen** —2.006 duenos, 5.008 mascotas, 16 "
            "veterinarios y 30.010 citas, con `ANALYZE` ya corrido y **sin ningun indice** mas "
            "alla de las llaves primarias—, asi que las mediciones significan algo. Segundo: la "
            "version ANTES de la pregunta 3 ejecuta una subconsulta 2.006 veces y en el navegador "
            "**puede tardar de varios segundos a mas de un minuto**; no esta colgada, y hay que "
            "decirlo o media clase va a recargar la pagina. Tercero: los milisegundos que "
            "aparecen en esta solucion son de una corrida de referencia y **cambian en cada "
            "maquina**; lo que no cambia son los conteos de filas, y por eso los conteos son lo "
            "que se califica."
        ),
        "preguntas": [
            {
                "n": 1,
                "titulo": "Reescribir la consulta de agenda del dia",
                "tipo": "bd_sql",
                "puntos": 30,
                "sql": """-- =====================================================================
    -- ANTES: la version con los cuatro antipatrones, tal como la escribio
    -- quien la programo. Se corre primero para tener la linea base y, sobre
    -- todo, el numero de filas que la version nueva esta obligada a igualar.
    -- =====================================================================
    SELECT *
    FROM cita c, mascota m, dueno d, veterinario v
    WHERE c.id_mascota = m.id_mascota
      AND m.id_dueno = d.id_dueno
      AND c.id_veterinario = v.id_veterinario
      AND to_char(c.fecha_hora, 'YYYY-MM-DD') = '2026-03-10'
      AND UPPER(c.estado) = 'PROGRAMADA';

    -- =====================================================================
    -- DESPUES: la misma informacion util, con los cuatro antipatrones
    -- corregidos. Cada correccion va comentada con su razon.
    -- =====================================================================
    SELECT c.id_cita,                    -- (1) PROYECCION: seis columnas en vez
           c.fecha_hora,                 --     de las ~20 que traia SELECT *.
           m.nombre AS mascota,          --     Menos bytes por fila en el join,
           d.nombre AS dueno,            --     en el ordenamiento y en la red.
           v.nombre AS veterinario,
           c.estado
      FROM cita c
      -- (2) JOIN ... ON explicitos. No hacen la consulta mas rapida -- el plan
      --     es identico -- pero separan la condicion de union de la condicion
      --     de filtro, y asi no se puede "perder" un ON y producir un
      --     producto cartesiano de 30.010 x 5.008 filas sin darse cuenta.
      JOIN mascota     m ON m.id_mascota     = c.id_mascota
      JOIN dueno       d ON d.id_dueno       = m.id_dueno
      JOIN veterinario v ON v.id_veterinario = c.id_veterinario
      -- (3) PREDICADO DE RANGO. La columna queda sola a la izquierda del
      --     operador: eso es lo que la vuelve *sargable*. Con
      --     to_char(fecha_hora, ...) el motor tiene que calcular la funcion
      --     para las 30.010 filas antes de poder comparar, y ademas no puede
      --     estimar cuantas van a pasar. Se usa >= y < , no BETWEEN, para no
      --     tener que pensar si la medianoche del 11 entra o no.
     WHERE c.fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
       AND c.fecha_hora <  TIMESTAMP '2026-03-11 00:00:00'
      -- (4) COMPARACION DIRECTA. El dominio ya esta normalizado por el
      --     CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA')), asi que
      --     UPPER() no protege de nada y solo estorba: con la columna desnuda,
      --     el motor puede usar sus estadisticas de valores frecuentes.
       AND c.estado = 'PROGRAMADA'
     ORDER BY c.fecha_hora, c.id_cita;   -- id_cita como desempate: ver abajo

    -- =====================================================================
    -- EQUIVALENCIA: optimizar no puede cambiar el resultado. Los dos conteos
    -- tienen que dar el mismo numero.
    -- =====================================================================
    SELECT COUNT(*) AS filas_antes
    FROM cita c, mascota m, dueno d, veterinario v
    WHERE c.id_mascota = m.id_mascota
      AND m.id_dueno = d.id_dueno
      AND c.id_veterinario = v.id_veterinario
      AND to_char(c.fecha_hora, 'YYYY-MM-DD') = '2026-03-10'
      AND UPPER(c.estado) = 'PROGRAMADA';

    SELECT COUNT(*) AS filas_despues
      FROM cita c
      JOIN mascota     m ON m.id_mascota     = c.id_mascota
      JOIN dueno       d ON d.id_dueno       = m.id_dueno
      JOIN veterinario v ON v.id_veterinario = c.id_veterinario
     WHERE c.fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
       AND c.fecha_hora <  TIMESTAMP '2026-03-11 00:00:00'
       AND c.estado = 'PROGRAMADA';

    -- =====================================================================
    -- Y la version de una sola linea, que es la que conviene pegar al
    -- corregir: si la diferencia no es 0, la reescritura cambio el resultado.
    -- =====================================================================
    SELECT (SELECT COUNT(*) FROM cita c
             WHERE to_char(c.fecha_hora, 'YYYY-MM-DD') = '2026-03-10'
               AND UPPER(c.estado) = 'PROGRAMADA')            AS antes,
           (SELECT COUNT(*) FROM cita c
             WHERE c.fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
               AND c.fecha_hora <  TIMESTAMP '2026-03-11 00:00:00'
               AND c.estado = 'PROGRAMADA')                   AS despues,
           (SELECT COUNT(*) FROM cita
             WHERE fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
               AND fecha_hora <  TIMESTAMP '2026-03-11 00:00:00') AS ese_dia_en_total;""",
                "salida": """Version DESPUES -- 91 filas

     id_cita |     fecha_hora      |   mascota    |   dueno    |  veterinario   |   estado
    ---------+---------------------+--------------+------------+----------------+------------
          74 | 2026-03-10 08:45:00 | Mascota 57   | Dueno 52   | Veterinario 1  | PROGRAMADA
        1874 | 2026-03-10 08:45:00 | Mascota 1857 | Dueno 1852 | Veterinario 1  | PROGRAMADA
        3674 | 2026-03-10 08:45:00 | Mascota 3657 | Dueno 1652 | Veterinario 1  | PROGRAMADA
        5474 | 2026-03-10 08:45:00 | Mascota 457  | Dueno 452  | Veterinario 1  | PROGRAMADA
         ... 87 filas mas ...
       28674 | 2026-03-10 14:00:00 | Mascota 3657 | Dueno 1652 | Veterinario 5  | PROGRAMADA

    Equivalencia -- 1 fila

     antes | despues | ese_dia_en_total
    -------+---------+------------------
        91 |      91 |              150

    Reparto de las 91 por franja horaria (mismo dato, agrupado):

     08:45 -> 15    09:30 -> 15    11:00 -> 15
     11:45 -> 16    13:15 -> 15    14:00 -> 15""",
                "nota_salida": """**91 es el numero de la pregunta.** Es el que hay que buscar en cualquier
entrega, y no depende de la maquina: el 2026-03-10 tiene 150 citas —150 por dia en
toda la base— y de esas 91 estan PROGRAMADA, 45 ATENDIDA y 14 CANCELADA. Si un
estudiante reporta 150, se le olvido el filtro de estado; si reporta 0, casi siempre
escribio `BETWEEN '2026-03-10' AND '2026-03-10'`, que con TIMESTAMP solo atrapa la
medianoche exacta.

Son **seis** franjas y no nueve, y el detalle tiene explicacion: la base genera las
horas en pasos de 45 minutos y hace ATENDIDA una de cada tres citas, y las tres
franjas que caen en los multiplos —08:00, 10:15 y 12:30— quedan todas ATENDIDA o
CANCELADA. No es un error de nadie.

**Sobre el `ORDER BY`:** el enunciado pide ordenar por `c.fecha_hora`, y con eso solo
hay entre 15 y 16 filas **empatadas** dentro de cada franja, cuyo orden el motor no
garantiza. Dos corridas de la misma consulta pueden imprimir la agenda en distinto
orden. Por eso esta solucion agrega `, c.id_cita`: no se exige, y no se descuenta por
no tenerlo, pero es lo que hace que la evidencia del estudiante sea reproducible y
vale la pena senalarlo en la devolucion.""",
                "como_calificar": [
                    "**16 pts — los cuatro antipatrones corregidos, 4 pts cada uno.** "
                    "(1) La proyeccion con las seis columnas y los alias `mascota`, `dueno`, "
                    "`veterinario` exactos. (2) Los tres `JOIN ... ON` explicitos. (3) El "
                    "**predicado de rango** con `>=` y `<` y la columna sola a la izquierda. "
                    "(4) `c.estado = 'PROGRAMADA'` sin `UPPER`. Los 4 pts del punto 3 son los que "
                    "mas se pierden y los que mas importan: es el unico cambio que habilita el "
                    "indice de la Clase 7.",
                    "**4 pts — `ORDER BY c.fecha_hora`.** Se dan completos con la columna pedida. "
                    "Se anota como observacion —sin puntos extra— si el estudiante agrego un "
                    "desempate: con solo `fecha_hora` hay 15 o 16 filas empatadas por franja y el "
                    "orden dentro de cada una no esta garantizado.",
                    "**6 pts — la version ANTES se ejecuto** y quedo como linea base, tal cual, "
                    "sin «arreglarla» de paso. Sin la linea base la comparacion de la pregunta 2 "
                    "no tiene contra que medirse.",
                    "**4 pts — los dos `COUNT(*)` coinciden y valen 91.** 2 pts que esten los dos "
                    "conteos y 2 pts que el numero sea 91. Si coinciden pero valen 150 o 0, la "
                    "equivalencia esta demostrada y el filtro esta mal: se dan los 2 primeros y "
                    "no los otros 2.",
                    "**Se descuenta segun la rubrica** si queda `SELECT *`, si sobrevive cualquier "
                    "funcion sobre `fecha_hora` en el `WHERE`, o si el conteo difiere del de la "
                    "version ANTES. Lo ultimo es lo mas grave de los tres y conviene decirlo asi: "
                    "una consulta mas rapida que devuelve otra cosa no esta optimizada, esta "
                    "rota.",
                    "**Bono conceptual, sin puntos, y es el mejor de la clase:** quien escriba que "
                    "el predicado de rango **todavia no evita el `Seq Scan`**, porque no hay "
                    "ningun indice sobre `fecha_hora`, y que lo que gana hoy es dejar de calcular "
                    "la funcion 30.010 veces y darle al planeador una estimacion correcta, "
                    "entendio la clase completa y ya escribio la seccion 4 de la pregunta 5.",
                ],
                "errores": [
                    "**`BETWEEN '2026-03-10' AND '2026-03-10'`** para «el dia». Devuelve **0 "
                    "filas** y es el error mas comun del semestre: el literal se convierte a "
                    "`2026-03-10 00:00:00` y solo atrapa la medianoche exacta. La variante "
                    "`BETWEEN '2026-03-10' AND '2026-03-11'` es peor todavia, porque **si** "
                    "devuelve algo pero se lleva de contrabando las citas de la medianoche del 11. "
                    "Con `>=` y `<` el problema no existe y no hay que pensarlo.",
                    "**Cambiar `to_char(...)` por `DATE(c.fecha_hora) = '2026-03-10'`** o por "
                    "`EXTRACT`. Es mas corto y **mantiene intacto el antipatron**: sigue habiendo "
                    "una funcion envolviendo la columna, la sargabilidad sigue perdida y los 4 pts "
                    "no se dan. Vale explicar la regla en una frase: la columna tiene que quedar "
                    "**sola** a la izquierda del operador.",
                    "**Dejar `SELECT *` y solo cambiar las comas por `JOIN`.** Es media entrega y "
                    "se detecta al instante porque la salida trae unas veinte columnas, con "
                    "`id_mascota` repetido tres veces. La rubrica lo penaliza de forma explicita.",
                    "**Perder un `ON` al convertir las comas.** Produce un producto cartesiano "
                    "silencioso: en vez de 91 filas salen decenas de miles, y en el navegador el "
                    "sintoma es que la pestana se congela. Es justamente el accidente que los "
                    "`JOIN ... ON` explicitos existen para prevenir, asi que conviene usar el "
                    "error para justificar el antipatron 2.",
                    "**Cambiar el resultado y no notarlo.** Las dos variantes tipicas: agregar "
                    "`AND m.activa = 'S'` «para que sea mas util» —quedan menos de 91 filas— o "
                    "convertir un `JOIN` en `LEFT JOIN` «por seguridad» —quedan mas—. Las dos son "
                    "mejoras de negocio, no optimizaciones, y las dos rompen la equivalencia. Si "
                    "el estudiante quiere el filtro, va en una consulta aparte.",
                    "**Reportar el numero de filas sin haberlo medido.** Se reconoce porque el "
                    "numero es redondo: 150, 100, 90. El unico numero correcto es **91**, y sale "
                    "solo de correr la consulta.",
                ],
            },
            {
                "n": 2,
                "titulo": "Medir con EXPLAIN ANALYZE: la evidencia del antes/despues",
                "tipo": "bd_sql",
                "puntos": 20,
                "sql": """-- =====================================================================
    -- 1) EXPLAIN de la version ANTES. Se pega la consulta con antipatrones
    --    tal cual, sin tocar nada: es la linea base.
    -- =====================================================================
    EXPLAIN (ANALYZE, BUFFERS)
    SELECT *
    FROM cita c, mascota m, dueno d, veterinario v
    WHERE c.id_mascota = m.id_mascota
      AND m.id_dueno = d.id_dueno
      AND c.id_veterinario = v.id_veterinario
      AND to_char(c.fecha_hora, 'YYYY-MM-DD') = '2026-03-10'
      AND UPPER(c.estado) = 'PROGRAMADA';

    -- =====================================================================
    -- 2) EXPLAIN de la version DESPUES.
    -- =====================================================================
    EXPLAIN (ANALYZE, BUFFERS)
    SELECT c.id_cita, c.fecha_hora, m.nombre AS mascota, d.nombre AS dueno,
           v.nombre AS veterinario, c.estado
      FROM cita c
      JOIN mascota     m ON m.id_mascota     = c.id_mascota
      JOIN dueno       d ON d.id_dueno       = m.id_dueno
      JOIN veterinario v ON v.id_veterinario = c.id_veterinario
     WHERE c.fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
       AND c.fecha_hora <  TIMESTAMP '2026-03-11 00:00:00'
       AND c.estado = 'PROGRAMADA'
     ORDER BY c.fecha_hora, c.id_cita;

    -- =====================================================================
    -- 3) DESPUES + LIMIT 50, que es lo que de verdad necesita la pantalla de
    --    agenda: la recepcionista ve medio dia, no las 91 citas de golpe.
    -- =====================================================================
    EXPLAIN ANALYZE
    SELECT c.id_cita, c.fecha_hora, m.nombre AS mascota, d.nombre AS dueno,
           v.nombre AS veterinario, c.estado
      FROM cita c
      JOIN mascota     m ON m.id_mascota     = c.id_mascota
      JOIN dueno       d ON d.id_dueno       = m.id_dueno
      JOIN veterinario v ON v.id_veterinario = c.id_veterinario
     WHERE c.fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
       AND c.fecha_hora <  TIMESTAMP '2026-03-11 00:00:00'
       AND c.estado = 'PROGRAMADA'
     ORDER BY c.fecha_hora, c.id_cita
     LIMIT 50;

    -- =====================================================================
    -- LECTURA DEL PLAN. Los conteos de filas son los de esta base y no
    -- cambian; los milisegundos son de una corrida de referencia.
    -- =====================================================================
    -- VERSION       | nodo mas costoso                        | filas est. vs reales | tiempo (ms)
    -- ANTES         | Seq Scan on cita, Filter: to_char()+upper(), Rows Removed by Filter: 29919 | rows=1 vs 91 -> el planeador se equivoco por un factor de ~91 | 118
    -- DESPUES       | Seq Scan on cita, Filter: rango de fecha_hora + estado, Rows Removed by Filter: 29919 | rows=90 vs 91 -> error menor al 2 % | 41
    -- DESPUES+LIM50 | el mismo Seq Scan; el LIMIT no lo evita porque el ORDER BY no tiene indice | 50 de 91 | 39
    --
    -- CONCLUSION: factor de mejora de aproximadamente 2,9x (118 -> 41 ms) en este
    -- entorno. NO es un orden de magnitud, y la razon es la parte honesta del
    -- ejercicio: sin ningun indice sobre fecha_hora, las DOS versiones recorren
    -- las 30.010 filas de cita y descartan las mismas 29.919. Lo que la version
    -- DESPUES si elimina son 60.020 llamadas a funcion (to_char y upper, una vez
    -- por fila cada una), unas 14 columnas de acarreo por fila en los joins y en
    -- el ordenamiento, y -- lo mas importante para el plan -- el error de
    -- estimacion: con rows=1 el planeador cree que va a unir una sola cita y
    -- elige la forma de join equivocada. El salto grande queda pendiente para la
    -- Clase 7: con un indice sobre (fecha_hora, estado) el Seq Scan de 30.010
    -- filas se convierte en un Index Scan de ~150, y ese si es el orden de
    -- magnitud.

    -- =====================================================================
    -- Comprobacion opcional que hace visible el error de estimacion sin tener
    -- que leer el plan completo: el mismo filtro, primero envuelto en
    -- funciones y luego desnudo.
    -- =====================================================================
    EXPLAIN ANALYZE SELECT COUNT(*) FROM cita c
     WHERE to_char(c.fecha_hora, 'YYYY-MM-DD') = '2026-03-10'
       AND UPPER(c.estado) = 'PROGRAMADA';

    EXPLAIN ANALYZE SELECT COUNT(*) FROM cita c
     WHERE c.fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
       AND c.fecha_hora <  TIMESTAMP '2026-03-11 00:00:00'
       AND c.estado = 'PROGRAMADA';""",
                "salida": """Version ANTES -- forma del plan (los nombres de los nodos son los que hay que
    reconocer; el reparto entre Hash Join y Nested Loop puede variar):

    Nested Loop  (cost=... rows=1 width=...) (actual time=... rows=91 loops=1)
      Buffers: shared hit=...
      ->  Nested Loop  ... (actual rows=91 loops=1)
            ->  Nested Loop  ... (actual rows=91 loops=1)
                  ->  Seq Scan on cita c  (cost=0.00..1050.25 rows=1 width=...)
                                          (actual time=... rows=91 loops=1)
                        Filter: ((to_char(fecha_hora, 'YYYY-MM-DD'::text) = '2026-03-10'::text)
                                 AND (upper(estado) = 'PROGRAMADA'::text))
                        Rows Removed by Filter: 29919
                  ->  Index Scan using mascota_pkey on mascota m  (actual rows=1 loops=91)
            ->  Index Scan using dueno_pkey on dueno d  (actual rows=1 loops=91)
      ->  Index Scan using veterinario_pkey on veterinario v  (actual rows=1 loops=91)
    Execution Time: 118.4 ms

    Version DESPUES -- misma forma, dos diferencias que si importan:

    Sort  (actual rows=91 loops=1)
      Sort Key: c.fecha_hora, c.id_cita
      ->  Nested Loop  (cost=... rows=90 width=...) (actual rows=91 loops=1)
            ->  Seq Scan on cita c  (cost=0.00..750.15 rows=90 width=...)
                                    (actual time=... rows=91 loops=1)
                  Filter: ((fecha_hora >= '2026-03-10 00:00:00'::timestamp)
                           AND (fecha_hora < '2026-03-11 00:00:00'::timestamp)
                           AND (estado = 'PROGRAMADA'::text))
                  Rows Removed by Filter: 29919
            ->  ... los mismos tres Index Scan por llave primaria ...
    Execution Time: 41.2 ms""",
                "nota_salida": """Los cuatro numeros que hay que saber leer en esta salida, y **solo los tres
primeros son deterministas**:

1. **`Rows Removed by Filter: 29919`, igual en las dos.** Es la parte incomoda y es
   la mas instructiva: sin indice, las dos versiones leen las 30.010 filas y tiran
   las mismas 29.919. El predicado sargable **por si solo** no evita el `Seq Scan`;
   lo que hace es dejar la puerta abierta para el indice de la Clase 7. Un estudiante
   que reporte «desaparecio el Seq Scan» no leyo su plan.
2. **`rows=1` estimadas contra `rows=91` reales, en la version ANTES.** Ese 1 no es
   casualidad: cuando el filtro es una funcion sobre la columna, el motor no tiene
   estadisticas y aplica una selectividad por omision del 0,5 % por cada condicion;
   30.010 x 0,005 x 0,005 da 0,75, que se redondea a 1. Con el predicado desnudo usa
   el histograma de `fecha_hora` y la lista de valores frecuentes de `estado`, y
   estima ~90 contra 91 reales.
3. **El plan del `LIMIT 50` conserva el `Seq Scan` completo.** Tiene que conservarlo:
   para saber cuales son las 50 primeras por `fecha_hora` sin un indice que ya venga
   ordenado, hay que encontrar y ordenar las 91. El `LIMIT` solo ahorra el transporte
   de 41 filas. Es el segundo argumento para el indice de la Clase 7.
4. **`Execution Time`.** Aqui 118 -> 41 ms, un factor de 2,9x. **Este es el unico
   numero que cambia de maquina a maquina** y en el navegador puede variar el doble
   entre dos corridas seguidas. Se acepta cualquier factor entre 1,5x y 3x; lo que no
   se acepta es un factor inventado.

Si el entorno rechaza la opcion `BUFFERS`, se corre `EXPLAIN ANALYZE` a secas y se
dice en la pregunta 5, tal como autoriza el enunciado. Cuando si funciona, el dato que
importa es que el `shared hit` del `Seq Scan on cita` es del mismo orden en las dos
versiones -- otra vez: se leen los mismos bloques.""",
                "como_calificar": [
                    "**6 pts — los tres `EXPLAIN` corren y corresponden.** 2 pts cada uno. El "
                    "tercero, la variante con `LIMIT 50`, es el que mas se olvida y la rubrica lo "
                    "nombra de forma explicita.",
                    "**9 pts — la tabla en comentarios, 3 pts por columna.** Nodo mas costoso, "
                    "filas estimadas contra reales, y tiempo de ejecucion, **para las tres "
                    "versiones**: la columna se da completa cuando estan ANTES, DESPUES y "
                    "DESPUES+LIM50, y vale 2 de 3 si falta la fila del `LIMIT 50`. La exigencia "
                    "de la rubrica es que los valores esten **tomados del plan real**: se "
                    "verifica con dos anclas que no se pueden adivinar, el "
                    "`Rows Removed by Filter: 29919` y las 91 filas reales.",
                    "**3 pts — la linea `-- CONCLUSION:` cuantifica la mejora.** Basta un factor "
                    "aproximado con los dos tiempos que lo sustentan. **Un factor pequeno y "
                    "honesto vale los 3 pts completos**, y un 50x sin dos tiempos que lo respalden "
                    "vale 0: en esta base, sin indices, el factor real esta entre 1,5x y 3x.",
                    "**2 pts — la interpretacion, no el volcado.** La rubrica descuenta si solo se "
                    "pega el plan. Se dan los 2 pts cuando hay al menos una frase que explique "
                    "**por que** el numero es el que es, y no solo cual es.",
                    "**Se reconoce como sobresaliente, sin puntos extra pero se anota en la "
                    "devolucion:** senalar que el `Seq Scan` **no desaparecio** y explicar que sin "
                    "indice no puede desaparecer. Es la lectura correcta del plan y es exactamente "
                    "lo contrario de lo que el estudiante espera encontrar, asi que solo llega ahi "
                    "quien de verdad leyo.",
                    "**No se califican los milisegundos.** Varian por maquina, por navegador y "
                    "entre dos corridas seguidas. Se califica que esten, que sean coherentes entre "
                    "si y que sustenten el factor declarado.",
                ],
                "errores": [
                    "**Pegar los tres planes completos y nada mas.** Es el error que la rubrica "
                    "penaliza de frente. Un volcado no es evidencia: la evidencia es la tabla de "
                    "cuatro campos que el enunciado pide, y esa tabla obliga a **elegir** que "
                    "numero importa.",
                    "**Inventar los numeros.** Se detecta con dos preguntas: ¿cuantas filas "
                    "descarto el filtro? —tiene que decir 29.919— y ¿cuantas filas reales "
                    "devolvio? —91—. Quien invento el plan casi siempre pone 150, o un numero "
                    "redondo, o el mismo `Rows Removed` distinto en las dos versiones.",
                    "**Escribir «el `Seq Scan` desaparecio».** No desaparecio y no podia "
                    "desaparecer: no hay ningun indice sobre `fecha_hora` en esta base. Es la "
                    "confusion mas frecuente de la clase y viene de esperar el resultado en vez de "
                    "leerlo. La correccion es una pregunta: ¿que indice usaria el motor, si no hay "
                    "ninguno?",
                    "**Reportar un factor de 50x o 100x.** Suele venir de comparar la primera "
                    "corrida de la version ANTES —con la cache fria y el motor recien arrancado— "
                    "contra la tercera de la version DESPUES. La forma correcta de medir es "
                    "alternar: ANTES, DESPUES, ANTES, DESPUES, y quedarse con la segunda de cada "
                    "una.",
                    "**Confundir `cost=` con tiempo.** El `cost` es una unidad interna y "
                    "arbitraria del planeador, no milisegundos ni bytes. El tiempo esta en "
                    "`actual time=` de cada nodo y en el `Execution Time` del final. Comparar "
                    "costes entre dos consultas distintas casi nunca dice nada util.",
                    "**Omitir el `EXPLAIN` con `LIMIT 50`,** o cambiarlo por un `LIMIT` sin "
                    "`ORDER BY`. Sin el `ORDER BY` el `LIMIT` **si** puede cortar el escaneo "
                    "temprano y el plan deja de mostrar lo que la pregunta quiere ensenar: que un "
                    "`LIMIT` con `ORDER BY` y sin indice no ahorra el trabajo, solo el transporte.",
                ],
            },
            {
                "n": 3,
                "titulo": "Matar la subconsulta correlacionada del reporte de duenos",
                "tipo": "bd_sql",
                "puntos": 20,
                "sql": """-- =====================================================================
    -- ANTES: una subconsulta en la lista de columnas. Se evalua UNA VEZ POR
    -- CADA FILA de dueno, es decir 2.006 veces, y cada una de esas veces une
    -- las 30.010 citas con las 5.008 mascotas. AVISO: en el navegador esto
    -- puede tardar de varios segundos a mas de un minuto. No esta colgado.
    -- =====================================================================
    SELECT d.id_dueno,
           d.nombre,
           (SELECT COUNT(*)
              FROM cita c
              JOIN mascota m ON m.id_mascota = c.id_mascota
             WHERE m.id_dueno = d.id_dueno) AS total_citas
    FROM dueno d
    ORDER BY total_citas DESC;

    EXPLAIN ANALYZE
    SELECT d.id_dueno,
           d.nombre,
           (SELECT COUNT(*)
              FROM cita c
              JOIN mascota m ON m.id_mascota = c.id_mascota
             WHERE m.id_dueno = d.id_dueno) AS total_citas
    FROM dueno d
    ORDER BY total_citas DESC;

    -- =====================================================================
    -- DESPUES: una sola pasada. Los dos LEFT JOIN y el COUNT de la COLUMNA
    -- son las dos decisiones de la pregunta:
    --   * LEFT JOIN, porque un dueno sin mascotas -- o con mascotas sin citas
    --     -- tiene que seguir apareciendo con cero. Con INNER JOIN
    --     desaparecen seis duenos del reporte.
    --   * COUNT(c.id_cita) y NO COUNT(*), porque el LEFT JOIN fabrica una
    --     fila con NULL para el dueno sin citas: COUNT(*) contaria esa fila
    --     fantasma y diria 1. COUNT de una columna ignora los NULL y dice 0.
    -- =====================================================================
    SELECT d.id_dueno,
           d.nombre,
           COUNT(c.id_cita) AS total_citas
      FROM dueno d
      LEFT JOIN mascota m ON m.id_dueno    = d.id_dueno
      LEFT JOIN cita    c ON c.id_mascota  = m.id_mascota
     GROUP BY d.id_dueno, d.nombre
     ORDER BY total_citas DESC, d.id_dueno
     LIMIT 20;

    EXPLAIN ANALYZE
    SELECT d.id_dueno,
           d.nombre,
           COUNT(c.id_cita) AS total_citas
      FROM dueno d
      LEFT JOIN mascota m ON m.id_dueno    = d.id_dueno
      LEFT JOIN cita    c ON c.id_mascota  = m.id_mascota
     GROUP BY d.id_dueno, d.nombre
     ORDER BY total_citas DESC, d.id_dueno
     LIMIT 20;

    -- =====================================================================
    -- EQUIVALENCIA con EXCEPT en los DOS sentidos, sin LIMIT. EXCEPT no es
    -- simetrico: A EXCEPT B vacio solo dice que A no tiene nada que B no
    -- tenga. Hacen falta las dos direcciones para probar la igualdad de los
    -- conjuntos, y por eso se unen con UNION ALL: el resultado correcto es
    -- CERO FILAS.
    -- =====================================================================
    (
      SELECT d.id_dueno,
             (SELECT COUNT(*)
                FROM cita c JOIN mascota m ON m.id_mascota = c.id_mascota
               WHERE m.id_dueno = d.id_dueno) AS total_citas
        FROM dueno d
      EXCEPT
      SELECT d.id_dueno, COUNT(c.id_cita)
        FROM dueno d
        LEFT JOIN mascota m ON m.id_dueno   = d.id_dueno
        LEFT JOIN cita    c ON c.id_mascota = m.id_mascota
       GROUP BY d.id_dueno
    )
    UNION ALL
    (
      SELECT d.id_dueno, COUNT(c.id_cita)
        FROM dueno d
        LEFT JOIN mascota m ON m.id_dueno   = d.id_dueno
        LEFT JOIN cita    c ON c.id_mascota = m.id_mascota
       GROUP BY d.id_dueno
      EXCEPT
      SELECT d.id_dueno,
             (SELECT COUNT(*)
                FROM cita c JOIN mascota m ON m.id_mascota = c.id_mascota
               WHERE m.id_dueno = d.id_dueno) AS total_citas
        FROM dueno d
    );

    -- =====================================================================
    -- Y la comprobacion corta, para el momento de calificar: los seis duenos
    -- sin ninguna cita tienen que decir 0, no 1.
    -- =====================================================================
    SELECT d.id_dueno, d.nombre, COUNT(c.id_cita) AS total_citas
      FROM dueno d
      LEFT JOIN mascota m ON m.id_dueno   = d.id_dueno
      LEFT JOIN cita    c ON c.id_mascota = m.id_mascota
     GROUP BY d.id_dueno, d.nombre
    HAVING COUNT(c.id_cita) = 0
     ORDER BY d.id_dueno;""",
                "salida": """Version DESPUES -- 20 filas

     id_dueno |     nombre     | total_citas
    ----------+----------------+-------------
            3 | Marcela Diaz   |          33
            1 | Ana Gomez      |          28
            4 | Jorge Pineda   |          26
            5 | Luisa Cardona  |          25
            2 | Carlos Ruiz    |          24
            6 | Andres Vallejo |          24
            7 | Dueno 1        |          18
            8 | Dueno 2        |          18
          ... hasta el id_dueno 20, todos con 18 ...

    Equivalencia -- 0 filas

     (el EXCEPT en los dos sentidos no devolvio ninguna fila)

    Comprobacion de los duenos sin citas -- 6 filas

     id_dueno |  nombre   | total_citas
    ----------+-----------+-------------
         2001 | Dueno 1995|           0
         2002 | Dueno 1996|           0
         2003 | Dueno 1997|           0
         2004 | Dueno 1998|           0
         2005 | Dueno 1999|           0
         2006 | Dueno 2000|           0""",
                "nota_salida": """**El ranking.** Los seis primeros son los duenos sembrados a mano, y tiene
sentido: son los unicos que tienen mascotas de las dos tandas —las 8 sembradas y las
generadas—. Del septimo hacia abajo hay **987 duenos empatados en 18**, asi que el
`ORDER BY total_citas DESC, d.id_dueno` no es un adorno: sin el desempate por
`id_dueno`, las filas 7 a 20 salen distintas en cada corrida y la evidencia del
estudiante no se puede comparar con nada.

**La equivalencia: cero filas es el resultado correcto**, y es la unica forma de
afirmar que las dos versiones son iguales. Si devuelve 6 filas —las de los id_dueno
2001 a 2006— el error esta identificado sin necesidad de leer el codigo: se uso
`COUNT(*)` en vez de `COUNT(c.id_cita)`.

**Las seis filas con 0** son el numero que separa las tres entregas posibles: 6 filas
con 0 = correcto; 6 filas con **1** = se uso `COUNT(*)`; **0 filas** = se uso
`INNER JOIN` y esos seis duenos desaparecieron del reporte. Los tres casos se
distinguen con esta sola consulta.

**Sobre el rendimiento:** la version ANTES ejecuta el `SubPlan` **2.006 veces** y en
cada una recorre las 30.010 citas; el plan lo dice con `loops=2006`. La version
DESPUES es un `HashAggregate` sobre un solo recorrido. Aqui la diferencia si es de
ordenes de magnitud —de segundos a decenas de milisegundos— y no depende de que haya
indices, porque lo que se elimino no fue un escaneo: fueron 2.005 escaneos.""",
                "como_calificar": [
                    "**7 pts — la version DESPUES elimina la correlacion.** 3 pts los dos "
                    "`LEFT JOIN`, 2 pts el `GROUP BY d.id_dueno, d.nombre` y 2 pts "
                    "**`COUNT(c.id_cita)` y no `COUNT(*)`**. Estos ultimos 2 pts son el corazon de "
                    "la pregunta y se verifican con una sola consulta: los duenos 2001 a 2006 "
                    "tienen que decir **0**, no 1.",
                    "**3 pts — el `ORDER BY total_citas DESC, d.id_dueno` y el `LIMIT 20`.** El "
                    "desempate no es cosmetico: hay 987 duenos empatados en 18 y sin el las filas "
                    "7 a 20 cambian entre corridas.",
                    "**4 pts — los dos `EXPLAIN ANALYZE`** corren y se aprecia la diferencia de "
                    "plan. El ancla verificable es el `loops=2006` del `SubPlan` en la version "
                    "ANTES: quien lo cita, lo leyo.",
                    "**6 pts — la prueba de equivalencia con `EXCEPT` en los dos sentidos "
                    "devuelve cero filas.** 4 pts que este la prueba con las dos direcciones y "
                    "2 pts que el resultado sea cero. Un `EXCEPT` en un solo sentido vale 2 de los "
                    "6, y conviene explicar por que: `A EXCEPT B` vacio no prueba que B no tenga "
                    "filas extra.",
                    "**Se descuenta segun la rubrica** por usar `INNER JOIN` —que hace desaparecer "
                    "a los seis duenos sin citas— o por omitir la verificacion. El primero es un "
                    "error de resultado, no de rendimiento: el reporte que ve la clinica queda con "
                    "2.000 duenos en vez de 2.006.",
                    "**Bono conceptual, sin puntos:** quien note que esta reescritura mejora sin "
                    "necesidad de ningun indice —porque lo que se elimino no fue un escaneo sino "
                    "2.005 escaneos— entendio la diferencia entre las dos preguntas del taller. "
                    "La pregunta 1 prepara el terreno para un indice; esta se arregla sola.",
                ],
                "errores": [
                    "**`COUNT(*)` en vez de `COUNT(c.id_cita)`.** Es el error firmado de esta "
                    "pregunta. Con `LEFT JOIN`, un dueno sin citas produce **una** fila llena de "
                    "`NULL`, y `COUNT(*)` cuenta filas: reporta 1. `COUNT` de una columna ignora "
                    "los `NULL` y reporta 0. El sintoma es exacto y facil de buscar: los seis "
                    "ultimos duenos dicen 1.",
                    "**`INNER JOIN` en vez de `LEFT JOIN`.** Mas rapido y **mal**: los seis duenos "
                    "sin mascotas desaparecen y el reporte deja de cuadrar con el total de "
                    "clientes de la clinica. Es el mismo principio de la pregunta 1 —optimizar no "
                    "puede cambiar el resultado— y aqui el `EXCEPT` lo delata.",
                    "**`GROUP BY d.id_dueno` sin `d.nombre`,** con `d.nombre` en el `SELECT`. "
                    "PostgreSQL lo acepta porque `id_dueno` es llave primaria y determina "
                    "funcionalmente el resto de la fila, asi que no se descuenta. Pero conviene "
                    "advertirlo: en cuanto se agrupe por algo que **no** sea la llave, el mismo "
                    "codigo falla con `column d.nombre must appear in the GROUP BY clause`.",
                    "**Un solo `EXCEPT`.** `A EXCEPT B` vacio dice que A no tiene nada que B no "
                    "tenga; no dice nada sobre las filas que B pueda tener de mas. El enunciado "
                    "pide los dos sentidos y por eso las dos partes se unen con `UNION ALL`: una "
                    "sola lectura, cero filas.",
                    "**Comparar con `EXCEPT` incluyendo el `LIMIT 20`.** Entonces la prueba solo "
                    "cubre 20 de las 2.006 filas y precisamente **excluye** a los seis duenos con "
                    "cero, que son los que fallan. El enunciado dice «sin `LIMIT`» por esta razon "
                    "exacta.",
                    "**Recargar la pagina porque la version ANTES «se colgo».** No se colgo: son "
                    "2.006 ejecuciones de una consulta que recorre 30.010 filas, y en el navegador "
                    "eso tarda. Vale la pena anunciarlo antes de que empiecen, porque el "
                    "estudiante que recarga pierde el resto de sus respuestas.",
                ],
            },
            {
                "n": 4,
                "titulo": "Antipatrones de consulta en VetCare",
                "tipo": "cerrada_multi",
                "puntos": 10,
                "justificacion": {
                    0: "**Correcta, y es el antipatron 3 de la pregunta 1.** *Sargable* viene de "
                       "«**S**earch **ARG**ument **able**»: el motor solo puede usar un indice "
                       "cuando la columna aparece **sola** a la izquierda del operador. En "
                       "`to_char(fecha_hora, 'YYYY-MM-DD') = '2026-03-10'` el indice esta "
                       "construido sobre `fecha_hora` y la comparacion es sobre otra cosa —el "
                       "texto que devuelve la funcion—, asi que no hay nada que buscar. Se pierde "
                       "dos veces: el motor calcula la funcion 30.010 veces y, ademas, se queda "
                       "sin estadisticas para estimar. La forma correcta es el predicado de "
                       "rango.",
                    1: "**Correcta.** En el join de cuatro tablas de la pregunta 1, `SELECT *` "
                       "arrastra unas veinte columnas —con `id_mascota` repetido tres veces— "
                       "cuando la pantalla usa seis. Ese peso se paga en cada etapa: en el ancho "
                       "de la fila que viaja por los joins, en la memoria del `Sort` —y si no "
                       "cabe, en un archivo temporal en disco— y en los bytes que salen hacia el "
                       "cliente. Ademas rompe el codigo el dia que alguien agregue una columna a "
                       "`cita`.",
                    2: "**Incorrecta, y es la mas importante de descartar de las seis.** "
                       "Optimizar es hacer lo mismo mas rapido; si el resultado cambia, no se "
                       "optimizo nada, se rompio la consulta y encima se rompio sin avisar. Por "
                       "eso el taller exige la prueba de equivalencia dos veces: los dos "
                       "`COUNT(*)` de la pregunta 1 —que valen 91— y el `EXCEPT` vacio de la "
                       "pregunta 3. La velocidad no es un permiso para devolver otra cosa.",
                    3: "**Correcta, y es la pregunta 3 entera.** La subconsulta de la lista de "
                       "columnas se evalua una vez por fila del exterior, y el plan lo dice sin "
                       "ambiguedad: `loops=2006`. Reescrita como `LEFT JOIN` + `GROUP BY` pasa a "
                       "una sola pasada con un `HashAggregate`, y la mejora es de ordenes de "
                       "magnitud sin necesidad de ningun indice, porque lo que se elimino no fue "
                       "un escaneo sino 2.005 escaneos.",
                    4: "**Incorrecta,** y es la que separa a quien entendio de quien memorizo la "
                       "lista de antipatrones. En PostgreSQL, `FROM a, b WHERE a.x = b.x` y "
                       "`FROM a JOIN b ON a.x = b.x` producen **exactamente el mismo plan**: el "
                       "motor las normaliza a la misma representacion interna. Cambiar la coma por "
                       "`JOIN ... ON` **si** vale la pena, pero por otras dos razones: separa la "
                       "condicion de union de la condicion de filtro, y hace evidente cuando falta "
                       "un `ON` —que es como se producen los productos cartesianos accidentales "
                       "de 30.010 x 5.008 filas—. Se gana legibilidad y seguridad, no "
                       "milisegundos.",
                    5: "**Correcta, y es la herramienta de la pregunta 2.** `EXPLAIN` muestra el "
                       "plan **estimado** y no ejecuta nada; `EXPLAIN ANALYZE` lo ejecuta de "
                       "verdad y reporta `actual rows` y `actual time` al lado de las "
                       "estimaciones. Comparar las dos columnas es el diagnostico mas rentable que "
                       "existe: el `rows=1` estimado contra las 91 reales de la version ANTES "
                       "avisa de que el motor esta ciego sobre ese filtro, y una desviacion "
                       "parecida en una consulta normal casi siempre significa `ANALYZE` sin "
                       "correr o estadisticas viejas.",
                },
                "como_calificar": [
                    "**10 pts con las 4 correctas marcadas y ninguna incorrecta**, con puntaje "
                    "proporcional por acierto parcial, tal como dice la rubrica. La plataforma "
                    "calcula el parcial y la clave se lee del banco.",
                    "**La opcion del `JOIN` es el discriminador de la pregunta.** Marcarla es el "
                    "error mas frecuente y el mas comprensible, porque el taller obliga a "
                    "cambiar las comas por `JOIN`. La devolucion tiene que ser precisa: el cambio "
                    "es correcto y obligatorio, pero **no** por velocidad; el plan es identico. Es "
                    "por legibilidad y por no perder un `ON`.",
                    "**La opcion de «puede cambiar el numero de filas» no admite matices.** Si "
                    "alguien la marca, la conversacion no es sobre optimizacion sino sobre que "
                    "significa que una consulta sea correcta. Vale la pena mirar si esa misma "
                    "persona omitio la prueba de equivalencia en las preguntas 1 y 3: casi "
                    "siempre van juntas.",
                    "Si mas de un tercio del grupo falla la de sargabilidad, conviene abrir la "
                    "Clase 7 mostrando en vivo el mismo `EXPLAIN` con y sin el indice sobre "
                    "`fecha_hora`: es un minuto y deja la idea fijada mejor que la definicion.",
                ],
                "errores": [
                    "**Marcar la del `JOIN` como correcta.** Se corrige con el dato, no con la "
                    "teoria: los dos `EXPLAIN` son iguales. Y se aprovecha para dar la razon real "
                    "del cambio, que es la que va al informe.",
                    "**Marcar la de «puede cambiar el resultado».** Es la unica de las seis que "
                    "invalida el trabajo del taller completo. La devolucion mas eficaz es "
                    "devolverle su propio numero: la version ANTES y la DESPUES de su pregunta 1 "
                    "**tienen** que decir 91 las dos.",
                    "**No marcar la del `SELECT *`,** por pensar que «solo son unas columnas mas». "
                    "El costo no esta en leerlas: esta en acarrearlas por tres joins y por un "
                    "`Sort`. Es facil de mostrar con el `width=` que aparece en cada nodo del "
                    "plan, y ese numero esta en su propia evidencia de la pregunta 2.",
                    "**No marcar la de `EXPLAIN` contra `EXPLAIN ANALYZE`,** casi siempre por no "
                    "haber leido la segunda mitad de la frase —la de estimado contra real—. Es la "
                    "parte que mas sirve en el trabajo: la brecha entre las dos columnas es el "
                    "sintoma de estadisticas desactualizadas.",
                ],
            },
            {
                "n": 5,
                "titulo": "Justificacion tecnica del antes/despues (media pagina)",
                "tipo": "abierta",
                "puntos": 20,
                "respuesta": (
                    "**1. Consulta elegida y para que sirve en Huellitas.** La agenda del dia: la "
                    "pantalla que recepcion abre al llegar y vuelve a consultar cada vez que "
                    "entra un paciente, de modo que se ejecuta del orden de **50 a 80 veces por "
                    "jornada** y siempre con alguien esperando delante del mostrador. Es la "
                    "consulta mas ejecutada del PI y por eso es la que se optimiza primero: "
                    "mejorar un reporte mensual habria sido mas facil y no le habria servido a "
                    "nadie.\n\n"
                    "**2. Tres cambios concretos.**\n\n"
                    "- **Cambio 1 — de `to_char(fecha_hora, 'YYYY-MM-DD') = '2026-03-10'` a un "
                    "predicado de rango `>= '2026-03-10 00:00:00' AND < '2026-03-11 00:00:00'`.** "
                    "*Por que mejora:* deja la columna **sargable**, es decir sola a la izquierda "
                    "del operador, y con eso el motor recupera dos cosas: deja de calcular una "
                    "funcion 30.010 veces y vuelve a poder usar el histograma de `fecha_hora` "
                    "para estimar la **cardinalidad** del filtro. *Evidencia:* en el plan ANTES la "
                    "linea del `Seq Scan` dice `rows=1` estimadas contra `actual rows=91`; en el "
                    "plan DESPUES dice `rows=90` contra 91. El error de estimacion paso de un "
                    "factor de 91 a menos del 2 %, y con una estimacion correcta el planeador "
                    "elige bien la forma de los joins en vez de dimensionarlos para una sola "
                    "fila.\n"
                    "- **Cambio 2 — de `SELECT *` a seis columnas proyectadas.** *Por que mejora:* "
                    "la **proyeccion** reduce el ancho de la fila que atraviesa los tres joins y "
                    "el `Sort`. `SELECT *` sobre cuatro tablas trae unas veinte columnas, "
                    "incluidos tres `id_mascota` y datos que la pantalla no muestra —telefono, "
                    "correo, fecha de nacimiento—, y todo eso se copia en cada etapa y se "
                    "transporta al cliente. *Evidencia:* el `width=` del nodo raiz baja de mas de "
                    "150 bytes a unas decenas, y con el baja el trabajo del `Sort`, que es el "
                    "nodo que se lleva la memoria.\n"
                    "- **Cambio 3 — de la subconsulta correlacionada del reporte de duenos a "
                    "`LEFT JOIN` + `GROUP BY`.** *Por que mejora:* baja el **numero de pasadas "
                    "sobre la tabla** de 2.006 a 1. La subconsulta estaba en la lista de columnas, "
                    "asi que se ejecutaba una vez por cada dueno y cada vez recorria las 30.010 "
                    "citas. *Evidencia:* en el plan ANTES el `SubPlan` aparece con `loops=2006`; "
                    "en el plan DESPUES ese nodo **no existe** y en su lugar hay un solo "
                    "`HashAggregate`. Es la unica de las tres mejoras que es de ordenes de "
                    "magnitud, y es la unica que no necesita ningun indice para conseguirlo.\n\n"
                    "**3. Que NO cambio.** El resultado. La agenda del 2026-03-10 devuelve "
                    "**91 filas** en las dos versiones, verificado con un `COUNT(*)` de cada una "
                    "en la misma corrida. El reporte de duenos devuelve los mismos 2.006 pares "
                    "`(id_dueno, total_citas)`, verificado con `EXCEPT` en **ambos sentidos**: "
                    "cero filas. La prueba en un solo sentido no habria servido, porque no detecta "
                    "filas de mas en el segundo conjunto. Y hay un caso que la prueba protege "
                    "expresamente: los seis duenos sin citas —los id 2001 a 2006— siguen "
                    "apareciendo con **0**, que es lo que se pierde con un `INNER JOIN` o se "
                    "falsea con un `COUNT(*)`.\n\n"
                    "**4. Que sigue: el indice de la Clase 7.** "
                    "`CREATE INDEX ix_cita_fecha_estado ON cita (fecha_hora, estado);`, y en ese "
                    "orden. La razon esta en el propio plan de hoy: la version DESPUES sigue "
                    "haciendo un `Seq Scan` de las 30.010 filas y descartando 29.919, porque no "
                    "hay nada que la ayude a llegar directo al dia. Con el indice, ese nodo deberia "
                    "convertirse en un `Index Scan` sobre las ~150 citas del dia, y ademas el "
                    "`Sort` deberia desaparecer, porque el indice ya entrega las filas ordenadas "
                    "por `fecha_hora` —lo que hace que el `LIMIT 50` por fin sirva de algo—. El "
                    "orden de las columnas importa: `fecha_hora` primero porque es el filtro de "
                    "rango, y `estado` despues, para poder afinar sin volver a la tabla. La "
                    "hipotesis se escribe hoy y se **mide** la clase que viene; si el motor decide "
                    "que no le conviene usarlo, eso tambien es un resultado.\n\n"
                    "**5. Limites de la medicion, honestamente.** Se midio sobre PostgreSQL "
                    "compilado a WebAssembly y corriendo **dentro del navegador**, con 30.010 "
                    "citas, un solo usuario y **sin concurrencia**. Cuatro cosas cambiarian en un "
                    "servidor real con millones de citas y varios usuarios:\n\n"
                    "- **Los tiempos absolutos no se pueden trasladar.** El factor de 2,9x "
                    "medido aqui es una comparacion entre dos consultas en el mismo entorno, no "
                    "una prediccion de nada. Entre dos corridas seguidas en el navegador la "
                    "diferencia ya puede ser del doble.\n"
                    "- **La escala favorece a la version optimizada.** Con 30.010 filas la tabla "
                    "entera cabe en memoria y un `Seq Scan` es baratisimo; con millones de citas "
                    "no cabe, hay lectura de disco real y ahi la diferencia entre recorrer todo y "
                    "usar un indice deja de ser de 3x. Lo mismo con la subconsulta correlacionada: "
                    "2.006 iteraciones son lentas, 200.000 son inviables.\n"
                    "- **No se midio el costo de escribir.** Cada indice que se agregue en la "
                    "Clase 7 hay que mantenerlo en cada `INSERT` de `sp_agendar_cita`. En este "
                    "entorno, sin concurrencia, ese costo es invisible; en produccion, con 150 "
                    "citas nuevas al dia y varios indices, no lo es.\n"
                    "- **No hubo bloqueos ni competencia por recursos.** Con varios usuarios, la "
                    "consulta lenta no solo es lenta para quien la lanza: retiene conexiones y "
                    "memoria de ordenamiento que le hacen falta al resto. Ese efecto es "
                    "exactamente el que este entorno **no puede** reproducir, y es el argumento "
                    "principal para optimizar la consulta que se ejecuta 80 veces al dia antes que "
                    "la que se ejecuta una vez al mes.\n\n"
                    "*(La opcion `BUFFERS` se uso donde el entorno la acepto; donde no, se corrio "
                    "`EXPLAIN ANALYZE` a secas, tal como autoriza el enunciado.)*\n\n"
                    "**Archivos del PI:** `06_opt_antes.sql` y `06_opt_despues.sql` en la carpeta "
                    "del proyecto, mas los tres planes guardados como texto en "
                    "`/informe/06-planes.txt`. El plan sirve de evidencia solo si queda guardado: "
                    "en la Clase 7 hay que poder comparar contra el de hoy."
                ),
                "como_calificar": [
                    # Decia «3 pts secciones 1 y 3, y 3 pts la seccion 5», y la seccion 5 ya
                    # tiene sus 2 pts en la cuarta vinneta: quien calificara al pie de la
                    # letra le daba 5 pts a la 5, dejaba la 3 sin calificar y llegaba a 22
                    # sobre 20. El cuerpo de la vinneta solo explica la 1 y la 3, que es lo
                    # que confirma cual de los dos numeros era el equivocado.
                    "**3 pts — la seccion 1, y 3 pts la seccion 3.** La 1 necesita la pantalla "
                    "concreta y una **frecuencia**; «se usa mucho» no vale. La 3 necesita la "
                    "afirmacion de equivalencia **y** el metodo con su resultado (91 = 91, "
                    "`EXCEPT` vacio). Con los 9 de la seccion 2, los 3 de la 4 y los 2 de la 5, "
                    "el desglose suma los 20 puntos de la pregunta.",
                    "**9 pts — los tres cambios, 3 pts cada uno.** Cada cambio se parte en tres: "
                    "1 pt que se diga **que** se cambio, 1 pt **por que** mejora con el "
                    "vocabulario correcto —sargabilidad, proyeccion, cardinalidad, numero de "
                    "pasadas—, y 1 pt la **evidencia anclada al plan**: un nodo que aparecio o "
                    "desaparecio, un `loops=`, un `rows=` estimado contra el real, un tiempo. Un "
                    "cambio sin evidencia vale 2 de 3; una evidencia que no se puede verificar en "
                    "el plan vale 0 de ese punto.",
                    "**3 pts — la seccion 4, el indice propuesto.** 2 pts el `CREATE INDEX` "
                    "concreto sobre las columnas correctas y 1 pt **la razon tomada de su propio "
                    "plan** («sigue habiendo un `Seq Scan` que descarta 29.919 filas»). Un indice "
                    "propuesto «porque acelera las consultas» vale 1 de 3.",
                    "**2 pts — la seccion 5 reconoce los limites del entorno,** nombrando al menos "
                    "dos: el volumen, la ausencia de concurrencia, el navegador como entorno de "
                    "medicion, o el costo de escritura que no se midio. La rubrica pide honestidad "
                    "y aqui se premia: **un informe que admite que midio poco vale mas que uno "
                    "que finge haber medido produccion.**",
                    "**Vocabulario tecnico, transversal.** La rubrica lo exige de forma explicita. "
                    "Se descuenta medio punto por cambio cuando la justificacion es circular "
                    "—«mejora porque es mas eficiente»— aunque la evidencia este bien citada: la "
                    "seccion existe para explicar el mecanismo.",
                    "**Extension.** Media pagina. Se califica que las 5 secciones esten con "
                    "contenido verificable; no se premia la longitud. Y se verifica lo ultimo del "
                    "enunciado, que es facil de olvidar: **los dos archivos `.sql` guardados** en "
                    "la carpeta del PI.",
                ],
                "errores": [
                    "**Justificaciones circulares.** «Cambie `SELECT *` porque es mas eficiente» "
                    "repite la pregunta. La respuesta es el mecanismo: transporta columnas que "
                    "nadie usa a traves de tres joins y de un `Sort`. Es el descuento mas frecuente "
                    "de esta pregunta.",
                    "**Evidencia que no se puede verificar en el plan.** «El tiempo bajo mucho» o "
                    "«se ve mas rapido» no son evidencia. Las que si lo son, y estan en su propia "
                    "pregunta 2: `Rows Removed by Filter: 29919`, `loops=2006`, `rows=1` contra "
                    "`actual rows=91`, el `width=` que bajo.",
                    "**Afirmar que el `Seq Scan` desaparecio.** No desaparecio y no podia: en esta "
                    "base no hay ningun indice sobre `fecha_hora`. Cuando aparece esta frase, casi "
                    "siempre la seccion 4 tambien esta mal, porque el estudiante ya cree que el "
                    "problema esta resuelto y entonces el indice de la Clase 7 le sobra.",
                    "**Proponer un indice sobre `estado`,** o sobre las tres columnas en cualquier "
                    "orden, sin argumento. `estado` tiene tres valores y el 60 % de las filas son "
                    "`PROGRAMADA`: un indice sobre una columna asi casi nunca se usa, porque leer "
                    "el 60 % de la tabla por el indice es mas caro que recorrerla. La columna "
                    "selectiva es `fecha_hora`, y va primera.",
                    "**Declarar la equivalencia sin haberla medido.** «El resultado es el mismo» "
                    "sin el 91 = 91 ni el `EXCEPT` vacio es una promesa, no una verificacion. Es "
                    "exactamente lo que la opcion falsa de la pregunta 4 pone a prueba.",
                    "**Saltarse la seccion 5** o escribirla como formalidad («los resultados "
                    "podrian variar»). Se pide algo concreto: que **si** cambiaria con millones de "
                    "citas y con varios usuarios. Sin eso, el informe presenta como conclusion "
                    "general una medicion de un solo usuario en un navegador.",
                ],
            },
        ],
        "preguntas_frecuentes": [
            ("¿Que significa exactamente «sargable»?",
             "Viene de «**S**earch **ARG**ument **able**»: que el motor pueda usar la condicion "
             "como argumento de busqueda en un indice. La regla practica es de una linea: **la "
             "columna tiene que quedar sola a la izquierda del operador.** `fecha_hora >= X` es "
             "sargable; `to_char(fecha_hora, ...) = X`, `DATE(fecha_hora) = X` y "
             "`EXTRACT(DAY FROM fecha_hora) = X` no lo son, porque el indice esta hecho sobre la "
             "columna y la comparacion es contra el resultado de una funcion. Cambiar `to_char` "
             "por `DATE()` no arregla nada: sigue habiendo una funcion envolviendo la columna."),
            ("Corregi el predicado y el `Seq Scan` sigue ahi. ¿Hice algo mal?",
             "No, esta correcto, y darse cuenta es el mejor resultado del taller. En **esta** base "
             "no hay ningun indice sobre `fecha_hora`, asi que no existe alternativa al recorrido "
             "completo: las dos versiones leen las 30.010 filas y descartan las mismas 29.919. Lo "
             "que si ganaste hoy son tres cosas medibles: 60.020 llamadas a funcion que ya no se "
             "hacen, filas mucho mas angostas viajando por los joins y por el `Sort`, y una "
             "estimacion correcta —de `rows=1` a `rows=90` contra 91 reales—. La sargabilidad es "
             "la condicion **previa** para que el indice de la Clase 7 pueda servir: si dejas el "
             "`to_char`, el indice se crea y el motor lo ignora."),
            ("¿Por que la version ANTES estima `rows=1` si devuelve 91 filas?",
             "Porque el motor no tiene estadisticas sobre `to_char(fecha_hora, ...)` ni sobre "
             "`upper(estado)` —solo las tiene sobre las columnas desnudas—, asi que aplica una "
             "selectividad por omision del 0,5 % a cada condicion de igualdad. La cuenta sale "
             "exacta: 30.010 x 0,005 x 0,005 = 0,75, que se redondea a 1. Y esa estimacion "
             "equivocada no es cosmetica: el planeador dimensiona los joins creyendo que va a "
             "unir **una** cita. Comparar `rows=` estimadas contra `actual rows=` es el "
             "diagnostico mas rentable que existe; en una consulta normal, una brecha asi suele "
             "significar que falta correr `ANALYZE`."),
            ("¿`JOIN ... ON` es mas rapido que separar las tablas con comas?",
             "No. En PostgreSQL las dos formas producen **exactamente el mismo plan**: el motor las "
             "normaliza a la misma representacion interna. Aun asi el cambio es obligatorio en el "
             "taller y vale la pena en el trabajo, por dos razones que no son de velocidad. Una: "
             "separa la condicion de **union** de la condicion de **filtro**, que es la diferencia "
             "entre leer una consulta y descifrarla. Dos: cuando falta un `ON`, el motor te avisa; "
             "cuando falta una condicion en un `WHERE` con comas, te devuelve un producto "
             "cartesiano de 30.010 x 5.008 filas sin decir nada."),
            ("¿Por que `COUNT(c.id_cita)` y no `COUNT(*)`?",
             "Por los duenos sin citas, que son seis en esta base: los id 2001 a 2006. Con "
             "`LEFT JOIN`, un dueno sin citas **si** produce una fila —una fila con todas las "
             "columnas de `cita` en `NULL`— y `COUNT(*)` cuenta filas: reporta **1**. `COUNT` de "
             "una columna ignora los `NULL` y reporta **0**, que es la verdad. Es la razon por la "
             "que la prueba de la pregunta 3 se hace con `EXCEPT`: si usaste `COUNT(*)`, el "
             "`EXCEPT` te devuelve exactamente esas seis filas."),
            ("¿Por que el `EXCEPT` tiene que ir en los dos sentidos?",
             "Porque `EXCEPT` no es simetrico. `A EXCEPT B` vacio solo dice que A no tiene ninguna "
             "fila que B no tenga; no dice nada sobre filas que B pueda tener de mas. Para probar "
             "que los dos conjuntos son **iguales** hacen falta las dos direcciones, y lo mas "
             "comodo es unirlas con `UNION ALL` para leer un solo resultado: cero filas. Y ojo con "
             "el detalle que el enunciado subraya: la comparacion va **sin `LIMIT`**, porque el "
             "`LIMIT 20` excluye justamente a los seis duenos con cero, que son los que fallan."),
            ("La consulta de la pregunta 3 lleva un minuto corriendo. ¿Se colgo?",
             "No. Es una subconsulta correlacionada ejecutandose **2.006 veces**, y cada una "
             "recorre las 30.010 citas unidas con las 5.008 mascotas: son decenas de millones de "
             "filas tocadas, dentro de un motor que corre en el navegador. Espera. **No recargues "
             "la pagina**, porque perderias las respuestas de las otras preguntas. Y esa espera es "
             "el argumento de la pregunta: cuando la version DESPUES conteste en decenas de "
             "milisegundos, la diferencia la vas a haber sentido, no solo leido."),
            ("Mi factor de mejora en la pregunta 2 es de 1,8x. ¿Esta mal?",
             "Esta bien, y un 1,8x medido vale mas que un 50x inventado. En esta base, sin "
             "indices, el factor real esta entre 1,5x y 3x, y ya sabes por que: las dos versiones "
             "recorren las 30.010 filas. Escribelo asi en el informe, con los dos tiempos que lo "
             "sustentan y con la explicacion. Dos advertencias para medir bien: alterna las "
             "corridas —ANTES, DESPUES, ANTES, DESPUES— y quedate con la segunda de cada una, "
             "porque la primera paga el arranque del motor; y no compares tu numero con el del "
             "compañero de al lado, porque su maquina es otra."),
        ],
        "cierre": [
            "Al terminar, cada estudiante debe tener: la agenda del dia reescrita con los cuatro "
            "antipatrones corregidos y las **91 filas** confirmadas en las dos versiones; los "
            "tres `EXPLAIN` con su tabla de lectura y un factor de mejora sustentado; el reporte "
            "de duenos en una sola pasada con el `EXCEPT` de los dos sentidos devolviendo **cero "
            "filas**; las cuatro afirmaciones correctas de la pregunta 4; y la justificacion "
            "tecnica con el indice propuesto y los limites de la medicion, mas "
            "`06_opt_antes.sql` y `06_opt_despues.sql` guardados en la carpeta del PI.",
            "Lo que hay que verificar antes de cerrar la sesion son **tres numeros**, y los tres "
            "se leen sin ejecutar nada. Que el conteo diga **91** en las dos versiones —150 "
            "significa que falta el filtro de estado, 0 significa que se uso `BETWEEN` con "
            "literales de fecha—. Que los seis duenos finales digan **0** y no 1 —si dicen 1, fue "
            "`COUNT(*)`; si no aparecen, fue `INNER JOIN`—. Y que la tabla de lectura del plan "
            "traiga el **29.919** de `Rows Removed by Filter`, que es el numero que no se puede "
            "inventar. Proyectar una entrega voluntaria y buscar esos tres numeros toma dos "
            "minutos.",
            "Dejar dicho en voz alta lo que sigue, porque esta clase termina a proposito con una "
            "pregunta abierta. Hoy quedo demostrado que la consulta corregida **sigue leyendo las "
            "30.010 filas**: la sargabilidad por si sola no evito el recorrido completo, solo "
            "dejo la puerta abierta. La Clase 7 crea el indice sobre `(fecha_hora, estado)` y "
            "vuelve a medir el mismo plan, con dos hipotesis escritas hoy que hay que confirmar o "
            "desmentir: que el `Seq Scan` se convierta en `Index Scan` sobre unas 150 filas, y "
            "que el `Sort` desaparezca porque el indice ya entrega las filas ordenadas. Y con la "
            "contraparte que nadie quiere oir: ese indice hay que mantenerlo en cada `INSERT` de "
            "`sp_agendar_cita`, asi que la Clase 7 tambien es sobre lo que cuesta.",
        ],
    },

    7: {
        "titulo": "Solucion del taller · Clase 7 · Indices y particionamiento de VetCare",
        "resumen": (
            "La promesa que quedo abierta en la Clase 6, cumplida y medida: los tres indices de "
            "las tablas calientes con la evidencia de que el planeador **si** los usa —incluido "
            "el parcial, que es el que gana la agenda del dia—, el experimento del orden de "
            "columnas con el `DROP INDEX` que demuestra por que un indice cuya columna lider no "
            "esta en el `WHERE` se queda sin usar, el historico particionado por ano con sus "
            "**2.620 y 2.390** filas enrutadas y la poda visible en el plan, las cuatro "
            "afirmaciones correctas sobre sobre-indexar, y la tabla de justificacion "
            "consulta → indice que va al informe con su veredicto honesto sobre "
            "particionamiento."
        ),
        "total": 100,
        "nota_actividad": (
            "**El motor es PostgreSQL, no Oracle:** aqui hay indices **parciales** "
            "(`CREATE INDEX ... WHERE ...`), `Bitmap Index Scan` y `pg_indexes`; no hay "
            "`USER_INDEXES`, ni indices de mapa de bits de Oracle, ni `REBUILD ONLINE`. Cuatro "
            "avisos operativos. Primero: cada pregunta arranca con su **propia base recien "
            "sembrada** y **sin indices** mas alla de las llaves primarias, asi que los "
            "`CREATE INDEX` de la pregunta 1 **no existen** en la pregunta 2 —hay que volver a "
            "crear lo que se necesite—. Segundo: las preguntas 1, 2 y 4 corren sobre las 30.010 "
            "citas, pero la pregunta 3 corre sobre **otra base**, con 5.010 citas repartidas "
            "entre 2025 y 2026; los numeros no se pueden mezclar. Tercero: con 5.010 filas el "
            "particionamiento **no** va a ser mas rapido, y eso no es un defecto del ejercicio "
            "sino su leccion —lo que se demuestra es la poda de particiones y el archivado, no la "
            "velocidad—. Cuarto: hay que insistir en el orden `CREATE INDEX` → `ANALYZE` → "
            "`EXPLAIN`; quien mida sin `ANALYZE` de por medio va a ver planes que no explican "
            "nada y va a creer que el indice no sirve."
        ),
        "preguntas": [
            {
                "n": 1,
                "titulo": "Crear los indices de las tablas calientes y probar que se usan",
                "tipo": "bd_sql",
                "puntos": 30,
                "sql": """-- =====================================================================
    -- PASO 1. LINEA BASE. Sin esto no hay nada que comparar despues, y es lo
    -- que mas se olvida: una vez creado el indice ya no se puede volver a
    -- medir el "antes" sin borrarlo.
    -- =====================================================================
    EXPLAIN ANALYZE   -- C1: agenda del dia
    SELECT id_cita, fecha_hora, estado
      FROM cita
     WHERE fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
       AND fecha_hora <  TIMESTAMP '2026-03-11 00:00:00'
       AND estado = 'PROGRAMADA';

    EXPLAIN ANALYZE   -- C2: mascotas de un dueno
    SELECT id_mascota, nombre, especie
      FROM mascota
     WHERE id_dueno = 1234;

    -- =====================================================================
    -- PASO 2. LOS TRES INDICES, con los nombres exactos que pide el
    -- enunciado. El nombre no es un capricho: en la pregunta 5 hay que
    -- referirse a cada uno, y en el plan aparece literalmente
    -- "Index Scan using <nombre>".
    -- =====================================================================

    -- (a) fecha_hora es la columna mas selectiva de cita: 30.010 filas
    --     repartidas en 200 dias, unas 150 por dia. Sirve para CUALQUIER
    --     consulta por rango de fecha, sin importar el estado.
    CREATE INDEX idx_cita_fecha_hora ON cita (fecha_hora);

    -- (b) La llave foranea NO crea indice sola en PostgreSQL. Sin este
    --     indice, "las mascotas de un dueno" recorre las 5.008 mascotas, y
    --     ademas cada DELETE de un dueno tendria que hacer lo mismo para
    --     comprobar la integridad referencial.
    CREATE INDEX idx_mascota_dueno ON mascota (id_dueno);

    -- (c) INDICE PARCIAL. Solo indexa las filas PROGRAMADA -- 18.187 de
    --     30.010, el 61 % -- porque la pantalla de agenda nunca pregunta por
    --     citas canceladas. Es mas pequeno que el indice completo y, como la
    --     condicion del indice YA garantiza el estado, el motor no tiene que
    --     volver a la tabla a verificarlo.
    CREATE INDEX idx_cita_programada_fecha
        ON cita (fecha_hora)
     WHERE estado = 'PROGRAMADA';

    -- =====================================================================
    -- PASO 3. ANALYZE. Crear el indice no actualiza las estadisticas: el
    -- planeador decide por costo estimado, y si sus numeros son viejos puede
    -- ignorar un indice perfectamente bueno. Este paso es la diferencia
    -- entre medir y adivinar.
    -- =====================================================================
    ANALYZE cita;
    ANALYZE mascota;

    -- =====================================================================
    -- PASO 4. LAS MISMAS DOS CONSULTAS, otra vez. Identicas al paso 1: si se
    -- cambia una coma, la comparacion deja de valer.
    -- =====================================================================
    EXPLAIN ANALYZE   -- C1 con indices
    SELECT id_cita, fecha_hora, estado
      FROM cita
     WHERE fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
       AND fecha_hora <  TIMESTAMP '2026-03-11 00:00:00'
       AND estado = 'PROGRAMADA';

    EXPLAIN ANALYZE   -- C2 con indices
    SELECT id_mascota, nombre, especie
      FROM mascota
     WHERE id_dueno = 1234;

    -- El enunciado pide comentar CUAL de los dos indices sobre fecha_hora
    -- eligio el planeador para C1, y la respuesta esperada es el PARCIAL:
    --   * idx_cita_programada_fecha recorre 91 entradas y ya sabe que todas
    --     cumplen estado = 'PROGRAMADA'.
    --   * idx_cita_fecha_hora recorreria 150 entradas -- las citas del dia en
    --     cualquier estado -- y tendria que descartar 59 despues de ir a la
    --     tabla a leer el estado.
    -- El parcial gana por menos entradas y por no tener que reverificar. Si en
    -- tu corrida gano el completo, la diferencia de costo es pequena: reporta
    -- lo que VISTE, no lo que dice esta linea.

    -- =====================================================================
    -- PASO 5. Inventario de lo creado. Es la prueba de que los tres indices
    -- existen con el nombre correcto y con la definicion correcta -- y en el
    -- caso del parcial, con su clausula WHERE.
    -- =====================================================================
    SELECT indexname, tablename, indexdef
      FROM pg_indexes
     WHERE tablename IN ('cita', 'mascota')
     ORDER BY tablename, indexname;

    -- =====================================================================
    -- Comprobacion de una linea, la que conviene pegar al calificar: cuantas
    -- filas indexa cada uno de los dos indices sobre fecha_hora.
    -- =====================================================================
    SELECT (SELECT COUNT(*) FROM cita)                                   AS indexa_el_completo,
           (SELECT COUNT(*) FROM cita WHERE estado = 'PROGRAMADA')       AS indexa_el_parcial,
           (SELECT COUNT(*) FROM cita
             WHERE fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
               AND fecha_hora <  TIMESTAMP '2026-03-11 00:00:00')        AS entradas_que_leeria_el_completo,
           (SELECT COUNT(*) FROM cita
             WHERE fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
               AND fecha_hora <  TIMESTAMP '2026-03-11 00:00:00'
               AND estado = 'PROGRAMADA')                                AS entradas_que_lee_el_parcial;""",
                "salida": """PASO 1 -- linea base, las dos con Seq Scan

    C1:  Seq Scan on cita  (cost=0.00..750.15 rows=90 width=20)
                           (actual time=... rows=91 loops=1)
           Filter: ((fecha_hora >= '2026-03-10 00:00:00'::timestamp)
                    AND (fecha_hora < '2026-03-11 00:00:00'::timestamp)
                    AND (estado = 'PROGRAMADA'::text))
           Rows Removed by Filter: 29919
         Execution Time: 12.8 ms

    C2:  Seq Scan on mascota  (actual time=... rows=2 loops=1)
           Filter: (id_dueno = 1234)
           Rows Removed by Filter: 5006
         Execution Time: 2.9 ms

    PASO 4 -- las mismas consultas despues de indexar y de ANALYZE

    C1:  Index Scan using idx_cita_programada_fecha on cita
             (cost=0.29..8.62 rows=90 width=20) (actual time=... rows=91 loops=1)
           Index Cond: ((fecha_hora >= '2026-03-10 00:00:00'::timestamp)
                        AND (fecha_hora < '2026-03-11 00:00:00'::timestamp))
         Execution Time: 0.4 ms

    C2:  Index Scan using idx_mascota_dueno on mascota
             (actual time=... rows=2 loops=1)
           Index Cond: (id_dueno = 1234)
         Execution Time: 0.1 ms

    Los cuatro hechos que hay que reconocer en esa salida:

    1. **Desaparecio el `Rows Removed by Filter`.** En C1 pasa de 29.919 a **nada**:
       el motor ya no lee las 30.010 filas para tirar 29.919, va directo a las 91.
       Esta es la diferencia con la Clase 6, donde el predicado sargable por si solo
       no habia conseguido esto. **El indice es lo que faltaba.**
    2. **`Index Cond` en vez de `Filter`.** No es un detalle de vocabulario: un
       `Index Cond` se resuelve **dentro** del indice, sin tocar la tabla; un `Filter`
       se evalua **despues** de leer la fila. Cuando un estudiante ve su condicion en
       `Filter`, el indice no le esta sirviendo para esa condicion.
    3. **El planeador eligio el indice PARCIAL para C1**, no el completo. Es la
       respuesta a la pregunta del enunciado. Tambien puede aparecer
       `Bitmap Index Scan` seguido de `Bitmap Heap Scan`: es igual de correcto, y
       significa que el motor prefirio recoger primero todas las direcciones de fila
       y ordenarlas antes de ir a la tabla.
    4. **`estado` ya no aparece en la condicion.** Con el indice parcial no hace
       falta: la definicion del indice garantiza que todo lo que hay dentro es
       `PROGRAMADA`. Eso es exactamente lo que lo hace mas barato que el completo.

    PASO 5 -- pg_indexes: **4 filas** (3 indices creados + la PK de cada tabla = 5;
    aqui se listan las de las dos tablas pedidas)

     indexname                  | tablename |  indexdef
    ----------------------------+-----------+------------------------------------------------
     cita_pkey                  | cita      | CREATE UNIQUE INDEX cita_pkey ON public.cita
                                |           |   USING btree (id_cita)
     idx_cita_fecha_hora        | cita      | CREATE INDEX idx_cita_fecha_hora ON public.cita
                                |           |   USING btree (fecha_hora)
     idx_cita_programada_fecha  | cita      | CREATE INDEX idx_cita_programada_fecha ON
                                |           |   public.cita USING btree (fecha_hora)
                                |           |   WHERE (estado = 'PROGRAMADA'::text)
     idx_mascota_dueno          | mascota   | CREATE INDEX idx_mascota_dueno ON public.mascota
                                |           |   USING btree (id_dueno)
     mascota_pkey               | mascota   | CREATE UNIQUE INDEX mascota_pkey ON
                                |           |   public.mascota USING btree (id_mascota)

    **Lo que hay que mirar en el `indexdef` del parcial es la clausula `WHERE`.** Si
    no esta, el estudiante creo un indice completo con nombre de parcial, y eso es lo
    que el enunciado penaliza de forma explicita.

    Comprobacion de una linea -- 1 fila

     indexa_el_completo | indexa_el_parcial | entradas_que_leeria_el_completo | entradas_que_lee_el_parcial
    --------------------+-------------------+---------------------------------+-----------------------------
                  30010 |             18187 |                             150 |                          91

    Ahi esta el argumento del indice parcial en cuatro numeros: es **39 % mas
    pequeno** (18.187 contra 30.010 entradas) y para la agenda del dia lee **91
    entradas en vez de 150**. Y ahi esta tambien su limite, que va en la pregunta 5:
    solo sirve cuando la consulta trae `estado = 'PROGRAMADA'`. La pantalla que
    muestre el historico completo de un dia va a usar el otro.

    **C2 devuelve 2 filas** —`(1241, Mascota 1233, Felino)` y
    `(3241, Mascota 3233, Felino)`—: 2 de 5.008, que es el caso ideal para un indice.
    Si alguien reporta 0 filas, casi siempre confundio `id_dueno` con `id_mascota`.""",
                "como_calificar": [
                    "**6 pts — la linea base con `Seq Scan` en las dos consultas,** 3 pts cada "
                    "una. Es el paso que la rubrica exige primero y el que mas se salta. El ancla "
                    "verificable es el `Rows Removed by Filter: 29919` de C1: sin haber corrido el "
                    "`EXPLAIN` antes de indexar, ese numero no se puede inventar.",
                    "**9 pts — los tres indices con los nombres exactos, 3 pts cada uno.** El del "
                    "parcial solo se da si el `indexdef` de `pg_indexes` muestra la clausula "
                    "`WHERE estado = 'PROGRAMADA'`. Un indice completo con nombre de parcial vale "
                    "0 de esos 3: la rubrica descuenta «si falta el indice parcial», y aqui "
                    "efectivamente falta.",
                    "**3 pts — el `ANALYZE cita;` y el `ANALYZE mascota;` despues de crear los "
                    "indices** y antes de volver a medir. No es burocracia: sin estadisticas "
                    "frescas el planeador puede ignorar un indice bueno, y entonces el estudiante "
                    "concluye lo contrario de lo que la clase quiere ensenar.",
                    "**6 pts — los `EXPLAIN` posteriores evidencian `Index Scan` o "
                    "`Bitmap Index Scan`** en C1 y en C2, 3 pts cada uno. Las dos formas valen "
                    "igual. Lo que se verifica es que el nodo nombre el indice "
                    "(`using idx_...`) y que la condicion aparezca como `Index Cond` y no como "
                    "`Filter`.",
                    "**3 pts — la consulta a `pg_indexes` lista los tres indices.** Con las PK "
                    "salen 5 filas en total; se aceptan las 5 y tambien una version filtrada, "
                    "siempre que los tres indices propios esten.",
                    "**3 pts — el comentario sobre cual de los dos indices sobre `fecha_hora` "
                    "eligio el planeador.** La rubrica lo pide de forma explicita y es el punto "
                    "que separa a quien leyo el plan de quien lo pego. Se dan los 3 pts si el "
                    "estudiante nombra el indice que **su** plan muestra y da una razon "
                    "—normalmente el parcial, por tener menos entradas y no tener que reverificar "
                    "el estado—. Si nombro el completo pero su plan dice el completo, valen igual "
                    "los 3: se califica la lectura, no el resultado esperado.",
                ],
                "errores": [
                    "**Crear los indices primero y medir despues, sin linea base.** Es el error "
                    "estructural de esta pregunta: cuando se dan cuenta, ya no hay «antes» que "
                    "medir. La salida es honesta y vale la pena ensenarla: "
                    "`DROP INDEX idx_cita_fecha_hora, idx_cita_programada_fecha;`, medir, y "
                    "volverlos a crear. Improvisar la linea base cuesta los 6 pts.",
                    "**Crear el «parcial» sin la clausula `WHERE`.** Queda un segundo indice "
                    "completo sobre `fecha_hora`, con nombre enganoso, que no aporta nada y que "
                    "hay que mantener en cada `INSERT`. Es el peor de los mundos y se detecta en "
                    "una linea, en el `indexdef`.",
                    "**Poner el `WHERE` del indice parcial en el lugar equivocado:** "
                    "`CREATE INDEX ... (fecha_hora WHERE estado = 'PROGRAMADA')` o "
                    "`CREATE INDEX ... WHERE fecha_hora >= ...`. La sintaxis es "
                    "`CREATE INDEX nombre ON tabla (columnas) WHERE condicion;` —la condicion va "
                    "al final, sobre el indice completo, no dentro del parentesis—.",
                    "**Omitir el `ANALYZE`** y concluir «el indice no sirvio porque el plan no "
                    "cambio». Con 30.010 filas normalmente el plan si cambia sin `ANALYZE`, asi "
                    "que el error suele quedar invisible aqui y aparecer despues en la pregunta 2. "
                    "El habito que se ensena es el orden: crear, `ANALYZE`, medir.",
                    "**Cambiar la consulta entre la medicion de antes y la de despues** —agregar "
                    "un `ORDER BY`, quitar el filtro de estado, cambiar el dia—. Entonces se estan "
                    "comparando dos cosas distintas y la evidencia no dice nada. Las dos consultas "
                    "del enunciado se pegan **literalmente**, las dos veces.",
                    "**Escribir «se uso el indice» sin nombrarlo.** El plan dice "
                    "`Index Scan using idx_cita_programada_fecha`: el nombre esta ahi y es "
                    "gratis. La devolucion util es pedir esa palabra, porque es la que obliga a "
                    "mirar el plan de verdad y la que hace falta en la tabla de la pregunta 5.",
                ],
            },
            {
                "n": 2,
                "titulo": "Orden de columnas en un indice compuesto",
                "tipo": "bd_sql",
                "puntos": 20,
                "sql": """-- =====================================================================
    -- PASO 1. Los dos indices compuestos con las MISMAS dos columnas y en
    -- orden invertido. Todo el experimento consiste en que el planeador
    -- elija, y en ver cual elige para cada consulta.
    -- =====================================================================
    CREATE INDEX idx_cita_estado_fecha ON cita (estado, fecha_hora);
    CREATE INDEX idx_cita_fecha_estado ON cita (fecha_hora, estado);
    ANALYZE cita;

    -- =====================================================================
    -- PASO 2. Las tres consultas. Cada una esta disenada para que gane un
    -- indice distinto (o ninguno).
    -- =====================================================================

    -- Q1: igualdad en estado + rango en fecha_hora. Es el caso de libro.
    EXPLAIN ANALYZE
    SELECT id_cita, fecha_hora
      FROM cita
     WHERE estado = 'PROGRAMADA'
       AND fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
       AND fecha_hora <  TIMESTAMP '2026-03-11 00:00:00';
    -- Esperado: Index Scan using idx_cita_estado_fecha.
    -- Por que: con (estado, fecha_hora) el motor fija estado = 'PROGRAMADA' y
    -- dentro de ese bloque las entradas ya vienen ordenadas por fecha_hora,
    -- asi que lee un tramo CONTIGUO de exactamente 91 entradas y para.
    -- Con (fecha_hora, estado) tendria que leer las 150 del dia y descartar 59.

    -- Q2: solo rango de fecha. estado no aparece en el WHERE.
    EXPLAIN ANALYZE
    SELECT id_cita, fecha_hora
      FROM cita
     WHERE fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
       AND fecha_hora <  TIMESTAMP '2026-03-11 00:00:00';
    -- Esperado: Index Scan using idx_cita_fecha_estado.
    -- Por que: fecha_hora es la columna LIDER, asi que el rango es un tramo
    -- contiguo del indice: 150 entradas. El otro indice esta ordenado primero
    -- por estado, de modo que las citas del 10 de marzo estan repartidas en
    -- TRES tramos distintos y ninguno se puede localizar sin recorrer todo.

    -- Q3: solo estado, que tiene 3 valores y donde PROGRAMADA es el 61 %.
    EXPLAIN ANALYZE
    SELECT COUNT(*) FROM cita WHERE estado = 'PROGRAMADA';
    -- Esperado: Seq Scan on cita (dentro de un nodo Aggregate).
    -- Por que: hay que tocar 18.187 de 30.010 filas. Leer el 61 % de la tabla
    -- brincando por un indice sale MAS CARO que recorrerla de corrido, porque
    -- el recorrido secuencial va en orden fisico. Un indice sobre una columna
    -- de baja cardinalidad casi nunca se usa, y esta es la demostracion.
    -- (Si aparece un Index Only Scan, tambien es correcto: como COUNT(*) no
    --  necesita mas columnas, el motor puede resolverlo dentro del indice
    --  siempre que el mapa de visibilidad este al dia. La conclusion no
    --  cambia: no vale la pena crear ese indice solo para esto.)

    -- =====================================================================
    -- PASO 3. El experimento forzado: se le quita al motor el indice que
    -- estaba usando para Q2 y se ve que hace.
    -- =====================================================================
    DROP INDEX idx_cita_fecha_estado;
    ANALYZE cita;

    EXPLAIN ANALYZE     -- Q2 otra vez, identica
    SELECT id_cita, fecha_hora
      FROM cita
     WHERE fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
       AND fecha_hora <  TIMESTAMP '2026-03-11 00:00:00';
    -- Resultado: vuelve el Seq Scan con Rows Removed by Filter: 29860,
    -- que son las 30.010 filas menos las 150 del dia.
    -- El indice idx_cita_estado_fecha SIGUE EXISTIENDO y contiene fecha_hora,
    -- pero el motor prefiere no usarlo. La razon es la estructura del arbol:
    -- solo se puede entrar por la columna lider. Como estado no esta en el
    -- WHERE, para encontrar las citas del 10 de marzo habria que recorrer el
    -- indice COMPLETO -- las 30.010 entradas -- y ademas ir a la tabla por
    -- cada candidata, porque id_cita no esta en el indice. Sale mas caro que
    -- el Seq Scan, y el planeador lo calcula asi.

    -- =====================================================================
    -- Comprobacion de una linea: los tres numeros que sostienen las tres
    -- conclusiones de arriba.
    -- =====================================================================
    SELECT (SELECT COUNT(*) FROM cita)                                  AS filas_totales,
           (SELECT COUNT(*) FROM cita WHERE estado = 'PROGRAMADA')      AS q3_toca_el_61_por_ciento,
           (SELECT COUNT(*) FROM cita
             WHERE fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
               AND fecha_hora <  TIMESTAMP '2026-03-11 00:00:00')       AS q2_lee_150,
           (SELECT COUNT(*) FROM cita
             WHERE estado = 'PROGRAMADA'
               AND fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
               AND fecha_hora <  TIMESTAMP '2026-03-11 00:00:00')       AS q1_lee_91;

    -- =====================================================================
    -- CONCLUSION: en un indice compuesto va PRIMERO la columna de IGUALDAD y
    -- DESPUES la de RANGO, porque el motor puede fijar la igualdad y luego
    -- recorrer un tramo contiguo; al reves, el rango abre el abanico y la
    -- segunda columna ya no acota nada, solo filtra.
    -- CONCLUSION (2): un indice cuya columna lider no aparece en el WHERE
    -- normalmente queda sin usar, porque a un arbol B solo se entra por la
    -- izquierda. Corolario practico: (estado, fecha_hora) NO reemplaza a
    -- (fecha_hora), pero (fecha_hora, estado) SI reemplaza a (fecha_hora) --
    -- por eso dos indices bien ordenados suelen bastar donde alguien queria
    -- cuatro.""",
                "salida": """PASO 2 -- que indice eligio cada consulta

    Q1  (igualdad + rango) -- 91 filas
        Index Scan using idx_cita_estado_fecha on cita
            (actual time=... rows=91 loops=1)
          Index Cond: ((estado = 'PROGRAMADA'::text)
                       AND (fecha_hora >= '2026-03-10 00:00:00'::timestamp)
                       AND (fecha_hora < '2026-03-11 00:00:00'::timestamp))
        Execution Time: 0.4 ms
        --> LAS DOS condiciones estan en Index Cond. Eso es lo que significa que
            el orden de columnas es el correcto: el indice resuelve todo.

    Q2  (solo rango) -- 150 filas
        Index Scan using idx_cita_fecha_estado on cita
            (actual time=... rows=150 loops=1)
          Index Cond: ((fecha_hora >= '2026-03-10 00:00:00'::timestamp)
                       AND (fecha_hora < '2026-03-11 00:00:00'::timestamp))
        Execution Time: 0.5 ms
        --> Eligio el OTRO indice. Con las mismas dos columnas. Solo cambia el orden.

    Q3  (solo estado, 61 % de la tabla) -- 1 fila: 18187
        Aggregate  (actual time=... rows=1 loops=1)
          ->  Seq Scan on cita  (actual time=... rows=18187 loops=1)
                Filter: (estado = 'PROGRAMADA'::text)
                Rows Removed by Filter: 11823
        Execution Time: 9.6 ms
        --> NINGUN indice, teniendo dos disponibles que empiezan por estado.
            No es un error del motor: es la respuesta correcta. Tambien puede
            aparecer un Index Only Scan usando idx_cita_estado_fecha, y sirve
            igual para la conclusion.

    PASO 3 -- Q2 despues del DROP INDEX idx_cita_fecha_estado

        Seq Scan on cita  (actual time=... rows=150 loops=1)
          Filter: ((fecha_hora >= '2026-03-10 00:00:00'::timestamp)
                   AND (fecha_hora < '2026-03-11 00:00:00'::timestamp))
          Rows Removed by Filter: 29860
        Execution Time: 11.4 ms
        --> **Este es el resultado de la pregunta.** El indice
            idx_cita_estado_fecha sigue existiendo y CONTIENE fecha_hora, y aun
            asi el motor volvio al recorrido completo: de 0,5 ms a 11,4 ms, unas
            20 veces mas lento. La columna lider es la puerta de entrada al
            indice, y si no esta en el WHERE, el indice esta cerrado.

    Comprobacion de una linea -- 1 fila

     filas_totales | q3_toca_el_61_por_ciento | q2_lee_150 | q1_lee_91
    ---------------+--------------------------+------------+-----------
             30010 |                    18187 |        150 |        91

    Los tres numeros explican las tres decisiones del planeador sin necesidad de
    teoria: 91 de 30.010 (0,3 %) es un caso ideal para un indice; 150 de 30.010
    (0,5 %) tambien; **18.187 de 30.010 (61 %) no lo es**, y por eso Q3 recorre la
    tabla. La regla de bolsillo que se puede dar en clase: por debajo de un 5 % a un
    10 % de la tabla el indice suele ganar; por encima de un tercio, casi nunca.""",
                "como_calificar": [
                    "**4 pts — los dos indices compuestos creados con los nombres exactos** y el "
                    "`ANALYZE cita;` de por medio, 2 pts cada indice. Sin `ANALYZE` el "
                    "experimento se vuelve ruido y el resto de la pregunta puede salir al reves.",
                    "**6 pts — los tres `EXPLAIN` con el indice elegido identificado, 2 pts cada "
                    "uno.** La rubrica pide **identificar**, no solo ejecutar: hay que nombrar "
                    "`idx_cita_estado_fecha` en Q1, `idx_cita_fecha_estado` en Q2 y decir que Q3 "
                    "**no uso ninguno** —o que uso un `Index Only Scan`, que vale igual—. El punto "
                    "de Q3 se da solo si el estudiante explica **por que** el motor no quiso el "
                    "indice, no solo que no lo uso.",
                    "**5 pts — el `DROP INDEX` y la nueva medicion de Q2, comparada.** 3 pts que "
                    "el experimento este completo —`DROP`, volver a medir, y la misma consulta sin "
                    "cambiar— y 2 pts la comparacion explicita con el numero: volvio el `Seq Scan` "
                    "con `Rows Removed by Filter: 29860`. Ese numero es el ancla que no se puede "
                    "adivinar.",
                    "**5 pts — la linea `-- CONCLUSION:`.** 3 pts enunciar bien la regla "
                    "**igualdad antes de rango** y 2 pts explicar por que un indice cuya columna "
                    "lider no esta en el filtro suele quedar sin usar. La rubrica acepta como "
                    "matiz correcto que ese indice todavia pueda servir para un barrido completo "
                    "tipo `Index Only Scan`, y quien lo mencione muestra que entendio el "
                    "mecanismo, no la formula.",
                    "**Se reconoce como sobresaliente, sin puntos extra:** el corolario que casi "
                    "nadie escribe y que es el mas util en el trabajo —`(fecha_hora, estado)` "
                    "**si** hace innecesario un indice suelto sobre `(fecha_hora)`, pero "
                    "`(estado, fecha_hora)` **no**—. Es la razon por la que dos indices bien "
                    "ordenados suelen reemplazar a cuatro, y conecta directo con la pregunta 4.",
                    "**No se califican los milisegundos**, sino los conteos de filas y el nodo "
                    "elegido. Si un estudiante reporta que Q2 quedo mas rapida despues del `DROP`, "
                    "casi siempre esta comparando una corrida en frio contra una en caliente: la "
                    "devolucion es que alterne y repita.",
                ],
                "errores": [
                    "**Concluir que «los dos indices sirven igual porque tienen las mismas "
                    "columnas».** Es exactamente la intuicion que la pregunta existe para romper, "
                    "y se rompe con la propia evidencia del estudiante: Q1 eligio uno, Q2 eligio "
                    "el otro, y tras el `DROP` Q2 se quedo sin ninguno. El orden no es un detalle "
                    "de estilo, es la estructura del arbol.",
                    "**Interpretar Q3 como un fallo.** «El motor no uso mi indice» no es un error "
                    "del motor ni del indice: tocar el 61 % de la tabla brincando por un indice es "
                    "mas caro que recorrerla en orden fisico. Es la evidencia experimental de la "
                    "opcion falsa de la pregunta 4, y conviene senalar esa conexion en la "
                    "devolucion.",
                    "**Cambiar Q2 despues del `DROP`** —agregar un `ORDER BY`, quitar una de las "
                    "dos cotas del rango, mover el dia—. El experimento consiste en variar **una "
                    "sola cosa**: el indice disponible. Si tambien cambia la consulta, no hay "
                    "conclusion posible.",
                    "**Confundir el orden del indice con el orden del `WHERE`.** El orden en que "
                    "se escriben las condiciones en el `WHERE` es irrelevante: el planeador las "
                    "reordena. Lo que importa es el orden de las columnas **en la definicion del "
                    "indice**. Vale la pena demostrarlo en vivo invirtiendo las dos lineas del "
                    "`WHERE` de Q1: el plan sale identico.",
                    "**Creer que la conclusion es «siempre poner la fecha primero»** o «siempre "
                    "poner el estado primero». La regla no es sobre columnas concretas, es sobre "
                    "**el tipo de comparacion**: igualdad primero, rango despues. Se comprueba "
                    "leyendo Q1 y Q2 juntas: la misma columna gana o pierde el primer puesto segun "
                    "como se la compare.",
                    "**Olvidar el `ANALYZE` despues del `DROP INDEX`.** No cambia el resultado en "
                    "esta base, pero mantiene el habito de la pregunta 1 y evita explicaciones "
                    "raras cuando un plan no coincide con lo esperado.",
                ],
            },
            {
                "n": 3,
                "titulo": "Particionar el historico de citas por rango de fecha",
                "tipo": "bd_sql",
                "puntos": 20,
                "sql": """-- =====================================================================
    -- OJO: esta pregunta corre sobre OTRA base. Aqui hay 5.010 citas
    -- repartidas entre enero de 2025 y diciembre de 2026, no las 30.010 de
    -- las preguntas 1 y 2. Los numeros no se mezclan.
    -- =====================================================================

    -- =====================================================================
    -- PASO 1. La tabla padre particionada. NO tiene datos propios: es solo la
    -- definicion de la estructura y la regla de enrutamiento.
    -- =====================================================================
    CREATE TABLE cita_hist (
      id_cita         INT,
      id_mascota      INT,
      id_veterinario  INT,
      fecha_hora      TIMESTAMP NOT NULL,
      estado          TEXT,
      -- La PK TIENE que incluir la columna de particion. La razon es
      -- estructural: PostgreSQL implementa la unicidad con un indice por
      -- particion, y no puede garantizar que un id_cita no se repita entre
      -- dos particiones distintas si no sabe en cual buscar. Con id_cita solo
      -- falla con:
      --   "unique constraint on partitioned table must include all
      --    partitioning columns"
      PRIMARY KEY (id_cita, fecha_hora)
    ) PARTITION BY RANGE (fecha_hora);

    -- =====================================================================
    -- PASO 2. Las dos particiones. El limite inferior es INCLUSIVO y el
    -- superior EXCLUSIVO -- FROM ... TO ... --, y por eso 2026-01-01 aparece
    -- en las dos lineas sin que haya solape: cierra 2025 y abre 2026. Es la
    -- misma logica del predicado de rango de la Clase 6.
    -- =====================================================================
    CREATE TABLE cita_hist_2025 PARTITION OF cita_hist
        FOR VALUES FROM (TIMESTAMP '2025-01-01') TO (TIMESTAMP '2026-01-01');

    CREATE TABLE cita_hist_2026 PARTITION OF cita_hist
        FOR VALUES FROM (TIMESTAMP '2026-01-01') TO (TIMESTAMP '2027-01-01');

    -- =====================================================================
    -- PASO 3. Migracion. Se inserta en la tabla PADRE y PostgreSQL enruta
    -- cada fila a su particion segun fecha_hora. No hace falta ningun
    -- trigger ni ningun CASE: el enrutamiento es del motor.
    -- =====================================================================
    INSERT INTO cita_hist
    SELECT id_cita, id_mascota, id_veterinario, fecha_hora, estado FROM cita;

    ANALYZE cita_hist;    -- para que la poda del PASO 5 se vea con numeros reales

    -- =====================================================================
    -- PASO 4. Prueba del enrutamiento. tableoid es una columna de sistema que
    -- dice de que tabla FISICA salio cada fila; el cast ::regclass la
    -- convierte en el nombre. Es la unica forma limpia de demostrar el
    -- reparto sin consultar cada particion por separado.
    -- =====================================================================
    SELECT tableoid::regclass AS particion,
           COUNT(*),
           MIN(fecha_hora),
           MAX(fecha_hora)
      FROM cita_hist
     GROUP BY 1
     ORDER BY 1;

    -- =====================================================================
    -- PASO 5. Prueba de la PODA DE PARTICIONES. En el plan solo debe aparecer
    -- cita_hist_2026: la particion de 2025 no se lee, no se abre, no existe
    -- para esta consulta.
    -- =====================================================================
    EXPLAIN ANALYZE
    SELECT COUNT(*) FROM cita_hist
     WHERE fecha_hora >= TIMESTAMP '2026-01-01'
       AND fecha_hora <  TIMESTAMP '2027-01-01';

    -- Contraprueba util: sin filtro por fecha_hora no hay nada que podar y el
    -- plan tiene que mostrar las DOS particiones bajo un nodo Append.
    EXPLAIN ANALYZE
    SELECT COUNT(*) FROM cita_hist;

    -- Y la trampa que conviene mostrar: si el filtro se envuelve en una
    -- funcion, se pierde la poda igual que se perdia el indice en la Clase 6.
    -- Aqui vuelven a aparecer las dos particiones.
    EXPLAIN ANALYZE
    SELECT COUNT(*) FROM cita_hist
     WHERE EXTRACT(YEAR FROM fecha_hora) = 2026;

    -- =====================================================================
    -- PASO 6. Comprobacion de que no se perdio ni se duplico nada en la
    -- migracion.
    -- =====================================================================
    SELECT (SELECT COUNT(*) FROM cita)      AS origen,
           (SELECT COUNT(*) FROM cita_hist) AS destino,
           (SELECT COUNT(*) FROM cita) - (SELECT COUNT(*) FROM cita_hist) AS debe_ser_cero;

    -- =====================================================================
    -- La operacion de mantenimiento que se vuelve trivial:
    --
    --   DROP TABLE cita_hist_2025;   -- archivar el ano completo
    --
    -- Eso libera las 2.620 filas de 2025 en una operacion de METADATOS: el
    -- motor desengancha el archivo y lo borra. Es practicamente instantaneo,
    -- no genera WAL por fila, no deja filas muertas y no necesita VACUUM.
    --
    -- El equivalente sin particiones seria
    --   DELETE FROM cita WHERE fecha_hora < TIMESTAMP '2026-01-01';
    -- que recorre la tabla, escribe 2.620 registros en el WAL, deja 2.620
    -- filas muertas que hay que aspirar despues, mantiene todos los indices
    -- durante el borrado y NO devuelve el espacio al sistema sin un
    -- VACUUM FULL -- que bloquea la tabla entera --. Con 2.620 filas la
    -- diferencia es un detalle; con dos anos de historia real de Huellitas,
    -- es la diferencia entre un segundo y una ventana de mantenimiento.
    --
    -- Variante que se usa de verdad cuando la ley obliga a conservar el dato:
    --   ALTER TABLE cita_hist DETACH PARTITION cita_hist_2025;
    -- deja la tabla intacta pero fuera del conjunto consultado, lista para
    -- respaldarla con el pg_dump de la Clase 4 y despues borrarla.
    -- =====================================================================""",
                "salida": """PASO 4 -- enrutamiento: 2 filas

        particion    | count |         min         |         max
    -----------------+-------+---------------------+---------------------
     cita_hist_2025  |  2620 | 2025-01-06 08:00:00 | 2025-12-31 15:00:00
     cita_hist_2026  |  2390 | 2026-01-01 08:00:00 | 2026-12-06 15:00:00

    **2.620 + 2.390 = 5.010.** Son los dos numeros de la pregunta y los que hay que
    buscar al calificar. Tres cosas se leen de esta tabla sola:

    - **Los rangos no se solapan y encajan sin hueco:** 2025 termina el 31 de
      diciembre y 2026 empieza el 1 de enero. Eso es lo que consigue el limite
      superior **exclusivo** de `FROM ... TO ...`.
    - **2026 tiene 2.390 y no 2.380** porque ademas de las citas sintetizadas se
      lleva las **10 citas sembradas a mano** de septiembre de 2026 —las de
      Firulais, Luna y compania—.
    - **El reparto es desigual a proposito** (2.620 contra 2.390): la historia
      sintetica arranca el 6 de enero de 2025 y termina el 6 de diciembre de 2026,
      asi que 2025 esta completo y 2026 le faltan tres semanas y media.

    PASO 5 -- poda de particiones

    Consulta con filtro de 2026 -- 1 fila: 2390

        Aggregate  (actual time=... rows=1 loops=1)
          ->  Seq Scan on cita_hist_2026 cita_hist  (actual rows=2390 loops=1)
                Filter: ((fecha_hora >= '2026-01-01 00:00:00'::timestamp)
                         AND (fecha_hora < '2027-01-01 00:00:00'::timestamp))
        Execution Time: 1.2 ms

    **`cita_hist_2025` no aparece en ninguna parte del plan.** Eso es la poda, y es
    lo que la pregunta pide demostrar. Con una sola particula en el plan puede que ni
    siquiera salga el nodo `Append`: cuando queda una sola relacion, el motor lo
    elimina.

    Contraprueba, sin filtro -- 1 fila: 5010

        Aggregate
          ->  Append  (actual rows=5010 loops=1)
                ->  Seq Scan on cita_hist_2025 cita_hist_1  (actual rows=2620 loops=1)
                ->  Seq Scan on cita_hist_2026 cita_hist_2  (actual rows=2390 loops=1)

    Aqui **si** aparecen las dos, bajo un `Append`. Tener las dos salidas al lado es
    lo que convierte «se podo» en evidencia: sin la contraprueba no se sabe si la
    particion de 2025 falto por la poda o porque nunca hubo nada dentro.

    Con `EXTRACT(YEAR FROM fecha_hora) = 2026` -- 1 fila: 2390, pero:

        Aggregate
          ->  Append  (actual rows=2390 loops=1)
                ->  Seq Scan on cita_hist_2025 ...  (actual rows=0 loops=1)
                      Filter: (EXTRACT(year FROM fecha_hora) = 2026)
                      Rows Removed by Filter: 2620
                ->  Seq Scan on cita_hist_2026 ...  (actual rows=2390 loops=1)

    **El resultado es correcto y la poda se perdio.** Las dos particiones se leen y
    2025 aporta 0 filas despues de descartar 2.620. Es la misma leccion de la
    Clase 6 en otro escenario: envolver la columna en una funcion le quita al motor
    la informacion que necesita para decidir, y aqui lo que pierde no es un indice,
    es una particion entera. Vale la pena mostrar esta salida en clase.

    PASO 6 -- integridad de la migracion: 1 fila

     origen | destino | debe_ser_cero
    --------+---------+---------------
       5010 |    5010 |             0""",
                "como_calificar": [
                    "**5 pts — `cita_hist` bien creada.** 3 pts el `PARTITION BY RANGE "
                    "(fecha_hora)` y 2 pts la `PRIMARY KEY (id_cita, fecha_hora)`. Si el "
                    "estudiante intento `PRIMARY KEY (id_cita)` y el motor lo rechazo, y despues "
                    "lo corrigio, se dan los 2 pts completos: el mensaje de error es la mejor "
                    "explicacion de por que la llave tiene que incluir la columna de particion.",
                    "**4 pts — las dos particiones cubren 2025 y 2026 sin solaparse,** 2 pts cada "
                    "una. Se verifica en el `MIN`/`MAX` del paso 4: 2025 cierra el 31 de diciembre "
                    "y 2026 abre el 1 de enero. Un solape se detecta al instante porque el "
                    "`CREATE TABLE` falla —el motor no lo permite—, asi que el error real que "
                    "aparece es el hueco.",
                    "**4 pts — la migracion inserta las 5.010 filas.** 2 pts que el `INSERT` vaya "
                    "contra la tabla **padre** —insertar directo en cada particion con un `WHERE` "
                    "por ano funciona pero se salta lo que se queria ensenar: vale 1 de esos 2— y "
                    "2 pts que el conteo cuadre.",
                    "**4 pts — el `tableoid::regclass` evidencia el reparto con "
                    "2.620 / 2.390.** 2 pts la consulta y 2 pts que los numeros sean los correctos "
                    "y con rangos que no se solapan.",
                    "**3 pts — el `EXPLAIN` muestra la poda: solo `cita_hist_2026`.** Se dan los 3 "
                    "pts con la salida de la poda; se anota como sobresaliente —sin puntos extra— "
                    "quien haya agregado la **contraprueba sin filtro**, porque es lo que "
                    "distingue «se podo» de «esa particion estaba vacia».",
                    "**Los 20 pts no cierran sin el comentario final del paso 6:** identificar que "
                    "lo que se vuelve trivial es **archivar o eliminar un ano completo** con un "
                    "`DROP TABLE` de la particion en vez de un `DELETE` masivo. Es un requisito "
                    "explicito de la rubrica y se reparte dentro de los puntos anteriores; una "
                    "entrega que hace todo el SQL y omite el comentario pierde 3 pts sobre el "
                    "bloque de la poda.",
                ],
                "errores": [
                    "**`PRIMARY KEY (id_cita)` a secas.** Falla con «unique constraint on "
                    "partitioned table must include all partitioning columns». No es una "
                    "arbitrariedad: la unicidad se implementa con un indice **por particion**, y "
                    "sin la columna de particion el motor no sabria en cual buscar para "
                    "garantizarla. Es el error de arranque mas comun y el que mejor se explica "
                    "solo.",
                    "**Rangos que dejan un hueco:** `TO ('2025-12-31')` en vez de "
                    "`TO ('2026-01-01')`. El `INSERT` falla con «no partition of relation "
                    "cita_hist found for row» y el estudiante suele culpar a la migracion. El "
                    "limite superior es **exclusivo**, asi que la fecha de corte se repite en las "
                    "dos particiones: cierra una y abre la otra.",
                    "**Insertar en cada particion por separado** con un `WHERE` por ano. Da el "
                    "resultado correcto y demuestra lo contrario de lo que se pedia: el punto es "
                    "que el **motor** enruta. Ademas es el habito que rompe el sistema el dia que "
                    "llegue una fila de 2027 y nadie recuerde que hay que insertar a mano.",
                    "**Confundir particionamiento con indices.** Aparece como «cree la particion "
                    "para que la consulta use el indice». Son dos mecanismos distintos: el indice "
                    "encuentra filas dentro de una tabla, la particion decide **que tablas ni "
                    "siquiera se abren**. Se pueden combinar —y en produccion se combinan—, pero "
                    "no se sustituyen.",
                    "**Filtrar con `EXTRACT(YEAR FROM fecha_hora) = 2026` y afirmar que hubo "
                    "poda.** El resultado es correcto —2.390— y en el plan aparecen **las dos** "
                    "particiones. Es exactamente el antipatron de la Clase 6 reapareciendo: si el "
                    "estudiante lo cometio, no hay que corregirselo sin mas, hay que hacerle "
                    "comparar los dos planes.",
                    "**Concluir que particionar «hizo la consulta mas rapida».** Con 5.010 filas "
                    "**no** hay ganancia de rendimiento apreciable, y el propio enunciado lo dice. "
                    "Lo demostrado aqui es sintaxis, enrutamiento, poda en el plan y facilidad de "
                    "archivado. Quien reporte una mejora de velocidad esta midiendo ruido, y esa "
                    "distincion es la que la pregunta 5 califica de frente.",
                ],
            },
            {
                "n": 4,
                "titulo": "Riesgos de sobre-indexar VetCare",
                "tipo": "cerrada_multi",
                "puntos": 10,
                "justificacion": {
                    0: "**Correcta, y es el costo que nadie ve porque no aparece en ningun "
                       "`EXPLAIN` de `SELECT`.** Un indice es una estructura **separada** de la "
                       "tabla y el motor tiene que mantenerla sincronizada: cada `INSERT` escribe "
                       "una entrada en cada indice, cada `UPDATE` de una columna indexada borra la "
                       "vieja y escribe la nueva, cada `DELETE` marca las suyas. En VetCare eso "
                       "pesa sobre `sp_agendar_cita` y `sp_registrar_consulta`, que son las dos "
                       "operaciones con alguien esperando en el mostrador. Indexar «cada columna» "
                       "de `cita` significa multiplicar por cinco o seis el trabajo de escritura "
                       "de la operacion mas sensible del sistema.",
                    1: "**Incorrecta, y esta demostrada experimentalmente en la pregunta 2.** "
                       "`estado` tiene 3 valores y `PROGRAMADA` es el 61 % de las 30.010 filas: "
                       "Q3 recorrio la tabla completa **teniendo dos indices disponibles que "
                       "empiezan por `estado`**. Leer el 61 % de una tabla brincando por un "
                       "indice es mas caro que recorrerla en orden fisico, y el planeador lo "
                       "calcula asi. La palabra que delata la opcion es **«siempre»**: la "
                       "excepcion existe —un valor raro dentro de una columna de baja "
                       "cardinalidad, o el indice **parcial** de la opcion siguiente—, pero eso ya "
                       "no es «indexar la columna `estado`».",
                    2: "**Correcta, y es el costo que se paga incluso cuando el indice no se "
                       "usa.** Ocupa disco, pero sobre todo compite por la **cache**: el motor "
                       "tiene una cantidad fija de memoria para paginas, y cada pagina de indice "
                       "muerto que entra ahi expulsa una pagina de datos que si se estaba "
                       "consultando. Ademas engorda los respaldos de la Clase 4 y alarga cada "
                       "restauracion, porque los indices se **reconstruyen** al restaurar. Un "
                       "indice inutil no es neutro: cobra sin dar nada.",
                    3: "**Correcta, y es la del indice que se creo en la pregunta 1.** "
                       "`idx_cita_programada_fecha` indexa 18.187 entradas en vez de 30.010 —un "
                       "39 % menos— y para la agenda del dia lee 91 en vez de 150, porque su "
                       "propia definicion ya garantiza el estado y no hay que reverificarlo. La "
                       "condicion esta en la ultima frase de la opcion y es la que hay que "
                       "subrayar: **«cuando las consultas siempre traen ese filtro»**. Una "
                       "pantalla que muestre el historico completo de un dia no puede usar este "
                       "indice, y para eso queda el completo.",
                    4: "**Incorrecta, y es la mas peligrosa de las seis porque suena a dato "
                       "tecnico.** PostgreSQL crea un indice automatico para una "
                       "`PRIMARY KEY` y para un `UNIQUE`, pero **no** para una `FOREIGN KEY`. Sin "
                       "`idx_mascota_dueno`, «las mascotas de un dueno» recorre las 5.008 "
                       "mascotas —lo midio la pregunta 1— y ademas cada `DELETE` o `UPDATE` de un "
                       "`dueno` tiene que hacer ese mismo recorrido para comprobar la integridad "
                       "referencial. Indexar el lado **hijo** de una llave foranea es una de las "
                       "poquisimas indexaciones que se pueden dar por buenas casi sin medir.",
                    5: "**Correcta, y es la regla de trabajo que la pregunta 5 pide adoptar por "
                       "escrito.** Un indice se justifica con una **consulta concreta** y con la "
                       "**evidencia** de que el planeador lo eligio, no con una intuicion sobre lo "
                       "que alguien podria buscar algun dia. Los indices creados por intuicion "
                       "acaban siendo indices muertos: cobran escritura, cache y espacio de "
                       "respaldo, y no aparecen en ningun plan. Es literalmente lo que hace la "
                       "propuesta que abre la pregunta —«un indice sobre cada columna, por si "
                       "acaso»—, y por eso las dos opciones correctas de este par, la 0 y la 5, "
                       "son las dos caras del mismo argumento.",
                },
                "como_calificar": [
                    "**10 pts con las 4 correctas marcadas y ninguna incorrecta**, con puntaje "
                    "proporcional por acierto parcial, tal como dice la rubrica. La clave se lee "
                    "del banco de la plataforma.",
                    "**La opcion de la `FOREIGN KEY` es el discriminador tecnico de la "
                    "pregunta.** Se corrige con un dato, no con una opinion: `pg_indexes` de la "
                    "pregunta 1 lista `mascota_pkey` y `idx_mascota_dueno`, y **no** hay ningun "
                    "indice que el motor haya creado solo para la llave foranea. Si mas de un "
                    "tercio del grupo la marca, vale la pena volver a proyectar esa salida.",
                    "**La opcion de la baja cardinalidad ya esta refutada por su propia "
                    "evidencia.** Quien la marque tiene en su pregunta 2 un `Seq Scan` en Q3 "
                    "teniendo dos indices que empiezan por `estado`. Es la devolucion mas eficaz "
                    "que existe: su experimento contradice su respuesta.",
                    "Si alguien argumenta que un indice sobre `estado` **si** podria servir para "
                    "buscar `CANCELADA` —2.728 filas, el 9 %—, tiene razon y conviene decirlo: la "
                    "opcion es falsa por la palabra «siempre» y por «la mejor inversion», no "
                    "porque un indice de baja cardinalidad sea inutil en todos los casos. Ese "
                    "matiz es justamente el que hace valiosa la opcion del indice **parcial**.",
                ],
                "errores": [
                    "**Marcar la de la `FOREIGN KEY`.** Es una confusion muy extendida, "
                    "probablemente por analogia con la `PRIMARY KEY` —que si crea indice— y por "
                    "motores donde el comportamiento es distinto. En PostgreSQL el lado hijo de "
                    "una llave foranea queda sin indexar, y es una de las causas mas frecuentes de "
                    "lentitud inexplicada en bases que «ya tienen sus llaves».",
                    "**Marcar la de la baja cardinalidad,** normalmente por leer «`estado` se usa "
                    "en muchas consultas» y concluir que hay que indexarlo. Lo que decide no es "
                    "cuantas veces aparece la columna, es **que fraccion de la tabla devuelve el "
                    "filtro**. La regla de bolsillo: por debajo del 5–10 %, el indice suele ganar; "
                    "por encima de un tercio, casi nunca.",
                    "**No marcar la del espacio y la cache,** por pensar que «el disco es "
                    "barato». El disco es barato; la memoria de cache y la ventana de "
                    "restauracion, no. Un indice muerto expulsa paginas de datos utiles de la "
                    "cache y alarga cada restauracion, porque al restaurar los indices se "
                    "reconstruyen —eso conecta directo con el ensayo de restauracion de la "
                    "Clase 4—.",
                    "**Marcar las seis** o marcar solo la primera. Suele significar que la "
                    "pregunta se contesto antes de haber hecho las tres primeras. Las cuatro "
                    "correctas estan todas demostradas en el propio taller: la del parcial en la "
                    "pregunta 1, la de la cardinalidad y su contraria en la pregunta 2, y la de "
                    "medir antes de crear en la pregunta 5.",
                ],
            },
            {
                "n": 5,
                "titulo": "Tabla de justificacion consulta -> indice",
                "tipo": "abierta",
                "puntos": 20,
                "tabla": {
                    "headers": ["Indice", "Tabla y columnas", "Consulta del PI que lo usa",
                                "Cardinalidad de la lider", "Evidencia en EXPLAIN",
                                "Costo de mantenimiento", "Veredicto"],
                    "rows": [
                        ["`idx_cita_programada_fecha`",
                         "`cita (fecha_hora)` **parcial** `WHERE estado = 'PROGRAMADA'`",
                         "Agenda del dia: citas PROGRAMADA de una fecha. ~60-80 ejecuciones por "
                         "jornada, con alguien esperando en el mostrador",
                         "**Alta.** `fecha_hora` tiene ~30.000 valores distintos en 200 dias; el "
                         "indice cubre 18.187 de 30.010 filas (61 %)",
                         "`Index Scan using idx_cita_programada_fecha`, `Index Cond` sobre el "
                         "rango, **91 filas y `Rows Removed by Filter` desaparecido** (era "
                         "29.919). 12,8 ms → 0,4 ms",
                         "Una entrada por cada cita PROGRAMADA que agende "
                         "`sp_agendar_cita`. Al pasar a ATENDIDA, la entrada **sale** del indice: "
                         "el parcial se mantiene solo",
                         "**Se queda.** Es el indice mejor justificado del proyecto"],
                        ["`idx_cita_fecha_hora`",
                         "`cita (fecha_hora)`",
                         "Historico del dia y reportes por rango de fechas, **sin** filtro de "
                         "estado (cierre de caja, citas canceladas del mes)",
                         "**Alta.** La misma columna, pero cubriendo las 30.010 filas",
                         "En la agenda del dia el planeador prefirio el parcial. Para la consulta "
                         "sin filtro de estado si es el elegido: 150 filas por `Index Cond`",
                         "Una entrada por **cada** cita, en todo `INSERT` y en todo `UPDATE` de "
                         "`fecha_hora` (reprogramaciones)",
                         "**Se queda, pero es el primer candidato a revisar.** Si en el semestre "
                         "ninguna consulta por rango sin filtro de estado aparece de verdad, se "
                         "descarta y queda solo el parcial"],
                        ["`idx_mascota_dueno`",
                         "`mascota (id_dueno)`",
                         "Ficha del dueno: sus mascotas. Se abre en cada atencion, antes de "
                         "agendar",
                         "**Alta.** 2.006 duenos para 5.008 mascotas, ~2,5 mascotas por dueno",
                         "`Index Scan using idx_mascota_dueno`, `Index Cond: (id_dueno = 1234)`, "
                         "**2 filas de 5.008**. 2,9 ms → 0,1 ms",
                         "Bajo: `mascota` casi no cambia —una mascota se registra una vez—. "
                         "Ademas **ahorra** trabajo en cada `DELETE`/`UPDATE` de `dueno`, que sin "
                         "el recorre las 5.008 mascotas para verificar la llave foranea",
                         "**Se queda.** Lado hijo de una llave foranea: es el caso que se puede "
                         "dar por bueno casi sin medir"],
                        ["`idx_cita_estado_fecha`",
                         "`cita (estado, fecha_hora)`",
                         "La misma agenda del dia, escrita con la igualdad explicita. Creado en "
                         "la pregunta 2 para el experimento del orden",
                         "**Baja en la lider.** `estado` tiene solo 3 valores y `PROGRAMADA` es "
                         "el 61 % de la tabla",
                         "`Index Scan using idx_cita_estado_fecha` en Q1, con **las dos** "
                         "condiciones en `Index Cond` (91 filas). Pero en Q2 —solo rango— y en "
                         "Q3 —solo estado— el motor **no lo uso**",
                         "Una entrada por cada cita, y la entrada se **reescribe** en cada cambio "
                         "de estado porque `estado` es la columna lider",
                         "**Se cambia por el parcial.** Cubre el mismo caso de uso, es mas "
                         "pequeno y no se reescribe en cada cambio de estado. Mantener los dos es "
                         "sobre-indexar"],
                        ["`idx_cita_fecha_estado`",
                         "`cita (fecha_hora, estado)`",
                         "Ninguna propia: se solapa con `idx_cita_fecha_hora`, del que solo se "
                         "diferencia por llevar `estado` de acompanante",
                         "**Alta.** `fecha_hora` como lider",
                         "Era el elegido de Q2. Tras el `DROP INDEX` de la pregunta 2, Q2 volvio "
                         "al `Seq Scan` con `Rows Removed by Filter: 29860`: 0,5 ms → 11,4 ms",
                         "Una entrada por cita, mas ancha que la de `idx_cita_fecha_hora` por "
                         "llevar la segunda columna",
                         "**Se descarta,** o **reemplaza** a `idx_cita_fecha_hora` —no se "
                         "conservan los dos—. Un indice `(A, B)` sirve para todo lo que sirve "
                         "`(A)`; al reves no"],
                    ],
                },
                "respuesta": (
                    "**1. Regla de sobre-indexacion que adopto.** Ningun indice entra al proyecto "
                    "sin estas cuatro cosas, y la cuarta es la que casi nadie escribe:\n\n"
                    "- **(a) Una consulta documentada** que lo use, con su pantalla y su "
                    "frecuencia aproximada. «Por si buscamos por ahi algun dia» no es una "
                    "consulta.\n"
                    "- **(b) Evidencia de `EXPLAIN ANALYZE`** de que el planeador lo elige, "
                    "pegada en `/informe/07-indices.txt`. Un indice que no aparece en ningun plan "
                    "es un indice muerto que cobra escritura, cache y espacio de respaldo sin "
                    "devolver nada.\n"
                    "- **(c) El costo de escritura nombrado**: sobre que procedimiento del PI pesa "
                    "—`sp_agendar_cita`, `sp_registrar_consulta`— y con que frecuencia.\n"
                    "- **(d) Fecha de revision.** Cada indice se vuelve a mirar al final del "
                    "semestre, y el que no aparezca en ningun plan **se borra**. Sin esta regla la "
                    "lista de indices solo crece, porque agregar tiene un dueno y quitar no tiene "
                    "ninguno.\n\n"
                    "Y una regla derivada del experimento de la pregunta 2, que es la que mas "
                    "indices ahorra: **antes de crear un indice nuevo, comprobar si uno existente "
                    "ya lo cubre por su columna lider.** `(fecha_hora, estado)` sirve para todo lo "
                    "que sirve `(fecha_hora)`; `(estado, fecha_hora)` no sirve para nada de lo "
                    "que sirve `(fecha_hora)`. Aplicando eso, los cinco indices de la tabla se "
                    "quedan en **tres**: el parcial de la agenda, el de `fecha_hora` para el "
                    "historico y el de `mascota (id_dueno)`.\n\n"
                    "**2. Particionamiento: veredicto para VetCare.** **No, todavia no.** Y "
                    "conviene decirlo con los numeros propios: Huellitas atiende del orden de "
                    "**30 a 40 citas por dia**, unos 26 dias al mes, lo que da unas **10.000 "
                    "citas al ano** y aproximadamente **1,5 MB anuales** en la tabla `cita` con "
                    "sus indices. A ese ritmo, la tabla tarda **una decada** en alcanzar las "
                    "100.000 filas, un volumen que PostgreSQL atiende sin esfuerzo con los tres "
                    "indices de arriba. Particionar hoy agregaria complejidad permanente —una "
                    "particion nueva que crear cada ano y que **nadie va a recordar** hasta que un "
                    "`INSERT` falle con «no partition found for row»— para resolver un problema "
                    "que no existe. La regla que dejo escrita es un **umbral**: se revisa cuando "
                    "`cita` pase de **5 millones de filas** o cuando el archivado anual empiece a "
                    "necesitar una ventana de mantenimiento, lo que llegue primero.\n\n"
                    "Y sobre lo que **si** quedo demostrado, con honestidad: en ExamLab se "
                    "particiono una tabla de **5.010 filas**, y a ese volumen la ganancia de "
                    "**rendimiento no es apreciable** —la tabla entera cabe en memoria y un "
                    "recorrido completo cuesta poco mas de un milisegundo—. Los dos beneficios que "
                    "**si** se comprobaron son de otra naturaleza y no dependen del volumen:\n\n"
                    "- **La poda de particiones en el plan.** Al filtrar por el rango de 2026, "
                    "`cita_hist_2025` **no aparece** en el plan: no se abre, no se lee, no se "
                    "estima. Y la contraprueba lo confirma: sin filtro, el plan muestra las dos "
                    "bajo un `Append`. Eso es una propiedad estructural y se cumple igual con 5 "
                    "millones de filas, donde si seria una diferencia enorme.\n"
                    "- **La facilidad de archivado.** `DROP TABLE cita_hist_2025;` libera 2.620 "
                    "filas en una operacion de metadatos: sin WAL por fila, sin filas muertas, sin "
                    "`VACUUM` posterior. El `DELETE FROM cita WHERE fecha_hora < '2026-01-01'` "
                    "equivalente recorre la tabla, escribe 2.620 registros en el WAL, mantiene "
                    "todos los indices durante el borrado y **no devuelve el espacio** sin un "
                    "`VACUUM FULL` que bloquea la tabla. Con 2.620 filas es un detalle; a escala "
                    "es la diferencia entre un segundo y una ventana nocturna. La variante que se "
                    "usa cuando hay que conservar el dato es "
                    "`ALTER TABLE ... DETACH PARTITION`, y se conecta directo con el `pg_dump` de "
                    "la Clase 4.\n\n"
                    "Tambien aprendi un limite que no esperaba y que va al informe: la poda "
                    "**se pierde** si el filtro se envuelve en una funcion. Con "
                    "`EXTRACT(YEAR FROM fecha_hora) = 2026` el resultado sigue siendo correcto "
                    "—2.390— pero el plan lee **las dos** particiones y descarta 2.620 filas en "
                    "2025. Es el mismo antipatron de sargabilidad de la Clase 6 apareciendo en "
                    "otro nivel: alli costaba un indice, aqui cuesta una particion entera.\n\n"
                    "**Archivos del PI:** la tabla de arriba en `/informe/07-indices.md`, los "
                    "`CREATE INDEX` definitivos en `/db/04_indices.sql` —los tres que sobreviven, "
                    "no los cinco— y los planes en `/informe/07-planes.txt`, al lado de los de la "
                    "Clase 6 para poder comparar."
                ),
                "como_calificar": [
                    "**10 pts — la tabla, con al menos 3 indices y las 7 columnas.** Se reparte "
                    "por columna, no por fila: 1,5 pts que esten los 3 indices identificados con "
                    "su tabla y columnas, y 1,7 pts por cada una de las 5 columnas de contenido "
                    "—consulta del PI, cardinalidad, evidencia, costo, veredicto— evaluadas en el "
                    "conjunto de las filas. Una tabla con 5 indices y una columna vacia vale menos "
                    "que una con 3 indices completa.",
                    "**La columna de evidencia es la que decide la nota de esta pregunta.** Tiene "
                    "que traer el **nodo concreto** —`Index Scan using idx_...`, "
                    "`Bitmap Heap Scan`— y la caida de tiempo. «Mejoro» no es evidencia. Las "
                    "anclas que se pueden verificar contra las preguntas 1 y 2: el "
                    "`Rows Removed by Filter` que desaparece, las 91 filas, las 2 filas de C2, el "
                    "29.860 de despues del `DROP`.",
                    "**La columna de cardinalidad se califica por el razonamiento, no por el "
                    "numero.** Lo que se exige es que distinga **alta** —`fecha_hora`, "
                    "`id_dueno`— de **baja** —`estado`, 3 valores, 61 % de la tabla— y que "
                    "conecte eso con la utilidad del indice. Quien escriba «`estado` tiene baja "
                    "cardinalidad» y aun asi deje ese indice sin justificar el caso parcial, no "
                    "entendio la columna.",
                    "**La columna de veredicto tiene que decidir de verdad.** Los cinco indices de "
                    "las preguntas 1 y 2 **se solapan a proposito**, asi que una tabla donde los "
                    "cinco «se quedan» esta incompleta: falta ver que "
                    "`(fecha_hora, estado)` y `(fecha_hora)` cubren lo mismo, y que el parcial "
                    "hace innecesario el `(estado, fecha_hora)`. **Reducir cinco indices a tres "
                    "con argumento es la mejor respuesta posible a esta pregunta.**",
                    "**4 pts — la regla de sobre-indexacion, operativa y verificable.** «No crear "
                    "indices innecesarios» vale 1 de 4: no se puede verificar. Se dan los 4 pts "
                    "cuando la regla dice **quien** decide, **con que evidencia** y **cuando se "
                    "revisa**. La condicion de retiro —el indice que no aparezca en ningun plan se "
                    "borra— es lo que la vuelve una regla y no un deseo.",
                    "**6 pts — el veredicto sobre particionamiento.** 2 pts la estimacion de "
                    "volumen **propia** con la cuenta a la vista (citas por dia x dias), 2 pts la "
                    "decision con su umbral de revision, y 2 pts —los que exige la rubrica de "
                    "forma explicita— **reconocer que con 5.010 filas la ganancia de rendimiento "
                    "no es medible** y distinguir la poda de particiones y el archivado de la "
                    "mejora de velocidad. Un informe que presente el particionamiento del taller "
                    "como una mejora de rendimiento pierde los 6 pts completos, aunque el SQL de "
                    "la pregunta 3 este perfecto.",
                ],
                "errores": [
                    "**La tabla convertida en una lista de `CREATE INDEX`.** Se reconoce porque "
                    "las columnas de cardinalidad, costo y veredicto dicen lo mismo en todas las "
                    "filas, o estan vacias. La pregunta no pide inventariar los indices —eso ya lo "
                    "hizo `pg_indexes`—, pide **justificarlos uno por uno**.",
                    "**Todos los veredictos en «se queda».** Es la senal mas clara de que no se "
                    "comparo un indice contra otro. Los cinco indices del taller se solapan "
                    "deliberadamente, y quien no proponga retirar por lo menos uno se perdio el "
                    "punto de la clase, que es que **cada indice hay que pagarlo**.",
                    "**Confundir el costo de mantenimiento con el tamano.** «Ocupa 2 MB» no es el "
                    "costo que se pregunta. El costo es **sobre que escrituras del PI pesa**: cada "
                    "`INSERT` de `sp_agendar_cita` mantiene todos los indices de `cita`, y un "
                    "indice cuya columna lider es `estado` se **reescribe** en cada cambio de "
                    "estado. Ese es el dato que sirve para decidir.",
                    "**Escribir que el particionamiento «mejoro el rendimiento» del historico.** "
                    "Con 5.010 filas no mejoro nada medible, y el enunciado lo advierte por "
                    "escrito. Es el descuento mas grande de la pregunta y el mas facil de evitar. "
                    "La respuesta correcta reconoce el limite y **aun asi** defiende lo que si se "
                    "demostro: la poda en el plan y el archivado.",
                    "**Un veredicto de particionamiento sin numeros propios.** «Depende del "
                    "volumen» no decide nada. La rubrica pide una estimacion —citas por dia x "
                    "dias de operacion— y una conclusion. La cuenta cabe en una linea y es la que "
                    "convierte la opinion en criterio.",
                    "**Olvidar que la regla de sobre-indexacion necesita una condicion de "
                    "retiro.** Casi todas las entregas dicen como **crear** un indice y ninguna "
                    "dice cuando **borrarlo**. Por eso las bases reales acumulan indices muertos: "
                    "agregar tiene un responsable y quitar no tiene ninguno.",
                ],
            },
        ],
        "preguntas_frecuentes": [
            ("¿Por que el planeador eligio el indice parcial y no el completo, si los dos son "
             "sobre `fecha_hora`?",
             "Porque el parcial le cuesta menos por dos razones a la vez. Tiene **menos "
             "entradas** —18.187 contra 30.010, un 39 % menos de arbol que recorrer— y, sobre "
             "todo, **su definicion ya garantiza el estado**: todo lo que hay dentro es "
             "`PROGRAMADA`, asi que el motor lee las 91 entradas del dia y ninguna sobra. Con el "
             "indice completo tendria que leer las 150 citas del dia, ir a la tabla por cada una a "
             "mirar el `estado` y descartar 59. Si en tu corrida gano el completo, la diferencia "
             "de costo entre los dos es pequena: **reporta lo que viste**, que es lo que se "
             "califica."),
            ("Cree el indice y el plan no cambio. ¿El indice no sirve?",
             "Revisa tres cosas en este orden. **Una:** ¿corriste `ANALYZE` despues del "
             "`CREATE INDEX`? El planeador decide por costo estimado, y con estadisticas viejas "
             "puede ignorar un indice perfectamente bueno. **Dos:** ¿la columna lider del indice "
             "aparece en tu `WHERE`? A un arbol B solo se entra por la izquierda; es literalmente "
             "el experimento de la pregunta 2. **Tres:** ¿cuantas filas devuelve tu consulta? Si "
             "es mas de un tercio de la tabla, el motor **hace bien** en recorrerla completa "
             "—eso es lo que pasa en Q3—. Y si tras las tres el plan sigue igual y la consulta "
             "devuelve pocas filas, entonces si tienes un hallazgo que vale la pena mirar."),
            ("¿Que es un indice parcial y cuando conviene?",
             "Es un indice que solo incluye las filas que cumplen una condicion: "
             "`CREATE INDEX ... ON cita (fecha_hora) WHERE estado = 'PROGRAMADA';`. Conviene "
             "cuando las consultas **siempre** traen ese mismo filtro, y entonces gana dos veces: "
             "es mas pequeno y no tiene que reverificar la condicion. Tiene dos limites que hay "
             "que conocer. Uno: si una consulta **no** trae `estado = 'PROGRAMADA'`, el motor "
             "**no puede** usarlo, ni siquiera parcialmente —por eso el indice completo sobre "
             "`fecha_hora` sigue teniendo sentido para el historico—. Dos, y es la parte elegante: "
             "cuando una cita pasa a `ATENDIDA`, su entrada **sale** del indice sola; el parcial "
             "se mantiene pequeno sin que nadie lo limpie."),
            ("¿Por que la llave foranea no crea su indice automaticamente?",
             "Porque PostgreSQL crea indice para lo que necesita **garantizar** —la unicidad de "
             "una `PRIMARY KEY` o de un `UNIQUE`— y una llave foranea no garantiza unicidad, "
             "garantiza existencia, y para eso le basta el indice del lado **padre**, que ya "
             "existe. El lado **hijo** queda sin indexar, y eso se paga dos veces: «las mascotas "
             "de un dueno» recorre las 5.008 mascotas —lo mediste en la pregunta 1— y cada "
             "`DELETE` de un `dueno` hace ese mismo recorrido para comprobar que no queden "
             "mascotas huerfanas. Indexar el lado hijo de cada llave foranea es una de las "
             "poquisimas indexaciones que se pueden dar por buenas casi sin medir."),
            ("¿`(estado, fecha_hora)` y `(fecha_hora, estado)` no son lo mismo?",
             "No, y la pregunta 2 existe para que lo compruebes en tu propia maquina. Piensa en el "
             "indice como una guia telefonica: si esta ordenada por **apellido y luego nombre**, "
             "encontrar «todos los Gomez» es abrir en una pagina y leer seguido; encontrar «todos "
             "los que se llaman Ana» obliga a leerla entera. Aqui pasa igual: "
             "`(estado, fecha_hora)` fija `PROGRAMADA` y dentro de ese bloque las fechas ya vienen "
             "ordenadas, asi que el rango es un tramo contiguo de 91 entradas. Con "
             "`(fecha_hora, estado)`, las citas del 10 de marzo estan juntas pero repartidas en "
             "tres estados. La regla es **igualdad primero, rango despues**, y el corolario que "
             "mas indices ahorra es este: `(A, B)` sirve para todo lo que sirve `(A)`; al reves, "
             "no."),
            ("Borre `idx_cita_fecha_estado` y Q2 volvio al `Seq Scan`, pero "
             "`idx_cita_estado_fecha` **si** tiene `fecha_hora`. ¿Por que no la uso?",
             "Porque a un arbol B solo se entra por la **columna lider**, y `estado` no esta en tu "
             "`WHERE`. Para encontrar las citas del 10 de marzo con ese indice, el motor tendria "
             "que recorrer las **30.010 entradas** completas y ademas ir a la tabla por cada "
             "candidata —`id_cita` no esta en el indice, asi que no puede resolverlo sin la "
             "tabla—. Eso sale mas caro que el `Seq Scan`, y el planeador lo calcula: "
             "`Rows Removed by Filter: 29860`, de 0,5 ms a 11,4 ms. Es la demostracion "
             "experimental de la regla, y es el resultado que la pregunta busca."),
            ("¿Por que la PK de `cita_hist` tiene que llevar `fecha_hora`?",
             "Porque PostgreSQL implementa la unicidad con un indice **por particion**, no con uno "
             "global. Si la PK fuera solo `id_cita`, para garantizar que no se repite habria que "
             "revisar **todas** las particiones en cada `INSERT`, y el motor no lo hace: exige que "
             "la columna de particion este en la llave, porque asi sabe en cual particion buscar. "
             "Si lo intentas sin ella, el error es literal: «unique constraint on partitioned "
             "table must include all partitioning columns». La consecuencia practica es que "
             "`(id_cita, fecha_hora)` permite en teoria el mismo `id_cita` en dos anos distintos; "
             "en un historico de solo lectura, alimentado desde `cita`, eso no es un problema, "
             "pero hay que saberlo."),
            ("Particione la tabla y no quedo mas rapida. ¿Hice algo mal?",
             "No, y darte cuenta vale mas que la mejora que esperabas. Con **5.010 filas** la "
             "tabla entera cabe en memoria y recorrerla cuesta poco mas de un milisegundo: no hay "
             "de donde sacar una ganancia. Lo que si demostraste son dos cosas que **no dependen "
             "del volumen**: la **poda de particiones** —`cita_hist_2025` no aparece en el plan, y "
             "la contraprueba sin filtro muestra que si aparece cuando no hay nada que podar— y el "
             "**archivado**, un `DROP TABLE` de la particion contra un `DELETE` masivo. "
             "Escribelo asi en la pregunta 5: la rubrica premia esa distincion de forma explicita "
             "y penaliza el informe que presenta el particionamiento como una mejora de velocidad. "
             "Prueba ademas el filtro con `EXTRACT(YEAR FROM ...)`: veras que la poda se pierde, y "
             "ese hallazgo si es un resultado."),
        ],
        "cierre": [
            "Al terminar, cada estudiante debe tener: los tres indices de la pregunta 1 con su "
            "linea base, su `ANALYZE` y su `Index Scan` verificado en `pg_indexes`; el "
            "experimento del orden de columnas con los tres `EXPLAIN`, el `DROP INDEX` y la "
            "conclusion de igualdad-antes-de-rango; `cita_hist` particionada con "
            "**2.620 / 2.390** filas enrutadas y la poda visible en el plan; las cuatro "
            "afirmaciones correctas de la pregunta 4; y la tabla de justificacion de siete "
            "columnas con su regla de sobre-indexacion y su veredicto de particionamiento, mas "
            "`/db/04_indices.sql` y `/informe/07-planes.txt` guardados.",
            "Antes de cerrar hay que verificar **tres numeros y una coherencia**, y los cuatro se "
            "leen sin ejecutar nada. Que el `Rows Removed by Filter` de la agenda del dia **haya "
            "desaparecido** del plan de la pregunta 1 —era 29.919 en la Clase 6 y en la linea base "
            "de hoy—. Que tras el `DROP INDEX` de la pregunta 2 aparezca **29.860**, que es el "
            "numero que solo sale de haber corrido el experimento. Que el enrutamiento diga "
            "**2.620 y 2.390** y no un reparto mitad y mitad. Y la coherencia: quien acerto la "
            "opcion de la baja cardinalidad en la pregunta 4 **no** puede haber escrito en la "
            "pregunta 5 que `idx_cita_estado_fecha` se queda sin discutirlo, porque su propio Q3 "
            "muestra un `Seq Scan` teniendo ese indice disponible.",
            "Esta clase cierra la promesa que la Clase 6 dejo abierta —el `Seq Scan` de 30.010 "
            "filas se volvio un `Index Scan` de 91— y conviene decirlo en voz alta, porque es la "
            "unica vez del semestre en que una hipotesis escrita una semana antes se confirma con "
            "una medicion propia. Tambien conviene dejar la contraparte: esos indices hay que "
            "mantenerlos en cada `INSERT` de `sp_agendar_cita`, y la pregunta 5 obliga a reducir "
            "cinco indices a tres precisamente por eso. Y como puente: la Clase 8 deja de hablar "
            "de una sola sesion midiendo sola y pasa a **varias sesiones peleandose por la misma "
            "fila** —transacciones, aislamiento y bloqueos—, donde el problema ya no es el tiempo "
            "de una consulta sino quien espera a quien.",
        ],
    },

    8: {
        "titulo": "Solucion del taller · Clase 8 · Transacciones de facturacion y tuning de VetCare",
        "resumen": (
            "`sp_facturar` completo, con el patron de `UPDATE` condicional que resuelve la "
            "comprobacion y el descuento en **una sola sentencia**, la factura 4 por "
            "**27.400** y los stocks en 11, 58 y 5; la prueba de atomicidad donde el descuento "
            "que **si** habia alcanzado se deshace y el insumo 3 vuelve a 40 —con el detalle que "
            "sorprende a todo el mundo, que la factura exitosa despues del fallo sale con el id "
            "**5** y no con el 4—; el patron encapsulado en `fn_descontar_stock` devolviendo "
            "`true/false/true` sin dejar un solo stock negativo; la explicacion exacta de por que "
            "la base quedo intacta; y el checklist de tuning del PI con el hueco de concurrencia "
            "declarado por escrito."
        ),
        "total": 100,
        "nota_actividad": (
            "**El motor es PostgreSQL, no Oracle,** y esta clase es donde mas se nota. No existe "
            "`SQL%ROWCOUNT`: se usa `GET DIAGNOSTICS v_filas = ROW_COUNT;`. **No se pone `COMMIT` "
            "ni `ROLLBACK` dentro del procedimiento:** cada sentencia de nivel superior ya es su "
            "propia transaccion, y si el procedimiento lanza una excepcion, todo lo que hizo se "
            "deshace solo. Y una diferencia que en Oracle es un error y aqui no: una funcion "
            "**puede** ejecutar `UPDATE` y llamarse desde un `SELECT`, que es exactamente lo que "
            "hace la pregunta 3. Dos avisos operativos. Uno: cada pregunta arranca con su propia "
            "base recien sembrada, asi que la pregunta 2 **ya trae** `sp_facturar` creado —la "
            "version de referencia— y no hay que volver a escribirlo. Dos: hay que anunciar antes "
            "de empezar que ExamLab corre con **una sola sesion**, de modo que el escenario de dos "
            "recepcionistas facturando el mismo insumo a la vez **no se puede reproducir aqui**; "
            "eso no es un defecto del taller, es literalmente el entregable 4 de la pregunta 5 y "
            "el punto de partida de la Clase 10."
        ),
        "preguntas": [
            {
                "n": 1,
                "titulo": "sp_facturar: factura + detalle + descuento de stock, todo o nada",
                "tipo": "bd_sql",
                "puntos": 35,
                "sql": """CREATE OR REPLACE PROCEDURE sp_facturar(
    p_id_consulta INT,
    p_insumos     INT[],
    p_cantidades  INT[]
)
LANGUAGE plpgsql
AS $proc$
DECLARE
  v_id_factura INT;
  v_total      NUMERIC(12,2) := 0;   -- se acumula linea por linea
  v_precio     NUMERIC(12,2);
  v_filas      INT;                  -- para GET DIAGNOSTICS
  i            INT;
BEGIN
  -- --------------------------------------------------------------------
  -- 1) Los dos arreglos tienen que venir parejos. IS DISTINCT FROM y no
  --    <> porque array_length de un arreglo vacio devuelve NULL, y
  --    NULL <> NULL es NULL: con <> la validacion no dispararia y el
  --    bucle de abajo no se ejecutaria ninguna vez, dejando una factura
  --    en cero sin una sola linea.
  -- --------------------------------------------------------------------
  IF array_length(p_insumos, 1) IS DISTINCT FROM array_length(p_cantidades, 1) THEN
    RAISE EXCEPTION 'ERROR: insumos y cantidades deben tener la misma longitud';
  END IF;

  -- --------------------------------------------------------------------
  -- 2) Cabecera primero, con total 0. Hay que insertarla antes que las
  --    lineas porque detalle_factura tiene una FK hacia factura, y
  --    RETURNING ... INTO es la unica forma correcta de recuperar el id
  --    que acaba de generar el SERIAL: currval() o un MAX(id_factura)
  --    serian una carrera con cualquier otra sesion.
  -- --------------------------------------------------------------------
  INSERT INTO factura (id_consulta, total) VALUES (p_id_consulta, 0)
  RETURNING id_factura INTO v_id_factura;

  -- --------------------------------------------------------------------
  -- 3) Una pasada por linea de la factura.
  -- --------------------------------------------------------------------
  FOR i IN 1 .. array_length(p_insumos, 1) LOOP

    -- El precio se toma de la tabla, NO se recibe por parametro: quien
    -- factura no debe poder decidir el precio. Y se guarda en el detalle
    -- (precio_unit) para que la factura de hoy no cambie si manana sube
    -- el insumo.
    SELECT precio_unit INTO v_precio FROM insumo WHERE id_insumo = p_insumos[i];
    IF NOT FOUND THEN
      RAISE EXCEPTION 'ERROR: el insumo % no existe', p_insumos[i];
    END IF;

    -- ----------------------------------------------------------------
    -- EL PATRON DE LA CLASE. La comprobacion del stock va DENTRO del
    -- WHERE, no en un IF anterior. Asi comprobar y descontar son UNA
    -- sola sentencia: no hay ninguna ventana entre el "hay stock" y el
    -- "lo descuento" en la que otra sesion pueda meterse.
    -- Si no habia suficiente, el UPDATE no encuentra fila que cumpla la
    -- condicion y afecta 0 filas -- no falla, simplemente no hace nada --
    -- y por eso hay que preguntarle cuantas filas toco.
    -- ----------------------------------------------------------------
    UPDATE insumo
       SET stock = stock - p_cantidades[i]
     WHERE id_insumo = p_insumos[i]
       AND stock >= p_cantidades[i];

    GET DIAGNOSTICS v_filas = ROW_COUNT;   -- en Oracle seria SQL%ROWCOUNT
    IF v_filas = 0 THEN
      RAISE EXCEPTION 'ERROR: stock insuficiente del insumo % (se pidieron %)',
        p_insumos[i], p_cantidades[i];
    END IF;

    INSERT INTO detalle_factura (id_factura, id_insumo, cantidad, precio_unit)
    VALUES (v_id_factura, p_insumos[i], p_cantidades[i], v_precio);

    v_total := v_total + (v_precio * p_cantidades[i]);
  END LOOP;

  -- --------------------------------------------------------------------
  -- 4) Recien ahora se sabe el total. Y NO va ningun COMMIT aqui: el
  --    CALL de nivel superior ya es su propia transaccion. Si algo de
  --    arriba hubiera fallado, nada de esto existiria.
  -- --------------------------------------------------------------------
  UPDATE factura SET total = v_total WHERE id_factura = v_id_factura;

  RAISE NOTICE 'Factura % creada por %', v_id_factura, v_total;
END;
$proc$;

-- ======================================================================
-- CASO EXITOSO: 1 vacuna antirrabica (22.000), 2 jeringas (900) y
-- 3 gasas (1.200) para la consulta 4.
-- ======================================================================
CALL sp_facturar(4, ARRAY[1, 6, 5], ARRAY[1, 2, 3]);

SELECT f.id_factura, f.id_consulta, f.total FROM factura f ORDER BY f.id_factura;

SELECT id_insumo, nombre, stock FROM insumo ORDER BY id_insumo;

-- ======================================================================
-- Comprobacion de una linea, la que conviene pegar al calificar: el
-- total tiene que cuadrar con la suma de su propio detalle, no con un
-- numero escrito a mano.
-- ======================================================================
SELECT f.id_factura,
       f.total                                     AS total_en_la_cabecera,
       SUM(d.cantidad * d.precio_unit)             AS suma_del_detalle,
       f.total - SUM(d.cantidad * d.precio_unit)   AS debe_ser_cero,
       COUNT(*)                                    AS lineas
  FROM factura f
  JOIN detalle_factura d ON d.id_factura = f.id_factura
 WHERE f.id_factura = 4
 GROUP BY f.id_factura, f.total;""",
                "salida": """NOTICE:  Factura 4 creada por 27400.00

Facturas -- 4 filas

 id_factura | id_consulta |   total
------------+-------------+-----------
          1 |           1 |  71000.00
          2 |           2 |  47000.00
          3 |           3 |  60200.00
          4 |           4 |  27400.00     <-- la nueva

Insumos -- 6 filas

 id_insumo |         nombre          | stock
-----------+-------------------------+-------
         1 | Vacuna antirrabica      |    11     <-- 12 - 1
         2 | Vacuna triple felina    |     3
         3 | Antiparasitario oral    |    40
         4 | Suero fisiologico 500ml |    25
         5 | Gasa esteril            |     5     <-- 8 - 3
         6 | Jeringa 5ml             |    58     <-- 60 - 2

Comprobacion -- 1 fila

 id_factura | total_en_la_cabecera | suma_del_detalle | debe_ser_cero | lineas
------------+----------------------+------------------+---------------+--------
          4 |             27400.00 |         27400.00 |          0.00 |      3

Los cuatro numeros de la pregunta son 27.400, 11, 58 y 5, y conviene tenerlos a
la vista al calificar porque cada desviacion tiene una causa distinta:

  * Total 27.400 = 22.000x1 + 900x2 + 1.200x3. Si sale 24.100 (22.000 + 900 +
    1.200), el estudiante acumulo el precio sin multiplicar por la cantidad. Si
    sale 0, le falto el UPDATE factura SET total = ... del paso 4 y la cabecera
    quedo con el cero con que nacio.
  * Stocks 11, 58 y 5. Si los tres bajaron UNA sola unidad cada uno, el UPDATE
    dice stock = stock - 1 en vez de stock - p_cantidades[i].
  * detalle_factura pasa de 8 filas a 11. Si quedaron 9, el INSERT del detalle
    esta fuera del bucle.
  * La factura nueva es la 4 y su id_consulta es 4. Coinciden por casualidad
    --hay 3 facturas previas y la consulta pedida es la 4--; no es que el
    procedimiento copie uno en el otro.

El RAISE NOTICE final no se exige, pero cuando esta ahorra media hora de
depuracion en la pregunta 2: es la unica forma de ver el id y el total sin
consultar nada.""",
                "como_calificar": [
                    "**5 pts — la firma exacta** `sp_facturar(p_id_consulta INT, p_insumos INT[], "
                    "p_cantidades INT[])` como **procedimiento** en `plpgsql`, mas la validacion "
                    "de que los dos arreglos vengan parejos con su `RAISE EXCEPTION`. Se acepta "
                    "`<>` en lugar de `IS DISTINCT FROM`; se anota en la devolucion por que el "
                    "segundo es mejor —con un arreglo vacio, `array_length` devuelve `NULL` y la "
                    "comparacion con `<>` no dispara—.",
                    "**5 pts — `RETURNING id_factura INTO v_id_factura`.** Es un requisito "
                    "explicito de la rubrica. Resolverlo con `SELECT MAX(id_factura) INTO ...` o "
                    "con `currval()` vale 2 de los 5, y la devolucion tiene que decir por que: el "
                    "`MAX` es una carrera con cualquier otra sesion, y este taller entero es sobre "
                    "no dejar carreras abiertas.",
                    "**12 pts — el nucleo: el bucle con el `UPDATE` condicional.** 3 pts el "
                    "`FOR i IN 1 .. array_length(p_insumos, 1) LOOP`; **5 pts que la comprobacion "
                    "del stock este en el `WHERE` del `UPDATE`** y no en un `IF` previo —es el "
                    "aprendizaje de la clase y el que la pregunta 3 vuelve a pedir—; 4 pts el "
                    "`GET DIAGNOSTICS v_filas = ROW_COUNT;` con su `IF v_filas = 0 THEN RAISE "
                    "EXCEPTION`. Un `IF` previo que lee y luego decide vale 0 de esos 5 aunque el "
                    "resultado del caso exitoso sea correcto: funciona por casualidad, porque hay "
                    "una sola sesion.",
                    "**5 pts — el detalle y el total.** 2 pts el `INSERT INTO detalle_factura` "
                    "**dentro** del bucle con el `precio_unit` leido de la tabla, y 3 pts el "
                    "`UPDATE factura SET total = v_total` al final. Se verifica con la comprobacion "
                    "de una linea: `total - SUM(cantidad * precio_unit)` tiene que dar **0**.",
                    "**5 pts — el caso exitoso ejecutado, con los cuatro numeros:** factura 4 con "
                    "total **27.400** y stocks en **11, 58 y 5**. 2 pts el `CALL` mas los dos "
                    "`SELECT` finales que pide el enunciado, y 3 pts que los numeros salgan.",
                    "**3 pts — no aparece `COMMIT` dentro del procedimiento y no aparece "
                    "`SQL%ROWCOUNT`.** La rubrica lo verifica de forma explicita. Un `COMMIT` "
                    "dentro **rompe la atomicidad** que la pregunta 2 va a medir: se pierden los "
                    "3 pts y hay que avisarlo antes de que llegue a la pregunta 2, porque si no va "
                    "a concluir lo contrario de lo que la clase ensena.",
                ],
                "errores": [
                    "**Leer el stock y decidir despues:** `SELECT stock INTO v_stock ...; IF "
                    "v_stock >= p_cantidades[i] THEN UPDATE ...`. Es el error central de la clase "
                    "y el mas dificil de ver, porque en ExamLab **funciona**: con una sola sesion "
                    "nunca se pierde la carrera. Entre el `SELECT` y el `UPDATE` hay una ventana en "
                    "la que otra recepcionista puede haberse llevado la ultima vacuna. La "
                    "condicion va en el `WHERE`, y la pregunta 3 pide justificar exactamente eso.",
                    "**Poner `COMMIT` dentro del procedimiento,** por costumbre de Oracle. Es la "
                    "peor consecuencia posible en este taller: la cabecera de la factura queda "
                    "confirmada, y cuando la linea 2 falle la factura huerfana **se queda**. La "
                    "pregunta 2 va a mostrar `factura` con 4 filas en vez de 3 y el estudiante va "
                    "a concluir que PostgreSQL no es atomico.",
                    "**`GET DIAGNOSTICS` sin usar,** o mal escrito. Tres variantes reales: "
                    "declararlo y no comprobar nunca `v_filas`; escribir "
                    "`v_filas := SQL%ROWCOUNT`, que es Oracle y no compila; o comprobar "
                    "`IF v_filas > 0 THEN RAISE EXCEPTION`, invirtiendo la condicion —entonces "
                    "falla el caso bueno y pasa el malo—. Sin la comprobacion, el `UPDATE` que no "
                    "afecta filas **no falla**: la factura sale con el detalle escrito y el stock "
                    "sin descontar.",
                    "**`v_total := v_total + v_precio`,** olvidando la cantidad. Da **24.100** en "
                    "vez de 27.400 y es facil de pasar por alto porque el numero parece razonable. "
                    "La comprobacion `total - SUM(cantidad * precio_unit) = 0` lo detecta sin tener "
                    "que hacer cuentas.",
                    "**El `INSERT` del detalle fuera del bucle,** o el `UPDATE factura` **dentro** "
                    "del bucle. El primero deja una sola linea de tres —`detalle_factura` queda en "
                    "9 y no en 11—; el segundo funciona pero escribe tres veces la cabecera y es "
                    "un habito caro cuando la factura tenga treinta lineas.",
                    "**Recibir el precio por parametro** o escribirlo a mano en el `INSERT`. Dos "
                    "problemas de una vez: quien factura no debe poder decidir el precio, y el "
                    "detalle debe conservar el precio **vigente al facturar** para que la factura "
                    "de hoy no cambie cuando el insumo suba de precio. Por eso `detalle_factura` "
                    "tiene su propia columna `precio_unit`.",
                ],
            },
            {
                "n": 2,
                "titulo": "Probar la atomicidad: fallo a mitad de la factura",
                "tipo": "bd_sql",
                "puntos": 25,
                "sql": """-- ======================================================================
-- 1) FOTO INICIAL. Una sola fila, para poder compararla de un vistazo
--    con la foto final. Aqui sp_facturar YA VIENE CREADO en la base.
-- ======================================================================
SELECT (SELECT COUNT(*) FROM factura)                  AS facturas,
       (SELECT COUNT(*) FROM detalle_factura)          AS detalles,
       (SELECT stock FROM insumo WHERE id_insumo = 3)  AS stock_insumo_3,
       (SELECT stock FROM insumo WHERE id_insumo = 2)  AS stock_insumo_2;

-- ======================================================================
-- 2) EL INTENTO QUE DEBE FALLAR A MITAD DE CAMINO.
--    Linea 1: 2 unidades del insumo 3, que tiene 40  -> alcanza y se
--             descuenta de verdad (queda en 38).
--    Linea 2: 10 unidades del insumo 2, que tiene 3   -> NO alcanza.
--    El DO con EXCEPTION captura el error para que el script siga; sin
--    el, la plataforma se detendria aqui y no habria foto final.
-- ======================================================================
DO $$
BEGIN
  CALL sp_facturar(4, ARRAY[3, 2], ARRAY[2, 10]);
  RAISE NOTICE 'No deberia llegar aqui';
EXCEPTION WHEN OTHERS THEN
  RAISE NOTICE 'Fallo esperado: %', SQLERRM;
END $$;

-- ======================================================================
-- 3) FOTO FINAL. La MISMA consulta del punto 1, sin cambiarle una coma:
--    si se cambia, la comparacion no vale.
-- ======================================================================
SELECT (SELECT COUNT(*) FROM factura)                  AS facturas,
       (SELECT COUNT(*) FROM detalle_factura)          AS detalles,
       (SELECT stock FROM insumo WHERE id_insumo = 3)  AS stock_insumo_3,
       (SELECT stock FROM insumo WHERE id_insumo = 2)  AS stock_insumo_2;

-- Version directa de la comparacion, la que se pega al calificar: si los
-- cuatro dicen true, la atomicidad quedo demostrada.
SELECT (SELECT COUNT(*) FROM factura) = 3                  AS no_hay_factura_huerfana,
       (SELECT COUNT(*) FROM detalle_factura) = 8          AS no_hay_lineas_nuevas,
       (SELECT stock FROM insumo WHERE id_insumo = 3) = 40 AS el_descuento_parcial_se_deshizo,
       (SELECT stock FROM insumo WHERE id_insumo = 2) = 3  AS el_insumo_2_intacto;

-- ======================================================================
-- 4) COMPARACION Y CONCLUSION.
--
-- ANTES:   facturas 3 | detalles 8 | insumo 3 -> 40 | insumo 2 -> 3
-- DESPUES: facturas 3 | detalles 8 | insumo 3 -> 40 | insumo 2 -> 3
--          ... es decir, IDENTICO.
--
-- Y no es que el procedimiento no hubiera hecho nada antes de fallar:
-- alcanzo a insertar la cabecera de la factura, alcanzo a bajar el stock
-- del insumo 3 de 40 a 38 y alcanzo a escribir la primera linea del
-- detalle. TODO ESO SE DESHIZO cuando la segunda linea lanzo la
-- excepcion. El dato que lo prueba es el mas importante de la pregunta:
-- el stock del insumo 3 VOLVIO A 40. Si solo se mirara el conteo de
-- facturas, no se sabria si el procedimiento fallo antes o despues de
-- empezar a trabajar.
--
-- El mecanismo: el CALL de nivel superior es su propia transaccion, y al
-- propagarse la excepcion se revierte completa. El bloque
-- BEGIN ... EXCEPTION del DO agrega un savepoint implicito, que es lo que
-- permite capturar el error y seguir con el script -- pero lo que se
-- deshizo, se deshizo igual.
--
-- LO UNICO que NO se deshace es la secuencia del SERIAL: el id 4 de
-- factura quedo consumido. Las secuencias viven fuera de la transaccion
-- a proposito, porque si volvieran atras dos sesiones podrian recibir el
-- mismo id. Por eso la factura buena del paso 5 sale con el id 5.
-- ======================================================================

-- ======================================================================
-- 5) LA MISMA FACTURA, AHORA VIABLE: 3 unidades del insumo 2 en vez de
--    10. Mismo procedimiento, mismos insumos, misma consulta.
-- ======================================================================
CALL sp_facturar(4, ARRAY[3, 2], ARRAY[2, 3]);

SELECT f.id_factura, f.id_consulta, f.total FROM factura f ORDER BY f.id_factura;

SELECT d.id_detalle, d.id_factura, d.id_insumo, d.cantidad, d.precio_unit
  FROM detalle_factura d
 WHERE d.id_factura = (SELECT MAX(id_factura) FROM factura)
 ORDER BY d.id_detalle;

SELECT id_insumo, nombre, stock FROM insumo ORDER BY id_insumo;""",
                "salida": """FOTO INICIAL -- 1 fila

 facturas | detalles | stock_insumo_3 | stock_insumo_2
----------+----------+----------------+----------------
        3 |        8 |             40 |              3

EL INTENTO QUE FALLA

NOTICE:  Fallo esperado: ERROR: stock insuficiente del insumo 2 (se pidieron 10)
DO

El NOTICE 'No deberia llegar aqui' NO aparece: la excepcion corto el CALL antes.
Y el bloque termina en DO, no en ERROR, porque el EXCEPTION lo capturo -- que es
lo que permite que el script continue.

FOTO FINAL -- 1 fila

 facturas | detalles | stock_insumo_3 | stock_insumo_2
----------+----------+----------------+----------------
        3 |        8 |             40 |              3

Comparacion directa -- 1 fila

 no_hay_factura_huerfana | no_hay_lineas_nuevas | el_descuento_parcial_se_deshizo | el_insumo_2_intacto
-------------------------+----------------------+---------------------------------+---------------------
 t                       | t                    | t                               | t

El 40 es el numero de la pregunta. Los otros tres se pueden explicar diciendo que
el procedimiento «no llego a hacer nada», pero el insumo 3 SI habia bajado a 38
antes del fallo, y volvio solo. Eso es lo que la rubrica exige evidenciar y lo que
se descuenta si falta.

PASO 5 -- la misma factura, ahora viable

NOTICE:  Factura 5 creada por 112000.00

Facturas -- 4 filas

 id_factura | id_consulta |   total
------------+-------------+-----------
          1 |           1 |  71000.00
          2 |           2 |  47000.00
          3 |           3 |  60200.00
          5 |           4 | 112000.00     <-- el id 5, NO el 4

Detalle de la factura 5 -- 2 filas

 id_detalle | id_factura | id_insumo | cantidad | precio_unit
------------+------------+-----------+----------+-------------
          9 |          5 |         3 |        2 |     9500.00
         10 |          5 |         2 |        3 |    31000.00

Insumos -- 6 filas

 id_insumo |         nombre          | stock
-----------+-------------------------+-------
         1 | Vacuna antirrabica      |    12
         2 | Vacuna triple felina    |     0     <-- 3 - 3, exactamente en el limite
         3 | Antiparasitario oral    |    38     <-- 40 - 2, ahora si de verdad
         4 | Suero fisiologico 500ml |    25
         5 | Gasa esteril            |     8
         6 | Jeringa 5ml             |    60

Total 112.000 = 9.500x2 + 31.000x3. Y hay dos cosas que vale la pena senalar en
clase con esta salida delante:

  1. La factura salio con el id 5, no con el 4, y no es un error de nadie. El
     intento fallido consumio el 4 de la secuencia, y las secuencias NO vuelven
     atras con el ROLLBACK --a proposito: si volvieran, dos sesiones podrian
     recibir el mismo id--. En cualquier base real hay huecos en los ids y no
     significan datos perdidos: significan intentos que fallaron. Ese detalle no
     hay que explicarlo en el enunciado, pero si hay que estar preparado para la
     pregunta «¿por que hay huecos?».
  2. El insumo 2 quedo en 0 y no en negativo. Es el caso limite exacto: se
     pidieron 3 de 3. El WHERE stock >= p_cantidades[i] acepta la igualdad, que
     es lo correcto --pedir todo lo que hay es una venta valida--, y el
     CHECK (stock >= 0) de la tabla nunca tuvo que intervenir. Los dos
     mecanismos coinciden, que es la senal de que el diseno esta bien.""",
                "como_calificar": [
                    "**5 pts — la foto inicial y la foto final con la MISMA consulta,** 2 pts cada "
                    "una y 1 pt que sean literalmente identicas. Si la consulta cambia entre las "
                    "dos, no hay comparacion posible y se pierden los 5.",
                    "**5 pts — el intento invalido se captura sin abortar el script.** El `DO` con "
                    "su `EXCEPTION WHEN OTHERS` viene dado en el enunciado, asi que estos puntos se "
                    "dan por ejecutarlo y por mostrar el `NOTICE` con el `SQLERRM`. Si el script "
                    "murio en un `ERROR` y no hay foto final, la pregunta se queda sin la mitad de "
                    "su evidencia.",
                    "**8 pts — la demostracion con datos, 2 pts por cada una de las cuatro "
                    "afirmaciones:** `factura` sigue en 3, `detalle_factura` sigue en 8, **el "
                    "stock del insumo 3 volvio a 40** y el insumo 2 quedo intacto en 3. La tercera "
                    "es la que la rubrica exige de forma explicita: **si no se evidencia la "
                    "reversion del stock del primer insumo, se descuenta**, porque es la unica que "
                    "prueba que hubo trabajo hecho y deshecho.",
                    "**4 pts — la comparacion y la conclusion escritas en comentarios `--`.** No "
                    "basta con que los numeros esten: la rubrica pide compararlos «explicitamente». "
                    "Se dan los 4 pts cuando el comentario dice **que alcanzo a hacer** el "
                    "procedimiento antes de fallar y **que se deshizo**. Una conclusion que solo "
                    "diga «no quedo nada» vale 2 de 4.",
                    "**3 pts — la segunda llamada viable se ejecuta y se muestra el contraste.** "
                    "Total **112.000**, insumo 3 en 38 e insumo 2 en 0. Sin este paso la pregunta "
                    "solo demuestra que la base sabe deshacer, no que sabe hacer.",
                    "**Se reconoce como sobresaliente, sin puntos extra:** notar que la factura "
                    "buena salio con el **id 5** y explicar por que —las secuencias no vuelven "
                    "atras con el `ROLLBACK`, y no vuelven a proposito—. Casi nadie lo nota y es un "
                    "dato que en produccion evita dos horas de confusion. Si nadie del grupo lo "
                    "menciona, conviene proyectarlo y preguntarlo.",
                ],
                "errores": [
                    "**Mostrar solo el conteo de facturas.** «`factura` sigue en 3, luego hubo "
                    "`ROLLBACK`» es una conclusion debil: seria igual de cierta si el "
                    "procedimiento hubiera fallado **antes** de insertar la cabecera. Lo que prueba "
                    "la atomicidad es el **40** del insumo 3, porque ese descuento **si** se hizo "
                    "y **si** se deshizo. Es exactamente lo que la rubrica manda descontar.",
                    "**Cambiar la consulta entre la foto inicial y la final** —agregar una columna, "
                    "mirar otro insumo, contar de otra tabla—. Entonces las dos fotos no son "
                    "comparables y toda la pregunta se queda sin sustento. Se copia y se pega, "
                    "literal.",
                    "**Ejecutar el `CALL` invalido sin el `DO ... EXCEPTION`.** La plataforma corta "
                    "el script en el error y no queda foto final. La captura no es un adorno: es "
                    "lo que permite que la prueba y su verificacion vivan en la misma respuesta.",
                    "**Concluir que «PostgreSQL no es atomico» porque quedo una factura "
                    "huerfana.** Cuando esto aparece, el problema no esta en la pregunta 2: hay un "
                    "`COMMIT` dentro del `sp_facturar` de la pregunta 1. Vale la pena revisar las "
                    "dos preguntas juntas antes de calificar, porque la confusion se arrastra.",
                    "**Reportar que la factura buena es la 4.** Es la 5, y quien escriba 4 "
                    "normalmente no la ejecuto o la ejecuto en la base de la pregunta 1. No se "
                    "descuenta por no **explicar** el salto, pero si por reportar un numero que su "
                    "propia salida no muestra.",
                    "**Interpretar el insumo 2 en `0` como un error.** Es el caso limite correcto: "
                    "se pidieron 3 de 3 y `stock >= cantidad` acepta la igualdad. Un stock en cero "
                    "es un dato de negocio —hay que reponer—, no una violacion; la violacion seria "
                    "un **negativo**, y para eso estan el patron y el `CHECK`.",
                ],
            },
            {
                "n": 3,
                "titulo": "El patron de descuento seguro como funcion reutilizable",
                "tipo": "bd_sql",
                "puntos": 15,
                "sql": """CREATE OR REPLACE FUNCTION fn_descontar_stock(
    p_id_insumo INT,
    p_cantidad  INT
)
RETURNS BOOLEAN
LANGUAGE plpgsql
-- Sin IMMUTABLE ni STABLE: esta funcion ESCRIBE. El valor por omision es
-- VOLATILE y es el correcto; marcarla STABLE haria que el motor se
-- sintiera libre de reusar un resultado anterior, y aqui cada llamada
-- tiene que ejecutarse de verdad.
AS $fn$
DECLARE
  v_filas INT;
BEGIN
  -- Una cantidad de 0 o negativa NO es "no hay stock": es una llamada mal
  -- hecha, y por eso aqui SI se lanza excepcion. Ojo con el detalle: sin
  -- esta validacion, p_cantidad = -5 haria stock = stock + 5 y el UPDATE
  -- devolveria TRUE. Un regalo de inventario disfrazado de descuento.
  IF p_cantidad IS NULL OR p_cantidad <= 0 THEN
    RAISE EXCEPTION 'ERROR: la cantidad a descontar debe ser mayor que cero (llego %)',
      p_cantidad;
  END IF;

  -- El patron de la clase, otra vez: comprobar y descontar en UNA sola
  -- sentencia. La condicion del stock esta en el WHERE.
  UPDATE insumo
     SET stock = stock - p_cantidad
   WHERE id_insumo = p_id_insumo
     AND stock >= p_cantidad;

  GET DIAGNOSTICS v_filas = ROW_COUNT;

  -- Y aqui esta la diferencia de diseno con sp_facturar: "no hay stock"
  -- es una RESPUESTA, no un error. Quien llama decide que hacer con el
  -- FALSE -- ofrecer un sustituto, avisar al mostrador, apartar el
  -- pedido -- en vez de recibir una excepcion que le tumba la
  -- transaccion entera.
  RETURN v_filas = 1;
END;
$fn$;

-- ======================================================================
-- PRUEBA. Las tres respuestas en una sola fila, tal como pide el
-- enunciado. Y observese lo que esto significa: una funcion que hace
-- UPDATE, llamada desde un SELECT. En Oracle seria un error; en
-- PostgreSQL es legal y aqui es lo que se pide.
-- ======================================================================
SELECT fn_descontar_stock(5, 3)  AS caso_ok,         -- insumo 5 tiene 8 -> alcanza
       fn_descontar_stock(2, 10) AS caso_sin_stock,  -- insumo 2 tiene 3 -> no alcanza
       fn_descontar_stock(2, 3)  AS caso_limite;     -- insumo 2 tiene 3 -> justo justo

-- ======================================================================
-- ESTADO FINAL: ningun stock negativo.
-- ======================================================================
SELECT id_insumo, nombre, stock FROM insumo ORDER BY id_insumo;

-- Comprobacion de una linea, la que conviene pegar al calificar.
SELECT COUNT(*) FILTER (WHERE stock < 0)              AS negativos_debe_ser_cero,
       (SELECT stock FROM insumo WHERE id_insumo = 5) AS insumo_5_debe_ser_5,
       (SELECT stock FROM insumo WHERE id_insumo = 2) AS insumo_2_debe_ser_0
  FROM insumo;

-- Y la comprobacion de que la validacion de la cantidad tambien funciona:
-- esto tiene que fallar, no devolver TRUE.
DO $$
BEGIN
  PERFORM fn_descontar_stock(1, -5);
  RAISE NOTICE 'MAL: acepto una cantidad negativa';
EXCEPTION WHEN OTHERS THEN
  RAISE NOTICE 'Bien, la rechazo: %', SQLERRM;
END $$;

-- ======================================================================
-- POR QUE ESTE PATRON Y NO "leer primero, decidir despues"
--
-- El patron inseguro es este:
--     SELECT stock INTO v_stock FROM insumo WHERE id_insumo = X;
--     IF v_stock >= v_cantidad THEN
--       UPDATE insumo SET stock = stock - v_cantidad WHERE id_insumo = X;
--     END IF;
--
-- Entre el SELECT y el UPDATE hay una VENTANA. Con dos recepcionistas
-- facturando la ultima vacuna al mismo tiempo:
--
--   Sesion A: SELECT stock -> 1     "hay una, sigo"
--   Sesion B: SELECT stock -> 1     "hay una, sigo"   <-- las dos leyeron 1
--   Sesion A: UPDATE stock = 1 - 1 = 0                (correcto)
--   Sesion B: UPDATE stock = 0 - 1 = -1               (ya no habia)
--
-- Las dos leyeron un dato que era cierto cuando lo leyeron y falso cuando
-- actuaron. El nombre del problema es "comprobar y luego usar": la
-- decision se toma sobre una foto vieja.
--
-- Con la condicion en el WHERE no hay ventana, porque comprobar y
-- escribir son la MISMA sentencia y el motor bloquea la fila mientras la
-- modifica. En el nivel de aislamiento por omision de PostgreSQL
-- (READ COMMITTED), cuando la sesion B intenta actualizar una fila que A
-- esta cambiando, B ESPERA a que A termine y despues VUELVE A EVALUAR su
-- propio WHERE contra la version nueva de la fila. Entonces ve stock = 0,
-- la condicion stock >= 1 ya no se cumple, el UPDATE afecta 0 filas y la
-- funcion devuelve FALSE. Nadie queda en negativo y nadie tuvo que
-- coordinarse con nadie.
--
-- Y hay una segunda red, de la Clase 4: el CHECK (stock >= 0) de la
-- tabla. Si el patron estuviera mal escrito, el CHECK abortaria la
-- sentencia. La diferencia es que el CHECK GARANTIZA -- nunca habra un
-- negativo -- mientras el patron del WHERE EXPLICA y ademas permite
-- responder con elegancia: FALSE en vez de una excepcion.
--
-- LIMITE HONESTO: en ExamLab hay UNA sola sesion, asi que la carrera de
-- arriba NO se puede reproducir aqui. Lo escrito es el razonamiento, no
-- una medicion. Comprobarlo con dos sesiones es el tema de la Clase 10 y
-- es el "gap honesto" que pide la pregunta 5.
-- ======================================================================""",
                "salida": """Prueba -- 1 fila

 caso_ok | caso_sin_stock | caso_limite
---------+----------------+-------------
 t       | f              | t

true / false / true es el resultado de la pregunta. Y hay algo elegante en esta
prueba que conviene senalar: da lo mismo en que orden evalue el motor las tres
llamadas. Si fn_descontar_stock(2, 3) corriera antes que fn_descontar_stock(2,
10), el insumo 2 quedaria en 0 y la de 10 seguiria devolviendo false. La prueba
es correcta sin depender del orden de evaluacion de la lista de columnas, que es
algo que PostgreSQL NO garantiza y en lo que no conviene apoyarse.

Estado final -- 6 filas

 id_insumo |         nombre          | stock
-----------+-------------------------+-------
         1 | Vacuna antirrabica      |    12
         2 | Vacuna triple felina    |     0     <-- 3 - 3 (caso limite)
         3 | Antiparasitario oral    |    40
         4 | Suero fisiologico 500ml |    25
         5 | Gasa esteril            |     5     <-- 8 - 3 (caso ok)
         6 | Jeringa 5ml             |    60

El insumo 2 quedo en 0 y no en -7: la llamada de 10 unidades no toco nada. Eso es
el WHERE haciendo su trabajo, no el CHECK salvando la situacion -- y la
diferencia importa, porque un CHECK que salta aborta la sentencia mientras que el
WHERE simplemente responde false.

Comprobacion -- 1 fila

 negativos_debe_ser_cero | insumo_5_debe_ser_5 | insumo_2_debe_ser_0
-------------------------+---------------------+---------------------
                       0 |                   5 |                   0

Validacion de la cantidad

NOTICE:  Bien, la rechazo: ERROR: la cantidad a descontar debe ser mayor que cero (llego -5)

Esta ultima prueba no la pide el enunciado y vale la pena hacerla en clase,
porque el agujero que tapa no es evidente: sin la validacion, una cantidad
negativa haria stock = stock - (-5), es decir stock + 5, y la funcion devolveria
true. Un regalo de inventario disfrazado de descuento, y ademas silencioso.""",
                "como_calificar": [
                    "**4 pts — la firma y el tipo de retorno:** `fn_descontar_stock(p_id_insumo "
                    "INT, p_cantidad INT)` **`RETURNS BOOLEAN`** en `plpgsql`. Tiene que ser una "
                    "`FUNCTION`, no un `PROCEDURE`: un procedimiento no puede llamarse desde el "
                    "`SELECT` de prueba que pide el enunciado. Se descuenta si se declaro "
                    "`IMMUTABLE` o `STABLE` —hace `UPDATE`, tiene que ser `VOLATILE`, que es lo "
                    "que ya es por omision—.",
                    "**3 pts — la validacion de `p_cantidad > 0` con `RAISE EXCEPTION`.** Se "
                    "reconoce como sobresaliente quien ademas cubra el `NULL` con "
                    "`p_cantidad IS NULL OR p_cantidad <= 0`, porque `NULL <= 0` es `NULL` y no "
                    "dispara el `IF`.",
                    "**4 pts — el `UPDATE` condicional con `GET DIAGNOSTICS` y el "
                    "`RETURN v_filas = 1`.** 2 pts que la condicion del stock este en el `WHERE` y "
                    "2 pts que devuelva `FALSE` **sin lanzar excepcion** cuando no alcanza. Un "
                    "`RAISE EXCEPTION` en el caso de stock insuficiente vale 0 de esos 2: "
                    "contradice de frente el enunciado, que dice que aqui «no hay stock» es una "
                    "respuesta y no un error.",
                    "**2 pts — la prueba devuelve `true / false / true`** y el estado final deja el "
                    "insumo 5 en **5**, el 2 en **0** y **ningun negativo**. Es la unica "
                    "verificacion objetiva de la pregunta y no admite interpretacion.",
                    "**2 pts — el comentario `--` explica bien las dos cosas:** por que "
                    "leer-y-despues-decidir es vulnerable con varios usuarios, y por que la "
                    "condicion en el `WHERE` lo evita al resolver comprobacion y escritura en una "
                    "sola sentencia. Se dan los 2 pts completos cuando el estudiante narra la "
                    "carrera con las dos sesiones intercaladas; una frase generica sobre "
                    "«concurrencia» vale 1.",
                    "**Se reconoce como sobresaliente, sin puntos extra,** cualquiera de estas "
                    "tres: mencionar que en `READ COMMITTED` la segunda sesion **espera y vuelve a "
                    "evaluar** su `WHERE` contra la fila nueva —que es el mecanismo real, no una "
                    "metafora—; distinguir que el `CHECK (stock >= 0)` **garantiza** mientras el "
                    "`WHERE` **explica y responde**; o senalar que con una sola sesion en ExamLab "
                    "la carrera **no se puede reproducir** y que lo escrito es razonamiento, no "
                    "medicion. Esa ultima es literalmente el entregable 4 de la pregunta 5.",
                ],
                "errores": [
                    "**Lanzar excepcion cuando no hay stock.** Es la confusion de diseno de la "
                    "pregunta y viene de copiar `sp_facturar` sin leer el enunciado. Las dos "
                    "decisiones son correctas **en su sitio**: en `sp_facturar` la excepcion es "
                    "necesaria porque tiene que abortar la factura completa; en "
                    "`fn_descontar_stock` el `FALSE` deja que quien llama decida —ofrecer un "
                    "sustituto, avisar, apartar el pedido— sin perder su transaccion.",
                    "**Devolver `TRUE` siempre,** o devolver `v_filas` en vez de `v_filas = 1`. Lo "
                    "primero pasa cuando se olvida el `GET DIAGNOSTICS` y se devuelve un literal; "
                    "lo segundo no compila, porque `INT` no es `BOOLEAN`. La prueba lo delata al "
                    "instante: `caso_sin_stock` tiene que salir **`f`**.",
                    "**Volver al patron inseguro dentro de la funcion:** `SELECT stock INTO ...` y "
                    "luego un `IF`. Aqui es especialmente grave, porque la pregunta entera consiste "
                    "en **encapsular el patron seguro** para poder reutilizarlo. Si la funcion es "
                    "insegura, se acaba de crear una herramienta que propaga el error a todo el "
                    "proyecto.",
                    "**Omitir la validacion de la cantidad** y no darse cuenta de lo que abre: "
                    "`fn_descontar_stock(1, -5)` haria `stock - (-5) = stock + 5`, cumpliria "
                    "`stock >= -5` sin problema y devolveria `TRUE`. Un aumento de inventario "
                    "silencioso, autorizado por una funcion que se llama «descontar». Vale la pena "
                    "mostrar esta linea en clase.",
                    "**Declarar la funcion como `PROCEDURE`,** y despues no poder ejecutar el "
                    "`SELECT` de prueba. Un `PROCEDURE` se invoca con `CALL` y no devuelve valor; "
                    "lo que la pregunta necesita es un valor de retorno dentro de un `SELECT`.",
                    "**Explicar la vulnerabilidad sin narrarla.** «Puede haber problemas de "
                    "concurrencia» no explica nada. Lo que se pide es la secuencia: A lee 1, B lee "
                    "1, A descuenta a 0, B descuenta a -1. Con cuatro lineas queda claro; sin "
                    "ellas, el estudiante repitio una frase que oyo.",
                ],
            },
            {
                "n": 4,
                "titulo": "Que pasa con el bloque EXCEPTION en PL/pgSQL",
                "tipo": "cerrada",
                "puntos": 10,
                "justificacion": {
                    0: "**Incorrecta, y es la respuesta que da quien viene de Oracle.** En "
                       "PostgreSQL **no se pone** `ROLLBACK` dentro de un procedimiento: el "
                       "`sp_facturar` de referencia no tiene ninguno —se puede verificar en la "
                       "propia base de la pregunta 2— y la reversion ocurrio igual. Es mas: poner "
                       "un `COMMIT` ahi dentro es lo que **rompe** la atomicidad, porque confirma "
                       "la cabecera de la factura antes de que fallen las lineas.",
                    1: "**Incorrecta,** y ninguna base de datos serie funciona asi. Copiar cada "
                       "tabla antes de cada `CALL` seria inviable con tablas grandes. El mecanismo "
                       "real es el opuesto y mucho mas barato: PostgreSQL escribe versiones "
                       "**nuevas** de las filas modificadas y, al abortar, esas versiones "
                       "simplemente **nunca se vuelven visibles** para nadie. No se restaura nada, "
                       "se descarta lo que se habia escrito.",
                    2: "**Correcta, y hay que quedarse con las dos mitades porque son dos "
                       "mecanismos distintos.** *Primera mitad:* la sentencia `CALL` de nivel "
                       "superior es su propia transaccion —PostgreSQL no necesita un `BEGIN` "
                       "explicito para tenerla—, asi que cuando la excepcion se propaga hacia "
                       "afuera, **todo** el trabajo del procedimiento se deshace: la cabecera de la "
                       "factura, el descuento del insumo 3 de 40 a 38 y la primera linea del "
                       "detalle. *Segunda mitad:* un bloque `BEGIN ... EXCEPTION` en PL/pgSQL crea "
                       "un **savepoint implicito**, y eso es lo que permite que el `DO` de la "
                       "pregunta 2 capture el error y el script continue: se revierte lo hecho "
                       "dentro de ese bloque y la ejecucion sigue por el manejador. Sin la primera "
                       "mitad no habria atomicidad; sin la segunda, no habria foto final.",
                    3: "**Incorrecta, y es la mas tentadora de las cuatro falsas** porque explica "
                       "bien el resultado con el mecanismo equivocado. PL/pgSQL **no** acumula nada "
                       "en memoria: cada `UPDATE` se aplica de verdad, y dentro de la misma "
                       "transaccion el propio procedimiento **puede volver a leer** el stock ya "
                       "descontado. Se comprueba sin salir del taller: si los `UPDATE` no se "
                       "aplicaran hasta el final, el patron `WHERE stock >= cantidad` no podria "
                       "funcionar cuando la misma factura descuenta dos veces el mismo insumo, y "
                       "funciona.",
                    4: "**Incorrecta, y en esta base es facil de descartar: no hay ningun "
                       "trigger.** El trigger de stock es de la **Clase 4** y aqui no existe; lo "
                       "que protege el stock en esta base son el `CHECK (stock >= 0)` de la tabla y "
                       "el patron del `WHERE`. Y hay un error conceptual mas de fondo: un trigger "
                       "reacciona a **una** operacion sobre **una** fila; no tiene ninguna manera "
                       "de deshacer lo que otras sentencias hicieron antes en la misma "
                       "transaccion. Eso solo lo puede hacer el gestor de transacciones.",
                },
                "como_calificar": [
                    "**10 pts con la opcion correcta marcada; cualquier otra respuesta, 0.** Es una "
                    "pregunta de opcion unica y la rubrica no admite puntaje parcial. La clave se "
                    "lee del banco de la plataforma y es la que combina las dos mitades: el `CALL` "
                    "de nivel superior es su propia transaccion **y** el bloque "
                    "`BEGIN ... EXCEPTION` crea un savepoint implicito.",
                    "**La opcion del `ROLLBACK` explicito es la que mas se marca,** y se corrige "
                    "con un dato en vez de una explicacion: el `sp_facturar` de referencia esta "
                    "**en la base** de la pregunta 2 y no contiene ningun `ROLLBACK`. Vale la pena "
                    "proyectarlo, porque el mismo malentendido es el que hace que alguien escriba "
                    "`COMMIT` dentro del procedimiento de la pregunta 1.",
                    "**La opcion de «PL/pgSQL acumula los `UPDATE` en memoria» merece medio "
                    "minuto,** porque explica correctamente el resultado con el mecanismo "
                    "equivocado y por eso sobrevive a un examen rapido. La refutacion es del propio "
                    "taller: dentro de la misma transaccion el procedimiento vuelve a leer el stock "
                    "ya descontado, que es justamente lo que hace posible el patron del `WHERE`.",
                    "Al devolver la pregunta conviene pedir las **dos** mitades de la opcion "
                    "correcta, no solo la primera. Muchos estudiantes saben que el `CALL` es una "
                    "transaccion y no saben que el `BEGIN ... EXCEPTION` crea un savepoint "
                    "implicito —y es la segunda mitad la que explica por que el `DO` de la pregunta "
                    "2 pudo seguir corriendo despues del error—.",
                ],
                "errores": [
                    "**Marcar la del `ROLLBACK` explicito.** Es transferencia directa de Oracle. En "
                    "PostgreSQL el procedimiento no gestiona su transaccion: la hereda de la "
                    "sentencia que lo llamo. Quien marque esta opcion conviene revisarle la "
                    "pregunta 1, porque suele haber un `COMMIT` de mas.",
                    "**Marcar la del respaldo automatico de cada tabla.** Suele venir de la palabra "
                    "«`ROLLBACK`» entendida como «restaurar». No se restaura nada: se escribieron "
                    "versiones nuevas de las filas y esas versiones nunca llegaron a ser visibles. "
                    "La diferencia importa cuando en la Clase 10 haya que entender por que dos "
                    "sesiones ven cosas distintas de la misma fila.",
                    "**Marcar la del trigger.** En esta base no hay triggers —los de stock son de "
                    "la Clase 4—, asi que la opcion se cae con un `SELECT` a "
                    "`information_schema.triggers`. El error de fondo es de escala: un trigger "
                    "actua sobre una fila y una operacion; deshacer una transaccion es de otro "
                    "nivel del motor.",
                    "**Contestar bien por eliminacion y no poder explicarlo.** Se detecta en la "
                    "pregunta 2, donde la conclusion en comentarios queda vaga —«hubo "
                    "`ROLLBACK`»— sin decir **quien** lo hizo ni **por que**. Las dos preguntas se "
                    "califican juntas de forma natural: la 4 dice si conoce el mecanismo y la 2 si "
                    "lo sabe usar.",
                ],
            },
            {
                "n": 5,
                "titulo": "Checklist de tuning y transacciones del PI",
                "tipo": "abierta",
                "puntos": 15,
                "tabla": {
                    "headers": ["Transaccion de negocio", "Tablas que toca",
                                "Paso que puede fallar", "Que debe pasar si falla"],
                    "rows": [
                        ["**Facturar una consulta** (`sp_facturar`)",
                         "`factura` (cabecera), `detalle_factura` (una fila por linea), "
                         "`insumo` (descuento de stock)",
                         "El descuento de stock de **cualquiera** de las lineas: el `UPDATE ... "
                         "WHERE stock >= cantidad` afecta 0 filas. Tambien puede fallar un "
                         "`id_insumo` inexistente",
                         "**Todo o nada.** Se deshace la cabecera, las lineas ya escritas y los "
                         "descuentos ya aplicados. Verificado en la pregunta 2: el insumo 3 volvio "
                         "de 38 a **40**. El mostrador recibe el mensaje «stock insuficiente del "
                         "insumo N» y decide: sustituir, apartar o reponer"],
                        ["**Registrar una consulta y cerrar la cita** "
                         "(`sp_registrar_consulta`, Clase 3)",
                         "`consulta` (alta), `cita` (paso a `ATENDIDA`)",
                         "La cita no existe, esta `CANCELADA`, o ya tiene consulta —lo garantiza el "
                         "`UNIQUE (id_cita)`—. Tambien un precio nulo o no positivo",
                         "**Todo o nada.** Si el alta de la consulta falla, la cita **no** puede "
                         "quedar en `ATENDIDA`: seria una cita atendida sin diagnostico ni precio, "
                         "invisible para la facturacion. El caso inverso es peor: una consulta cuya "
                         "cita sigue `PROGRAMADA` se volveria a agendar"],
                        ["**Cancelar una cita y liberar la franja**",
                         "`cita` (paso a `CANCELADA`), `audit_cita` (traza del cambio de estado, "
                         "Clase 4)",
                         "Que la cita ya este `ATENDIDA` —una cita atendida no se cancela— o que el "
                         "registro en la auditoria falle",
                         "**Todo o nada, y en este orden de importancia:** si la auditoria no se "
                         "escribe, la cancelacion **tampoco** se confirma. Una cancelacion sin "
                         "traza es exactamente el caso que la auditoria existe para cubrir. Efecto "
                         "secundario deseado: la franja queda libre, porque `sp_agendar_cita` no "
                         "cuenta las `CANCELADA`"],
                    ],
                },
                "respuesta": (
                    "**2. Checklist de tuning.** Siete items, cada uno con estado y con evidencia "
                    "**concreta** —nombre de indice, archivo, consulta—, no con una casilla "
                    "marcada:\n\n"
                    "| # | Item | Estado | Evidencia concreta |\n"
                    "|---|---|---|---|\n"
                    "| 1 | Indices sobre columnas de filtro y join de las consultas frecuentes | "
                    "**listo** | `idx_cita_programada_fecha` (parcial), `idx_cita_fecha_hora` y "
                    "`idx_mascota_dueno`, en `/db/04_indices.sql`. Planes en "
                    "`/informe/07-planes.txt`: `Index Scan using idx_cita_programada_fecha`, 91 "
                    "filas, `Rows Removed by Filter` desaparecido |\n"
                    "| 2 | Consultas sin `SELECT *` en los reportes | **listo** | "
                    "`06_opt_despues.sql`: la agenda del dia proyecta 6 columnas en vez de ~20. "
                    "Revisado a mano el resto de `/db` y de la aplicacion |\n"
                    "| 3 | Predicados sargables | **listo** | Se elimino "
                    "`to_char(fecha_hora,'YYYY-MM-DD') = ...` y quedo el rango "
                    "`>= '2026-03-10' AND < '2026-03-11'`. Sin el cambio, "
                    "`idx_cita_programada_fecha` no se usaria: sargabilidad primero, indice "
                    "despues |\n"
                    "| 4 | Transacciones cortas, sin esperar al usuario con la transaccion "
                    "abierta | **parcial** | `sp_facturar` es una sola sentencia `CALL`: no hay "
                    "interaccion humana dentro. Pero la pantalla de facturacion **arma el "
                    "carrito** en memoria y llama al procedimiento **una sola vez** al confirmar; "
                    "falta revisar que ningun formulario deje una transaccion abierta mientras el "
                    "usuario piensa |\n"
                    "| 5 | Validaciones criticas en la base, no solo en la aplicacion | "
                    "**listo** | `CHECK (stock >= 0)` y `CHECK (cantidad > 0)`; "
                    "`UNIQUE (id_cita)` en `consulta`; `CHECK (estado IN (...))`; el trigger de "
                    "stock no negativo y las validaciones dentro de `sp_facturar` y "
                    "`fn_descontar_stock`. La aplicacion valida **tambien**, para dar mejores "
                    "mensajes, no en lugar de la base |\n"
                    "| 6 | `ANALYZE` / estadisticas al dia despues de cargas masivas | "
                    "**parcial** | Se corrio `ANALYZE cita; ANALYZE mascota;` tras crear los "
                    "indices de la Clase 7 y se comprobo su efecto —la estimacion paso de "
                    "`rows=1` a `rows=90` contra 91 reales—. Falta dejarlo **automatizado**: hoy "
                    "depende de que alguien se acuerde |\n"
                    "| 7 | Plan de respaldo con restauracion probada | **pendiente** | El plan "
                    "esta escrito (Clase 4): `pg_dump -Fc` diario 20:30, "
                    "`pg_dumpall --globals-only` 20:25, `pg_basebackup` semanal, WAL continuo, "
                    "**RPO 15 min / RTO 4 h**. El ensayo de restauracion **no se ha hecho ni una "
                    "vez**, asi que el RTO de 4 horas es una estimacion sin respaldo. Es el riesgo "
                    "mas grande del proyecto y se declara como tal |\n\n"
                    "Cuatro «listo», dos «parcial» y un «pendiente». La lista sirve precisamente "
                    "porque no esta toda en verde: los tres items que no lo estan son los tres que "
                    "hay que hacer, y estan nombrados.\n\n"
                    "**3. Decision documentada: por que `UPDATE ... WHERE stock >= cantidad` y no "
                    "leer primero.** El patron inseguro deja una **ventana** entre la lectura y la "
                    "escritura, y en esa ventana el dato leido puede dejar de ser cierto. Con dos "
                    "recepcionistas facturando la ultima vacuna a la vez:\n\n"
                    "```\n"
                    "Sesion A: SELECT stock -> 1     \"hay una, sigo\"\n"
                    "Sesion B: SELECT stock -> 1     \"hay una, sigo\"\n"
                    "Sesion A: UPDATE stock = 1 - 1 = 0     (correcto)\n"
                    "Sesion B: UPDATE stock = 0 - 1 = -1    (ya no habia)\n"
                    "```\n\n"
                    "Las dos leyeron un dato que era cierto al leerlo y falso al actuar. Con la "
                    "condicion en el `WHERE`, comprobar y descontar son **la misma sentencia**: la "
                    "sesion B espera a que A termine de modificar la fila y —en `READ COMMITTED`, "
                    "el nivel por omision— **vuelve a evaluar su propio `WHERE` contra la version "
                    "nueva**, ve `stock = 0`, afecta 0 filas y `GET DIAGNOSTICS ROW_COUNT` lo "
                    "delata. Nadie queda en negativo y nadie tuvo que coordinarse con nadie.\n\n"
                    "> **La frase para la sustentacion:** «El stock se descuenta con la "
                    "comprobacion dentro del `WHERE` porque asi verificar y escribir son una sola "
                    "operacion indivisible; leer primero y decidir despues deja una ventana en la "
                    "que el dato leido ya no es cierto, y con dos recepcionistas facturando el "
                    "mismo insumo esa ventana es un stock negativo.»\n\n"
                    "**4. Gap honesto: la concurrencia no se pudo comprobar.** PostgreSQL en el "
                    "navegador corre con **una sola sesion**, asi que todo lo del punto 3 es un "
                    "**razonamiento, no una medicion**. Concretamente, tres cosas quedaron sin "
                    "verificar:\n\n"
                    "- **El escenario de las dos recepcionistas.** No se pudo abrir una segunda "
                    "sesion, dejar una transaccion a medias y ver a la otra esperar. La carrera "
                    "que el patron previene **nunca ocurrio** en las pruebas, porque no podia "
                    "ocurrir: todos los `true` y `false` de la pregunta 3 salieron de una sola "
                    "sesion, donde el patron inseguro habria dado exactamente los mismos "
                    "resultados. **Eso es lo incomodo de admitir: el taller no distingue el codigo "
                    "correcto del incorrecto.**\n"
                    "- **Los bloqueos y su duracion.** No se midio cuanto espera la segunda sesion "
                    "ni que pasa si la primera no confirma nunca. Tampoco se pudo provocar un "
                    "**interbloqueo** —dos facturas que descuentan los mismos dos insumos en orden "
                    "inverso—, que es el problema real de esta operacion en produccion.\n"
                    "- **La diferencia entre niveles de aislamiento.** Todo corrio en "
                    "`READ COMMITTED` sin poder compararlo con `REPEATABLE READ` ni con "
                    "`SERIALIZABLE`, que es donde el mismo patron cambia de comportamiento.\n\n"
                    "**Como se aborda en la Clase 10, en concreto:** la Clase 10 trabaja con dos "
                    "sesiones simuladas y transacciones explicitas, y ahi se van a hacer tres "
                    "cosas. **(a)** Reproducir la carrera con el patron **inseguro**, para verlo "
                    "fallar de verdad y no solo en un comentario. **(b)** Repetir el mismo "
                    "escenario con el patron del `WHERE` y comprobar que la segunda sesion espera, "
                    "vuelve a evaluar y recibe `false`. **(c)** Provocar un interbloqueo a "
                    "proposito y ver como PostgreSQL lo detecta y mata una de las dos "
                    "transacciones, para decidir una **regla de orden de descuento** —por "
                    "`id_insumo` ascendente— que lo prevenga. Con eso, el item 4 del checklist "
                    "puede pasar de «parcial» a «listo» con evidencia, y no antes.\n\n"
                    "**Archivos del PI:** esta seccion en `/informe/08-transacciones-tuning.md`, "
                    "`sp_facturar` y `fn_descontar_stock` en `/db/02_procedimientos.sql`, y las "
                    "salidas de la prueba de atomicidad en `/informe/08-atomicidad.txt` —la foto "
                    "inicial, la final y el `40` del insumo 3—."
                ),
                "como_calificar": [
                    "**5 pts — el inventario de transacciones, al menos 3.** Cada una vale 1,7 pts "
                    "y se reparte en tres tercios: **tablas** que toca, **paso que puede fallar** y "
                    "**que debe pasar si falla**. El tercero es el que se queda corto: «se hace "
                    "`ROLLBACK`» vale medio tercio, porque no dice que ve el usuario ni que estado "
                    "queda. Se exige nombrar el paso concreto —«el `UPDATE` de stock afecta 0 "
                    "filas»—, no «puede fallar algo».",
                    "**5 pts — el checklist con los 7 items, estado y evidencia concreta.** "
                    "Aproximadamente 0,7 pts por item. **La evidencia es lo que se califica:** un "
                    "nombre de indice, un archivo, una consulta, un numero. La rubrica dice "
                    "explicitamente «no solo casillas marcadas», asi que un checklist con siete "
                    "«listo» y ninguna evidencia vale 1 de 5. **Un checklist con «parcial» y "
                    "«pendiente» bien argumentados vale mas que uno todo en verde**, y conviene "
                    "decirlo en voz alta antes del taller: el item 7 —restauracion probada— todavia "
                    "**no** puede estar listo en ningun proyecto del curso.",
                    "**2 pts — la decision del `UPDATE` condicional, con la frase defendible.** "
                    "1 pt el argumento —la ventana entre leer y escribir— y 1 pt que la frase de "
                    "cierre sea de verdad una frase sostenible en sustentacion, no un parrafo. Se "
                    "premia con el punto completo quien narre la carrera con las dos sesiones "
                    "intercaladas.",
                    "**3 pts — el gap de concurrencia reconocido y con plan.** 1,5 pts admitir que "
                    "con **una sola sesion** el escenario de dos recepcionistas **no se pudo "
                    "comprobar**, y 1,5 pts un plan concreto para la Clase 10. «Lo vere en la "
                    "Clase 10» vale 0 de esos 1,5: se pide **que** se va a hacer. Un informe que "
                    "presente la concurrencia como resuelta pierde los 3 pts completos, aunque todo "
                    "el SQL de las preguntas 1 a 3 este perfecto.",
                    "**Se reconoce como sobresaliente, sin puntos extra pero se anota:** admitir "
                    "que en una sola sesion el patron **inseguro** habria dado exactamente los "
                    "mismos resultados que el seguro, y que por lo tanto el taller **no distingue** "
                    "el codigo correcto del incorrecto. Es la observacion mas madura que puede "
                    "hacer un estudiante en esta clase y es la mejor entrada posible a la "
                    "Clase 10.",
                    "**Extension:** una pagina. Se califica que las cuatro partes esten con "
                    "contenido verificable, no la longitud. El item que mas se olvida del checklist "
                    "es el 7, y es el unico del que se espera un «pendiente»: si alguien lo marca "
                    "«listo», hay que preguntarle cuando corrio el ensayo de restauracion.",
                ],
                "errores": [
                    "**El checklist como siete casillas marcadas.** Es el error dominante de esta "
                    "pregunta y la rubrica lo penaliza de frente. Sin evidencia, un «listo» no se "
                    "puede verificar ni auditar y no significa nada. El minimo aceptable por item "
                    "es un nombre propio: un indice, un archivo, una consulta, un numero.",
                    "**Marcar el item 7 como «listo» sin haber restaurado nunca.** Tener el plan de "
                    "respaldo escrito no es tenerlo probado, y esa es exactamente la leccion de la "
                    "Clase 4: un respaldo que no se ha restaurado es una hipotesis. Es el item en "
                    "el que un «pendiente» honesto vale mas que un «listo» falso.",
                    "**Presentar la concurrencia como resuelta.** Aparece como «el patron del "
                    "`WHERE` garantiza que no haya problemas de concurrencia, verificado en la "
                    "pregunta 3». No se verifico nada: hubo **una sola sesion**. El patron es "
                    "correcto y el razonamiento es correcto, pero la evidencia no existe todavia. "
                    "Confundir las dos cosas es lo que la pregunta esta midiendo.",
                    "**Un inventario de menos de tres transacciones,** o tres que en realidad son "
                    "la misma con distinto nombre. Las tres del taller son bien distintas y estan "
                    "todas construidas: facturar (Clase 8), registrar consulta y cerrar cita "
                    "(Clase 3), cancelar cita con su auditoria (Clase 4). Si alguien no encuentra "
                    "tres, el problema es que no esta releyendo su propio proyecto.",
                    "**Confundir «transaccion corta» con «consulta rapida».** El item 4 no es sobre "
                    "milisegundos: es sobre **no dejar una transaccion abierta esperando a un "
                    "humano**. Una transaccion de 50 ms que espera a que alguien confirme en "
                    "pantalla puede retener un bloqueo diez minutos. La distincion es la que hace "
                    "util el item.",
                    "**Un plan para la Clase 10 que es solo un titulo.** «Probare la concurrencia» "
                    "no es un plan. Lo que se pide es el escenario: dos sesiones, que hace cada "
                    "una, en que orden y que se espera observar. Quien ya lo tenga escrito llega a "
                    "la Clase 10 con el ejercicio medio hecho.",
                ],
            },
        ],
        "preguntas_frecuentes": [
            ("¿Por que no puedo poner `COMMIT` dentro del procedimiento?",
             "Porque destruye justo lo que la clase quiere demostrar. La sentencia `CALL` de nivel "
             "superior **ya es** su propia transaccion: no hace falta abrirla ni cerrarla. Si pones "
             "un `COMMIT` despues de insertar la cabecera de la factura, esa cabecera queda "
             "confirmada, y cuando la segunda linea falle por stock la factura huerfana **se "
             "queda** —con su total en cero y sin un solo detalle—. La pregunta 2 va a mostrarte "
             "`factura` con 4 filas en vez de 3 y vas a concluir que PostgreSQL no es atomico, "
             "cuando lo que pasa es que le quitaste la atomicidad tu. Si el procedimiento lanza una "
             "excepcion, **todo** lo que hizo se deshace solo, sin escribir una linea."),
            ("¿Que es `GET DIAGNOSTICS` y por que no puedo usar `SQL%ROWCOUNT`?",
             "`SQL%ROWCOUNT` es de Oracle y en PL/pgSQL no existe. El equivalente es "
             "`GET DIAGNOSTICS v_filas = ROW_COUNT;` inmediatamente despues de la sentencia que "
             "quieres medir —si pones otra sentencia en medio, mides esa otra—. Y es "
             "**imprescindible** en este patron por una razon que no es obvia: un `UPDATE` que no "
             "encuentra ninguna fila que cumpla el `WHERE` **no falla**; afecta 0 filas y sigue "
             "adelante tranquilamente. Sin preguntar cuantas filas toco, tu factura saldria con el "
             "detalle escrito y el stock sin descontar."),
            ("¿Por que la condicion del stock va en el `WHERE` y no en un `IF` antes?",
             "Porque el `IF` deja una **ventana**. Con dos recepcionistas facturando la ultima "
             "vacuna: A lee stock 1 y decide seguir, B lee stock 1 y decide seguir, A descuenta a "
             "0, B descuenta a **-1**. Las dos leyeron un dato que era cierto cuando lo leyeron y "
             "falso cuando actuaron. Con la condicion en el `WHERE`, comprobar y descontar son "
             "**una sola** sentencia: B espera a que A termine con la fila, vuelve a evaluar su "
             "propio `WHERE` contra la version nueva, ve `stock = 0`, afecta 0 filas y `ROW_COUNT` "
             "te lo dice. En ExamLab las dos versiones funcionan igual porque hay una sola sesion "
             "—esa es exactamente la trampa, y es el hueco que tienes que declarar en la "
             "pregunta 5—."),
            ("¿Por que la factura buena salio con el id 5 y no con el 4?",
             "Porque el intento fallido **consumio** el 4 de la secuencia, y las secuencias no "
             "vuelven atras con el `ROLLBACK`. Es a proposito: si volvieran, dos sesiones que "
             "pidieran un id al mismo tiempo podrian recibir el mismo numero, y entonces el "
             "`SERIAL` no serviria para nada. La consecuencia practica es que en cualquier base "
             "real **hay huecos** en los ids, y no significan datos perdidos: significan intentos "
             "que fallaron. Si alguien te pide «numeracion consecutiva sin huecos» para las "
             "facturas —y en Colombia la facturacion electronica lo pide—, eso **no** se resuelve "
             "con un `SERIAL`: hace falta una tabla de consecutivos con su propio bloqueo, y cuesta "
             "concurrencia."),
            ("En la pregunta 3, ¿por que `FALSE` y no una excepcion, si en `sp_facturar` si "
             "lanzamos excepcion?",
             "Porque son dos decisiones de diseno distintas y las dos son correctas **en su "
             "sitio**. En `sp_facturar` la excepcion es necesaria: si una linea no se puede servir, "
             "la factura completa no debe existir, y la excepcion es lo que consigue que se deshaga "
             "todo. En `fn_descontar_stock` el «no hay stock» es una **respuesta**: quien llama "
             "recibe `false` y decide —ofrecer un sustituto, avisar al mostrador, apartar el "
             "pedido— sin perder su transaccion. La regla general: **excepcion cuando la operacion "
             "no puede continuar; valor de retorno cuando quien llama tiene algo que decidir.**"),
            ("¿Una funcion puede hacer `UPDATE` y llamarse desde un `SELECT`?",
             "En PostgreSQL si, y es lo que pide la pregunta 3. En Oracle seria un error "
             "—`ORA-14551`—, asi que si venias de alli el reflejo es dudarlo. Dos cuidados. Uno: "
             "**no** la marques `IMMUTABLE` ni `STABLE`; el valor por omision es `VOLATILE` y es el "
             "correcto, porque una funcion que escribe tiene que ejecutarse de verdad en cada "
             "llamada. Dos: el orden en que el motor evalua varias funciones en la misma lista de "
             "columnas **no esta garantizado**, asi que no construyas una prueba que dependa de el. "
             "En este caso da igual —revisa por que en la salida esperada—, pero es suerte, no "
             "diseno."),
            ("¿Para que sirve el `CHECK (stock >= 0)` si el patron del `WHERE` ya lo evita?",
             "Para lo mismo que el cinturon cuando ya frenaste bien. Son dos cosas distintas: el "
             "`CHECK` **garantiza** —no existe forma de dejar un stock negativo en esa tabla, ni con "
             "un `UPDATE` a mano, ni con un procedimiento nuevo mal escrito, ni con una carga "
             "masiva— y el patron del `WHERE` **explica y responde**, porque en vez de abortar la "
             "sentencia devuelve `false` y permite reaccionar con elegancia. Es la misma pareja de "
             "la Clase 4: la restriccion es la garantia, el codigo es la explicacion. Si en tu "
             "prueba salta el `CHECK`, no celebres que te salvo: significa que el patron esta mal "
             "escrito."),
            ("¿Por que el `DO $$ ... EXCEPTION ... END $$` permite que el script siga despues del "
             "error?",
             "Porque un bloque `BEGIN ... EXCEPTION` en PL/pgSQL crea un **savepoint implicito**. "
             "Cuando la excepcion sube desde el `CALL`, el motor deshace lo hecho **dentro** de ese "
             "bloque, entra al manejador y continua desde ahi: por eso ves el "
             "`NOTICE 'Fallo esperado: ...'` y el bloque termina en `DO` en vez de `ERROR`. Es la "
             "segunda mitad de la respuesta correcta de la pregunta 4, y es la mitad que casi nadie "
             "menciona. Sin ella no tendrias foto final, y sin foto final no habria prueba de "
             "atomicidad."),
        ],
        "cierre": [
            "Al terminar, cada estudiante debe tener: `sp_facturar` con el `UPDATE` condicional y "
            "el `GET DIAGNOSTICS`, la factura **4** por **27.400** y los stocks en 11, 58 y 5; la "
            "prueba de atomicidad con las dos fotos identicas, el **40** del insumo 3 recuperado y "
            "la factura viable por **112.000**; `fn_descontar_stock` devolviendo `true/false/true` "
            "con el insumo 5 en 5, el 2 en 0 y ningun negativo; la opcion correcta de la pregunta "
            "4; y la seccion de transacciones y tuning con las tres transacciones inventariadas, "
            "los siete items con evidencia y el hueco de concurrencia declarado, en "
            "`/informe/08-transacciones-tuning.md`.",
            "Antes de cerrar hay que verificar **tres numeros y una ausencia**, y los cuatro se "
            "leen sin ejecutar nada. Que el total de la factura nueva sea **27.400** y no 24.100 "
            "—24.100 significa que se acumulo el precio sin multiplicar por la cantidad—. Que el "
            "stock del insumo 3 haya **vuelto a 40** en la pregunta 2, que es el unico dato que "
            "prueba que hubo trabajo hecho y deshecho. Que la funcion de la pregunta 3 devuelva "
            "**`f`** en el caso sin stock y que no quede ni un negativo. Y la ausencia: que **no** "
            "aparezca la palabra `COMMIT` dentro de ningun procedimiento —si aparece, hay que "
            "revisar la pregunta 2 de esa misma entrega, porque la conclusion va a estar "
            "invertida—.",
            "Dejar dicho en voz alta el limite de la clase, porque es el mejor puente del "
            "semestre: **todo lo que se argumento hoy sobre dos recepcionistas facturando a la vez "
            "no se pudo comprobar**, porque ExamLab corre con una sola sesion. Y hay una "
            "consecuencia incomoda que vale la pena decir sin adornos: en una sola sesion, el "
            "patron **inseguro** —leer y despues decidir— habria dado exactamente los mismos "
            "`true` y `false` que el seguro. El taller no distingue el codigo correcto del "
            "incorrecto; lo distingue el razonamiento. La Clase 10 lo convierte en medicion: dos "
            "sesiones simuladas con transacciones explicitas, la carrera reproducida primero con "
            "el patron malo para verla fallar, luego con el bueno para ver a la segunda sesion "
            "esperar y recibir `false`, y un interbloqueo provocado a proposito para decidir la "
            "regla de orden de descuento. El item 4 del checklist pasa a «listo» ese dia, y no "
            "antes.",
        ],
    },

    10: {
        "titulo": "Solucion del taller · Clase 10 · Control de concurrencia en VetCare",
        "resumen": (
            "La linea de tiempo de la doble reserva con el intervalo exacto en que **las dos** "
            "transacciones leyeron `COUNT(*) = 0`, y la razon de fondo de por que ninguna "
            "validacion podia detectarlo —**no se puede bloquear una fila que todavia no "
            "existe**—; la reproduccion en SQL con las dos citas aceptadas, la deteccion "
            "encontrando la franja duplicada, el **indice unico parcial** cerrandola y la prueba "
            "de que no es excesiva porque la `CANCELADA` si entra; los dos mecanismos de stock "
            "—`UPDATE` condicional dando `true/false` y `FOR UPDATE` / `NOWAIT` / `SKIP LOCKED`— "
            "con la explicacion de por que en una sola sesion los tres se ven iguales; y el "
            "informe con el contrato de errores para la aplicacion y el limite del entorno "
            "declarado sin adornos."
        ),
        "total": 100,
        "nota_actividad": (
            "**Esta es una clase autonoma: no hay docente en vivo,** asi que el enunciado tiene "
            "que sostenerse solo y esta solucion se usa sobre todo para calificar y para responder "
            "por escrito. Conviene publicar un aviso el mismo dia con las tres cosas que mas se "
            "atascan y que estan resueltas aqui: que el `CREATE UNIQUE INDEX` de la pregunta 2 "
            "**falla** si no se borro antes el duplicado —y ese fallo es informacion, no un "
            "error—; que la pregunta 3 pide **dos** mecanismos y no dos versiones del mismo; y que "
            "en la pregunta 5 el punto 4 se califica por reconocer el limite, no por disimularlo. "
            "**El motor es PostgreSQL, no Oracle:** aqui aparecen `GET DIAGNOSTICS ... ROW_COUNT`, "
            "`FOR UPDATE SKIP LOCKED` y `EXCEPTION WHEN unique_violation`, que no tienen "
            "equivalente literal en Oracle. Y el aviso central del dia: ExamLab corre PostgreSQL "
            "compilado a WebAssembly con **una unica conexion**, asi que **ningun** bloqueo real, "
            "ninguna espera y ningun interbloqueo se pueden observar. Toda la clase esta disenada "
            "alrededor de eso: se demuestra lo que **si** es demostrable con una sesion —que la "
            "base **acepta** el dato invalido sin restriccion y lo **rechaza** con ella— y se "
            "declara por escrito lo que no."
        ),
        "preguntas": [
            {
                "n": 1,
                "titulo": "Escenario de doble reserva con linea de tiempo T1/T2",
                "tipo": "abierta",
                "puntos": 25,
                "tabla": {
                    "headers": ["Momento", "Transaccion T1 (Recepcion A)",
                                "Transaccion T2 (Recepcion B)", "Estado de la tabla `cita`",
                                "Comentario"],
                    "rows": [
                        ["**t0**", "`BEGIN`", "—",
                         "0 citas para (vet 1, 2026-10-12 09:00)",
                         "A contesta el telefono: el dueno de Firulais quiere el lunes a las 9"],
                        ["**t1**", "—", "`BEGIN`",
                         "0 citas para esa franja",
                         "B contesta otra linea: la duena de Luna quiere **la misma** franja. "
                         "Ninguna de las dos sabe de la otra"],
                        ["**t2**", "`SELECT COUNT(*) ... = 0` **-> 0**", "—",
                         "0 citas para esa franja",
                         "A valida y **cree** que la franja esta libre. Es verdad: en este "
                         "instante lo esta. **El `SELECT` no toma ningun bloqueo**"],
                        ["**t3**", "—", "`SELECT COUNT(*) ... = 0` **-> 0**",
                         "0 citas para esa franja",
                         "**AQUI ESTA LA FALLA.** B valida y tambien lee **0**, porque A no ha "
                         "insertado nada todavia. **Las dos leyeron 0 antes de que cualquiera "
                         "escribiera:** este es el instante que hay que senalar"],
                        ["**t4**", "`INSERT` (Firulais, vet 1, 09:00)", "—",
                         "1 fila (no confirmada por A)",
                         "A inserta. La fila existe pero **nadie fuera de A la ve**: la "
                         "transaccion sigue abierta"],
                        ["**t5**", "—", "`INSERT` (Luna, vet 1, 09:00)",
                         "2 filas (una por transaccion, ninguna visible a la otra)",
                         "B inserta. **Su validacion ya paso hace dos pasos y nadie la va a "
                         "repetir.** Sin restriccion en la tabla, no hay nada que se oponga"],
                        ["**t6**", "`COMMIT`", "—",
                         "1 fila confirmada",
                         "A confirma. La franja ya esta ocupada de verdad"],
                        ["**t7**", "—", "`COMMIT`",
                         "**2 filas confirmadas en la misma franja**",
                         "B confirma. La base acepta el dato invalido **sin un solo error**: nadie "
                         "le pidio que lo impidiera. Laura Restrepo tiene dos pacientes a las 9:00"],
                    ],
                },
                "respuesta": (
                    "El intervalo critico es **t2–t5**: entre la primera lectura y la ultima "
                    "escritura, las dos transacciones sostienen una creencia —«la franja esta "
                    "libre»— que era cierta cuando la formaron y falsa cuando actuaron sobre "
                    "ella. Vale la pena decirlo asi porque describe **toda** la familia de "
                    "problemas de concurrencia: no hay un dato mal leido en ninguna parte; hay una "
                    "decision tomada sobre una foto que envejecio.\n\n"
                    "**1. Nombre de la anomalia y por que `READ COMMITTED` no la evita.** Es un "
                    "**write skew sobre un predicado**, y en la forma concreta en que aparece aqui "
                    "—dos transacciones que consultan un predicado y despues **insertan** filas "
                    "que lo cambian— se le llama tambien **lectura fantasma** (*phantom*): la fila "
                    "de la otra transaccion es un fantasma que no estaba cuando cada una miro. "
                    "`READ COMMITTED` **no** lo evita, y no por descuido, sino porque hace "
                    "exactamente lo que promete y nada mas:\n\n"
                    "- Garantiza que cada sentencia vea una foto de lo **confirmado** en el "
                    "instante en que esa sentencia empieza. En t3 el `INSERT` de A todavia no "
                    "existe (t4) y, aunque existiera, no estaria confirmado hasta t6. B lee **0** "
                    "y esa lectura es **correcta**. No hay lectura sucia, no hay lectura mal "
                    "hecha: hay una lectura veraz que caduco.\n"
                    "- **Y la razon de fondo, que es la que hay que entender: un `SELECT COUNT(*)` "
                    "no bloquea nada, y no puede.** Un bloqueo se pone sobre **filas que existen**, "
                    "y aqui el conflicto lo produce una fila que **todavia no existe** en ninguna "
                    "de las dos transacciones. Ni siquiera un `SELECT ... FOR UPDATE` sobre el "
                    "resultado del `COUNT(*)` ayudaria: no hay ninguna fila que bloquear. Por eso "
                    "la unica salida es **desplazar el candado a otro objeto** —una fila que si "
                    "exista, como la del veterinario; una estructura fisica, como el B-tree de un "
                    "indice unico; o un bloqueo de predicado, que es lo que hace `SERIALIZABLE`—.\n\n"
                    "> La frase corta: **el problema no es que se lea mal, es que se decide sobre "
                    "algo que no se puede bloquear porque no existe.**\n\n"
                    "**2. Que pasaria en el negocio.** No es un problema estetico:\n\n"
                    "- **Para la clinica:** dos duenos con confirmacion escrita de la misma hora, "
                    "y quien lo descubre es la recepcionista del turno de la manana, delante de "
                    "los dos. La respuesta invariable es dar por buena la primera y reagendar la "
                    "segunda «por un error del sistema», que es la version publica de «nadie "
                    "puso una restriccion».\n"
                    "- **Para la veterinaria:** una consulta de 30 minutos se convierte en dos de "
                    "15, o en 60 minutos que desbordan la agenda del resto del dia. Si la agenda "
                    "estaba completa, el retraso se arrastra hasta la ultima cita.\n"
                    "- **Para los duenos:** uno espera con su mascota estresada en la sala, y el "
                    "otro se lleva la impresion de que su reserva no vale nada. En una clinica "
                    "chica esa impresion se paga en la siguiente vacunacion.\n"
                    "- **Y el dano invisible:** el reporte de ocupacion queda inflado. La franja "
                    "de las 9:00 aparece con dos citas, y cualquier decision que se tome sobre "
                    "ese dato —contratar, ampliar horario, medir productividad— parte de un "
                    "numero falso.\n\n"
                    "**3. Tres mitigaciones, de la mas fuerte a la mas debil.** El orden no es de "
                    "gusto: es por **quien queda a cargo de que la regla se cumpla**.\n\n"
                    "| # | Mitigacion | Que garantiza | Que cuesta | Que hace la aplicacion cuando la base rechaza |\n"
                    "|---|---|---|---|---|\n"
                    "| **(a)** | **Indice unico parcial** `CREATE UNIQUE INDEX uq_cita_vet_franja "
                    "ON cita (id_veterinario, fecha_hora) WHERE estado <> 'CANCELADA';` | "
                    "**La garantia mas fuerte que existe: no hay forma de que el dato invalido "
                    "entre.** No depende del orden, ni de la velocidad, ni de que el procedimiento "
                    "este bien escrito, ni de que manana alguien haga un `INSERT` a mano. Funciona "
                    "**precisamente porque** las transacciones son simultaneas: la segunda que "
                    "intenta escribir la misma clave **espera** en el B-tree del indice y, cuando "
                    "la primera confirma, recibe el error | Un indice mas que mantener en cada "
                    "`INSERT` y `UPDATE` de `cita` —costo real pero minimo—, y hay que decidir la "
                    "condicion parcial con cuidado: sin el `WHERE estado <> 'CANCELADA'`, una "
                    "franja liberada por una cancelacion no se podria volver a usar nunca | "
                    "Captura `unique_violation` (SQLSTATE **23505**) y **no** la muestra en crudo. "
                    "Traduce: «esa franja se acaba de ocupar», recarga la agenda del dia y ofrece "
                    "las franjas libres mas cercanas. **No reintenta el mismo `INSERT`:** volveria "
                    "a fallar |\n"
                    "| **(b)** | **`SELECT ... FOR UPDATE` sobre una fila que si exista** —la del "
                    "veterinario— antes de validar: `SELECT 1 FROM veterinario WHERE "
                    "id_veterinario = 1 FOR UPDATE;` y luego el `COUNT(*)` y el `INSERT` | "
                    "Serializa a todas las transacciones que agenden con **ese** veterinario: la "
                    "segunda espera y, cuando entra, su `COUNT(*)` ya ve la cita de la primera y "
                    "se detiene sola. Es una garantia **fuerte pero condicionada**: solo protege "
                    "a quien recuerde pedir el candado | **Es el que cuesta mas.** Reduce la "
                    "concurrencia a una reserva a la vez por veterinario, y una transaccion lenta "
                    "hace esperar a todas las demas. Y si dos operaciones bloquean varias filas en "
                    "orden distinto, aparece el **interbloqueo**. Sobre todo: **es una convencion, "
                    "no una garantia** —un `INSERT` que se olvide del `FOR UPDATE` pasa por "
                    "encima— | Recibe una espera, no un error: la operacion simplemente tarda. Si "
                    "el `COUNT(*)` posterior encuentra la franja ocupada, es la propia aplicacion "
                    "la que decide y mensaje: «franja ocupada, elige otra». Con `NOWAIT` recibiria "
                    "**55P03** y podria decir «intentalo de nuevo en un momento» |\n"
                    "| **(c)** | **`SET TRANSACTION ISOLATION LEVEL SERIALIZABLE`** con reintento "
                    "en la aplicacion | La garantia teorica mas limpia: PostgreSQL vigila los "
                    "**predicados** leidos —no solo las filas— y, si el resultado final no "
                    "equivale a haber ejecutado las transacciones una tras otra, **aborta una de "
                    "las dos**. Es la unica de las tres que resuelve el fantasma *sin* que haya "
                    "que anticipar la regla ni nombrar la columna | Costo de seguimiento en el "
                    "servidor, y sobre todo **obliga a que toda la aplicacion sepa reintentar**. "
                    "El error llega **al confirmar**, no al escribir, asi que hay que poder "
                    "repetir la operacion completa. Un solo camino de codigo sin reintento "
                    "convierte la garantia en errores intermitentes para el usuario | Captura "
                    "`serialization_failure` (SQLSTATE **40001**) y **reintenta la transaccion "
                    "entera** —de forma automatica, con un tope de 3 intentos y una espera "
                    "creciente—. Solo si agota los intentos muestra un mensaje. Es el unico caso "
                    "de los tres en que reintentar **es** la respuesta correcta |\n\n"
                    "**Recomendacion para VetCare: (a), y ademas.** La (a) es la que se implementa "
                    "en la pregunta 2 porque es **estructural**: sigue funcionando cuando alguien "
                    "reescriba `sp_agendar_cita`, cuando entre un `INSERT` desde un script de "
                    "carga o cuando el proximo semestre llegue otro programador. La (b) y la (c) "
                    "protegen **codigo**; la (a) protege **datos**. Las tres no son alternativas "
                    "excluyentes: lo razonable es (a) como red de la que no se puede escapar, y la "
                    "aplicacion traduciendo el `23505` a un mensaje util."
                ),
                "como_calificar": [
                    "**10 pts — la linea de tiempo, con al menos 6 pasos y las cinco columnas "
                    "pedidas.** 4 pts la estructura y que los pasos esten intercalados de verdad "
                    "—T1 y T2 alternandose, no primero toda T1 y despues toda T2—; **6 pts que "
                    "quede senalado con precision el intervalo en que las dos leyeron `COUNT(*) = "
                    "0` antes de que cualquiera insertara**. La rubrica lo dice explicitamente: "
                    "**se descuenta si la narrativa no distingue el instante de la lectura del de "
                    "la escritura.** Una tabla donde T1 lee, inserta y confirma antes de que T2 "
                    "lea no describe el problema: describe el caso que funciona bien.",
                    "**5 pts — el nombre de la anomalia y por que `READ COMMITTED` no la evita.** "
                    "2 pts el nombre: se acepta **lectura fantasma**, **phantom**, **write skew "
                    "sobre un predicado** o cualquiera de las dos con la otra como sinonimo. 3 pts "
                    "la explicacion, y aqui hay dos niveles: decir que «cada sentencia ve una foto "
                    "nueva de lo confirmado» vale 2 de 3; **llegar a que un `SELECT COUNT(*)` no "
                    "bloquea nada porque la fila del conflicto todavia no existe** vale los 3 y es "
                    "la comprension real del problema.",
                    "**3 pts — el impacto en el negocio,** repartido entre clinica, veterinaria y "
                    "los dos duenos. Se piden efectos concretos y no adjetivos: «dos duenos a la "
                    "misma hora y una agenda que se corre el resto del dia» vale; «afecta la "
                    "calidad del servicio» no. Se reconoce como sobresaliente quien note el dano "
                    "invisible —el reporte de ocupacion queda inflado y las decisiones que salgan "
                    "de ahi parten de un numero falso—.",
                    "**7 pts — las tres mitigaciones, aproximadamente 2,3 pts cada una,** y cada "
                    "una vale por sus **tres** partes: que garantiza, que cuesta y que hace la "
                    "aplicacion cuando la base rechaza. La tercera parte es la que casi siempre "
                    "falta y es la que la rubrica nombra: sin ella, la mitigacion es un buen deseo "
                    "sin contrato.",
                    "**Se reconoce como sobresaliente, sin puntos extra:** notar que reintentar es "
                    "la respuesta correcta **solo** con `SERIALIZABLE` —el `40001` es reintentable "
                    "y el `23505` no lo es, porque el segundo `INSERT` volveria a fallar siempre—; "
                    "o senalar que la (b) y la (c) protegen **codigo** mientras la (a) protege "
                    "**datos**, y que por eso la (a) sobrevive a que alguien reescriba el "
                    "procedimiento.",
                    "**Extension:** la tabla mas una pagina. No se premia la longitud. Si la linea "
                    "de tiempo esta bien y las tres mitigaciones traen sus tres partes, la "
                    "pregunta esta completa en menos de lo que la mayoria escribe.",
                ],
                "errores": [
                    "**La linea de tiempo secuencial en vez de intercalada:** T1 valida, inserta y "
                    "confirma; despues T2 valida, ve 1 y se detiene. Es el error dominante y "
                    "delata que no se entendio el problema, porque esa secuencia **funciona "
                    "correctamente**: es lo que pasa cuando no hay concurrencia. El defecto solo "
                    "existe si las dos lecturas caen **antes** de la primera escritura.",
                    "**Decir que `READ COMMITTED` «lee datos sucios» o que «lee mal».** Es al "
                    "contrario: PostgreSQL **nunca** permite lecturas sucias, en ningun nivel. "
                    "Aqui las dos lecturas son veraces. Confundir esto lleva directo a marcar mal "
                    "la opcion de `READ UNCOMMITTED` en la pregunta 4.",
                    "**Proponer «poner el `SELECT` y el `INSERT` mas cerca» o «hacer la "
                    "transaccion mas rapida» como mitigacion.** Reducir la ventana **no** es "
                    "cerrarla: con dos recepcionistas y una ventana de 5 milisegundos, el problema "
                    "pasa de diario a mensual, y un problema mensual de agenda es peor que uno "
                    "diario porque nadie lo relaciona con el software.",
                    "**Afirmar que un `SELECT ... FOR UPDATE` sobre `cita` resolveria el "
                    "problema.** No hay nada que bloquear: la fila en conflicto **no existe** "
                    "todavia. Si se elige la via (b), el candado tiene que ir sobre una fila que "
                    "si exista —la del veterinario— y usarla como representante de la franja. "
                    "Quien no vea esta distincion tampoco va a poder justificar por que la (a) "
                    "funciona.",
                    "**Presentar las tres mitigaciones sin decir que hace la aplicacion.** «Se "
                    "crea un `UNIQUE` y listo» deja al usuario final viendo "
                    "`duplicate key value violates unique constraint \"uq_cita_vet_franja\"` en "
                    "pantalla. La restriccion es la mitad del trabajo; la otra mitad es "
                    "traducirla a «esa franja se acaba de ocupar, aqui tienes las tres mas "
                    "cercanas».",
                    "**Ordenar las mitigaciones al azar** o justificar el orden por dificultad de "
                    "implementacion. El enunciado pide **de la mas fuerte a la mas debil**, y "
                    "fuerte significa **de quien no se puede escapar**: la restriccion no depende "
                    "de nadie, el `FOR UPDATE` depende de que todo el mundo lo pida, y el "
                    "`SERIALIZABLE` depende de que toda la aplicacion sepa reintentar.",
                ],
            },
            {
                "n": 2,
                "titulo": "Reproducir la doble reserva y cerrarla con una restriccion",
                "tipo": "bd_sql",
                "puntos": 25,
                "sql": """-- ======================================================================
-- PASO 1. MOSTRAR EL PROBLEMA.
-- Las dos citas del escenario de la pregunta 1: mismo veterinario, misma
-- franja, dos mascotas distintas. La tabla NO tiene ninguna restriccion
-- de unicidad de franja, asi que las dos entran sin un solo error.
-- Esto no es un fallo del motor: es que nadie le pidio que lo impidiera.
-- ======================================================================
INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, estado) VALUES
  (1, 1, TIMESTAMP '2026-10-12 09:00:00', 'PROGRAMADA'),   -- Firulais, Recepcion A
  (2, 1, TIMESTAMP '2026-10-12 09:00:00', 'PROGRAMADA');   -- Luna, Recepcion B

INSERT INTO evidencia (paso, resultado) VALUES
  ('sin restriccion',
   'PROBLEMA: las dos citas se insertaron sin error. La franja del veterinario 1 '
   'el 2026-10-12 09:00 quedo con 2 citas PROGRAMADA.');

-- ======================================================================
-- PASO 2. EVIDENCIAR EL DATO INVALIDO.
-- Esta consulta es la que hay que dejar escrita en el proyecto: es la que
-- responde "¿tengo el problema hoy?" sin depender de que alguien se
-- acuerde de revisar. Devuelve exactamente la franja duplicada.
-- ======================================================================
SELECT id_veterinario,
       fecha_hora,
       COUNT(*) AS citas_en_la_misma_franja
  FROM cita
 WHERE estado <> 'CANCELADA'
 GROUP BY id_veterinario, fecha_hora
HAVING COUNT(*) > 1;

-- ======================================================================
-- PASO 3. LIMPIAR EL DUPLICADO.
-- Se borra la de mayor id_cita, es decir la que llego despues. Y se
-- escribe con una subconsulta en vez de un id fijo, porque el id
-- depende de cuantas veces se haya corrido el script.
--
-- OJO, y esto es lo que mas confunde en esta pregunta: si se salta este
-- paso, el CREATE UNIQUE INDEX del paso 4 FALLA con
--   ERROR: could not create unique index "uq_cita_vet_franja"
--   DETALLE: Key (id_veterinario, fecha_hora)=(1, 2026-10-12 09:00:00) is duplicated.
-- Eso no es un error del ejercicio: es la base diciendo "no puedo
-- prometerte una regla que tus datos actuales ya rompen". Una restriccion
-- se puede crear solo si lo que ya hay la cumple.
-- ======================================================================
DELETE FROM cita
 WHERE id_cita = (
   SELECT MAX(id_cita)
     FROM cita
    WHERE id_veterinario = 1
      AND fecha_hora = TIMESTAMP '2026-10-12 09:00:00'
      AND estado <> 'CANCELADA');

-- ======================================================================
-- PASO 4. APLICAR LA MITIGACION.
-- Indice unico PARCIAL. El WHERE es lo importante: las citas CANCELADAS
-- SI pueden repetir franja, porque una cancelacion libera la hora y esa
-- hora tiene que poder volver a venderse. Un UNIQUE total sobre
-- (id_veterinario, fecha_hora) dejaria una franja quemada para siempre
-- cada vez que alguien cancelara.
--
-- Y aqui esta el mecanismo que responde a la pregunta 4 de este taller:
-- la restriccion no funciona "si las transacciones van una despues de
-- otra". Funciona PRECISAMENTE cuando son simultaneas, porque la segunda
-- que intenta escribir la misma clave se queda ESPERANDO en el B-tree del
-- indice hasta que la primera confirme, y entonces recibe el error. Es un
-- punto de serializacion fisico, no una convencion.
-- ======================================================================
CREATE UNIQUE INDEX uq_cita_vet_franja
    ON cita (id_veterinario, fecha_hora)
 WHERE estado <> 'CANCELADA';

-- ======================================================================
-- PASO 5. PROBAR QUE AHORA LA BASE RECHAZA EL CONFLICTO.
-- El DO con EXCEPTION captura el error para que el script no se detenga.
-- Se captura unique_violation y no OTHERS a proposito: si el INSERT
-- fallara por otra razon -- una FK, un CHECK -- queremos que el script
-- muera y nos lo diga, no anotar "OK rechazada" por el motivo equivocado.
-- ======================================================================
DO $$
BEGIN
  INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, estado)
  VALUES (4, 1, TIMESTAMP '2026-10-12 09:00:00', 'PROGRAMADA');
  INSERT INTO evidencia (paso, resultado)
  VALUES ('con restriccion', 'FALLO: se permitio la doble reserva');
EXCEPTION WHEN unique_violation THEN
  INSERT INTO evidencia (paso, resultado)
  VALUES ('con restriccion', 'OK rechazada: ' || SQLERRM);
END $$;

-- ======================================================================
-- PASO 6. PROBAR QUE LA RESTRICCION NO ES EXCESIVA.
-- La misma franja, pero CANCELADA. TIENE que entrar: el indice parcial no
-- la vigila. Esta prueba es la que distingue una restriccion bien pensada
-- de una que simplemente prohibe cosas: sirve para demostrar que no se
-- rompio el caso legitimo.
-- ======================================================================
DO $$
BEGIN
  INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, estado)
  VALUES (5, 1, TIMESTAMP '2026-10-12 09:00:00', 'CANCELADA');
  INSERT INTO evidencia (paso, resultado)
  VALUES ('cancelada en la misma franja',
          'OK aceptada: el indice parcial no aplica a CANCELADA, la franja liberada se puede reusar');
EXCEPTION WHEN unique_violation THEN
  INSERT INTO evidencia (paso, resultado)
  VALUES ('cancelada en la misma franja',
          'FALLO: la restriccion es excesiva, bloqueo una cita CANCELADA');
END $$;

-- ======================================================================
-- PASO 7. CIERRE.
-- ======================================================================
SELECT paso, resultado FROM evidencia ORDER BY id_evidencia;

-- La MISMA consulta de deteccion del paso 2, sin cambiarle una coma.
-- Ahora tiene que devolver CERO filas.
SELECT id_veterinario,
       fecha_hora,
       COUNT(*) AS citas_en_la_misma_franja
  FROM cita
 WHERE estado <> 'CANCELADA'
 GROUP BY id_veterinario, fecha_hora
HAVING COUNT(*) > 1;

-- Comprobacion de una linea, la que conviene pegar al calificar.
SELECT (SELECT COUNT(*) FROM cita
          WHERE id_veterinario = 1
            AND fecha_hora = TIMESTAMP '2026-10-12 09:00:00'
            AND estado <> 'CANCELADA')                    AS programadas_debe_ser_1,
       (SELECT COUNT(*) FROM cita
          WHERE id_veterinario = 1
            AND fecha_hora = TIMESTAMP '2026-10-12 09:00:00'
            AND estado = 'CANCELADA')                     AS canceladas_debe_ser_1,
       (SELECT COUNT(*) FROM evidencia)                   AS pasos_registrados_debe_ser_3,
       (SELECT COUNT(*) FROM pg_indexes
          WHERE tablename = 'cita'
            AND indexname = 'uq_cita_vet_franja')         AS indice_creado_debe_ser_1;""",
                "salida": """PASO 2 -- la deteccion encuentra el problema: 1 fila

 id_veterinario |     fecha_hora      | citas_en_la_misma_franja
----------------+---------------------+--------------------------
              1 | 2026-10-12 09:00:00 |                        2

Una sola fila, y es la unica: las 10 citas sembradas no repiten ninguna franja, asi
que todo lo que aparece aqui lo produjo el paso 1.

PASO 3 -- DELETE 1

PASO 4 -- CREATE INDEX

Si aqui sale un error en vez de CREATE INDEX, falto el paso 3. El mensaje exacto es:

  ERROR:  could not create unique index "uq_cita_vet_franja"
  DETAIL:  Key (id_veterinario, fecha_hora)=(1, 2026-10-12 09:00:00) is duplicated.

Vale la pena provocarlo a proposito una vez: es la base explicando que una
restriccion solo se puede crear si los datos que ya existen la cumplen.

PASO 5 y PASO 6 -- los dos bloques terminan en DO, sin ERROR

PASO 7 -- evidencia: 3 filas

              paso              |                          resultado
--------------------------------+-------------------------------------------------------------
 sin restriccion                | PROBLEMA: las dos citas se insertaron sin error. La franja
                                | del veterinario 1 el 2026-10-12 09:00 quedo con 2 citas
                                | PROGRAMADA.
 con restriccion                | OK rechazada: duplicate key value violates unique constraint
                                | "uq_cita_vet_franja"
 cancelada en la misma franja    | OK aceptada: el indice parcial no aplica a CANCELADA, la
                                | franja liberada se puede reusar

El texto del paso 1 y del paso 3 lo escribe cada estudiante y no se califica palabra
por palabra. Lo que SI se califica es que el segundo diga "rechazada" y traiga el
SQLERRM, y que el tercero diga "aceptada". Si el tercero dice FALLO, el indice se
creo sin la condicion parcial.

Deteccion final -- 0 filas

(0 rows)

Comprobacion -- 1 fila

 programadas_debe_ser_1 | canceladas_debe_ser_1 | pasos_registrados_debe_ser_3 | indice_creado_debe_ser_1
------------------------+-----------------------+------------------------------+--------------------------
                      1 |                     1 |                            3 |                        1

Los cuatro numeros son 1, 1, 3 y 1, y resumen la pregunta completa: queda UNA cita
programada en la franja disputada -- no dos y no cero --, entro UNA cancelada en la
misma franja -- prueba de que la restriccion no es excesiva --, se registraron los
TRES pasos y el indice existe.

Estado final de la tabla cita: 12 filas. Las 10 sembradas, mas la cita 11
(PROGRAMADA, la que gano la franja) y la cita 14 (CANCELADA). Los ids 12 y 13 no
estan: el 12 lo consumio la cita duplicada que se borro en el paso 3, y el 13 lo
consumio el INSERT rechazado del paso 5. Las secuencias no vuelven atras ni con un
DELETE ni con un ROLLBACK, y por eso en cualquier base real hay huecos en los ids.""",
                "como_calificar": [
                    "**6 pts — el problema demostrado primero.** 3 pts que los dos `INSERT` se "
                    "ejecuten **sin error** y quede registrado en `evidencia`, y 3 pts que la "
                    "consulta de deteccion devuelva **la franja duplicada con `COUNT(*) = 2`**. El "
                    "orden importa y la rubrica lo dice: **se demuestra primero que sin restriccion "
                    "la doble reserva entra**. Quien cree el indice antes de reproducir el problema "
                    "pierde estos 6 pts aunque el resto quede perfecto, porque ya no puede "
                    "demostrar que habia algo que arreglar.",
                    "**7 pts — el indice unico PARCIAL, bien escrito.** 3 pts que sea `UNIQUE` "
                    "sobre `(id_veterinario, fecha_hora)`, y **4 pts la condicion "
                    "`WHERE estado <> 'CANCELADA'`**. Un `UNIQUE` total —sin `WHERE`— vale 3 de 7 y "
                    "hay que explicar en la devolucion que rompe el caso legitimo: dejaria una "
                    "franja quemada para siempre cada vez que alguien cancelara. Se acepta "
                    "`ALTER TABLE ... ADD CONSTRAINT ... UNIQUE` **solo** si se argumenta el "
                    "cambio, porque una `CONSTRAINT UNIQUE` **no** admite condicion parcial y por "
                    "eso el enunciado pide un indice.",
                    "**5 pts — el rechazo capturado.** 3 pts que el segundo `INSERT` sea rechazado "
                    "y 2 pts que quede en `evidencia` como `unique_violation` con el `SQLERRM`. Se "
                    "reconoce como mejor solucion capturar `WHEN unique_violation` en lugar de "
                    "`WHEN OTHERS`: con `OTHERS`, un fallo por otra causa —una FK, un `CHECK`— se "
                    "registraria como «OK rechazada» y la evidencia mentiria.",
                    "**4 pts — la prueba de que la restriccion no es excesiva:** el `INSERT` con "
                    "estado `'CANCELADA'` en la misma franja **si** entra, y queda registrado. Es "
                    "el punto que distingue una restriccion pensada de una que solo prohibe cosas, "
                    "y es la unica prueba de que el `WHERE` del indice hace lo que se dice que "
                    "hace. Quien haya puesto un `UNIQUE` total va a ver esta insercion **fallar** y "
                    "eso mismo le muestra el error.",
                    "**3 pts — el cierre completo:** `SELECT` de `evidencia` con los **3** pasos y "
                    "la consulta de deteccion devolviendo **cero filas**, con la misma consulta del "
                    "paso 2 sin cambiar una coma. 1 pt adicional dentro de estos 3 si el script "
                    "**no aborta** en ningun punto, que es requisito explicito de la rubrica.",
                    "**Se reconoce como sobresaliente, sin puntos extra:** haber provocado a "
                    "proposito el fallo del `CREATE UNIQUE INDEX` sin limpiar antes y haberlo "
                    "dejado documentado en un comentario; explicar por que la restriccion funciona "
                    "**precisamente** cuando las transacciones son simultaneas —la segunda espera "
                    "en el B-tree del indice y recibe el error al confirmar la primera—; o notar "
                    "los huecos en los ids y por que existen.",
                ],
                "errores": [
                    "**Crear el indice antes de reproducir el problema.** Es el error de "
                    "procedimiento mas costoso: los dos `INSERT` del paso 1 fallan, la consulta de "
                    "deteccion no encuentra nada y la pregunta se queda sin su mitad demostrativa. "
                    "El taller no pide implementar la restriccion: pide **demostrar que hacia "
                    "falta** y despues que funciona.",
                    "**El `UNIQUE` total, sin la condicion parcial.** Es el error conceptual "
                    "central. Funciona para el caso de la doble reserva y rompe el caso legitimo: "
                    "con un `UNIQUE` sobre `(id_veterinario, fecha_hora)` a secas, cada cita "
                    "cancelada deja su franja **inutilizable para siempre**. El paso 6 esta puesto "
                    "justo para que este error se vea, no para que se explique.",
                    "**Olvidar el `DELETE` del paso 3** y quedarse trabado en el error del "
                    "`CREATE UNIQUE INDEX`. Suele terminar en un mensaje de «no me deja crear el "
                    "indice». No es un problema de la plataforma: **una restriccion solo se puede "
                    "crear si los datos que ya existen la cumplen**, y esa es una de las cosas "
                    "utiles que se aprenden en esta pregunta.",
                    "**Capturar `WHEN OTHERS` y anotar «OK rechazada» sin mirar el error.** La "
                    "evidencia queda diciendo que la restriccion funciono cuando en realidad pudo "
                    "haber fallado la FK de `id_mascota` o el `CHECK` de `estado`. Capturar "
                    "`unique_violation` no es purismo: es la diferencia entre una prueba y una "
                    "suposicion.",
                    "**Cambiar la consulta de deteccion en el paso 7** —quitarle el "
                    "`WHERE estado <> 'CANCELADA'`, agrupar por otra cosa—. Entonces el «cero "
                    "filas» no prueba nada, porque no es la misma pregunta que devolvio una fila "
                    "en el paso 2. Y si se le quita el filtro de estado, **vuelve a devolver una "
                    "fila** por la cita cancelada del paso 6, que es correcta.",
                    "**Concluir que «la restriccion resuelve la concurrencia» y dejarlo ahi.** "
                    "Resuelve la **integridad**: garantiza que el dato invalido no entre nunca. Lo "
                    "que sigue faltando es el otro lado del contrato: que la aplicacion capture el "
                    "`23505`, no lo muestre en crudo y ofrezca otra franja. Eso se pide en la "
                    "pregunta 5 y conviene senalarlo aqui para que llegue advertido.",
                ],
            },
            {
                "n": 3,
                "titulo": "Doble descuento de stock: bloqueo explicito y actualizacion condicional",
                "tipo": "bd_sql",
                "puntos": 20,
                "sql": """-- ======================================================================
-- PARTE A - ACTUALIZACION CONDICIONAL (sin bloqueo explicito)
-- ======================================================================
CREATE OR REPLACE FUNCTION fn_tomar_stock(p_id_insumo INT, p_cantidad INT)
RETURNS BOOLEAN
LANGUAGE plpgsql
AS $fn$
DECLARE
  v_filas INT;
BEGIN
  -- Comprobar y descontar en UNA sola sentencia. La condicion del stock
  -- va en el WHERE, no en un IF previo: asi no existe ningun instante
  -- entre el "hay stock" y el "lo descuento" en el que otra sesion pueda
  -- meterse. Si no alcanza, el UPDATE no encuentra fila que cumpla la
  -- condicion y afecta 0 filas -- no falla, simplemente no hace nada.
  UPDATE insumo
     SET stock = stock - p_cantidad
   WHERE id_insumo = p_id_insumo
     AND stock >= p_cantidad;

  GET DIAGNOSTICS v_filas = ROW_COUNT;
  RETURN v_filas = 1;
END;
$fn$;

-- Las dos auxiliares pidiendo lo mismo, una detras de la otra. La primera
-- se lleva las 3 unidades; la segunda se queda sin nada, pero el stock no
-- baja de 0 en ningun momento.
SELECT fn_tomar_stock(2, 3) AS primera,
       fn_tomar_stock(2, 3) AS segunda;

SELECT id_insumo, nombre, stock FROM insumo WHERE id_insumo IN (2, 5);

-- ======================================================================
-- PARTE B - BLOQUEO EXPLICITO DE FILA
--
-- Bloque 1: FOR UPDATE. El SELECT toma la fila del insumo 5 y no la
-- suelta hasta que termine la transaccion. Cualquier otra sesion que
-- quiera esa misma fila para escribirla ESPERA.
-- ======================================================================
DO $$
DECLARE
  v_stock INT;
BEGIN
  SELECT stock INTO v_stock
    FROM insumo
   WHERE id_insumo = 5
     FOR UPDATE;                       -- <-- toma el candado de la fila

  IF v_stock >= 4 THEN
    UPDATE insumo SET stock = stock - 4 WHERE id_insumo = 5;
    RAISE NOTICE 'FOR UPDATE: habia % gasas, descuento 4, quedan %', v_stock, v_stock - 4;
  ELSE
    RAISE NOTICE 'FOR UPDATE: solo habia % gasas, no alcanza para 4', v_stock;
  END IF;
END $$;

-- ======================================================================
-- Bloque 2: FOR UPDATE NOWAIT. Identico, salvo el candado: si la fila
-- estuviera tomada por otra sesion, en vez de esperar falla en el acto
-- con lock_not_available (SQLSTATE 55P03). Se captura para poder
-- distinguir en la evidencia "no habia stock" de "no pude ni mirar".
-- ======================================================================
DO $$
DECLARE
  v_stock INT;
BEGIN
  SELECT stock INTO v_stock
    FROM insumo
   WHERE id_insumo = 5
     FOR UPDATE NOWAIT;                -- <-- o muerte

  IF v_stock >= 4 THEN
    UPDATE insumo SET stock = stock - 4 WHERE id_insumo = 5;
    RAISE NOTICE 'NOWAIT: habia % gasas, descuento 4, quedan %', v_stock, v_stock - 4;
  ELSE
    RAISE NOTICE 'NOWAIT: solo habia % gasas, no alcanza para 4', v_stock;
  END IF;
EXCEPTION WHEN lock_not_available THEN
  RAISE NOTICE 'NOWAIT: la fila estaba tomada por otra sesion, no espero. %', SQLERRM;
END $$;

-- ======================================================================
-- Bloque 3 (opcional pero muy ilustrativo): FOR UPDATE SKIP LOCKED.
-- No espera y no falla: SALTA la fila bloqueada, asi que el SELECT
-- devuelve CERO filas y v_stock se queda en NULL. Hay que detectarlo con
-- IF NOT FOUND, porque "IF NULL >= 4" no es falso: es NULL, y el IF no
-- entra por ninguna rama. Es el error silencioso de este mecanismo.
-- ======================================================================
DO $$
DECLARE
  v_stock INT;
BEGIN
  SELECT stock INTO v_stock
    FROM insumo
   WHERE id_insumo = 5
     FOR UPDATE SKIP LOCKED;

  IF NOT FOUND THEN
    RAISE NOTICE 'SKIP LOCKED: la fila estaba tomada, la salte. No hice nada.';
  ELSIF v_stock >= 4 THEN
    UPDATE insumo SET stock = stock - 4 WHERE id_insumo = 5;
    RAISE NOTICE 'SKIP LOCKED: habia % gasas, descuento 4, quedan %', v_stock, v_stock - 4;
  ELSE
    RAISE NOTICE 'SKIP LOCKED: solo habia % gasas, no alcanza para 4', v_stock;
  END IF;
END $$;

SELECT id_insumo, nombre, stock FROM insumo WHERE id_insumo IN (2, 5);

-- ======================================================================
-- LAS TRES VARIANTES DEL CANDADO, EN UNA LINEA CADA UNA
--
--   FOR UPDATE             -> ESPERA a que la otra sesion suelte la fila.
--                             La operacion tarda mas, pero se hace.
--   FOR UPDATE NOWAIT      -> NO espera: falla en el acto con 55P03
--                             (lock_not_available). Sirve cuando es mejor
--                             decirle al usuario "intentalo otra vez" que
--                             dejarlo mirando un reloj de arena.
--   FOR UPDATE SKIP LOCKED -> NO espera y NO falla: devuelve las filas que
--                             puede y SALTA las tomadas. Es el mecanismo
--                             de las colas de trabajo: diez procesos leen
--                             la misma tabla y cada uno se lleva tareas
--                             distintas sin pisarse. Para descontar stock
--                             de un insumo concreto es peligroso, porque
--                             "no pude" se disfraza de "no hay".
--
-- POR QUE AQUI LOS TRES SE COMPORTAN IGUAL
-- Porque en esta sesion unica nadie mas tiene la fila tomada. El candado
-- se concede siempre de inmediato, asi que no hay nada que esperar, nada
-- que fallar y nada que saltar: los tres bloques descuentan igual. Los
-- tres NOTICE que se ven arriba no prueban que los tres mecanismos sean
-- equivalentes; prueban que el escenario que los diferencia NO SE PUEDE
-- MONTAR aqui.
--
-- QUE VERIAMOS EN UN SERVIDOR REAL, con dos sesiones de psql: la sesion A
-- abre BEGIN, hace SELECT ... FOR UPDATE del insumo 5 y NO confirma. Con
-- FOR UPDATE, la sesion B se queda colgada -- visible en pg_locks con
-- granted = false y en pg_stat_activity con wait_event_type = 'Lock' --
-- hasta que A haga COMMIT o ROLLBACK. Con NOWAIT, B falla al instante con
-- 55P03. Con SKIP LOCKED, B recibe 0 filas y sigue de largo.
--
-- CUAL ELIJO PARA VETCARE: el A, la actualizacion condicional, y no es
-- por comodidad. El A resuelve la comprobacion y la escritura en UNA sola
-- sentencia atomica, asi que no hay ventana ni convencion que recordar:
-- funciona aunque manana alguien escriba un procedimiento nuevo. El B
-- deja el candado tomado durante todo lo que la transaccion tarde en
-- pensar, y solo protege a quien se acuerde de pedirlo.
-- El B es NECESARIO -- y ahi si no hay alternativa -- cuando hay que
-- LEER, CALCULAR con datos de varias tablas y DESPUES escribir, porque el
-- calculo no cabe en el WHERE de un UPDATE. En VetCare ese caso existe:
-- el reporte de cierre de caja que suma detalle_factura, compara contra
-- el total de factura y ajusta. Ahi el A no sirve.
-- ======================================================================""",
                "salida": """PARTE A -- 1 fila

 primera | segunda
---------+---------
 t       | f

La primera auxiliar se lleva las 3 unidades; la segunda recibe false. Nadie queda
en negativo y nadie tuvo que coordinarse con nadie.

Un detalle honesto sobre esta prueba: el orden en que PostgreSQL evalua las dos
funciones de la lista de columnas NO esta garantizado por el estandar. En la
practica se evalua de izquierda a derecha y se ve t | f. Si alguna vez se viera
f | t, la conclusion seria exactamente la misma -- el par siempre es {true,
false} -- y lo que no se puede es construir una prueba que dependa de cual de las
dos columnas trae el true.

 id_insumo |        nombre        | stock
-----------+----------------------+-------
         2 | Vacuna triple felina |     0     <-- 3 - 3, exactamente en el limite
         5 | Gasa esteril         |     8     <-- todavia sin tocar

PARTE B -- los NOTICE de los tres bloques

NOTICE:  FOR UPDATE: habia 8 gasas, descuento 4, quedan 4
NOTICE:  NOWAIT: habia 4 gasas, descuento 4, quedan 0
NOTICE:  SKIP LOCKED: solo habia 0 gasas, no alcanza para 4

Los tres bloques obtuvieron el candado de inmediato, porque no habia nadie mas.
El insumo 5 baja 8 -> 4 -> 0, y el tercer bloque ya no alcanza: entra por la rama
del ELSE, que es exactamente la que hay que tener escrita. Si el tercer bloque se
escribio sin la validacion del IF, el UPDATE tampoco habria hecho dano -- el
CHECK (stock >= 0) lo habria abortado --, pero el mensaje habria sido un error en
vez de una explicacion.

Ninguno de los tres NOTICE dice nada sobre esperas ni sobre candados negados, y
eso es el resultado que hay que reportar: el escenario que diferencia a los tres
mecanismos NO se puede montar con una sola sesion.

 id_insumo |        nombre        | stock
-----------+----------------------+-------
         2 | Vacuna triple felina |     0
         5 | Gasa esteril         |     0

Estado final: los dos insumos en 0 y ninguno negativo. Los numeros de la pregunta
son true/false en la parte A, el insumo 2 en 0, y la secuencia 8 -> 4 -> 0 del
insumo 5 en la parte B.

Nota para calificar la parte B: el enunciado pide "otro bloque identico" con NOWAIT
o SKIP LOCKED, asi que dos bloques bastan y el tercero es voluntario. Si el
estudiante entrego solo dos, los NOTICE esperados son 8 -> 4 y 4 -> 0, y el insumo
5 termina igual en 0.""",
                "como_calificar": [
                    "**6 pts — `fn_tomar_stock` con el `UPDATE` condicional y su prueba.** 3 pts la "
                    "funcion: condicion del stock en el `WHERE`, `GET DIAGNOSTICS v_filas = "
                    "ROW_COUNT` y `RETURN v_filas = 1`. 3 pts que la prueba arroje "
                    "**`true` y luego `false`**, el insumo 2 quede en **0** y no haya negativos. Un "
                    "`SELECT stock INTO` seguido de un `IF` vale 0 de los 3 primeros, aunque el "
                    "resultado sea correcto: es el patron que toda la clase esta desmontando.",
                    "**6 pts — los bloques `DO` con bloqueo explicito.** 3 pts el "
                    "`SELECT stock INTO v_stock ... FOR UPDATE` seguido de la validacion y el "
                    "`UPDATE`, con su `RAISE NOTICE`; 3 pts el segundo bloque con **`NOWAIT` o "
                    "`SKIP LOCKED`**. El enunciado pide **uno** de los dos, asi que con dos bloques "
                    "la pregunta esta completa; el tercero se reconoce y no se exige.",
                    "**4 pts — la diferencia entre los tres comportamientos, explicada en "
                    "comentarios `--`.** Aproximadamente 1,3 pts cada uno y se pide precision, no "
                    "extension: `FOR UPDATE` **espera**, `NOWAIT` **falla de inmediato** con "
                    "`lock_not_available` (**55P03**), `SKIP LOCKED` **salta la fila** y devuelve "
                    "cero filas. Confundir `NOWAIT` con `SKIP LOCKED` —los dos «no esperan», pero "
                    "uno grita y el otro calla— es el error mas frecuente y cuesta la mitad de "
                    "estos puntos.",
                    "**4 pts — el comentario de cierre, y aqui esta el nucleo de la clase.** "
                    "1,5 pts reconocer que **en una sola sesion los tres se comportan igual porque "
                    "nadie tiene la fila tomada** —el candado se concede siempre de inmediato—; "
                    "1,5 pts describir que se veria con dos sesiones reales; 1 pt elegir un "
                    "mecanismo con argumento tecnico. La rubrica exige las tres cosas. Un cierre "
                    "que diga «los tres funcionan igual» **sin** explicar que eso es un limite del "
                    "entorno y no una propiedad de los mecanismos vale 0 de los primeros 1,5: es "
                    "justo la conclusion equivocada que el taller quiere evitar.",
                    "**Sobre la eleccion (el 1 pt final):** se acepta **A** o **B** si esta "
                    "argumentado, pero **A** es la respuesta esperada y la pista del enunciado lo "
                    "dice. El argumento completo es que A resuelve comprobacion y escritura en una "
                    "sola sentencia atomica —sin ventana y sin convencion que recordar—, y que B es "
                    "**necesario** cuando hay que leer, calcular con datos de varias tablas y "
                    "despues escribir, porque ese calculo no cabe en el `WHERE` de un `UPDATE`. "
                    "Quien nombre un caso concreto de VetCare para B —el cierre de caja que suma "
                    "`detalle_factura` y ajusta `factura`— tiene la mejor respuesta posible.",
                    "**Se reconoce como sobresaliente, sin puntos extra:** notar que con "
                    "`SKIP LOCKED` el `SELECT ... INTO` no devuelve fila y `v_stock` queda en "
                    "`NULL`, de modo que `IF v_stock >= 4` **no entra por ninguna rama** —hay que "
                    "usar `IF NOT FOUND`—; o senalar que en un descuento de stock `SKIP LOCKED` es "
                    "**peligroso** porque disfraza «no pude» de «no hay», mientras que en una cola "
                    "de trabajos es exactamente el mecanismo correcto.",
                ],
                "errores": [
                    "**Concluir que los tres candados «son equivalentes» porque dieron el mismo "
                    "resultado.** Es la trampa central de la pregunta y la conclusion opuesta a la "
                    "que se pide. Dieron el mismo resultado porque **el escenario que los "
                    "diferencia no se puede montar con una sola sesion**. Lo que hay que reportar "
                    "es la imposibilidad de la prueba, no una equivalencia inexistente.",
                    "**Confundir `NOWAIT` con `SKIP LOCKED`.** Los dos «no esperan» y ahi termina "
                    "el parecido: `NOWAIT` **lanza un error** —`55P03`, que la aplicacion puede "
                    "capturar y traducir— y `SKIP LOCKED` **devuelve cero filas en silencio**. En "
                    "un descuento de stock esa diferencia es grave: con `SKIP LOCKED` y sin "
                    "`IF NOT FOUND`, «no pude tomar la fila» se reporta al usuario como «no hay "
                    "gasas».",
                    "**Volver al patron inseguro dentro de `fn_tomar_stock`:** `SELECT stock INTO` "
                    "y despues un `IF`. En ExamLab da exactamente el mismo `true / false`, asi que "
                    "el estudiante no tiene forma de notarlo por si mismo —y por eso hay que "
                    "senalarlo en la devolucion—. La condicion va en el `WHERE`.",
                    "**Entregar dos versiones del mismo mecanismo** en vez de los dos que se "
                    "piden: por ejemplo, dos `UPDATE` condicionales con distinto nombre, o dos "
                    "bloques `DO` los dos con `FOR UPDATE`. La pregunta compara **A contra B**: "
                    "una sentencia atomica frente a un candado explicito. Sin las dos, no hay nada "
                    "que comparar y el cierre se queda sin sustento.",
                    "**Poner el `FOR UPDATE` en el `UPDATE`** en vez de en el `SELECT`. Un "
                    "`UPDATE` ya bloquea las filas que modifica —eso no hay que pedirlo— y "
                    "`FOR UPDATE` es clausula de `SELECT`: la sintaxis ni compila. Lo que el "
                    "mecanismo B aporta es bloquear la fila **antes** de leerla, para que el valor "
                    "leido siga siendo valido cuando se escriba.",
                    "**Un cierre de una linea que solo elige un mecanismo.** La rubrica pide tres "
                    "cosas en ese comentario y la eleccion es la menos valiosa de las tres. Sin el "
                    "reconocimiento del limite del entorno y sin la descripcion de lo que se veria "
                    "con dos sesiones, la pregunta pierde 3 de sus 20 puntos.",
                ],
            },
            {
                "n": 4,
                "titulo": "Niveles de aislamiento y anomalias en PostgreSQL",
                "tipo": "cerrada_multi",
                "puntos": 10,
                "justificacion": {
                    0: "**Correcta.** `READ COMMITTED` es el nivel por omision y su promesa es "
                       "exactamente esa: **cada sentencia** toma una foto nueva de lo confirmado en "
                       "el instante en que empieza. Dos `SELECT` iguales dentro de la misma "
                       "transaccion pueden dar resultados distintos si entre ellos alguien "
                       "confirmo un cambio, y eso se llama **lectura no repetible**. No es un "
                       "defecto: es el contrato. Quien necesite que las dos lecturas coincidan "
                       "tiene que pedir `REPEATABLE READ`, donde la foto se toma una vez por "
                       "**transaccion** y no por sentencia.",
                    1: "**Correcta, y conviene aprenderse los tres nombres por separado.** "
                       "`READ COMMITTED` **si** evita las **lecturas sucias** —nunca se ve un dato "
                       "no confirmado— pero **no** evita las **lecturas no repetibles** —el mismo "
                       "`SELECT` dos veces con distinto resultado— ni los **fantasmas** —filas "
                       "nuevas que aparecen y cambian el resultado de un predicado—. La doble "
                       "reserva de las preguntas 1 y 2 es justamente un fantasma: la fila que "
                       "rompe la validacion **no existia** cuando cada transaccion la hizo.",
                    2: "**Incorrecta, y es la que mas se marca porque en otros motores seria "
                       "cierta.** PostgreSQL **acepta la sintaxis** "
                       "`SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED` —para no romper "
                       "aplicaciones portadas— pero **la trata como `READ COMMITTED`**. En "
                       "PostgreSQL las lecturas sucias **no son posibles en ningun nivel**, y no "
                       "por una decision de configuracion sino por como funciona MVCC: una "
                       "version de fila no confirmada simplemente **no es visible** para las demas "
                       "transacciones. No hay forma de pedirle que la muestre.",
                    3: "**Correcta, y es la parte que casi siempre se olvida al implementar.** Con "
                       "`SERIALIZABLE`, PostgreSQL vigila los predicados leidos y, si el resultado "
                       "conjunto no equivale a haber ejecutado las transacciones una tras otra, "
                       "**aborta una** con `serialization_failure` (SQLSTATE **40001**) y el "
                       "mensaje «could not serialize access due to read/write dependencies among "
                       "transactions». El error llega normalmente **al confirmar**, no al "
                       "escribir. La consecuencia practica es la que dice la opcion: si la "
                       "aplicacion no sabe **reintentar la transaccion completa**, elegir "
                       "`SERIALIZABLE` no da mas seguridad, da errores intermitentes.",
                    4: "**Incorrecta, y es exactamente al reves: la restriccion funciona sobre todo "
                       "cuando las transacciones son simultaneas.** El propio taller la refuta: en "
                       "la pregunta 2, el `INSERT` posterior fue rechazado con `unique_violation` "
                       "sin que hiciera falta coordinar nada. Y el mecanismo tiene nombre: la "
                       "insercion en un indice unico es un **punto de serializacion fisico**. La "
                       "segunda transaccion que intenta escribir la misma clave **se queda "
                       "esperando** en el B-tree hasta que la primera resuelva, y entonces recibe "
                       "el error —o entra, si la primera hizo `ROLLBACK`—. Esa es la razon por la "
                       "que la restriccion es la mitigacion **mas fuerte** de las tres de la "
                       "pregunta 1: es la unica que no depende de que nadie se acuerde de nada.",
                    5: "**Correcta, y es la unica de las seis que no es sobre el motor sino sobre "
                       "como se escribe la aplicacion.** Mientras una transaccion esta abierta "
                       "sostiene sus candados, y cada milisegundo que los sostiene es ventana para "
                       "un conflicto. Dejar una transaccion abierta esperando que alguien llene un "
                       "formulario convierte segundos de espera humana en minutos de bloqueo para "
                       "todos los demas: el usuario se fue por un cafe y la agenda de la clinica "
                       "esta detenida. La regla practica es leer, calcular y decidir **fuera** de "
                       "la transaccion, y abrirla solo para escribir. Y ojo: **transaccion corta "
                       "no es lo mismo que consulta rapida** —una transaccion de 50 ms que espera "
                       "una confirmacion en pantalla puede retener un candado diez minutos—.",
                },
                "como_calificar": [
                    "**10 pts con las cuatro correctas marcadas y ninguna incorrecta;** puntaje "
                    "proporcional por acierto parcial, tal como dice la rubrica del banco. Las "
                    "correctas son las cuatro que hablan de `READ COMMITTED` como nivel por "
                    "omision, de que evita lecturas sucias pero no no-repetibles ni fantasmas, del "
                    "reintento necesario con `SERIALIZABLE` y de mantener las transacciones cortas.",
                    "**La opcion de `READ UNCOMMITTED` es la que decide la nota de esta pregunta,** "
                    "porque es correcta en otros motores y por eso se marca por analogia. Vale la "
                    "pena responderla siempre con el dato concreto: PostgreSQL **acepta la "
                    "sintaxis** y **la trata como `READ COMMITTED`**; las lecturas sucias no son "
                    "posibles en ningun nivel por como funciona MVCC.",
                    "**La opcion del `UNIQUE` que «solo funciona en secuencial» se refuta con el "
                    "propio taller,** no con teoria: en la pregunta 2 el `INSERT` fue rechazado y "
                    "no hubo que coordinar nada. Si un estudiante la marco, conviene revisarle "
                    "tambien la pregunta 1, porque probablemente ordeno mal las mitigaciones —y "
                    "esa es la comprension que la pregunta 4 esta midiendo—.",
                    "Al devolver la pregunta conviene insistir en el matiz de la opcion del "
                    "reintento: el error de `SERIALIZABLE` llega **al confirmar**, no al escribir. "
                    "Es lo que hace que «poner `SERIALIZABLE`» no sea una decision del motor sino "
                    "de la arquitectura de la aplicacion, y es lo que separa una respuesta "
                    "memorizada de una entendida.",
                ],
                "errores": [
                    "**Marcar la de `READ UNCOMMITTED`.** Transferencia desde SQL Server o desde "
                    "la teoria generica de los cuatro niveles del estandar. En PostgreSQL ese "
                    "nivel existe **solo como sinonimo** de `READ COMMITTED`. Quien lo marque "
                    "suele tambien creer que `READ COMMITTED` «lee mal», y eso arrastra un error "
                    "en la pregunta 1.",
                    "**Marcar la del `UNIQUE` en secuencial.** Es la que revela si se entendio el "
                    "mecanismo o solo se copio la sentencia. Una restriccion unica **serializa "
                    "fisicamente** las inserciones de la misma clave; su valor esta justamente en "
                    "el caso concurrente.",
                    "**Dejar sin marcar la del reintento con `SERIALIZABLE`,** por parecer «un "
                    "detalle de programacion». Es la unica de las seis que dice que hacer cuando "
                    "la base dice no, y es la que separa una mitigacion implementable de una "
                    "teorica.",
                    "**Marcar las seis, o marcar cuatro «por si acaso» sin poder justificarlas.** "
                    "El puntaje es proporcional y penaliza las incorrectas, asi que marcar todo "
                    "baja la nota. Al devolver conviene pedir la justificacion de una sola opcion "
                    "al azar: es la forma rapida de distinguir el acierto del tanteo.",
                ],
            },
            {
                "n": 5,
                "titulo": "Informe de concurrencia del PI y limites de la verificacion",
                "tipo": "abierta",
                "puntos": 20,
                "tabla": {
                    "headers": ["Momento", "T1 (Auxiliar A)", "T2 (Auxiliar B)",
                                "`insumo`: stock del id 2", "Comentario"],
                    "rows": [
                        ["**t0**", "`BEGIN`", "—", "**3**",
                         "Quedan 3 vacunas triple felina. A empieza a facturar la consulta de "
                         "Mishi y necesita 3"],
                        ["**t1**", "—", "`BEGIN`", "**3**",
                         "B empieza a facturar la de Nube y **tambien** necesita 3. Hay para una "
                         "sola de las dos"],
                        ["**t2**", "`SELECT stock` **-> 3**", "—", "**3**",
                         "A lee y decide: «3 >= 3, alcanza». **El `SELECT` no toma ningun "
                         "candado**"],
                        ["**t3**", "—", "`SELECT stock` **-> 3**", "**3**",
                         "**AQUI ESTA LA FALLA.** B lee el **mismo 3** y toma la **misma** "
                         "decision. Las dos leyeron antes de que cualquiera escribiera"],
                        ["**t4**", "`UPDATE stock = 3 - 3`", "—", "**0** (visible solo a T1)",
                         "A descuenta. Correcto: habia 3 y se llevo 3"],
                        ["**t5**", "—", "`UPDATE stock = 3 - 3`",
                         "espera / **-3** segun como se escribio",
                         "B descuenta **sobre el 3 que leyo hace dos pasos**. Con "
                         "`stock = stock - 3` sin condicion, el resultado es **-3**: tres vacunas "
                         "que no existen, ya facturadas"],
                        ["**t6**", "`COMMIT`", "—", "**0** confirmado",
                         "A confirma su factura"],
                        ["**t7**", "—", "`COMMIT`", "**-3** … o error del `CHECK`",
                         "B confirma. Si la tabla tiene `CHECK (stock >= 0)`, **aqui aborta** y el "
                         "dano se queda en un error feo en lugar de un inventario falso. Si no lo "
                         "tiene, la clinica cree tener -3 vacunas y **las dos facturas ya se "
                         "cobraron**"],
                    ],
                },
                "respuesta": (
                    "El instante que hay que senalar es **t2–t5**, igual que en la doble reserva: "
                    "las dos lecturas caen antes de la primera escritura, y las dos decisiones se "
                    "toman sobre una foto que ya envejecio. Los dos escenarios del PI son el mismo "
                    "problema con distinto disfraz —uno sobre una fila que **no existe** todavia, "
                    "otro sobre una fila que **si existe** y cambia de valor—, y por eso llevan "
                    "mitigaciones distintas.\n\n"
                    "**2. Mitigacion elegida para cada escenario, con la sentencia exacta.**\n\n"
                    "*Escenario 1 — doble reserva de franja:* **indice unico parcial**.\n\n"
                    "```sql\n"
                    "CREATE UNIQUE INDEX uq_cita_vet_franja\n"
                    "    ON cita (id_veterinario, fecha_hora)\n"
                    " WHERE estado <> 'CANCELADA';\n"
                    "```\n\n"
                    "Se elige porque es la unica **estructural**: no depende de que el "
                    "procedimiento este bien escrito, ni de que el proximo programador se acuerde "
                    "de nada, ni de un `INSERT` a mano en una migracion. La condicion parcial no "
                    "es un adorno: sin ella, cada cita cancelada dejaria su franja inutilizable "
                    "para siempre. **Descartadas:** `SELECT ... FOR UPDATE` sobre la fila del "
                    "veterinario, porque protege **codigo** y no **datos** —una via de insercion "
                    "que se olvide del candado pasa por encima— y porque serializa todas las "
                    "reservas de ese veterinario; y `SERIALIZABLE`, porque obligaria a que **toda** "
                    "la aplicacion sepa reintentar y en este proyecto no hay ese nivel de control "
                    "sobre el codigo cliente. Ninguna de las dos es mala: son mas fragiles para "
                    "este equipo.\n\n"
                    "*Escenario 2 — doble descuento de stock:* **`UPDATE` condicional**, con el "
                    "`CHECK` como segunda red.\n\n"
                    "```sql\n"
                    "UPDATE insumo\n"
                    "   SET stock = stock - p_cantidad\n"
                    " WHERE id_insumo = p_id_insumo\n"
                    "   AND stock >= p_cantidad;   -- la condicion va aqui, no en un IF previo\n"
                    "GET DIAGNOSTICS v_filas = ROW_COUNT;\n"
                    "-- v_filas = 0 significa: no habia suficiente. Es una respuesta, no un error.\n"
                    "```\n\n"
                    "Se elige porque comprobar y escribir quedan en **una sola sentencia atomica**: "
                    "no hay ventana t2–t5 en la que meterse. **Descartado** "
                    "`SELECT ... FOR UPDATE` **para este caso**, no por debilidad —es correcto— "
                    "sino porque es mas caro y no hace falta: sostiene el candado de la fila "
                    "durante toda la transaccion y solo protege a quien lo pida. **Pero se "
                    "conserva** para el unico caso del PI donde el `UPDATE` condicional no "
                    "alcanza: el **cierre de caja**, que lee `detalle_factura`, suma, compara "
                    "contra el total de `factura` y despues ajusta. Ese calculo no cabe en un "
                    "`WHERE`, asi que ahi el candado explicito es obligatorio. Y el "
                    "`CHECK (stock >= 0)` se queda como red final: garantiza que un negativo no "
                    "pueda existir **aunque** alguien escriba mañana un procedimiento "
                    "equivocado.\n\n"
                    "> **La regla en una linea:** cuando la condicion cabe en el `WHERE`, va en el "
                    "`WHERE`; cuando hay que calcular con varias tablas antes de escribir, hace "
                    "falta el candado explicito; y la restriccion declarativa va **siempre**, "
                    "porque es la unica que sigue ahi cuando el codigo cambie.\n\n"
                    "**3. Contrato con la aplicacion.** Una fila por caso. La restriccion es la "
                    "mitad del trabajo; esta tabla es la otra mitad:\n\n"
                    "| Caso | Que recibe la aplicacion | Que debe hacer | Que **no** debe hacer |\n"
                    "|---|---|---|---|\n"
                    "| **Doble reserva** | `unique_violation`, SQLSTATE **23505**, sobre "
                    "`uq_cita_vet_franja` | Traducir a **«esa franja se acaba de ocupar»**, "
                    "recargar la agenda del dia y ofrecer las tres franjas libres mas cercanas del "
                    "mismo veterinario | **No reintentar el mismo `INSERT`**: volveria a fallar "
                    "siempre. Y no mostrar el mensaje del motor en crudo |\n"
                    "| **Stock insuficiente** | La funcion devuelve **`false`** "
                    "(`ROW_COUNT = 0`). **No hay excepcion:** es una respuesta de negocio | "
                    "Mostrar **«quedan N unidades de X»** con el stock real, y ofrecer sustituto, "
                    "cantidad menor o dejar el item en pedido. La factura no se emite | No tratarlo "
                    "como error tecnico ni escribirlo en el log de fallos: **es un caso normal** y "
                    "va al log de negocio |\n"
                    "| **Error de serializacion** (si algun dia se usa `SERIALIZABLE`) | "
                    "`serialization_failure`, SQLSTATE **40001**, normalmente **al confirmar** | "
                    "**Reintentar la transaccion completa** de forma automatica: hasta 3 intentos "
                    "con espera creciente. Es el unico de los tres casos en que reintentar es la "
                    "respuesta correcta | No mostrarle nada al usuario en los primeros intentos: "
                    "no hizo nada mal. Solo si se agotan, un «intentalo de nuevo» |\n"
                    "| **Candado no disponible** (`FOR UPDATE NOWAIT` en el cierre de caja) | "
                    "`lock_not_available`, SQLSTATE **55P03** | «La caja la esta cerrando otra "
                    "persona en este momento». Reintentable, pero con intervencion humana | No "
                    "reintentar en bucle: se estaria compitiendo con quien ya tiene el candado |\n\n"
                    "**4. Limitacion del entorno, explicitamente.** **No fue posible reproducir "
                    "ningun bloqueo ni ningun interbloqueo real.** ExamLab ejecuta PostgreSQL "
                    "compilado a **WebAssembly dentro del navegador**, con **una unica conexion**. "
                    "No es que sea lento o limitado: es que **no existen dos transacciones "
                    "concurrentes que puedan esperarse**. De ahi salen tres consecuencias "
                    "concretas, y conviene escribirlas sin suavizarlas:\n\n"
                    "- **Las lineas de tiempo T1/T2 de las secciones 1 y 4 son razonamiento, no "
                    "medicion.** Estan construidas sobre como funciona `READ COMMITTED`, no sobre "
                    "una ejecucion observada.\n"
                    "- **Los tres candados —`FOR UPDATE`, `NOWAIT`, `SKIP LOCKED`— se comportaron "
                    "igual,** porque el candado siempre se concedio de inmediato. Eso **no** "
                    "prueba que sean equivalentes: prueba que el escenario que los distingue no se "
                    "puede montar aqui.\n"
                    "- **Y lo mas incomodo: en una sola sesion, el patron inseguro habria dado "
                    "exactamente los mismos resultados que el seguro.** El `true/false` de la "
                    "pregunta 3 sale igual con la condicion en el `WHERE` que con un `IF` previo. "
                    "El entorno **no distingue** el codigo correcto del incorrecto; lo distingue "
                    "el razonamiento.\n\n"
                    "*Lo que si quedo demostrado, y no es poco:* que **sin** restriccion la base "
                    "acepta el dato invalido y **con** ella lo rechaza, sin importar el orden ni "
                    "la velocidad de las transacciones. Esa es la mitigacion estructural, y es "
                    "verificable con una sola sesion precisamente porque no depende de la "
                    "concurrencia.\n\n"
                    "*Como se probaria en un servidor real, con la evidencia que se capturaria:*\n\n"
                    "| Herramienta | Que se haria | Evidencia concreta a capturar |\n"
                    "|---|---|---|\n"
                    "| **Dos sesiones de `psql`** | Sesion A: `BEGIN`, "
                    "`SELECT ... FOR UPDATE` del insumo 2, **sin confirmar**. Sesion B: el mismo "
                    "`SELECT ... FOR UPDATE` | Captura de la sesion B **colgada**, y despues del "
                    "`COMMIT` de A, la marca de tiempo en que se desbloquea. Repetir con `NOWAIT` "
                    "para capturar el **55P03** inmediato |\n"
                    "| **`pg_locks`** | `SELECT locktype, relation::regclass, mode, granted, pid "
                    "FROM pg_locks WHERE NOT granted;` mientras B espera | La fila con "
                    "**`granted = false`**: es la prueba fotografiable de que un bloqueo existe y "
                    "de quien lo tiene |\n"
                    "| **`pg_stat_activity`** | `SELECT pid, state, wait_event_type, wait_event, "
                    "query FROM pg_stat_activity WHERE wait_event_type = 'Lock';` | El "
                    "**`wait_event_type = 'Lock'`** de la sesion B, con la consulta exacta que "
                    "esta esperando |\n"
                    "| **`pgbench`** con script propio | 20 clientes intentando reservar **la "
                    "misma** franja y descontar el mismo insumo, 1.000 transacciones | El conteo "
                    "de `23505` frente al de exitos: tiene que haber **exactamente 1 exito** por "
                    "franja. Y el `stock` final, que debe cuadrar con las unidades facturadas |\n"
                    "| **Interbloqueo provocado** | Dos transacciones que descuentan los insumos "
                    "2 y 5 en **orden inverso** | El mensaje `deadlock detected` en el log con el "
                    "**grafo de espera** que PostgreSQL imprime, y la confirmacion de que el motor "
                    "mata a una de las dos. De ahi sale la regla de descontar **siempre en orden "
                    "de `id_insumo` ascendente** |\n\n"
                    "**5. Riesgo residual.** Dos, y el segundo es el que de verdad preocupa:\n\n"
                    "- **Interbloqueo en facturas con varios insumos, sin mitigar.** Dos facturas "
                    "que toman los insumos 2 y 5 en orden inverso pueden quedarse esperandose. La "
                    "mitigacion es barata —**descontar siempre ordenando por `id_insumo` "
                    "ascendente**, un `ORDER BY` en el bucle de `sp_facturar`— pero **no esta "
                    "implementada ni probada**, porque no se puede probar aqui. *Vigilancia:* "
                    "activar `log_lock_waits = on` con `deadlock_timeout = 1s` y revisar el log "
                    "semanalmente; cualquier `deadlock detected` es un incidente que se investiga, "
                    "no una curiosidad.\n"
                    "- **La franja del veterinario esta protegida; la de la mascota no.** El "
                    "indice unico impide dos citas del mismo **veterinario** a la misma hora, pero "
                    "**nada** impide que la misma **mascota** tenga dos citas simultaneas con dos "
                    "veterinarios distintos. Es un dato invalido igual de real —Firulais no puede "
                    "estar en dos consultorios— y **no** se cerro, porque hay un caso legitimo "
                    "que habria que decidir primero: una urgencia atendida por dos veterinarios a "
                    "la vez. *Vigilancia:* la misma consulta de deteccion de la pregunta 2, "
                    "agrupando por `(id_mascota, fecha_hora)` en lugar de por veterinario, "
                    "ejecutada como reporte semanal. **Si en tres meses devuelve cero filas, se "
                    "convierte en un segundo indice unico parcial;** si devuelve filas legitimas, "
                    "ya se sabe que el caso existe y como tratarlo. Documentar el criterio de "
                    "decision es la mitad del trabajo.\n\n"
                    "**Archivos del PI:** esta seccion en `/informe/10-concurrencia.md`, el indice "
                    "en `/db/05_restricciones_concurrencia.sql`, `fn_tomar_stock` en "
                    "`/db/02_procedimientos.sql`, y las salidas de `evidencia` en "
                    "`/informe/10-evidencia.txt`."
                ),
                "como_calificar": [
                    "**5 pts — el escenario 2 con linea de tiempo de al menos 5 pasos.** 2 pts la "
                    "estructura intercalada y **3 pts que esten marcados los instantes del `SELECT "
                    "stock` de cada una y los de los `UPDATE`**, que es lo que la rubrica exige "
                    "literalmente. Una linea de tiempo donde A lee, descuenta y confirma antes de "
                    "que B lea describe el caso que funciona bien y vale 1 de 5. Se reconoce como "
                    "sobresaliente notar que con el `CHECK (stock >= 0)` la anomalia termina en un "
                    "**error** en vez de en un inventario falso: el dano cambia de forma, no "
                    "desaparece.",
                    "**5 pts — las dos mitigaciones con su sentencia SQL exacta y el descarte "
                    "razonado.** 2,5 pts cada escenario, repartidos en tres: la sentencia completa "
                    "y pegable —no «un `UNIQUE`» sino el `CREATE UNIQUE INDEX ... WHERE ...` "
                    "entero—, el argumento de por que esa, y **el descarte de las alternativas**. "
                    "El descarte es lo que mas falta y es lo que la rubrica nombra: sin el, no hay "
                    "decision, hay una unica opcion considerada.",
                    "**4 pts — la tabla del contrato con la aplicacion, cubriendo los tres tipos "
                    "de error.** Aproximadamente 1,3 pts cada uno: `unique_violation` / **23505**, "
                    "la funcion que devuelve `false`, y `serialization_failure` / **40001**. Lo que "
                    "se califica es **la accion**, no el nombre del error. **El punto que separa "
                    "una respuesta buena de una excelente:** distinguir que el `40001` **si** se "
                    "reintenta automaticamente y el `23505` **no** —porque volveria a fallar "
                    "siempre—. Quien invierta esos dos casos no entendio ninguno de los dos.",
                    "**4 pts — la limitacion del entorno, y es donde se juega la clase.** 2 pts "
                    "reconocer con precision **por que** no se puede: PostgreSQL en WebAssembly con "
                    "**una unica conexion**, asi que no existen dos transacciones que puedan "
                    "esperarse. 2 pts nombrar herramientas reales —dos sesiones de `psql`, "
                    "`pg_locks`, `pg_stat_activity`, `pgbench`— **con la evidencia concreta que se "
                    "capturaria en cada una**. «Usaria `pg_locks`» vale la mitad; «capturaria la "
                    "fila con `granted = false` mientras B espera» vale el punto entero. **Un "
                    "informe que presente la concurrencia como verificada pierde los 4 pts "
                    "completos**, por perfecto que este el resto.",
                    "**2 pts — el riesgo residual con su forma de vigilancia.** 1 pt identificar "
                    "al menos uno de verdad sin mitigar y 1 pt **como se vigila**: una consulta "
                    "concreta, una frecuencia, un parametro del servidor. «Habria que revisarlo» "
                    "vale 0 de ese punto. Los dos residuos mas defendibles son el **interbloqueo** "
                    "en facturas de varios insumos y que **la franja de la mascota no esta "
                    "protegida** —solo la del veterinario—; el segundo es el mejor porque sale de "
                    "leer su propia solucion de la pregunta 2 con ojo critico.",
                    "**Extension:** dos paginas con las tablas. Se califican las cinco secciones "
                    "completas, no la longitud. **Se reconoce como sobresaliente, sin puntos "
                    "extra:** admitir que en una sola sesion el patron **inseguro** habria dado "
                    "los mismos resultados que el seguro, y que por lo tanto el taller no "
                    "distingue el codigo correcto del incorrecto. Es la observacion mas madura "
                    "posible sobre esta clase.",
                ],
                "errores": [
                    "**Presentar la concurrencia como resuelta y verificada.** Aparece como «se "
                    "probo que el `UPDATE` condicional evita el doble descuento». No se probo: "
                    "hubo **una sola sesion**, y la anomalia nunca ocurrio porque no podia "
                    "ocurrir. El patron es correcto y el razonamiento es correcto; la evidencia no "
                    "existe. La seccion 4 esta puesta exactamente para medir esa distincion, y "
                    "confundirla cuesta 4 de los 20 puntos.",
                    "**La linea de tiempo del escenario 2 sin marcar las lecturas.** Es el mismo "
                    "error de la pregunta 1 y se repite porque se copia la estructura sin "
                    "entenderla. Sin los instantes de los dos `SELECT stock` **antes** del primer "
                    "`UPDATE`, la tabla no describe una anomalia: describe una operacion normal.",
                    "**Mitigaciones sin la sentencia SQL.** «Se usa un indice unico» y «se usa un "
                    "`UPDATE` condicional» no son mitigaciones: son titulos. La rubrica pide la "
                    "**sentencia exacta**, y la razon es practica: quien no la escriba completa "
                    "casi siempre olvida el `WHERE estado <> 'CANCELADA'`, que es la parte que "
                    "evita romper el caso legitimo.",
                    "**Invertir el contrato del reintento:** reintentar el `INSERT` que fallo con "
                    "`23505` —volveria a fallar siempre, y en bucle es un ataque contra la propia "
                    "base— y **no** reintentar el `40001`, que es el unico de los tres que **si** "
                    "se debe reintentar de forma automatica. Es el error mas costoso en produccion "
                    "de toda la clase.",
                    "**Tratar el stock insuficiente como un error tecnico.** La funcion devuelve "
                    "`false`, no lanza excepcion, y eso es deliberado: «no hay suficiente» es un "
                    "**caso normal de negocio**. Mandarlo al log de fallos lo esconde entre ruido; "
                    "mostrarle al usuario «error del sistema» en vez de «quedan 2 unidades» "
                    "convierte una decision de mostrador en una llamada a soporte.",
                    "**Nombrar herramientas sin decir que se capturaria con ellas.** Una lista "
                    "—`pg_locks`, `pgbench`, `pg_stat_activity`— sin la evidencia asociada es un "
                    "indice, no un plan. Lo que hace verificable la seccion 4 es la columna de la "
                    "derecha: la fila con `granted = false`, el `wait_event_type = 'Lock'`, el "
                    "conteo de `23505` frente a los exitos.",
                    "**Decir «no hay riesgo residual».** Siempre hay. En este proyecto hay dos "
                    "identificables sin salir del propio taller, y uno de ellos —que la franja de "
                    "la **mascota** no esta protegida, solo la del **veterinario**— se encuentra "
                    "releyendo el indice que se acaba de crear. Un informe sin riesgo residual no "
                    "es un informe seguro: es uno que no se reviso.",
                ],
            },
        ],
        "preguntas_frecuentes": [
            ("¿Por que `READ COMMITTED` no evita la doble reserva, si es el nivel «normal»?",
             "Porque hace exactamente lo que promete y nada mas: cada sentencia ve una foto de lo "
             "**confirmado** en el instante en que esa sentencia empieza. Cuando la Recepcion B "
             "hace su `SELECT COUNT(*)`, la cita de A **todavia no existe** —o existe sin "
             "confirmar, que para B es lo mismo—, asi que B lee **0** y esa lectura es "
             "**correcta**. No hay lectura sucia en ninguna parte. Y la razon de fondo es la que "
             "hay que recordar: **un `SELECT COUNT(*)` no bloquea nada, y no puede**, porque un "
             "bloqueo se pone sobre filas que existen y aqui el conflicto lo produce una fila que "
             "todavia no existe. Por eso la solucion pasa por mover el candado a otro objeto: una "
             "fila que si exista, el B-tree de un indice unico, o un bloqueo de predicado con "
             "`SERIALIZABLE`."),
            ("¿Por que el indice tiene que ser **parcial**? ¿No basta un `UNIQUE` normal?",
             "No, y es el error mas caro de la pregunta 2. Con un `UNIQUE` sobre "
             "`(id_veterinario, fecha_hora)` a secas, la primera vez que alguien cancele una cita "
             "esa franja queda **inutilizable para siempre**: la fila cancelada sigue ahi "
             "ocupando la clave, y nadie podra volver a agendar el lunes a las 9 con Laura. Con "
             "`WHERE estado <> 'CANCELADA'` el indice solo vigila las citas vivas, que es la regla "
             "de negocio real: una franja liberada se puede volver a vender. El paso 6 del "
             "enunciado —insertar una `CANCELADA` en la misma franja y comprobar que **si** "
             "entra— esta puesto justo para que este error se vea en pantalla y no en un "
             "comentario."),
            ("Me dice `could not create unique index ... is duplicated`. ¿Que hice mal?",
             "Nada raro: te saltaste el paso 3, el `DELETE` del duplicado. Y el mensaje es una de "
             "las cosas mas utiles que aprendes hoy: **una restriccion solo se puede crear si los "
             "datos que ya existen la cumplen.** La base no te va a prometer una regla que tu "
             "propia tabla ya rompe. En un proyecto real esto es el orden obligatorio de "
             "cualquier arreglo de integridad: primero encuentras los datos malos con una "
             "consulta de deteccion, despues los limpias o los decides caso por caso, y solo "
             "entonces creas la restriccion. Vale la pena provocar el error a proposito una vez y "
             "dejarlo documentado."),
            ("Si ExamLab tiene una sola sesion, ¿de que sirve el taller?",
             "Sirve para lo que **si** es demostrable con una sesion, que resulta ser lo mas "
             "importante: que sin restriccion la base **acepta** el dato invalido y con ella lo "
             "**rechaza**, sin importar el orden ni la velocidad de las transacciones. Esa es la "
             "mitigacion estructural, y es verificable precisamente porque **no** depende de la "
             "concurrencia. Lo que no se puede montar aqui es el escenario de la espera: ver a "
             "una sesion colgada esperando a otra. Eso no se disimula, se **declara** —es el punto "
             "4 de la pregunta 5 y vale 4 de los 20 puntos—, y se dice con que herramientas se "
             "probaria en un servidor real."),
            ("¿Cual es la diferencia real entre `FOR UPDATE`, `NOWAIT` y `SKIP LOCKED`?",
             "Es lo que cada uno hace **cuando la fila ya esta tomada por otra sesion**, y por eso "
             "aqui los tres se ven iguales: nunca esta tomada. `FOR UPDATE` **espera** a que la "
             "suelten —la operacion tarda, pero se hace—. `FOR UPDATE NOWAIT` **falla en el acto** "
             "con `lock_not_available`, SQLSTATE **55P03**, que la aplicacion puede capturar y "
             "traducir a «lo esta haciendo otra persona, intentalo en un momento». "
             "`FOR UPDATE SKIP LOCKED` **salta** la fila y devuelve cero filas, en silencio: es el "
             "mecanismo de las colas de trabajo, donde diez procesos leen la misma tabla y cada "
             "uno se lleva tareas distintas sin pisarse. Para descontar stock de un insumo "
             "concreto `SKIP LOCKED` es **peligroso**, porque «no pude tomar la fila» se disfraza "
             "de «no hay existencias»."),
            ("Con `SKIP LOCKED`, ¿por que mi `IF v_stock >= 4` no entra por ninguna rama?",
             "Porque si la fila se salta, el `SELECT ... INTO` **no devuelve ninguna fila** y "
             "`v_stock` se queda en `NULL`. Y `NULL >= 4` no es falso: es `NULL`, asi que el `IF` "
             "no entra por el `THEN` **ni** por el `ELSE`. Es el error silencioso de este "
             "mecanismo y hay que detectarlo con `IF NOT FOUND THEN ...` justo despues del "
             "`SELECT`, que es lo unico que distingue «no pude leer la fila» de «la lei y no "
             "alcanza». La leccion general es la misma de siempre con `NULL`: no significa cero, "
             "significa que no se sabe."),
            ("¿Y si simplemente pongo `SERIALIZABLE` y me olvido del problema?",
             "Es la opcion mas limpia en teoria y la mas fragil en la practica, y la razon esta en "
             "**cuando** llega el error. Con `SERIALIZABLE`, PostgreSQL vigila los predicados que "
             "cada transaccion leyo y, si el resultado conjunto no equivale a haberlas ejecutado "
             "una tras otra, **aborta una** con `serialization_failure` (SQLSTATE **40001**) — y "
             "normalmente lo hace **al confirmar**, no al escribir. Eso significa que **toda** la "
             "aplicacion tiene que poder repetir la operacion completa. Un solo camino de codigo "
             "sin reintento convierte la garantia en errores intermitentes para el usuario, que es "
             "peor que no tener la garantia, porque nadie sabe reproducirlos. Es el unico de los "
             "casos de esta clase en que **reintentar es la respuesta correcta**: el `23505` de "
             "una franja ocupada, en cambio, volveria a fallar siempre."),
            ("¿Por que el `UNIQUE` funciona con transacciones simultaneas, si nadie lo coordina?",
             "Porque el propio indice es el punto de coordinacion. Insertar en un indice unico es "
             "un **punto de serializacion fisico**: cuando la segunda transaccion intenta escribir "
             "la misma clave, se encuentra la entrada de la primera —todavia sin confirmar— y **se "
             "queda esperando** ahi. Cuando la primera resuelve, la segunda recibe el "
             "`unique_violation` si aquella confirmo, o entra tranquilamente si hizo `ROLLBACK`. "
             "Nadie tuvo que pedir un candado ni acordar nada: la estructura de datos lo impone. "
             "Es la razon por la que la restriccion es la mitigacion **mas fuerte** de las tres — "
             "es la unica que no depende de que alguien se acuerde de usarla— y es por eso que la "
             "opcion «el `UNIQUE` solo sirve si las transacciones van una despues de otra» de la "
             "pregunta 4 es falsa."),
        ],
        "cierre": [
            "Al terminar, cada estudiante debe tener: la linea de tiempo de la doble reserva con "
            "el intervalo **t2–t5** senalado y las tres mitigaciones con garantia, costo y accion "
            "de la aplicacion; el script de la pregunta 2 con la deteccion encontrando la franja "
            "duplicada, el **indice unico parcial** creado, el rechazo capturado como "
            "`unique_violation` y la `CANCELADA` aceptada —**1, 1, 3 y 1** en la comprobacion "
            "final—; `fn_tomar_stock` dando **`true / false`** con el insumo 2 en 0, y los bloques "
            "`DO` con `FOR UPDATE` y `NOWAIT` o `SKIP LOCKED` llevando el insumo 5 de **8 a 4 a "
            "0**; las cuatro opciones correctas de la pregunta 4; y la seccion de concurrencia en "
            "`/informe/10-concurrencia.md` con el contrato de errores y el limite del entorno "
            "declarado.",
            "Antes de cerrar hay que verificar **tres cosas y una coherencia**, y todas se leen "
            "sin ejecutar nada. Que la deteccion final devuelva **cero filas** y que la de la "
            "franja disputada deje **una** cita `PROGRAMADA` y **una** `CANCELADA` —si la "
            "cancelada no entro, el indice se creo sin la condicion parcial—. Que la pregunta 3 "
            "traiga **dos mecanismos distintos** y no dos versiones del mismo. Que la pregunta 5 "
            "diga en alguna parte que la concurrencia **no se pudo verificar**. Y la coherencia: "
            "quien haya marcado en la pregunta 4 que «el `UNIQUE` solo funciona en secuencial» no "
            "puede haber puesto la restriccion como mitigacion **mas fuerte** en la pregunta 1 — "
            "las dos respuestas se contradicen y conviene senalarlo en la devolucion, porque es "
            "ahi donde se aprende.",
            "Y el mensaje del dia, que hay que dejar por escrito porque no hay clase en vivo para "
            "decirlo: **la conclusion honesta de esta clase es una imposibilidad, no un "
            "resultado**. Con una sola sesion, los tres candados se comportaron igual y el patron "
            "inseguro habria dado exactamente los mismos `true` y `false` que el seguro. El "
            "entorno **no distingue** el codigo correcto del incorrecto; lo distingue el "
            "razonamiento, y por eso el peso de la nota esta en las lineas de tiempo y en el "
            "informe, no en que el SQL corra. Lo que si quedo probado es lo que mas vale en "
            "produccion: que una **restriccion declarativa** cierra el problema sin depender de "
            "nadie, mientras que un candado o un nivel de aislamiento dependen de que todo el "
            "mundo se acuerde. La Clase 11 cambia de tema —vistas, procedimientos y la capa que "
            "la aplicacion consume—, pero se lleva esta regla intacta: **si la regla se puede "
            "declarar, se declara; el codigo explica, la restriccion garantiza**.",
        ],
    },

    11: {
        "titulo": "Solucion del taller · Clase 11 · Avance del PI VetCare DB (hito formal)",
        "resumen": (
            "El ER consolidado con los nombres **reales** del DDL —incluida `audit_cita` sin FK y "
            "las columnas que el borrador de la Clase 1 no tenia—; la bateria de cinco pruebas de "
            "verificacion que arroja **4 de 5** y encuentra un defecto real: las tres facturas "
            "historicas estan descuadradas contra sus detalles, y eso **no es un error del "
            "estudiante sino el hallazgo del hito**; los tres reportes de la demo con sus filas "
            "exactas, la trampa del conteo inflado desmontada con numeros y la advertencia de que "
            "dos de los tres reportes **pasan por suerte** con estos datos; y el checklist de 14 "
            "items con el 79 % declarado, el item mas debil argumentado y los seis gaps con "
            "responsable, fecha anterior al 16 de noviembre y evidencia concreta de cierre."
        ),
        "total": 100,
        "nota_actividad": (
            "**Tres avisos de logistica antes de nada.** Primero: **las Clases 11 y 12 son la "
            "misma sesion doble** del lunes **2026-10-26**, de 18:00 a 20:00, asi que las dos "
            "horas tienen que cubrir el hito formal **y** el tema de integracion de apps "
            "externas. La demo de 3 a 5 minutos por estudiante **no cabe en vivo** para un grupo "
            "completo: hay que decidir de antemano si se graba y se entrega como enlace, o si solo "
            "sale una muestra al aire. Segundo: la sustentacion final del PI es el **2026-11-16** "
            "(sesion 13), asi que **todas** las fechas de cierre de la pregunta 5 tienen que ser "
            "anteriores a esa —y conviene recordar que el 2026-11-09 es el Parcial 3 y ese dia no "
            "se cierra nada—. Tercero y mas importante: **la prueba 5 de la pregunta 2 da `cumple "
            "= FALSE` a proposito.** Las tres facturas que trae la base sembrada estan "
            "descuadradas contra la suma de sus detalles —71.000 contra 41.400, 47.000 contra "
            "16.500 y 60.200 contra 28.600— y ese `FALSE` es la respuesta **correcta**. Hay que "
            "avisarlo al abrir el taller o media clase va a creer que escribio mal la consulta. Y "
            "es la leccion del hito, que conviene decir en voz alta: **una bateria de verificacion "
            "donde todo sale bien no verifico nada.** **El motor es PostgreSQL, no Oracle.** Por "
            "ultimo, las preguntas 4 y 5 son sobre el PI **real** de cada estudiante, asi que lo "
            "que sigue es un **modelo de referencia y no una clave**: se califica que la evidencia "
            "sea rastreable y que la aritmetica cuadre, no que los estados coincidan con estos. En "
            "la firma se acepta unicamente el nombre propio del estudiante; no se piden ni se "
            "guardan datos personales de terceros."
        ),
        "preguntas": [
            {
                "n": 1,
                "titulo": "ER consolidado de VetCare DB (version del hito)",
                "tipo": "diagrama",
                "puntos": 20,
                "respuesta": (
                    "Lo que separa este diagrama del de la Clase 1 no es que tenga una tabla mas: "
                    "es que **se puede verificar contra el DDL linea por linea**. El enunciado pide "
                    "«los nombres exactos que usaste en tu DDL», y ahi esta el criterio de "
                    "calificacion mas objetivo de toda la pregunta —se abre `/db/01_ddl.sql` y se "
                    "compara—. Tres decisiones merecen explicacion:\n\n"
                    "**1. `audit_cita` va sin relacion de FK, y es una decision, no un olvido.** "
                    "Guarda `id_cita` pero **no** lo declara como clave foranea. La razon es de "
                    "negocio: una bitacora tiene que sobrevivir a lo que audita. Si `audit_cita` "
                    "tuviera una FK contra `cita`, borrar una cita obligaria a borrar su historia "
                    "—y entonces el registro de auditoria protegeria a la base de todo menos de "
                    "quien quiera tapar algo—. Es el mismo criterio de cualquier sistema contable: "
                    "la traza no puede depender del dato que traza. Por eso en el diagrama la "
                    "entidad aparece dibujada y **no sale ninguna linea de ella**, y conviene que "
                    "en la demo se diga esa frase completa.\n\n"
                    "**2. La cardinalidad `cita`–`consulta` es la unica discutible, y hay que saber "
                    "defender las dos versiones.** El enunciado pide **1-1** y eso es lo que se "
                    "califica. Pero el DDL real dice "
                    "`id_cita INT NOT NULL UNIQUE REFERENCES cita(id_cita)`, que en rigor "
                    "significa **uno a cero-o-uno** (`||--o|` en Mermaid): cada consulta pertenece "
                    "a exactamente una cita, y cada cita tiene **como maximo** una consulta. Y los "
                    "datos lo confirman: de las 10 citas sembradas, **solo 4** tienen consulta —las "
                    "ATENDIDAS 2, 5, 7 y 10—; las otras seis no la tienen porque estan PROGRAMADAS "
                    "o CANCELADAS. Se acepta `||--||` porque es lo que pide el enunciado, y se "
                    "reconoce `||--o|` como la version mas precisa. Lo mismo pasa con "
                    "`consulta`–`factura`: es 1-N y en los datos la consulta 4 **no** tiene "
                    "factura, asi que en rigor es cero-o-mas (`||--o{`), que es justamente lo que "
                    "escribe el modelo de abajo.\n\n"
                    "**3. Las columnas que el borrador de la Clase 1 no tenia.** Este es el punto "
                    "que distingue un ER copiado de uno consolidado. Aparecieron por el camino y "
                    "tienen que estar: `dueno.ciudad` (con `DEFAULT 'Cali'`), `mascota.fecha_nac`, "
                    "`mascota.activa` —la que sostiene la regla «mascota inactiva no agenda»—, "
                    "`veterinario.activo`, `cita.estado` con su `CHECK` de tres valores, y "
                    "`audit_cita.usuario_bd` con `DEFAULT current_user`, que es la columna que "
                    "convierte una bitacora en una auditoria: sin ella se sabe **que** cambio, pero "
                    "no **quien** lo cambio.\n\n"
                    "> **La frase para la demo:** «este no es el modelo que planeamos, es el "
                    "modelo que quedo». Si el diagrama y el DDL no coinciden, el que esta "
                    "equivocado es el diagrama."
                ),
                "respuesta_mermaid": """erDiagram
    dueno {
        int id_dueno PK
        text nombre
        text telefono
        text email
        text ciudad
    }
    mascota {
        int id_mascota PK
        int id_dueno FK
        text nombre
        text especie
        date fecha_nac
        char activa
    }
    veterinario {
        int id_veterinario PK
        text nombre
        text especialidad
        char activo
    }
    cita {
        int id_cita PK
        int id_mascota FK
        int id_veterinario FK
        timestamp fecha_hora
        text estado
    }
    consulta {
        int id_consulta PK
        int id_cita FK
        text diagnostico
        numeric precio
    }
    insumo {
        int id_insumo PK
        text nombre
        int stock
        numeric precio_unit
    }
    factura {
        int id_factura PK
        int id_consulta FK
        timestamp fecha
        numeric total
    }
    detalle_factura {
        int id_detalle PK
        int id_factura FK
        int id_insumo FK
        int cantidad
        numeric precio_unit
    }
    audit_cita {
        int id_audit PK
        int id_cita
        text accion
        text valor_anterior
        text valor_nuevo
        text usuario_bd
        timestamp fecha_evento
    }
    dueno ||--o{ mascota : tiene
    mascota ||--o{ cita : genera
    veterinario ||--o{ cita : atiende
    cita ||--o| consulta : produce
    consulta ||--o{ factura : facturada_en
    factura ||--o{ detalle_factura : contiene
    insumo ||--o{ detalle_factura : aparece_en""",
                "como_calificar": [
                    "**6 pts — las 9 entidades.** Las 8 del dominio mas `audit_cita`, a 0,67 pts "
                    "cada una. La que mas se olvida es `audit_cita`, porque no estaba en el "
                    "borrador de la Clase 1 y aparecio en la Clase 4. Si falta, se pierden esos "
                    "0,67 **y** los 3 pts del punto siguiente, porque no hay nada que dibujar sin "
                    "FK.",
                    "**5 pts — las 7 relaciones con su cardinalidad,** a 0,71 pts cada una. Se "
                    "aceptan **las dos** versiones de `cita`–`consulta`: `||--||` porque es lo que "
                    "pide el enunciado, y `||--o|` porque es lo que dice el DDL —`UNIQUE` mas seis "
                    "citas sin consulta en los datos—. Quien escriba `||--o|` y lo explique en una "
                    "linea tiene la mejor respuesta; quien escriba `}o--o{` en cualquier relacion "
                    "no entendio la direccion de la FK y ahi si se descuenta.",
                    "**3 pts — `audit_cita` dibujada sin FK y con la razon dicha.** 1 pt que no "
                    "salga ninguna linea de ella y **2 pts la justificacion**: una bitacora tiene "
                    "que sobrevivir a lo que audita, y con una FK contra `cita` borrar una cita "
                    "borraria su historia. Dibujarla sin FK sin poder explicar por que vale 1 de "
                    "3: es la diferencia entre copiar el enunciado y entenderlo.",
                    "**4 pts — al menos dos atributos mas de la PK y las FK, en las 9 entidades, "
                    "con los nombres exactos del DDL.** Este es el punto mas verificable de la "
                    "pregunta: se abre el DDL del estudiante y se compara. Se descuenta por "
                    "`nombre_mascota` cuando el DDL dice `nombre`, por `precio_unitario` cuando "
                    "dice `precio_unit`, o por columnas inventadas que no existen. Se reconoce como "
                    "sobresaliente que aparezcan las que se agregaron por el camino —`ciudad`, "
                    "`fecha_nac`, `activa`, `activo`, `usuario_bd`—, porque son la prueba de que el "
                    "diagrama se actualizo de verdad.",
                    "**2 pts — que renderice sin errores y sea legible al proyectarlo.** Un "
                    "`erDiagram` que no renderiza vale 0 en toda la pregunta, porque el entregable "
                    "**es** la lamina de la demo. Vale la pena decirlo antes del taller: se pega en "
                    "ExamLab, se mira que salga el dibujo, y solo entonces se entrega.",
                    "**Se reconoce como sobresaliente, sin puntos extra:** notar que `usuario_bd` "
                    "con `DEFAULT current_user` es lo que convierte una bitacora en una auditoria "
                    "—sin ella se sabe que cambio pero no quien—; o llegar a la frase de que si el "
                    "diagrama y el DDL no coinciden, el equivocado es el diagrama.",
                ],
                "errores": [
                    "**Entregar el ER de la Clase 1 sin tocarlo.** Es el error dominante y se "
                    "detecta en dos segundos: no trae `audit_cita`. La pregunta pide el modelo "
                    "**tal como quedo despues de las Clases 1 a 8**, no el que se planeo. Un ER "
                    "que no cambio en ocho clases de un proyecto que si cambio esta mintiendo.",
                    "**Dibujarle una FK a `audit_cita`.** Parece mas «correcto» y es peor: acopla "
                    "la bitacora al dato que vigila. Al devolverlo conviene hacer la pregunta "
                    "concreta —«¿que pasa con la auditoria si se borra la cita 1?»—, porque la "
                    "respuesta se contesta sola.",
                    "**Nombres inventados o castellanizados que no estan en el DDL:** "
                    "`precio_unitario` por `precio_unit`, `fecha_nacimiento` por `fecha_nac`, "
                    "`esta_activa` por `activa`. El diagrama deja de servir para lo unico que "
                    "sirve, que es orientarse en el codigo real, y en la demo cualquier pregunta "
                    "del jurado lo descubre.",
                    "**Invertir la direccion de una relacion:** poner `mascota ||--o{ dueno` en "
                    "vez de `dueno ||--o{ mascota`. La FK esta en `mascota`, asi que el lado «uno» "
                    "es `dueno`. La regla practica que conviene repetir: **el lado «muchos» es "
                    "siempre el que carga la FK.**",
                    "**Omitir `detalle_factura` o fundirla con `factura`.** Sin ella no hay "
                    "manera de explicar la pregunta 2 —la prueba 5 compara justamente "
                    "`factura.total` contra la suma de sus detalles— ni la coherencia de la "
                    "facturacion en la demo.",
                    "**Un diagrama con las 9 entidades y 25 atributos cada una, ilegible al "
                    "proyectarlo.** El enunciado pide «al menos dos atributos mas», no todos. La "
                    "lamina se juzga en la demo: si el jurado no puede leer la PK a tres metros, el "
                    "diagrama esta mal aunque el modelo este bien.",
                ],
            },
            {
                "n": 2,
                "titulo": "Bateria de verificacion del avance del PI",
                "tipo": "bd_sql",
                "puntos": 35,
                "sql": """-- ======================================================================
-- PRUEBA 1 - INTEGRIDAD REFERENCIAL cita -> mascota
-- Se intenta insertar una cita con id_mascota = 999, que no existe. La FK
-- tiene que rechazarla. Se captura foreign_key_violation y NO ...WHEN
-- OTHERS: si el INSERT fallara por otra razon -- un CHECK, un NOT NULL --
-- queremos que el script muera y nos lo diga, en vez de anotar "OK" por
-- el motivo equivocado.
--
-- Cada prueba escribe SIEMPRE una fila en checklist_pi: la del camino
-- feliz (FALLO, cumple = FALSE) y la del camino esperado (OK, TRUE). Si
-- solo se escribe la del EXCEPTION, un dia que la regla se rompa la
-- bateria no dira "FALLO": simplemente no dira nada, que es peor.
-- ======================================================================
DO $$
BEGIN
  INSERT INTO cita (id_mascota, id_veterinario, fecha_hora)
  VALUES (999, 1, TIMESTAMP '2026-11-05 10:00:00');

  INSERT INTO checklist_pi (item, resultado, cumple)
  VALUES ('Integridad referencial cita->mascota',
          'FALLO: la base acepto una cita con id_mascota = 999, que no existe',
          FALSE);
EXCEPTION WHEN foreign_key_violation THEN
  INSERT INTO checklist_pi (item, resultado, cumple)
  VALUES ('Integridad referencial cita->mascota',
          'OK rechazada por la FK: ' || SQLERRM,
          TRUE);
END $$;

-- ======================================================================
-- PRUEBA 2 - REGLA DE NEGOCIO: MASCOTA INACTIVA NO AGENDA
-- Rocky (mascota 3) tiene activa = 'N'. sp_agendar_cita valida eso y
-- lanza excepcion. Aqui SI se captura WHEN OTHERS, porque lo que llega es
-- una excepcion de usuario -- el RAISE EXCEPTION que escribimos dentro
-- del procedimiento -- y esa cae en raise_exception (P0001), no en un
-- codigo especifico del motor. Guardamos el SQLERRM completo: sin el, la
-- evidencia dice que "fallo" pero no que fallo POR LA REGLA que se queria
-- probar (pudo fallar porque la franja estaba ocupada, y seria otra cosa).
-- ======================================================================
DO $$
BEGIN
  CALL sp_agendar_cita(3, 2, TIMESTAMP '2026-11-05 09:00:00');

  INSERT INTO checklist_pi (item, resultado, cumple)
  VALUES ('Regla: mascota inactiva no agenda',
          'FALLO: se agendo cita para Rocky (mascota 3), que esta inactiva',
          FALSE);
EXCEPTION WHEN OTHERS THEN
  INSERT INTO checklist_pi (item, resultado, cumple)
  VALUES ('Regla: mascota inactiva no agenda',
          'OK rechazada por el procedimiento: ' || SQLERRM,
          TRUE);
END $$;

-- ======================================================================
-- PRUEBA 3 - REGLA DE NEGOCIO: STOCK NUNCA NEGATIVO
-- El insumo 2 tiene stock 3 y se piden 10. sp_facturar hace el UPDATE
-- condicional, obtiene 0 filas y lanza excepcion.
--
-- El detalle fino de esta prueba: el SELECT del stock va DENTRO del
-- manejador, DESPUES de la excepcion. Eso no es casualidad -- el bloque
-- BEGIN...EXCEPTION abre un savepoint implicito, asi que cuando el
-- manejador arranca la base YA volvio atras todo lo que el procedimiento
-- alcanzo a hacer, incluida la factura que ya habia insertado. El 3 que
-- leemos aqui es el valor restaurado, y por eso es evidencia valida de
-- que el intento fallido no movio nada.
-- ======================================================================
DO $$
DECLARE
  v_stock INT;
BEGIN
  CALL sp_facturar(4, ARRAY[2], ARRAY[10]);

  INSERT INTO checklist_pi (item, resultado, cumple)
  VALUES ('Regla: stock nunca negativo',
          'FALLO: se facturaron 10 unidades del insumo 2, que solo tenia 3',
          FALSE);
EXCEPTION WHEN OTHERS THEN
  SELECT stock INTO v_stock FROM insumo WHERE id_insumo = 2;

  INSERT INTO checklist_pi (item, resultado, cumple)
  VALUES ('Regla: stock nunca negativo',
          'OK rechazada: ' || SQLERRM
            || ' | stock actual del insumo 2 = ' || v_stock,
          TRUE);
END $$;

-- ======================================================================
-- PRUEBA 4 - AUDITORIA ACTIVA
-- La cita 1 esta PROGRAMADA. Al pasarla a CANCELADA, el trigger
-- trg_audit_cita (AFTER UPDATE OF estado, con WHEN de estado distinto)
-- tiene que dejar la fila en audit_cita.
--
-- El veredicto se calcula con la propia consulta, no a mano: el
-- INSERT ... SELECT toma el COUNT(*) de las filas que cumplen las CUATRO
-- condiciones -- la cita, la accion, el valor anterior y el nuevo -- y de
-- ahi sale el booleano. Escribir "TRUE" a mano despues de mirar el
-- resultado no es una prueba: es una opinion.
-- ======================================================================
UPDATE cita SET estado = 'CANCELADA' WHERE id_cita = 1;

INSERT INTO checklist_pi (item, resultado, cumple)
SELECT 'Auditoria de cambios de estado',
       CASE WHEN COUNT(*) = 1
            THEN 'OK auditada: audit_cita registro PROGRAMADA -> CANCELADA'
                 || ' para la cita 1 (' || COUNT(*) || ' fila)'
            ELSE 'FALLO: audit_cita tiene ' || COUNT(*)
                 || ' filas para el cambio de estado de la cita 1, se esperaba 1'
       END,
       COUNT(*) = 1
  FROM audit_cita
 WHERE id_cita = 1
   AND accion = 'CAMBIO_ESTADO'
   AND valor_anterior = 'PROGRAMADA'
   AND valor_nuevo = 'CANCELADA';

-- ======================================================================
-- PRUEBA 5 - COHERENCIA DE FACTURACION
-- Para cada factura: el total guardado, coincide con la suma de
-- cantidad * precio_unit de sus detalles?
--
-- Se usa LEFT JOIN y COALESCE a proposito: una factura SIN detalles tiene
-- que aparecer como descuadrada si su total no es 0, no desaparecer del
-- analisis. Con un INNER JOIN, la factura mas sospechosa de todas -- una
-- con total y sin un solo detalle -- seria justo la que no se revisa.
--
-- AVISO: esta prueba devuelve cumple = FALSE, y esa es la respuesta
-- correcta. Las tres facturas historicas de esta base ESTAN descuadradas.
-- Ver el bloque de cierre.
-- ======================================================================
WITH descuadre AS (
  SELECT f.id_factura,
         f.total                                       AS total_guardado,
         COALESCE(SUM(d.cantidad * d.precio_unit), 0)   AS suma_detalles
    FROM factura f
    LEFT JOIN detalle_factura d ON d.id_factura = f.id_factura
   GROUP BY f.id_factura, f.total
  HAVING f.total <> COALESCE(SUM(d.cantidad * d.precio_unit), 0)
)
INSERT INTO checklist_pi (item, resultado, cumple)
SELECT 'Total de factura coincide con sus detalles',
       CASE WHEN NOT EXISTS (SELECT 1 FROM descuadre)
            THEN 'OK: ninguna factura descuadrada'
            ELSE 'FALLO: ' || (SELECT string_agg('factura ' || id_factura
                                                 || ' guarda ' || total_guardado
                                                 || ' y sus detalles suman ' || suma_detalles,
                                                 '; ' ORDER BY id_factura)
                                 FROM descuadre)
       END,
       NOT EXISTS (SELECT 1 FROM descuadre);

-- Consulta de diagnostico: la que se proyecta cuando el jurado pregunte
-- "y por que ese FALSE?". No arregla nada, muestra el tamano del problema
-- factura por factura.
SELECT f.id_factura,
       f.total                                                AS total_guardado,
       COALESCE(SUM(d.cantidad * d.precio_unit), 0)            AS suma_detalles,
       f.total - COALESCE(SUM(d.cantidad * d.precio_unit), 0)  AS diferencia,
       COUNT(d.id_detalle)                                     AS lineas_de_detalle
  FROM factura f
  LEFT JOIN detalle_factura d ON d.id_factura = f.id_factura
 GROUP BY f.id_factura, f.total
 ORDER BY f.id_factura;

-- ======================================================================
-- CIERRE DE LA BATERIA
-- ======================================================================
SELECT id_item, item, cumple, resultado FROM checklist_pi ORDER BY id_item;

-- Resumen de una linea, el que se proyecta en la demo.
SELECT COUNT(*) FILTER (WHERE cumple)     AS pruebas_ok,
       COUNT(*) FILTER (WHERE NOT cumple) AS pruebas_falladas,
       COUNT(*)                           AS total_pruebas
  FROM checklist_pi;

-- ======================================================================
-- QUE SIGNIFICA EL 4 DE 5
--
-- Las cuatro primeras pruebas confirman que las reglas escritas en las
-- Clases 1 a 8 SIRVEN: la FK rechaza, el procedimiento valida, el stock
-- no baja de cero y el trigger deja rastro. La quinta encontro algo que
-- nadie habia mirado: las tres facturas historicas no cuadran con sus
-- detalles. Y no es un error de la consulta -- se comprueba a mano:
--   factura 1: 31.000 + 900 + 9.500       = 41.400, pero guarda 71.000
--   factura 2: 9.500 + 7.000              = 16.500, pero guarda 47.000
--   factura 3: 22.000 + 4.800 + 1.800     = 28.600, pero guarda 60.200
--
-- Lo importante es DONDE esta el problema y donde NO esta: sp_facturar
-- calcula bien -- la factura que crea en la Clase 8 cuadra al centavo --,
-- asi que el descuadre esta en los datos cargados ANTES de que el
-- procedimiento existiera. Es la historia de cualquier migracion real: el
-- codigo nuevo es correcto y los datos viejos no lo cumplen.
--
-- Y LO QUE NO SE HACE AQUI: no se "arregla" con un
--   UPDATE factura SET total = (SELECT SUM(...) FROM detalle_factura ...)
-- Por dos razones. Primera, esos totales pueden ser lo que el cliente
-- REALMENTE pago -- quiza incluyen el precio de la consulta o un cargo
-- que nunca se detallo --, y sobrescribirlos con la suma de los insumos
-- seria falsear la contabilidad para que cuadre el reporte. Segunda, en
-- medio de una demo se estaria borrando la evidencia del unico hallazgo
-- del hito. Se documenta, se decide con quien conozca el negocio, y se
-- convierte en el gap numero 1 de la pregunta 5. Un checklist con 5 de 5
-- no habria descubierto nada.
-- ======================================================================""",
                "salida": """checklist_pi -- 5 filas

 id_item |                    item                    | cumple |                     resultado
---------+--------------------------------------------+--------+---------------------------------------------------
       1 | Integridad referencial cita->mascota       | t      | OK rechazada por la FK: insert or update on table
         |                                            |        | "cita" violates foreign key constraint
         |                                            |        | "cita_id_mascota_fkey"
       2 | Regla: mascota inactiva no agenda          | t      | OK rechazada por el procedimiento: ERROR: la
         |                                            |        | mascota 3 esta inactiva; no se agenda cita
       3 | Regla: stock nunca negativo                | t      | OK rechazada: ERROR: stock insuficiente del
         |                                            |        | insumo 2 (se pidieron 10) | stock actual del
         |                                            |        | insumo 2 = 3
       4 | Auditoria de cambios de estado             | t      | OK auditada: audit_cita registro PROGRAMADA ->
         |                                            |        | CANCELADA para la cita 1 (1 fila)
       5 | Total de factura coincide con sus detalles | f      | FALLO: factura 1 guarda 71000.00 y sus detalles
         |                                            |        | suman 41400.00; factura 2 guarda 47000.00 y sus
         |                                            |        | detalles suman 16500.00; factura 3 guarda
         |                                            |        | 60200.00 y sus detalles suman 28600.00

Dos detalles de las filas 2 y 3 que sorprenden y no son errores. El texto dice
"ERROR: ERROR:" cuando se lee entero, porque el mensaje que el procedimiento
escribio con RAISE EXCEPTION ya empieza con "ERROR:" y SQLERRM devuelve ese
texto tal cual. Y el "stock actual del insumo 2 = 3" se lee DESPUES de la
excepcion, cuando la base ya volvio atras: por eso vale como evidencia.

Consulta de diagnostico -- 3 filas

 id_factura | total_guardado | suma_detalles | diferencia | lineas_de_detalle
------------+----------------+---------------+------------+-------------------
          1 |       71000.00 |      41400.00 |   29600.00 |                 3
          2 |       47000.00 |      16500.00 |   30500.00 |                 2
          3 |       60200.00 |      28600.00 |   31600.00 |                 3

Las tres estan descuadradas y las tres tienen sus lineas de detalle, asi que no
es una factura huerfana: son totales cargados sin conciliar. Ninguna diferencia
coincide con el precio de su consulta -- 40.000, 38.000 y 55.000 --, asi que
tampoco es que el total incluya la consulta. Es un dato historico que nunca se
verifico, y hoy se verifico.

Resumen -- 1 fila

 pruebas_ok | pruebas_falladas | total_pruebas
------------+------------------+---------------
          4 |                1 |             5

El numero de la clase es 4 de 5. Un 5 de 5 aqui significaria que la prueba 5 se
escribio de forma que no puede fallar.

Estado de la base al terminar, para el que califique de cerca:

- cita: 10 filas, con la cita 1 ya en CANCELADA. El INSERT rechazado de la
  prueba 1 no dejo fila, pero SI consumio el id 11 de la secuencia: las
  secuencias no vuelven atras.
- audit_cita: 1 fila (id_audit 1), con valor_anterior = 'PROGRAMADA' y
  valor_nuevo = 'CANCELADA'.
- factura: 3 filas. La prueba 3 alcanzo a insertar la factura 4 antes de fallar
  en el stock, y el savepoint implicito la deshizo -- pero el id 4 de la
  secuencia quedo consumido y la proxima factura sera la 5.
- insumo 2: stock 3, intacto. Es el numero que sostiene la prueba 3.
- detalle_factura: 8 filas, sin cambios.
- checklist_pi: 5 filas.""",
                "como_calificar": [
                    "**6 pts — prueba 1, integridad referencial.** 3 pts que el `INSERT` con "
                    "`id_mascota = 999` sea rechazado y capturado, y 3 pts que quede **una** fila "
                    "en `checklist_pi` con el item exacto `'Integridad referencial cita->mascota'` "
                    "y `cumple = TRUE`. Se reconoce como mejor solucion capturar "
                    "`WHEN foreign_key_violation` en vez de `WHEN OTHERS`: con `OTHERS`, un fallo "
                    "por un `CHECK` o un `NOT NULL` se registraria como «OK rechazada» por el "
                    "motivo equivocado.",
                    "**6 pts — prueba 2, mascota inactiva.** 3 pts que el `CALL sp_agendar_cita(3, "
                    "2, ...)` lance excepcion y quede capturado, y **3 pts que el `SQLERRM` este "
                    "guardado en `resultado`**, que es lo que el enunciado pide literalmente. Sin "
                    "el `SQLERRM`, la evidencia dice que «fallo» pero no que fallo **por la regla** "
                    "que se queria probar —podria haber fallado porque la franja estaba ocupada, y "
                    "seria otra prueba—. Aqui `WHEN OTHERS` **si** es correcto: un "
                    "`RAISE EXCEPTION` de usuario cae en `raise_exception` (P0001), no en un codigo "
                    "especifico del motor.",
                    "**8 pts — prueba 3, stock nunca negativo.** 3 pts el `CALL sp_facturar(4, "
                    "ARRAY[2], ARRAY[10])` capturado, 2 pts el `SQLERRM`, y **3 pts la evidencia "
                    "del stock: el `resultado` tiene que traer el `3`**. Es el requisito explicito "
                    "de la rubrica y el que mas se olvida. Se reconoce como sobresaliente explicar "
                    "**por que** ese 3 es evidencia valida: el manejador corre despues del "
                    "`ROLLBACK` al savepoint implicito, asi que el valor leido es el restaurado.",
                    "**7 pts — prueba 4, auditoria.** 2 pts el `UPDATE` de la cita 1 a "
                    "`'CANCELADA'`, 3 pts la verificacion de que `audit_cita` tiene la fila con "
                    "`valor_anterior = 'PROGRAMADA'` y `valor_nuevo = 'CANCELADA'`, y 2 pts que el "
                    "`cumple` **se calcule con la consulta** y no se escriba a mano. Un `TRUE` "
                    "literal despues de mirar el resultado no es una prueba: si manana el trigger "
                    "se cae, la bateria seguira diciendo que todo esta bien.",
                    "**8 pts — prueba 5, coherencia de facturacion, y aqui esta el corazon del "
                    "hito.** 3 pts que la consulta compare `factura.total` contra "
                    "`SUM(cantidad * precio_unit)` agrupando por factura; 2 pts el `NOT EXISTS` (o "
                    "equivalente) que produce el booleano; y **3 pts que se registre "
                    "`cumple = FALSE` y se nombren las tres facturas descuadradas**. "
                    "**`FALSE` es la respuesta correcta y hay que decirlo asi en la devolucion.** "
                    "Quien reporte `TRUE` escribio una consulta que no puede fallar —casi siempre "
                    "un `INNER JOIN` mal agrupado o un `HAVING` invertido— y pierde los 8 pts, no "
                    "por el veredicto sino porque su bateria no verifica nada. Se reconoce como "
                    "sobresaliente el `LEFT JOIN` con `COALESCE`, que deja visible la factura mas "
                    "sospechosa de todas: una con total y sin un solo detalle.",
                    "**Los 35 pts requieren ademas que el script no aborte en ningun punto** y que "
                    "el `SELECT` final muestre las **5** filas, que es requisito literal de la "
                    "rubrica. Se reconoce como sobresaliente, sin puntos extra: haber escrito "
                    "**las dos** filas de `checklist_pi` en cada prueba —la del camino feliz y la "
                    "del esperado—, de modo que el dia que una regla se rompa la bateria diga "
                    "«FALLO» en vez de quedarse callada; y no haber «arreglado» el descuadre con un "
                    "`UPDATE factura SET total = ...` en medio de la demo.",
                ],
                "errores": [
                    "**Reportar `cumple = TRUE` en la prueba 5.** Es el error mas revelador de "
                    "toda la clase. Las tres facturas **estan** descuadradas —41.400 contra 71.000, "
                    "16.500 contra 47.000, 28.600 contra 60.200— y se comprueba con una suma a "
                    "mano. Un `TRUE` significa que la consulta esta escrita de forma que no puede "
                    "fallar, y una prueba que no puede fallar no es una prueba. Al devolverlo "
                    "conviene pedir la resta de la factura 1 en voz alta.",
                    "**«Arreglar» el descuadre con un `UPDATE factura SET total = (SELECT "
                    "SUM(...))`.** Aparece con buena intencion y es la decision mas peligrosa del "
                    "taller: esos totales pueden ser lo que el cliente **realmente pago**, asi que "
                    "sobrescribirlos para que el reporte cuadre es falsear la contabilidad. Y "
                    "encima borra la evidencia del unico hallazgo del hito. Se documenta, se "
                    "decide con quien conozca el negocio, y se convierte en un gap.",
                    "**Escribir el `cumple` a mano en vez de calcularlo.** Se mira el resultado, se "
                    "escribe `TRUE`, y la bateria queda inservible: el proximo semestre el trigger "
                    "se cae y el checklist sigue diciendo que todo esta bien. El veredicto tiene "
                    "que salir de la consulta —un `COUNT(*) = 1`, un `NOT EXISTS`—, siempre.",
                    "**Olvidar el stock en el `resultado` de la prueba 3.** Sin el `3`, la prueba "
                    "demuestra que el procedimiento fallo, pero **no** que el intento fallido dejo "
                    "la base intacta, que es la mitad interesante. Es el requisito explicito de la "
                    "rubrica y cuesta 3 de los 8 puntos de esa prueba.",
                    "**Capturar `WHEN OTHERS` en la prueba 1.** Ahi si importa: se quiere probar "
                    "que **la FK** rechaza, no que «algo» fallo. Con `OTHERS`, un `NOT NULL` "
                    "olvidado en el `INSERT` se registraria como integridad referencial "
                    "funcionando. Al reves, en las pruebas 2 y 3 `OTHERS` es lo correcto porque lo "
                    "que llega es una excepcion de usuario.",
                    "**Que el script aborte a mitad de camino** —normalmente por escribir los "
                    "`CALL` sin bloque `DO`, o por un `$$` mal cerrado—. Entonces `checklist_pi` "
                    "queda con dos o tres filas y la demo se cae en vivo. Conviene correr la "
                    "bateria completa una vez antes de presentarla y contar las filas: tienen que "
                    "ser 5.",
                    "**Registrar solo la fila del `EXCEPTION` y omitir la del camino feliz.** "
                    "Funciona hoy y falla en silencio manana: si la regla se rompe, el `INSERT` no "
                    "lanza excepcion, el manejador no corre y en `checklist_pi` **no aparece "
                    "nada**. Una prueba que desaparece cuando falla es peor que ninguna, porque el "
                    "conteo final dice «4 de 4».",
                ],
            },
            {
                "n": 3,
                "titulo": "Los tres reportes de la demo",
                "tipo": "bd_sql",
                "puntos": 20,
                "sql": """-- ======================================================================
-- R1 - AGENDA OPERATIVA
-- Citas no canceladas de septiembre de 2026, con todo lo que la
-- recepcionista necesita para llamar: mascota, especie, dueno, telefono y
-- veterinario.
--
-- El filtro de fecha va por RANGO y no con EXTRACT(MONTH FROM ...) = 9.
-- Dos razones: la version con funcion sobre la columna NO es sargable --
-- ningun indice sobre fecha_hora se puede usar -- y ademas confundiria
-- septiembre de 2026 con septiembre de cualquier otro ano. El limite
-- superior es "< 2026-10-01", nunca "<= 2026-09-30": con un TIMESTAMP,
-- ese <= perderia todo lo que pase entre las 00:00:01 y las 23:59:59 del
-- 30 de septiembre.
-- ======================================================================
SELECT c.fecha_hora,
       m.nombre     AS mascota,
       m.especie,
       d.nombre     AS dueno,
       d.telefono,
       v.nombre     AS veterinario,
       c.estado
  FROM cita c
  JOIN mascota m     ON m.id_mascota     = c.id_mascota
  JOIN dueno d       ON d.id_dueno       = m.id_dueno
  JOIN veterinario v ON v.id_veterinario = c.id_veterinario
 WHERE c.estado <> 'CANCELADA'
   AND c.fecha_hora >= TIMESTAMP '2026-09-01 00:00:00'
   AND c.fecha_hora <  TIMESTAMP '2026-10-01 00:00:00'
 ORDER BY c.fecha_hora, m.nombre;

-- ======================================================================
-- R2 - HISTORIA CLINICA Y FACTURACION POR DUENO
-- Una fila por dueno, incluidos los que no tienen actividad.
--
-- Cuatro subconsultas escalares en vez de una cadena de LEFT JOIN. Es la
-- forma que NO se puede inflar: cada subconsulta cuenta sobre su propia
-- tabla y no hay producto cartesiano posible. La cadena
--   dueno -> mascota -> cita -> consulta -> factura
-- multiplica filas, y COUNT(m.id_mascota) empieza a contar la misma
-- mascota una vez por cada cita que tenga. Con COUNT(DISTINCT ...) se
-- arregla, pero hay que acordarse en las cuatro columnas y una sola que
-- se olvide da un numero falso con cara de correcto.
--
-- Los COUNT no necesitan COALESCE: un COUNT sin filas devuelve 0. El SUM
-- si, porque un SUM sin filas devuelve NULL, y "0" y "no se sabe" no son
-- lo mismo en un reporte de facturacion.
-- ======================================================================
SELECT d.id_dueno,
       d.nombre,
       (SELECT COUNT(*)
          FROM mascota m
         WHERE m.id_dueno = d.id_dueno)                      AS mascotas,
       (SELECT COUNT(*)
          FROM cita c
          JOIN mascota m ON m.id_mascota = c.id_mascota
         WHERE m.id_dueno = d.id_dueno)                      AS citas,
       (SELECT COUNT(*)
          FROM consulta co
          JOIN cita c    ON c.id_cita    = co.id_cita
          JOIN mascota m ON m.id_mascota = c.id_mascota
         WHERE m.id_dueno = d.id_dueno)                      AS consultas,
       (SELECT COALESCE(SUM(f.total), 0)
          FROM factura f
          JOIN consulta co ON co.id_consulta = f.id_consulta
          JOIN cita c      ON c.id_cita      = co.id_cita
          JOIN mascota m   ON m.id_mascota   = c.id_mascota
         WHERE m.id_dueno = d.id_dueno)                      AS total_facturado
  FROM dueno d
 ORDER BY total_facturado DESC, d.id_dueno;
-- El segundo criterio del ORDER BY no es adorno: cuatro duenos empatan en
-- 0.00 y sin desempate su orden lo decide el motor. Un reporte que sale
-- en distinto orden cada vez que se proyecta no es un reporte.

-- ======================================================================
-- R3 - INSUMOS EN RIESGO
-- Stock actual, unidades consumidas segun detalle_factura y semaforo.
--
-- LEFT JOIN para que un insumo que nunca se vendio aparezca con 0 y no
-- desaparezca -- justo el que hay que revisar antes de comprar mas.
--
-- El orden de los WHEN del CASE hace el trabajo: cuando se evalua el
-- segundo, ya se sabe que stock >= 5, asi que "stock <= 10" significa
-- "entre 5 y 10" sin tener que escribirlo. El 10 queda en BAJO, que es la
-- lectura inclusiva de "entre 5 y 10" del enunciado.
-- ======================================================================
SELECT i.id_insumo,
       i.nombre,
       i.stock,
       COALESCE(SUM(d.cantidad), 0)      AS unidades_consumidas,
       CASE WHEN i.stock <  5  THEN 'CRITICO'
            WHEN i.stock <= 10 THEN 'BAJO'
            ELSE                    'OK'
       END                               AS alerta
  FROM insumo i
  LEFT JOIN detalle_factura d ON d.id_insumo = i.id_insumo
 GROUP BY i.id_insumo, i.nombre, i.stock
 ORDER BY CASE WHEN i.stock <  5  THEN 1
               WHEN i.stock <= 10 THEN 2
               ELSE                    3
          END,
          i.stock,
          i.id_insumo;

-- ======================================================================
-- QUE DECISION DEL NEGOCIO HABILITA CADA REPORTE
--
-- R1 -> Es la hoja de ruta del dia: a quien llamar y a que hora. Decide a
--       quien se le confirma la cita el dia anterior y, si una veterinaria
--       falta, a que duenos hay que telefonear para reagendar -- por eso
--       el telefono va en el reporte y no en otra consulta.
--
-- R2 -> Decide a quien se le ofrece el plan de vacunacion anual y a quien
--       se le hace seguimiento. Las dos puntas importan: Ana Gomez
--       concentra 131.200 de los 178.200 facturados, asi que perderla es
--       perder tres cuartas partes del ingreso conocido; y los cuatro
--       duenos en 0.00 son la lista de reactivacion -- entre ellos Marcela
--       Diaz, que tiene 3 citas y ninguna factura, que es una pregunta
--       para el mostrador, no para la base.
--
-- R3 -> Decide la orden de compra de esta semana. La Vacuna triple felina
--       esta en CRITICO con 3 unidades y es el insumo mas caro de los
--       consumidos (31.000), asi que quedarse sin ella cancela consultas
--       facturables. La Gasa esteril esta en BAJO con 8 y ya se
--       consumieron 4: es la que sigue.
-- ======================================================================""",
                "salida": """R1 - Agenda operativa -- 9 filas

     fecha_hora      | mascota  | especie |    dueno      |  telefono  |  veterinario   |   estado
---------------------+----------+---------+---------------+------------+----------------+------------
 2026-09-01 08:00:00 | Firulais | Canino  | Ana Gomez     | 3001112233 | Laura Restrepo | PROGRAMADA
 2026-09-01 09:00:00 | Luna     | Felino  | Ana Gomez     | 3001112233 | Laura Restrepo | ATENDIDA
 2026-09-01 10:00:00 | Mishi    | Felino  | Marcela Diaz  | 3027778899 | Diego Moreno   | PROGRAMADA
 2026-09-02 11:00:00 | Nube     | Felino  | Jorge Pineda  | 3105551212 | Diego Moreno   | ATENDIDA
 2026-09-03 07:45:00 | Toby     | Canino  | Luisa Cardona | 3123334455 | Ivan Ortiz     | PROGRAMADA
 2026-09-05 15:00:00 | Firulais | Canino  | Ana Gomez     | 3001112233 | Laura Restrepo | ATENDIDA
 2026-09-08 16:00:00 | Luna     | Felino  | Ana Gomez     | 3001112233 | Paula Salazar  | PROGRAMADA
 2026-09-10 08:00:00 | Mishi    | Felino  | Marcela Diaz  | 3027778899 | Ivan Ortiz     | PROGRAMADA
 2026-09-10 09:00:00 | Nube     | Felino  | Jorge Pineda  | 3105551212 | Laura Restrepo | ATENDIDA

9 de las 10 citas: la unica que se cae es la del 2026-09-02 08:30 de Bobby, que
esta CANCELADA. Ese 9 es el numero que hay que ver.

Honestidad sobre el filtro de fecha: las 10 citas de esta base estan en
septiembre de 2026, asi que el rango NO excluye ninguna fila. El resultado seria
identico con un filtro mal escrito o incluso sin filtro de fecha. Eso significa
que R1 se califica leyendo el SQL, no contando filas -- y que quien use
EXTRACT(MONTH FROM c.fecha_hora) = 9 va a ver las mismas 9 filas y a creer que
esta bien.

R2 - Historia clinica y facturacion por dueno -- 6 filas

 id_dueno |     nombre     | mascotas | citas | consultas | total_facturado
----------+----------------+----------+-------+-----------+-----------------
        1 | Ana Gomez      |        2 |     4 |         2 |       131200.00
        4 | Jorge Pineda   |        1 |     2 |         2 |        47000.00
        2 | Carlos Ruiz    |        1 |     0 |         0 |            0.00
        3 | Marcela Diaz   |        2 |     3 |         0 |            0.00
        5 | Luisa Cardona  |        1 |     1 |         0 |            0.00
        6 | Andres Vallejo |        1 |     0 |         0 |            0.00

Los seis duenos aparecen, incluidos los cuatro sin facturacion: eso es lo que
prueba el LEFT JOIN o, aqui, las subconsultas escalares. Las columnas cuadran
contra el total: 2+1+2+1+1+1 = 8 mascotas, 4+0+3+2+1+0 = 10 citas,
2+0+0+2+0+0 = 4 consultas y 131200 + 47000 = 178200 = 71000 + 47000 + 60200.
Los cuatro subtotales son la forma rapida de calificar la pregunta.

Y asi se ve el conteo inflado, para el que uso la cadena de LEFT JOIN sin
DISTINCT (solo las filas que cambian):

 id_dueno |     nombre     | mascotas | citas | consultas | total_facturado
----------+----------------+----------+-------+-----------+-----------------
        1 | Ana Gomez      |        4 |     4 |         2 |       131200.00
        3 | Marcela Diaz   |        3 |     3 |         0 |            0.00
        4 | Jorge Pineda   |        2 |     2 |         2 |        47000.00

Ana Gomez pasa de 2 mascotas a 4 y Marcela Diaz de 2 a 3: la cadena repite la
mascota una vez por cada cita. Ojo con lo que NO se infla: las citas, las
consultas y el total facturado salen correctos, porque cita->consulta es 1 a 1 y
cada factura aparece una sola vez. Es decir, la trampa se delata en UNA sola
columna con estos datos -- y si alguien pone COUNT(DISTINCT m.id_mascota) y
olvida el resto, no habria diferencia visible. La columna de mascotas es el
punto donde hay que mirar.

R3 - Insumos en riesgo -- 6 filas

 id_insumo |         nombre          | stock | unidades_consumidas | alerta
-----------+-------------------------+-------+---------------------+---------
         2 | Vacuna triple felina    |     3 |                   1 | CRITICO
         5 | Gasa esteril            |     8 |                   4 | BAJO
         1 | Vacuna antirrabica      |    12 |                   1 | OK
         4 | Suero fisiologico 500ml |    25 |                   1 | OK
         3 | Antiparasitario oral    |    40 |                   2 | OK
         6 | Jeringa 5ml             |    60 |                   3 | OK

Un CRITICO, un BAJO y cuatro OK, con los criticos arriba. Las unidades
consumidas suman 12, que es el total de cantidad en las 8 filas de
detalle_factura: 1+1+2+1+4+3 = 12.

Dos limites de este reporte que conviene decir en la devolucion. Primero: los 6
insumos aparecen en detalle_factura, asi que un INNER JOIN devuelve exactamente
las mismas 6 filas y el LEFT JOIN no se puede distinguir por el resultado -- hay
que leer el SQL. Segundo: ningun insumo tiene stock 5 ni 10, asi que los bordes
del CASE tampoco se prueban con estos datos. Quien quiera comprobarlos de verdad
puede correr
  UPDATE insumo SET stock = 10 WHERE id_insumo = 6;
y confirmar que el 10 queda en BAJO, que es la lectura inclusiva de "entre 5 y
10". Los dos reportes que pasan por suerte son R1 y R3; el unico que se delata
solo es R2.""",
                "como_calificar": [
                    "**6 pts — R1, agenda operativa.** 3 pts las **siete** columnas pedidas —"
                    "`fecha_hora`, mascota, especie, dueno, telefono del dueno, veterinario y "
                    "`estado`—, que salen de un `JOIN` de cuatro tablas; 2 pts el filtro **por "
                    "rango** (`>= '2026-09-01'` y `< '2026-10-01'`) y la exclusion de las "
                    "canceladas; 1 pt el `ORDER BY fecha_hora`. **Se califica leyendo el SQL, no "
                    "contando filas:** las 10 citas de esta base estan en septiembre de 2026, asi "
                    "que un `EXTRACT(MONTH FROM c.fecha_hora) = 9` devuelve las mismas 9 filas y "
                    "aun asi vale 0 de los 2 pts del filtro, por no ser sargable y por confundir "
                    "septiembre de 2026 con el de cualquier otro ano.",
                    "**8 pts — R2, y es la pregunta que de verdad se evalua aqui.** 2 pts las seis "
                    "columnas; 2 pts que los **seis** duenos aparezcan, con `0` los que no tienen "
                    "actividad —`LEFT JOIN` o subconsultas escalares, mas `COALESCE` en el `SUM`—; "
                    "**3 pts que los conteos no esten inflados**, con `COUNT(DISTINCT ...)` o con "
                    "subconsultas agregadas; 1 pt el `ORDER BY total_facturado DESC`. La forma "
                    "rapida de calificar es sumar las columnas: **8 mascotas, 10 citas, 4 "
                    "consultas y 178.200** facturados. Si algun subtotal no cuadra, el conteo esta "
                    "inflado.",
                    "**5 pts — R3, insumos en riesgo.** 2 pts el `CASE` con los tres niveles bien "
                    "delimitados —`CRITICO` con stock menor que 5, `BAJO` entre 5 y 10, `OK` el "
                    "resto—; 2 pts las unidades consumidas desde `detalle_factura` con `LEFT JOIN` "
                    "y `COALESCE`; 1 pt el orden por criticidad. El resultado esperado es **un "
                    "`CRITICO` (Vacuna triple felina, 3), un `BAJO` (Gasa esteril, 8) y cuatro "
                    "`OK`**, con 12 unidades consumidas en total.",
                    "**1 pt — los tres comentarios `--` de decision de negocio,** uno por reporte. "
                    "Se pide una **decision concreta** —«decide la orden de compra de esta "
                    "semana»—, no una descripcion del reporte —«muestra los insumos con poco "
                    "stock»—. Se reconoce como sobresaliente citar un numero de la propia salida: "
                    "que Ana Gomez concentra 131.200 de los 178.200, o que Marcela Diaz tiene 3 "
                    "citas y ninguna factura, que es una pregunta para el mostrador y no para la "
                    "base.",
                    "**Advertencia para calificar, que vale la pena decirle al grupo:** de los "
                    "tres reportes, **dos pasan por suerte con estos datos**. En R1 el filtro de "
                    "fecha no excluye ninguna fila, y en R3 los seis insumos aparecen en "
                    "`detalle_factura`, asi que un `INNER JOIN` da el mismo resultado que el "
                    "`LEFT JOIN`, y ningun stock vale 5 ni 10, asi que los bordes del `CASE` no se "
                    "prueban. **R2 es el unico que se delata solo.** Por eso R2 pesa 8 de los 20 "
                    "puntos y los otros dos se leen linea por linea.",
                    "**Se reconoce como sobresaliente, sin puntos extra:** notar que los `COUNT` no "
                    "necesitan `COALESCE` pero el `SUM` si —un `COUNT` sin filas devuelve 0, un "
                    "`SUM` sin filas devuelve `NULL`—; o poner un segundo criterio en el `ORDER BY` "
                    "de R2 porque **cuatro duenos empatan en 0.00** y sin desempate el orden lo "
                    "decide el motor.",
                ],
                "errores": [
                    "**El conteo inflado en R2.** Es el error central de la pregunta y el enunciado "
                    "lo avisa. Con la cadena `dueno -> mascota -> cita -> consulta -> factura` sin "
                    "`DISTINCT`, Ana Gomez pasa de **2 mascotas a 4** y Marcela Diaz de 2 a 3. Lo "
                    "traicionero es que las citas, las consultas y el total facturado **salen "
                    "correctos** con estos datos, asi que la trampa se delata en una sola columna: "
                    "la de mascotas es la que hay que mirar siempre.",
                    "**`EXTRACT(MONTH FROM c.fecha_hora) = 9` en R1.** Devuelve las 9 filas "
                    "correctas y aun asi esta mal por dos razones independientes: no es sargable "
                    "—ningun indice sobre `fecha_hora` se puede usar, que es toda la Clase 6— y "
                    "confunde septiembre de 2026 con septiembre de cualquier otro ano. Con esta "
                    "base no se nota; con dos anos de historia, si.",
                    "**`c.fecha_hora <= TIMESTAMP '2026-09-30'`** en vez de "
                    "`< '2026-10-01'`. Con un `TIMESTAMP`, ese `<=` corta a las 00:00:00 y **pierde "
                    "todo el 30 de septiembre**. Aqui no hay citas ese dia, asi que el error no se "
                    "ve —y por eso es de los que llegan a produccion—. La regla: con fechas-hora, "
                    "el limite superior siempre es exclusivo y del dia siguiente.",
                    "**`INNER JOIN` en R2 y los duenos sin actividad desaparecen.** El reporte "
                    "sale con 2 filas en vez de 6, y las cuatro que faltan son precisamente la "
                    "lista de reactivacion: el reporte pierde a los clientes que hay que llamar. "
                    "Se detecta contando filas —tienen que ser **6**—.",
                    "**Olvidar el `COALESCE` en el `SUM` de R2.** Los cuatro duenos sin facturas "
                    "salen con `NULL` en lugar de `0.00`, y al proyectarlo se ven cuatro celdas "
                    "vacias. El enunciado lo pide explicitamente. Ademas cualquier calculo "
                    "posterior sobre esa columna se contamina, porque `NULL` no es cero.",
                    "**Los bordes del `CASE` en R3 mal delimitados:** dejar el 5 en `CRITICO` o "
                    "escribir los tres `WHEN` como rangos independientes con un hueco entre ellos, "
                    "y que un insumo caiga en `NULL`. Con estos datos no se ve, porque **ningun "
                    "stock vale 5 ni 10**. Un `UPDATE insumo SET stock = 10 WHERE id_insumo = 6;` "
                    "lo comprueba en cinco segundos.",
                    "**Comentarios de decision que describen el reporte en vez de decidir algo:** "
                    "«R3 muestra los insumos con poco stock». Eso ya se ve en el titulo. Lo que se "
                    "pide es la frase que se dice en la demo: «este reporte decide la orden de "
                    "compra de esta semana, y hoy dice que la Vacuna triple felina se pide ya».",
                ],
            },
            {
                "n": 4,
                "titulo": "Checklist de avance del PI (firmada)",
                "tipo": "abierta",
                "puntos": 15,
                "tabla": {
                    "headers": ["#", "Item", "Estado", "Evidencia (archivo u objeto)",
                                "Observacion"],
                    "rows": [
                        ["1", "Modelo ER actualizado y coherente con el DDL real", "**SI**",
                         "`/informe/01-modelo-er.md` y la pregunta 1 de esta clase en ExamLab",
                         "Ya trae `audit_cita` sin FK y las columnas que aparecieron por el "
                         "camino: `ciudad`, `fecha_nac`, `activa`, `activo`, `usuario_bd`"],
                        ["2", "DDL completo de las 8 tablas con PK, FK y `CHECK`", "**PARCIAL**",
                         "`/db/01_ddl.sql`",
                         "Las 8 tablas con PK, FK y los `CHECK` de `activa`, `activo`, `estado`, "
                         "`stock >= 0`, `precio >= 0` y `cantidad > 0`. Faltan dos cosas: el "
                         "`uq_cita_vet_franja` de la Clase 10 **no se llevo al script**, y no hay "
                         "**ninguna** restriccion que proteja la coherencia de `factura.total` — "
                         "la prueba 5 de hoy encontro las tres facturas historicas descuadradas"],
                        ["3", "Plan de roles y privilegios con matriz rol x objeto", "**PARCIAL**",
                         "`/informe/03-roles.md` (la matriz) y `/db/03_roles.sql`",
                         "La matriz esta completa para los tres roles —`vetcare_recepcion`, "
                         "`vetcare_veterinario`, `vetcare_admin`— pero solo se probaron los "
                         "`GRANT` de recepcion. **Ninguna prueba negativa:** nadie verifico que "
                         "recepcion *no* pueda borrar una factura"],
                        ["4", "Al menos un procedimiento de negocio con validacion", "**SI**",
                         "objeto `sp_agendar_cita` en `/db/02_procedimientos.sql`",
                         "Valida existencia de la mascota, `activa` y franja ocupada. Verificado "
                         "hoy en la prueba 2 con el `SQLERRM` guardado"],
                        ["5", "Al menos una funcion util al PI", "**SI**",
                         "objetos `fn_precio_consulta` y `fn_tomar_stock` en "
                         "`/db/02_procedimientos.sql`",
                         "Dos funciones, no una. `fn_tomar_stock` es la de la Clase 10 y devuelve "
                         "`BOOLEAN` en vez de lanzar excepcion, a proposito: «no hay stock» es un "
                         "caso de negocio, no un error tecnico"],
                        ["6", "Al menos un trigger de auditoria funcionando", "**SI**",
                         "objetos `fn_trg_audit_cita` y `trg_audit_cita`, tabla `audit_cita`",
                         "Son **dos** objetos, no uno: la funcion y el disparador. Verificado hoy "
                         "en la prueba 4, con `PROGRAMADA -> CANCELADA` registrado"],
                        ["7", "Regla «mascota inactiva no agenda» verificada con una prueba que "
                         "falla a proposito", "**SI**",
                         "prueba 2 de la pregunta 2 de hoy; fila 2 de `checklist_pi`",
                         "La evidencia guarda el `SQLERRM`, no solo el veredicto: se puede "
                         "demostrar que fallo **por esa** regla y no por otra"],
                        ["8", "Regla «stock nunca negativo» verificada con una prueba que falla a "
                         "proposito", "**SI**",
                         "prueba 3 de la pregunta 2 de hoy; fila 3 de `checklist_pi`",
                         "Ademas del rechazo, la evidencia trae el **stock del insumo 2 = 3** "
                         "despues del intento: prueba que el fallo no movio nada"],
                        ["9", "Transaccion de facturacion atomica con rollback demostrado",
                         "**SI**",
                         "Clase 8, pregunta 2, y `/informe/08-transacciones.md`",
                         "El intento fallido dejo la base identica y el reintento valido paso. "
                         "Documentado ademas que el `id_factura` de la secuencia **si** se "
                         "consume, asi que quedan huecos en la numeracion"],
                        ["10", "Par de consultas antes/despues con evidencia de `EXPLAIN`",
                         "**SI**",
                         "`/informe/06-explain-antes-despues.md` con las dos capturas",
                         "`Seq Scan` con `Rows Removed by Filter` antes, `Index Cond` despues. "
                         "Las dos capturas con el `EXPLAIN (ANALYZE, BUFFERS)` completo, no "
                         "recortado"],
                        ["11", "Al menos dos indices justificados", "**SI**",
                         "`/db/04_indices.sql`",
                         "Tres: `cita (id_veterinario, fecha_hora)`, el parcial de "
                         "`estado <> 'CANCELADA'` y `detalle_factura (id_insumo)` —este ultimo "
                         "porque PostgreSQL **no** crea indice por declarar una FK, solo por PK y "
                         "`UNIQUE`"],
                        ["12", "Plan de respaldo con procedimiento de restore de prueba", "**NO**",
                         "`/informe/04-respaldo.md`, que trae **solo el plan**",
                         "El plan esta escrito con RPO de 15 minutos y RTO de 4 horas, pero **el "
                         "restore nunca se ensayo**. Un respaldo que no se ha restaurado no es un "
                         "respaldo: es un archivo del que nadie sabe si sirve"],
                        ["13", "Escenarios de concurrencia documentados con su mitigacion",
                         "**PARCIAL**",
                         "`/informe/10-concurrencia.md` y `/db/05_restricciones_concurrencia.sql`",
                         "Los dos escenarios documentados con linea de tiempo y mitigacion "
                         "elegida, y la restriccion **si** quedo probada. Lo que no se pudo es "
                         "**verificar la concurrencia**: ExamLab corre PostgreSQL en WebAssembly "
                         "con una sola conexion"],
                        ["14", "Scripts organizados y ejecutables en orden", "**PARCIAL**",
                         "carpeta `/db/` con `01_ddl.sql` a `05_restricciones_concurrencia.sql`",
                         "Estan numerados y ordenados, pero **nunca se corrieron de cero sobre "
                         "una base vacia**. El orden es una suposicion razonable, no un hecho "
                         "verificado"],
                    ],
                },
                "respuesta": (
                    "**Porcentaje de avance declarado: 79 %.** La cuenta, que tiene que estar "
                    "escrita y no solo el resultado: **9 items en `SI`** —1, 4, 5, 6, 7, 8, 9, 10 "
                    "y 11— valen 1 cada uno; **4 en `PARCIAL`** —2, 3, 13 y 14— valen 0,5 cada "
                    "uno; **1 en `NO`** —el 12— vale 0. Total **9 + 2 = 11 sobre 14 = 78,57 %**, "
                    "que se declara como **79 %**. Si el porcentaje no se puede reconstruir desde "
                    "la tabla, el checklist no es un checklist: es una opinion con formato de "
                    "tabla.\n\n"
                    "**El item mas debil: el 12, el respaldo.** Y no es el mas debil por ser el "
                    "unico `NO` —eso seria contar—, sino por una razon que conviene decir "
                    "completa: **es el unico item cuyo fallo no tiene arreglo posterior.** Si la "
                    "matriz de roles esta a medias, un dia alguien ve datos que no debia y se "
                    "corrige. Si la concurrencia no esta verificada, aparece una cita duplicada y "
                    "se limpia. Pero si el respaldo no restaura, **no hay nada que corregir**: se "
                    "perdio. Y lo mas incomodo es que un respaldo roto se ve exactamente igual que "
                    "uno bueno hasta el dia en que se necesita —el archivo esta ahi, pesa lo que "
                    "debe, la tarea programada dice «exito»—. El plan documenta un RPO de 15 "
                    "minutos y un RTO de 4 horas, y esos dos numeros hoy son **promesas sin "
                    "medir**: nadie ha cronometrado un restore, asi que el RTO de 4 horas es una "
                    "estimacion tan buena como cualquier otra.\n\n"
                    "*Segundo mas debil, para tenerlo a la vista:* el item 2, y no por las 8 tablas "
                    "—esas estan— sino por lo que la prueba 5 de hoy destapo. No hay ninguna "
                    "restriccion que impida que `factura.total` se separe de la suma de sus "
                    "detalles, y las tres facturas historicas ya estan separadas. El DDL protege "
                    "bien el dominio de cada columna y **no protege ninguna relacion entre "
                    "columnas de tablas distintas**, que es exactamente donde se escondio el "
                    "defecto.\n\n"
                    "**Compromiso.** Los seis gaps de la pregunta 5 se cierran antes del "
                    "**2026-11-16**, fecha de la sustentacion del PI, con las fechas y la "
                    "evidencia que ahi se detallan. El item 12 se cierra primero, porque es el "
                    "unico irreversible.\n\n"
                    "> Firmado: **(nombre y apellido del estudiante que entrega)** — Bases de "
                    "Datos II, grupo 641A-2 — **2026-10-26**.\n\n"
                    "*Nota sobre la firma, para quien califique:* se exige el nombre propio y la "
                    "fecha, y se rechaza «el equipo» o un nombre de grupo. Si el trabajo es en "
                    "equipo autorizado, firman todos los integrantes, cada uno con su nombre. No "
                    "se piden ni se registran otros datos personales: nombre y fecha bastan para "
                    "que el compromiso sea atribuible."
                ),
                "como_calificar": [
                    "**7 pts — los 14 items con estado, evidencia y observacion,** a 0,5 pts cada "
                    "uno. El estado tiene que ser `SI` / `NO` / `PARCIAL`, sin inventar categorias "
                    "intermedias. Los tres campos son obligatorios: un item con estado y sin "
                    "observacion vale 0,25.",
                    "**4 pts — que la evidencia sea rastreable, y este es el criterio duro de la "
                    "pregunta.** La rubrica dice literalmente «evidencia nombrada (archivo u "
                    "objeto concreto)», y **nombrada** significa que se puede abrir: "
                    "`/db/02_procedimientos.sql`, el objeto `trg_audit_cita`, «la prueba 3 de la "
                    "pregunta 2 de esta clase». Se descuenta sin excepcion por «esta en mi "
                    "carpeta», «lo hice en clase», «ver el codigo» o «en ExamLab» sin decir cual. "
                    "La regla practica al calificar: si no se puede verificar en 30 segundos, no "
                    "es evidencia.",
                    "**2 pts — el porcentaje aritmeticamente coherente con los estados marcados.** "
                    "`SI` = 1, `PARCIAL` = 0,5, `NO` = 0, sobre 14. Se exige **la cuenta escrita**, "
                    "no solo el numero: cuantos `SI`, cuantos `PARCIAL`, cuantos `NO` y la "
                    "division. Un 95 % declarado sobre una tabla con cuatro `PARCIAL` y un `NO` "
                    "pierde estos 2 pts completos —y conviene senalar en la devolucion que es el "
                    "tipo de incoherencia que un jurado detecta en la primera lamina—.",
                    "**1,5 pts — el item mas debil, argumentado.** 0,5 pts nombrarlo y **1 pt la "
                    "razon**. Se acepta cualquier item si el argumento se sostiene, pero el "
                    "argumento tiene que ir mas alla de «es el unico `NO`»: lo que se busca es un "
                    "criterio —irreversibilidad, impacto en el negocio, dependencia de otros "
                    "items—. El razonamiento mas fuerte es el del respaldo: **es el unico cuyo "
                    "fallo no se puede corregir despues**, y encima un respaldo roto se ve igual "
                    "que uno bueno hasta el dia en que se necesita.",
                    "**0,5 pts — la firma con nombre propio y fecha.** Se rechaza «el equipo» o un "
                    "nombre de grupo; en equipo autorizado firman todos los integrantes con su "
                    "nombre. La fecha es la de la sesion, **2026-10-26**. No se piden ni se "
                    "registran mas datos personales.",
                    "**Este checklist es un modelo de referencia, no una clave.** Cada estudiante "
                    "declara su propio PI y la distribucion correcta de estados es la que "
                    "corresponda a su avance real. Lo que **si** conviene contrastar: los items 7 y "
                    "8 deberian ser `SI` en todo el grupo, porque se verificaron hoy en la "
                    "pregunta 2 de esta misma clase; y el item 13 dificilmente puede ser `SI`, "
                    "porque el entorno no permite verificar concurrencia. Un checklist con 14 `SI` "
                    "es la senal mas clara de que no se reviso nada —y con el item 12, ademas, es "
                    "casi seguro falso, porque el restore no se ha podido ensayar en ninguna "
                    "clase—.",
                ],
                "errores": [
                    "**Los 14 items en `SI` y un 100 % declarado.** Es el error dominante y el que "
                    "mas cuesta, porque contradice el sentido del hito: un checklist sirve para "
                    "encontrar lo que falta. Se desmonta con dos preguntas concretas —«¿cuando "
                    "ensayaste el restore?» y «¿como verificaste la concurrencia con una sola "
                    "conexion?»— y ninguna de las dos tiene respuesta posible con lo visto en el "
                    "curso.",
                    "**Evidencia generica:** «esta en mi carpeta del PI», «lo trabajamos en "
                    "clase», «ver el codigo», «en ExamLab». No es evidencia porque no se puede "
                    "abrir. Cuesta hasta 4 pts y ademas hace inutil el checklist para lo unico que "
                    "sirve, que es reencontrar el trabajo tres semanas despues.",
                    "**El porcentaje que no cuadra con la tabla.** Aparece de dos formas: "
                    "inventado a ojo, o contando los `PARCIAL` como 1. Es el punto mas facil de "
                    "verificar al calificar —se cuentan los estados y se divide— y el mas facil de "
                    "evitar: se escribe la cuenta debajo de la tabla.",
                    "**Marcar `PARCIAL` sin decir que falta.** «Parcial» sin la parte que falta no "
                    "informa nada, y sobre todo **no se puede convertir en un gap** de la pregunta "
                    "5. La observacion de un `PARCIAL` tiene que ser precisamente la tarea "
                    "pendiente: «falta llevar `uq_cita_vet_franja` al script», no «esta a medias».",
                    "**Marcar el item 13 como `SI` porque «se documento la concurrencia».** "
                    "Documentar no es verificar, y el item dice «documentados con su mitigacion», "
                    "que es justo el punto discutible. `PARCIAL` con la razon —una sola conexion en "
                    "ExamLab— es la respuesta madura; `SI` a secas contradice la propia solucion "
                    "de la Clase 10, donde se declaro por escrito que no se pudo probar.",
                    "**Firmar «el equipo» o con el nombre del grupo.** El compromiso tiene que ser "
                    "atribuible a una persona. Es la misma logica de la pregunta 5 con los "
                    "responsables, y es lo que separa un plan de un deseo colectivo.",
                    "**Un item mas debil elegido sin argumento,** o argumentado solo con «es el "
                    "unico que no hice». La pregunta pide un criterio. Sin el, se pierde 1 de los "
                    "1,5 pts, y en la sustentacion la respuesta a «¿que es lo que mas te "
                    "preocupa?» se queda en el aire.",
                ],
            },
            {
                "n": 5,
                "titulo": "Lista de gaps con responsable y fecha",
                "tipo": "abierta",
                "puntos": 10,
                "tabla": {
                    "headers": ["#", "Gap (tarea verificable)", "Item", "Impacto si no se cierra",
                                "Responsable", "Fecha", "Como se verificara"],
                    "rows": [
                        ["1",
                         "Conciliar las facturas 1, 2 y 3: decidir con el criterio del negocio si "
                         "el total correcto es el guardado o la suma de los detalles, documentar "
                         "la decision y ajustar el lado que corresponda",
                         "2",
                         "El reporte de facturacion de la demo no cuadra. Si el jurado suma una "
                         "factura a mano, el PI queda con un descuadre de 29.600 sin explicacion",
                         "(el estudiante que firma)", "**2026-10-30**",
                         "La prueba 5 de la bateria devuelve `cumple = TRUE` **y** el archivo "
                         "`/informe/11-conciliacion-facturas.md` contiene la decision con el "
                         "antes y el despues de las tres filas"],
                        ["2",
                         "Llevar `CREATE UNIQUE INDEX uq_cita_vet_franja ON cita "
                         "(id_veterinario, fecha_hora) WHERE estado <> 'CANCELADA'` al script "
                         "`/db/01_ddl.sql`",
                         "2",
                         "La mitigacion de la doble reserva existe en ExamLab pero no en el "
                         "proyecto: al recrear la base desde los scripts, la clinica vuelve a "
                         "poder agendar dos citas en la misma franja",
                         "(el estudiante que firma)", "**2026-10-30**",
                         "`SELECT indexname FROM pg_indexes WHERE tablename = 'cita';` devuelve "
                         "`uq_cita_vet_franja` en una base creada **solo** con los scripts de "
                         "`/db/`"],
                        ["3",
                         "Ejecutar los `GRANT` y `REVOKE` de los tres roles y correr **una prueba "
                         "negativa por rol**: que `vetcare_recepcion` reciba «permiso denegado» al "
                         "intentar `DELETE FROM factura`",
                         "3",
                         "La matriz de roles es un documento sin efecto. Cualquier usuario de la "
                         "aplicacion puede borrar facturas, y eso es justo lo que la auditoria no "
                         "puede reconstruir",
                         "(el estudiante que firma)", "**2026-11-06**",
                         "`/informe/03-roles.md` con las tres capturas del mensaje "
                         "`permission denied for table factura`, una por rol"],
                        ["4",
                         "Ensayar el restore completo: generar el respaldo, crear una base vacia, "
                         "restaurarla, **cronometrar** y verificar con la bateria de la pregunta 2 "
                         "que las 5 pruebas dan el mismo resultado",
                         "12",
                         "Es el unico gap irreversible. Si el respaldo no sirve y se descubre el "
                         "dia del incidente, no hay correccion posible: el PI se queda sin base y "
                         "la clinica sin historia clinica",
                         "(el estudiante que firma)", "**2026-11-06**",
                         "`/informe/04-respaldo.md` con el tiempo real medido frente al RTO "
                         "prometido de 4 horas, y la salida de `checklist_pi` sobre la base "
                         "restaurada"],
                        ["5",
                         "Verificar los dos escenarios de concurrencia con **dos sesiones de "
                         "`psql`** contra un PostgreSQL local, capturando la sesion bloqueada",
                         "13",
                         "La seccion de concurrencia se sustenta con razonamiento y sin evidencia. "
                         "Si el jurado pregunta «¿lo probaste?», la respuesta honesta hoy es no",
                         "(el estudiante que firma)", "**2026-11-11**",
                         "`/informe/10-evidencia.txt` con la fila de `pg_locks` en "
                         "`granted = false`, el `wait_event_type = 'Lock'` de "
                         "`pg_stat_activity` y el `unique_violation` de la segunda sesion"],
                        ["6",
                         "Correr `/db/01_ddl.sql` a `/db/05_restricciones_concurrencia.sql` en ese "
                         "orden sobre una base **vacia**, sin editar nada, y corregir el orden si "
                         "algo falla",
                         "14",
                         "Es el gap que se cobra el dia de la sustentacion: si un script depende "
                         "de un objeto que se crea despues, la demo se cae en vivo y no hay "
                         "tiempo de arreglarlo",
                         "(el estudiante que firma)", "**2026-11-13**",
                         "Bitacora en `/informe/14-orden-de-scripts.md` con la salida de los cinco "
                         "scripts sin un solo `ERROR`, y la bateria de la pregunta 2 corriendo al "
                         "final"],
                    ],
                },
                "respuesta": (
                    "**El riesgo mas grande es el gap 4, el restore que nunca se ha ensayado, y "
                    "por dos razones que se suman.** Es el unico irreversible —los otros cinco se "
                    "descubren, se corrigen y se sigue; este se descubre el dia en que ya no hay "
                    "nada que corregir— y es el unico que depende de algo que **no** esta en "
                    "ExamLab: hace falta un PostgreSQL de verdad, con `pg_dump` y `psql`, y ahi "
                    "puede aparecer cualquier tropiezo de instalacion que consuma la unica semana "
                    "disponible. Encima el RTO de 4 horas que el plan promete es hoy una "
                    "estimacion sin medir: puede resultar que restaurar tome veinte minutos, y "
                    "tambien puede resultar que el respaldo no cargue.\n\n"
                    "**Plan B si el gap 4 no se cierra:** presentar el procedimiento de restore "
                    "**escrito paso a paso y ejecutable** —comandos exactos de `pg_dump` y `psql`, "
                    "con el orden y los parametros—, declarar en la lamina que **no se ensayo** y "
                    "por que, y sustituir el ensayo completo por la evidencia parcial que si es "
                    "alcanzable: un `pg_dump` generado, su tamano, y el `pg_restore --list` que "
                    "demuestra que el archivo es legible y trae las 8 tablas mas los "
                    "procedimientos. No es lo mismo que un restore cronometrado y hay que decirlo "
                    "asi: **prueba que el respaldo existe y es legible, no que la base vuelve a "
                    "funcionar.** El RTO se presenta marcado como «estimado, sin medir». Es lo "
                    "mismo que se hizo con la concurrencia en la Clase 10 y es la unica forma "
                    "honesta de cerrar: se entrega la mitigacion en papel con el limite escrito "
                    "encima, nunca un `SI` que no se puede sostener.\n\n"
                    "*Y una nota sobre el calendario, porque las fechas de la tabla no son "
                    "arbitrarias:* del **2026-10-26** al **2026-11-16** hay tres semanas, pero el "
                    "**2026-11-09 es el Parcial 3** y ese dia no se cierra ningun gap. Por eso los "
                    "dos gaps baratos —1 y 2, que son media hora de SQL— caen el 30 de octubre; "
                    "los dos que necesitan montar algo —3 y 4— el 6 de noviembre, antes del "
                    "parcial; y los dos ultimos el 11 y el 13, dejando el fin de semana del 14 y "
                    "15 libre para armar la presentacion. **Ningun gap cae el mismo dia de la "
                    "sustentacion**, que es el error clasico de estas tablas."
                ),
                "como_calificar": [
                    "**5 pts — la tabla con 4 a 8 gaps y sus siete columnas completas.** "
                    "Aproximadamente 0,8 pts por gap con las columnas llenas. Menos de 4 filas o "
                    "mas de 8 se descuenta por no seguir el enunciado. **Los gaps tienen que "
                    "corresponder a los `NO` y `PARCIAL` de la pregunta 4** —eso lo exige la "
                    "rubrica— asi que la primera cosa que se hace al calificar es contrastar las "
                    "dos preguntas: un gap que no sale de ningun item marcado es un gap inventado, "
                    "y un `PARCIAL` sin gap es un pendiente que nadie va a cerrar.",
                    "**2 pts — que cada gap este redactado como tarea verificable.** El enunciado "
                    "da el contraste exacto: «crear el trigger `trg_stock_no_negativo` y probarlo "
                    "con dos casos» **si**, «mejorar los triggers» **no**. La prueba practica al "
                    "calificar: si al leer el gap no se puede decir quien hace **que** y como se "
                    "sabra que termino, no es verificable. Un buen gap nombra el objeto, el "
                    "archivo o el comando.",
                    "**1,5 pts — un responsable con nombre real por fila y fechas anteriores a la "
                    "sustentacion.** 1 pt el responsable: **se rechaza «el equipo»** sin excepcion, "
                    "y si el estudiante trabaja solo tiene que aparecer su nombre en las seis "
                    "filas. 0,5 pts las fechas, todas anteriores al **2026-11-16**. Se reconoce "
                    "como sobresaliente que las fechas esten escalonadas por costo y que ninguna "
                    "caiga el 2026-11-09, que es el Parcial 3, ni el dia mismo de la sustentacion.",
                    "**1 pt — la columna de verificacion con evidencia concreta.** Tiene que "
                    "nombrar una consulta, un script, una captura o una fila: «la prueba 5 devuelve "
                    "`TRUE`», «`SELECT indexname FROM pg_indexes ...` devuelve "
                    "`uq_cita_vet_franja`», «la fila de `pg_locks` con `granted = false`». Se "
                    "descuenta por «se revisara», «quedara funcionando» o «se verificara en clase».",
                    "**0,5 pts — el riesgo mas grande y el plan B, en 3 a 5 lineas.** El plan B "
                    "tiene que ser **realista y especifico**, y el enunciado ya sugiere la forma: "
                    "documentar el limite y presentar la mitigacion en papel en lugar de "
                    "ejecutada. Se reconoce como sobresaliente que el plan B diga **que prueba "
                    "menos** que el plan A —«un `pg_restore --list` demuestra que el archivo es "
                    "legible, no que la base vuelve a funcionar»—, porque eso es exactamente lo "
                    "que un jurado va a preguntar.",
                    "**Este plan es un modelo de referencia, no una clave:** los gaps de cada "
                    "estudiante son los de su propio checklist. Lo que si conviene esperar en casi "
                    "todo el grupo son dos: el **descuadre de las facturas** que la pregunta 2 "
                    "destapo hoy, y el **restore sin ensayar**. Si ninguno de los dos aparece en la "
                    "tabla, vale la pena releer la pregunta 4 del mismo estudiante, porque casi "
                    "seguro hay un `SI` que no se sostiene.",
                ],
                "errores": [
                    "**Gaps redactados como deseos:** «mejorar la seguridad», «optimizar las "
                    "consultas», «terminar la documentacion». No se pueden cerrar porque no se "
                    "puede decir cuando estan cerrados. El enunciado lo advierte con un ejemplo "
                    "literal y aun asi es el error mas comun. Al devolverlo conviene pedir la "
                    "reescritura de uno solo: casi siempre el estudiante ve el patron y corrige "
                    "los demas.",
                    "**«El equipo» o «todos» como responsable.** Un gap con responsable colectivo "
                    "no tiene responsable. Es la traduccion practica de la firma de la pregunta 4: "
                    "si el trabajo es individual, van seis filas con el mismo nombre y eso esta "
                    "bien; si hay equipo autorizado, se reparte por nombre.",
                    "**Fechas posteriores a la sustentacion, o todas el mismo dia.** Poner los seis "
                    "gaps «para el 2026-11-15» no es un plan: es la misma frase repetida seis "
                    "veces. Y cualquier fecha del 2026-11-16 o despues incumple el enunciado, "
                    "porque cerrar un gap el dia de la sustentacion es no cerrarlo.",
                    "**Gaps que no salen del checklist de la pregunta 4.** Aparecen dos formas y "
                    "las dos se descuentan: inventar gaps nuevos que no corresponden a ningun `NO` "
                    "ni `PARCIAL`, y —peor— dejar un `PARCIAL` de la pregunta 4 sin ningun gap que "
                    "lo cierre. Las dos preguntas se califican juntas, siempre.",
                    "**Columna de verificacion vacia de contenido:** «se verificara con una "
                    "prueba», «quedara funcionando», «lo revisara el docente». Si la verificacion "
                    "no nombra una consulta, un archivo o una captura, el gap no se puede declarar "
                    "cerrado y el plan no sirve para nada.",
                    "**Un plan B que es el plan A otra vez:** «si no alcanzo a ensayar el restore, "
                    "lo ensayo el fin de semana». Eso no es un plan B, es la misma tarea con otra "
                    "fecha. Un plan B verdadero **entrega menos y lo dice**: el procedimiento "
                    "escrito, la evidencia parcial que si es alcanzable, y el limite declarado en "
                    "la lamina.",
                    "**Omitir el descuadre de facturas y el restore sin ensayar.** Son los dos "
                    "gaps que este hito destapo y los dos que un jurado va a encontrar. Un plan de "
                    "cierre que no los incluye esta escrito sobre un checklist demasiado "
                    "optimista, y conviene decirselo asi al devolver la pregunta.",
                ],
            },
        ],
        "preguntas_frecuentes": [
            ("La prueba 5 me da `cumple = FALSE`. ¿Escribi mal la consulta?",
             "Casi seguro que no: **`FALSE` es la respuesta correcta.** Las tres facturas que trae "
             "la base estan descuadradas de verdad y se comprueba con una suma a mano: la factura "
             "1 guarda 71.000 y sus detalles suman 31.000 + 900 + 9.500 = **41.400**; la 2 guarda "
             "47.000 contra 9.500 + 7.000 = **16.500**; la 3 guarda 60.200 contra 22.000 + 4.800 + "
             "1.800 = **28.600**. Si te salio `TRUE`, revisa la consulta: lo mas probable es un "
             "`INNER JOIN` mal agrupado o un `HAVING` invertido. Y no lo tomes como un problema: es "
             "el hallazgo del hito. Una bateria de verificacion donde las cinco pruebas salen bien "
             "no verifico nada; la tuya encontro un dato incorrecto que llevaba semanas ahi."),
            ("Entonces, ¿arreglo las facturas con un `UPDATE` antes de la demo?",
             "**No, y esta es la pregunta mas importante de la clase.** Por dos razones. La "
             "primera es tecnica y es facil: en medio de la demo estarias borrando la evidencia del "
             "unico hallazgo del hito. La segunda es de negocio y es la que importa: **esos totales "
             "pueden ser lo que el cliente realmente pago.** Si sobrescribes 71.000 con 41.400 "
             "«para que cuadre el reporte», estas cambiando un registro contable para que encaje "
             "con tu consulta, no arreglando un error. Lo correcto es lo que haria cualquiera en un "
             "trabajo real: documentar el descuadre con numeros, preguntarle a quien conozca el "
             "negocio cual de los dos valores es el bueno, y dejarlo como gap numero 1 con "
             "responsable y fecha. Fijate ademas donde **no** esta el problema: `sp_facturar` "
             "calcula bien —la factura que creo en la Clase 8 cuadra al centavo—, asi que el "
             "descuadre es de los datos cargados antes de que el procedimiento existiera. Es la "
             "historia de cualquier migracion."),
            ("¿Por que en la prueba 1 hay que capturar `foreign_key_violation` y en la 2 vale "
             "`WHEN OTHERS`?",
             "Porque lo que se quiere probar es distinto. En la prueba 1 se quiere probar que **la "
             "FK** rechaza: si capturas `OTHERS`, un `NOT NULL` olvidado en tu `INSERT` tambien "
             "entraria por el manejador y quedaria registrado como «integridad referencial "
             "funcionando», cuando en realidad no probaste nada. En las pruebas 2 y 3, en cambio, "
             "lo que llega es una **excepcion de usuario**: el `RAISE EXCEPTION` que escribiste "
             "dentro del procedimiento, que cae en `raise_exception` (`P0001`) y no en un codigo "
             "especifico del motor. Ahi `WHEN OTHERS` es lo razonable, y por eso el enunciado pide "
             "guardar el `SQLERRM`: el texto del mensaje es lo unico que demuestra que fallo por "
             "**esa** regla y no porque la franja estuviera ocupada."),
            ("En la prueba 3, ¿por que el stock que leo es 3 y no 0 o un negativo?",
             "Porque el `SELECT` del stock esta **dentro del manejador**, y el manejador corre "
             "**despues** de que la base volvio atras. Un bloque `BEGIN ... EXCEPTION` abre un "
             "savepoint implicito: cuando salta la excepcion, PostgreSQL deshace todo lo que el "
             "procedimiento alcanzo a hacer —incluida la factura que ya habia insertado— y solo "
             "entonces ejecuta tu manejador. Ese 3 es el valor **restaurado**, y justamente por eso "
             "vale como evidencia: prueba que el intento fallido no dejo rastro. Un detalle para la "
             "demo: la fila de `factura` desaparecio, pero el **id 4 de la secuencia si se "
             "consumio**, asi que la proxima factura sera la 5. Las secuencias no vuelven atras ni "
             "con un `ROLLBACK`."),
            ("Mi reporte R1 da las mismas 9 filas usando `EXTRACT(MONTH ...) = 9`. ¿Esta bien?",
             "Da el resultado correcto y aun asi esta mal, por dos razones independientes. La "
             "primera es la de la Clase 6: envolver la columna en una funcion **rompe la "
             "sargabilidad**, asi que ningun indice sobre `fecha_hora` se puede usar y la consulta "
             "queda condenada a leer la tabla entera. La segunda es de correccion: "
             "`EXTRACT(MONTH ...) = 9` es septiembre **de cualquier ano**, asi que el dia que la "
             "clinica tenga dos temporadas de historia el reporte de septiembre de 2026 va a traer "
             "tambien el de 2025. Que con esta base no se note es precisamente el problema: las 10 "
             "citas estan todas en septiembre de 2026, asi que el filtro **no excluye ninguna "
             "fila** y hasta sin `WHERE` de fecha verias lo mismo. Esta pregunta se califica "
             "leyendo el SQL."),
            ("¿Como evito el conteo inflado en R2 sin volverme loco con los `DISTINCT`?",
             "Con **una subconsulta escalar por metrica**, que es la forma que no se puede inflar: "
             "cada `COUNT` cuenta sobre su propia tabla y no hay producto cartesiano posible. La "
             "alternativa —`COUNT(DISTINCT ...)` en una cadena de `LEFT JOIN`— tambien funciona, "
             "pero hay que acordarse en las cuatro columnas y una sola que se olvide da un numero "
             "falso con cara de correcto. Con estos datos, la cadena sin `DISTINCT` infla a Ana "
             "Gomez de **2 mascotas a 4** y a Marcela Diaz de 2 a 3, mientras que las citas, las "
             "consultas y el total facturado salen bien. O sea que la trampa se delata en **una "
             "sola columna**: mira siempre la de mascotas. Y un detalle util: los `COUNT` no "
             "necesitan `COALESCE` porque un `COUNT` sin filas devuelve 0; el `SUM` si, porque "
             "devuelve `NULL`."),
            ("¿La demo de 3 a 5 minutos es en clase? Las Clases 11 y 12 son la misma sesion.",
             "Correcto, y es un dato que conviene tener claro desde el principio: **las Clases 11 y "
             "12 se dictan juntas el lunes 2026-10-26**, de 18:00 a 20:00, y esas dos horas tienen "
             "que cubrir el hito **y** el tema de integracion de apps externas. Para un grupo "
             "completo la demo en vivo no cabe, asi que lo que se pide es tenerla **lista y "
             "ensayada** —el ER de la pregunta 1 como lamina, la bateria de la pregunta 2 "
             "corriendo, los tres reportes de la pregunta 3 proyectables— y entregarla como "
             "grabacion o presentarla en la muestra que alcance. La practica que ahorra el peor "
             "momento: correr la bateria completa una vez de principio a fin **antes** de "
             "presentarla y contar las filas de `checklist_pi`. Tienen que ser 5."),
            ("¿Que fecha maxima puedo poner en los gaps de la pregunta 5?",
             "Cualquiera **anterior al 2026-11-16**, que es la sesion de sustentaciones del PI. Dos "
             "advertencias practicas. Una: el **2026-11-09 es el Parcial 3**, asi que no pongas "
             "gaps ese dia porque no vas a cerrar nada. Dos: poner los seis gaps «para el "
             "2026-11-15» no es un plan, es la misma frase repetida seis veces, y se descuenta. Lo "
             "que se espera es que las fechas esten **escalonadas por costo**: lo que son treinta "
             "minutos de SQL —conciliar las facturas, llevar el indice al script— va primero; lo "
             "que exige montar un PostgreSQL local va despues, con margen para que algo salga mal; "
             "y el fin de semana anterior queda libre para armar la presentacion. Que ningun gap "
             "caiga el dia de la sustentacion es lo primero que revisa quien califica."),
        ],
        "cierre": [
            "Al terminar, cada estudiante debe tener listo lo que se proyecta en la demo: el **ER "
            "consolidado** con las 9 entidades, `audit_cita` sin FK y los nombres verificados "
            "contra su propio DDL; la **bateria de cinco pruebas** que corre completa sin abortar "
            "y deja **5 filas** en `checklist_pi` con un veredicto de **4 de 5**; los **tres "
            "reportes** —9 filas en la agenda, 6 duenos con 8 mascotas / 10 citas / 4 consultas / "
            "178.200 facturados, y un `CRITICO` mas un `BAJO` en insumos—; el **checklist de 14 "
            "items** con evidencia rastreable, el porcentaje reconstruible y la firma; y la "
            "**lista de gaps** con responsable, fecha anterior al 2026-11-16 y evidencia concreta "
            "de cierre.",
            "Antes de cerrar hay que verificar **cuatro cosas**, y todas se leen sin ejecutar nada. "
            "Que la prueba 5 diga **`FALSE`** —si dice `TRUE`, la consulta esta escrita de forma "
            "que no puede fallar—. Que el `resultado` de la prueba 3 traiga el **3** del insumo 2, "
            "que es la evidencia de que el intento fallido no movio nada. Que en R2 los subtotales "
            "cuadren —**8, 10, 4 y 178.200**—, porque si alguno no cuadra el conteo esta inflado. Y "
            "la coherencia entre las preguntas 4 y 5: **cada `PARCIAL` o `NO` del checklist tiene "
            "que tener su gap**, y cada gap tiene que salir de un item marcado. Un checklist con 14 "
            "`SI` y una lista de gaps vacia no es un avance del 100 %: es una revision que no se "
            "hizo.",
            "Y el mensaje del hito, que es el que conviene dejar dicho: **la bateria valio la pena "
            "precisamente porque una prueba fallo.** Las cuatro primeras confirmaron lo que ya se "
            "sabia —la FK rechaza, el procedimiento valida, el stock no baja de cero, el trigger "
            "deja rastro—; la quinta encontro tres facturas descuadradas que llevaban semanas ahi "
            "y que nadie habia mirado, en datos cargados antes de que `sp_facturar` existiera. Un "
            "5 de 5 no habria descubierto nada. Eso cambia la forma de leer el checklist de la "
            "pregunta 4: el numero que importa no es el 79 %, es el **12** —el respaldo que nunca "
            "se ensayo—, porque es el unico item cuyo fallo no se puede corregir despues y porque "
            "un respaldo roto se ve exactamente igual que uno bueno hasta el dia en que se "
            "necesita. La Clase 12 arma la capa que la aplicacion consume y la integracion con "
            "apps externas; el 2026-11-16 hay que sustentar. **Los seis gaps de hoy son la lista "
            "real de trabajo hasta esa fecha, y el primero que se cierra es el irreversible.**",
        ],
    },

    12: {
        "titulo": "Solucion del taller · Clase 12 · Contrato de integracion app ↔ BD y sustentacion",
        "resumen": (
            "Las tres funciones `api_*` con el contrato uniforme `(ok, mensaje, id_generado)` y las "
            "seis llamadas con sus valores exactos; el cliente Python con parametros ligados, "
            "`dataclass` y corte en el primer rechazo; el diagrama de secuencia con la rama de "
            "error; el blindaje de privilegios **con la prueba negativa via `SET ROLE`, que destapa "
            "el defecto central de la clase: sin `SECURITY DEFINER` el rol de la aplicacion no "
            "puede usar la API**; el contrato de integracion con la tabla de los 13 mensajes de "
            "rechazo y el veredicto honesto de idempotencia (dos de las tres operaciones absorben "
            "el reintento por accidente, `api_facturar` cobra dos veces); y el guion de "
            "sustentacion de 7 minutos con la demo de 10 sentencias, el plan B y las tres "
            "preguntas del jurado que de verdad van a hacer."
        ),
        "total": 100,
        "nota_actividad": (
            "**Esta clase comparte sesion con la 11:** el lunes **2026-10-26**, 18:00 a 20:00, "
            "entran las dos. Seis preguntas no caben en lo que queda de esas dos horas, asi que lo "
            "razonable es guiar en vivo la pregunta 1 —que es donde se aprende el contrato— y "
            "dejar el resto como trabajo autonomo con fecha de cierre antes del **2026-11-16**, "
            "que es la sustentacion. **El motor es PostgreSQL, no Oracle.** Y hay que subrayar tres "
            "cosas antes de abrir el taller, porque son las que el jurado va a tocar. Primera y "
            "mas importante: **tal como esta escrita la pregunta 4, el rol `app_vetcare` no puede "
            "usar la API.** Las funciones se crean con `SECURITY INVOKER` —el valor por omision—, "
            "asi que corren con los privilegios de quien llama, y quien llama solo tiene `SELECT`: "
            "el `INSERT INTO cita` de adentro falla con «permission denied» y el "
            "`EXCEPTION WHEN OTHERS` lo devuelve como si fuera un rechazo de negocio. Falta "
            "`SECURITY DEFINER`, la rubrica no lo pide y por lo tanto no se descuenta, pero hay que "
            "decirlo en voz alta y la solucion lo demuestra con `SET ROLE`. Segunda: "
            "`api_agendar_cita` valida la franja con un `SELECT COUNT(*)`, que es **exactamente** "
            "el write skew de la Clase 10 —codigo, no restriccion—, asi que la API hereda el "
            "problema completo. Tercera: ese `EXCEPTION WHEN OTHERS` que hace elegante el contrato "
            "tambien convierte cualquier fallo de infraestructura en un mensaje de negocio, y eso "
            "es un riesgo, no una virtud. Por ultimo: la pregunta 2 es de tipo `codigo` y **no se "
            "ejecuta** —se califica leyendola—, y las preguntas 5 y 6 son sobre el PI real de cada "
            "estudiante, asi que lo que sigue es un **modelo de referencia y no una clave**. En la "
            "pregunta 2 no se aceptan credenciales escritas en el codigo: van por variables de "
            "entorno."
        ),
        "preguntas": [
            {
                "n": 1,
                "titulo": "La capa de API de VetCare: tres operaciones con contrato uniforme",
                "tipo": "bd_sql",
                "puntos": 28,
                "sql": """-- ======================================================================
-- POR QUE LAS TRES FUNCIONES SE PARECEN TANTO
--
-- El contrato es identico a proposito: RETURNS TABLE (ok, mensaje,
-- id_generado). La aplicacion aprende UNA forma de leer la respuesta y la
-- usa para las tres operaciones -- y para las que vengan despues. Eso es
-- lo que se entrega en la pregunta 5 como "contrato de integracion".
--
-- Tres detalles de plpgsql que hay que tener claros antes de escribir:
--
-- 1) RETURN QUERY NO TERMINA LA FUNCION. Agrega filas al resultado y
--    sigue ejecutando la linea de abajo. Por eso cada rechazo lleva un
--    RETURN; desnudo detras. Si se omite, la funcion devuelve DOS filas
--    -- una con ok = false y otra con ok = true -- y ademas hace el
--    INSERT que se queria evitar. Es el error mas grave y mas silencioso
--    de esta pregunta.
--
-- 2) IF NOT FOUND funciona despues de SELECT columna INTO var, pero NO
--    despues de SELECT COUNT(*) INTO var: un COUNT siempre devuelve una
--    fila, aunque sea 0. Por eso la franja se comprueba con
--    "IF v_ocupado > 0", no con NOT FOUND.
--
-- 3) El bloque EXCEPTION es lo que hace ATOMICA a cada funcion. Abre un
--    savepoint implicito: si algo falla a mitad de camino -- por ejemplo
--    en api_facturar, despues de descontar el stock y antes de insertar
--    la factura -- se deshace TODO lo de ese bloque y la aplicacion
--    recibe ok = false. Sin el, quedaria stock descontado sin factura.
--
-- Y una advertencia sobre ese mismo bloque, que va en el informe: el
-- WHEN OTHERS atrapa TODO, incluidos los errores que no son de negocio
-- (permisos, disco lleno, tabla inexistente). El contrato se cumple --
-- la app nunca ve una excepcion cruda -- pero un problema de
-- infraestructura llega disfrazado de rechazo de negocio. Se resuelve en
-- la aplicacion: SQLERRM se registra en el log y al usuario se le muestra
-- un mensaje genérico, nunca el texto crudo (delata nombres de tablas).
-- ======================================================================

-- ----------------------------------------------------------------------
-- 1. api_agendar_cita
-- ----------------------------------------------------------------------
CREATE OR REPLACE FUNCTION api_agendar_cita(p_id_mascota INT,
                                            p_id_veterinario INT,
                                            p_fecha_hora TIMESTAMP)
RETURNS TABLE (ok BOOLEAN, mensaje TEXT, id_generado INT)
LANGUAGE plpgsql
AS $fn$
DECLARE
  v_activa  CHAR(1);
  v_ocupado INT;
  v_id      INT;
BEGIN
  -- Existencia. SELECT ... INTO deja FOUND en falso si no hubo fila, y
  -- por eso aqui SI sirve IF NOT FOUND.
  SELECT activa INTO v_activa FROM mascota WHERE id_mascota = p_id_mascota;
  IF NOT FOUND THEN
    RETURN QUERY SELECT FALSE, 'La mascota no existe', NULL::INT;
    RETURN;                      -- <-- sin este RETURN la funcion sigue
  END IF;

  -- Regla de negocio: mascota inactiva no agenda.
  IF v_activa <> 'S' THEN
    RETURN QUERY SELECT FALSE, 'La mascota esta inactiva', NULL::INT;
    RETURN;
  END IF;

  -- Franja libre. OJO: esto es codigo, no una restriccion. Con dos
  -- sesiones concurrentes las dos pueden contar 0 y las dos insertar --
  -- es el write skew de la Clase 10. La mitigacion real es el indice
  -- unico parcial uq_cita_vet_franja; esta validacion solo da un mensaje
  -- amable en el caso secuencial.
  SELECT COUNT(*) INTO v_ocupado
    FROM cita
   WHERE id_veterinario = p_id_veterinario
     AND fecha_hora     = p_fecha_hora
     AND estado        <> 'CANCELADA';
  IF v_ocupado > 0 THEN
    RETURN QUERY SELECT FALSE, 'Franja ocupada', NULL::INT;
    RETURN;
  END IF;

  INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, estado)
  VALUES (p_id_mascota, p_id_veterinario, p_fecha_hora, 'PROGRAMADA')
  RETURNING id_cita INTO v_id;   -- el id que la app necesita para el paso siguiente

  RETURN QUERY SELECT TRUE, 'Cita agendada', v_id;
EXCEPTION WHEN OTHERS THEN
  RETURN QUERY SELECT FALSE, SQLERRM, NULL::INT;
END;
$fn$;

-- ----------------------------------------------------------------------
-- 2. api_registrar_consulta
-- ----------------------------------------------------------------------
CREATE OR REPLACE FUNCTION api_registrar_consulta(p_id_cita INT,
                                                  p_diagnostico TEXT,
                                                  p_precio NUMERIC)
RETURNS TABLE (ok BOOLEAN, mensaje TEXT, id_generado INT)
LANGUAGE plpgsql
AS $fn$
DECLARE
  v_estado TEXT;
  v_id     INT;
BEGIN
  SELECT estado INTO v_estado FROM cita WHERE id_cita = p_id_cita;
  IF NOT FOUND THEN
    RETURN QUERY SELECT FALSE, 'La cita no existe', NULL::INT;
    RETURN;
  END IF;

  IF v_estado = 'CANCELADA' THEN
    RETURN QUERY SELECT FALSE, 'La cita esta cancelada', NULL::INT;
    RETURN;
  END IF;

  -- Esta validacion tiene red de seguridad: consulta.id_cita es UNIQUE en
  -- el DDL. Si dos sesiones pasaran el EXISTS al mismo tiempo, la segunda
  -- chocaria contra el indice unico, el WHEN OTHERS lo atraparia y la app
  -- recibiria ok = false. Es el patron correcto: la restriccion garantiza,
  -- el EXISTS solo mejora el mensaje.
  IF EXISTS (SELECT 1 FROM consulta WHERE id_cita = p_id_cita) THEN
    RETURN QUERY SELECT FALSE, 'La cita ya tiene consulta', NULL::INT;
    RETURN;
  END IF;

  -- p_precio IS NULL primero: NULL <= 0 no es falso, es NULL, y un IF con
  -- condicion NULL no entra. Sin la comprobacion explicita, un precio
  -- nulo se colaria hasta el CHECK de la tabla.
  IF p_precio IS NULL OR p_precio <= 0 THEN
    RETURN QUERY SELECT FALSE, 'Precio invalido', NULL::INT;
    RETURN;
  END IF;

  INSERT INTO consulta (id_cita, diagnostico, precio)
  VALUES (p_id_cita, p_diagnostico, p_precio)
  RETURNING id_consulta INTO v_id;

  UPDATE cita SET estado = 'ATENDIDA' WHERE id_cita = p_id_cita;

  RETURN QUERY SELECT TRUE, 'Consulta registrada', v_id;
EXCEPTION WHEN OTHERS THEN
  RETURN QUERY SELECT FALSE, SQLERRM, NULL::INT;
END;
$fn$;

-- ----------------------------------------------------------------------
-- 3. api_facturar
-- ----------------------------------------------------------------------
CREATE OR REPLACE FUNCTION api_facturar(p_id_consulta INT,
                                        p_id_insumo INT,
                                        p_cantidad INT)
RETURNS TABLE (ok BOOLEAN, mensaje TEXT, id_generado INT)
LANGUAGE plpgsql
AS $fn$
DECLARE
  v_precio NUMERIC(12,2);
  v_filas  INT;
  v_id     INT;
BEGIN
  IF NOT EXISTS (SELECT 1 FROM consulta WHERE id_consulta = p_id_consulta) THEN
    RETURN QUERY SELECT FALSE, 'La consulta no existe', NULL::INT;
    RETURN;
  END IF;

  IF p_cantidad IS NULL OR p_cantidad <= 0 THEN
    RETURN QUERY SELECT FALSE, 'Cantidad invalida', NULL::INT;
    RETURN;
  END IF;

  SELECT precio_unit INTO v_precio FROM insumo WHERE id_insumo = p_id_insumo;
  IF NOT FOUND THEN
    RETURN QUERY SELECT FALSE, 'El insumo no existe', NULL::INT;
    RETURN;
  END IF;

  -- El corazon de la funcion, y es el patron de la Clase 10: la condicion
  -- del stock va en el WHERE, no en un IF previo. Asi la comprobacion y
  -- el descuento son UNA operacion y no hay ventana entre las dos. Si no
  -- hay stock, el UPDATE afecta 0 filas y no toca nada.
  UPDATE insumo
     SET stock = stock - p_cantidad
   WHERE id_insumo = p_id_insumo
     AND stock    >= p_cantidad;
  GET DIAGNOSTICS v_filas = ROW_COUNT;   -- no existe SQL%ROWCOUNT aqui
  IF v_filas = 0 THEN
    RETURN QUERY SELECT FALSE, 'Stock insuficiente', NULL::INT;
    RETURN;
  END IF;

  -- De aqui en adelante el stock ya bajo. Si alguno de los dos INSERT
  -- fallara, el bloque EXCEPTION deshace tambien el descuento: eso es lo
  -- que hace atomica la operacion completa.
  INSERT INTO factura (id_consulta, total)
  VALUES (p_id_consulta, v_precio * p_cantidad)
  RETURNING id_factura INTO v_id;

  INSERT INTO detalle_factura (id_factura, id_insumo, cantidad, precio_unit)
  VALUES (v_id, p_id_insumo, p_cantidad, v_precio);

  RETURN QUERY SELECT TRUE, 'Factura generada', v_id;
EXCEPTION WHEN OTHERS THEN
  RETURN QUERY SELECT FALSE, SQLERRM, NULL::INT;
END;
$fn$;

-- ======================================================================
-- LAS SEIS LLAMADAS QUE DEMUESTRAN EL CONTRATO
--
-- Todas con SELECT * FROM ..., y no es capricho: una funcion
-- RETURNS TABLE se consume en el FROM. Un CALL api_agendar_cita(...)
-- falla con "api_agendar_cita(...) is not a procedure", porque CALL es
-- para procedimientos.
--
-- Ninguna de las seis lanza error. Tres devuelven ok = true y tres
-- ok = false, y esa es toda la idea: la aplicacion siempre recibe una
-- fila que puede leer igual.
-- ======================================================================
SELECT * FROM api_agendar_cita(1, 2, TIMESTAMP '2026-10-01 09:00:00');   -- ok = true
SELECT * FROM api_agendar_cita(3, 2, TIMESTAMP '2026-10-01 10:00:00');   -- Rocky inactiva
SELECT * FROM api_registrar_consulta(1, 'Vacunacion anual', 45000);      -- ok = true
SELECT * FROM api_registrar_consulta(4, 'Revision', 30000);              -- cita 4 CANCELADA
SELECT * FROM api_facturar(1, 6, 2);                                     -- ok = true
SELECT * FROM api_facturar(1, 2, 10);                                    -- insumo 2 tiene 3

-- ======================================================================
-- VERIFICACION: que quedo en la base, que es lo que se proyecta
-- ======================================================================
-- La cita nueva, y el estado de la cita 1. Ojo al detalle: la llamada 3
-- registro la consulta de la cita 1, NO de la cita 11. Las seis llamadas
-- del enunciado no forman una cadena.
SELECT id_cita, id_mascota, id_veterinario, fecha_hora, estado
  FROM cita
 WHERE id_cita IN (1, 11)
 ORDER BY id_cita;

-- La consulta nueva es la 5, sobre la cita 1.
SELECT id_consulta, id_cita, diagnostico, precio
  FROM consulta
 ORDER BY id_consulta;

-- El insumo 6 bajo de 60 a 58; el 2 sigue en 3, intacto. El CHECK
-- (stock >= 0) nunca se activo: lo que protegio fue el WHERE del UPDATE.
-- El CHECK es la red por si alguien escribe mal el procedimiento.
SELECT id_insumo, nombre, stock FROM insumo WHERE id_insumo IN (2, 6) ORDER BY id_insumo;

-- La factura nueva con su unico detalle, y el total cuadrado.
SELECT f.id_factura, f.id_consulta, f.total,
       d.id_insumo, d.cantidad, d.precio_unit,
       d.cantidad * d.precio_unit AS suma_detalle
  FROM factura f
  JOIN detalle_factura d ON d.id_factura = f.id_factura
 WHERE f.id_factura = 4;

-- ======================================================================
-- DOS LIMITES DE ESTA API QUE VAN AL INFORME, NO SE OCULTAN
--
-- a) api_facturar cobra UNA linea por llamada, como pide el enunciado
--    "para simplificar". La consecuencia real: una visita con tres
--    insumos produce TRES facturas, no una factura con tres lineas. Por
--    eso factura 4 queda sobre la consulta 1, que ya tenia la factura 1.
--    El modelo lo permite (consulta 1-N factura) y de paso explica por
--    que estas facturas si cuadran: cada una tiene un solo detalle. La
--    version util para el negocio recibe arrays -- como el sp_facturar
--    de la Clase 8 -- y crea una sola factura con N detalles.
--
-- b) La validacion de franja de api_agendar_cita no resiste concurrencia,
--    por la razon de la Clase 10: un SELECT COUNT(*) no toma candado y no
--    puede tomarlo, porque la fila en conflicto todavia no existe. Lo
--    tranquilizador es que la API ya esta preparada para la mitigacion:
--    al agregar el indice unico parcial uq_cita_vet_franja, la segunda
--    sesion recibe unique_violation, el WHEN OTHERS lo atrapa y la app
--    ve un ok = false normal. O sea que la restriccion no rompe el
--    contrato: lo completa.
-- ======================================================================""",
                "salida": """Las seis llamadas, una fila cada una y ningun error:

  ok  |         mensaje          | id_generado
------+--------------------------+-------------
 t    | Cita agendada            |          11
 f    | La mascota esta inactiva |      (null)
 t    | Consulta registrada      |           5
 f    | La cita esta cancelada   |      (null)
 t    | Factura generada         |           4
 f    | Stock insuficiente       |      (null)

Tres exitos y tres rechazos, y cero excepciones: eso es el contrato. Fijate en
que los tres rechazos devuelven id_generado en NULL -- no en 0, no en -1 -- y
que ese detalle esta documentado en la pregunta 5.

Estado de cita 1 y 11 -- 2 filas

 id_cita | id_mascota | id_veterinario |     fecha_hora      |   estado
---------+------------+----------------+---------------------+------------
       1 |          1 |              1 | 2026-09-01 08:00:00 | ATENDIDA
      11 |          1 |              2 | 2026-10-01 09:00:00 | PROGRAMADA

Aqui esta la sorpresa que hay que explicar: la cita **1** paso a ATENDIDA y la
**11** sigue PROGRAMADA. La tercera llamada del enunciado es
api_registrar_consulta(1, ...), o sea sobre la cita 1, no sobre la que se acabo
de crear. Las seis llamadas son seis casos de prueba independientes, no un flujo
encadenado -- el flujo encadenado es lo que se arma en la pregunta 2 con
flujo_atencion, que si pasa el id_generado de un paso al siguiente.

consulta -- 5 filas

 id_consulta | id_cita |        diagnostico        |  precio
-------------+---------+---------------------------+----------
           1 |       2 | Vacunacion triple felina  | 40000.00
           2 |       5 | Control de peso           | 38000.00
           3 |       7 | Otitis externa            | 55000.00
           4 |      10 | Desparasitacion           | 35000.00
           5 |       1 | Vacunacion anual          | 45000.00

insumo -- 2 filas

 id_insumo |        nombre        | stock
-----------+----------------------+-------
         2 | Vacuna triple felina |     3
         6 | Jeringa 5ml          |    58

El 6 bajo de 60 a 58 (dos jeringas). El 2 sigue en 3: el UPDATE condicional
afecto 0 filas y no toco nada. El CHECK (stock >= 0) nunca se activo, y eso es
lo correcto -- el CHECK es la red por si el procedimiento esta mal escrito, no
el mecanismo de todos los dias.

factura 4 con su detalle -- 1 fila

 id_factura | id_consulta |  total  | id_insumo | cantidad | precio_unit | suma_detalle
------------+-------------+---------+-----------+----------+-------------+--------------
          4 |           1 | 1800.00 |         6 |        2 |      900.00 |      1800.00

total = suma_detalle. Compara con lo que encontro la Clase 11: las facturas
historicas 1, 2 y 3 estan descuadradas y esta cuadra al centavo. La diferencia
es que esta la creo una funcion y aquellas las cargo alguien a mano.

Y un dato para la pregunta 5: los tres rechazos NO consumieron secuencia,
porque los tres devuelven antes de llegar a su INSERT. Por eso la cita nueva es
la 11 y no la 13. La secuencia solo se quema cuando el INSERT se intenta y
falla, que es lo que paso en la Clase 11.""",
                "como_calificar": [
                    "**12 pts — las tres funciones con el contrato exacto,** 4 pts cada una. 1,5 "
                    "pts la firma con `RETURNS TABLE (ok BOOLEAN, mensaje TEXT, id_generado INT)` "
                    "**literal** —cambiar un nombre de columna rompe el contrato que la pregunta 5 "
                    "documenta y la pregunta 2 consume—; 1,5 pts las validaciones propias de cada "
                    "una; 1 pt el `RETURNING ... INTO` que devuelve el id generado.",
                    "**6 pts — el bloque `EXCEPTION WHEN OTHERS THEN RETURN QUERY SELECT FALSE, "
                    "SQLERRM, NULL::INT;` en las tres,** 2 pts cada una. Es lo que garantiza que la "
                    "aplicacion **nunca** reciba una excepcion cruda, y es requisito literal del "
                    "enunciado. Se reconoce como sobresaliente explicar el efecto secundario "
                    "valioso: el bloque abre un savepoint implicito, asi que si `api_facturar` "
                    "falla despues de descontar el stock, el descuento se deshace. **Sin `EXCEPTION` "
                    "la funcion no es atomica.**",
                    "**4 pts — el `RETURN;` desnudo detras de cada `RETURN QUERY` de rechazo.** Es "
                    "el punto tecnico que decide la pregunta y conviene calificarlo aparte. "
                    "`RETURN QUERY` **no** termina la funcion: agrega filas y sigue. Sin el "
                    "`RETURN;`, `api_agendar_cita(3, ...)` devuelve **dos filas** —una `false` y "
                    "una `true`— y **agenda la cita de la mascota inactiva**. La forma de "
                    "detectarlo al calificar es contar filas: cada llamada tiene que devolver "
                    "exactamente 1.",
                    "**4 pts — `api_facturar` con el `UPDATE` condicional y `GET DIAGNOSTICS ... "
                    "ROW_COUNT`.** 2 pts que la condicion del stock este **en el `WHERE`** y no en "
                    "un `IF` previo, y 2 pts el `GET DIAGNOSTICS` con el `IF v_filas = 0`. Es "
                    "requisito literal de la rubrica y es la conclusion de la Clase 10: cuando la "
                    "condicion cabe en el `WHERE`, va en el `WHERE`.",
                    "**2 pts — las seis llamadas con `SELECT * FROM ...`,** todas devolviendo fila "
                    "y ninguna lanzando error, con los valores esperados: `11`, rechazo por "
                    "inactiva, `5`, rechazo por cancelada, `4`, rechazo por stock. Un `CALL` en vez "
                    "de `SELECT` falla con «is not a procedure» y cuesta estos 2 pts.",
                    "**Se reconoce como sobresaliente, sin puntos extra:** notar que la llamada 3 "
                    "opera sobre la cita **1** y no sobre la 11 recien creada, asi que las seis "
                    "llamadas son casos independientes y no un flujo; ver que los tres rechazos "
                    "**no** queman secuencia porque devuelven antes del `INSERT`; o dejar escrito "
                    "que `api_facturar` produce una factura por llamada y que por eso una visita "
                    "con tres insumos generaria tres facturas.",
                ],
                "errores": [
                    "**Omitir el `RETURN;` despues de un `RETURN QUERY` de rechazo.** Es el error "
                    "mas grave del taller y el mas facil de pasar por alto, porque «funciona»: la "
                    "primera fila dice `false` y el estudiante se queda tranquilo. Lo que en "
                    "realidad ocurre es que la funcion sigue y **hace el `INSERT`**, de modo que la "
                    "mascota inactiva **si** queda agendada. El sintoma es visible: la llamada "
                    "devuelve **dos** filas. Al devolverlo conviene pedir "
                    "`SELECT COUNT(*) FROM api_agendar_cita(3, 2, ...)`.",
                    "**Usar `IF NOT FOUND` despues de `SELECT COUNT(*) INTO`.** Nunca entra, porque "
                    "un `COUNT` siempre devuelve una fila aunque valga 0. Es el mismo error que "
                    "aparecio en la Clase 8 y sigue vivo. La franja se comprueba con "
                    "`IF v_ocupado > 0`.",
                    "**Comprobar el stock con un `IF` antes del `UPDATE`:** "
                    "`SELECT stock INTO v_stock ...; IF v_stock >= p_cantidad THEN UPDATE ...`. Da "
                    "el mismo resultado en ExamLab y es el patron inseguro que la Clase 10 "
                    "desmonto: entre el `SELECT` y el `UPDATE` hay una ventana. Cuesta los 2 pts "
                    "del `WHERE` aunque la salida sea identica.",
                    "**Cambiar los nombres del contrato:** `exito` por `ok`, `msg` por `mensaje`, "
                    "`id` por `id_generado`. Rompe la pregunta 2 —el `SELECT ok, mensaje, "
                    "id_generado FROM ...` deja de compilar— y rompe el documento de la pregunta 5. "
                    "El contrato se llama contrato precisamente porque no se negocia.",
                    "**Olvidar `p_precio IS NULL` en `api_registrar_consulta`.** `NULL <= 0` no es "
                    "falso: es `NULL`, y un `IF` con condicion nula no entra. El precio nulo se "
                    "cuela hasta el `NOT NULL` de la tabla, salta como excepcion, el `WHEN OTHERS` "
                    "la atrapa y la aplicacion recibe un mensaje del motor en ingles en vez del "
                    "«Precio invalido» del contrato. Funciona, pero el mensaje ya no es el "
                    "documentado.",
                    "**Llamar las funciones con `CALL`.** Falla con «is not a procedure»: `CALL` es "
                    "para procedimientos, y una funcion `RETURNS TABLE` se consume en el `FROM`. "
                    "Aparece por arrastre de la Clase 8, donde todo era `CALL sp_*`.",
                    "**Declarar una variable con el mismo nombre que una columna del "
                    "`RETURNS TABLE`** —por ejemplo `DECLARE mensaje TEXT;`—. PostgreSQL responde "
                    "«column reference “mensaje” is ambiguous» y el error no dice donde. La "
                    "convencion `v_` para variables locales, que el curso viene usando desde la "
                    "Clase 4, existe justamente para esto.",
                ],
            },
            {
                "n": 2,
                "titulo": "El cliente de la aplicacion: consumir la API con parametros ligados",
                "tipo": "codigo",
                "puntos": 17,
                "respuesta": (
                    "Esta pregunta **no se ejecuta**: se califica leyendo el codigo. Y lo que se "
                    "lee son cuatro cosas concretas —parametros ligados sin excepcion, el "
                    "`dataclass` que traduce el contrato, `commit`/`rollback` gobernados por `ok`, "
                    "y el corte en el primer rechazo—. Una decision de diseno que conviene "
                    "explicar antes del codigo: **las tres funciones delegan en un unico helper "
                    "`_llamar`**. El enunciado pide `with conn.cursor()` y captura de "
                    "`psycopg2.Error` en cada operacion, y ponerlo tres veces seria copiar y pegar "
                    "el mismo `try` con la misma decision de transaccion; concentrarlo en un lugar "
                    "significa que **hay un solo sitio donde se ejecuta SQL en todo el archivo**, y "
                    "eso es exactamente lo que hace auditable el requisito de «ningun `INSERT` "
                    "directo»: se revisa una funcion, no tres. Las dos formas se aceptan.\n\n"
                    "```python\n"
                    '"""Capa de acceso a datos de la app VetCare (Huellitas).\n'
                    "\n"
                    "Regla del PI: la app NUNCA hace INSERT/UPDATE/DELETE directo sobre\n"
                    "cita, consulta ni factura. Solo invoca las funciones api_*.\n"
                    '"""\n'
                    "import os\n"
                    "from dataclasses import dataclass\n"
                    "\n"
                    "import psycopg2\n"
                    "\n"
                    "\n"
                    "@dataclass\n"
                    "class Resultado:\n"
                    "    ok: bool\n"
                    "    mensaje: str\n"
                    "    id_generado: int | None\n"
                    "\n"
                    "\n"
                    "# Las tres sentencias de la capa. Son constantes con marcadores %s: el\n"
                    "# texto del SQL nunca depende de los datos del usuario, y por eso no hay\n"
                    "# forma de inyectar nada.\n"
                    "_SQL_AGENDAR = (\n"
                    '    "SELECT ok, mensaje, id_generado "\n'
                    '    "FROM api_agendar_cita(%s, %s, %s)"\n'
                    ")\n"
                    "_SQL_CONSULTA = (\n"
                    '    "SELECT ok, mensaje, id_generado "\n'
                    '    "FROM api_registrar_consulta(%s, %s, %s)"\n'
                    ")\n"
                    "_SQL_FACTURAR = (\n"
                    '    "SELECT ok, mensaje, id_generado "\n'
                    '    "FROM api_facturar(%s, %s, %s)"\n'
                    ")\n"
                    "\n"
                    "\n"
                    "def _llamar(conn, sql: str, params: tuple) -> Resultado:\n"
                    '    """Unico punto del modulo donde se ejecuta SQL.\n'
                    "\n"
                    "    Traduce el contrato (ok, mensaje, id_generado) de la base al\n"
                    "    Resultado de la aplicacion y decide la transaccion: se confirma\n"
                    "    solo si la base dijo ok; en cualquier otro caso se deshace.\n"
                    '    """\n'
                    "    try:\n"
                    "        with conn.cursor() as cur:\n"
                    "            cur.execute(sql, params)   # <- parametros ligados, siempre\n"
                    "            fila = cur.fetchone()\n"
                    "    except psycopg2.Error as exc:\n"
                    "        # Falla de infraestructura: la funcion no llego a responder.\n"
                    "        conn.rollback()\n"
                    "        # El texto crudo va al log, no a la pantalla del usuario.\n"
                    '        print(f"[ERROR BD] {exc}")\n'
                    "        return Resultado(\n"
                    "            False,\n"
                    '            "No fue posible completar la operacion. Intenta de nuevo.",\n'
                    "            None,\n"
                    "        )\n"
                    "\n"
                    "    if fila is None:\n"
                    "        # No deberia pasar: las api_* siempre devuelven una fila. Si\n"
                    "        # pasa, el contrato esta roto y hay que enterarse.\n"
                    "        conn.rollback()\n"
                    '        return Resultado(False, "La API no devolvio fila", None)\n'
                    "\n"
                    "    ok, mensaje, id_generado = fila\n"
                    "    if ok:\n"
                    "        conn.commit()\n"
                    "    else:\n"
                    "        conn.rollback()\n"
                    "    return Resultado(bool(ok), mensaje, id_generado)\n"
                    "\n"
                    "\n"
                    "def agendar_cita(conn, id_mascota: int, id_veterinario: int,\n"
                    "                 fecha_hora) -> Resultado:\n"
                    "    return _llamar(conn, _SQL_AGENDAR,\n"
                    "                   (id_mascota, id_veterinario, fecha_hora))\n"
                    "\n"
                    "\n"
                    "def registrar_consulta(conn, id_cita: int, diagnostico: str,\n"
                    "                       precio) -> Resultado:\n"
                    "    return _llamar(conn, _SQL_CONSULTA, (id_cita, diagnostico, precio))\n"
                    "\n"
                    "\n"
                    "def facturar(conn, id_consulta: int, id_insumo: int,\n"
                    "             cantidad: int) -> Resultado:\n"
                    "    return _llamar(conn, _SQL_FACTURAR,\n"
                    "                   (id_consulta, id_insumo, cantidad))\n"
                    "\n"
                    "\n"
                    "def flujo_atencion(conn, id_mascota, id_veterinario, fecha_hora,\n"
                    "                   diagnostico, precio, id_insumo,\n"
                    "                   cantidad) -> Resultado:\n"
                    '    """Caso de uso completo: agendar -> registrar consulta -> facturar.\n'
                    "\n"
                    "    Corta en el primer ok = False y devuelve ese Resultado, que ya trae\n"
                    "    el mensaje que se le muestra al usuario. Cada paso recibe el\n"
                    "    id_generado del anterior: para eso existe esa columna del contrato.\n"
                    '    """\n'
                    "    r_cita = agendar_cita(conn, id_mascota, id_veterinario, fecha_hora)\n"
                    "    if not r_cita.ok:\n"
                    "        return r_cita\n"
                    "\n"
                    "    r_consulta = registrar_consulta(conn, r_cita.id_generado,\n"
                    "                                    diagnostico, precio)\n"
                    "    if not r_consulta.ok:\n"
                    "        return r_consulta\n"
                    "\n"
                    "    return facturar(conn, r_consulta.id_generado, id_insumo, cantidad)\n"
                    "\n"
                    "\n"
                    "def _conectar():\n"
                    '    """Credenciales por variables de entorno, nunca en el codigo."""\n'
                    "    return psycopg2.connect(\n"
                    '        host=os.environ.get("VETCARE_HOST", "localhost"),\n'
                    '        dbname=os.environ.get("VETCARE_DB", "vetcare"),\n'
                    '        user=os.environ["VETCARE_USER"],\n'
                    '        password=os.environ["VETCARE_PASSWORD"],\n'
                    "    )\n"
                    "\n"
                    "\n"
                    "def _mostrar(titulo: str, r: Resultado) -> None:\n"
                    '    etiqueta = "OK" if r.ok else "RECHAZADO"\n'
                    '    print(f"{titulo}\\n  [{etiqueta}] {r.mensaje} (id={r.id_generado})")\n'
                    "\n"
                    "\n"
                    'if __name__ == "__main__":\n'
                    "    conn = _conectar()\n"
                    "    try:\n"
                    "        _mostrar(\n"
                    '            "Caso exitoso: Firulais (mascota 1) con Diego Moreno (vet 2)",\n'
                    "            flujo_atencion(conn, 1, 2, \"2026-10-01 09:00:00\",\n"
                    '                           "Vacunacion anual", 45000, 6, 2),\n'
                    "        )\n"
                    "        _mostrar(\n"
                    '            "Caso rechazado: Rocky (mascota 3) esta inactiva",\n'
                    "            flujo_atencion(conn, 3, 2, \"2026-10-01 10:00:00\",\n"
                    '                           "Revision general", 30000, 6, 1),\n'
                    "        )\n"
                    "    finally:\n"
                    "        conn.close()\n"
                    "```\n\n"
                    "**Lo que imprime el bloque `main`,** que es lo que el enunciado pide "
                    "mostrar:\n\n"
                    "```\n"
                    "Caso exitoso: Firulais (mascota 1) con Diego Moreno (vet 2)\n"
                    "  [OK] Factura generada (id=4)\n"
                    "Caso rechazado: Rocky (mascota 3) esta inactiva\n"
                    "  [RECHAZADO] La mascota esta inactiva (id=None)\n"
                    "```\n\n"
                    "**Tres cosas que conviene senalar al revisar.** La primera es la que mas se "
                    "malinterpreta: en el caso exitoso el mensaje final es «Factura generada», no "
                    "«Cita agendada», porque `flujo_atencion` devuelve el `Resultado` del **ultimo** "
                    "paso. Si la interfaz necesita mostrar el numero de cita, hay que guardarlo "
                    "durante el recorrido —o devolver los tres resultados—; es una limitacion "
                    "real del diseno y se documenta en lugar de disimularse. La segunda: en el "
                    "caso rechazado el `id_generado` llega como `None` y no como `0`, porque la "
                    "base devuelve `NULL::INT` y `psycopg2` lo traduce a `None`; por eso el "
                    "`dataclass` declara `int | None`. La tercera: el `except psycopg2.Error` "
                    "**no** le muestra el texto del error al usuario. Ese texto puede decir "
                    "«permission denied for table cita» y estaria delatando nombres de tablas y "
                    "fallas de configuracion a quien esta al otro lado de la pantalla; va al log y "
                    "al usuario se le da un mensaje generico.\n\n"
                    "*Nota tecnica:* `int | None` en una anotacion requiere Python 3.10 o "
                    "superior, igual que el `starter` que entrega la plataforma. En una version "
                    "anterior se escribe `Optional[int]` con `from typing import Optional`."
                ),
                "como_calificar": [
                    "**5 pts — parametros ligados en las tres funciones, sin una sola excepcion.** "
                    "El SQL tiene que ser una cadena constante con `%s` y los valores viajar en la "
                    "tupla del segundo argumento de `execute`. **Una sola f-string o una "
                    "concatenacion con `+` o `%` dentro del SQL cuesta los 5 pts completos**, "
                    "aunque el resto del archivo sea impecable: es la puerta de la inyeccion y el "
                    "enunciado la prohibe con esa palabra. Se descuenta igual "
                    "`cur.execute(sql % params)`, que es concatenacion disfrazada.",
                    "**3 pts — el `dataclass Resultado` traduciendo el contrato.** 2 pts que las "
                    "tres funciones devuelvan `Resultado` y no la tupla cruda de `fetchone()`, y 1 "
                    "pt que el tipo sea `int | None` (u `Optional[int]`) porque un rechazo trae "
                    "`NULL` y `psycopg2` lo entrega como `None`. Devolver la tupla directa cuesta "
                    "los 2 pts: la aplicacion quedaria atada a la posicion de las columnas.",
                    "**3 pts — `commit` / `rollback` gobernados por `ok`,** mas "
                    "`with conn.cursor() as cur:` y `except psycopg2.Error`. Se acepta que esto "
                    "viva en un helper compartido —es mejor diseno— o repetido en cada funcion, "
                    "que es lo que sugiere el enunciado. Lo que **no** se acepta es confirmar "
                    "siempre, ni dejar la transaccion abierta cuando `ok` es falso.",
                    "**3 pts — `flujo_atencion` cortando en el primer `ok = False`.** 2 pts el "
                    "corte con retorno inmediato y 1 pt que cada paso reciba el `id_generado` del "
                    "anterior —`registrar_consulta(conn, r_cita.id_generado, ...)`—, que es la "
                    "razon de ser de esa columna del contrato. Un `flujo_atencion` que ejecuta los "
                    "tres pasos y despues revisa vale 1 de 3: facturaria una consulta que no "
                    "existe.",
                    "**2 pts — ningun `INSERT`, `UPDATE` ni `DELETE` directo a `cita`, `consulta` o "
                    "`factura` en todo el archivo.** Se verifica buscando esas cuatro palabras en "
                    "el codigo; la unica sentencia permitida es `SELECT ... FROM api_*`. Es la "
                    "regla de oro del PI y se califica de forma binaria.",
                    "**1 pt — el bloque `if __name__ == \"__main__\":` con un caso exitoso y uno "
                    "rechazado,** imprimiendo el mensaje que veria el usuario final. Se reconoce "
                    "como sobresaliente que las credenciales vengan de variables de entorno y no "
                    "escritas en el archivo, y que el caso rechazado sea el de la mascota inactiva "
                    "que pide el enunciado.",
                    "**Se reconoce como sobresaliente, sin puntos extra:** notar que en el caso "
                    "exitoso el mensaje que llega es «Factura generada» y no «Cita agendada», "
                    "porque `flujo_atencion` devuelve el ultimo paso; o no mostrarle al usuario el "
                    "texto de `psycopg2.Error`, que puede delatar nombres de tablas.",
                ],
                "errores": [
                    "**Cualquier f-string o concatenacion en el SQL:** "
                    "`cur.execute(f\"SELECT * FROM api_agendar_cita({id_mascota}, ...)\")`. Es el "
                    "error mas costoso de la pregunta y aparece porque «se ve mas corto». Con un "
                    "campo de texto —el diagnostico— basta para que un usuario cierre la cadena y "
                    "agregue su propia sentencia. Al devolverlo conviene mostrar el ejemplo "
                    "concreto con un `'); DROP TABLE cita; --` en el diagnostico.",
                    "**Confundir marcadores:** usar `?` (que es de SQLite) o `:nombre` (que es de "
                    "SQLAlchemy y de Oracle) en vez de `%s`. `psycopg2` usa `%s` para **todos** los "
                    "tipos, tambien para cadenas y fechas, y **sin comillas alrededor**: escribir "
                    "`'%s'` convierte el marcador en un literal y rompe la consulta.",
                    "**Hacer `commit()` siempre, o no hacer `rollback()` cuando `ok` es falso.** "
                    "Con estas tres funciones el dano es limitado porque el rechazo no escribe "
                    "nada, pero deja la transaccion abierta y la siguiente operacion hereda un "
                    "estado que nadie previo. La regla del contrato es directa: **la transaccion la "
                    "decide `ok`.**",
                    "**Un `flujo_atencion` que no corta.** Ejecuta los tres pasos y revisa al "
                    "final, o ignora el `id_generado` y pasa el parametro original. Si agendar "
                    "falla, `r_cita.id_generado` es `None` y `registrar_consulta(conn, None, ...)` "
                    "sale con «La cita no existe»: dos mensajes de error por una sola causa, y el "
                    "usuario ve el equivocado.",
                    "**Devolver la tupla de `fetchone()` en vez del `Resultado`.** Obliga a toda la "
                    "aplicacion a recordar que `ok` es la posicion 0, y el dia que la base agregue "
                    "una cuarta columna al contrato hay que tocar cada pantalla. El `dataclass` es "
                    "requisito del enunciado, no un adorno.",
                    "**Dejar usuario y contrasena escritos en el archivo,** aunque sea "
                    "`password=\"1234\"` en una demo. Es lo que despues llega a un repositorio "
                    "publico y ademas contradice toda la pregunta 4: no tiene sentido montar "
                    "privilegio minimo y publicar la credencial. Variables de entorno o un archivo "
                    "de configuracion fuera del control de versiones.",
                    "**Mostrarle al usuario el `SQLERRM` o el texto de `psycopg2.Error`.** Aparece "
                    "como «para que se entienda mejor» y es una fuga de informacion: esos mensajes "
                    "traen nombres de tablas, de restricciones y a veces la consulta completa. Al "
                    "log el texto crudo, a la pantalla un mensaje generico.",
                ],
            },
            {
                "n": 3,
                "titulo": "Flujo app → BD del caso de uso «atender una mascota»",
                "tipo": "diagrama",
                "puntos": 12,
                "respuesta": (
                    "El diagrama tiene una sola tarea: **dejar visible que la aplicacion no toca "
                    "las tablas.** Si un jurado ve una flecha que va de `APP` a `DB`, toda la "
                    "arquitectura de la clase se cae en esa lamina, y por eso la rubrica dice "
                    "literalmente que «se descuenta si el diagrama muestra a la aplicacion "
                    "escribiendo directamente en las tablas». La regla de dibujo que lo garantiza: "
                    "**`APP` solo habla con `API`, y solo `API` habla con `DB`.**\n\n"
                    "El `alt` / `else` es la otra pieza que se califica, y conviene entender por "
                    "que importa tanto en un diagrama que parece una formalidad: sin la rama, el "
                    "diagrama cuenta el camino feliz, que es justo el que nunca da problemas. Lo "
                    "que hay que poder mostrar es el corte —cuando `ok = false`, la aplicacion "
                    "muestra el mensaje y **se detiene**—, porque es el comportamiento que "
                    "`flujo_atencion` implementa en la pregunta 2 y el que la pregunta 5 documenta "
                    "como accion de interfaz. El diagrama, el codigo y el contrato tienen que "
                    "contar la misma historia.\n\n"
                    "El modelo de abajo usa **dos** `alt` anidados: uno para el rechazo al agendar "
                    "y otro para el rechazo al facturar por stock, porque son los dos rechazos que "
                    "se demuestran en vivo en la sustentacion. Un solo `alt` en el nivel superior "
                    "**cumple la rubrica completa**; el segundo es un extra que ayuda en la demo. "
                    "Lo unico no negociable es que renderice: se pega en ExamLab, se comprueba que "
                    "salga el dibujo, y solo entonces se entrega."
                ),
                "respuesta_mermaid": """sequenceDiagram
    actor R as Recepcionista
    participant APP as App VetCare
    participant API as Capa api_* (PL/pgSQL)
    participant DB as Tablas VetCare
    Note over APP,API: Regla del PI: la app NUNCA hace INSERT/UPDATE directo.<br/>Solo tiene EXECUTE de api_* y SELECT de lectura.
    R->>APP: Agendar cita para Firulais con Diego Moreno
    APP->>API: SELECT * FROM api_agendar_cita($1, $2, $3)
    Note right of APP: Parametros ligados,<br/>nunca concatenados
    API->>DB: Valida mascota activa y franja libre
    DB-->>API: activa = S, franja libre
    API->>DB: INSERT cita ... RETURNING id_cita
    DB-->>API: id_cita = 11
    API-->>APP: (ok=true, 'Cita agendada', 11)
    alt ok = false
        APP-->>R: Muestra el mensaje y ofrece otra franja
        Note over APP,API: Corte: no se llama al paso siguiente
    else ok = true
        APP-->>R: Cita 11 confirmada
        R->>APP: Registrar la atencion del veterinario
        APP->>API: SELECT * FROM api_registrar_consulta($1, $2, $3)
        API->>DB: INSERT consulta + UPDATE cita a ATENDIDA
        DB-->>API: id_consulta = 5
        API-->>APP: (ok=true, 'Consulta registrada', 5)
        R->>APP: Cobrar los insumos utilizados
        APP->>API: SELECT * FROM api_facturar($1, $2, $3)
        API->>DB: UPDATE insumo SET stock = stock - n WHERE stock >= n
        DB-->>API: filas afectadas
        alt Sin stock (0 filas)
            API-->>APP: (ok=false, 'Stock insuficiente', null)
            APP-->>R: Deshabilita cobrar y avisa faltante
        else Con stock
            API->>DB: INSERT factura + detalle_factura
            DB-->>API: id_factura = 4
            API-->>APP: (ok=true, 'Factura generada', 4)
            APP-->>R: Factura impresa
        end
    end
    Note over API,DB: El bloque EXCEPTION de cada api_* hace atomico el paso:<br/>si algo falla, se deshace todo y llega ok = false""",
                "como_calificar": [
                    "**3 pts — que renderice sin errores y esten los cuatro participantes:** la "
                    "recepcionista, la aplicacion, la capa `api_*` y las tablas. Un diagrama que no "
                    "renderiza vale 0 en la pregunta completa, porque el entregable es una lamina "
                    "de la sustentacion. Se acepta `actor` o `participant` para la recepcionista.",
                    "**4 pts — las tres invocaciones `api_*` con sus parametros y el retorno del "
                    "contrato,** algo mas de 1,3 pts cada una. La flecha de ida tiene que nombrar "
                    "la funcion y la de vuelta tiene que traer las **tres** columnas —`(ok, "
                    "mensaje, id_generado)`—, no un «responde OK». Mostrar el `id_generado` "
                    "concreto (11, 5, 4) es lo que deja ver que el flujo se encadena.",
                    "**3 pts — el bloque `alt` / `else` que representa el corte cuando `ok` es "
                    "falso.** 2 pts la estructura y 1 pt que en la rama de error se vea que la "
                    "aplicacion **no continua**. Un `alt` en el nivel superior cumple la rubrica "
                    "completa; los anidados son un extra que no da mas puntos y si añade riesgo de "
                    "que no renderice.",
                    "**2 pts — la nota `Note over` con la regla del PI:** la aplicacion no hace "
                    "`INSERT` directo. Se reconoce como mejor version la que ademas dice **por "
                    "que** es cierto —solo tiene `EXECUTE` de `api_*` y `SELECT` de lectura—, "
                    "porque conecta esta lamina con la pregunta 4.",
                    "**Se descuenta hasta el total de la pregunta si aparece una flecha de `APP` a "
                    "`DB`.** Es requisito literal de la rubrica y no es una formalidad: esa flecha "
                    "contradice la arquitectura que el estudiante acaba de construir, y es lo "
                    "primero que un jurado va a mirar. La regla de dibujo: `APP` solo habla con "
                    "`API`, y solo `API` habla con `DB`.",
                    "**Se reconoce como sobresaliente, sin puntos extra:** anotar que "
                    "`api_facturar` descuenta el stock de forma atomica —con el `UPDATE` "
                    "condicional visible en la flecha—, o dejar una nota sobre el bloque "
                    "`EXCEPTION` que hace atomico cada paso.",
                ],
                "errores": [
                    "**La flecha de `APP` directo a `DB`.** Es el error que la rubrica castiga por "
                    "nombre y aparece casi siempre por comodidad de dibujo, no por convencimiento. "
                    "Vale la pena senalarlo con la pregunta que hara el jurado: «entonces, ¿para "
                    "que sirve la capa `api_*`?».",
                    "**Un diagrama sin `alt`, solo con el camino feliz.** Cuenta la mitad de la "
                    "historia, y la mitad que sobra: el camino feliz nunca es el que genera "
                    "soporte. Ademas contradice el `flujo_atencion` de la pregunta 2, que existe "
                    "precisamente para cortar.",
                    "**Flechas de retorno que dicen «OK» o «responde bien» en vez del contrato.** "
                    "Toda la clase gira alrededor de que la respuesta son **tres** columnas "
                    "siempre; si el diagrama no las muestra, no esta documentando la integracion "
                    "que la pregunta 5 va a entregar por escrito.",
                    "**Un diagrama que no renderiza.** Casi siempre por un `alt` mal cerrado —falta "
                    "un `end`— o por un `Note` con un salto de linea literal en vez de `<br/>`. "
                    "Cada `alt` necesita su `end`, y si hay anidados, los `end` van en orden "
                    "inverso. La comprobacion cuesta cinco segundos y evita perder los 12 pts.",
                    "**Usar un `flowchart` o un `graph TD` en vez de `sequenceDiagram`.** El "
                    "enunciado pide un diagrama de secuencia y no es un detalle de sintaxis: lo que "
                    "se quiere mostrar es **el orden temporal y quien llama a quien**, y un grafo "
                    "de cajas no lo dice.",
                    "**Poner a la recepcionista hablando con `API`.** La recepcionista usa una "
                    "pantalla; la que invoca funciones es la aplicacion. Parece un detalle y no lo "
                    "es: el diagrama tiene que reflejar que la persona nunca tiene credenciales de "
                    "base de datos.",
                ],
            },
            {
                "n": 4,
                "titulo": "Blindar la API: la aplicacion solo puede EXECUTE",
                "tipo": "bd_sql",
                "puntos": 13,
                "sql": """-- ======================================================================
-- 1. El rol de la aplicacion
-- NOLOGIN porque no es una persona ni un servicio que se conecte por si
-- mismo: es el conjunto de permisos que despues se le otorga al usuario
-- real de la aplicacion con GRANT app_vetcare TO usuario_app. Separar el
-- rol de permisos del usuario que se conecta es lo que permite rotar
-- credenciales sin volver a repartir privilegios.
-- ======================================================================
CREATE ROLE app_vetcare NOLOGIN;

-- ======================================================================
-- 2. Cerrar la puerta grande
-- Redundante hoy -- a app_vetcare nunca se le otorgo nada -- y aun asi se
-- escribe, porque un script de permisos tiene que poder leerse como la
-- DECISION de diseno y no solo como su efecto. El dia que alguien haga un
-- GRANT ALL de apuro, esta linea al reejecutar el script lo revierte.
--
-- Es normal que PostgreSQL responda "WARNING: no privileges could be
-- revoked for ..." una vez por tabla: esta avisando que no habia nada que
-- quitar, que es exactamente lo que se queria confirmar. No es un error y
-- el script sigue.
-- ======================================================================
REVOKE INSERT, UPDATE, DELETE
    ON cita, consulta, factura, detalle_factura, insumo
  FROM app_vetcare;

-- ======================================================================
-- 3. EL PUNTO QUE CASI TODOS OLVIDAN
-- En PostgreSQL, una funcion recien creada queda con EXECUTE otorgado a
-- PUBLIC. O sea que sin este REVOKE, CUALQUIER rol de la base puede
-- llamar api_facturar y cobrarle a un cliente. El GRANT del paso 4 no
-- sirve de nada mientras PUBLIC siga teniendo el privilegio: no se le
-- esta dando acceso a app_vetcare, se le esta quitando a todos los demas.
--
-- La firma tiene que ir COMPLETA y con los tipos exactos, porque las
-- funciones se identifican por nombre + tipos de argumentos. Un
-- REVOKE ... ON FUNCTION api_facturar(INT, INT) falla con "function
-- api_facturar(integer, integer) does not exist".
-- ======================================================================
REVOKE EXECUTE ON FUNCTION api_agendar_cita(INT, INT, TIMESTAMP)   FROM PUBLIC;
REVOKE EXECUTE ON FUNCTION api_registrar_consulta(INT, TEXT, NUMERIC) FROM PUBLIC;
REVOKE EXECUTE ON FUNCTION api_facturar(INT, INT, INT)             FROM PUBLIC;

-- ======================================================================
-- 4. Otorgar EXECUTE solo al rol de la aplicacion
-- ======================================================================
GRANT EXECUTE ON FUNCTION api_agendar_cita(INT, INT, TIMESTAMP)      TO app_vetcare;
GRANT EXECUTE ON FUNCTION api_registrar_consulta(INT, TEXT, NUMERIC) TO app_vetcare;
GRANT EXECUTE ON FUNCTION api_facturar(INT, INT, INT)                TO app_vetcare;

-- ======================================================================
-- 5. Solo la lectura que necesita para pintar pantallas
-- Cuatro tablas y ni una mas. Notese lo que NO esta: consulta, factura,
-- detalle_factura e insumo. La aplicacion no lee precios ni stock
-- directamente; lo que necesite de ahi se lo devuelve una funcion, y asi
-- la lista de precios no se puede extraer con un SELECT.
-- ======================================================================
GRANT SELECT ON dueno, mascota, veterinario, cita TO app_vetcare;

-- ======================================================================
-- 6. Verificacion
-- ======================================================================
SELECT grantee, routine_name, privilege_type
  FROM information_schema.routine_privileges
 WHERE routine_name LIKE 'api_%'
 ORDER BY routine_name, grantee;

SELECT grantee, table_name, privilege_type
  FROM information_schema.role_table_grants
 WHERE grantee = 'app_vetcare'
 ORDER BY table_name, privilege_type;

-- ======================================================================
-- 7. LA PRUEBA NEGATIVA (esto va mas alla de lo que pide el enunciado y
--    es lo mas valioso de la pregunta, porque destapa un hueco real)
--
-- Un privilegio no esta probado hasta que se comprueba que estorba. Y a
-- diferencia de la concurrencia de la Clase 10, esto SI se puede
-- verificar con una sola conexion: un superusuario puede ponerse la piel
-- de cualquier rol con SET ROLE, incluso de uno NOLOGIN.
-- ======================================================================
SET ROLE app_vetcare;

SELECT current_user;                                   -- app_vetcare

SELECT id_mascota, nombre, activa FROM mascota WHERE id_mascota = 1;  -- funciona

-- La puerta grande, cerrada. Tiene que fallar.
INSERT INTO cita (id_mascota, id_veterinario, fecha_hora)
VALUES (1, 3, TIMESTAMP '2026-10-02 09:00:00');
-- ERROR: permission denied for table cita

-- Y ahora la sorpresa: la puerta autorizada tampoco sirve.
SELECT * FROM api_agendar_cita(1, 3, TIMESTAMP '2026-10-02 09:00:00');
-- (f, 'permission denied for table cita', null)

RESET ROLE;

-- ======================================================================
-- POR QUE FALLA LA API Y COMO SE ARREGLA
--
-- Las funciones se crearon con SECURITY INVOKER, que es el valor por
-- omision: la funcion corre con los privilegios de QUIEN LA LLAMA. Y
-- app_vetcare solo tiene SELECT, asi que el INSERT INTO cita de adentro
-- se rechaza. El EXCEPTION WHEN OTHERS lo atrapa y lo devuelve como si
-- fuera un rechazo de negocio -- el contrato se cumple, la aplicacion no
-- ve una excepcion cruda, y precisamente por eso el problema puede vivir
-- meses sin que nadie lo note.
--
-- Para que el diseno de esta pregunta funcione hace falta SECURITY
-- DEFINER: la funcion corre con los privilegios de su PROPIETARIO, que si
-- puede escribir. Eso es lo que permite que la app tenga EXECUTE y nada
-- mas. Y va acompanado obligatoriamente de fijar el search_path: una
-- funcion SECURITY DEFINER con search_path abierto se puede enganar
-- creando una tabla "cita" en un esquema que aparezca antes.
-- ======================================================================
ALTER FUNCTION api_agendar_cita(INT, INT, TIMESTAMP)
  SECURITY DEFINER SET search_path = public, pg_temp;
ALTER FUNCTION api_registrar_consulta(INT, TEXT, NUMERIC)
  SECURITY DEFINER SET search_path = public, pg_temp;
ALTER FUNCTION api_facturar(INT, INT, INT)
  SECURITY DEFINER SET search_path = public, pg_temp;

-- Ahora si: mismo rol, misma llamada, resultado distinto.
SET ROLE app_vetcare;
SELECT * FROM api_agendar_cita(1, 3, TIMESTAMP '2026-10-02 09:00:00');
-- (t, 'Cita agendada', 11)

-- Y la puerta grande sigue cerrada, que es el punto: la app puede hacer
-- el negocio y no puede hacer nada mas.
INSERT INTO cita (id_mascota, id_veterinario, fecha_hora)
VALUES (1, 3, TIMESTAMP '2026-10-02 11:00:00');
-- ERROR: permission denied for table cita

RESET ROLE;

-- ======================================================================
-- POR QUE ESTE ESQUEMA HACE IMPOSIBLE SALTARSE LAS VALIDACIONES
--
-- -- La aplicacion no tiene INSERT, UPDATE ni DELETE sobre ninguna tabla
-- -- de negocio, asi que el UNICO camino que le queda para modificar
-- -- datos son las tres funciones api_*, y cada una de ellas ejecuta sus
-- -- validaciones antes de escribir. No es que la app "deba" validar: es
-- -- que no tiene forma fisica de escribir sin pasar por la validacion.
-- -- Un bug de la aplicacion, un desarrollador nuevo que no leyo el
-- -- contrato o incluso una inyeccion SQL exitosa terminan igual --
-- -- "permission denied" --, porque el permiso vive en la base y no en el
-- -- codigo que se puede olvidar de llamar.
-- ======================================================================""",
                "salida": """routine_privileges -- 6 filas

   grantee   |      routine_name      | privilege_type
-------------+------------------------+----------------
 app_vetcare | api_agendar_cita       | EXECUTE
 postgres    | api_agendar_cita       | EXECUTE
 app_vetcare | api_facturar           | EXECUTE
 postgres    | api_facturar           | EXECUTE
 app_vetcare | api_registrar_consulta | EXECUTE
 postgres    | api_registrar_consulta | EXECUTE

Dos filas por funcion y las dos son correctas: app_vetcare porque se le acaba de
otorgar, y el propietario porque un propietario conserva EXECUTE sobre lo suyo.
El nombre del propietario depende del entorno -- en ExamLab suele ser postgres --
y no es lo que se califica. Lo que se califica es que **PUBLIC ya no aparece**:
antes del REVOKE habia una fila con el grantee vacio o PUBLIC por cada funcion, y
esa era la puerta abierta.

role_table_grants para app_vetcare -- 4 filas

   grantee   | table_name  | privilege_type
-------------+-------------+----------------
 app_vetcare | cita        | SELECT
 app_vetcare | dueno       | SELECT
 app_vetcare | mascota     | SELECT
 app_vetcare | veterinario | SELECT

Cuatro filas, las cuatro SELECT, y aqui esta el detalle mas fino de la pregunta:
**la evidencia del REVOKE de escritura es una ausencia.** No hay ninguna fila que
diga "INSERT revocado"; lo que prueba el blindaje es que en estas 4 filas no
aparece ni un INSERT, ni un UPDATE, ni un DELETE, y que consulta, factura,
detalle_factura e insumo no aparecen en absoluto. Al calificar se cuenta: 4 filas
exactas. Si salen 5 o mas, algo se otorgo de mas.

Prueba negativa con SET ROLE -- lo que de verdad cierra la pregunta

 current_user
--------------
 app_vetcare

 id_mascota |  nombre  | activa
------------+----------+--------
          1 | Firulais | S

INSERT INTO cita ...
ERROR:  permission denied for table cita

SELECT * FROM api_agendar_cita(1, 3, TIMESTAMP '2026-10-02 09:00:00');
  ok |               mensaje                | id_generado
-----+--------------------------------------+-------------
 f   | permission denied for table cita     |      (null)

Ese ultimo resultado es el hallazgo de la clase y hay que detenerse en el. La
aplicacion no recibio una excepcion -- el contrato funciono perfectamente -- y
justo por eso el problema es peligroso: la interfaz mostraria "permission denied
for table cita" como si fuera un mensaje de negocio, al lado de "La mascota esta
inactiva". Nadie abre un ticket por eso. La causa es que las funciones son
SECURITY INVOKER (el valor por omision) y corren con los privilegios de quien
llama.

Despues de ALTER FUNCTION ... SECURITY DEFINER SET search_path = public, pg_temp:

SELECT * FROM api_agendar_cita(1, 3, TIMESTAMP '2026-10-02 09:00:00');
  ok |    mensaje    | id_generado
-----+---------------+-------------
 t   | Cita agendada |          11

INSERT INTO cita ...
ERROR:  permission denied for table cita

Y ese par de resultados es la arquitectura completa en dos lineas: la aplicacion
**puede hacer el negocio** y **no puede hacer nada mas**. El id 11 es el que
corresponde en una base recien sembrada; si en tu corrida sale 12, es porque el
intento rechazado alcanzo a pedir el nextval antes del chequeo de permisos. El
numero no es lo que se califica.

Sobre el WARNING del paso 2: es esperable ver una vez por tabla
  WARNING:  no privileges could be revoked for "cita"
porque a app_vetcare nunca se le habia otorgado nada. Es informativo, no es un
error, y el script continua.""",
                "como_calificar": [
                    "**2 pts — `CREATE ROLE app_vetcare NOLOGIN;`.** Se reconoce como "
                    "sobresaliente explicar por que `NOLOGIN`: el rol es el paquete de permisos, no "
                    "la credencial; el usuario real se conecta y recibe el paquete con "
                    "`GRANT app_vetcare TO usuario_app`, y asi la contrasena se puede rotar sin "
                    "volver a repartir privilegios.",
                    "**2 pts — el `REVOKE INSERT, UPDATE, DELETE` sobre las cinco tablas de "
                    "negocio.** Se otorga aunque sea redundante, porque el enunciado lo pide como "
                    "evidencia explicita de la decision. Si el estudiante lo omite «porque no hacia "
                    "falta», se descuentan los 2 pts y se le senala que un script de permisos se "
                    "lee como la decision de diseno, no solo como su efecto.",
                    "**4 pts — el `REVOKE EXECUTE ... FROM PUBLIC` de las tres funciones con su "
                    "firma exacta.** Es el punto de mas peso de la pregunta porque es el que casi "
                    "todos olvidan, y sin el, el `GRANT` del paso siguiente no protege nada: **una "
                    "funcion recien creada trae `EXECUTE` para `PUBLIC`**, asi que cualquier rol de "
                    "la base puede llamar `api_facturar`. Se descuenta 1 pt por cada firma "
                    "incompleta o con tipos que no corresponden: las funciones se identifican por "
                    "nombre mas tipos de argumentos, y "
                    "`api_facturar(INT, INT)` no existe.",
                    "**2 pts — el `GRANT EXECUTE` de las tres solo a `app_vetcare`,** y **1,5 pts "
                    "el `GRANT SELECT` limitado a las cuatro tablas pedidas** —`dueno`, `mascota`, "
                    "`veterinario`, `cita`— y a nada mas. Un `GRANT SELECT ON ALL TABLES` cuesta "
                    "esos 1,5 pts completos: le entrega a la aplicacion la lista de precios y el "
                    "stock, que es justo lo que no debe poder leer.",
                    "**1,5 pts — las dos consultas de verificacion devolviendo filas coherentes:** "
                    "**6 filas** en `routine_privileges` —dos por funcion: `app_vetcare` y el "
                    "propietario— y **4 filas** en `role_table_grants`, todas `SELECT`. Se reconoce "
                    "como sobresaliente notar que **la evidencia del `REVOKE` de escritura es una "
                    "ausencia**: no hay fila que diga «revocado», lo que prueba el blindaje es que "
                    "no aparezca ningun `INSERT`/`UPDATE`/`DELETE` y que `PUBLIC` haya desaparecido.",
                    "**Los 13 pts requieren el comentario final de dos lineas** explicando por que "
                    "la aplicacion no puede saltarse las validaciones. La respuesta correcta no es "
                    "«porque la app siempre llama a las funciones» —eso es una promesa— sino "
                    "**«porque no tiene forma fisica de escribir sin pasar por ellas»**: el permiso "
                    "vive en la base, no en el codigo que alguien puede olvidar de invocar. Se "
                    "reconoce como sobresaliente cerrar con la consecuencia fuerte: hasta una "
                    "inyeccion SQL exitosa termina en «permission denied».",
                    "**Se reconoce como muy sobresaliente, sin puntos extra, la prueba negativa con "
                    "`SET ROLE app_vetcare`** y el descubrimiento de que **la API tampoco funciona** "
                    "por falta de `SECURITY DEFINER`. La rubrica no lo pide y por lo tanto no se "
                    "descuenta a nadie, pero quien llegue ahi resolvio el hueco de diseno de todo "
                    "el taller y tiene lista la respuesta a la pregunta mas probable del jurado.",
                ],
                "errores": [
                    "**Omitir el `REVOKE EXECUTE ... FROM PUBLIC`.** Es el error dominante y el "
                    "mas costoso: el estudiante hace el `GRANT` a `app_vetcare`, ve las filas de la "
                    "verificacion y concluye que blindo la API, cuando en realidad **cualquier rol "
                    "de la base sigue pudiendo facturar**. Se detecta mirando si `PUBLIC` aparece "
                    "todavia en `routine_privileges`.",
                    "**Firmas incompletas o con tipos equivocados en el `REVOKE` o el `GRANT`:** "
                    "`api_facturar(INT, INT)`, o `api_registrar_consulta(INT, VARCHAR, NUMERIC)` "
                    "cuando el parametro es `TEXT`. Falla con «function ... does not exist» y el "
                    "estudiante suele culpar al `REVOKE`. Las funciones se identifican por nombre "
                    "**mas** tipos de argumentos.",
                    "**`GRANT SELECT ON ALL TABLES IN SCHEMA public TO app_vetcare;`** en vez de "
                    "las cuatro tablas. Es mas rapido de escribir y contradice el objetivo entero: "
                    "le entrega a la aplicacion `insumo` —la lista de precios y el stock— y "
                    "`factura`. Se detecta contando filas en la segunda verificacion: tienen que "
                    "ser 4.",
                    "**Interpretar el `WARNING: no privileges could be revoked for \"cita\"` como "
                    "un fallo** y empezar a cambiar el script. Es informativo: avisa que no habia "
                    "nada que quitar, que es justo lo que se queria confirmar. El script sigue "
                    "corriendo.",
                    "**Dar `LOGIN` y contrasena al rol** «para poder probarlo». No hace falta y "
                    "empeora la postura de seguridad: con `SET ROLE` se prueba desde la misma "
                    "sesion, sin crear una credencial mas que despues hay que administrar.",
                    "**Un comentario final que promete en vez de explicar:** «la app no se puede "
                    "saltar las validaciones porque siempre usa las funciones». Eso es una "
                    "convencion de equipo, y las convenciones se rompen con un desarrollador nuevo. "
                    "Lo que se pide es el argumento de imposibilidad: sin `INSERT`, no hay camino.",
                    "**Concluir que la pregunta esta cerrada sin haber intentado usar la API como "
                    "`app_vetcare`.** No cuesta puntos, pero deja pasar el hueco de "
                    "`SECURITY INVOKER`: el rol tiene todos los permisos que el enunciado pide y "
                    "aun asi **no puede agendar una cita**. Vale la pena mostrarlo en clase, porque "
                    "es la diferencia entre configurar permisos y verificarlos.",
                ],
            },
            {
                "n": 5,
                "titulo": "Contrato de integracion app ↔ BD",
                "tipo": "abierta",
                "puntos": 18,
                "tabla": {
                    "headers": ["Funcion", "`mensaje` devuelto", "Causa", "Accion de la interfaz"],
                    "rows": [
                        ["`api_agendar_cita`", "`La mascota no existe`",
                         "El `id_mascota` no esta en la tabla",
                         "Error de programacion o dato viejo en pantalla: recargar la lista de "
                         "mascotas y registrar el caso en el log. **No** se le pide al usuario que "
                         "reintente"],
                        ["`api_agendar_cita`", "`La mascota esta inactiva`",
                         "`mascota.activa = 'N'`",
                         "Aviso claro —«Rocky esta inactivo»— y ofrecer el boton de reactivar, que "
                         "es otra operacion con su propio permiso. Deshabilitar «Agendar» mientras "
                         "siga inactiva"],
                        ["`api_agendar_cita`", "`Franja ocupada`",
                         "Ese veterinario ya tiene una cita no cancelada a esa hora",
                         "Mostrar las tres franjas libres mas cercanas del mismo veterinario. Es "
                         "el rechazo mas frecuente y el que mas se gana con una buena interfaz"],
                        ["`api_registrar_consulta`", "`La cita no existe`",
                         "`id_cita` invalido; casi siempre porque el paso anterior devolvio "
                         "`id_generado` en `NULL` y la app lo paso igual",
                         "Cortar el flujo y registrar el caso: es un defecto de la aplicacion, no "
                         "del usuario. Es exactamente lo que `flujo_atencion` evita cortando en el "
                         "primer `ok = false`"],
                        ["`api_registrar_consulta`", "`La cita esta cancelada`",
                         "`cita.estado = 'CANCELADA'`",
                         "Aviso y ofrecer agendar una cita nueva. No se «revive» una cita "
                         "cancelada: se crea otra, para que la historia quede completa"],
                        ["`api_registrar_consulta`", "`La cita ya tiene consulta`",
                         "Existe una consulta con ese `id_cita` (`UNIQUE` en el DDL)",
                         "**Es la respuesta esperada ante un reintento por timeout.** La interfaz "
                         "debe mostrar la consulta existente en vez de un error, y para eso "
                         "necesita poder recuperar su id: ver la seccion de idempotencia"],
                        ["`api_registrar_consulta`", "`Precio invalido`",
                         "`p_precio` nulo, cero o negativo",
                         "Validar tambien en el formulario para no gastar un viaje a la base, pero "
                         "**sin quitar** la validacion de la funcion: la del formulario es "
                         "comodidad, la de la base es la garantia"],
                        ["`api_facturar`", "`La consulta no existe`",
                         "`id_consulta` invalido, mismo patron que arriba",
                         "Cortar y registrar. Nunca ofrecer «reintentar cobro»"],
                        ["`api_facturar`", "`Cantidad invalida`",
                         "`p_cantidad` nula, cero o negativa",
                         "Control numerico con minimo 1 en la interfaz. Una cantidad negativa "
                         "seria una devolucion, y eso es otra operacion que hoy no existe"],
                        ["`api_facturar`", "`El insumo no existe`",
                         "`id_insumo` fuera de catalogo",
                         "Recargar el catalogo. Indica que la pantalla quedo abierta mientras "
                         "alguien cambio el inventario"],
                        ["`api_facturar`", "`Stock insuficiente`",
                         "El `UPDATE` condicional afecto 0 filas",
                         "**Deshabilitar el boton de cobrar** para ese insumo, mostrar el faltante "
                         "y ofrecer un sustituto. Reintentar tal cual **no** sirve: el stock no va "
                         "a aparecer solo"],
                        ["Las tres", "Cualquier texto en ingles del motor",
                         "Cayo en el `EXCEPTION WHEN OTHERS`: `unique_violation`, "
                         "`permission denied`, disco lleno, tabla inexistente",
                         "**Mensaje generico al usuario y el texto crudo al log.** Nunca se muestra "
                         "el `SQLERRM` en pantalla: delata nombres de tablas y de restricciones. "
                         "Si el texto empieza por `duplicate key`, se puede tratar como reintento "
                         "absorbido; si dice `permission denied`, es una alerta de operaciones, no "
                         "un aviso al usuario"],
                        ["Las tres", "*(sin mensaje: cero filas)*",
                         "El contrato esta roto —normalmente falta un `RETURN;` detras de un "
                         "`RETURN QUERY`, o sobran filas—",
                         "Tratarlo como fallo duro y alertar. La aplicacion debe comprobar que "
                         "recibio **exactamente una** fila; dos filas significan que una funcion "
                         "hizo el `INSERT` que decia estar rechazando"],
                    ],
                },
                "respuesta": (
                    "### 1. `api_agendar_cita`\n\n"
                    "**Proposito.** Reservar una franja horaria de un veterinario para una mascota "
                    "activa, sin permitir que dos citas ocupen el mismo hueco.\n\n"
                    "**Firma e invocacion.** "
                    "`api_agendar_cita(p_id_mascota INT, p_id_veterinario INT, p_fecha_hora "
                    "TIMESTAMP)`. Se invoca como "
                    "`SELECT * FROM api_agendar_cita($1, $2, $3);` —en el `FROM`, porque es una "
                    "funcion `RETURNS TABLE`; un `CALL` falla—.\n\n"
                    "**Retorno.** `ok BOOLEAN` dice si la operacion se realizo. `mensaje TEXT` es "
                    "texto para el usuario cuando `ok` es verdadero o falso por regla de negocio, y "
                    "texto **del motor** cuando cayo en el manejador de excepciones. "
                    "`id_generado INT` trae el `id_cita` creado si `ok` es verdadero y **`NULL` "
                    "siempre que `ok` sea falso** —`NULL`, no `0` ni `-1`: el cliente debe "
                    "tipificarlo como nullable—.\n\n"
                    "**Precondiciones del llamador.** Los tres parametros no nulos; "
                    "`p_fecha_hora` como `TIMESTAMP` sin zona; el rol necesita `EXECUTE` de esta "
                    "funcion. No se exige que la mascota exista ni este activa: **eso lo valida la "
                    "funcion**, que es el punto de tener una API.\n\n"
                    "**Efectos si `ok` es verdadero.** Exactamente una fila nueva en `cita` con "
                    "`estado = 'PROGRAMADA'`. Nada mas. Si `ok` es falso, **cero** cambios, y "
                    "ademas los tres rechazos de negocio devuelven antes del `INSERT`, asi que "
                    "tampoco consumen la secuencia.\n\n"
                    "### 2. `api_registrar_consulta`\n\n"
                    "**Proposito.** Dejar constancia clinica de la atencion y marcar la cita como "
                    "atendida, en un solo paso indivisible.\n\n"
                    "**Firma e invocacion.** "
                    "`api_registrar_consulta(p_id_cita INT, p_diagnostico TEXT, p_precio NUMERIC)`; "
                    "`SELECT * FROM api_registrar_consulta($1, $2, $3);`.\n\n"
                    "**Retorno.** El mismo contrato. `id_generado` trae el `id_consulta`.\n\n"
                    "**Precondiciones.** `p_id_cita` debe venir del `id_generado` de "
                    "`api_agendar_cita` o de una consulta de lectura sobre `cita`; `p_precio` "
                    "mayor que 0. `p_diagnostico` puede ser nulo en la base, pero el contrato "
                    "**exige** que la aplicacion lo envie: una consulta sin diagnostico es una "
                    "historia clinica inservible.\n\n"
                    "**Efectos si `ok` es verdadero.** Dos cambios que van juntos o no van: una "
                    "fila nueva en `consulta` y `cita.estado` pasando a `'ATENDIDA'`. Es "
                    "atomico por el bloque `EXCEPTION`, no porque la aplicacion los pida "
                    "seguidos.\n\n"
                    "### 3. `api_facturar`\n\n"
                    "**Proposito.** Cobrar **un** insumo consumido en una consulta, descontando "
                    "inventario sin que el stock pueda quedar negativo.\n\n"
                    "**Firma e invocacion.** "
                    "`api_facturar(p_id_consulta INT, p_id_insumo INT, p_cantidad INT)`; "
                    "`SELECT * FROM api_facturar($1, $2, $3);`.\n\n"
                    "**Retorno.** El mismo contrato. `id_generado` trae el `id_factura`.\n\n"
                    "**Precondiciones.** `p_cantidad` mayor que 0. Y una advertencia que **tiene "
                    "que estar en el contrato porque cambia la interfaz**: esta version cobra una "
                    "linea por llamada, asi que una visita con tres insumos produce **tres "
                    "facturas**, no una factura con tres lineas. Es una simplificacion aceptada, no "
                    "un descuido, y la version con arrays —como el `sp_facturar` de la Clase 8— es "
                    "la que el negocio necesita.\n\n"
                    "**Efectos si `ok` es verdadero.** Tres cambios atomicos: "
                    "`insumo.stock` baja, una fila nueva en `factura` con "
                    "`total = precio_unit * cantidad`, y una fila nueva en `detalle_factura`. Si "
                    "`ok` es falso, cero cambios —incluido el caso en que el stock ya se habia "
                    "descontado y falla el `INSERT`, porque el `EXCEPTION` deshace el bloque "
                    "completo—.\n\n"
                    "---\n\n"
                    "### Idempotencia y reintentos: el veredicto honesto\n\n"
                    "**Ninguna de las tres operaciones es idempotente por diseno. Dos lo parecen "
                    "por accidente y la tercera es peligrosa.** El escenario a considerar es "
                    "concreto: la aplicacion llama, la base ejecuta y confirma, y la respuesta se "
                    "pierde en la red. El cliente no sabe si paso o no y vuelve a llamar.\n\n"
                    "- **`api_agendar_cita` — reintento absorbido, pero con el mensaje "
                    "equivocado.** El segundo intento encuentra la franja ocupada... **por la "
                    "propia cita del primer intento**, y devuelve «Franja ocupada». No se duplica "
                    "nada, que es lo importante, pero la aplicacion se queda sin el `id_cita` y el "
                    "usuario recibe un mensaje que suena a error ajeno cuando en realidad su cita "
                    "quedo agendada. Se salva por accidente, y el accidente es fragil: **solo "
                    "protege si el reintento usa el mismo veterinario y la misma hora exacta**.\n"
                    "- **`api_registrar_consulta` — reintento absorbido, y este si con red "
                    "estructural.** El segundo intento devuelve «La cita ya tiene consulta», y "
                    "detras de esa validacion hay un `UNIQUE` sobre `consulta.id_cita`, asi que la "
                    "proteccion no depende del `EXISTS`: aunque dos llamadas pasaran la validacion "
                    "a la vez, la segunda choca contra el indice. Mismo problema de siempre: no "
                    "devuelve el id de la consulta que ya existe.\n"
                    "- **`api_facturar` — NO es segura, y es la que cuesta dinero.** No hay nada "
                    "que impida dos facturas identicas: el segundo intento **descuenta el stock "
                    "otra vez y cobra otra vez**. Doble cargo al cliente y doble descuento de "
                    "inventario, sin ningun error visible. Es el unico de los tres casos donde el "
                    "reintento produce dano real y silencioso.\n\n"
                    "**Que se le agrega, concretamente.** Dos cambios, en este orden:\n\n"
                    "1. **Clave de idempotencia en `api_facturar`.** Un cuarto parametro "
                    "`p_clave_idem TEXT` que la aplicacion genera **una vez por intento de cobro** "
                    "—un UUID que sobrevive al reintento—, una columna "
                    "`factura.clave_idem TEXT UNIQUE` y esta logica: si la clave ya existe, la "
                    "funcion **no** cobra otra vez y devuelve "
                    "`(true, 'Factura ya generada', id_factura_existente)`. Asi el reintento es "
                    "seguro **y** util, porque la app recupera el id. Que la garantia sea un "
                    "`UNIQUE` y no un `IF` es deliberado: es la conclusion de la Clase 10.\n"
                    "2. **Devolver el id existente en vez de un error en las otras dos.** Cambiar "
                    "«La cita ya tiene consulta» por "
                    "`(true, 'La cita ya tenia consulta', id_consulta_existente)`, y lo equivalente "
                    "en agendar cuando la cita ocupada resulte ser de la misma mascota. Convierte "
                    "dos rechazos confusos en dos reintentos limpios.\n\n"
                    "Y un limite que se declara y no se disimula: **el hueco de concurrencia de "
                    "`api_agendar_cita` sigue abierto** mientras la franja se valide con un "
                    "`SELECT COUNT(*)`. La mitigacion esta identificada desde la Clase 10 —el "
                    "indice unico parcial `uq_cita_vet_franja`— y encaja sin tocar el contrato: la "
                    "segunda sesion recibiria `unique_violation`, el `EXCEPTION WHEN OTHERS` la "
                    "atrapa y la aplicacion ve un `ok = false` normal. Falta llevar el indice al "
                    "script del proyecto.\n\n"
                    "---\n\n"
                    "### Las dos reglas del contrato\n\n"
                    "> **Regla de acceso.** La aplicacion tiene `EXECUTE` de "
                    "`api_agendar_cita`, `api_registrar_consulta` y `api_facturar`, y `SELECT` "
                    "sobre `dueno`, `mascota`, `veterinario` y `cita`. **No** tiene `INSERT`, "
                    "`UPDATE` ni `DELETE` sobre ninguna tabla de negocio, y no se le otorgaran: "
                    "toda escritura entra por una funcion `api_*`. Si una operacion nueva hace "
                    "falta, se publica una funcion nueva; no se abre una tabla.\n\n"
                    "> **Regla de parametros.** Todo valor que provenga del usuario viaja como "
                    "parametro ligado —`%s` en `psycopg2`, `$1` en el SQL—. Queda **prohibido** "
                    "construir el texto de una sentencia concatenando datos, con `+`, con `%` o con "
                    "f-strings. El texto del SQL es una constante del programa; los datos son "
                    "argumentos.\n\n"
                    "*Nota para el docente:* el hueco de `SECURITY DEFINER` que aparece en la "
                    "pregunta 4 afecta a este documento. La regla de acceso, tal como esta escrita, "
                    "**solo es implementable** si las tres funciones son `SECURITY DEFINER` con "
                    "`search_path` fijado; con el `SECURITY INVOKER` por omision, un rol que solo "
                    "tiene `EXECUTE` y `SELECT` recibe `permission denied for table cita` desde "
                    "dentro de la funcion. Se acepta el contrato sin esa mencion —la rubrica no la "
                    "pide— y se reconoce como sobresaliente que aparezca."
                ),
                "como_calificar": [
                    "**9 pts — los siete puntos documentados para las tres operaciones,** 3 pts por "
                    "operacion. Dentro de cada una: 0,5 el proposito de negocio, 0,5 la firma "
                    "exacta con la forma de invocacion, 0,5 el contrato de retorno **incluido que "
                    "`id_generado` es `NULL` cuando `ok` es falso** —lo pide el enunciado con esas "
                    "palabras—, 0,5 las precondiciones, 1 los efectos en la base nombrando "
                    "**tablas y filas concretas**. «Inserta los datos» no vale: se pide «una fila "
                    "en `consulta` y `cita.estado` a `'ATENDIDA'`».",
                    "**3 pts — que las firmas coincidan exactamente con las funciones de la "
                    "pregunta 1.** Es el punto mas mecanico de calificar y el que mas revela: se "
                    "ponen los dos documentos uno al lado del otro. Un contrato que documenta "
                    "`api_facturar(id_consulta, arreglo_insumos)` cuando la funcion recibe tres "
                    "enteros no es un contrato, es un borrador.",
                    "**3 pts — la tabla de casos de rechazo cubriendo todos los mensajes que "
                    "devuelve el codigo,** con causa y accion de interfaz. Los mensajes explicitos "
                    "son **diez** —tres en agendar, cuatro en registrar consulta, cuatro en "
                    "facturar, y ese ultimo cuenta `El insumo no existe`— mas el caso del "
                    "`EXCEPTION WHEN OTHERS`. Se descuenta por acciones de interfaz que no son "
                    "acciones: «mostrar error» aparece once veces y no informa nada. Lo que se pide "
                    "es «deshabilitar el boton de cobrar», «ofrecer las tres franjas libres mas "
                    "cercanas», «recargar el catalogo».",
                    "**2 pts — la seccion de idempotencia con veredicto honesto y propuesta "
                    "concreta.** 1 pt el veredicto y 1 pt la propuesta. El veredicto correcto es "
                    "que **`api_facturar` no es segura ante reintentos** —cobra y descuenta dos "
                    "veces, sin error visible— y que las otras dos absorben el duplicado sin "
                    "haberlo buscado. Se acepta cualquier propuesta que funcione; la mas fuerte es "
                    "una clave de idempotencia con `UNIQUE` que **devuelva el id existente** en vez "
                    "de un error. Un «si, es idempotente» sin argumento vale 0 de los 2 pts.",
                    "**1 pt — las dos reglas de cierre redactadas en imperativo,** como pide la "
                    "rubrica. «Seria bueno usar parametros ligados» no es una regla; «todo valor "
                    "que provenga del usuario viaja como parametro ligado» si. Son las dos frases "
                    "que un desarrollador nuevo tiene que poder cumplir sin discutir.",
                    "**Se reconoce como sobresaliente, sin puntos extra:** declarar que "
                    "`api_facturar` produce **una factura por llamada**, con la consecuencia de que "
                    "una visita con tres insumos genera tres facturas; senalar que el hueco de "
                    "concurrencia de la franja sigue abierto y que el indice unico parcial encaja "
                    "sin tocar el contrato; o advertir que la regla de acceso **solo es "
                    "implementable** con `SECURITY DEFINER`.",
                ],
                "errores": [
                    "**Documentar la API que se queria y no la que se escribio.** Firmas con "
                    "parametros que no existen, arrays donde hay enteros, mensajes de rechazo "
                    "inventados. Es el error mas comun porque el documento se redacta de memoria. "
                    "Se detecta en un minuto poniendo la pregunta 1 al lado, y hace inservible el "
                    "documento para su unico proposito: que un equipo que nunca vio la base pueda "
                    "programar contra ella.",
                    "**Omitir que `id_generado` viene en `NULL` cuando `ok` es falso.** Es "
                    "requisito literal del enunciado y tiene consecuencia directa en el cliente: "
                    "quien lo tipifique como `int` no nulo se rompe en el primer rechazo. La "
                    "pregunta 2 lo declara `int | None` precisamente por esto.",
                    "**Una tabla de rechazos con «mostrar error» en las once filas.** No es una "
                    "accion de interfaz: es la ausencia de una. Cada mensaje habilita algo distinto "
                    "—sugerir franja, deshabilitar cobro, recargar catalogo, reactivar mascota, "
                    "cortar y alertar— y ese mapeo **es** el valor del documento.",
                    "**Declarar la API «idempotente» sin analizarla.** Suena bien y es falso donde "
                    "mas importa: dos llamadas a `api_facturar` cobran dos veces. El enunciado pide "
                    "honestidad explicita, asi que un «si» a la ligera cuesta los 2 pts y ademas es "
                    "el tipo de afirmacion que el jurado desmonta con una sola pregunta.",
                    "**Mostrarle el `SQLERRM` al usuario final** como accion de interfaz para el "
                    "caso del `EXCEPTION WHEN OTHERS`. Ese texto puede decir «permission denied for "
                    "table cita» o «duplicate key value violates unique constraint "
                    "uq_cita_vet_franja»: nombres de tablas y restricciones en pantalla. Al log el "
                    "texto crudo, a la pantalla un mensaje generico.",
                    "**Confundir precondiciones con validaciones.** Escribir «precondicion: la "
                    "mascota debe estar activa» invierte el diseno: si el llamador tuviera que "
                    "garantizarlo, la funcion no haria falta. La precondicion es lo que la funcion "
                    "**no** verifica —tipos, no nulos, permiso de `EXECUTE`—; lo demas es "
                    "responsabilidad de la API y hay que documentarlo como rechazo, no como "
                    "requisito.",
                    "**Reglas de cierre redactadas como recomendaciones.** «Se recomienda no "
                    "concatenar SQL» le deja la decision al desarrollador apurado. La rubrica pide "
                    "forma imperativa porque un contrato no sugiere: obliga.",
                ],
            },
            {
                "n": 6,
                "titulo": "Guion de la sustentacion (5 a 8 minutos)",
                "tipo": "abierta",
                "puntos": 12,
                "tabla": {
                    "headers": ["#", "Titulo de la diapositiva", "Que se muestra en pantalla",
                                "Quien habla", "Minutos"],
                    "rows": [
                        ["1", "Huellitas: el problema y hasta donde llegamos",
                         "Tres cifras de la clinica —8 mascotas, 10 citas, 4 consultas del corte de "
                         "prueba— y una frase de alcance: **agenda, historia clinica y "
                         "facturacion de insumos**. Lo que queda fuera, escrito: nomina, "
                         "proveedores y contabilidad",
                         "(el estudiante que sustenta)", "0,5"],
                        ["2", "El modelo que quedo",
                         "El `erDiagram` de la Clase 11 con las 9 entidades, `audit_cita` sin FK "
                         "resaltada, y una sola frase: «esto no es el modelo que planeamos, es el "
                         "que quedo»",
                         "(el estudiante que sustenta)", "1"],
                        ["3", "Las reglas y quien las hace cumplir",
                         "Tabla de 4 filas: regla · donde vive · como se probo. `stock >= 0` en un "
                         "`CHECK` + `UPDATE` condicional; mascota inactiva en `api_agendar_cita`; "
                         "auditoria en `trg_audit_cita`; franja unica en "
                         "`uq_cita_vet_franja`. La columna «como se probo» apunta a la bateria de "
                         "la Clase 11",
                         "(el estudiante que sustenta)", "1,5"],
                        ["4", "Demo: la app no puede escribir en las tablas",
                         "ExamLab en vivo con las 10 sentencias del guion de abajo. El momento "
                         "clave son las dos que **fallan a proposito** y el `stock` que **no se "
                         "movio**",
                         "(el estudiante que sustenta)", "2"],
                        ["5", "Rendimiento: antes y despues",
                         "Las dos capturas de `EXPLAIN (ANALYZE, BUFFERS)` de la Clase 6 lado a "
                         "lado: `Seq Scan` con `Rows Removed by Filter` arriba, `Index Cond` "
                         "abajo, con los dos tiempos reales. Debajo, los tres indices con una "
                         "linea de justificacion cada uno",
                         "(el estudiante que sustenta)", "1"],
                        ["6", "Seguridad, respaldo y lo que aprendimos",
                         "La matriz rol x objeto en tres filas, el `REVOKE ... FROM PUBLIC` "
                         "resaltado, el estado real del respaldo —**plan escrito, restore sin "
                         "ensayar**— y las dos lecciones: «una bateria donde todo pasa no verifico "
                         "nada» y «si la regla se puede declarar, se declara»",
                         "(el estudiante que sustenta)", "1"],
                    ],
                },
                "respuesta": (
                    "**Total: 7 minutos** —0,5 + 1 + 1,5 + 2 + 1 + 1—, dentro del rango de 5 a 8 "
                    "que pide el enunciado y con margen para las preguntas. La distribucion no es "
                    "uniforme a proposito: la diapositiva 4 se lleva casi un tercio del tiempo "
                    "porque es la unica donde se **demuestra** algo; las demas lo cuentan.\n\n"
                    "### Guion de la demo en vivo (diapositiva 4)\n\n"
                    "Diez sentencias en orden, sobre una base recien sembrada. Van pegadas en un "
                    "solo archivo y se ejecutan de arriba hacia abajo; nada se escribe en vivo.\n\n"
                    "```sql\n"
                    "-- 1. El escenario, en una linea. \"Firulais esta activo, Rocky no.\"\n"
                    "SELECT id_mascota, nombre, activa FROM mascota WHERE id_mascota IN (1, 3);\n"
                    "-- espera: 1 Firulais S | 3 Rocky N\n\n"
                    "-- 2. El camino feliz.\n"
                    "SELECT * FROM api_agendar_cita(1, 2, TIMESTAMP '2026-10-01 09:00:00');\n"
                    "-- espera: t | Cita agendada | 11\n\n"
                    "-- 3. FALLA A PROPOSITO: mascota inactiva.\n"
                    "SELECT * FROM api_agendar_cita(3, 2, TIMESTAMP '2026-10-01 10:00:00');\n"
                    "-- espera: f | La mascota esta inactiva | null   <- sin excepcion\n\n"
                    "-- 4. FALLA A PROPOSITO: la misma franja otra vez.\n"
                    "SELECT * FROM api_agendar_cita(1, 2, TIMESTAMP '2026-10-01 09:00:00');\n"
                    "-- espera: f | Franja ocupada | null\n\n"
                    "-- 5. Se encadena con el id que devolvio el paso 2.\n"
                    "SELECT * FROM api_registrar_consulta(11, 'Vacunacion anual', 45000);\n"
                    "-- espera: t | Consulta registrada | 5\n\n"
                    "-- 6. El stock antes de cobrar.\n"
                    "SELECT stock FROM insumo WHERE id_insumo = 2;   -- espera: 3\n\n"
                    "-- 7. FALLA A PROPOSITO: se piden 10 y hay 3.\n"
                    "SELECT * FROM api_facturar(5, 2, 10);\n"
                    "-- espera: f | Stock insuficiente | null\n\n"
                    "-- 8. LA SENTENCIA MAS IMPORTANTE DE LA DEMO.\n"
                    "SELECT stock FROM insumo WHERE id_insumo = 2;   -- espera: 3, sin moverse\n\n"
                    "-- 9. Cobro valido.\n"
                    "SELECT * FROM api_facturar(5, 6, 2);\n"
                    "-- espera: t | Factura generada | 4\n\n"
                    "-- 10. El total cuadra con su detalle.\n"
                    "SELECT f.id_factura, f.total, d.cantidad, d.precio_unit,\n"
                    "       d.cantidad * d.precio_unit AS suma_detalle\n"
                    "  FROM factura f JOIN detalle_factura d ON d.id_factura = f.id_factura\n"
                    " WHERE f.id_factura = 4;\n"
                    "-- espera: 4 | 1800.00 | 2 | 900.00 | 1800.00\n"
                    "```\n\n"
                    "**La frase que hay que decir en el paso 8,** porque es donde se gana la "
                    "sustentacion: «el cobro se rechazo y el inventario no se movio ni una "
                    "unidad; eso no lo garantiza el programa, lo garantiza el `UPDATE` "
                    "condicional». Y **si el tiempo aprieta, lo que se recorta es el paso 1 y el "
                    "paso 4** —el escenario se puede contar de palabra y un rechazo ya se mostro en "
                    "el 3—. Lo que **no** se recorta nunca es el par 7-8: es el unico momento en "
                    "que se ve una garantia funcionando.\n\n"
                    "### Plan B de la demo\n\n"
                    "Tres niveles, en este orden, y decididos **antes** de subir:\n\n"
                    "1. **Si una sentencia falla pero la base responde:** se pasa a la captura de "
                    "esa sentencia —`/demo/capturas/01.png` a `10.png`, numeradas igual que los "
                    "pasos— y se sigue en voz alta sin detenerse a depurar. Depurar en vivo consume "
                    "los dos minutos y deja las diapositivas 5 y 6 sin tiempo.\n"
                    "2. **Si la base no carga o no hay internet:** video de 90 segundos "
                    "(`/demo/demo.mp4`) con la corrida completa hecha la noche anterior, **en el "
                    "computador propio y descargado**, no en un enlace de nube.\n"
                    "3. **Si falla el proyector o el equipo:** las diez sentencias con su salida "
                    "impresas en una hoja, y la demo se cuenta. Es el peor caso y aun asi la "
                    "sustentacion se sostiene, porque el argumento no depende del espectaculo.\n\n"
                    "*Regla de oro del plan B:* se prueba el dia anterior en el equipo real y con "
                    "el proyector real si se puede. Un plan B que no se ensayo es exactamente el "
                    "item 12 del checklist de la Clase 11.\n\n"
                    "### Tres preguntas del jurado, con respuesta\n\n"
                    "**1. «Si la aplicacion solo tiene `EXECUTE`, ¿como escribe la funcion en las "
                    "tablas?»** *(la mas probable, y la que descubre el hueco)*\n\n"
                    "Con `SECURITY INVOKER`, que es el valor por omision, **no puede**: la funcion "
                    "corre con los privilegios de quien llama y el `INSERT` de adentro devuelve "
                    "«permission denied for table cita», que el `EXCEPTION WHEN OTHERS` disfraza de "
                    "rechazo de negocio. La correccion es "
                    "`ALTER FUNCTION api_* SECURITY DEFINER SET search_path = public, pg_temp`, "
                    "para que la funcion corra con los privilegios de su propietario; el "
                    "`search_path` fijo es obligatorio, porque una funcion `SECURITY DEFINER` con "
                    "el camino abierto se puede enganar. Lo verifique con `SET ROLE app_vetcare` "
                    "antes y despues.\n\n"
                    "**2. «¿Que pasa si dos recepcionistas agendan la misma franja al mismo "
                    "tiempo?»** *(concurrencia)*\n\n"
                    "Hoy se cuelan las dos. `api_agendar_cita` valida con un `SELECT COUNT(*)`, que "
                    "no toma candado y **no puede tomarlo**, porque la fila en conflicto todavia no "
                    "existe: es un write skew sobre un predicado. La mitigacion esta identificada y "
                    "probada en la Clase 10 —el indice unico parcial `uq_cita_vet_franja`— y encaja "
                    "sin tocar el contrato: la segunda sesion recibiria `unique_violation` y la "
                    "aplicacion veria un `ok = false` normal. Lo que falta es llevar el indice al "
                    "script del proyecto, y es el gap 2 de mi lista con fecha del 30 de octubre.\n\n"
                    "**3. «¿Probaron el restore?»** *(respaldo)*\n\n"
                    "No todavia, y prefiero decirlo: el plan esta escrito con RPO de 15 minutos y "
                    "RTO de 4 horas, pero esos dos numeros son estimaciones sin medir. Es el unico "
                    "item de mi checklist en `NO` y lo puse primero en la lista de cierre porque es "
                    "el unico irreversible: un respaldo roto se ve igual que uno bueno hasta el dia "
                    "en que se necesita. La prueba de aceptacion ya esta definida —correr la "
                    "bateria de verificacion sobre la base restaurada y confirmar el mismo "
                    "resultado— y la fecha es el 6 de noviembre.\n\n"
                    "### Checklist de empaquetado\n\n"
                    "```\n"
                    "vetcare-db-<apellido>.zip\n"
                    "  LEEME.md                      <- como correr todo, en 10 lineas\n"
                    "  db/\n"
                    "    01_ddl.sql                  <- tablas, PK, FK, CHECK\n"
                    "    02_procedimientos.sql       <- sp_* y fn_*\n"
                    "    03_roles.sql                <- roles y GRANT de tablas\n"
                    "    04_indices.sql              <- los tres indices justificados\n"
                    "    05_restricciones_concurrencia.sql  <- uq_cita_vet_franja\n"
                    "    06_api.sql                  <- las tres funciones api_*\n"
                    "    07_privilegios_api.sql      <- REVOKE FROM PUBLIC + GRANT EXECUTE\n"
                    "    08_datos_demo.sql           <- la siembra de la demo\n"
                    "  app/\n"
                    "    vetcare_datos.py            <- la capa de la pregunta 2\n"
                    "  informe/                      <- 01-modelo-er.md ... 14-orden-de-scripts.md\n"
                    "  demo/\n"
                    "    demo.sql                    <- las 10 sentencias en orden\n"
                    "    demo.mp4                    <- plan B nivel 2\n"
                    "    capturas/01.png ... 10.png  <- plan B nivel 1\n"
                    "```\n\n"
                    "**El orden de ejecucion es `01` a `08` y no es decorativo: hay una dependencia "
                    "real.** `07_privilegios_api.sql` tiene que ir **despues** de `06_api.sql`, "
                    "porque no se puede otorgar `EXECUTE` sobre una funcion que no existe —falla "
                    "con «function does not exist»—. Y `08_datos_demo.sql` va al final, porque "
                    "`05_restricciones_concurrencia.sql` crea un indice unico que fallaria si los "
                    "datos ya lo violaran. El `LEEME.md` dice esas dos cosas en una linea cada una. "
                    "Correr los ocho scripts de cero sobre una base vacia es el gap 6 de la lista "
                    "de la Clase 11, con fecha del 13 de noviembre: **el orden es una suposicion "
                    "hasta que se ejecuta.**"
                ),
                "como_calificar": [
                    "**4 pts — el storyboard de 6 filas con contenido real, responsable nombrado y "
                    "minutos que suman entre 5 y 8.** 3 pts las filas —0,5 cada una, y una fila "
                    "cuenta solo si la columna «que se muestra en pantalla» dice algo concreto: «el "
                    "`erDiagram` con `audit_cita` resaltada», no «el modelo»— y 1 pt la suma dentro "
                    "del rango. **La suma se verifica con la calculadora**: es el error mas facil de "
                    "cometer y el mas facil de detectar. Los seis temas obligatorios del enunciado "
                    "tienen que estar los seis.",
                    "**4 pts — el guion de la demo con sentencias exactas, en orden, y al menos un "
                    "fallo intencional con su resultado esperado.** 2 pts que las sentencias sean "
                    "**ejecutables tal como estan escritas** —no «llamar a la funcion de agendar»—, "
                    "1 pt el orden con el encadenamiento de ids, 1 pt el caso que falla a proposito "
                    "con lo que el publico debe ver. Se reconoce como sobresaliente incluir la "
                    "sentencia de **despues** del fallo —el `SELECT stock` que demuestra que no se "
                    "movio—, porque un rechazo sin esa comprobacion solo prueba que salio un "
                    "mensaje.",
                    "**1,5 pts — el plan B especifico.** «Tengo capturas» no alcanza: se pide que "
                    "diga **cuando** se usa cada nivel y **donde** estan los archivos. Se reconoce "
                    "como sobresaliente el plan de tres niveles —falla una sentencia / no carga la "
                    "base / falla el equipo— y sobre todo tener el video **descargado en el "
                    "computador propio** y no en un enlace de nube, que es lo que falla justo cuando "
                    "se necesita.",
                    "**1,5 pts — las tres preguntas del jurado con respuesta de 2 o 3 lineas, al "
                    "menos una de concurrencia o de respaldo.** 0,5 cada una. Lo que se califica es "
                    "que la pregunta sea **incomoda de verdad** y que la respuesta sea honesta: «no "
                    "lo ensaye todavia, es mi unico `NO` y lo cierro el 6 de noviembre» vale mas "
                    "que una respuesta que finge. Una pregunta autocomplaciente —«¿por que "
                    "eligieron PostgreSQL?»— vale 0,25.",
                    "**1 pt — el checklist de empaquetado nombrando archivos y su orden de "
                    "ejecucion.** Se reconoce como sobresaliente nombrar una **dependencia real** "
                    "del orden: los privilegios de la API van despues de crear la API, porque no se "
                    "puede otorgar `EXECUTE` sobre algo que no existe.",
                    "**Este guion es un modelo de referencia, no una clave:** cada estudiante "
                    "sustenta su propio PI. Lo que si conviene contrastar es la coherencia con las "
                    "otras preguntas: si la diapositiva 6 declara el respaldo como resuelto "
                    "mientras el checklist de la Clase 11 lo tiene en `NO`, hay una contradiccion "
                    "que el jurado va a encontrar antes que nadie, y es mejor senalarla al calificar "
                    "que dejarla para el dia de la sustentacion.",
                ],
                "errores": [
                    "**Minutos que no suman entre 5 y 8.** Aparece de dos formas: sumar 12 o 15 "
                    "—porque cada diapositiva «necesita» dos minutos— o no poner la suma en ningun "
                    "lado. El enunciado da un rango explicito y la comprobacion es una resta. Un "
                    "guion de 15 minutos para una franja de 8 no es un guion: es la garantia de que "
                    "las diapositivas 5 y 6 no se van a ver.",
                    "**Un guion de demo con descripciones en vez de sentencias:** «muestro que "
                    "agendar una mascota inactiva falla». El dia de la sustentacion eso se escribe "
                    "en vivo, con el jurado mirando, y ahi aparece el error de sintaxis. El "
                    "enunciado pide **las sentencias exactas** y la razon es practica: se pegan y se "
                    "ejecutan.",
                    "**No incluir ningun caso que falle a proposito,** o incluirlo sin decir que se "
                    "espera ver. Una demo donde todo sale bien no demuestra que las reglas existan: "
                    "demuestra que se eligieron datos que no las activan. El par «rechazo + "
                    "comprobar que nada se movio» es lo que convence.",
                    "**Plan B generico:** «si algo falla, lo explico de palabra». No es un plan, es "
                    "una resignacion. Y el clasico que si parece plan y falla igual: dejar el video "
                    "en un enlace de nube, que es lo que no abre cuando la red esta caida —que es "
                    "justo el escenario del plan B—.",
                    "**Preguntas del jurado autocomplacientes:** «¿por que eligieron PostgreSQL?», "
                    "«¿fue dificil el proyecto?». El ejercicio sirve para lo contrario: anticipar "
                    "las tres que **no** se quieren oir. Si ninguna incomoda, la lista esta mal "
                    "hecha, y el enunciado obliga a que al menos una sea de concurrencia o "
                    "respaldo, que son las dos areas mas debiles del proyecto.",
                    "**Responder la pregunta del respaldo con un «si, esta cubierto».** Contradice "
                    "el checklist de la Clase 11, donde el item 12 esta en `NO`, y un jurado que "
                    "compare los dos documentos lo encuentra en un minuto. La respuesta fuerte es "
                    "la honesta con fecha de cierre: reconocer el hueco y mostrar el plan pesa mas "
                    "que fingir que no existe.",
                    "**Un checklist de empaquetado que lista carpetas sin orden de ejecucion.** El "
                    "enunciado pide «en que orden se ejecutan los scripts», porque de eso depende "
                    "que el proyecto se pueda reconstruir. Un ZIP con los archivos correctos y sin "
                    "el orden es un rompecabezas sin la caja.",
                ],
            },
        ],
        "preguntas_frecuentes": [
            ("Mi `api_agendar_cita(3, ...)` devuelve `ok = false` y **aun asi** la cita queda "
             "creada. ¿Que pasa?",
             "Te falta el `RETURN;` desnudo detras del `RETURN QUERY` del rechazo. Es el error "
             "numero uno de esta clase y vale la pena entenderlo bien: **`RETURN QUERY` no termina "
             "la funcion.** Lo que hace es agregar filas al resultado y seguir ejecutando la linea "
             "de abajo, asi que la funcion llega al `INSERT`, lo hace, y despues agrega una segunda "
             "fila con `ok = true`. El sintoma que lo confirma en dos segundos: "
             "`SELECT COUNT(*) FROM api_agendar_cita(3, 2, TIMESTAMP '2026-10-01 10:00:00');` "
             "devuelve **2** y tiene que devolver 1. La regla: cada `RETURN QUERY SELECT FALSE, "
             "...` lleva un `RETURN;` inmediatamente detras, sin excepcion."),
            ("¿Por que `CALL api_agendar_cita(...)` me dice «is not a procedure»?",
             "Porque no lo es. `CALL` sirve para procedimientos —los `sp_*` de la Clase 8— y aqui "
             "son **funciones** que devuelven una tabla, asi que se consumen en el `FROM`: "
             "`SELECT * FROM api_agendar_cita(1, 2, TIMESTAMP '2026-10-01 09:00:00');`. La "
             "confusion es normal porque en la Clase 8 todo era `CALL`. Y hay una razon de diseno "
             "detras del cambio: un procedimiento no puede devolver una fila de resultado a la "
             "aplicacion de forma comoda, y todo el contrato `(ok, mensaje, id_generado)` depende "
             "precisamente de eso."),
            ("Hice todo lo de la pregunta 4 y `app_vetcare` sigue sin poder agendar. ¿Que me falta?",
             "**Nada de lo que pide el enunciado: te falta algo que el enunciado no pide.** Y es el "
             "hallazgo mas importante de la clase. Las funciones se crearon con `SECURITY INVOKER`, "
             "que es el valor por omision, y eso significa que corren con los privilegios de **quien "
             "las llama**. `app_vetcare` solo tiene `SELECT`, asi que el `INSERT INTO cita` de "
             "adentro se rechaza con «permission denied for table cita», el `EXCEPTION WHEN OTHERS` "
             "lo atrapa, y tu aplicacion recibe un `ok = false` con ese texto como si fuera un "
             "rechazo de negocio. La correccion son tres lineas: `ALTER FUNCTION api_agendar_cita("
             "INT, INT, TIMESTAMP) SECURITY DEFINER SET search_path = public, pg_temp;` y lo "
             "equivalente para las otras dos. El `search_path` fijo no es opcional: una funcion "
             "`SECURITY DEFINER` con el camino abierto se puede enganar creando una tabla `cita` en "
             "otro esquema. Compruebalo con `SET ROLE app_vetcare;` antes y despues."),
            ("¿Puedo probar los permisos si `app_vetcare` es `NOLOGIN` y en ExamLab hay una sola "
             "conexion?",
             "Si, y es la diferencia con la Clase 10. Un superusuario puede ponerse la piel de "
             "cualquier rol con `SET ROLE app_vetcare;` —tambien de uno `NOLOGIN`—, hacer las "
             "pruebas y volver con `RESET ROLE;`. Asi que aqui **si** se puede verificar de verdad: "
             "un `INSERT INTO cita` tiene que fallar con «permission denied» y un `SELECT` sobre "
             "`mascota` tiene que funcionar. Aprovechalo, porque es la unica prueba negativa del "
             "curso que el entorno permite ejecutar. Y no crees un rol con `LOGIN` y contrasena "
             "«para poder probar»: no hace falta y es una credencial mas que administrar."),
            ("¿Por que la llamada 3 registra la consulta de la cita **1** y no de la 11 que acabo "
             "de crear?",
             "Porque las seis llamadas del enunciado son **seis casos de prueba independientes**, "
             "no un flujo encadenado. Estan escritas para ejercitar tres exitos y tres rechazos con "
             "los datos que ya trae la base, y la cita 1 sirve porque esta `PROGRAMADA` y sin "
             "consulta. Por eso al final vas a ver algo que sorprende: la cita **1** quedo "
             "`ATENDIDA` y la **11** sigue `PROGRAMADA`. El flujo encadenado —donde el "
             "`id_generado` de un paso alimenta al siguiente— es lo que armas en la pregunta 2 con "
             "`flujo_atencion`, y ahi si la consulta se registra sobre la cita que se acabo de "
             "crear."),
            ("¿Puedo usar f-strings en Python si los datos vienen de un formulario que ya valide?",
             "No, y conviene ser categorico: **es la unica prohibicion de la pregunta 2 que cuesta "
             "los 5 puntos completos.** La validacion del formulario es comodidad, no garantia: "
             "cambia el dia que alguien agregue una pantalla nueva, o una llamada desde otro "
             "modulo, o un script de carga masiva. Con parametros ligados el texto del SQL es una "
             "constante del programa y los datos son argumentos, asi que **no hay forma** de que un "
             "dato se convierta en sentencia. Piensa en el campo del diagnostico, que es texto "
             "libre escrito por un veterinario apurado: con una f-string, un `'); DROP TABLE cita; "
             "--` ahi dentro es una sentencia; con `%s` es una cadena de caracteres y nada mas."),
            ("¿`api_facturar` es segura si la app reintenta por un timeout de red?",
             "**No, y es la unica de las tres que hace dano real.** Un segundo intento crea una "
             "segunda factura y **descuenta el stock otra vez**: doble cargo al cliente y doble "
             "descuento de inventario, sin ningun error visible. Las otras dos se salvan, aunque "
             "por accidente: agendar devuelve «Franja ocupada» —ocupada por tu propia cita del "
             "primer intento— y registrar consulta devuelve «La cita ya tiene consulta», con un "
             "`UNIQUE` de verdad detras. Ni una ni otra te devuelven el id de lo que ya existe, que "
             "es lo que la aplicacion necesitaba. La solucion concreta que va en el contrato: un "
             "parametro `p_clave_idem TEXT` que la app genera una vez por intento, una columna "
             "`factura.clave_idem TEXT UNIQUE`, y que si la clave ya existe la funcion devuelva "
             "`(true, 'Factura ya generada', id_existente)` sin cobrar de nuevo."),
            ("El `REVOKE` del paso 2 de la pregunta 4 me saca un `WARNING`. ¿Esta mal?",
             "No. `WARNING: no privileges could be revoked for \"cita\"` significa que a "
             "`app_vetcare` nunca se le habia otorgado nada sobre esa tabla, que es exactamente lo "
             "que querias confirmar. Es informativo, aparece una vez por tabla y el script sigue "
             "corriendo. La sentencia se escribe igual, y el enunciado explica por que: un script "
             "de permisos tiene que poder leerse como la **decision** de diseno y no solo como su "
             "efecto. El dia que alguien haga un `GRANT ALL` de apuro, esa linea lo revierte al "
             "reejecutar el script."),
        ],
        "cierre": [
            "Al terminar, cada estudiante debe tener: las **tres funciones `api_*`** con el "
            "contrato literal `(ok, mensaje, id_generado)` y las seis llamadas devolviendo "
            "`11 / rechazo / 5 / rechazo / 4 / rechazo` **sin una sola excepcion**; el **cliente "
            "Python** con parametros ligados, `dataclass` y `flujo_atencion` cortando en el primer "
            "`ok = false`; el **diagrama de secuencia** con los cuatro participantes, el `alt` del "
            "corte y ninguna flecha de la app a las tablas; el **script de privilegios** con el "
            "`REVOKE EXECUTE ... FROM PUBLIC` —6 filas y 4 filas en las verificaciones—; el "
            "**contrato de integracion** con los tres bloques de siete puntos, la tabla de "
            "rechazos y el veredicto de idempotencia; y el **guion de sustentacion** de 7 minutos "
            "con la demo de 10 sentencias y el plan B de tres niveles.",
            "Cuatro comprobaciones rapidas antes de cerrar, todas de leer y contar. Que cada "
            "llamada `api_*` devuelva **exactamente una fila** —dos filas significan que falta un "
            "`RETURN;` y que la funcion hizo el `INSERT` que decia estar rechazando—. Que en el "
            "archivo Python **no haya ni una f-string dentro del SQL** ni la palabra `INSERT`. Que "
            "el diagrama **renderice** y que ninguna flecha vaya de `APP` a `DB`. Y que el "
            "`REVOKE EXECUTE ... FROM PUBLIC` este, con las tres firmas completas: sin el, el "
            "`GRANT` a `app_vetcare` no protege nada, porque una funcion recien creada trae "
            "`EXECUTE` para todo el mundo.",
            "El mensaje de la clase es el de la pregunta 4, y conviene decirlo con las dos mitades. "
            "La primera es la que se buscaba: **el permiso hace imposible lo que la disciplina solo "
            "hace improbable.** La aplicacion no se salta las validaciones no porque el equipo se "
            "haya comprometido a llamar las funciones, sino porque sin `INSERT` **no tiene camino** "
            "—y eso vale igual para un bug, para un desarrollador nuevo o para una inyeccion SQL "
            "exitosa, que terminan todas en «permission denied»—. La segunda mitad es la incomoda, "
            "y es lo mejor que se llevan de hoy: al probarlo con `SET ROLE` resulta que **la API "
            "tampoco funciona**, porque falta `SECURITY DEFINER`, y el `EXCEPTION WHEN OTHERS` que "
            "hace tan elegante el contrato disfraza ese fallo de configuracion como si fuera un "
            "rechazo de negocio. Un permiso configurado y no verificado es una suposicion, igual "
            "que el respaldo que nunca se restauro. El **2026-11-09** es el Parcial 3 y el "
            "**2026-11-16** hay que sustentar: la pregunta 1 del jurado ya esta escrita en esta "
            "clase, y tambien su respuesta.",
        ],
    },

    13: {
        "titulo": "Solucion del taller · Clase 13 · Analisis de un caso real aplicado a VetCare (clase autonoma)",
        "resumen": (
            "El analisis del caso GitLab 2017 con las seis secciones y la causa raiz separada de "
            "la aparente; la demostracion cuantificada de la inyeccion —la funcion vulnerable "
            "devuelve **las 8 mascotas** y, con una variante `UNION`, **los correos de los 6 "
            "duenos**— y su cierre con `EXECUTE ... USING`, incluida la trampa de ambiguedad que "
            "hace fallar la variante estatica; el control de borrados completo: respaldo con "
            "bitacora calculada, trigger `BEFORE DELETE` que archiva `OLD`, el `DELETE` sin "
            "`WHERE` que deja `cita` en 0 y `cita_borrada` en 10, la restauracion y la consulta de "
            "veredicto que devuelve `RESTAURACION OK`; la clave razonada de las cuatro opciones "
            "correctas; y el plan de tres mejoras con la unica pendiente que sigue siendo la misma "
            "desde la Clase 11: **el restore que nadie ha ensayado**."
        ),
        "total": 100,
        "nota_actividad": (
            "**Clase autonoma: Sesion 11, lunes 2026-11-02, sin docente en vivo.** Eso cambia como "
            "se usa este documento. No hay momento para aclarar dudas en el aula, asi que la "
            "retroalimentacion tiene que ser **escrita** y llegar rapido: el 2026-11-09 es el "
            "Parcial 3 —tampoco hay espacio ahi— y el 2026-11-16 es la sustentacion. En la "
            "practica, el ultimo momento util para devolver correcciones es la semana del "
            "2026-11-02, y conviene publicar junto con el taller las tres advertencias de abajo, "
            "porque son las que sin docente presente bloquean a un estudiante media tarde. **El "
            "motor es PostgreSQL, no Oracle.**\n\n"
            "**Advertencia etica, primero que todo y en el enunciado publicado.** La pregunta 2 "
            "pide ejecutar cadenas de ataque. Se ejecutan contra la base de practica del propio "
            "estudiante en ExamLab, que es suya y es desechable. Probar lo mismo contra un sistema "
            "ajeno y sin autorizacion escrita no es un ejercicio: es un delito. El objetivo de la "
            "pregunta es **cerrar** el agujero, y la evidencia que se califica es el 0 filas del "
            "final.\n\n"
            "**Tres trampas tecnicas que hay que anunciar.** (1) La variante estatica que sugiere "
            "el enunciado —`buscar_mascota_directa` con "
            "`SELECT id_mascota, nombre ... WHERE nombre = p_nombre`— **falla** con «column "
            "reference “id_mascota” is ambiguous», porque los nombres del `RETURNS TABLE` son "
            "variables de PL/pgSQL y chocan con las columnas; se arregla con alias "
            "(`m.id_mascota`, `m.nombre`, …) y es instructivo que la version con `EXECUTE` no tenga "
            "ese problema. (2) En la pregunta 3, `RETURN NEW` en un trigger de `DELETE` devuelve "
            "`NULL` y **cancela el borrado en silencio**: el estudiante vera 10 filas en las dos "
            "tablas y creera que funciono. (3) `DROP FUNCTION buscar_mascota_insegura(TEXT);` es lo "
            "ultimo del script: si se ejecuta antes, los pasos 1 a 3 ya no corren.\n\n"
            "**Y una incoherencia del banco que conviene resolver antes de publicar.** La pregunta "
            "1 deja elegir entre tres casos, pero las preguntas 2 y 3 implementan mejoras del caso "
            "**C** (inyeccion) y del caso **A** (respaldo). Quien elija el **B** —rendimiento— se "
            "encuentra en la pregunta 5 con que las dos mejoras «ya implementadas» no derivan de su "
            "caso. Lo razonable es sugerir A o C; y si alguien elige B, se acepta que cite como "
            "mejora ya implementada el indice de la Clase 6 (`idx_cita_vet_fecha`, con sus dos "
            "`EXPLAIN`) y que la tabla mezcle los tres origenes, siempre que cada fila nombre un "
            "objeto real. Las preguntas 1 y 5 son sobre el caso y el PI de cada estudiante, asi que "
            "lo que sigue es un **modelo de referencia y no una clave**: se desarrolla el caso A y "
            "se dan las notas para calificar B y C."
        ),
        "preguntas": [
            {
                "n": 1,
                "titulo": "El caso: que paso, por que y que aprendemos",
                "tipo": "abierta",
                "puntos": 25,
                "respuesta": (
                    "Se desarrolla el **caso A**, porque es el que conecta con el control que se "
                    "implementa en la pregunta 3 y con el unico item que sigue en `NO` en el "
                    "checklist de la Clase 11. Las notas para calificar B y C van al final.\n\n"
                    "### 1. Contexto\n\n"
                    "GitLab.com, plataforma de alojamiento de codigo fuente y gestion de proyectos "
                    "de software, con millones de repositorios alojados y equipos de desarrollo de "
                    "todo el mundo trabajando sobre ella. La base de datos principal es PostgreSQL, "
                    "con una replica secundaria que deberia servir para conmutar en caso de fallo. "
                    "Lo que estaba en juego no era solo el codigo —que casi todos los usuarios "
                    "tienen tambien en sus maquinas— sino **todo lo que vive unicamente en la base "
                    "de datos**: incidencias, solicitudes de fusion, comentarios, cuentas de "
                    "usuario y proyectos recien creados. Es decir, la conversacion y el historial de "
                    "decisiones de miles de equipos.\n\n"
                    "### 2. Que fallo, en orden\n\n"
                    "1. Un aumento anormal de carga —trafico de spam que generaba escrituras "
                    "masivas— saturo la base de datos principal.\n"
                    "2. Por efecto de esa carga, la **replicacion hacia el servidor secundario se "
                    "quedo atras** y termino rompiendose.\n"
                    "3. Para volver a sincronizar la replica hay que dejar su directorio de datos "
                    "vacio y copiarlo de nuevo desde el principal. Un ingeniero, ya de noche y "
                    "varias horas dentro del incidente, ejecuto ese borrado.\n"
                    "4. **Lo ejecuto en la terminal del servidor principal, no en la de la "
                    "replica.** Se dio cuenta en segundos y lo interrumpio, pero para entonces ya "
                    "se habia eliminado la mayor parte del directorio de datos de produccion.\n"
                    "5. Empezo la recuperacion, y ahi aparecio el verdadero problema: de los cinco "
                    "mecanismos de respaldo que la organizacion creia tener, **ninguno estaba en "
                    "condiciones de usarse**. Los volcados logicos periodicos fallaban en silencio "
                    "—una diferencia de version entre las herramientas y el servidor los dejaba "
                    "practicamente vacios— y las alertas de ese fallo no llegaban a ninguna "
                    "bandeja. Las instantaneas de disco no estaban habilitadas en ese servidor. La "
                    "replica ya estaba destruida por el paso 3.\n"
                    "6. La unica copia utilizable era una de un entorno de pruebas, tomada unas "
                    "**seis horas antes**. Se restauro desde ahi, y todo lo ocurrido en esas seis "
                    "horas se perdio de forma definitiva.\n\n"
                    "### 3. Causa raiz, separada de la causa aparente\n\n"
                    "**Causa aparente:** «un ingeniero se equivoco de terminal». Es cierto y es "
                    "irrelevante para la prevencion, porque un equipo que trabaja a las once de la "
                    "noche en un incidente **va** a equivocarse de terminal alguna vez; disenar "
                    "para que eso no ocurra nunca es disenar para un ser humano que no existe.\n\n"
                    "**Causa raiz: no habia ningun control que detuviera ese error ni que "
                    "garantizara la vuelta atras.** Y es doble.\n\n"
                    "- **La raiz proxima:** el mismo comando destructivo se podia ejecutar en "
                    "produccion sin confirmacion, sin distincion visual del entorno y sin ninguna "
                    "barrera. El error humano tenia acceso directo al dato.\n"
                    "- **La raiz de fondo, que es la importante:** **ninguno de los cinco "
                    "respaldos se habia verificado nunca restaurandolo.** Existian como "
                    "procedimiento y como archivo, no como capacidad comprobada. Y el fallo era "
                    "silencioso por diseno accidental: el proceso avisaba por correo, y esos "
                    "correos se rechazaban, asi que la senal de que el respaldo estaba roto se "
                    "perdia todos los dias sin que nadie la viera. **Un respaldo que falla en "
                    "silencio es indistinguible de uno que funciona, hasta el dia en que hace "
                    "falta.**\n\n"
                    "Dicho de otra manera: el borrado accidental no causo la perdida de datos. El "
                    "borrado accidental **reveló** que la capacidad de recuperacion no existia. La "
                    "perdida llevaba meses siendo inevitable.\n\n"
                    "### 4. Impacto\n\n"
                    "- **Datos:** aproximadamente seis horas de escrituras perdidas de forma "
                    "irrecuperable —incidencias, comentarios, solicitudes de fusion, usuarios y "
                    "proyectos creados en esa ventana—. No se pudo reconstruir: no habia de donde.\n"
                    "- **Tiempo:** del orden de dieciocho horas de servicio interrumpido o "
                    "degradado, mas dias de trabajo del equipo en la recuperacion y el analisis "
                    "posterior.\n"
                    "- **Confianza:** es el costo mas caro y el menos medible. Miles de equipos "
                    "descubrieron el mismo dia que su historial de decisiones dependia de una "
                    "cadena de respaldos que no funcionaba.\n"
                    "- **Contrapeso honesto:** la organizacion publico el analisis completo del "
                    "incidente, con los cinco mecanismos y por que fallo cada uno. Esa "
                    "transparencia es la razon por la que hoy se puede estudiar en un curso, y es "
                    "en si misma una practica que vale la pena copiar.\n\n"
                    "### 5. Leccion en una frase accionable\n\n"
                    "> **Un respaldo que no se ha restaurado no es un respaldo: es un archivo con "
                    "un nombre tranquilizador. La copia no es el control; el control es la "
                    "restauracion verificada.**\n\n"
                    "Y una segunda, que se deriva de la misma raiz: **si el fallo de un control "
                    "puede pasar inadvertido, el control no existe.** Un respaldo que avisa cuando "
                    "falla —y que se comprueba que avisa— vale mas que cinco que se ejecutan en "
                    "silencio.\n\n"
                    "### 6. Traduccion a VetCare\n\n"
                    "El proceso vulnerable al **mismo** tipo de fallo es el borrado de `cita`, y el "
                    "mecanismo es identico, no analogo:\n\n"
                    "- **Hoy `DELETE FROM cita;` sin `WHERE` se ejecuta y no deja nada.** No hay "
                    "confirmacion, no hay archivo de lo borrado y no hay copia previa. Diez filas "
                    "en el taller; en produccion, la agenda completa de la clinica.\n"
                    "- **La bitacora que si existe no cubre este caso.** `audit_cita`, de la Clase "
                    "4, se dispara con los `UPDATE` de estado. **Un `DELETE` no deja rastro en "
                    "ella**, asi que el evento mas destructivo es justamente el unico que no se "
                    "audita.\n"
                    "- **Y la copia esta en el mismo sitio que el original.** Cualquier "
                    "`respaldo_cita` o `audit_cita` vive en la misma base de datos: protege contra "
                    "un error logico y **no** protege contra perder la instancia, el disco o el "
                    "servidor. Es exactamente el error de razonamiento del caso —confundir «tengo "
                    "una copia» con «puedo recuperar»—.\n"
                    "- **El equivalente exacto del respaldo que falla en silencio, en mi "
                    "proyecto,** es el item 12 del checklist de la Clase 11: plan de respaldo "
                    "escrito, con RPO y RTO estimados, y **restauracion nunca ensayada**. Es el "
                    "unico item en `NO` y es el unico irreversible.\n\n"
                    "La pregunta 3 implementa los dos controles que faltaban: el archivo de lo "
                    "borrado, que convierte el accidente en recuperable, y la consulta de "
                    "verificacion, que convierte la copia en capacidad comprobada.\n\n"
                    "---\n\n"
                    "### Notas para calificar los otros dos casos\n\n"
                    "**Caso B (rendimiento).** La causa raiz correcta **no** es «la consulta estaba "
                    "mal escrita»: es que un proceso automatico podia consumir recursos sin limite "
                    "y sin que nadie lo notara antes de la hora pico —sin limite de tiempo de "
                    "ejecucion, sin tope de conexiones, sin revision del plan antes de publicar el "
                    "panel—. El `SELECT *` y el indice ausente son el mecanismo; la raiz es la "
                    "ausencia de control. La traduccion a VetCare esta hecha desde la Clase 6: la "
                    "consulta de agenda por veterinario y rango de fechas hacia `Seq Scan` con "
                    "`Rows Removed by Filter`, y el indice `idx_cita_vet_fecha` lo cerro. Quien "
                    "elija B puede citar ese trabajo como mejora ya implementada en la pregunta 5.\n\n"
                    "**Caso C (inyeccion).** La causa raiz es que el texto de la sentencia se "
                    "construia con datos del usuario, de modo que un dato podia convertirse en "
                    "codigo; **no** es «no se validaba la entrada». La distincion importa porque "
                    "lleva a soluciones distintas: validar es una lista de casos que siempre queda "
                    "incompleta, y ligar parametros elimina el mecanismo. La traduccion a VetCare "
                    "es `buscar_mascota_insegura`, y la pregunta 2 la ejecuta y la cierra. Se "
                    "reconoce como sobresaliente notar que era una funcion de **solo lectura**, y "
                    "que por eso nadie la reviso: no escribia nada, «no podia hacer dano», y "
                    "entregaba la base completa."
                ),
                "como_calificar": [
                    "**9 pts — las seis secciones presentes,** 1,5 cada una. Se califica la "
                    "presencia y que cada una responda lo suyo: contexto (que organizacion y que "
                    "estaba en juego), secuencia **en orden**, causa raiz, impacto, leccion y "
                    "traduccion. Una seccion que existe pero repite otra —impacto que vuelve a "
                    "contar los hechos— cuenta como media.",
                    "**6 pts — la causa raiz distinguida explicitamente de la aparente y apuntando "
                    "a un control ausente.** Es el punto de mas peso y el que decide la calidad del "
                    "analisis. Requiere las dos mitades escritas: la aparente («alguien se "
                    "equivoco», «la consulta estaba mal escrita», «no se validaba la entrada») y la "
                    "raiz formulada como **ausencia de control** («no habia nada que detuviera ese "
                    "error», «los respaldos nunca se restauraron»). Un texto que se queda en la "
                    "culpa de una persona vale 2 de 6, aunque este bien escrito: es el analisis que "
                    "no cambia nada.",
                    "**4 pts — impacto concreto.** Se piden magnitudes en las cuatro dimensiones "
                    "que nombra el enunciado —datos, dinero o tiempo, y confianza— con cifras u "
                    "ordenes de magnitud, no adjetivos. «Fue muy grave» vale 0; «unas seis horas de "
                    "escrituras perdidas sin posibilidad de reconstruirlas» vale completo. Se "
                    "acepta «aproximadamente» y se agradece: es mas honesto que una cifra falsa.",
                    "**3 pts — la leccion redactada como regla accionable,** en imperativo o como "
                    "afirmacion verificable. «Hay que cuidar los respaldos» no es accionable; «un "
                    "respaldo que no se ha restaurado no es un respaldo» si, porque se puede "
                    "comprobar si se cumple o no.",
                    "**3 pts — la traduccion a VetCare nombrando tablas, funciones o triggers "
                    "reales y explicando el mecanismo.** 1,5 pts nombrar el objeto y 1,5 pts "
                    "explicar **como** se reproduce el mismo fallo ahi. «VetCare tambien podria "
                    "tener problemas de respaldo» vale 0. «`DELETE FROM cita;` se ejecuta hoy sin "
                    "nada que lo detenga, y `audit_cita` solo registra `UPDATE`, asi que el evento "
                    "mas destructivo es el unico sin auditoria» vale completo.",
                    "**Si el caso es propio, la fuente es obligatoria** —enlace o publicacion— y su "
                    "ausencia cuesta 3 pts: sin fuente no es un caso real, es un relato. Se "
                    "reconoce como sobresaliente citar el analisis publico del incidente en lugar "
                    "de una nota de prensa que lo resume.",
                    "**Se reconoce como sobresaliente, sin puntos extra:** senalar que el fallo era "
                    "**silencioso** —la alerta de que el respaldo no servia no llegaba a nadie— y "
                    "sacar de ahi la segunda regla; o notar que la copia logica vive en la misma "
                    "base que el original y por tanto no protege contra perder la instancia.",
                ],
                "errores": [
                    "**Confundir la causa raiz con la culpa.** «El error fue del ingeniero que se "
                    "equivoco de servidor» es la version que no sirve para nada, porque la "
                    "conclusion practica seria «tener mas cuidado», y eso no es un control. La "
                    "pregunta util es la contraria: ¿que tendria que haber existido para que ese "
                    "error, que iba a ocurrir tarde o temprano, no terminara en perdida de datos?",
                    "**Un resumen en vez de un analisis.** Media pagina contando los hechos, sin "
                    "separar causa aparente de raiz y sin traduccion al proyecto. Es lo que sale "
                    "cuando se copia el enunciado con otras palabras. La forma de detectarlo: si el "
                    "texto no contiene ninguna afirmacion que no estuviera ya en el enunciado, no "
                    "hay analisis.",
                    "**Impacto con adjetivos:** «enorme», «gravisimo», «se perdio mucha "
                    "informacion». No informa y no se puede comparar con nada. Cualquier magnitud "
                    "aproximada —horas de datos, horas de servicio, numero de usuarios afectados— "
                    "vale mas que tres superlativos.",
                    "**Una leccion que no es accionable:** «hay que ser cuidadoso con la base de "
                    "datos», «la seguridad es importante». No se puede comprobar si se cumple. Una "
                    "regla accionable siempre se puede convertir en una pregunta de si o no: ¿se "
                    "restauro el ultimo respaldo? ¿se comparo el conteo?",
                    "**Una traduccion a VetCare por analogia y no por mecanismo:** «a VetCare "
                    "tambien le podria pasar algo parecido». Hay que nombrar el objeto —`cita`, "
                    "`audit_cita`, `buscar_mascota_insegura`, `api_facturar`— y describir la "
                    "sentencia o el camino concreto por el que el fallo se reproduce.",
                    "**Elegir el caso B y despues no poder conectarlo con las preguntas 2 y 3,** "
                    "que implementan mejoras de C y de A. No es culpa del estudiante —el enunciado "
                    "lo permite—, pero deja la pregunta 5 sin sustento. La salida correcta es citar "
                    "el trabajo de indices de la Clase 6 como la mejora ya implementada del caso B.",
                    "**Inventar cifras precisas.** «Se perdieron 4.312 registros y 2,3 millones de "
                    "dolares» sin fuente resta credibilidad a todo el analisis. Si no se sabe, se "
                    "escribe el orden de magnitud y se dice que es aproximado.",
                ],
            },
            {
                "n": 2,
                "titulo": "Mejora implementada 1: cerrar la inyeccion de SQL en VetCare",
                "tipo": "bd_sql",
                "puntos": 25,
                "sql": """-- ======================================================================
-- ADVERTENCIA, y no es formalismo
-- Las cadenas de ataque de abajo se ejecutan contra TU base de practica en
-- ExamLab: es tuya, es desechable y se vuelve a sembrar en cada pregunta.
-- Probar esto mismo contra un sistema que no es propio y sin autorizacion
-- escrita no es un ejercicio, es un delito. Lo que se aprende aqui es a
-- CERRAR el agujero, y la evidencia que se entrega es el 0 filas del final.
-- ======================================================================

-- ----------------------------------------------------------------------
-- 1. Uso normal: la funcion vulnerable parece impecable
-- ----------------------------------------------------------------------
SELECT * FROM buscar_mascota_insegura('Firulais');
-- 1 fila. Y ahi esta el problema de fondo de todo incidente de inyeccion:
-- en la prueba que hizo quien la escribio, funciono.

-- ----------------------------------------------------------------------
-- 2. El ataque: el usuario reescribe el WHERE
--
-- La cadena que se envia es    Firulais' OR '1'='1
-- y en SQL se escribe duplicando cada comilla simple. La funcion la
-- concatena y el texto que termina ejecutando el motor es:
--
--   SELECT id_mascota, nombre, especie, activa
--     FROM mascota WHERE nombre = 'Firulais' OR '1'='1'
--
-- El dato dejo de ser un dato y se convirtio en codigo. Nadie violo una
-- contrasena ni un permiso: la funcion hizo exactamente lo que le
-- pidieron.
-- ----------------------------------------------------------------------
SELECT * FROM buscar_mascota_insegura('Firulais'' OR ''1''=''1');
-- 8 filas: la tabla completa, incluidas Rocky y Kiara, que el buscador
-- del negocio nunca deberia mostrar.

-- ----------------------------------------------------------------------
-- 3. Cuantificar la fuga: la evidencia del incidente
--
-- Este par de consultas es lo que se pega en el informe. Una captura de
-- "salieron muchas filas" no prueba nada; dos numeros iguales, si.
-- ----------------------------------------------------------------------
SELECT COUNT(*) AS filas_devueltas_por_el_ataque
  FROM buscar_mascota_insegura('x'' OR ''1''=''1');
-- 8. Notese que ahora el nombre buscado es 'x', que NO existe: el
-- resultado no depende del dato, depende del OR que el atacante inyecto.

SELECT COUNT(*) AS filas_totales_en_la_tabla FROM mascota;
-- 8. Coinciden. Un buscador de una mascota entrego la tabla entera.

-- ----------------------------------------------------------------------
-- 3b. EXTRA: lo que de verdad se roba (opcional, y es el que convence)
--
-- El OR '1'='1' entrega una tabla. Un UNION entrega OTRA tabla, una que
-- la funcion no menciona en ninguna parte. La cadena enviada es:
--
--   x' UNION SELECT id_dueno, nombre, email, 'S'::CHAR(1) FROM dueno --
--
-- El -- del final comenta la comilla suelta que quedaba. Resultado: los
-- correos de los seis duenos, viajando por un buscador de mascotas. Esto
-- es la fuga de datos personales del caso C, reproducida en dos lineas.
-- ----------------------------------------------------------------------
SELECT * FROM buscar_mascota_insegura(
  'x'' UNION SELECT id_dueno, nombre, email, ''S''::CHAR(1) FROM dueno --');
-- 6 filas con los datos de contacto de los duenos. El ::CHAR(1) esta
-- porque las columnas del UNION deben coincidir con el RETURNS TABLE; sin
-- el, el motor responde "structure of query does not match function result
-- type", que tambien es informativo: el atacante ajusta los tipos y sigue.

-- ----------------------------------------------------------------------
-- 4. La version segura: el dato viaja como parametro, no como texto
--
-- La diferencia esta en $1 y en USING. El texto de la sentencia es una
-- constante del programa; el valor va aparte y el motor NUNCA lo analiza
-- como codigo. No hay nada que escapar porque no hay nada que interpretar.
-- ----------------------------------------------------------------------
CREATE FUNCTION buscar_mascota_segura(p_nombre TEXT)
RETURNS TABLE (id_mascota INT, nombre TEXT, especie TEXT, activa CHAR(1))
LANGUAGE plpgsql
AS $fn$
BEGIN
  RETURN QUERY EXECUTE
    'SELECT id_mascota, nombre, especie, activa FROM mascota WHERE nombre = $1'
    USING p_nombre;
END;
$fn$;

-- ----------------------------------------------------------------------
-- 4b. Mejor todavia: aqui no hacia falta SQL dinamico
--
-- El EXECUTE existe para armar sentencias cuyo TEXTO cambia -- otra tabla,
-- otra columna, otro ORDER BY --. Cuando lo unico que cambia es un valor,
-- la consulta estatica es mas simple, se planifica mejor y no da
-- oportunidad de equivocarse.
--
-- OJO A LA TRAMPA: los nombres del RETURNS TABLE son variables de
-- PL/pgSQL, asi que en una consulta estatica "id_mascota" es ambiguo
-- -- ¿la columna o la variable? --. Sin los alias m., esta funcion se crea
-- sin protestar y falla en la PRIMERA llamada con
--   ERROR: column reference "id_mascota" is ambiguous
-- La version con EXECUTE no tiene el problema porque su cadena se pasa al
-- motor sin sustitucion de variables. Es una diferencia real entre las dos
-- formas y conviene entenderla en vez de pelearse con el error.
-- ----------------------------------------------------------------------
CREATE FUNCTION buscar_mascota_directa(p_nombre TEXT)
RETURNS TABLE (id_mascota INT, nombre TEXT, especie TEXT, activa CHAR(1))
LANGUAGE plpgsql
AS $fn$
BEGIN
  RETURN QUERY
    SELECT m.id_mascota, m.nombre, m.especie, m.activa
      FROM mascota m
     WHERE m.nombre = p_nombre;
END;
$fn$;

-- ----------------------------------------------------------------------
-- 5. Probar que el agujero quedo cerrado
--
-- Dos pruebas, no una: que el ataque falle Y que el uso legitimo siga
-- funcionando. Una funcion que devuelve 0 filas para todo tambien pasaria
-- la primera prueba.
-- ----------------------------------------------------------------------
SELECT * FROM buscar_mascota_segura('Firulais'' OR ''1''=''1');
-- 0 filas. La cadena completa -- con sus comillas y su OR -- se comparo
-- como un VALOR contra la columna nombre. Ninguna mascota se llama asi.

SELECT * FROM buscar_mascota_segura('Firulais');
-- 1 fila. El buscador sigue sirviendo para lo que existe.

SELECT * FROM buscar_mascota_directa('Firulais'' OR ''1''=''1');   -- 0 filas
SELECT * FROM buscar_mascota_directa('Firulais');                   -- 1 fila

-- El UNION tampoco pasa: ya no hay sentencia que reescribir.
SELECT COUNT(*) AS filas_del_ataque_contra_la_segura
  FROM buscar_mascota_segura(
    'x'' UNION SELECT id_dueno, nombre, email, ''S''::CHAR(1) FROM dueno --');
-- 0. El contraste 8 -> 0 es la evidencia del antes y despues.

-- ----------------------------------------------------------------------
-- 6. Eliminar la funcion vulnerable y dejar la regla escrita
--
-- Va de ultimo a proposito: si se hace el DROP antes, los pasos 1 a 3 ya
-- no se pueden ejecutar y se pierde la evidencia del incidente.
-- ----------------------------------------------------------------------
DROP FUNCTION buscar_mascota_insegura(TEXT);

-- Y la comprobacion de que ya no existe -- porque "la borre" tambien es
-- una afirmacion que se verifica:
SELECT COUNT(*) AS funciones_inseguras_restantes
  FROM information_schema.routines
 WHERE routine_name = 'buscar_mascota_insegura';
-- 0

-- ======================================================================
-- REGLA QUE ADOPTO PARA VETCARE (esto es lo que pide el punto 6)
--
-- -- 1. Ningun valor que provenga de un usuario se concatena en el texto
-- --    de una sentencia. Nunca, ni "solo por esta vez", ni en funciones
-- --    de solo lectura. Los valores viajan como parametros: $1 con USING
-- --    en PL/pgSQL, %s en psycopg2.
-- -- 2. El SQL dinamico se usa solo cuando cambia la ESTRUCTURA de la
-- --    sentencia (nombre de tabla, de columna, sentido del ORDER BY).
-- --    Si lo unico que cambia es un valor, la consulta va estatica.
-- -- 3. Cuando de verdad haya que construir un identificador, se hace con
-- --    format('... %I ...', v_columna), nunca con ||, porque los
-- --    parametros no pueden ligar identificadores: $1 sirve para valores.
-- -- 4. Una funcion de solo lectura tambien es una puerta.
-- --    buscar_mascota_insegura no escribia nada y entregaba la base
-- --    completa; precisamente por "solo consultar" nadie la reviso.
-- ======================================================================""",
                "salida": """1. Uso normal de la funcion vulnerable -- 1 fila

 id_mascota |  nombre  | especie | activa
------------+----------+---------+--------
          1 | Firulais | Canino  | S

2. El ataque OR '1'='1' -- 8 filas

 id_mascota |  nombre  | especie | activa
------------+----------+---------+--------
          1 | Firulais | Canino  | S
          2 | Luna     | Felino  | S
          3 | Rocky    | Canino  | N
          4 | Mishi    | Felino  | S
          5 | Bobby    | Canino  | S
          6 | Nube     | Felino  | S
          7 | Toby     | Canino  | S
          8 | Kiara    | Canino  | N

Ocho filas donde el negocio esperaba una. Y notese el detalle que suele pasar
inadvertido: aparecen Rocky y Kiara, que estan inactivas. El buscador de la
aplicacion filtraria las inactivas en la interfaz; el ataque se salta la
interfaz completa. La consulta no lleva ORDER BY, asi que el orden no esta
garantizado -- en una tabla recien sembrada sale el fisico, 1 a 8 -- y por eso la
evidencia que se entrega es el COUNT, no la captura.

3. La fuga, cuantificada -- 1 fila cada una

 filas_devueltas_por_el_ataque
-------------------------------
                             8

 filas_totales_en_la_tabla
---------------------------
                         8

Iguales. Ese par de numeros es el informe del incidente: un buscador de una
mascota devolvio el 100 % de la tabla. Y el nombre buscado era 'x', que no
existe -- el resultado ya no depende del dato.

3b. EXTRA, el UNION -- 6 filas

 id_mascota |     nombre     |         especie          | activa
------------+----------------+--------------------------+--------
          1 | Ana Gomez      | ana.gomez@mail.com       | S
          2 | Carlos Ruiz    | carlos.ruiz@mail.com     | S
          3 | Marcela Diaz   | marcela.diaz@mail.com    | S
          4 | Jorge Pineda   | jorge.pineda@mail.com    | S
          5 | Luisa Cardona  | luisa.cardona@mail.com   | S
          6 | Andres Vallejo | andres.vallejo@mail.com  | S

Detente aqui un momento, porque es el resultado que cambia la conversacion. La
columna que dice "especie" trae CORREOS ELECTRONICOS. La funcion nunca menciono
la tabla dueno y aun asi acaba de entregar los datos de contacto de los seis
clientes de la clinica. El OR '1'='1' era una fuga de una tabla; el UNION es una
fuga de cualquier tabla que el rol pueda leer. Un UNION no garantiza orden; da
igual, lo que importa son las 6 filas.

5. Contra la version segura -- 0 filas

 id_mascota | nombre | especie | activa
------------+--------+---------+--------
(0 filas)

Cero. La cadena Firulais' OR '1'='1 se comparo como un valor contra la columna
nombre, y ninguna mascota se llama asi. No hubo nada que escapar porque no hubo
nada que interpretar.

 id_mascota |  nombre  | especie | activa
------------+----------+---------+--------
          1 | Firulais | Canino  | S

Y el uso legitimo sigue funcionando, que es la mitad de la prueba que se olvida:
una funcion que devolviera 0 filas para todo tambien "resiste" el ataque.

 filas_del_ataque_contra_la_segura
-----------------------------------
                                 0

El contraste completo, que es lo que la rubrica exige: **8 antes, 0 despues.**

6. Despues del DROP -- 1 fila

 funciones_inseguras_restantes
-------------------------------
                             0

Si en algun momento aparece
  ERROR:  column reference "id_mascota" is ambiguous
  DETAIL:  It could refer to either a PL/pgSQL variable or a table column.
es buscar_mascota_directa sin los alias m.: los nombres del RETURNS TABLE son
variables de PL/pgSQL y chocan con las columnas de la tabla. Se arregla
calificando las columnas, no cambiando la consulta.""",
                "como_calificar": [
                    "**4 pts — el uso normal y el ataque ejecutados y mostrados,** 2 pts cada uno. "
                    "El ataque tiene que devolver las **8** filas; si devuelve 1, casi siempre es "
                    "que las comillas no se duplicaron y la cadena llego literal. Se reconoce como "
                    "sobresaliente escribir en un comentario el texto **final** que ejecuta el "
                    "motor —`... WHERE nombre = 'Firulais' OR '1'='1'`—, porque es lo que hace "
                    "visible que el dato se volvio codigo.",
                    "**5 pts — el contraste cuantitativo con `COUNT`.** Es requisito literal de la "
                    "rubrica —«se descuenta si no se muestra el contraste cuantitativo antes/"
                    "despues»— y se califica de forma estricta: hacen falta los dos `COUNT` del "
                    "antes (8 y 8, iguales) y el 0 del despues. Capturas de pantalla con «salieron "
                    "muchas filas» valen 0 de 5: el informe de un incidente se sostiene en numeros "
                    "comparables.",
                    "**7 pts — `buscar_mascota_segura` con `EXECUTE ... USING` y la firma de "
                    "retorno intacta.** 4 pts el `$1` con `USING` —no un `||` con comillas "
                    "escapadas— y 3 pts que el `RETURNS TABLE (id_mascota INT, nombre TEXT, especie "
                    "TEXT, activa CHAR(1))` sea identico al de la funcion que reemplaza, porque una "
                    "funcion que cierra el agujero y cambia el contrato rompe la aplicacion que la "
                    "llama.",
                    "**4 pts — el ataque contra la version segura devolviendo 0 filas,** y se "
                    "reconoce como sobresaliente probar **tambien** que el uso legitimo sigue "
                    "devolviendo 1: una funcion que devolviera 0 filas para cualquier entrada "
                    "tambien «resiste» el ataque y no sirve para nada. La pareja 0 filas / 1 fila "
                    "es la prueba completa.",
                    "**2 pts — la variante estatica `buscar_mascota_directa`,** que el enunciado "
                    "sugiere como «mejor aun». Se otorgan si funciona; y **no se descuenta a quien "
                    "no la incluya**, porque es opcional. Al calificar hay que anticipar el error "
                    "de ambiguedad: sin los alias `m.` la funcion se crea sin protestar y falla en "
                    "la primera llamada con «column reference “id_mascota” is ambiguous», porque los "
                    "nombres del `RETURNS TABLE` son variables de PL/pgSQL.",
                    "**3 pts — el `DROP FUNCTION buscar_mascota_insegura(TEXT);` y la regla propia "
                    "en un comentario `--`.** 1 pt el `DROP` con la firma —`(TEXT)` es obligatorio— "
                    "y 2 pts que la regla sea una regla: «usar parametros ligados siempre que sea "
                    "posible» no lo es, «ningun valor de usuario se concatena en el texto de una "
                    "sentencia» si. Se reconoce como sobresaliente distinguir que el SQL dinamico "
                    "se justifica solo cuando cambia la **estructura** de la sentencia, y que para "
                    "identificadores va `format('%I')` porque los parametros no ligan nombres de "
                    "objetos.",
                    "**Se reconoce como muy sobresaliente, sin puntos extra, la variante con "
                    "`UNION`** que extrae los correos de los seis duenos a traves de un buscador de "
                    "mascotas. Demuestra lo que el `OR '1'='1'` solo insinua: la fuga no se limita a "
                    "la tabla consultada, alcanza cualquier tabla que el rol pueda leer. Es la "
                    "lamina que hay que llevar a la sustentacion.",
                ],
                "errores": [
                    "**El ataque devuelve 1 fila en vez de 8.** Casi siempre porque las comillas no "
                    "se duplicaron: se escribio `buscar_mascota_insegura('Firulais' OR '1'='1')`, "
                    "que ni siquiera es SQL valido, o se paso la cadena sin escapar. En SQL, para "
                    "meter una comilla simple dentro de una cadena se duplica: "
                    "`'Firulais'' OR ''1''=''1'`. Vale la pena mostrar el texto intermedio para que "
                    "se vea que son dos niveles de comillas, no uno.",
                    "**Escapar a mano en vez de ligar parametros:** "
                    "`replace(p_nombre, '''', '''''')` y seguir concatenando. Cierra **este** "
                    "ataque y no cierra el mecanismo: en un contexto numerico no hay comillas que "
                    "escapar —`WHERE id_mascota = ' || p_id` con `p_id = '1 OR 1=1'` pasa "
                    "limpio—, depende de la configuracion de escapes del servidor y hay que "
                    "recordar aplicarlo en cada camino. Es exactamente la opcion falsa de la "
                    "pregunta 4.",
                    "**Cambiar la firma de retorno «para que quede mas limpia»,** por ejemplo "
                    "devolviendo `SETOF mascota` o quitando `activa`. La funcion segura reemplaza a "
                    "la insegura **en una aplicacion que ya la llama**; cambiar el contrato "
                    "convierte una correccion de seguridad en una interrupcion del servicio, que es "
                    "la razon por la que estas correcciones se posponen en la vida real.",
                    "**`buscar_mascota_directa` sin alias de tabla.** Se crea sin errores y falla "
                    "en la primera llamada con «column reference “id_mascota” is ambiguous». El "
                    "estudiante suele concluir que «la consulta estatica no sirve» y volver al "
                    "`EXECUTE`. La causa real es el sombreado de nombres del `RETURNS TABLE`, y la "
                    "solucion son cuatro `m.`.",
                    "**Hacer el `DROP` antes de demostrar el ataque.** El script queda en un orden "
                    "que ya no se puede volver a ejecutar y la evidencia del incidente desaparece. "
                    "La demostracion va primero; el `DROP` es la ultima linea.",
                    "**`DROP FUNCTION buscar_mascota_insegura;` sin la firma.** Falla con «could "
                    "not find a function named ...» o pide desambiguar. Es el mismo aprendizaje de "
                    "la Clase 12 con los `GRANT`: las funciones se identifican por nombre **mas** "
                    "tipos de argumentos.",
                    "**Probar solo que el ataque falla.** Media prueba. Falta comprobar que la "
                    "busqueda legitima sigue devolviendo su fila; sin eso no se sabe si se cerro el "
                    "agujero o se rompio el buscador.",
                ],
            },
            {
                "n": 3,
                "titulo": "Mejora implementada 2: ningun borrado sin traza ni sin vuelta atras",
                "tipo": "bd_sql",
                "puntos": 25,
                "sql": """-- ======================================================================
-- LO QUE SE CONSTRUYE AQUI, Y POR QUE SON TRES COSAS DISTINTAS
--
--   respaldo_cita + bitacora_respaldo  -> la copia, y la constancia de
--                                         cuantas filas tenia
--   cita_borrada + trg_archivar_cita   -> el archivo, que hace RECUPERABLE
--                                         un borrado accidental
--   la consulta de veredicto           -> la VERIFICACION, que es lo que
--                                         convierte una copia en una
--                                         capacidad comprobada
--
-- El caso analizado tenia lo primero -- cinco veces -- y no tenia lo
-- tercero. Por eso se perdieron datos con cinco respaldos disponibles.
-- ======================================================================

-- ----------------------------------------------------------------------
-- 1. Respaldo logico previo y su bitacora
--
-- CREATE TABLE ... AS SELECT copia estructura de columnas y datos, y NADA
-- mas: no trae la PK, ni los CHECK, ni las FK, ni la secuencia del SERIAL.
-- Para un respaldo eso esta bien -- lo que se quiere es el dato -- pero hay
-- que saberlo: respaldo_cita no es una tabla equivalente a cita.
-- ----------------------------------------------------------------------
CREATE TABLE respaldo_cita AS SELECT * FROM cita;

CREATE TABLE bitacora_respaldo (
  id_bitacora       SERIAL PRIMARY KEY,
  tabla             TEXT NOT NULL,
  filas_respaldadas INT  NOT NULL,
  hecho_en          TIMESTAMP NOT NULL DEFAULT now()
);

-- El conteo se CALCULA. Escribir "10" a mano es la version en miniatura
-- del error del caso: dejar constancia de lo que uno cree en vez de lo que
-- hay. Si el respaldo se hubiera hecho a medias, el 10 escrito a mano
-- mentiria y la verificacion del paso 5 diria OK sobre una base incompleta.
INSERT INTO bitacora_respaldo (tabla, filas_respaldadas)
SELECT 'cita', COUNT(*) FROM respaldo_cita;

SELECT * FROM bitacora_respaldo;          -- 1 fila: cita | 10

-- ----------------------------------------------------------------------
-- 2. Archivo de borrados + trigger
--
-- Mismas columnas que cita, mas quien borro y cuando. Y a proposito SIN
-- llaves foraneas: un archivo tiene que poder sobrevivir a lo que archiva.
-- Es el mismo argumento de audit_cita en la Clase 4, y aqui es mas fuerte,
-- porque si manana se borra una mascota, una FK impediria conservar la
-- traza de sus citas -- justo cuando mas se necesita.
-- ----------------------------------------------------------------------
CREATE TABLE cita_borrada (
  id_cita        INT,
  id_mascota     INT,
  id_veterinario INT,
  fecha_hora     TIMESTAMP,
  estado         TEXT,
  borrado_en     TIMESTAMP DEFAULT now(),
  usuario_bd     TEXT      DEFAULT current_user
);

-- Un trigger son SIEMPRE dos objetos: la funcion y la asociacion.
CREATE FUNCTION fn_trg_archivar_cita()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $fn$
BEGIN
  INSERT INTO cita_borrada (id_cita, id_mascota, id_veterinario,
                            fecha_hora, estado)
  VALUES (OLD.id_cita, OLD.id_mascota, OLD.id_veterinario,
          OLD.fecha_hora, OLD.estado);
  -- RETURN OLD deja pasar el borrado. Si aqui se escribe RETURN NEW -- que
  -- en un DELETE vale NULL --, el borrado se CANCELA en silencio: la fila
  -- se archiva, cita conserva sus 10 filas y el DELETE informa 0. Parece
  -- que funciono y no funciono nada.
  RETURN OLD;
END;
$fn$;

CREATE TRIGGER trg_archivar_cita
  BEFORE DELETE ON cita
  FOR EACH ROW
  EXECUTE FUNCTION fn_trg_archivar_cita();

-- ----------------------------------------------------------------------
-- 3. Reproducir el incidente: el DELETE sin WHERE
--
-- Esta es la sentencia del caso, en miniatura y en una base desechable.
-- Diez filas aqui; la agenda completa de la clinica en produccion.
-- ----------------------------------------------------------------------
DELETE FROM cita;                          -- DELETE 10

SELECT COUNT(*) AS filas_en_cita          FROM cita;           -- 0
SELECT COUNT(*) AS filas_en_cita_borrada  FROM cita_borrada;   -- 10

-- Y el archivo, para verlo: trae quien y cuando, que es lo que el caso
-- real tuvo que reconstruir a mano.
SELECT id_cita, id_mascota, estado, usuario_bd
  FROM cita_borrada
 ORDER BY id_cita;

-- ----------------------------------------------------------------------
-- 4. Restaurar, con columnas explicitas
--
-- Columnas explicitas y no INSERT INTO cita SELECT * FROM cita_borrada,
-- que falla: cita_borrada tiene dos columnas mas. Ademas el SELECT *
-- depende del orden fisico de las columnas, y eso es exactamente el tipo
-- de suposicion que rompe un guion de recuperacion el dia que se usa.
-- ----------------------------------------------------------------------
INSERT INTO cita (id_cita, id_mascota, id_veterinario, fecha_hora, estado)
SELECT id_cita, id_mascota, id_veterinario, fecha_hora, estado
  FROM cita_borrada
 ORDER BY id_cita;                         -- INSERT 0 10

-- La secuencia del SERIAL NO se movio con estos INSERT, porque el id se
-- dio explicito. Aqui no hay choque -- la secuencia ya iba en 10 y las
-- secuencias no se devuelven, como se vio en la Clase 8 --, pero en una
-- restauracion sobre una tabla recien creada la secuencia estaria en 1 y
-- el primer INSERT normal reventaria contra la PK. Realinearla es parte
-- del guion de recuperacion, no un detalle:
SELECT last_value AS secuencia_antes FROM cita_id_cita_seq;      -- 10
SELECT setval(pg_get_serial_sequence('cita','id_cita'),
              (SELECT MAX(id_cita) FROM cita));                  -- 10

-- ----------------------------------------------------------------------
-- 5. Verificar la restauracion: la consulta que faltaba en el caso real
--
-- Una sola fila, con lo esperado, lo obtenido, los extremos del rango y un
-- veredicto calculado. No es adorno: es la diferencia entre "restaure" y
-- "comprobe que la restauracion quedo bien". El ORDER BY ... LIMIT 1 esta
-- porque si el script se vuelve a correr, la bitacora tendria dos filas y
-- la consulta dejaria de devolver una sola.
-- ----------------------------------------------------------------------
SELECT b.filas_respaldadas                        AS filas_esperadas,
       (SELECT COUNT(*) FROM cita)                AS filas_actuales,
       (SELECT MIN(fecha_hora) FROM cita)         AS primera_cita,
       (SELECT MAX(fecha_hora) FROM cita)         AS ultima_cita,
       CASE WHEN b.filas_respaldadas = (SELECT COUNT(*) FROM cita)
            THEN 'RESTAURACION OK'
            ELSE 'REVISAR'
       END                                        AS veredicto
  FROM bitacora_respaldo b
 WHERE b.tabla = 'cita'
 ORDER BY b.id_bitacora DESC
 LIMIT 1;

-- ----------------------------------------------------------------------
-- 5b. EXTRA: tapar el hueco del propio control (va mas alla del enunciado)
--
-- Un trigger FOR EACH ROW se dispara con DELETE y NO se dispara con
-- TRUNCATE, que borra sin recorrer filas. Es decir: el control que se
-- acaba de construir no cubre la sentencia mas destructiva de las dos.
-- Se cierra con un trigger de sentencia, y se puede COMPROBAR sin perder
-- nada, porque el TRUNCATE queda bloqueado.
-- ----------------------------------------------------------------------
CREATE FUNCTION fn_trg_bloquear_truncate()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $fn$
BEGIN
  RAISE EXCEPTION
    'TRUNCATE bloqueado en %: use DELETE para que el archivo funcione',
    TG_TABLE_NAME;
END;
$fn$;

CREATE TRIGGER trg_bloquear_truncate_cita
  BEFORE TRUNCATE ON cita
  FOR EACH STATEMENT
  EXECUTE FUNCTION fn_trg_bloquear_truncate();

TRUNCATE cita;
-- ERROR: TRUNCATE bloqueado en cita: use DELETE para que el archivo funcione
-- Las 10 filas siguen ahi. Un control probado es uno que se vio estorbar.

SELECT COUNT(*) AS filas_tras_intentar_truncate FROM cita;       -- 10

-- ======================================================================
-- POR QUE EL TRIGGER Y LA CONSULTA SON CONTROLES DISTINTOS
--
-- -- El trigger es un control de RECUPERACION: no evita nada. El DELETE
-- -- sin WHERE se ejecuta igual y cita queda en cero. Lo que hace es
-- -- convertir un dano irreversible en uno reversible, guardando el dato
-- -- y quien lo borro. Actua en el momento del incidente y de forma
-- -- automatica, sin depender de que nadie se acuerde.
-- --
-- -- La consulta de veredicto es un control de VERIFICACION: no protege
-- -- ningun dato, comprueba una afirmacion. Responde "¿la restauracion
-- -- quedo completa?" con un numero comparable, no con una impresion.
-- -- Actua DESPUES y solo si alguien la ejecuta.
-- --
-- -- Hacen falta los dos porque cada uno falla donde el otro no llega:
-- -- con archivo y sin verificacion se restaura a medias y se declara
-- -- resuelto -- que es literalmente el caso analizado, con cinco copias
-- -- y ninguna probada --; con verificacion y sin archivo se detecta la
-- -- perdida con precision y no hay nada que reponer. Y los dos juntos
-- -- siguen sin proteger contra perder la instancia: respaldo_cita y
-- -- cita_borrada viven en la MISMA base. Eso lo cubre un respaldo
-- -- fisico externo, que es la mejora pendiente de la pregunta 5.
-- ======================================================================""",
                "salida": """1. Bitacora del respaldo -- 1 fila

 id_bitacora | tabla | filas_respaldadas |          hecho_en
-------------+-------+-------------------+----------------------------
           1 | cita  |                10 | 2026-11-02 19:14:33.201

El 10 salio de un COUNT sobre respaldo_cita, no de los dedos. La marca de tiempo
varia en cada corrida y no se califica.

3. El incidente

DELETE 10

 filas_en_cita
---------------
             0

 filas_en_cita_borrada
-----------------------
                    10

Cero y diez: el borrado ocurrio de verdad -- el trigger no lo evita -- y el dato
esta a salvo. Esa es la definicion de "incidente recuperable".

El archivo -- 10 filas

 id_cita | id_mascota |   estado   | usuario_bd
---------+------------+------------+------------
       1 |          1 | PROGRAMADA | postgres
       2 |          2 | ATENDIDA   | postgres
       3 |          4 | PROGRAMADA | postgres
       4 |          5 | CANCELADA  | postgres
       5 |          6 | ATENDIDA   | postgres
       6 |          7 | PROGRAMADA | postgres
       7 |          1 | ATENDIDA   | postgres
       8 |          2 | PROGRAMADA | postgres
       9 |          4 | PROGRAMADA | postgres
      10 |          6 | ATENDIDA   | postgres

El usuario_bd sale de current_user y en ExamLab es el rol del entorno -- suele ser
postgres --; el nombre no es lo que se califica, que la columna exista y se
llene si. En produccion esa columna es la que responde "¿quien lo borro?" sin
tener que reconstruirlo de la memoria de nadie.

4. Restauracion

INSERT 0 10

 secuencia_antes
-----------------
              10

 setval
--------
     10

El setval no cambia nada aqui, y esta a proposito: la secuencia ya iba en 10
porque las secuencias no se devuelven. En una restauracion sobre una tabla recien
creada estaria en 1 y el primer INSERT normal chocaria contra la llave primaria.
Realinearla pertenece al guion de recuperacion.

5. El veredicto -- 1 fila

 filas_esperadas | filas_actuales |    primera_cita     |     ultima_cita     |    veredicto
-----------------+----------------+---------------------+---------------------+-----------------
              10 |             10 | 2026-09-01 08:00:00 | 2026-09-10 09:00:00 | RESTAURACION OK

Esta fila es el entregable de la pregunta. No dice "restaure la tabla": dice que
las filas esperadas y las presentes coinciden y que el rango de fechas es el que
tenia que ser -- del 1 al 10 de septiembre --. Los dos extremos importan: un
conteo correcto con un MIN o un MAX desplazado significa que se restauro otra
cosa, o solo una parte, y el conteo solo no lo delataria.

Si sale REVISAR, el veredicto esta haciendo su trabajo: hay que mirar el
INSERT ... SELECT antes de seguir. Y si la consulta devuelve DOS filas, es que el
script se corrio dos veces y la bitacora tiene dos entradas -- para eso esta el
ORDER BY ... LIMIT 1.

5b. EXTRA: el hueco del propio control

ERROR:  TRUNCATE bloqueado en cita: use DELETE para que el archivo funcione

 filas_tras_intentar_truncate
------------------------------
                           10

Y ahi esta lo incomodo: el trigger FOR EACH ROW que se acaba de construir **no
se dispara con TRUNCATE**, que es la sentencia mas destructiva de las dos. El
control tenia un agujero del tamano de una palabra. El trigger de sentencia lo
cierra, y se pudo comprobar sin perder nada porque el bloqueo funciona.""",
                "como_calificar": [
                    "**4 pts — `respaldo_cita` y `bitacora_respaldo`,** 1,5 y 1,5 pts, mas **1 pt "
                    "reservado a que el conteo se calcule con una subconsulta y no se escriba a "
                    "mano.** Ese punto suelto es deliberado: es requisito literal de la rubrica y "
                    "es la version en miniatura del error del caso —dejar constancia de lo que uno "
                    "cree en vez de lo que hay—. Un `filas_respaldadas` con un `10` literal "
                    "mentiria si el respaldo hubiera quedado a medias, y la verificacion del paso 5 "
                    "diria `RESTAURACION OK` sobre una base incompleta.",
                    "**7 pts — `cita_borrada` y el trigger.** 2 pts la tabla con las cinco columnas "
                    "de `cita` mas `borrado_en` y `usuario_bd` con sus `DEFAULT`; 3 pts la funcion "
                    "`fn_trg_archivar_cita()` insertando los valores de `OLD` **columna por "
                    "columna** y terminando en `RETURN OLD`; 2 pts la asociacion "
                    "`BEFORE DELETE ON cita FOR EACH ROW`. Se reconoce como sobresaliente justificar "
                    "que `cita_borrada` **no** lleva llaves foraneas: un archivo tiene que "
                    "sobrevivir a lo que archiva, y una FK a `mascota` impediria conservar la traza "
                    "el dia que se borre una mascota.",
                    "**4 pts — el `DELETE FROM cita;` y las dos consultas de comprobacion,** con "
                    "`cita` en **0** y `cita_borrada` en **10**. Si las dos dan 10, el trigger "
                    "devuelve `NULL` —tipicamente un `RETURN NEW`, que en un `DELETE` vale `NULL`— "
                    "y **el borrado se cancelo en silencio**: hay que devolverlo, porque el "
                    "estudiante suele leerlo como exito.",
                    "**4 pts — la restauracion con columnas explicitas.** 3 pts el "
                    "`INSERT INTO cita (...) SELECT ...` reponiendo las 10 filas y 1 pt que las "
                    "columnas esten enumeradas: un `SELECT *` desde `cita_borrada` falla —tiene dos "
                    "columnas mas— y ademas depende del orden fisico de las columnas, que es "
                    "justo la suposicion que rompe un guion de recuperacion el dia que se usa.",
                    "**5 pts — la consulta de validacion en una sola fila con las cinco columnas y "
                    "el `veredicto` calculado con `CASE`.** 3 pts la estructura —esperadas, "
                    "actuales, `MIN`, `MAX`, veredicto— y 2 pts que el veredicto sea **calculado** "
                    "y no un literal `'RESTAURACION OK'` escrito porque ya se sabe el resultado. "
                    "Una consulta que devuelva dos filas no cumple «una sola fila»: pasa cuando el "
                    "script se corre dos veces y la bitacora acumula, y se resuelve con "
                    "`ORDER BY id_bitacora DESC LIMIT 1`.",
                    "**1 pt — el comentario final distinguiendo los dos controles.** El argumento "
                    "correcto es que el trigger es **recuperacion** —no evita nada, hace reversible "
                    "el dano, actua automaticamente en el momento— y la consulta es "
                    "**verificacion** —no protege ningun dato, comprueba una afirmacion, actua "
                    "despues y solo si alguien la ejecuta—; y que hacen falta los dos porque con "
                    "archivo y sin verificacion se restaura a medias y se declara resuelto, que es "
                    "literalmente el caso analizado.",
                    "**Se reconoce como muy sobresaliente, sin puntos extra:** notar que un trigger "
                    "`FOR EACH ROW` **no se dispara con `TRUNCATE`**, de modo que el control recien "
                    "construido no cubre la sentencia mas destructiva, y cerrarlo con un trigger "
                    "`BEFORE TRUNCATE ... FOR EACH STATEMENT`; o dejar escrito que `respaldo_cita` "
                    "y `cita_borrada` viven en la **misma** base y por tanto no protegen contra "
                    "perder la instancia, que es exactamente el error de razonamiento del caso.",
                ],
                "errores": [
                    "**`RETURN NEW` en el trigger de `DELETE`.** Es el error mas enganoso de la "
                    "pregunta: en un `DELETE`, `NEW` vale `NULL`, y un trigger `BEFORE` que "
                    "devuelve `NULL` **cancela la operacion**. El resultado es que la fila se "
                    "archiva, `cita` conserva sus 10 filas, el motor informa `DELETE 0` y el "
                    "estudiante concluye que su control «evito el borrado». No evito nada: rompio "
                    "el `DELETE`. La comprobacion que lo delata son las dos consultas del paso 3.",
                    "**Escribir el conteo a mano** en `bitacora_respaldo`, casi siempre porque «son "
                    "10, ya lo vi». Es el error del caso reproducido: la bitacora deja de ser "
                    "evidencia y pasa a ser una opinion, y si el respaldo hubiera quedado "
                    "incompleto la verificacion del paso 5 daria `OK` de todas formas. La rubrica "
                    "lo pide calculado con esas palabras.",
                    "**`INSERT INTO cita SELECT * FROM cita_borrada;`.** Falla, porque "
                    "`cita_borrada` tiene siete columnas y `cita` cinco. Al intentar arreglarlo "
                    "aparece la segunda version del error —enumerar las columnas del `INSERT` pero "
                    "dejar el `SELECT *`—, que tambien falla. Las dos listas van explicitas y en el "
                    "mismo orden.",
                    "**Un `veredicto` escrito a mano:** `'RESTAURACION OK' AS veredicto`. Ya se "
                    "sabe que salio bien, asi que «para que el `CASE`». Porque el control no es "
                    "para hoy: es la consulta que alguien va a correr dentro de seis meses, a las "
                    "tres de la manana, sin saber el resultado esperado. Un veredicto literal "
                    "siempre dice OK, tambien cuando no lo esta.",
                    "**Olvidar el `RETURN OLD` por completo** —una funcion de trigger que termina "
                    "sin `RETURN`—. En PL/pgSQL una funcion `RETURNS TRIGGER` que cae al final "
                    "devuelve `NULL`, con el mismo efecto que el `RETURN NEW`: el borrado se "
                    "cancela. El sintoma es identico y la causa tambien.",
                    "**Creer que `CREATE TABLE respaldo_cita AS SELECT * FROM cita;` crea una tabla "
                    "equivalente.** Copia columnas y datos, y nada mas: sin PK, sin `CHECK`, sin "
                    "FK, sin secuencia. Sirve como respaldo de datos y no sirve para reemplazar la "
                    "tabla. Conviene decirlo antes de que alguien planee la recuperacion apoyandose "
                    "en eso.",
                    "**Poner llaves foraneas en `cita_borrada`** «para que quede bien modelada». "
                    "Invierte el proposito: el archivo tiene que sobrevivir a lo que archiva, y una "
                    "FK a `mascota` haria fallar el borrado de una mascota justo cuando conservar "
                    "la traza de sus citas es lo unico que queda. Es el mismo argumento de "
                    "`audit_cita` en la Clase 4.",
                    "**Concluir que con el trigger «ya no se puede perder una cita».** No cubre "
                    "`TRUNCATE`, no cubre `DROP TABLE`, no cubre a quien haga "
                    "`ALTER TABLE cita DISABLE TRIGGER`, y sobre todo el archivo vive en la misma "
                    "base que el original. Protege contra un error logico; no contra perder la "
                    "instancia.",
                ],
            },
            {
                "n": 4,
                "titulo": "Que control habria evitado el incidente",
                "tipo": "cerrada_multi",
                "puntos": 10,
                "justificacion": {
                    0: "**Correcta, y es la tesis del caso A.** Una copia es un archivo; el "
                       "control es la restauracion verificada. El caso analizado tenia cinco "
                       "copias y perdio datos porque ninguna se habia restaurado nunca. La palabra "
                       "que hace verdadera la afirmacion es «confirmo conteos y rangos»: es lo que "
                       "hace la consulta de veredicto de la pregunta 3, y por eso pide `MIN` y "
                       "`MAX` ademas del conteo —un conteo correcto con un rango desplazado "
                       "significa que se restauro otra cosa—.",
                    1: "**Falsa, y es la opcion que mas se marca por error,** porque escapar "
                       "*parece* resolver el problema. No es equivalente por tres razones "
                       "acumulativas. Primera: en un contexto numerico no hay comillas que "
                       "escapar, asi que `'... WHERE id_mascota = ' || p_id` con `p_id` igual a "
                       "`1 OR 1=1` pasa intacto. Segunda: escapar correctamente depende de la "
                       "configuracion de escapes del servidor y de la codificacion, y hay motores "
                       "donde la funcion ingenua es insuficiente. Tercera y decisiva: es un "
                       "control que hay que **acordarse** de aplicar en cada camino del codigo, y "
                       "un solo camino olvidado es el agujero completo. Ligar parametros no mejora "
                       "la defensa: **elimina el mecanismo**, porque el valor nunca llega al "
                       "analizador de sentencias.",
                    2: "**Correcta, y conviene fijarse en la razon que da la afirmacion,** que es "
                       "la que hay que poder repetir: «la entrada viaja como valor y nunca se "
                       "interpreta como codigo». No es que el motor limpie la cadena —no la "
                       "limpia—, es que el texto de la sentencia se planifica **antes** y por "
                       "separado, asi que el dato ya no tiene forma de convertirse en instruccion. "
                       "Es lo que la pregunta 2 demuestra con el 8 → 0.",
                    3: "**Falsa, y es la descripcion literal del incidente:** cinco mecanismos, "
                       "ninguno probado, cero recuperacion. Peor todavia, la cantidad genero una "
                       "falsa sensacion de seguridad —con cinco copias nadie sintio la necesidad "
                       "de probar una—. La regla practica que se deriva: **un respaldo verificado "
                       "vale mas que cinco sin verificar**, y un respaldo cuyo fallo pasa "
                       "inadvertido no cuenta como respaldo.",
                    4: "**Correcta, y hay que subrayar la segunda mitad de la frase:** «aunque no "
                       "evita el error humano». Es exactamente lo que se comprueba en la pregunta "
                       "3: el `DELETE FROM cita;` se ejecuta, `cita` queda en 0 y el trigger no lo "
                       "impide. Lo que hace es cambiar la naturaleza del incidente, de perdida "
                       "definitiva a interrupcion recuperable. Es un control de recuperacion, no "
                       "de prevencion, y confundirlos lleva a creerse protegido.",
                    5: "**Correcta, y es el caso B.** El mecanismo es concreto: sin indice, la "
                       "consulta recorre la tabla completa; con `SELECT *`, cada recorrido arrastra "
                       "columnas que el reporte no usa y multiplica la memoria y el trafico; y "
                       "cada minuto significa que una ejecucion todavia corriendo se solapa con la "
                       "siguiente, hasta agotar las conexiones. Los tres factores se suman, y es "
                       "el mismo diagnostico de las Clases 6 y 7: `Rows Removed by Filter` alto es "
                       "trabajo que se paga y no se usa.",
                },
                "como_calificar": [
                    "**10 pts con las cuatro correctas —0, 2, 4 y 5— y ninguna incorrecta;** "
                    "puntaje proporcional por acierto parcial, tal como declara la rubrica de la "
                    "plataforma. Al revisar en grupo conviene senalar que las cuatro correctas son "
                    "los cuatro controles del curso: verificar el respaldo, ligar parametros, "
                    "archivar antes de borrar y medir el plan de una consulta.",
                    "**La opcion 1 —escapar comillas a mano— es la que mas se marca por error** y "
                    "merece explicacion aparte, no solo un «es falsa». Tres razones acumulativas: "
                    "en contexto numerico no hay comillas que escapar; el escape correcto depende "
                    "de la configuracion del servidor; y es un control que hay que recordar aplicar "
                    "en cada camino del codigo. Ligar parametros **elimina el mecanismo** en vez de "
                    "reforzar la defensa.",
                    "**La opcion 3 es el caso A en una linea** y sirve para comprobar si el "
                    "estudiante lo leyo: quien marque «tener cinco respaldos garantiza la "
                    "recuperacion» no analizo el incidente, porque el incidente es precisamente eso "
                    "saliendo mal. Conviene devolverlo con la cifra: cinco mecanismos, ninguno "
                    "utilizable, seis horas perdidas.",
                    "**En la opcion 4 lo que se califica es entender la segunda mitad de la "
                    "frase:** «aunque no evita el error humano». Es la distincion "
                    "prevencion/recuperacion que la pregunta 3 demuestra ejecutando el `DELETE` y "
                    "viendo `cita` en 0. Un estudiante que la marque bien pero crea que el trigger "
                    "impide el borrado tiene el punto y no la idea.",
                    "**Errores frecuentes de seleccion:** marcar solo 0 y 2 —quedarse con los dos "
                    "controles «de libro» y descartar el trigger por «no evitar nada», que es "
                    "justamente lo que la opcion admite— o marcar las seis, que suele indicar que "
                    "se respondio por intuicion sin leer las dos negativas.",
                ],
                "errores": [
                    "**Marcar la opcion 1 creyendo que escapar y ligar son lo mismo.** Es el error "
                    "conceptual central de la clase y no se cierra diciendo «es falsa»: hay que "
                    "mostrar el contraejemplo numerico, donde no hay ni una comilla que escapar y "
                    "la inyeccion pasa igual.",
                    "**Marcar la opcion 3** porque «cinco es mejor que uno». Cinco copias sin "
                    "probar son cinco archivos con nombre tranquilizador, y ademas producen la "
                    "falsa sensacion de seguridad que impidio probar alguna. La opcion es el caso "
                    "analizado, escrito en afirmativo.",
                    "**Descartar la opcion 4** razonando «si no evita el error, no es un control». "
                    "Confunde prevencion con recuperacion. La mayoria de los controles de un "
                    "sistema real no evitan el fallo: acotan su consecuencia, y esa es toda la "
                    "diferencia entre una interrupcion de dos horas y una perdida definitiva.",
                    "**Descartar la opcion 5** por parecer exagerada. No lo es, y esta medida en el "
                    "propio curso: en la Clase 6 la misma consulta pasa de recorrer la tabla "
                    "completa a resolverse por indice, y en la Clase 7 se vio que el problema no es "
                    "solo el tiempo sino el trabajo desperdiciado que `Rows Removed by Filter` "
                    "delata.",
                    "**Marcar las seis opciones.** Con una pregunta de seleccion multiple y "
                    "puntaje proporcional, marcar todo no maximiza nada: las dos incorrectas "
                    "restan. Y ademas revela que no se leyeron, porque 1 y 3 se contradicen "
                    "directamente con las conclusiones de las preguntas 2 y 3 del mismo taller.",
                ],
            },
            {
                "n": 5,
                "titulo": "Tres mejoras priorizadas para VetCare",
                "tipo": "abierta",
                "puntos": 15,
                "tabla": {
                    "headers": ["#", "Mejora concreta", "Objeto de VetCare que cambia",
                                "Riesgo que mitiga", "Esfuerzo", "Impacto", "Como se verifica",
                                "Estado"],
                    "rows": [
                        ["1",
                         "Reemplazar el buscador que concatena por uno con parametros ligados y "
                         "eliminar el vulnerable",
                         "Funciones `buscar_mascota_segura` y `buscar_mascota_directa` creadas; "
                         "`buscar_mascota_insegura` eliminada con `DROP FUNCTION`",
                         "Fuga de datos personales por inyeccion de SQL. El ataque no solo "
                         "entregaba las 8 mascotas: con un `UNION` entregaba los correos de los 6 "
                         "duenos",
                         "Bajo", "Alto",
                         "Ya ejecutado: el ataque `'Firulais'' OR ''1''=''1'` devuelve **8 filas** "
                         "contra la funcion vieja y **0 filas** contra `buscar_mascota_segura`, y "
                         "`buscar_mascota_segura('Firulais')` sigue devolviendo su fila",
                         "**IMPLEMENTADA**"],
                        ["2",
                         "Archivar toda cita antes de borrarla y verificar cada restauracion con "
                         "una consulta de veredicto",
                         "Tabla `cita_borrada`, funcion `fn_trg_archivar_cita()`, trigger "
                         "`trg_archivar_cita` (`BEFORE DELETE ... FOR EACH ROW`) y tabla "
                         "`bitacora_respaldo`",
                         "Perdida definitiva por un borrado accidental, y restauracion incompleta "
                         "declarada como exitosa —los dos fallos del caso—",
                         "Medio", "Alto",
                         "Ya ejecutado: `DELETE FROM cita;` dejo `cita` en **0** y `cita_borrada` "
                         "en **10**; tras el `INSERT ... SELECT` la consulta de validacion devolvio "
                         "`10 | 10 | 2026-09-01 08:00 | 2026-09-10 09:00 | RESTAURACION OK`",
                         "**IMPLEMENTADA**"],
                        ["3",
                         "Ensayar de punta a punta un respaldo **fisico externo**: `pg_dump` de la "
                         "base completa, restauracion en una base vacia y ejecucion de la bateria "
                         "de verificacion de la Clase 11",
                         "Script nuevo `09_respaldo_y_restore.sql` mas la tabla `checklist_pi` de "
                         "la Clase 11, que registra el resultado del ensayo",
                         "Perdida total por fallo de la instancia o del disco. Las mejoras 1 y 2 "
                         "viven **dentro** de la misma base: no cubren este caso",
                         "Medio", "Alto",
                         "`pg_restore --list` demuestra que el archivo es legible; la prueba real "
                         "es que la bateria de la Clase 11 sobre la base restaurada devuelva el "
                         "**mismo** resultado, incluido el `cumple = FALSE` de la prueba 5",
                         "**PENDIENTE** · responsable: el estudiante que sustenta · fecha: "
                         "**2026-11-06**"],
                    ],
                },
                "respuesta": (
                    "### 1. Priorizacion: que haria primero con un solo dia\n\n"
                    "**La tercera, el ensayo de restauracion,** y no porque sea la mas atractiva "
                    "sino porque es la unica que queda y es **la unica irreversible**. Las mejoras "
                    "1 y 2 estan hechas, asi que la comparacion real es entre cerrar el ensayo o "
                    "dedicar el dia a pulir el informe. Con esfuerzo medio e impacto alto, el "
                    "ensayo gana sin discusion: un error de redaccion se arregla el dia siguiente, "
                    "y un respaldo que no restaura no se arregla **despues** del incidente. Ademas "
                    "es el unico item en `NO` del checklist de la Clase 11 y la tercera pregunta "
                    "que el jurado va a hacer.\n\n"
                    "**Y si ninguna estuviera hecha, el orden seria 1 → 2 → 3,** por dos criterios "
                    "distintos que conviene separar. Por esfuerzo/impacto, la mejora 1 es la "
                    "unica con esfuerzo **bajo** e impacto alto: dos funciones y un `DROP`, media "
                    "hora. Y por urgencia, es la unica que cierra un agujero **activo**: "
                    "`buscar_mascota_insegura` era explotable en ese momento, mientras que las "
                    "mejoras 2 y 3 mitigan un incidente **futuro**. Cuando un riesgo ya se esta "
                    "materializando y otro todavia no, el que se esta materializando va primero, "
                    "aunque el otro tenga peor consecuencia.\n\n"
                    "### 2. Que dice esto de mi diseno\n\n"
                    "El caso puso en evidencia **tres supuestos** que estaban en el proyecto sin "
                    "que nadie los hubiera escrito, y por lo tanto sin que nadie los hubiera "
                    "discutido.\n\n"
                    "**El primero, y el que mas me sorprendio: supuse que la capa `api_*` de la "
                    "Clase 12 cerraba la inyeccion.** No la cierra. La cierra para las tres "
                    "operaciones de escritura, que son las que revise; `buscar_mascota_insegura` "
                    "era una funcion de **solo lectura** y no la miro nadie, precisamente porque "
                    "«solo consulta». Ahi estaba el agujero, y era el mas grave del proyecto: no "
                    "modificaba un dato, entregaba la base. La leccion es incomoda y util: **el "
                    "codigo que nadie audita es el que solo lee.**\n\n"
                    "**El segundo: supuse que tener una copia era poder recuperar.** El plan de "
                    "respaldo del informe declara un RPO de 15 minutos y un RTO de 4 horas, y esos "
                    "dos numeros nunca se midieron: son estimaciones presentadas como compromisos. "
                    "El caso muestra el resultado de esa confusion con cinco copias en vez de "
                    "una.\n\n"
                    "**El tercero: supuse que auditar los cambios era auditar todo.** `audit_cita`, "
                    "de la Clase 4, registra los `UPDATE` de estado. **Un `DELETE` no dejaba "
                    "rastro**, asi que el evento mas destructivo era el unico sin traza. Es el "
                    "patron del caso otra vez: los controles cubrian lo que se esperaba que "
                    "pasara.\n\n"
                    "### 3. Actualizacion del informe del PI\n\n"
                    "El analisis entra en la seccion de **seguridad y control de acceso**, como una "
                    "subseccion nueva —«Analisis de un incidente real y mejoras derivadas»— con la "
                    "tabla de tres filas como cierre, y se referencia desde la seccion de "
                    "**respaldo y recuperacion**, donde la mejora 3 pasa a ser la prueba de "
                    "aceptacion del plan en lugar de una intencion. Los dos scripts nuevos entran "
                    "en el orden de ejecucion: el buscador seguro va con las funciones de la API "
                    "—despues de `06_api.sql`— y el archivo de borrados con el resto de triggers.\n\n"
                    "**Las dos frases que agrego a lecciones aprendidas:**\n\n"
                    "> Un respaldo que no se ha restaurado no es un respaldo: es un archivo con un "
                    "nombre tranquilizador. Lo unico que cuenta como control es la restauracion "
                    "verificada con conteos y rangos.\n\n"
                    "> Una funcion de solo lectura tambien es una puerta. "
                    "`buscar_mascota_insegura` no escribia nada, no aparecia en ninguna revision "
                    "por eso mismo, y entregaba la base completa —incluidos los correos de los "
                    "clientes— a quien escribiera una comilla en el buscador."
                ),
                "como_calificar": [
                    "**6 pts — la tabla con exactamente tres filas y las ocho columnas,** 2 pts por "
                    "fila. Dentro de cada fila: 0,5 que la mejora sea concreta, 0,5 que la columna "
                    "de objeto nombre un **objeto real** de la base —tabla, funcion, trigger, "
                    "indice, rol—, 0,5 el riesgo que mitiga, 0,5 esfuerzo e impacto. Una fila que "
                    "diga «mejorar la seguridad» en objeto vale 0,5 de 2: la rubrica exige objetos, "
                    "no intenciones. Mas o menos de tres filas incumple el enunciado.",
                    "**4 pts — que dos filas esten en `IMPLEMENTADA` y citen la prueba real que se "
                    "corrio** en las preguntas 2 y 3, 2 pts cada una. La cita tiene que ser "
                    "verificable: «el ataque contra `buscar_mascota_segura` devuelve 0 filas frente "
                    "a las 8 de la insegura», «la consulta de validacion devolvio 10 | 10 | "
                    "`RESTAURACION OK`». «Lo probe y funciono» vale 0,5 de 2. Este es el punto que "
                    "convierte la tabla en un informe de trabajo hecho y no en una lista de deseos.",
                    "**2 pts — la tercera fila en `PENDIENTE` con responsable y fecha,** 1 pt cada "
                    "uno. La fecha tiene que ser anterior al **2026-11-16**, que es la "
                    "sustentacion, y conviene revisar que no caiga el 2026-11-09, que es el Parcial "
                    "3. Un «pendiente» sin fecha no es un plan.",
                    "**2 pts — la priorizacion argumentada con esfuerzo/impacto,** no por gusto ni "
                    "por orden de aparicion. Se acepta cualquier orden bien defendido. Se reconoce "
                    "como sobresaliente separar los dos criterios que aqui apuntan distinto: por "
                    "esfuerzo/impacto gana la mejora 1 —esfuerzo bajo, impacto alto—, y por "
                    "urgencia tambien, porque es la unica que cierra un agujero **activo** frente a "
                    "dos que mitigan un incidente futuro.",
                    "**1 pt — el supuesto de diseno que el caso puso en evidencia,** formulado como "
                    "supuesto y no como tarea. «Me falta probar el respaldo» es una tarea; «supuse "
                    "que tener una copia era poder recuperar» es un supuesto, y es lo que se pide. "
                    "Se reconoce como sobresaliente el que casi nadie ve: **la capa `api_*` de la "
                    "Clase 12 no cerraba la inyeccion**, porque solo cubria las escrituras, y el "
                    "agujero estaba en una funcion de solo lectura que nadie reviso justamente por "
                    "«solo consultar».",
                    "**La actualizacion del informe se califica dentro de los puntos anteriores** y "
                    "lo que se busca es que nombre una seccion existente y una frase concreta para "
                    "lecciones aprendidas, no un «lo agrego al informe». Y conviene contrastar: si "
                    "la tabla declara el respaldo resuelto mientras el checklist de la Clase 11 lo "
                    "tiene en `NO`, hay una contradiccion entre dos entregables del mismo "
                    "estudiante, y es mejor senalarla al calificar que dejarla para el jurado.",
                ],
                "errores": [
                    "**Filas con intenciones en vez de objetos:** «mejorar la seguridad de la base», "
                    "«hacer respaldos». La rubrica pide un objeto real —`buscar_mascota_segura`, "
                    "`trg_archivar_cita`, `idx_cita_vet_fecha`, `app_vetcare`— porque un plan de "
                    "mejoras cuya unidad no es un objeto no se puede verificar ni asignar.",
                    "**Marcar `IMPLEMENTADA` sin citar la prueba,** o citando una que no se corrio. "
                    "Es lo mismo que declaro resuelto el respaldo en el caso analizado. La columna "
                    "de verificacion pide el numero: 8 → 0, 0 y 10, `RESTAURACION OK`.",
                    "**Una tercera fila con estado `PENDIENTE` y sin responsable ni fecha,** o con "
                    "una fecha posterior al 2026-11-16. Un pendiente sin fecha se convierte en un "
                    "pendiente permanente, que es como el item del respaldo llego hasta aqui.",
                    "**Priorizar por gusto:** «haria primero la 1 porque es la que mas me "
                    "interesa». El enunciado pide la relacion esfuerzo/impacto, y es una "
                    "herramienta, no un formalismo: obliga a comparar el costo de hacer con el "
                    "costo de no hacer.",
                    "**Confundir el supuesto con la tarea.** «Me falta ensayar el restore» es lo "
                    "que hay que hacer; el supuesto es el que llevo a no hacerlo: «supuse que tener "
                    "el respaldo era suficiente». La pregunta apunta al segundo, porque es el que "
                    "se repite en el proyecto siguiente.",
                    "**Repetir una de las mejoras ya implementadas como la tercera fila** con otras "
                    "palabras, para no tener que pensar una pendiente. Se detecta rapido: las tres "
                    "filas deben nombrar objetos distintos.",
                    "**Elegir el caso B en la pregunta 1 y despues no poder llenar las dos filas "
                    "`IMPLEMENTADA`.** El enunciado permite B pero las preguntas 2 y 3 implementan "
                    "mejoras de C y de A. La salida limpia es citar como implementada la mejora de "
                    "rendimiento de la Clase 6 —`idx_cita_vet_fecha` con sus dos `EXPLAIN`— y "
                    "decirlo asi en la tabla.",
                ],
            },
        ],
        "preguntas_frecuentes": [
            ("Es una clase autonoma y no hay quien me responda en el momento. ¿Que hago si me "
             "trabo?",
             "Todo lo que necesitas esta en el enunciado —incluidas las cadenas de ataque y el "
             "cuerpo de la funcion segura— y las tres cosas que trancan a mas gente estan "
             "resueltas en estas preguntas frecuentes: el error de ambiguedad de "
             "`buscar_mascota_directa`, el `RETURN NEW` que cancela el borrado y el orden del "
             "`DROP`. La sesion es el **2026-11-02**; el **2026-11-09** es el Parcial 3 y el "
             "**2026-11-16** la sustentacion, asi que no cuentes con una clase posterior para "
             "aclarar dudas: si algo no sale, entrega lo que tengas con una nota de que fallo y por "
             "donde ibas. Un entregable con un problema documentado se califica; uno en blanco, "
             "no."),
            ("¿Es legal ejecutar estos ataques? ¿Me puedo meter en problemas?",
             "Lo que haces aqui es ejecutarlos contra **tu propia** base de practica en ExamLab: es "
             "tuya, es desechable y se vuelve a sembrar en cada pregunta. Eso es igual que probar "
             "un candado en tu propia puerta. Lo que **no** puedes hacer —y esto no es una "
             "formalidad academica sino la ley— es probar la misma cadena contra un sistema que no "
             "es tuyo y sin autorizacion escrita, aunque «solo sea para ver si es vulnerable». El "
             "objetivo de la pregunta es el paso 5: demostrar que el agujero quedo cerrado. La "
             "evidencia que se califica es el **0 filas**, no el 8."),
            ("Mi ataque devuelve 1 fila en vez de 8. ¿La funcion no es vulnerable?",
             "Lo es; lo que pasa es que la cadena no llego como querias. En SQL, para escribir una "
             "comilla simple dentro de una cadena hay que **duplicarla**, asi que el ataque se "
             "escribe `buscar_mascota_insegura('Firulais'' OR ''1''=''1')` —con dos comillas "
             "seguidas en cada sitio—. Si escribes una sola, o el motor se queja de sintaxis o la "
             "funcion recibe un nombre literal que no existe. Para verlo claro, sigue los dos "
             "niveles: la cadena **enviada** es `Firulais' OR '1'='1`, y el texto que la funcion "
             "acaba construyendo es `... WHERE nombre = 'Firulais' OR '1'='1'`."),
            ("Escribi `buscar_mascota_directa` como dice el enunciado y me da «column reference "
             "“id_mascota” is ambiguous». ¿Esta mal el enunciado?",
             "El enunciado sugiere la idea correcta y le falta un detalle. Los nombres del "
             "`RETURNS TABLE (id_mascota INT, nombre TEXT, ...)` son **variables de PL/pgSQL**, asi "
             "que dentro de una consulta estatica `id_mascota` puede referirse a la columna o a la "
             "variable, y PostgreSQL no adivina: falla. Se arregla calificando las columnas con un "
             "alias de tabla —`SELECT m.id_mascota, m.nombre, m.especie, m.activa FROM mascota m "
             "WHERE m.nombre = p_nombre`—. Y fijate en algo interesante: la version con `EXECUTE` "
             "**no** tiene este problema, porque su cadena se entrega al motor sin sustitucion de "
             "variables. Es una diferencia real entre las dos formas y vale la pena entenderla en "
             "vez de volver al `EXECUTE` por miedo."),
            ("Hice el `DELETE FROM cita;` y `cita` sigue con 10 filas, aunque `cita_borrada` "
             "tambien tiene 10. ¿Funciono?",
             "No, y este es el error mas enganoso del taller. Tu funcion de trigger termina en "
             "`RETURN NEW` —o no tiene `RETURN`—, y en un trigger de `DELETE` **`NEW` vale "
             "`NULL`**. Un trigger `BEFORE` que devuelve `NULL` **cancela la operacion**, asi que "
             "la fila se archivo y el borrado no ocurrio: mira el mensaje del motor, dice "
             "`DELETE 0`. Cambia la ultima linea por `RETURN OLD;`. Y aprovecha el susto, porque la "
             "leccion es de la clase: tu control no «evito el borrado», rompio el `DELETE`. Un "
             "control que impide la operacion legitima no es seguridad, es una averia."),
            ("Si ya tengo el trigger que archiva, ¿para que la consulta de verificacion? Ya se que "
             "el dato esta ahi.",
             "Porque son controles de tipos distintos y ninguno hace el trabajo del otro. El "
             "trigger es **recuperacion**: no evita nada —el `DELETE` se ejecuta y `cita` queda en "
             "0— y lo que consigue es que el dano sea reversible. La consulta es **verificacion**: "
             "no protege ningun dato, comprueba una afirmacion, y responde «¿la restauracion quedo "
             "completa?» con numeros comparables en vez de una impresion. El caso analizado tenia "
             "cinco copias y ninguna verificacion, y perdio datos igual. Fijate ademas en que la "
             "consulta pide `MIN` y `MAX` y no solo el conteo: un conteo correcto con un rango "
             "desplazado significa que restauraste otra cosa, y el conteo solo no te lo diria."),
            ("¿El trigger me protege de cualquier perdida de citas?",
             "No, y conviene saber exactamente de que no protege. **No se dispara con "
             "`TRUNCATE cita;`**, porque un trigger `FOR EACH ROW` necesita recorrer filas y "
             "`TRUNCATE` no las recorre —eso se cierra con un trigger `BEFORE TRUNCATE ... FOR EACH "
             "STATEMENT`, y en la solucion esta—. No se dispara con `DROP TABLE`. No hace nada si "
             "alguien ejecuta `ALTER TABLE cita DISABLE TRIGGER trg_archivar_cita`. Y lo mas "
             "importante: `cita_borrada` y `respaldo_cita` viven en la **misma** base que `cita`, "
             "asi que si se pierde la instancia o el disco, se pierde todo junto. Protege contra un "
             "error logico, que es mucho, y no contra perder el servidor. Eso lo cubre un respaldo "
             "fisico externo, y es la mejora pendiente de la pregunta 5."),
            ("¿Puedo elegir el caso B, el de rendimiento?",
             "Puedes, y conviene que sepas lo que te vas a encontrar: las preguntas 2 y 3 "
             "implementan mejoras del caso C —inyeccion— y del caso A —respaldo—, asi que en la "
             "pregunta 5, donde dos de las tres filas deben ser mejoras «ya implementadas», no "
             "tendras nada de tu propio caso. La salida limpia es citar el trabajo de la Clase 6 "
             "como tu mejora implementada de rendimiento: el `EXPLAIN` con `Seq Scan` y "
             "`Rows Removed by Filter`, el indice `idx_cita_vet_fecha` y el segundo `EXPLAIN` con "
             "`Index Cond`. Si prefieres que todo el taller cuente la misma historia, elige A o C."),
        ],
        "cierre": [
            "Al terminar, cada estudiante debe tener: el **analisis del caso** con la causa raiz "
            "separada de la aparente y traducida a un objeto concreto de VetCare; el **contraste "
            "8 → 0** con `buscar_mascota_segura` creada, probada en los dos sentidos y la funcion "
            "vulnerable eliminada; el **control de borrados completo** —bitacora con el conteo "
            "calculado, `cita_borrada`, `trg_archivar_cita`, el `DELETE` que deja 0 y 10, la "
            "restauracion con columnas explicitas y la fila `RESTAURACION OK`—; las **cuatro "
            "opciones correctas** de la pregunta 4; y la **tabla de tres mejoras** con dos "
            "`IMPLEMENTADA` que citan su prueba y una `PENDIENTE` con responsable y fecha anterior "
            "al 2026-11-16.",
            "Cuatro comprobaciones antes de entregar, todas de mirar un numero. Que el `COUNT` del "
            "ataque contra la funcion insegura sea **8** y contra la segura **0**, y que "
            "`buscar_mascota_segura('Firulais')` siga devolviendo **1** —si devuelve 0, cerraste el "
            "buscador, no el agujero—. Que despues del `DELETE` sea `cita` = **0** y "
            "`cita_borrada` = **10**; si las dos dan 10, tu trigger devuelve `NULL` y cancelo el "
            "borrado. Que la consulta de validacion devuelva **una sola fila** con el veredicto "
            "**calculado** por un `CASE` y no escrito a mano. Y que el `DROP FUNCTION` sea la "
            "ultima linea del script de la pregunta 2, porque si va antes ya no puedes demostrar el "
            "incidente.",
            "La clase deja dos ideas y las dos vienen del mismo sitio. La primera: **el control no "
            "es la copia, es la restauracion verificada.** Cinco respaldos que nadie probo no "
            "sumaron cinco oportunidades de recuperar; sumaron cinco razones para no probar "
            "ninguna, y la diferencia entre «tengo respaldo» y «puedo recuperar» costo seis horas "
            "de datos que no volvieron. La segunda es la que sale de la pregunta 2 y es mas "
            "incomoda, porque toca lo que ya creiamos resuelto: **una funcion de solo lectura "
            "tambien es una puerta.** La capa `api_*` de la Clase 12 blindo las escrituras, que son "
            "las que revisamos, y el agujero grave del proyecto estaba en una funcion que «solo "
            "consultaba» —y que entregaba la base completa, con los correos de los clientes, a "
            "quien escribiera una comilla en el buscador—. El **2026-11-09** es el Parcial 3 y el "
            "**2026-11-16** la sustentacion: de las tres mejoras de hoy, dos quedan cerradas y la "
            "unica pendiente es la misma que viene abierta desde la Clase 11. Ya no es un "
            "hallazgo: es una decision.",
        ],
    },

    15: {
        "titulo": "Solucion del taller · Clase 15 · Entrega final y cierre de VetCare DB",
        "resumen": (
            "El **script maestro de referencia** completo —siete bloques que corren de arriba abajo "
            "sobre una base limpia sin un solo error, con los `CHECK` nombrados, los totales de "
            "factura **calculados** en vez de escritos, las tres pruebas de aceptacion (dos "
            "negativas y una positiva, que no se escriben igual) y el inventario que cierra en "
            "`5 | 8 | 3 | 8 | 2 | 4 | 2 | 4 | 1`—; los **cuatro KPIs** resueltos con sus numeros "
            "exactos, incluida la trampa de que la semilla del banco **no** ejerce las tres "
            "condiciones de borde que la rubrica exige y como forzarlas con tres `INSERT`; la clave "
            "razonada del checklist del ZIP; el acta de entrega con inventario, trazabilidad de las "
            "once clases y un guion de **7 minutos**; y la autoevaluacion modelo, con las tres "
            "diferencias PL/SQL → PL/pgSQL y la lista honesta de lo que este entorno no permitio "
            "verificar."
        ),
        "total": 100,
        "nota_actividad": (
            "**Sesion 13, lunes 2026-11-16: sustentacion.** Este taller es la **evaluacion final "
            "del PI, 20 % del Corte 3**, y tiene que estar entregado **antes** del turno de cada "
            "estudiante: el bloque de dos horas se consume en las presentaciones, asi que no hay "
            "tiempo de aula para escribir el script. Conviene publicarlo con el taller de la Clase "
            "13 —el 2026-11-02— para que el 2026-11-09, dia del Parcial 3, ya este cerrado. **El "
            "motor es PostgreSQL, no Oracle:** nada de `NUMBER`, `VARCHAR2`, "
            "`RAISE_APPLICATION_ERROR`, `DUAL`, `SQL%ROWCOUNT` ni `/` de terminacion.\n\n"
            "**Cuatro cosas que hay que decir antes de que empiecen, porque cuestan puntos por "
            "sorpresa.** (1) La pregunta 1 se califica **ejecutando** el script sobre una base "
            "limpia: un solo error de sintaxis a la mitad deja los bloques siguientes sin correr, y "
            "por eso vale la pena exigir que lo prueben de cero al menos una vez —la base de "
            "ExamLab se vuelve a sembrar en cada intento, asi que se puede—. (2) `entrega_final` "
            "**ya trae una fila de ejemplo** del docente: la del estudiante es la `id_entrega = 2`, "
            "y quien la borre para «dejarlo limpio» esta modificando la semilla, no entregando. (3) "
            "Para tener dos facturas hacen falta al menos dos `consulta`, y "
            "`consulta.id_cita` es **UNIQUE**: dos citas distintas y atendidas. Es la cadena de "
            "dependencias que rompe mas semillas. (4) Las tres pruebas del bloque 5 **no se "
            "escriben igual**: las dos primeras esperan un error y la tercera espera un efecto; "
            "envolver la tercera en un `EXCEPTION WHEN OTHERS` no prueba nada.\n\n"
            "**Y un defecto de la semilla de la pregunta 2 que conviene anunciar,** porque si no, "
            "la mitad del grupo cree que se equivoco. La rubrica exige que K1 conserve los "
            "veterinarios **sin citas** y que K3 incluya los insumos **nunca vendidos**, pero en "
            "los datos entregados **los cuatro veterinarios tienen citas y los seis insumos se han "
            "vendido**: la consulta correcta y la incorrecta devuelven exactamente lo mismo. Igual "
            "pasa con el «ordena cronologicamente» de K2, donde las tres facturas caen en el mismo "
            "mes y solo hay una fila. Lo razonable es pedir que el estudiante **cree** el caso de "
            "borde con tres `INSERT` —un veterinario nuevo, un insumo nuevo y una factura en "
            "octubre— y muestre las dos corridas; la solucion lo hace asi y son 6 de los 20 puntos. "
            "Ademas, hay que saberlo al calificar: **las tres facturas de la semilla estan "
            "descuadradas** —`factura.total` no coincide con `consulta.precio` mas la suma del "
            "detalle, ni con la suma del detalle sola—, exactamente la misma inconsistencia que la "
            "prueba 5 de la Clase 11. K2 reporta `factura.total`, que es lo que pide el enunciado, "
            "y el estudiante que lo note merece reconocimiento, no correccion. Las preguntas 4 y 5 "
            "son sobre el paquete y el proceso de cada estudiante: lo que sigue es un **modelo de "
            "referencia y no una clave**."
        ),
        "preguntas": [
            {
                "n": 1,
                "titulo": "Script maestro de entrega: VetCare DB de cero, en una sola corrida",
                "tipo": "bd_sql",
                "puntos": 35,
                "sql": """-- ======================================================================
-- VETCARE DB - SCRIPT MAESTRO DE ENTREGA
-- Bases de Datos II - FI303215 - Periodo 2026-2
-- Motor: PostgreSQL. Se ejecuta UNA vez, de arriba abajo, sobre base limpia.
--
-- Regla que gobierna todo el archivo: si hay que ejecutarlo dos veces o en
-- otro orden, no es un script maestro. Y si un numero se puede calcular,
-- no se escribe a mano -- esa es la leccion de las Clases 11 y 13.
-- ======================================================================

-- ======================================================================
-- BLOQUE 0 - REGISTRO DE LA ENTREGA
--
-- entrega_final YA trae una fila de ejemplo del docente. La del estudiante
-- es la id_entrega = 2. No se borra la del docente: modificar la semilla
-- no es entregar.
-- ======================================================================
INSERT INTO entrega_final (estudiante, codigo, proyecto, enlace_zip, integrantes)
VALUES ('Nombre Completo Del Estudiante', '1234567',
        'VetCare DB - Sistema de gestion para clinica veterinaria',
        'https://drive.google.com/mi-entrega-vetcare.zip',
        NULL);   -- NULL porque trabajo solo; si hubo equipo autorizado, va la lista

SELECT id_entrega, estudiante, codigo, proyecto, fecha_entrega
  FROM entrega_final ORDER BY id_entrega;   -- 2 filas: la del docente y la mia

-- ======================================================================
-- BLOQUE 1 - DDL COMPLETO (8 tablas + auditoria)
--
-- Las restricciones CHECK van con NOMBRE propio, y no es cosmetica: el
-- nombre aparece en el mensaje de error, y es lo que permite que la
-- aplicacion traduzca "ck_insumo_stock" a "stock insuficiente" en vez de
-- mostrarle al usuario el texto crudo del motor (Clase 12). Con nombres
-- automaticos el mensaje depende de como los genere el servidor.
-- ======================================================================
CREATE TABLE dueno (
  id_dueno SERIAL PRIMARY KEY,
  nombre   TEXT NOT NULL,
  telefono TEXT,
  email    TEXT,
  ciudad   TEXT DEFAULT 'Cali'
);

CREATE TABLE veterinario (
  id_veterinario SERIAL PRIMARY KEY,
  nombre         TEXT NOT NULL,
  especialidad   TEXT,
  activo         CHAR(1) NOT NULL DEFAULT 'S'
                 CONSTRAINT ck_veterinario_activo CHECK (activo IN ('S','N'))
);

CREATE TABLE mascota (
  id_mascota SERIAL PRIMARY KEY,
  id_dueno   INT  NOT NULL REFERENCES dueno(id_dueno),
  nombre     TEXT NOT NULL,
  especie    TEXT NOT NULL,
  fecha_nac  DATE,
  activa     CHAR(1) NOT NULL DEFAULT 'S'
             CONSTRAINT ck_mascota_activa CHECK (activa IN ('S','N'))
);

CREATE TABLE cita (
  id_cita        SERIAL PRIMARY KEY,
  id_mascota     INT NOT NULL REFERENCES mascota(id_mascota),
  id_veterinario INT NOT NULL REFERENCES veterinario(id_veterinario),
  fecha_hora     TIMESTAMP NOT NULL,
  estado         TEXT NOT NULL DEFAULT 'PROGRAMADA'
                 CONSTRAINT ck_cita_estado
                 CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))
);

-- id_cita es UNIQUE: una cita genera como maximo una consulta. Es una regla
-- de negocio, no un detalle tecnico, y es la que obliga a que dos facturas
-- necesiten dos citas atendidas distintas.
CREATE TABLE consulta (
  id_consulta SERIAL PRIMARY KEY,
  id_cita     INT NOT NULL UNIQUE REFERENCES cita(id_cita),
  diagnostico TEXT,
  precio      NUMERIC(12,2) NOT NULL
              CONSTRAINT ck_consulta_precio CHECK (precio >= 0)
);

CREATE TABLE insumo (
  id_insumo   SERIAL PRIMARY KEY,
  nombre      TEXT NOT NULL,
  stock       INT NOT NULL CONSTRAINT ck_insumo_stock CHECK (stock >= 0),
  precio_unit NUMERIC(12,2) NOT NULL
              CONSTRAINT ck_insumo_precio CHECK (precio_unit >= 0)
);

CREATE TABLE factura (
  id_factura  SERIAL PRIMARY KEY,
  id_consulta INT NOT NULL REFERENCES consulta(id_consulta),
  fecha       TIMESTAMP NOT NULL DEFAULT now(),
  total       NUMERIC(12,2) NOT NULL DEFAULT 0
              CONSTRAINT ck_factura_total CHECK (total >= 0)
);

-- ON DELETE CASCADE solo en id_factura: borrar una factura se lleva sus
-- lineas, porque una linea sin factura no significa nada. Pero NO en
-- id_insumo: borrar un insumo no puede borrar el historial de ventas.
CREATE TABLE detalle_factura (
  id_detalle  SERIAL PRIMARY KEY,
  id_factura  INT NOT NULL REFERENCES factura(id_factura) ON DELETE CASCADE,
  id_insumo   INT NOT NULL REFERENCES insumo(id_insumo),
  cantidad    INT NOT NULL CONSTRAINT ck_detalle_cantidad CHECK (cantidad > 0),
  precio_unit NUMERIC(12,2) NOT NULL
              CONSTRAINT ck_detalle_precio CHECK (precio_unit >= 0)
);

-- Auditoria. A PROPOSITO sin FK a cita: la bitacora tiene que sobrevivir a
-- lo que audita. Si manana se borra una cita, una FK impediria conservar su
-- traza justo cuando es lo unico que queda (Clases 4 y 13).
CREATE TABLE audit_cita (
  id_audit       SERIAL PRIMARY KEY,
  id_cita        INT  NOT NULL,
  accion         TEXT NOT NULL,
  valor_anterior TEXT,
  valor_nuevo    TEXT,
  usuario_bd     TEXT      NOT NULL DEFAULT current_user,
  fecha_evento   TIMESTAMP NOT NULL DEFAULT now()
);

-- ======================================================================
-- BLOQUE 2 - DATOS SEMILLA
-- 5 duenos, 3 veterinarios, 8 mascotas (2 inactivas), 8 citas en los tres
-- estados, 2 consultas, 4 insumos (1 con stock < 5), 2 facturas, 4 detalles.
-- ======================================================================
INSERT INTO dueno (nombre, telefono, email) VALUES
  ('Ana Gomez',     '3001112233', 'ana.gomez@mail.com'),
  ('Carlos Ruiz',   '3014445566', 'carlos.ruiz@mail.com'),
  ('Marcela Diaz',  '3027778899', 'marcela.diaz@mail.com'),
  ('Jorge Pineda',  '3105551212', 'jorge.pineda@mail.com'),
  ('Luisa Cardona', '3123334455', 'luisa.cardona@mail.com');

INSERT INTO veterinario (nombre, especialidad) VALUES
  ('Laura Restrepo', 'General'),
  ('Diego Moreno',   'Cirugia'),
  ('Paula Salazar',  'Dermatologia');

-- Rocky (3) y Kiara (8) quedan INACTIVAS: son las que usa la prueba 1.
INSERT INTO mascota (id_dueno, nombre, especie, fecha_nac, activa) VALUES
  (1, 'Firulais', 'Canino', DATE '2019-04-12', 'S'),
  (1, 'Luna',     'Felino', DATE '2021-08-30', 'S'),
  (2, 'Rocky',    'Canino', DATE '2015-01-20', 'N'),
  (3, 'Mishi',    'Felino', DATE '2022-11-05', 'S'),
  (3, 'Bobby',    'Canino', DATE '2018-06-17', 'S'),
  (4, 'Nube',     'Felino', DATE '2023-02-09', 'S'),
  (5, 'Toby',     'Canino', DATE '2020-09-25', 'S'),
  (5, 'Kiara',    'Canino', DATE '2013-03-03', 'N');

-- 8 citas: 4 PROGRAMADA, 3 ATENDIDA, 1 CANCELADA -> los tres estados.
INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, estado) VALUES
  (1, 1, TIMESTAMP '2026-09-01 08:00:00', 'PROGRAMADA'),
  (2, 1, TIMESTAMP '2026-09-01 09:00:00', 'ATENDIDA'),
  (4, 2, TIMESTAMP '2026-09-01 10:00:00', 'PROGRAMADA'),
  (5, 3, TIMESTAMP '2026-09-02 08:30:00', 'CANCELADA'),
  (6, 2, TIMESTAMP '2026-09-02 11:00:00', 'ATENDIDA'),
  (7, 3, TIMESTAMP '2026-09-03 07:45:00', 'PROGRAMADA'),
  (1, 1, TIMESTAMP '2026-09-05 15:00:00', 'ATENDIDA'),
  (2, 2, TIMESTAMP '2026-09-08 16:00:00', 'PROGRAMADA');

-- Dos consultas sobre dos citas ATENDIDAS distintas (id_cita es UNIQUE).
INSERT INTO consulta (id_cita, diagnostico, precio) VALUES
  (2, 'Vacunacion triple felina', 40000),
  (5, 'Control de peso',          38000);

-- El insumo 2 queda con stock 3 (< 5): es el que usa la prueba 2.
INSERT INTO insumo (nombre, stock, precio_unit) VALUES
  ('Vacuna antirrabica',   12, 22000),
  ('Vacuna triple felina',  3, 31000),
  ('Antiparasitario oral', 40,  9500),
  ('Gasa esteril',          8,  1200);

-- Las facturas nacen en 0 y su total se CALCULA abajo. Escribirlo a mano es
-- lo que dejo las facturas descuadradas del banco de la Clase 11: el numero
-- guardado y el numero derivado dejan de coincidir y nadie se entera.
INSERT INTO factura (id_consulta, fecha, total) VALUES
  (1, TIMESTAMP '2026-09-01 09:40:00', 0),
  (2, TIMESTAMP '2026-09-02 11:35:00', 0);

INSERT INTO detalle_factura (id_factura, id_insumo, cantidad, precio_unit) VALUES
  (1, 2, 1, 31000),
  (1, 4, 2,  1200),
  (2, 3, 1,  9500),
  (2, 1, 1, 22000);

UPDATE factura f
   SET total = (SELECT c.precio FROM consulta c WHERE c.id_consulta = f.id_consulta)
             + COALESCE((SELECT SUM(d.cantidad * d.precio_unit)
                           FROM detalle_factura d
                          WHERE d.id_factura = f.id_factura), 0);
-- factura 1 = 40000 + (31000 + 2400) = 73400
-- factura 2 = 38000 + ( 9500 + 22000) = 69500

-- ======================================================================
-- BLOQUE 3 - LOGICA DE NEGOCIO
-- ======================================================================

-- Funcion pura: mismo argumento, mismo resultado siempre. Por eso se puede
-- declarar IMMUTABLE y el planificador la evalua una sola vez.
CREATE FUNCTION fn_precio_consulta(p_especialidad TEXT)
RETURNS NUMERIC
LANGUAGE plpgsql
IMMUTABLE
AS $fn$
BEGIN
  RETURN CASE p_especialidad
           WHEN 'Cirugia'      THEN 120000
           WHEN 'Dermatologia' THEN  65000
           ELSE                       40000
         END;
END;
$fn$;

SELECT fn_precio_consulta('Cirugia')      AS cirugia,       -- 120000
       fn_precio_consulta('Dermatologia') AS dermatologia,  --  65000
       fn_precio_consulta('General')      AS general;       --  40000

-- Procedimiento de negocio con validacion. La regla del PI vive AQUI y no
-- en la aplicacion: asi la cumple cualquiera que se conecte, no solo quien
-- pase por la interfaz.
CREATE PROCEDURE sp_agendar_cita(p_id_mascota     INT,
                                 p_id_veterinario INT,
                                 p_fecha          TIMESTAMP)
LANGUAGE plpgsql
AS $proc$
DECLARE
  v_activa CHAR(1);
BEGIN
  SELECT m.activa INTO v_activa
    FROM mascota m WHERE m.id_mascota = p_id_mascota;

  -- IF NOT FOUND funciona porque el SELECT es de una columna a una
  -- variable. Despues de un SELECT COUNT(*) INTO nunca seria verdadero:
  -- COUNT siempre devuelve una fila, aunque valga 0 (Clase 3).
  IF NOT FOUND THEN
    RAISE EXCEPTION 'La mascota % no existe', p_id_mascota;
  END IF;

  IF v_activa <> 'S' THEN
    RAISE EXCEPTION 'La mascota % esta inactiva: no se puede agendar', p_id_mascota;
  END IF;

  INSERT INTO cita (id_mascota, id_veterinario, fecha_hora)
  VALUES (p_id_mascota, p_id_veterinario, p_fecha);
END;
$proc$;

-- Trigger de auditoria: DOS objetos, la funcion y la asociacion.
CREATE FUNCTION fn_trg_audit_cita()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $fn$
BEGIN
  -- El IF hace falta aunque el trigger diga UPDATE OF estado: esa clausula
  -- se dispara cuando la columna se MENCIONA en el UPDATE, aunque el valor
  -- no cambie. Sin el IF, un "SET estado = estado" ensuciaria la bitacora.
  IF NEW.estado IS DISTINCT FROM OLD.estado THEN
    INSERT INTO audit_cita (id_cita, accion, valor_anterior, valor_nuevo)
    VALUES (OLD.id_cita, 'CAMBIO_ESTADO', OLD.estado, NEW.estado);
  END IF;
  RETURN NEW;
END;
$fn$;

-- AFTER, no BEFORE: se audita lo que YA ocurrio. Si la fila termina no
-- cambiando por otro motivo, no queremos un registro que diga que cambio.
CREATE TRIGGER trg_audit_cita
  AFTER UPDATE OF estado ON cita
  FOR EACH ROW
  EXECUTE FUNCTION fn_trg_audit_cita();

-- ======================================================================
-- BLOQUE 4 - INDICES
--
-- PostgreSQL crea indice para la PK y para UNIQUE, y NO lo crea para las
-- llaves foraneas. Los indices de abajo no son decorativos: son las
-- columnas por las que filtran los reportes de la pregunta 2.
-- ======================================================================

-- Reporte de agenda por veterinario y rango de fechas (Clase 6). El orden
-- de las columnas importa: igualdad antes que rango.
CREATE INDEX idx_cita_vet_fecha ON cita (id_veterinario, fecha_hora);

-- Historia clinica por mascota (KPI 4) y apoyo a la FK.
CREATE INDEX idx_cita_mascota ON cita (id_mascota);

-- Indice PARCIAL: la bandeja de pendientes solo consulta las PROGRAMADA,
-- que son una fraccion de la tabla. Mas pequeno, mas barato de mantener y
-- solo se usa cuando la consulta trae el mismo WHERE (Clase 7).
CREATE INDEX idx_cita_programada ON cita (fecha_hora)
  WHERE estado = 'PROGRAMADA';

-- ======================================================================
-- BLOQUE 5 - PRUEBAS DE ACEPTACION DE LAS TRES REGLAS DEL PI
--
-- OJO A LA ASIMETRIA, que es lo que se califica de verdad: las pruebas 1 y
-- 2 son NEGATIVAS -- lo correcto es que revienten -- y la 3 es POSITIVA
-- -- lo correcto es que ocurra un efecto --. Envolver la 3 en un
-- EXCEPTION WHEN OTHERS y no comprobar nada no prueba absolutamente nada:
-- un bloque que no falla imprimiria "OK" tambien con el trigger borrado.
--
-- Cada bloque DO abre una subtransaccion, asi que cuando el handler corre,
-- lo que la prueba intento ya se deshizo (Clase 8). Por eso estas pruebas
-- no dejan basura en la base.
-- ======================================================================

-- PRUEBA 1: una mascota inactiva no puede agendar cita.
DO $$
BEGIN
  CALL sp_agendar_cita(3, 1, TIMESTAMP '2026-09-20 10:00:00');   -- Rocky, inactiva
  RAISE NOTICE 'FALLO LA PRUEBA 1: se agendo cita a una mascota inactiva';
EXCEPTION WHEN OTHERS THEN
  -- RAISE EXCEPTION sin codigo propio produce SQLSTATE P0001, cuya
  -- condicion se llama raise_exception; aqui se captura con OTHERS porque
  -- es lo que pide el enunciado.
  RAISE NOTICE 'PRUEBA 1 OK -> %', SQLERRM;
END $$;

-- PRUEBA 2: el stock de un insumo no puede quedar negativo.
DO $$
BEGIN
  UPDATE insumo SET stock = stock - 100 WHERE id_insumo = 2;   -- stock actual 3
  RAISE NOTICE 'FALLO LA PRUEBA 2: el stock quedo negativo';
EXCEPTION WHEN check_violation THEN
  -- Aqui SI conviene la condicion precisa (SQLSTATE 23514) en vez de
  -- OTHERS: con OTHERS, un error de escritura en el nombre de la tabla
  -- tambien se reportaria como "PRUEBA 2 OK". Una prueba que pasa por el
  -- motivo equivocado es peor que una prueba que falla.
  RAISE NOTICE 'PRUEBA 2 OK -> %', SQLERRM;
END $$;

SELECT stock AS stock_del_insumo_2 FROM insumo WHERE id_insumo = 2;   -- 3

-- PRUEBA 3: un cambio de estado de cita queda auditado.
DO $$
DECLARE
  v_antes   INT;
  v_despues INT;
BEGIN
  SELECT COUNT(*) INTO v_antes FROM audit_cita;
  UPDATE cita SET estado = 'ATENDIDA' WHERE id_cita = 1;   -- estaba PROGRAMADA
  SELECT COUNT(*) INTO v_despues FROM audit_cita;

  IF v_despues = v_antes + 1 THEN
    RAISE NOTICE 'PRUEBA 3 OK -> audit_cita paso de % a % filas', v_antes, v_despues;
  ELSE
    RAISE NOTICE 'FALLO LA PRUEBA 3: audit_cita sigue en % filas', v_despues;
  END IF;
EXCEPTION WHEN OTHERS THEN
  RAISE NOTICE 'PRUEBA 3 CON ERROR -> %', SQLERRM;
END $$;

SELECT id_cita, accion, valor_anterior, valor_nuevo, usuario_bd
  FROM audit_cita ORDER BY id_audit;   -- 1 fila: 1 | CAMBIO_ESTADO | PROGRAMADA | ATENDIDA

-- ======================================================================
-- BLOQUE 6 - CONSULTA DE CIERRE: INVENTARIO DE LA ENTREGA
--
-- UNION ALL no garantiza orden, asi que el ORDER BY no es opcional si se
-- quiere una salida estable para pegar en el informe.
-- ======================================================================
  SELECT 'dueno'           AS tabla, COUNT(*) AS filas FROM dueno
UNION ALL SELECT 'veterinario',     COUNT(*) FROM veterinario
UNION ALL SELECT 'mascota',         COUNT(*) FROM mascota
UNION ALL SELECT 'cita',            COUNT(*) FROM cita
UNION ALL SELECT 'consulta',        COUNT(*) FROM consulta
UNION ALL SELECT 'insumo',          COUNT(*) FROM insumo
UNION ALL SELECT 'factura',         COUNT(*) FROM factura
UNION ALL SELECT 'detalle_factura', COUNT(*) FROM detalle_factura
UNION ALL SELECT 'audit_cita',      COUNT(*) FROM audit_cita
ORDER BY tabla;

-- ----------------------------------------------------------------------
-- 6b. EXTRA: verificar los minimos exigidos, en vez de afirmarlos
--
-- Es la misma idea de la Clase 13: "cumple los minimos" es una afirmacion,
-- y una afirmacion se verifica con una consulta. La ultima fila es la mas
-- interesante -- comprueba que ninguna factura este descuadrada --, y es la
-- que las facturas del banco de la Clase 11 no pasarian.
-- ----------------------------------------------------------------------
  SELECT 'mascotas inactivas (>= 2)' AS requisito, COUNT(*) AS valor,
         CASE WHEN COUNT(*) >= 2 THEN 'CUMPLE' ELSE 'REVISAR' END AS veredicto
    FROM mascota WHERE activa = 'N'
UNION ALL
  SELECT 'insumos con stock < 5 (>= 1)', COUNT(*),
         CASE WHEN COUNT(*) >= 1 THEN 'CUMPLE' ELSE 'REVISAR' END
    FROM insumo WHERE stock < 5
UNION ALL
  SELECT 'estados distintos de cita (>= 3)', COUNT(DISTINCT estado),
         CASE WHEN COUNT(DISTINCT estado) >= 3 THEN 'CUMPLE' ELSE 'REVISAR' END
    FROM cita
UNION ALL
  SELECT 'facturas descuadradas (debe ser 0)', COUNT(*),
         CASE WHEN COUNT(*) = 0 THEN 'CUMPLE' ELSE 'REVISAR' END
    FROM factura f
   WHERE f.total <> (SELECT c.precio FROM consulta c
                      WHERE c.id_consulta = f.id_consulta)
                  + COALESCE((SELECT SUM(d.cantidad * d.precio_unit)
                                FROM detalle_factura d
                               WHERE d.id_factura = f.id_factura), 0);

-- ======================================================================
-- FIN DEL SCRIPT MAESTRO
-- Lo que este script NO cubre, y esta declarado en el informe: el respaldo
-- fisico y su restauracion nunca se ensayaron, y el particionamiento se
-- diseno pero no se probo con volumen real. Se documenta porque un
-- entregable que oculta sus limites obliga al jurado a encontrarlos.
-- ======================================================================""",
                "salida": """BLOQUE 0 - Registro

INSERT 0 1

 id_entrega |          estudiante            | codigo  |          proyecto           | fecha_entrega
------------+--------------------------------+---------+-----------------------------+---------------
          1 | Ejemplo del docente            | 000000  | VetCare-Demo                | 2026-11-16
          2 | Nombre Completo Del Estudiante | 1234567 | VetCare DB - Sistema de ... | 2026-11-16

Dos filas, y la del estudiante es la 2. La fecha sale de CURRENT_DATE.

BLOQUE 2 - El UPDATE que calcula los totales

UPDATE 2

factura 1 = 40000 + 31000 + 2400 = 73400.00
factura 2 = 38000 +  9500 + 22000 = 69500.00

Ninguno de los dos numeros se escribio a mano, y por eso la ultima fila de la
verificacion 6b puede dar CUMPLE.

BLOQUE 3 - La funcion

 cirugia | dermatologia | general
---------+--------------+---------
  120000 |        65000 |   40000

BLOQUE 5 - Las tres pruebas de aceptacion

NOTICE:  PRUEBA 1 OK -> La mascota 3 esta inactiva: no se puede agendar
NOTICE:  PRUEBA 2 OK -> new row for relation "insumo" violates check constraint "ck_insumo_stock"
NOTICE:  PRUEBA 3 OK -> audit_cita paso de 0 a 1 filas

Las tres lineas empiezan con OK y ninguna dice FALLO: eso es el entregable del
bloque. Fijate en el mensaje de la prueba 2 -- trae el nombre "ck_insumo_stock"
porque la restriccion se nombro a proposito, y ese nombre es lo que la
aplicacion puede traducir a "stock insuficiente" sin mostrarle al usuario el
texto crudo del motor.

 stock_del_insumo_2
--------------------
                  3

Sigue en 3: el UPDATE de la prueba 2 se deshizo completo. El bloque DO abrio una
subtransaccion y el handler corrio DESPUES del retroceso -- es el mismo mecanismo
que hace atomica una funcion de facturacion (Clase 8).

 id_cita |    accion     | valor_anterior | valor_nuevo | usuario_bd
---------+---------------+----------------+-------------+------------
       1 | CAMBIO_ESTADO | PROGRAMADA     | ATENDIDA    | postgres

BLOQUE 6 - Inventario de la entrega (9 filas)

      tabla      | filas
-----------------+-------
 audit_cita      |     1
 cita            |     8
 consulta        |     2
 detalle_factura |     4
 dueno           |     5
 factura         |     2
 insumo          |     4
 mascota         |     8
 veterinario     |     3

Nueve filas, una por tabla. Y notese que audit_cita esta en 1 y no en 0: la
unica fila que tiene la puso la prueba 3. Un inventario con audit_cita en 0
significa que el trigger no se disparo, y entonces la prueba 3 no probo nada
aunque haya impreso OK.

6b - Verificacion de los minimos (4 filas)

              requisito              | valor | veredicto
-------------------------------------+-------+-----------
 mascotas inactivas (>= 2)           |     2 | CUMPLE
 insumos con stock < 5 (>= 1)        |     1 | CUMPLE
 estados distintos de cita (>= 3)    |     3 | CUMPLE
 facturas descuadradas (debe ser 0)  |     0 | CUMPLE

Los estados distintos siguen siendo 3 despues de la prueba 3: la cita 1 paso de
PROGRAMADA a ATENDIDA, pero quedan PROGRAMADA (3, 6, 8), ATENDIDA (1, 2, 5, 7) y
CANCELADA (4).

Si alguna fila dice REVISAR, la verificacion esta haciendo su trabajo y hay que
volver al bloque 2 antes de entregar. La ultima es la que mas importa: es la
unica que compara un dato guardado contra el mismo dato derivado, y es
exactamente la comprobacion que las facturas de la Clase 11 no pasaban.""",
                "como_calificar": [
                    "**6 pts — el script corre completo, de arriba abajo y sin un solo error, sobre "
                    "la base limpia.** Es la condicion de la que dependen los demas puntos y se "
                    "verifica ejecutandolo, no leyendolo. Si un `CREATE` de la mitad falla, todo lo "
                    "que venga despues tampoco corre: en ese caso se califica hasta donde llego y "
                    "se devuelve el mensaje de error exacto, que casi siempre es un `REFERENCES` a "
                    "una tabla que se crea mas abajo o un `INSERT` que viola una FK por orden. "
                    "Incluye los 2 pts del **Bloque 0**: el `INSERT` en `entrega_final` con datos "
                    "reales, y sin borrar la fila de ejemplo del docente.",
                    "**8 pts — Bloque 1, el DDL.** 4 pts las 8 tablas mas `audit_cita` con sus PK; "
                    "2 pts **todas** las FK —`mascota→dueno`, `cita→mascota`, `cita→veterinario`, "
                    "`consulta→cita`, `factura→consulta`, `detalle_factura→factura` y "
                    "`detalle_factura→insumo`—; 2 pts las cinco restricciones de dominio que el "
                    "enunciado enumera. Se reconoce como sobresaliente **nombrar** los `CHECK` "
                    "—`ck_insumo_stock`— porque el nombre viaja en el mensaje de error y es lo que "
                    "permite traducirlo a un mensaje de negocio (Clase 12); y justificar que "
                    "`audit_cita` no lleva FK, que el `ON DELETE CASCADE` va solo en `id_factura` y "
                    "que `consulta.id_cita` es `UNIQUE` porque es una regla de negocio.",
                    "**5 pts — Bloque 2, la semilla, contra los minimos del enunciado:** 5 duenos, "
                    "3 veterinarios, 8 mascotas con **2 inactivas**, 8 citas en distintos estados, "
                    "4 insumos con **uno de stock menor a 5**, 2 facturas con detalle. Se verifica "
                    "con el inventario del bloque 6, no contando a ojo. El fallo mas comun no es de "
                    "cantidad sino de **cadena de dependencias**: dos facturas exigen dos "
                    "`consulta`, y `consulta.id_cita` es `UNIQUE`, asi que exigen dos citas "
                    "atendidas distintas. Se reconoce como sobresaliente **calcular** el "
                    "`factura.total` con un `UPDATE` en vez de escribirlo: es la leccion de la "
                    "Clase 11 aplicada a la propia entrega.",
                    "**7 pts — Bloque 3, la logica.** 2 pts la funcion; 3 pts el procedimiento con "
                    "la validacion **efectiva** —que la prueba 1 lo demuestre, no que el `IF` este "
                    "escrito—; 2 pts el trigger de auditoria **como dos objetos**, la funcion "
                    "`RETURNS TRIGGER` y el `CREATE TRIGGER`. Se reconoce como sobresaliente "
                    "declarar la funcion `IMMUTABLE` con su razon, usar `AFTER` y no `BEFORE` para "
                    "auditar, y conservar el `IF NEW.estado IS DISTINCT FROM OLD.estado` explicando "
                    "que `UPDATE OF estado` se dispara cuando la columna se **menciona**, aunque el "
                    "valor no cambie.",
                    "**3 pts — Bloque 4, los indices:** 1,5 cada uno, con nombre claro y sobre "
                    "columnas que **algun reporte de la pregunta 2 filtra de verdad**. Un indice "
                    "sobre una columna que nadie consulta cuesta escritura y no da nada, y eso "
                    "resta. Se reconoce como sobresaliente el orden igualdad-antes-de-rango en "
                    "`(id_veterinario, fecha_hora)`, un indice **parcial** con su justificacion, y "
                    "senalar que PostgreSQL **no** indexa las llaves foraneas automaticamente.",
                    "**4 pts — Bloque 5, las tres pruebas,** algo mas de 1,3 cada una, y se "
                    "califica el **resultado**, no la intencion: la prueba 1 tiene que imprimir el "
                    "mensaje de mascota inactiva, la prueba 2 el de la restriccion de stock y la "
                    "prueba 3 tiene que mostrar que `audit_cita` **crecio**. Aqui esta el "
                    "discriminador de la pregunta: **las dos primeras son negativas y la tercera es "
                    "positiva**, y por tanto no se escriben igual. Un `EXCEPTION WHEN OTHERS` "
                    "alrededor de un `UPDATE` que funciona no prueba nada —imprimiria «OK» tambien "
                    "con el trigger borrado—, y eso cuesta el punto completo de la prueba 3. Se "
                    "reconoce como sobresaliente usar `WHEN check_violation` en la prueba 2 y "
                    "explicar por que ahi la condicion precisa es mejor que `OTHERS`.",
                    "**2 pts — Bloque 6, el inventario,** en **una sola** consulta con `UNION ALL` "
                    "y las 9 tablas. Se descuenta si no lleva `ORDER BY`: `UNION ALL` no garantiza "
                    "orden y la salida deja de ser estable para el informe. Detalle que vale la pena "
                    "revisar: si `audit_cita` sale en **0**, el trigger no se disparo y la prueba 3 "
                    "no probo nada, aunque haya impreso «OK».",
                    "**Cero sintaxis Oracle, y es eliminatorio por bloque:** un `NUMBER`, un "
                    "`VARCHAR2`, un `RAISE_APPLICATION_ERROR`, un `DUAL`, un `SQL%ROWCOUNT` o un "
                    "`/` de terminacion **no compila**, asi que el bloque donde aparezca no corre y "
                    "pierde sus puntos por la via de los hechos. Al devolver la nota conviene decir "
                    "el equivalente correcto —`NUMERIC`, `TEXT`, `RAISE EXCEPTION`, "
                    "`GET DIAGNOSTICS ... = ROW_COUNT`— porque es el punto 4 de la pregunta 5.",
                ],
                "errores": [
                    "**Un script que solo corre a la segunda,** o que exige comentar unas lineas "
                    "para pasar. Es el error mas caro porque arrastra a todos los bloques "
                    "siguientes. Causas habituales: `REFERENCES` a una tabla que se crea mas abajo, "
                    "`INSERT` de `mascota` antes de `dueno`, o `CREATE TRIGGER` antes de su funcion. "
                    "La comprobacion es barata: ejecutarlo una vez de cero, que en ExamLab se puede "
                    "porque la base se vuelve a sembrar en cada intento.",
                    "**Escribir el `factura.total` a mano.** Funciona, pasa la corrida y deja la "
                    "entrega con el mismo defecto que se documento en la Clase 11: el numero "
                    "guardado y el numero derivado dejan de coincidir sin que nadie lo note. El "
                    "`UPDATE` que lo calcula son cuatro lineas y ademas habilita la ultima fila de "
                    "la verificacion 6b.",
                    "**Solo dos facturas «porque el enunciado pide dos», y una sola consulta.** "
                    "Falla, y el mensaje no es obvio: `consulta.id_cita` es `UNIQUE` y "
                    "`factura.id_consulta` es `NOT NULL REFERENCES consulta`, asi que dos facturas "
                    "necesitan dos consultas, que necesitan dos citas atendidas distintas. Es la "
                    "cadena de dependencias que rompe mas semillas.",
                    "**Escribir la prueba 3 con el molde de las dos primeras:** un `UPDATE` "
                    "envuelto en `EXCEPTION WHEN OTHERS THEN RAISE NOTICE` y nada mas. No prueba "
                    "nada: el bloque no falla, imprime «OK» y seguiria imprimiendolo con el trigger "
                    "eliminado. Una prueba positiva necesita **comparar** el antes con el despues, "
                    "y esa comparacion es la prueba.",
                    "**`RAISE_APPLICATION_ERROR`, `NUMBER`, `VARCHAR2`, `DUAL`, `SQL%ROWCOUNT` o "
                    "un `/` al final de los bloques.** Es material heredado de PL/SQL y en "
                    "PostgreSQL no compila. Los reemplazos: `RAISE EXCEPTION 'texto %', var;`, "
                    "`NUMERIC` y `TEXT`, un `SELECT` sin `FROM`, y "
                    "`GET DIAGNOSTICS v_filas = ROW_COUNT;`.",
                    "**Un trigger «de una sola pieza»,** con la logica dentro del `CREATE TRIGGER`. "
                    "En PostgreSQL son siempre dos objetos: la funcion `RETURNS TRIGGER` y la "
                    "asociacion que la llama con `EXECUTE FUNCTION`. Es la diferencia con Oracle "
                    "que mas se repite y merece estar en la respuesta de la pregunta 5.",
                    "**Indices puestos para cumplir el requisito:** `CREATE INDEX ON dueno(nombre)` "
                    "cuando ningun reporte filtra por ahi, o un indice sobre una columna que ya "
                    "tiene PK. Cuestan escritura, no aportan lectura y delatan que el bloque 4 se "
                    "lleno sin mirar el bloque de consultas.",
                    "**Borrar la fila de ejemplo de `entrega_final`** para «dejar la tabla limpia». "
                    "Modificar la semilla no es entregar, y ademas hace que el script deje de ser "
                    "reproducible sobre la base tal como se recibe.",
                    "**Un inventario sin `ORDER BY`,** o repartido en nueve consultas sueltas. El "
                    "enunciado pide **una** consulta, y sin `ORDER BY` el orden de un `UNION ALL` no "
                    "esta garantizado, asi que la captura del informe puede no coincidir con la del "
                    "docente al reejecutar.",
                ],
            },
            {
                "n": 2,
                "titulo": "Los KPIs que se proyectan en la sustentacion",
                "tipo": "bd_sql",
                "puntos": 20,
                "sql": """-- ======================================================================
-- ANTES DE EMPEZAR: LA SEMILLA NO EJERCE LAS CONDICIONES DE BORDE
--
-- La rubrica exige que K1 conserve los veterinarios SIN citas y que K3
-- incluya los insumos NUNCA vendidos. Pero en los datos entregados los 4
-- veterinarios tienen citas y los 6 insumos se han vendido, y K2 tiene sus
-- 3 facturas en un mismo mes. Es decir: la consulta correcta y la
-- incorrecta devuelven exactamente lo mismo, y nadie se enteraria.
--
-- Un KPI que no se ha probado contra su caso de borde es una suposicion.
-- Asi que primero se CREA el caso de borde -- tres INSERT -- y despues se
-- corre cada consulta. Esto es lo mismo que se hizo con el respaldo en la
-- Clase 13: la prueba que falta es la que decide si el control existe.
-- ======================================================================

-- Un veterinario recien contratado, sin citas todavia -> pone a prueba el
-- LEFT JOIN de K1 y la division por cero.
INSERT INTO veterinario (nombre, especialidad) VALUES ('Sara Quintero', 'Odontologia');

-- Un insumo que aun no se ha vendido -> pone a prueba el LEFT JOIN de K3.
INSERT INTO insumo (nombre, stock, precio_unit) VALUES ('Collar isabelino', 15, 18000);

-- La consulta 4 (cita 10, Desparasitacion, 35000) estaba sin facturar. Al
-- facturarla en octubre, K2 pasa a tener dos meses y su ORDER BY empieza a
-- significar algo. Ojo: si haces este INSERT antes de la primera corrida de
-- K2, tus numeros de septiembre no cambian pero aparece una fila mas.
INSERT INTO factura (id_consulta, fecha, total)
VALUES (4, TIMESTAMP '2026-10-02 10:15:00', 35000);

-- ======================================================================
-- K1 - CARGA POR VETERINARIO
--
-- Tres decisiones deliberadas:
--   LEFT JOIN  -> conserva al veterinario sin citas (si fuera JOIN, Sara
--                 desapareceria y el reporte diria que la clinica tiene 4
--                 veterinarios cuando tiene 5).
--   NULLIF     -> evita la division por cero justo en esa fila; sin el, la
--                 consulta no devuelve un numero raro: revienta entera.
--   ORDER BY con desempate -> tres veterinarios tienen 2 citas, y sin el
--                 segundo criterio el orden entre ellos no esta garantizado
--                 y la diapositiva puede salir distinta en la sustentacion.
-- ======================================================================
SELECT v.nombre                                          AS veterinario,
       COUNT(c.id_cita)                                  AS total_citas,
       COUNT(*) FILTER (WHERE c.estado = 'ATENDIDA')     AS atendidas,
       COUNT(*) FILTER (WHERE c.estado = 'CANCELADA')    AS canceladas,
       ROUND(COALESCE(COUNT(*) FILTER (WHERE c.estado = 'CANCELADA') * 100.0
                      / NULLIF(COUNT(c.id_cita), 0), 0), 1) AS pct_cancelacion
  FROM veterinario v
  LEFT JOIN cita c ON c.id_veterinario = v.id_veterinario
 GROUP BY v.id_veterinario, v.nombre
 ORDER BY total_citas DESC, v.nombre;

-- FILTER es la forma moderna y legible. El equivalente portable, por si el
-- motor de destino es viejo, es COUNT(CASE WHEN c.estado='ATENDIDA' THEN 1 END).
-- Lo que NO sirve es COUNT(*) sin filtro con LEFT JOIN: contaria 1 para el
-- veterinario sin citas, porque la fila extendida con nulos existe.

-- ======================================================================
-- K2 - INGRESOS POR MES
--
-- date_trunc('month', fecha) lleva toda fecha del mes al dia 1 a las 00:00,
-- y agrupar por esa expresion es lo que produce un mes calendario de
-- verdad. Se agrupa por la expresion, no por el alias.
-- ======================================================================
SELECT date_trunc('month', f.fecha) AS mes,
       COUNT(*)                     AS facturas,
       SUM(f.total)                 AS total_facturado
  FROM factura f
 GROUP BY date_trunc('month', f.fecha)
 ORDER BY mes;

-- ADVERTENCIA HONESTA PARA LA SUSTENTACION: este KPI suma factura.total,
-- que es lo que pide el enunciado. En los datos entregados ese total NO
-- coincide con consulta.precio + suma del detalle en ninguna de las tres
-- facturas originales -- es la misma inconsistencia que la prueba 5 de la
-- Clase 11 --. La consulta esta bien; el dato guardado es el que discrepa.
-- Si el jurado pregunta cual es la cifra buena, la respuesta es que hay que
-- elegir UNA definicion y hacerla cumplir con una restriccion o un trigger.
SELECT f.id_factura, f.total AS total_guardado,
       (SELECT c.precio FROM consulta c WHERE c.id_consulta = f.id_consulta)
       + COALESCE((SELECT SUM(d.cantidad * d.precio_unit) FROM detalle_factura d
                    WHERE d.id_factura = f.id_factura), 0) AS total_derivado
  FROM factura f ORDER BY f.id_factura;

-- ======================================================================
-- K3 - TOP INSUMOS CONSUMIDOS
--
-- El LEFT JOIN trae los insumos nunca vendidos y el COALESCE convierte su
-- SUM nulo en 0. El cast a NUMERIC(12,2) es para que la columna de valor
-- salga con dos decimales tambien en la fila del insumo sin ventas.
-- ======================================================================
SELECT i.nombre                                           AS insumo,
       COALESCE(SUM(d.cantidad), 0)                       AS unidades_vendidas,
       COALESCE(SUM(d.cantidad * d.precio_unit), 0)::NUMERIC(12,2) AS valor_generado,
       i.stock                                            AS stock_restante
  FROM insumo i
  LEFT JOIN detalle_factura d ON d.id_insumo = i.id_insumo
 GROUP BY i.id_insumo, i.nombre, i.stock
 ORDER BY unidades_vendidas DESC, valor_generado DESC;

-- ======================================================================
-- K4 - FICHA DE UN DUENO (historia clinica resumida)
--
-- Los dos primeros JOIN son internos a proposito: una cita sin mascota o
-- sin veterinario no puede existir, hay FK que lo garantizan. Los dos
-- ultimos son LEFT porque una cita PROGRAMADA todavia no tiene consulta, y
-- una consulta puede no estar facturada: si fueran JOIN, la ficha mostraria
-- solo lo ya cobrado, que es justo lo contrario de una historia clinica.
-- ======================================================================
SELECT m.nombre       AS mascota,
       c.fecha_hora,
       c.estado,
       v.nombre       AS veterinario,
       co.diagnostico,
       f.total        AS total_facturado
  FROM dueno du
  JOIN mascota m        ON m.id_dueno       = du.id_dueno
  JOIN cita c           ON c.id_mascota     = m.id_mascota
  JOIN veterinario v    ON v.id_veterinario = c.id_veterinario
  LEFT JOIN consulta co ON co.id_cita       = c.id_cita
  LEFT JOIN factura f   ON f.id_consulta    = co.id_consulta
 WHERE du.nombre = 'Ana Gomez'
 ORDER BY c.fecha_hora;

-- Filtrar por nombre es lo que pide el enunciado y conviene decir en voz
-- alta que en produccion se filtraria por du.id_dueno: dos duenos pueden
-- llamarse igual, y el nombre no es identificador. Ojo tambien con el
-- ultimo LEFT JOIN: factura.id_consulta no es UNIQUE, asi que si una
-- consulta llegara a tener dos facturas, esta ficha duplicaria la cita. Es
-- exactamente lo que produce api_facturar de la Clase 12 cuando una visita
-- lleva tres insumos.

-- ======================================================================
-- LO QUE HABILITA CADA NUMERO (esto es lo que pide el cierre del enunciado)
--
-- -- K1: Paula Salazar sale con 50,0 % de cancelacion, el peor indicador de
-- --     los cinco. DECISION: ninguna todavia, y decirlo es parte del
-- --     analisis -- son 1 de 2 citas, y una tasa sobre dos casos no es una
-- --     tasa. Lo que habilita es una medicion con mas volumen antes de
-- --     tocar la agenda. Laura Restrepo concentra 4 de las 10 citas: ahi si
-- --     hay una decision inmediata de reparto de carga.
-- -- K2: septiembre cierra en 178.200 con 3 facturas -> ticket promedio
-- --     59.400. DECISION: es la linea base contra la que se compara
-- --     octubre; con la factura de octubre (35.000) la caida es visible al
-- --     instante y dispara la revision de citas atendidas sin facturar.
-- -- K3: la gasa esteril es la mas vendida en unidades (4) y solo genera
-- --     4.800; la vacuna triple felina vende 1 unidad, genera 31.000 y
-- --     queda con stock 3. DECISION: la reposicion se prioriza por la
-- --     triple felina, no por la gasa. Unidades y valor ordenan distinto, y
-- --     ordenar por la columna equivocada invierte la decision.
-- -- K4: Ana Gomez tiene 4 citas y 2 sin consulta, una de ellas PROGRAMADA
-- --     para el 2026-09-08. DECISION: es la lista de llamadas de
-- --     confirmacion de la semana, y ademas explica por que la ficha usa
-- --     LEFT JOIN: las citas sin consulta son precisamente las accionables.
-- ======================================================================""",
                "salida": """K1 - Carga por veterinario (5 filas, con Sara Quintero ya insertada)

   veterinario   | total_citas | atendidas | canceladas | pct_cancelacion
-----------------+-------------+-----------+------------+-----------------
 Laura Restrepo  |           4 |         3 |          0 |             0.0
 Diego Moreno    |           2 |         1 |          0 |             0.0
 Ivan Ortiz      |           2 |         0 |          0 |             0.0
 Paula Salazar   |           2 |         0 |          1 |            50.0
 Sara Quintero   |           0 |         0 |          0 |             0.0

La fila que importa es la ultima, y es la que la semilla original no permitia
ver: 0 citas, 0 atendidas, 0 canceladas y 0.0 de porcentaje **sin que la
consulta reviente**. Sin el NULLIF esa fila no sale mal: la consulta entera
falla con "division by zero" y no hay diapositiva. Y sin el LEFT JOIN, Sara
simplemente no aparece y el reporte afirma que la clinica tiene 4 veterinarios.

Tres veterinarios empatan en 2 citas, asi que el desempate por nombre no es un
adorno: sin el, el orden entre Diego, Ivan y Paula no esta garantizado y la
captura del informe puede no coincidir con lo que se proyecte en vivo.

K2 - Ingresos por mes

Primera corrida, con las 3 facturas originales (1 fila):

         mes         | facturas | total_facturado
---------------------+----------+-----------------
 2026-09-01 00:00:00 |        3 |       178200.00

Con la factura de octubre (2 filas):

         mes         | facturas | total_facturado
---------------------+----------+-----------------
 2026-09-01 00:00:00 |        3 |       178200.00
 2026-10-01 00:00:00 |        1 |        35000.00

178.200 = 71.000 + 47.000 + 60.200. Con una sola fila, el "ordena
cronologicamente" de la rubrica no se puede comprobar; con dos, si.

Contraste total guardado / total derivado (4 filas):

 id_factura | total_guardado | total_derivado
------------+----------------+----------------
          1 |       71000.00 |       81400.00
          2 |       47000.00 |       54500.00
          3 |       60200.00 |       83600.00
          4 |       35000.00 |       35000.00

Las tres facturas de la semilla estan descuadradas -- y no por poco -- bajo la
definicion "precio de la consulta mas la suma del detalle". La unica que cuadra
es la 4, la que se acaba de crear calculando el numero. No es un error del
estudiante ni de la consulta: es el dato guardado, y es la misma inconsistencia
de la prueba 5 de la Clase 11. Llevar esta tabla a la sustentacion es mejor que
esperar a que el jurado la encuentre.

K3 - Top insumos consumidos (7 filas, con Collar isabelino ya insertado)

         insumo          | unidades_vendidas | valor_generado | stock_restante
-------------------------+-------------------+----------------+----------------
 Gasa esteril            |                 4 |        4800.00 |              8
 Jeringa 5ml             |                 3 |        2700.00 |             60
 Antiparasitario oral    |                 2 |       19000.00 |             40
 Vacuna triple felina    |                 1 |       31000.00 |              3
 Vacuna antirrabica      |                 1 |       22000.00 |             12
 Suero fisiologico 500ml |                 1 |        7000.00 |             25
 Collar isabelino        |                 0 |           0.00 |             15

Dos cosas para la sustentacion. La ultima fila es la que prueba el LEFT JOIN con
COALESCE: 0 unidades, 0.00 de valor, y **aparece**. Con un JOIN interno se
perderia justo el insumo del que interesa saber que no rota.

Y el orden: la gasa esteril encabeza por unidades con 4.800 de valor, mientras
la vacuna triple felina vende una sola unidad, genera 31.000 y se queda con
stock 3. Ordenar por unidades y ordenar por valor dan rankings casi invertidos,
y la decision de reposicion cambia por completo segun la columna elegida. Eso es
lo que hay que decir al proyectar la lamina.

K4 - Ficha de Ana Gomez (4 filas)

  mascota | fecha_hora          |   estado    |  veterinario   |       diagnostico        | total_facturado
----------+---------------------+-------------+----------------+--------------------------+-----------------
 Firulais | 2026-09-01 08:00:00 | PROGRAMADA  | Laura Restrepo |                          |
 Luna     | 2026-09-01 09:00:00 | ATENDIDA    | Laura Restrepo | Vacunacion triple felina |        71000.00
 Firulais | 2026-09-05 15:00:00 | ATENDIDA    | Laura Restrepo | Otitis externa           |        60200.00
 Luna     | 2026-09-08 16:00:00 | PROGRAMADA  | Paula Salazar  |                          |

Cuatro filas: las dos mascotas de Ana Gomez (Firulais y Luna) con dos citas cada
una. Dos traen diagnostico y total; dos vienen con las dos ultimas columnas
vacias, porque son citas PROGRAMADA que todavia no generaron consulta.

Esas dos filas vacias son la razon de ser del LEFT JOIN, y conviene decirlo asi
en la sustentacion: con JOIN interno la ficha mostraria 2 filas en vez de 4 y
seria un historial de cobros, no una historia clinica. Ademas la cita del
2026-09-08 sigue PROGRAMADA: es exactamente la fila accionable del reporte.""",
                "como_calificar": [
                    "**6 pts — K1.** 2 pts que corra y devuelva las cuatro columnas pedidas mas el "
                    "porcentaje redondeado a un decimal; **2 pts el `LEFT JOIN` que conserva al "
                    "veterinario sin citas**; 2 pts el `NULLIF` o el `CASE` que evita la division "
                    "por cero. Y aqui viene el detalle que hay que tener presente al calificar: "
                    "**con la semilla tal como llega, los cuatro veterinarios tienen citas**, asi "
                    "que la consulta correcta y la incorrecta devuelven lo mismo. Se otorgan los 4 "
                    "pts de borde solo si el estudiante **crea** el caso —un `INSERT` de un "
                    "veterinario nuevo— y muestra la fila con ceros, o si al menos deja escrito en "
                    "un comentario que la semilla no lo ejerce.",
                    "**4 pts — K2.** 2 pts el `date_trunc('month', f.fecha)` en el `SELECT` y en el "
                    "`GROUP BY` con el conteo y la suma correctos; 2 pts el orden cronologico "
                    "**demostrado**, que con las tres facturas originales cae todo en un solo mes y "
                    "no se puede comprobar: se otorgan si el estudiante agrega una factura en otro "
                    "mes o lo advierte por escrito. El total de septiembre es **178.200,00**. Se "
                    "reconoce como sobresaliente notar que `factura.total` **no** coincide con "
                    "`consulta.precio` mas el detalle en ninguna de las tres, que es la misma "
                    "inconsistencia de la Clase 11: la consulta esta bien, el dato guardado es el "
                    "que discrepa.",
                    "**4 pts — K3.** 2 pts las cuatro columnas con el `SUM(cantidad * precio_unit)` "
                    "y el orden por unidades descendente; **2 pts el `LEFT JOIN` con `COALESCE` que "
                    "incluye el insumo nunca vendido**, que —igual que en K1— la semilla no ejerce, "
                    "porque los seis insumos aparecen en `detalle_factura`. Se reconoce como "
                    "sobresaliente el analisis del orden: la gasa esteril lidera en unidades con "
                    "4.800 de valor mientras la vacuna triple felina vende 1 unidad, genera 31.000 "
                    "y queda con stock 3, de modo que **unidades y valor dan rankings invertidos** y "
                    "la decision de reposicion cambia segun la columna elegida.",
                    "**4 pts — K4.** 2 pts las seis columnas con los `JOIN` correctos y el filtro "
                    "por `Ana Gomez`; 2 pts los `LEFT JOIN` a `consulta` y a `factura` de modo que "
                    "salgan **4 filas**, dos de ellas con diagnostico y total vacios. Este es el "
                    "unico KPI cuyo caso de borde **si** esta en la semilla, asi que aqui el "
                    "`LEFT JOIN` se verifica directamente: si devuelve 2 filas, son `JOIN` "
                    "internos. Se reconoce como sobresaliente decir que en produccion se filtraria "
                    "por `id_dueno` y no por nombre, y que el ultimo `LEFT JOIN` puede duplicar "
                    "filas porque `factura.id_consulta` no es `UNIQUE`.",
                    "**2 pts — los comentarios de cierre,** medio punto por KPI, y se exigen las "
                    "**dos** mitades que pide el enunciado: el numero concreto obtenido y la "
                    "decision que habilita. «K1 muestra la carga de trabajo» no vale; «Laura "
                    "Restrepo concentra 4 de las 10 citas, hay que repartir» si. Se reconoce como "
                    "sobresaliente la honestidad estadistica en K1: el 50 % de Paula Salazar son 1 "
                    "de 2 citas, y una tasa sobre dos casos no habilita ninguna decision todavia.",
                    "**Criterio general de esta pregunta:** se califica el resultado contra los "
                    "datos entregados, no la elegancia. Cualquier consulta que devuelva las filas y "
                    "los numeros correctos vale completo, use `FILTER`, `CASE WHEN` o subconsultas. "
                    "Lo que no vale es una consulta cuya correccion no se pueda distinguir de su "
                    "incorreccion, y de ahi el peso de los cuatro puntos de borde.",
                ],
                "errores": [
                    "**`JOIN` interno donde el enunciado pide `LEFT JOIN`,** en K1, K3 o K4. En K4 "
                    "se detecta al instante —devuelve 2 filas en vez de 4—, pero en K1 y K3 **no se "
                    "nota con esta semilla**, y ahi esta el riesgo: el estudiante entrega una "
                    "consulta incorrecta que da el resultado correcto, la proyecta en la "
                    "sustentacion, y el dia que la clinica contrate un veterinario el reporte lo "
                    "borra del informe.",
                    "**Dividir sin proteger el cero.** `canceladas * 100.0 / total_citas` no "
                    "devuelve un valor raro para el veterinario sin citas: **la consulta entera "
                    "falla** con «division by zero» y no hay diapositiva. `NULLIF(total, 0)` la "
                    "deja en `NULL` y el `COALESCE` externo la muestra como 0.0.",
                    "**`COUNT(*)` en lugar de `COUNT(c.id_cita)` con `LEFT JOIN`.** La fila "
                    "extendida con nulos existe, asi que `COUNT(*)` devuelve **1** para el "
                    "veterinario sin citas: el reporte inventa una cita. Es el error clasico del "
                    "`LEFT JOIN` con agregados y conviene mostrarlo en pantalla.",
                    "**Agrupar K2 por `f.fecha` en vez de por `date_trunc('month', f.fecha)`.** "
                    "Devuelve una fila por factura, no por mes, y con tres facturas parece "
                    "plausible. La comprobacion es contar filas: si hay tantas filas como "
                    "facturas, no se agrupo por mes.",
                    "**Sumar en K3 `SUM(d.cantidad) * i.precio_unit` en vez de "
                    "`SUM(d.cantidad * d.precio_unit)`.** Usa el precio **actual** del insumo en "
                    "lugar del precio al que se vendio. Con esta semilla coinciden y no se nota; en "
                    "produccion, cualquier cambio de precio reescribe la historia de ventas. "
                    "`detalle_factura.precio_unit` existe exactamente para eso.",
                    "**Reportar solo el ranking por unidades y decidir con el.** Es el error de "
                    "interpretacion mas caro de esta pregunta: la gasa esteril encabeza la lista y "
                    "es el insumo que **menos** importa reponer. La decision de reposicion se toma "
                    "cruzando valor generado con stock restante.",
                    "**Comentarios de cierre genericos:** «este KPI sirve para tomar decisiones». "
                    "El enunciado pide el numero concreto obtenido y la decision concreta que "
                    "habilita. Sin el numero no hay evidencia; sin la decision, el KPI es un "
                    "adorno.",
                    "**Presentar el 50 % de cancelacion de Paula Salazar como un hallazgo.** Son 1 "
                    "de 2 citas. Un porcentaje sobre dos casos es ruido, y el jurado lo va a "
                    "senalar. Decirlo primero convierte un error en criterio.",
                ],
            },
            {
                "n": 3,
                "titulo": "Checklist de empaquetado del ZIP final",
                "tipo": "cerrada_multi",
                "puntos": 10,
                "justificacion": {
                    0: "**Correcta.** El criterio no es el orden alfabetico sino el **orden de "
                       "ejecucion**: `01_ddl.sql`, `02_datos.sql`, `03_logica.sql`, y asi. La "
                       "prueba de que sirve es la que se acaba de hacer en la pregunta 1: si "
                       "alguien que nunca vio el proyecto puede reconstruir la base ejecutando los "
                       "archivos en el orden en que estan numerados, el paquete funciona. Y hay "
                       "dependencias que el numero tiene que respetar: los privilegios sobre las "
                       "funciones van **despues** de crearlas, porque un `GRANT` sobre una funcion "
                       "que no existe falla (Clase 12).",
                    1: "**Correcta, y el motor es el dato que mas se olvida.** Un script "
                       "PL/pgSQL ejecutado contra Oracle no falla «un poco»: no compila. El README "
                       "tiene que decir PostgreSQL, la version si se conoce, el orden de ejecucion "
                       "y quien hizo que. Ese ultimo punto no es burocracia: es lo que permite "
                       "preguntarle a la persona correcta en la sustentacion, y en un equipo "
                       "autorizado es la unica base objetiva para calificar aportes desiguales.",
                    2: "**Falsa, y es la opcion mas tentadora,** porque la demo salio bien y las "
                       "capturas se ven convincentes. Una captura demuestra que **algo** funciono "
                       "una vez en una maquina; no permite reejecutar, ni revisar, ni corregir, ni "
                       "reutilizar. Un entregable de bases de datos que no se puede volver a "
                       "ejecutar no es verificable, y es precisamente el reflejo del error de la "
                       "Clase 13: confundir la evidencia de que algo ocurrio con la capacidad de "
                       "reproducirlo.",
                    3: "**Correcta, y la segunda mitad es la que tiene filo:** «si no coinciden, el "
                       "entregable es inconsistente». El ER en imagen sirve para explicar y el DDL "
                       "es lo que la base realmente ejecuta, asi que cuando discrepan hay dos "
                       "verdades y una es falsa. El caso tipico es un diagrama con una tabla o una "
                       "relacion que el DDL no tiene —o al reves, un `CHECK` que existe en la base "
                       "y no en el diagrama—, y el jurado lo encuentra en treinta segundos "
                       "comparando las dos laminas.",
                    4: "**Falsa, y es la unica opcion cuya respuesta incorrecta tiene consecuencias "
                       "fuera del curso.** Las credenciales no van en el README, ni en los scripts, "
                       "ni en el codigo de la aplicacion, ni en el repositorio: van en **variables "
                       "de entorno**, y el README explica **cuales** hay que definir sin decir sus "
                       "valores. Dos razones concretas: un ZIP se reenvia y se sube a sitios que no "
                       "se controlan, y una credencial en un archivo versionado queda en el "
                       "historial aunque se borre despues. Lo que el docente necesita para revisar "
                       "es el script que reconstruye la base, no una cuenta ajena.",
                    5: "**Correcta, y ademas es la lista de comprobacion del informe.** Las "
                       "secciones no se inventan al final: son los hitos del semestre —roles y "
                       "privilegios de la Clase 2 y la 12, respaldo de la 4 y la 13, optimizacion "
                       "antes/despues de la 6, indices y particionamiento de la 7, transacciones de "
                       "la 8, concurrencia de la 10 y lecciones de casos reales de la 13—. Si "
                       "alguna esta vacia, la señal no es «falta redactar»: es que ese hito no se "
                       "cerro, y es mejor declararlo que dejar que se note en las preguntas.",
                },
                "como_calificar": [
                    "**10 pts con las cuatro correctas —0, 1, 3 y 5— y ninguna incorrecta;** "
                    "puntaje proporcional por acierto parcial, como declara la rubrica de la "
                    "plataforma. Conviene revisarla en voz alta antes de los turnos de "
                    "sustentacion, porque las cuatro correctas son literalmente la lista de "
                    "verificacion del ZIP y varios paquetes se arreglan en cinco minutos con ella.",
                    "**La opcion 4 —credenciales en el README— se corrige aparte y sin ambiguedad,** "
                    "porque es la unica con consecuencias fuera del curso. Las credenciales van en "
                    "**variables de entorno** y el README dice cuales definir, no sus valores. Un "
                    "ZIP se reenvia, se sube y se copia; y una credencial en un archivo versionado "
                    "sigue en el historial aunque se borre en un commit posterior. Si algun "
                    "paquete entregado las trae, hay que avisarlo de inmediato y pedir que se "
                    "roten, no solo descontar el punto.",
                    "**La opcion 2 —capturas en lugar de codigo— es la que mas se marca,** porque "
                    "la demo salio bien y la captura se ve convincente. El argumento que hay que "
                    "devolver: una captura prueba que algo funciono una vez en una maquina, y no "
                    "permite reejecutar, revisar ni corregir. Es el reflejo exacto del error de la "
                    "Clase 13, con el respaldo que existia como archivo y no como capacidad.",
                    "**En la opcion 3 lo que se califica es la segunda mitad:** «si no coinciden, el "
                    "entregable es inconsistente». Vale la pena hacer la comparacion al revisar —ER "
                    "contra DDL— porque encontrar la discrepancia antes de la sustentacion es un "
                    "regalo, y despues es una pregunta incomoda.",
                    "**Errores de seleccion tipicos:** marcar solo 0 y 1 —quedarse con lo "
                    "«mecanico» del empaquetado y dejar fuera la coherencia ER/DDL y las secciones "
                    "del informe—, o marcar las seis, que con puntaje proporcional resta y delata "
                    "que no se leyeron las dos negativas.",
                ],
                "errores": [
                    "**Marcar la opcion 4.** Es el error que hay que atender primero, y no por los "
                    "puntos: si el paquete entregado incluye credenciales de verdad, hay que "
                    "avisarle al estudiante y pedirle que las cambie. La regla es la misma que se "
                    "aplico en la Clase 12: la conexion se arma desde variables de entorno y en el "
                    "codigo no hay ni usuario ni contrasena.",
                    "**Marcar la opcion 2 razonando «pero la demo funciono».** Que funcionara es la "
                    "condicion minima, no la evidencia. La evidencia es que otra persona pueda "
                    "reconstruirlo, y eso solo lo da el codigo con su orden de ejecucion.",
                    "**Descartar la opcion 3** porque «el ER es solo documentacion». Es la que se "
                    "usa para explicar el diseno en la sustentacion: si contradice el DDL, la "
                    "explicacion describe una base que no existe.",
                    "**Descartar la opcion 5** porque «el informe es aparte del ZIP». El informe es "
                    "parte del entregable y sus secciones son los hitos del semestre. Una seccion "
                    "vacia no significa que falte redactar: significa que ese hito quedo abierto, y "
                    "declararlo vale mas que disimularlo.",
                    "**Marcar las seis opciones.** Con puntaje proporcional, las dos incorrectas "
                    "restan; y ademas las opciones 1 y 3 del propio taller ya contradicen a la 2 y "
                    "a la 4, asi que marcarlas todas es responder sin leer.",
                ],
            },
            {
                "n": 4,
                "titulo": "Acta de entrega y reparto de la sustentacion",
                "tipo": "abierta",
                "puntos": 20,
                "tabla": {
                    "headers": ["Orden", "Archivo del ZIP", "Proposito", "Se ejecuta"],
                    "rows": [
                        ["—", "`00_README.md`",
                         "Motor y version (PostgreSQL), como ejecutar, orden de los scripts, que "
                         "variables de entorno definir —**sin valores**— y quien hizo que",
                         "No"],
                        ["1", "`01_ddl.sql`",
                         "Las 8 tablas mas `audit_cita`, con PK, FK y los `CHECK` nombrados",
                         "Si"],
                        ["2", "`02_datos_semilla.sql`",
                         "Datos de prueba coherentes con una veterinaria de Cali; los totales de "
                         "factura se **calculan** al final del script",
                         "Si"],
                        ["3", "`03_logica.sql`",
                         "`fn_precio_consulta`, `sp_agendar_cita` con su validacion y el trigger de "
                         "auditoria (funcion + asociacion)",
                         "Si"],
                        ["4", "`04_indices.sql`",
                         "`idx_cita_vet_fecha`, `idx_cita_mascota`, el parcial "
                         "`idx_cita_programada` y el unico parcial `uq_cita_vet_franja` de la "
                         "Clase 10",
                         "Si"],
                        ["5", "`05_optimizacion_antes_despues.sql`",
                         "El par de `EXPLAIN (ANALYZE, BUFFERS)` de la Clase 6: `Seq Scan` con "
                         "`Rows Removed by Filter` antes, `Index Cond` despues",
                         "Si"],
                        ["6", "`06_api.sql`",
                         "`api_agendar_cita`, `api_registrar_consulta` y `api_facturar`: el "
                         "contrato `(ok, mensaje, id_generado)` de la Clase 12",
                         "Si"],
                        ["7", "`07_privilegios_api.sql`",
                         "Rol `app_vetcare`, `REVOKE`/`GRANT` con firma exacta y el "
                         "`SECURITY DEFINER SET search_path` sin el cual la app no puede usar la "
                         "API. **Obligatoriamente despues del 06**",
                         "Si"],
                        ["8", "`08_seguridad_sql_dinamico.sql`",
                         "`buscar_mascota_segura` con `EXECUTE ... USING`, `DROP` de la version "
                         "vulnerable y la evidencia 8 → 0 (Clase 13)",
                         "Si"],
                        ["9", "`09_respaldo_y_restore.sql`",
                         "`respaldo_cita`, `bitacora_respaldo`, `trg_archivar_cita`, la consulta de "
                         "veredicto y el guion de `pg_dump`/`pg_restore` **aun sin ensayar**",
                         "Si"],
                        ["10", "`10_pruebas_aceptacion.sql`",
                         "Las 3 reglas de negocio del PI mas la bateria de 5 pruebas de la Clase "
                         "11, con la prueba 5 en `cumple = FALSE` documentada",
                         "Si"],
                        ["—", "`app/cliente.py`",
                         "Cliente Python de la Clase 12: solo llama a las funciones `api_*`, con "
                         "`%s` y sin un `INSERT` directo",
                         "No (no se evalua ejecucion)"],
                        ["—", "`er_vetcare.png` + `er_vetcare.mmd`",
                         "El ER en imagen y en Mermaid. Tiene que coincidir con `01_ddl.sql`: si no, "
                         "el entregable es inconsistente",
                         "No"],
                        ["—", "`informe_vetcare.pdf`",
                         "Roles y privilegios, respaldo, optimizacion antes/despues, indices, "
                         "transacciones, concurrencia y lecciones de casos reales",
                         "No"],
                        ["—", "`acta_entrega.pdf`",
                         "Este documento: identificacion, inventario, trazabilidad, guion, autoria "
                         "y estado final firmado",
                         "No"],
                    ],
                },
                "respuesta": (
                    "Modelo de referencia del acta. Las cifras y los nombres son de ejemplo; lo que "
                    "se califica es que las seis secciones existan y que el inventario, la "
                    "trazabilidad y el guion sean **verificables contra el ZIP entregado**.\n\n"
                    "### 1. Identificacion\n\n"
                    "- **Estudiante:** Nombre Completo Del Estudiante · **Codigo:** 1234567\n"
                    "- **Proyecto:** VetCare DB — Sistema de gestion para clinica veterinaria\n"
                    "- **Asignatura:** Bases de Datos II — **FI303215** · Grupo 641A-2\n"
                    "- **Periodo:** 2026-2 · **Fecha de entrega:** 2026-11-16\n"
                    "- **Integrantes:** trabajo individual. (Si el docente autorizo equipo, se "
                    "lista aqui cada integrante con su codigo, y las secciones 4, 5 y 6 se "
                    "desglosan por persona.)\n\n"
                    "### 2. Inventario del paquete\n\n"
                    "Es la tabla de arriba. Dos reglas que la gobiernan: los archivos numerados se "
                    "ejecutan **en ese orden** y ninguno necesita que se comente una linea para "
                    "correr; y `07_privilegios_api.sql` va obligatoriamente **despues** de "
                    "`06_api.sql`, porque un `GRANT` sobre una funcion que todavia no existe "
                    "falla.\n\n"
                    "### 3. Trazabilidad hito por hito\n\n"
                    "| Clase | Tema | Artefacto del paquete que lo contiene |\n"
                    "|---|---|---|\n"
                    "| 1 | Revision BD I · arranque VetCare | `01_ddl.sql` + `er_vetcare.mmd`: las "
                    "8 tablas y el modelo del que salio todo |\n"
                    "| 2 | Administracion de BD · roles | `07_privilegios_api.sql` (rol "
                    "`app_vetcare`, `REVOKE`/`GRANT`) + informe §roles y privilegios |\n"
                    "| 3 | Procedimientos almacenados | `03_logica.sql`: `sp_agendar_cita` con la "
                    "validacion de mascota inactiva |\n"
                    "| 4 | Funciones · triggers · respaldo | `03_logica.sql` "
                    "(`fn_precio_consulta`, `fn_trg_audit_cita` + `trg_audit_cita`) y "
                    "`09_respaldo_y_restore.sql` |\n"
                    "| 6 | Optimizacion de consultas | `05_optimizacion_antes_despues.sql`: el par "
                    "de `EXPLAIN` con `Seq Scan` → `Index Cond` |\n"
                    "| 7 | Indices y particionamiento | `04_indices.sql` (compuesto y parcial) + "
                    "informe §particionamiento, **diseñado y no probado con volumen real** |\n"
                    "| 8 | Tuning · transacciones | `10_pruebas_aceptacion.sql`: facturacion "
                    "atomica y `CHECK (stock >= 0)` demostrado |\n"
                    "| 10 | Control de concurrencia | `04_indices.sql` (`uq_cita_vet_franja` "
                    "parcial) + informe §concurrencia con el reintento ante 40001 |\n"
                    "| 11 | Avance PI | `10_pruebas_aceptacion.sql` (bateria de 5 pruebas) + tabla "
                    "`checklist_pi`, **con la prueba 5 en `FALSE` y explicada** |\n"
                    "| 12 | Integracion app ↔ BD | `06_api.sql`, `07_privilegios_api.sql` y "
                    "`app/cliente.py` |\n"
                    "| 13 | Analisis de casos reales | `08_seguridad_sql_dinamico.sql`, "
                    "`09_respaldo_y_restore.sql` e informe §lecciones aprendidas |\n\n"
                    "**Lo que quedo abierto, declarado aqui y no escondido:**\n\n"
                    "1. **El respaldo fisico no se ha ensayado.** El guion de `pg_dump` / "
                    "`pg_restore` esta escrito en `09_respaldo_y_restore.sql` y **nunca se ha "
                    "ejecutado de punta a punta**. Es el item 12 del checklist de la Clase 11 y "
                    "sigue en `NO`. Viene abierto desde la Clase 11 y es la consecuencia directa "
                    "del caso que analice en la Clase 13.\n"
                    "2. **El particionamiento se diseño y no se probo con volumen real.** El "
                    "criterio de partition pruning esta en el informe; con las 8 citas de la "
                    "semilla no se puede demostrar.\n"
                    "3. **Las facturas 1 a 3 del avance de la Clase 11 quedan descuadradas.** No es "
                    "un olvido: es el hallazgo de esa clase, y la correccion —calcular el total en "
                    "vez de escribirlo— ya esta aplicada en `02_datos_semilla.sql`.\n\n"
                    "### 4. Guion de la sustentacion — **7 minutos**\n\n"
                    "| Tramo | Bloque | Min |\n"
                    "|---|---|---|\n"
                    "| 1 | El problema de la clinica y el modelo en una lamina | 0,5 |\n"
                    "| 2 | ER y tres decisiones de diseno (`activa`, `audit_cita` sin FK, "
                    "`consulta.id_cita` UNIQUE) | 1 |\n"
                    "| 3 | **Demo 1:** `sp_agendar_cita` rechaza una mascota inactiva | 1 |\n"
                    "| 4 | **Demo 2:** stock — el `CHECK` bloquea el negativo y la transaccion "
                    "deja todo como estaba | 1 |\n"
                    "| 5 | Optimizacion: `EXPLAIN` antes y despues, y el indice que lo explica | "
                    "1 |\n"
                    "| 6 | Seguridad: la inyeccion cerrada (8 → 0) y el `SECURITY DEFINER` que "
                    "hace usable la API | 1 |\n"
                    "| 7 | KPIs: las cuatro laminas de la pregunta 2 | 1 |\n"
                    "| 8 | Lo que falta —el restore sin ensayar— y como lo verificaria | 0,5 |\n"
                    "| | **Total** | **7** |\n\n"
                    "Cabe en la ventana de 5 a 8 minutos con margen, y el tramo 8 es deliberado: "
                    "declarar el limite antes de que lo pregunten cambia el tono de la ronda de "
                    "preguntas. **Plan B en tres niveles:** si la base no responde, se proyecta la "
                    "salida guardada de `10_pruebas_aceptacion.sql`; si el proyector falla, se "
                    "cuenta con el ER impreso; y si hay que cortar a 5 minutos, se sacrifican los "
                    "tramos 5 y 7 —los unicos que no demuestran una regla de negocio—. Si el "
                    "docente autorizo equipo, cada tramo lleva un nombre y **todos los integrantes "
                    "hablan**; el reparto natural es modelo y demos para quien escribio la logica, "
                    "y optimizacion, seguridad y KPIs para quien escribio las consultas.\n\n"
                    "### 5. Declaracion de autoria y uso de herramientas\n\n"
                    "El modelo, el DDL, la logica, los indices, las consultas y las pruebas son "
                    "mios; los escribi y los ejecute. Use asistentes de IA en tres puntos "
                    "concretos, y en los tres verifique el resultado ejecutandolo: (1) para "
                    "recordar la sintaxis de `RETURNS TABLE` en PL/pgSQL, que verifique creando la "
                    "funcion y llamandola —y ahi encontre el error de ambiguedad por sombreado de "
                    "nombres—; (2) para redactar los comentarios del script maestro, que revise uno "
                    "por uno contra lo que hace el codigo; (3) para revisar la ortografia del "
                    "informe. **No** use codigo de terceros sin adaptarlo. Las consultas de la "
                    "pregunta 2 las escribi contra los datos reales y comprobe cada numero "
                    "ejecutandolas: el 178.200,00 de septiembre y las 4 filas de la ficha de Ana "
                    "Gomez salen de la corrida, no de una estimacion.\n\n"
                    "### 6. Estado final declarado\n\n"
                    "> **COMPLETO CON OBSERVACIONES.**\n\n"
                    "Los siete bloques del script maestro corren de cero sin errores y las tres "
                    "reglas de negocio quedan demostradas con su salida; las dos observaciones son "
                    "el respaldo fisico sin ensayar —item 12 del checklist, con fecha comprometida "
                    "el 2026-11-06— y el particionamiento sin volumen real. Declaro "
                    "`COMPLETO CON OBSERVACIONES` y no `COMPLETO` precisamente porque esas dos "
                    "cosas estan identificadas y fechadas: un `COMPLETO` con un item en `NO` seria "
                    "la misma afirmacion sin verificar que estudie en la Clase 13.\n\n"
                    "**Firma:** _________________ · Nombre Completo Del Estudiante · 1234567 · "
                    "2026-11-16"
                ),
                "como_calificar": [
                    "**2 pts — Identificacion completa:** nombre y codigo, nombre del proyecto, "
                    "asignatura con el codigo **FI303215**, periodo **2026-2** y fecha de entrega; "
                    "y los integrantes si el docente autorizo equipo. Es la seccion mas facil y la "
                    "que mas se entrega a medias —falta el codigo de la asignatura o la fecha—, asi "
                    "que conviene revisarla primero.",
                    "**5 pts — Inventario del paquete.** 3 pts que nombre **archivos concretos** "
                    "con su orden de ejecucion y 2 pts que cubra los minimos del enunciado: DDL, "
                    "datos semilla, logica, indices, el par antes/despues de optimizacion, las "
                    "pruebas de las tres reglas, el informe y el ER. «Scripts SQL» como una sola "
                    "linea vale 1 de 5. Se reconoce como sobresaliente registrar la dependencia de "
                    "orden que si importa: los privilegios sobre las funciones van **despues** de "
                    "crearlas, porque un `GRANT` sobre una funcion inexistente falla.",
                    "**6 pts — Trazabilidad de las once clases,** algo mas de 0,5 por fila. Se "
                    "exige que cada clase apunte a un **artefacto real del paquete**, no al tema: "
                    "«Clase 6 → optimizacion» vale 0; «Clase 6 → `05_optimizacion_antes_despues."
                    "sql`, el par de `EXPLAIN`» vale completo. **Y la mitad de la nota de esta "
                    "seccion esta en reconocer lo que quedo abierto:** un acta que declara las once "
                    "clases cerradas cuando el checklist de la Clase 11 tiene el respaldo en `NO` es "
                    "una contradiccion entre dos entregables del mismo estudiante, y es mejor "
                    "senalarla al calificar que dejarla para el jurado.",
                    "**4 pts — Guion de sustentacion.** 2 pts que los minutos sumen entre **5 y 8** "
                    "—se verifica sumando, y un guion de 12 minutos no cabe en la ventana— y 2 pts "
                    "que cubra todos los bloques: modelo, reglas de negocio, optimizacion, "
                    "seguridad y resultados. Si hubo equipo autorizado, **todos los integrantes "
                    "deben tener voz asignada**, y un tramo sin nombre cuesta 1 pt. Se reconoce "
                    "como sobresaliente reservar el tramo final a declarar el limite conocido, y "
                    "traer un plan B para cuando la base no responda.",
                    "**2 pts — Declaracion de autoria y uso de herramientas,** y se califica la "
                    "**especificidad**, no la confesion. «Use IA para algunas partes» vale 0,5; "
                    "«use IA para recordar la sintaxis de `RETURNS TABLE`, y lo verifique creando "
                    "la funcion y llamandola» vale completo, porque describe el uso **y** la "
                    "verificacion. Una declaracion que diga que no se uso ninguna herramienta es "
                    "perfectamente valida.",
                    "**1 pt — Estado final justificado y firmado,** con una de las tres etiquetas "
                    "del enunciado. Se reconoce como sobresaliente el `COMPLETO CON OBSERVACIONES` "
                    "**con las observaciones nombradas y fechadas**: es mas creible que un "
                    "`COMPLETO` que contradice el checklist, y es la misma leccion de la Clase 13 "
                    "aplicada al propio acta.",
                    "**Criterio transversal:** el acta se califica **contra el ZIP**, no por si "
                    "sola. Un inventario que nombra `05_optimizacion_antes_despues.sql` cuando ese "
                    "archivo no esta en el paquete es peor que no mencionarlo: convierte el acta en "
                    "una declaracion falsa. Vale la pena abrir el ZIP con el acta al lado y marcar "
                    "las filas que no existen.",
                ],
                "errores": [
                    "**Un inventario en prosa:** «entrego los scripts, el informe y el diagrama». "
                    "No sirve para verificar nada. La rubrica pide archivos concretos con su orden "
                    "de ejecucion, y ese orden es lo que permite que otra persona reconstruya la "
                    "base sin preguntar.",
                    "**Trazabilidad que repite el temario.** Una tabla con «Clase 8 → "
                    "transacciones» copia el programa del curso; lo que se pide es «Clase 8 → "
                    "`10_pruebas_aceptacion.sql`, la facturacion atomica». Si una clase no tiene "
                    "artefacto, se dice, y eso vale mas que inventar una correspondencia.",
                    "**Declarar las once clases cerradas cuando no lo estan.** Es el error de "
                    "fondo de la seccion 3 y suele venir de querer que el acta «quede bien». El "
                    "jurado tiene el checklist de la Clase 11 con el respaldo en `NO`, asi que la "
                    "contradiccion se ve; y declarar el pendiente convierte una debilidad en "
                    "criterio.",
                    "**Un guion que no suma,** o que suma 12 minutos. La ventana es de 5 a 8 y se "
                    "verifica sumando la columna. Un guion de 12 minutos no es ambicioso: garantiza "
                    "que el corte llegue justo antes de los resultados.",
                    "**En equipo autorizado, un guion con un solo expositor.** El enunciado exige "
                    "que **todos** hablen. El reparto natural es que cada uno presente lo que "
                    "escribio, y eso ademas hace verificable la declaracion de autoria.",
                    "**Declaracion de autoria generica:** «todo el trabajo es mio» sin detalle, o "
                    "«use IA» sin decir donde ni como se verifico. Las dos formas incumplen la "
                    "misma exigencia: la seccion pide especificidad, en las dos direcciones.",
                    "**Estado `COMPLETO` con observaciones evidentes en el propio paquete.** Es la "
                    "afirmacion sin verificar de la Clase 13, aplicada al acta. "
                    "`COMPLETO CON OBSERVACIONES`, con las dos observaciones nombradas y fechadas, "
                    "es una declaracion mas fuerte, no mas debil.",
                    "**Nombrar en el inventario archivos que no estan en el ZIP.** Convierte el "
                    "acta en una declaracion falsa y es facil de detectar: se abre el paquete con "
                    "el acta al lado. Si un archivo no llego a existir, se retira del inventario y "
                    "se declara en el punto 3.",
                ],
            },
            {
                "n": 5,
                "titulo": "Autoevaluacion de cierre: que harias distinto",
                "tipo": "abierta",
                "puntos": 15,
                "respuesta": (
                    "Modelo de referencia: lo que se califica es la **especificidad y la "
                    "evidencia**, no coincidir con estas respuestas. Una autoevaluacion honesta que "
                    "difiera en todo puede valer 15 de 15.\n\n"
                    "### 1. La decision de diseno de la que estoy mas orgulloso\n\n"
                    "Poner las reglas de negocio **en la base y no en la aplicacion**. Concretamente "
                    "`CHECK (stock >= 0)` en `insumo` y la validacion de mascota inactiva dentro de "
                    "`sp_agendar_cita`. La tome despues de la Clase 8, cuando entendi que una regla "
                    "que vive solo en la aplicacion la cumple quien pasa por la aplicacion, y "
                    "cualquier otro camino —una consulta manual, un script de carga, otro "
                    "programa— la ignora. **Evidencia:** la prueba 2 del script maestro intenta "
                    "`UPDATE insumo SET stock = stock - 100` sobre un stock de 3 y el motor la "
                    "rechaza con «violates check constraint “ck_insumo_stock”»; despues del bloque, "
                    "el stock sigue en 3 porque la subtransaccion se deshizo completa. No es una "
                    "opinion sobre mi diseno: es una linea de salida que puedo proyectar.\n\n"
                    "### 2. La decision que cambiaria\n\n"
                    "**Calcularia `factura.total` desde el principio en vez de guardarlo escrito a "
                    "mano.** En la Clase 1 lo puse como una columna que se llenaba al insertar, y en "
                    "la Clase 11 descubri que las tres facturas del avance estaban descuadradas: el "
                    "total guardado no coincidia con `consulta.precio` mas la suma del detalle, y "
                    "nadie se habia enterado en dos meses. Si empezara de nuevo haria una de dos "
                    "cosas, y las dos son mas trabajo por adelantado y menos despues: o no guardar "
                    "el total y derivarlo en una vista, o guardarlo y sostenerlo con un trigger que "
                    "lo recalcule en cada cambio del detalle. Lo que **no** volveria a hacer es "
                    "tener el mismo dato en dos sitios sin nada que los mantenga iguales. La "
                    "correccion ya esta en `02_datos_semilla.sql`, donde el total sale de un "
                    "`UPDATE` que lo calcula.\n\n"
                    "**Segunda, mas pequena y del mismo tipo:** nombraria las restricciones desde el "
                    "primer dia. Un `CHECK` sin nombre produce un mensaje de error que depende de "
                    "como el servidor lo genere, y por eso al principio la aplicacion mostraba el "
                    "texto crudo del motor al usuario.\n\n"
                    "### 3. El concepto que mas me costo\n\n"
                    "**La concurrencia, y en particular por que un `SELECT COUNT(*)` no puede "
                    "bloquear nada.** Venia de la Clase 8 con la idea de que una transaccion "
                    "«protege» lo que lee, asi que no entendia como dos sesiones podian agendar la "
                    "misma franja si las dos verificaban antes. Lo desatasque el dia que entendi "
                    "que un bloqueo se pone sobre **filas que existen**, y la fila conflictiva "
                    "todavia no existia cuando cada sesion hizo su conteo: no hay nada que "
                    "bloquear. De ahi salio que la unica solucion real es un punto de "
                    "serializacion **fisico** —el indice unico parcial `uq_cita_vet_franja`— y no "
                    "una verificacion mas cuidadosa. Lo que **todavia** no tengo claro, y lo digo "
                    "en vez de fingir: cuando conviene subir a `SERIALIZABLE` y pagar los "
                    "reintentos del 40001, frente a resolverlo con una restriccion. Entiendo los "
                    "dos mecanismos y no tengo criterio propio para elegir con volumen real.\n\n"
                    "### 4. De Oracle a PostgreSQL: tres diferencias que tuve que aprender\n\n"
                    "1. **`RAISE EXCEPTION 'texto %', var;` en lugar de "
                    "`RAISE_APPLICATION_ERROR(-20001, 'texto')`.** No es solo otro nombre: en "
                    "PostgreSQL no hay que administrar un rango de numeros de error propios, la "
                    "interpolacion va con `%` y el codigo por omision es `P0001`. Importa porque "
                    "todo el material de partida estaba escrito con la forma de Oracle y **no "
                    "compila**: no da un aviso, no arranca.\n"
                    "2. **Un trigger son dos objetos: la funcion `RETURNS TRIGGER` y el "
                    "`CREATE TRIGGER` que la asocia.** En Oracle el cuerpo va dentro del trigger y "
                    "se usan `:NEW` y `:OLD`; aqui son `NEW` y `OLD` sin dos puntos, y la funcion "
                    "se puede reutilizar en varias tablas. Importa porque el error tipico es "
                    "escribir la logica dentro del `CREATE TRIGGER` y no entender por que no "
                    "compila.\n"
                    "3. **`GET DIAGNOSTICS v_filas = ROW_COUNT;` en lugar de `SQL%ROWCOUNT`,** y "
                    "junto con eso que `IF NOT FOUND` sirve despues de un `SELECT columna INTO` "
                    "pero **nunca** despues de un `SELECT COUNT(*) INTO`, porque `COUNT` siempre "
                    "devuelve una fila aunque valga 0. Importa porque es un error que **no falla**: "
                    "el `IF` simplemente nunca se cumple y la validacion se cae en silencio, que es "
                    "la peor clase de defecto.\n\n"
                    "Y una cuarta que no era de sintaxis sino de habito: no hay `DUAL`. "
                    "`SELECT 1 + 1;` funciona sin `FROM`.\n\n"
                    "### 5. Lo que se queda sin verificar\n\n"
                    "- **La concurrencia real.** El entorno de practica es de **una sola sesion**, "
                    "asi que nunca vi dos transacciones peleando por la misma franja: lo demostre "
                    "con el indice unico, que es el control correcto, pero no con dos sesiones "
                    "simultaneas. **Como lo verificaria:** dos clientes `psql` abiertos, "
                    "`BEGIN` en los dos, el `INSERT` de la misma franja en ambos y observar que uno "
                    "espera y despues recibe `23505`; y para el escenario de `SERIALIZABLE`, "
                    "comprobar que el `40001` aparece **en el `COMMIT`** y que el reintento la "
                    "resuelve.\n"
                    "- **Los privilegios con usuarios conectados de verdad.** Probé `app_vetcare` "
                    "con `SET ROLE`, que es lo que el entorno permite y demostro lo importante —que "
                    "sin `SECURITY DEFINER` la app no puede usar su propia API—, pero no con una "
                    "conexion autenticada real. **Como lo verificaria:** crear el rol con `LOGIN` y "
                    "contrasena, conectarme como el desde otro cliente e intentar el `INSERT` "
                    "directo, revisando ademas `pg_hba.conf`.\n"
                    "- **El particionamiento.** Diseñé la particion por rango de `fecha_hora` y con "
                    "ocho citas el planificador no tiene nada que podar. **Como lo verificaria:** "
                    "cargar del orden de un millon de citas con `generate_series` y comprobar en el "
                    "`EXPLAIN` que solo se leen las particiones del rango consultado.\n"
                    "- **El respaldo fisico, y es el que mas me pesa.** El guion de "
                    "`pg_dump`/`pg_restore` esta escrito y **no lo he ejecutado**. Lo que si tengo "
                    "es el respaldo logico con su trigger de archivo y su consulta de veredicto, y "
                    "se exactamente por que no es suficiente: vive en la **misma** base. **Como lo "
                    "verificaria:** `pg_dump` completo, `pg_restore` en una base vacia, correr "
                    "encima la bateria de cinco pruebas de la Clase 11 y exigir el mismo resultado "
                    "—incluido el `cumple = FALSE` de la prueba 5— y cronometrarlo para saber si el "
                    "RTO de 4 horas que declare es real o es un deseo.\n\n"
                    "### 6. Nota que me pondria\n\n"
                    "**4,2 de 5.** El diseno esta completo, corre de cero y las tres reglas de "
                    "negocio estan demostradas con salida verificable, no afirmadas. Lo que me "
                    "impide ponerme mas es lo de arriba: el item mas importante del plan de "
                    "respaldo sigue sin ensayar desde la Clase 11, y despues de estudiar un "
                    "incidente que ocurrio exactamente por eso, mantenerlo abierto es una decision "
                    "y no un descuido."
                ),
                "como_calificar": [
                    "**2,5 pts — punto 1, con evidencia concreta.** El orgullo no se califica; la "
                    "evidencia si. Valen una prueba que pasa con su mensaje, un tiempo o un plan que "
                    "cambio, o un error que la base rechazo. «Estoy orgulloso de mi modelo, quedo "
                    "bien normalizado» vale 0,5 de 2,5; «la prueba 2 intenta dejar el stock en -97 "
                    "y el motor la rechaza con “violates check constraint ck_insumo_stock”» vale "
                    "completo.",
                    "**2,5 pts — punto 2, un cambio de diseno preciso.** El enunciado enumera lo "
                    "que cuenta: un tipo de dato, una tabla que falta, una regla que quedo en la "
                    "aplicacion y debio estar en la base, un indice que no servia. «Lo haria mejor» "
                    "o «estudiaria mas» vale 0. Se reconoce como sobresaliente que el cambio salga "
                    "de un hallazgo del propio semestre —las facturas descuadradas de la Clase 11, "
                    "la funcion de solo lectura vulnerable de la Clase 13— porque demuestra que el "
                    "hallazgo se convirtio en criterio.",
                    "**2 pts — punto 3, el concepto dificil y **como** se desatasco.** El «como» es "
                    "la mitad de la nota: nombrar el concepto sin contar que lo desbloqueo vale 1. "
                    "**Y reconocer que algo sigue sin estar claro se premia, no se castiga:** vale "
                    "los 2 pts completos si esta formulado con precision —«no tengo criterio para "
                    "elegir entre `SERIALIZABLE` con reintentos y una restriccion unica»— porque "
                    "eso es una duda tecnica util, y no lo vale un «no entendi las "
                    "transacciones».",
                    "**3 pts — punto 4, las tres diferencias PL/SQL → PL/pgSQL,** 1 pt cada una, y "
                    "solo se otorga con el **por que importa**. Enumerar «`RAISE EXCEPTION` en vez "
                    "de `RAISE_APPLICATION_ERROR`» vale 0,5; añadir que el material de partida no "
                    "compila y hay que reescribirlo, vale 1. Diferencias que valen: el trigger como "
                    "**dos** objetos y `NEW`/`OLD` sin dos puntos; "
                    "`GET DIAGNOSTICS ... = ROW_COUNT` frente a `SQL%ROWCOUNT`; la ausencia de "
                    "`DUAL`; `NUMERIC`/`TEXT` frente a `NUMBER`/`VARCHAR2`; los delimitadores "
                    "`$$`; que no haya `/` de terminacion. Se reconoce como sobresaliente el "
                    "`IF NOT FOUND` que **no** funciona tras un `SELECT COUNT(*) INTO`, porque es "
                    "un defecto que no falla: la validacion se cae en silencio.",
                    "**3 pts — punto 5, los limites del entorno y como verificarlos en "
                    "produccion.** 1,5 pts identificar correctamente al menos dos —una sola sesion, "
                    "asi que no hay concurrencia real; roles probados con `SET ROLE` y no con "
                    "conexiones autenticadas; particionamiento sin volumen; respaldo fisico sin "
                    "ensayar— y **1,5 pts el metodo concreto**, que es lo que separa una queja de "
                    "un plan: dos clientes `psql` con `BEGIN` para ver el `23505`, un rol con "
                    "`LOGIN` desde otra conexion, `generate_series` para el volumen, "
                    "`pg_dump`/`pg_restore` con la bateria de la Clase 11 encima y cronometro. Un "
                    "«no pude probar la concurrencia» sin metodo vale 0,5.",
                    "**2 pts — punto 6, la autonota justificada,** 1 pt la nota y 1 pt que la "
                    "justificacion sea coherente con el resto del documento. Cualquier nota es "
                    "aceptable si se sostiene; lo que no se sostiene es un 5,0 despues de declarar "
                    "cuatro cosas sin verificar, ni un 3,0 despues de entregar un script que corre "
                    "completo. En equipo autorizado, la linea con la nota al aporte de cada "
                    "integrante es obligatoria.",
                    "**Criterio transversal, y es el que decide la nota:** esta pregunta se "
                    "califica por **especificidad**, no por longitud ni por autocritica. Media "
                    "pagina de humildad general vale menos que cuatro lineas que nombran un "
                    "`CHECK`, una consulta y un numero. La honestidad tampoco es un adorno: una "
                    "autoevaluacion que contradice el acta —«todo verificado» aqui y un item en "
                    "`NO` alla— pierde puntos en las dos preguntas.",
                ],
                "errores": [
                    "**Generalidades en el punto 1:** «me gusto como quedo el modelo», «aprendi "
                    "mucho». La pregunta pide evidencia, y evidencia es una prueba, un mensaje de "
                    "error, un tiempo o un plan de ejecucion. Sin numero ni salida, no hay punto.",
                    "**Un punto 2 que es un proposito y no un cambio de diseno:** «estudiaria mas», "
                    "«empezaria antes», «organizaria mejor mi tiempo». Puede ser cierto y no es lo "
                    "que se pregunta. Lo que se pide es una decision tecnica concreta que hoy se "
                    "tomaria distinta.",
                    "**Fingir que todo quedo claro en el punto 3.** Es el error mas costoso porque "
                    "el enunciado dice explicitamente lo contrario —«reconocerlo vale mas que "
                    "fingir»— y porque una duda bien formulada demuestra mas dominio que una "
                    "seguridad vaga. Lo que no vale es la version generica: «no entendi las "
                    "transacciones».",
                    "**Un punto 4 que solo enumera.** Tres pares de terminos sin el «por que "
                    "importa» valen la mitad. La consecuencia practica es la respuesta: el material "
                    "heredado **no compila**, y hay defectos —como el `IF NOT FOUND` tras un "
                    "`COUNT(*)`— que no fallan y por eso se cuelan.",
                    "**Confundir en el punto 5 lo que no se probo con lo que no se hizo.** «No "
                    "implemente particionamiento» es una tarea pendiente; «diseñe la particion y "
                    "con ocho filas el planificador no tiene nada que podar» es un limite del "
                    "entorno, que es lo que se pregunta. Y en los dos casos falta la mitad que mas "
                    "vale: **como** se verificaria.",
                    "**Ponerse 5,0 despues de declarar cuatro cosas sin verificar,** o castigarse "
                    "con un 3,0 tras entregar un script que corre completo y demuestra las tres "
                    "reglas. Las dos son incoherentes con el propio documento, y la coherencia es "
                    "justo lo que se califica.",
                    "**Escribir una autoevaluacion que contradice el acta de la pregunta 4:** «todo "
                    "quedo verificado» aqui y el item 12 del checklist en `NO` alla. Es la misma "
                    "afirmacion sin comprobar del caso de la Clase 13, cometida en el ultimo "
                    "documento del semestre.",
                ],
            },
        ],
        "preguntas_frecuentes": [
            ("¿Cuando tengo que entregar esto, si el 2026-11-16 es la sustentacion?",
             "**Antes** de tu turno. El bloque del 2026-11-16 se consume en las presentaciones, asi "
             "que no hay tiempo de aula para escribir el script maestro, y el 2026-11-09 es el "
             "Parcial 3. En la practica el taller se publica con el de la Clase 13 —el "
             "2026-11-02— y la ventana util es esa semana y la siguiente. Si llegas a tu turno sin "
             "haber entregado, sustentas sobre un paquete que nadie pudo revisar, y eso se nota en "
             "la ronda de preguntas."),
            ("Mi script falla a la mitad y no se donde. ¿Como lo depuro sin volverme loco?",
             "Lee el **primer** error, no el ultimo: en un script largo, un fallo temprano provoca "
             "una cascada de errores que no significan nada. Y las tres causas cubren casi todos "
             "los casos. Una: un `REFERENCES` a una tabla que se crea mas abajo —el DDL va en orden "
             "de dependencia, `dueno` antes de `mascota`, `cita` antes de `consulta`—. Dos: un "
             "`INSERT` que viola una FK por el mismo motivo. Tres: un `CREATE TRIGGER` antes de su "
             "funcion. Ejecutalo bloque por bloque hasta encontrar el que revienta, y despues "
             "**vuelve a correrlo completo de cero**: la base de ExamLab se vuelve a sembrar en "
             "cada intento, asi que puedes hacerlo tantas veces como quieras, y esa corrida limpia "
             "es la que se califica."),
            ("Puse solo dos facturas como pide el enunciado y me falla el INSERT. ¿Por que?",
             "Por la cadena de dependencias, y es lo que rompe mas semillas. `factura.id_consulta` "
             "es `NOT NULL REFERENCES consulta`, asi que dos facturas necesitan **dos consultas**; y "
             "`consulta.id_cita` es **UNIQUE**, asi que esas dos consultas necesitan **dos citas "
             "distintas**, y con sentido, ambas `ATENDIDA`. Si tu semilla tiene una sola consulta, "
             "la segunda factura no tiene donde apoyarse. Revisa el orden completo: dueno → mascota "
             "→ veterinario → cita → consulta → factura → detalle_factura."),
            ("En la pregunta 2 mi consulta con JOIN normal da el mismo resultado que con LEFT JOIN. "
             "¿Entonces da igual?",
             "No da igual, y que den lo mismo es precisamente el problema: **la semilla no ejerce "
             "el caso de borde.** Los cuatro veterinarios tienen citas y los seis insumos se han "
             "vendido, asi que la consulta correcta y la incorrecta son indistinguibles con estos "
             "datos. Creale el caso: `INSERT INTO veterinario (nombre, especialidad) VALUES "
             "('Sara Quintero', 'Odontologia');` y un insumo nuevo sin ventas. Ahi veras que con "
             "`JOIN` interno desaparecen del reporte y con `LEFT JOIN` aparecen con ceros. Vale 4 "
             "de los 20 puntos de la pregunta, y es el habito que importa: un KPI que no se ha "
             "probado contra su caso de borde es una suposicion. La excepcion es K4, cuyo caso de "
             "borde si esta en los datos —dos de las cuatro citas de Ana Gomez no tienen "
             "consulta—."),
            ("Los totales de las facturas no me cuadran con los detalles. ¿Esta mal la base?",
             "Los datos son los que son y tu observacion es correcta: **las tres facturas de la "
             "semilla estan descuadradas**, y no por poco. `factura.total` no coincide con "
             "`consulta.precio` mas la suma del detalle en ninguna de las tres. Es la misma "
             "inconsistencia que encontro la prueba 5 del taller de la Clase 11, y no es un error "
             "de tu consulta. K2 pide sumar `factura.total`, asi que suma eso. Lo que se premia es "
             "que lo digas: lleva a la sustentacion la tabla que compara el total guardado con el "
             "derivado y la conclusion, que es la de la Clase 11 —hay que elegir **una** definicion "
             "del total y hacerla cumplir con una restriccion o un trigger, porque el mismo dato en "
             "dos sitios sin nada que los mantenga iguales siempre termina divergiendo—."),
            ("¿Puedo escribir la prueba 3 con el mismo molde que las dos primeras?",
             "No, y es el error mas comun del bloque 5. Las pruebas 1 y 2 son **negativas**: lo "
             "correcto es que revienten, y el `EXCEPTION` es lo que atrapa la prueba. La 3 es "
             "**positiva**: lo correcto es que ocurra un efecto —que `audit_cita` crezca—, y ahi un "
             "`EXCEPTION WHEN OTHERS` no prueba nada, porque el bloque no falla y el `RAISE NOTICE` "
             "imprimiria «OK» tambien con el trigger eliminado. Una prueba positiva **compara**: "
             "cuenta las filas antes, hace el `UPDATE`, cuenta despues y verifica que subio en 1. "
             "Ese `IF` es la prueba."),
            ("¿Es obligatorio el trigger de auditoria si ya tengo la tabla `audit_cita`?",
             "Si, y son cosas distintas: la tabla es donde se guarda, el trigger es lo que "
             "garantiza que **siempre** se guarde sin que nadie tenga que acordarse. Si la bitacora "
             "la llena la aplicacion, solo queda traza de lo que pasa por la aplicacion. Dos "
             "detalles que cuestan puntos. Uno: en PostgreSQL son **dos objetos**, la funcion "
             "`RETURNS TRIGGER` y el `CREATE TRIGGER ... EXECUTE FUNCTION` que la asocia; escribir "
             "la logica dentro del `CREATE TRIGGER` no compila y es la herencia de Oracle que mas "
             "se repite. Dos: la verificacion esta en el inventario del bloque 6 —si `audit_cita` "
             "sale en **0**, el trigger no se disparo y tu prueba 3 no probo nada aunque haya "
             "impreso «OK»—."),
            ("En la autoevaluacion, ¿me perjudica admitir que no ensaye el restore o que no entendi "
             "algo?",
             "Al contrario, y esto es en serio. El punto 5 **pide** lo que no pudiste verificar, y "
             "el punto 3 dice literalmente que reconocer una duda vale mas que fingir. Lo que "
             "perjudica es lo otro: declarar «todo verificado» cuando el checklist de la Clase 11 "
             "tiene el item del respaldo en `NO`, porque entonces hay dos entregables tuyos que se "
             "contradicen y el jurado lo va a encontrar. La diferencia entre una debilidad y un "
             "criterio esta en el metodo: no basta «no pude probar la concurrencia», hace falta "
             "«no pude, porque el entorno es de una sola sesion, y en produccion lo probaria con "
             "dos clientes `psql`, `BEGIN` en los dos y el mismo `INSERT`, esperando ver el "
             "`23505`». Eso no es una excusa: es la unica prueba que falta, y ya sabes escribirla."),
        ],
        "cierre": [
            "Al terminar, cada estudiante debe tener entregado: el **script maestro** con sus siete "
            "bloques corriendo de cero sin un solo error, las tres pruebas de aceptacion imprimiendo "
            "`OK` y el inventario cerrando en `5 | 3 | 8 | 8 | 2 | 4 | 2 | 4 | 1`; los **cuatro "
            "KPIs** con sus numeros —178.200,00 en septiembre, las 4 filas de la ficha de Ana Gomez, "
            "el 50,0 % de Paula Salazar y la fila del insumo nunca vendido—; las **cuatro opciones "
            "correctas** del checklist del ZIP; el **acta** con inventario, trazabilidad de las once "
            "clases y un guion de entre 5 y 8 minutos; y la **autoevaluacion** con las tres "
            "diferencias PL/SQL → PL/pgSQL y la lista de lo que no se pudo verificar.",
            "Cinco comprobaciones antes de subir el ZIP, todas de mirar un numero o abrir un "
            "archivo. Que el script maestro corra **de cero y de una sola vez**, sin comentar nada "
            "—la base de ExamLab se vuelve a sembrar en cada intento, asi que no hay excusa para no "
            "haberlo probado—. Que las tres lineas del bloque 5 digan `OK` y ninguna diga `FALLO`, "
            "y que `audit_cita` salga en **1** y no en 0. Que en la pregunta 2 el reporte muestre "
            "**la fila con ceros** del veterinario sin citas y la del insumo sin ventas: si no "
            "estan, la consulta no se probo contra su caso de borde. Que cada archivo que nombra el "
            "acta **exista** en el ZIP, y que el ER coincida con el DDL. Y que el guion **sume** "
            "entre 5 y 8 minutos, contando la columna.",
            "Este taller cierra el semestre con la misma idea con la que se cerro la Clase 13, "
            "porque es la que atraviesa el curso: **una afirmacion no verificada no es un "
            "resultado.** «El script corre» se comprueba ejecutandolo de cero; «los datos cumplen "
            "los minimos» se comprueba con la consulta 6b; «la regla de negocio esta» se comprueba "
            "con una prueba que la viola a proposito y falla; «el KPI conserva los casos sin "
            "datos» se comprueba creando el caso; y «tengo respaldo» se comprueba restaurando. Lo "
            "que se lleva un estudiante de Bases de Datos II no es la sintaxis de PL/pgSQL —eso se "
            "busca— sino el reflejo de preguntarse **como se comprueba** antes de declarar algo "
            "hecho. En la sustentacion del **2026-11-16** eso se ve en treinta segundos: quien "
            "trae numeros propios y sabe cual le falta esta parado sobre su trabajo; quien trae "
            "adjetivos, sobre su memoria. Y de las dos cosas que este paquete deja abiertas —el "
            "restore sin ensayar y el particionamiento sin volumen—, la primera es la que hay que "
            "decir en voz alta antes de que la pregunten.",
        ],
    },
}
