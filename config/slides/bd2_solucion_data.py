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
                "n": 5, "titulo": "Politica de altas y bajas de usuarios (y limites del entorno)",
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
                    "**5. Limite del entorno de practica.** En ExamLab la base es PostgreSQL "
                    "corriendo en el navegador, con **una sola sesion y un solo usuario**. Eso "
                    "alcanza para todo lo que es DDL de permisos — crear los cuatro roles, "
                    "otorgar, revocar, crear la vista, recortar por columna — y para verificarlo "
                    "con `information_schema`, porque esas consultas describen el estado del "
                    "catalogo y no requieren cambiar de identidad. Lo que **no** se puede hacer es "
                    "la prueba negativa: conectarse como `recepcion` e intentar un `DELETE FROM "
                    "cita` para ver el rechazo. En un servidor real se hace sin cambiar de "
                    "conexion, con `SET ROLE recepcion;` seguido de `DELETE FROM cita WHERE "
                    "id_cita = 1;`, y el resultado esperado es el error `permission denied for "
                    "table cita`; despues se vuelve con `RESET ROLE`. La ausencia de esa prueba es "
                    "una brecha de verificacion concreta en esta entrega: se comprobo que el "
                    "permiso **esta escrito** como se decidio, no que el motor **lo hace "
                    "cumplir**. Son dos afirmaciones distintas y solo una quedo demostrada."
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
                    "**3 pts — la seccion 5.** 1 pt por identificar bien la limitacion (una sola "
                    "sesion, no «no se pueden crear roles»), 1 pt por proponer `SET ROLE` u otra "
                    "conexion como prueba negativa, y 1 pt por nombrar la consecuencia: que sin "
                    "esa prueba lo verificado es la configuracion y no el cumplimiento.",
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
             "No en ExamLab, porque hay una sola sesion. En un servidor real, sin abrir otra "
             "conexion: `SET ROLE recepcion;` y luego `DELETE FROM cita WHERE id_cita = 1;`, que "
             "debe responder `permission denied for table cita`; se vuelve con `RESET ROLE`. Esa es "
             "la respuesta que vale puntos en la pregunta 5."),
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
}
