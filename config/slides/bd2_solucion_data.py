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
}
