# -*- coding: utf-8 -*-
"""Especificacion de los talleres en ExamLab - Bases de Datos II 2026-2.

La consume `examlab_talleres.py` para (a) decirle al estudiante, dentro del .docx
del taller, que va a encontrar en la plataforma y en que forma se responde cada
pregunta, y (b) generar en el Kit docente la guia con el texto exacto de cada
campo para crear el taller en ExamLab.

Por que existe: el taller decia «suba el resultado a ExamLab» y nada mas. El
estudiante no sabia que iba a encontrar, y el material pedia exportar PNG de
draw.io o correr SQL en DB Fiddle cuando la plataforma ya trae editor Mermaid,
PostgreSQL real (PGlite/WASM) y ejecucion de GUI de Java en el navegador.

Tipos usados, todos verificados contra el codigo de ExamLab
(`src/modules/workshops/WorkshopQuestions.tsx`):
    abierta · cerrada · cerrada_multi · codigo · diagrama · java_gui ·
    python_gui · codigo_zip · red_consola · red_gui · so_consola · bd_sql

OJO CON EL DIALECTO: ExamLab ejecuta PostgreSQL real (PGlite), NO Oracle. El resto
del material del curso usa Oracle Live SQL / PL-SQL; el SQL de este archivo esta
en PostgreSQL/PL-pgSQL a proposito, porque es el que va a correr en la plataforma.

Cada taller suma 100 puntos.
"""

EXAMLAB = {1: {'preguntas': [{'enunciado': '## 1. DDL base de VetCare DB\n'
                                 '\n'
                                 'La clinica veterinaria **Huellitas** arranca su base de datos '
                                 '`VetCare DB`. En esta base ya existe una tabla `proyecto_pi` '
                                 'donde cada estudiante registra su Proyecto Integrador.\n'
                                 '\n'
                                 '> **Modalidad de trabajo: individual por defecto.** El docente '
                                 'puede autorizar equipos de 2 o 3 integrantes; en ese caso el '
                                 'artefacto puede ser compartido, pero **la entrega en ExamLab '
                                 'siempre es individual**.\n'
                                 '\n'
                                 '**Escribe el SQL (PostgreSQL) que:**\n'
                                 '\n'
                                 '1. Registre tu proyecto en `proyecto_pi` con tu nombre completo, '
                                 'tu codigo y el nombre de tu proyecto. Si el docente te autorizo '
                                 'trabajar en equipo, lista ademas los otros integrantes en la '
                                 'columna opcional `integrantes`; si trabajas solo, dejala nula.\n'
                                 '2. Cree las **tres tablas base** con estas reglas exactas:\n'
                                 '\n'
                                 '| Tabla | Columnas y restricciones |\n'
                                 '|---|---|\n'
                                 '| `dueno` | `id_dueno` autonumerico PK; `nombre` texto '
                                 'obligatorio; `telefono`; `email`; `ciudad` con valor por defecto '
                                 "`'Cali'` |\n"
                                 '| `mascota` | `id_mascota` autonumerico PK; `id_dueno` '
                                 'obligatorio con **FK** a `dueno`; `nombre` obligatorio; '
                                 '`especie` obligatoria; `fecha_nac` tipo fecha; `activa` de un '
                                 "caracter, por defecto `'S'`, que **solo** acepte `'S'` o `'N'` "
                                 '|\n'
                                 '| `cita` | `id_cita` autonumerico PK; `id_mascota` obligatorio '
                                 'con **FK** a `mascota`; `fecha_hora` tipo `TIMESTAMP` '
                                 "obligatorio; `estado` texto por defecto `'PROGRAMADA'` que "
                                 "**solo** acepte `'PROGRAMADA'`, `'ATENDIDA'` o `'CANCELADA'` |\n"
                                 '\n'
                                 '3. Inserte **3 duenos**, **4 mascotas** (al menos una con '
                                 "`activa = 'N'`) y **3 citas** con datos realistas de una "
                                 "veterinaria en Cali (nombres en espanol: 'Firulais', 'Ana "
                                 "Gomez', ...).\n"
                                 '4. Termine con un `SELECT` que muestre nombre de mascota, nombre '
                                 'del dueno y fecha de la cita usando `JOIN`.\n'
                                 '\n'
                                 '**Recuerda:** el motor es **PostgreSQL**, no Oracle. Usa '
                                 '`SERIAL` (o `GENERATED ALWAYS AS IDENTITY`) y `TEXT`/`VARCHAR`; '
                                 'no existen `NUMBER` ni `VARCHAR2`.',
                    'puntos': 30,
                    'rubrica': 'Las 3 tablas se crean sin error con PK, las 2 FK, el DEFAULT de '
                               'ciudad y los 2 CHECK exigidos (activa y estado). Se insertan al '
                               'menos 3 duenos, 4 mascotas (>=1 inactiva) y 3 citas coherentes con '
                               'las FK. El SELECT final devuelve filas y usa JOIN explicito, no '
                               'producto cartesiano. Sintaxis 100% PostgreSQL (SERIAL/TEXT); se '
                               'penaliza NUMBER, VARCHAR2 o comillas dobles mal usadas. Se '
                               'registra el proyecto propio en proyecto_pi (estudiante, codigo y '
                               'proyecto); la columna integrantes solo se llena si hubo equipo '
                               'autorizado y su ausencia no descuenta.',
                    'setup_sql': '-- Base limpia para el arranque de VetCare DB.\n'
                                 '-- Solo se entrega la bitacora de proyectos; el esquema lo '
                                 'construye el estudiante.\n'
                                 'CREATE TABLE proyecto_pi (\n'
                                 '  id_registro SERIAL PRIMARY KEY,\n'
                                 '  estudiante TEXT NOT NULL,\n'
                                 '  codigo TEXT NOT NULL,\n'
                                 '  proyecto TEXT NOT NULL,\n'
                                 '  integrantes TEXT,  -- opcional: solo si el docente autorizo '
                                 'equipo\n'
                                 '  fecha_registro DATE NOT NULL DEFAULT CURRENT_DATE\n'
                                 ');\n'
                                 '\n'
                                 'INSERT INTO proyecto_pi (estudiante, codigo, proyecto)\n'
                                 "VALUES ('Ejemplo del docente', '000000', 'VetCare-Demo');\n",
                    'tipo': 'bd_sql'},
                   {'enunciado': '## 2. Modelo ER de VetCare DB en Mermaid\n'
                                 '\n'
                                 'Dibuja el **modelo entidad-relacion completo** del Proyecto '
                                 'Integrador usando `erDiagram` de Mermaid. Debe contener las **8 '
                                 'entidades** del dominio y las relaciones con su cardinalidad:\n'
                                 '\n'
                                 '- `dueno` **1 - N** `mascota`\n'
                                 '- `mascota` **1 - N** `cita`\n'
                                 '- `veterinario` **1 - N** `cita`\n'
                                 '- `cita` **1 - 1** `consulta`\n'
                                 '- `consulta` **1 - N** `factura`\n'
                                 '- `factura` **1 - N** `detalle_factura`\n'
                                 '- `insumo` **1 - N** `detalle_factura`\n'
                                 '\n'
                                 'Para cada entidad lista **al menos su PK y 2 atributos**, '
                                 'marcando `PK` y `FK`. Este diagrama es el ER borrador del '
                                 'entregable de la clase: exportalo tambien como PNG para tu '
                                 'carpeta del PI.',
                    'mermaid_esperado': 'erDiagram\n'
                                        '    dueno {\n'
                                        '        int id_dueno PK\n'
                                        '        text nombre\n'
                                        '        text telefono\n'
                                        '    }\n'
                                        '    mascota {\n'
                                        '        int id_mascota PK\n'
                                        '        int id_dueno FK\n'
                                        '        text nombre\n'
                                        '        char activa\n'
                                        '    }\n'
                                        '    veterinario {\n'
                                        '        int id_veterinario PK\n'
                                        '        text nombre\n'
                                        '        text especialidad\n'
                                        '    }\n'
                                        '    cita {\n'
                                        '        int id_cita PK\n'
                                        '        int id_mascota FK\n'
                                        '        int id_veterinario FK\n'
                                        '        timestamp fecha_hora\n'
                                        '        text estado\n'
                                        '    }\n'
                                        '    consulta {\n'
                                        '        int id_consulta PK\n'
                                        '        int id_cita FK\n'
                                        '        text diagnostico\n'
                                        '        numeric precio\n'
                                        '    }\n'
                                        '    factura {\n'
                                        '        int id_factura PK\n'
                                        '        int id_consulta FK\n'
                                        '        numeric total\n'
                                        '    }\n'
                                        '    detalle_factura {\n'
                                        '        int id_detalle PK\n'
                                        '        int id_factura FK\n'
                                        '        int id_insumo FK\n'
                                        '        int cantidad\n'
                                        '    }\n'
                                        '    insumo {\n'
                                        '        int id_insumo PK\n'
                                        '        text nombre\n'
                                        '        int stock\n'
                                        '    }\n'
                                        '    dueno ||--o{ mascota : tiene\n'
                                        '    mascota ||--o{ cita : genera\n'
                                        '    veterinario ||--o{ cita : atiende\n'
                                        '    cita ||--|| consulta : produce\n'
                                        '    consulta ||--o{ factura : facturada_en\n'
                                        '    factura ||--o{ detalle_factura : contiene\n'
                                        '    insumo ||--o{ detalle_factura : aparece_en',
                    'puntos': 20,
                    'rubrica': 'El diagrama renderiza sin error de sintaxis Mermaid (erDiagram). '
                               'Aparecen las 8 entidades con nombres exactos y las 7 relaciones '
                               'con la cardinalidad correcta (||--o{ para 1-N, ||--|| para 1-1). '
                               'Cada entidad declara al menos PK + 2 atributos, con PK/FK '
                               'marcados. Se descuenta por entidades faltantes, cardinalidades '
                               'invertidas o relaciones inventadas.',
                    'tipo': 'diagrama'},
                   {'enunciado': '## 3. Consultas de repaso sobre datos reales de Huellitas\n'
                                 '\n'
                                 'El esquema `dueno`, `mascota`, `veterinario` y `cita` **ya esta '
                                 'creado y poblado** (6 duenos, 4 veterinarios, 8 mascotas, 10 '
                                 'citas). Recuerda que **Rocky (id 3)** y **Kiara (id 8)** estan '
                                 'inactivas.\n'
                                 '\n'
                                 'Escribe **cuatro consultas**, en este orden, separadas por `;`:\n'
                                 '\n'
                                 '1. **Agenda del 1 de septiembre de 2026**: `id_cita`, '
                                 '`fecha_hora`, nombre de la mascota, nombre del dueno y nombre '
                                 'del veterinario, solo citas en estado `PROGRAMADA`, ordenadas '
                                 'por hora. Filtra por **rango de fecha** (`>=` y `<`), no con '
                                 'funciones sobre la columna.\n'
                                 '2. **Mascotas sin ninguna cita registrada**: nombre de la '
                                 'mascota y de su dueno. Usa `LEFT JOIN ... IS NULL` o `NOT '
                                 'EXISTS`.\n'
                                 '3. **Citas por veterinario**: nombre del veterinario y cuantas '
                                 'citas tiene en cada estado (`PROGRAMADA`, `ATENDIDA`, '
                                 '`CANCELADA`), con `COUNT` y `GROUP BY`. Los veterinarios sin '
                                 'citas deben aparecer igualmente.\n'
                                 '4. **Riesgo de negocio**: citas cuyo estado no sea `CANCELADA` '
                                 "pero cuya mascota este **inactiva** (`activa = 'N'`). Muestra "
                                 '`id_cita`, mascota y estado. Si el resultado sale vacio, la '
                                 'regla de negocio se cumple hoy.',
                    'puntos': 25,
                    'rubrica': 'Las 4 consultas corren sin error y responden exactamente lo '
                               'pedido. (1) usa rango de TIMESTAMP y no to_char/EXTRACT sobre '
                               'fecha_hora. (2) detecta correctamente las mascotas huerfanas de '
                               'cita. (3) incluye veterinarios sin citas (LEFT JOIN, no INNER). '
                               '(4) cruza cita con mascota inactiva y excluye CANCELADA. Se '
                               'descuenta por SELECT *, joins implicitos con comas o resultados '
                               'que no correspondan a los datos entregados.',
                    'setup_sql': 'CREATE TABLE dueno (\n'
                                 '  id_dueno SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  telefono TEXT,\n'
                                 '  email TEXT,\n'
                                 "  ciudad TEXT DEFAULT 'Cali'\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE mascota (\n'
                                 '  id_mascota SERIAL PRIMARY KEY,\n'
                                 '  id_dueno INT NOT NULL REFERENCES dueno(id_dueno),\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especie TEXT NOT NULL,\n'
                                 '  fecha_nac DATE,\n'
                                 "  activa CHAR(1) NOT NULL DEFAULT 'S' CHECK (activa IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE veterinario (\n'
                                 '  id_veterinario SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especialidad TEXT,\n'
                                 "  activo CHAR(1) NOT NULL DEFAULT 'S' CHECK (activo IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE cita (\n'
                                 '  id_cita SERIAL PRIMARY KEY,\n'
                                 '  id_mascota INT NOT NULL REFERENCES mascota(id_mascota),\n'
                                 '  id_veterinario INT NOT NULL REFERENCES '
                                 'veterinario(id_veterinario),\n'
                                 '  fecha_hora TIMESTAMP NOT NULL,\n'
                                 "  estado TEXT NOT NULL DEFAULT 'PROGRAMADA'\n"
                                 "    CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))\n"
                                 ');\n'
                                 '\n'
                                 '-- Duenos (ids 1..6 en este orden)\n'
                                 'INSERT INTO dueno (nombre, telefono, email) VALUES\n'
                                 "  ('Ana Gomez',      '3001112233', 'ana.gomez@mail.com'),\n"
                                 "  ('Carlos Ruiz',    '3014445566', 'carlos.ruiz@mail.com'),\n"
                                 "  ('Marcela Diaz',   '3027778899', 'marcela.diaz@mail.com'),\n"
                                 "  ('Jorge Pineda',   '3105551212', 'jorge.pineda@mail.com'),\n"
                                 "  ('Luisa Cardona',  '3123334455', 'luisa.cardona@mail.com'),\n"
                                 "  ('Andres Vallejo', '3159998877', 'andres.vallejo@mail.com');\n"
                                 '\n'
                                 '-- Veterinarios (ids 1..4)\n'
                                 'INSERT INTO veterinario (nombre, especialidad) VALUES\n'
                                 "  ('Laura Restrepo', 'General'),\n"
                                 "  ('Diego Moreno',   'Cirugia'),\n"
                                 "  ('Paula Salazar',  'Dermatologia'),\n"
                                 "  ('Ivan Ortiz',     'General');\n"
                                 '\n'
                                 '-- Mascotas (ids 1..8). Rocky (3) y Kiara (8) estan INACTIVAS.\n'
                                 'INSERT INTO mascota (id_dueno, nombre, especie, fecha_nac, '
                                 'activa) VALUES\n'
                                 "  (1, 'Firulais', 'Canino', DATE '2019-04-12', 'S'),\n"
                                 "  (1, 'Luna',     'Felino', DATE '2021-08-30', 'S'),\n"
                                 "  (2, 'Rocky',    'Canino', DATE '2015-01-20', 'N'),\n"
                                 "  (3, 'Mishi',    'Felino', DATE '2022-11-05', 'S'),\n"
                                 "  (3, 'Bobby',    'Canino', DATE '2018-06-17', 'S'),\n"
                                 "  (4, 'Nube',     'Felino', DATE '2023-02-09', 'S'),\n"
                                 "  (5, 'Toby',     'Canino', DATE '2020-09-25', 'S'),\n"
                                 "  (6, 'Kiara',    'Canino', DATE '2013-03-03', 'N');\n"
                                 '\n'
                                 '-- Citas (ids 1..10)\n'
                                 'INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                 'estado) VALUES\n'
                                 "  (1, 1, TIMESTAMP '2026-09-01 08:00:00', 'PROGRAMADA'),\n"
                                 "  (2, 1, TIMESTAMP '2026-09-01 09:00:00', 'ATENDIDA'),\n"
                                 "  (4, 2, TIMESTAMP '2026-09-01 10:00:00', 'PROGRAMADA'),\n"
                                 "  (5, 3, TIMESTAMP '2026-09-02 08:30:00', 'CANCELADA'),\n"
                                 "  (6, 2, TIMESTAMP '2026-09-02 11:00:00', 'ATENDIDA'),\n"
                                 "  (7, 4, TIMESTAMP '2026-09-03 07:45:00', 'PROGRAMADA'),\n"
                                 "  (1, 1, TIMESTAMP '2026-09-05 15:00:00', 'ATENDIDA'),\n"
                                 "  (2, 3, TIMESTAMP '2026-09-08 16:00:00', 'PROGRAMADA'),\n"
                                 "  (4, 4, TIMESTAMP '2026-09-10 08:00:00', 'PROGRAMADA'),\n"
                                 "  (6, 1, TIMESTAMP '2026-09-10 09:00:00', 'ATENDIDA');\n",
                    'tipo': 'bd_sql'},
                   {'correctas': [0, 2, 3, 5],
                    'enunciado': '## 4. Que puede garantizar el DDL por si solo\n'
                                 '\n'
                                 'En VetCare DB hay tres reglas de negocio criticas:\n'
                                 '\n'
                                 '- **R1:** una mascota inactiva no puede tener una cita nueva.\n'
                                 '- **R2:** el stock de un insumo nunca queda negativo.\n'
                                 '- **R3:** todo cambio de estado de una cita queda auditado.\n'
                                 '\n'
                                 'Selecciona **todas** las afirmaciones correctas sobre lo que se '
                                 'puede resolver con DDL declarativo (tipos, `NOT NULL`, `CHECK`, '
                                 '`UNIQUE`, `PRIMARY KEY`, `FOREIGN KEY`) frente a lo que exige '
                                 'logica programada (funcion, procedimiento o trigger) en '
                                 'PostgreSQL.',
                    'opciones': ['R2 se puede garantizar con un CHECK (stock >= 0) sobre la tabla '
                                 'insumo, porque solo depende de la fila que se modifica.',
                                 'R1 se puede garantizar con un CHECK en la tabla cita que '
                                 'consulte la columna activa de mascota.',
                                 'R1 necesita logica programada (trigger o procedimiento) porque '
                                 'involucra una fila de OTRA tabla en el momento de la insercion.',
                                 'R3 necesita un trigger AFTER UPDATE sobre cita: el DDL '
                                 'declarativo no registra historia de cambios.',
                                 'Una FOREIGN KEY de cita hacia mascota alcanza para impedir '
                                 'agendar mascotas inactivas.',
                                 "El CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA')) es un "
                                 'buen uso de DDL: valida un dominio cerrado sin mirar otras '
                                 'tablas.'],
                    'puntos': 10,
                    'rubrica': 'Se otorgan los 10 puntos con las 4 opciones correctas marcadas y '
                               'ninguna incorrecta; puntaje proporcional por acierto parcial. '
                               'Correctas: indices 0, 2, 3 y 5.',
                    'tipo': 'cerrada_multi'},
                   {'enunciado': '## 5. Alcance del Proyecto Integrador VetCare DB\n'
                                 '\n'
                                 'Redacta la ficha de alcance de tu proyecto. Debe incluir, con '
                                 'estos titulos:\n'
                                 '\n'
                                 '1. **Autor y proyecto**: tu nombre y codigo, el nombre de tu '
                                 'proyecto y una frase que describa VetCare DB. Si el docente '
                                 'autorizo equipo, agrega los otros integrantes.\n'
                                 '2. **Que SI hara el PI** (5 a 8 lineas): procesos de la clinica '
                                 'Huellitas que la base de datos va a soportar (por ejemplo '
                                 'agendamiento, historia clinica, facturacion con insumos, '
                                 'auditoria).\n'
                                 '3. **Que NO hara el PI** (3 a 5 lineas): limites explicitos (por '
                                 'ejemplo: no habra pasarela de pagos, no habra app movil, no se '
                                 'manejara nomina).\n'
                                 '4. **Tres reglas de negocio propias** que tu adoptas, distintas o '
                                 'adicionales a las tres del enunciado general, escritas de forma '
                                 'verificable ("...no puede...", "...siempre debe..."). Para cada '
                                 'una, indica **como piensas implementarla**: `CHECK`, `UNIQUE`, '
                                 '`FK`, trigger o procedimiento.\n'
                                 '5. **Riesgo principal** que ves para terminar el PI y como lo '
                                 'mitigas.',
                    'puntos': 15,
                    'rubrica': 'Estan las 5 secciones. El SI/NO delimita el alcance de forma '
                               'concreta y realista para un semestre (no promesas vagas). Las 3 '
                               'reglas de negocio son verificables y cada una viene con el '
                               'mecanismo de implementacion propuesto, coherente con lo visto en '
                               'la pregunta 4. Se descuenta si las reglas repiten literalmente las '
                               'del enunciado o si no se indica mecanismo.',
                    'tipo': 'abierta'}],
     'resumen': 'El estudiante deja creado el esqueleto de VetCare DB (dueno, mascota, cita) con '
                'integridad declarativa, su modelo ER en Mermaid y el alcance escrito del Proyecto '
                'Integrador.',
     'titulo': 'Taller Clase 1 en ExamLab - Arranque VetCare DB y repaso de DDL'},
 2: {'preguntas': [{'enunciado': '## 1. Crear los roles de VetCare y otorgar privilegios\n'
                                 '\n'
                                 '**Todo lo que necesitas esta aqui; si algo no te corre, '
                                 'preguntalo en clase antes de irte.**\n'
                                 '\n'
                                 'El esquema de VetCare (`dueno`, `mascota`, `veterinario`, '
                                 '`cita`, `consulta`, `insumo`, `factura`, `detalle_factura`) ya '
                                 'esta creado y poblado.\n'
                                 '\n'
                                 'En PostgreSQL un **rol** es la unidad de permisos (`CREATE '
                                 'ROLE`), y los permisos se dan y quitan con `GRANT` / `REVOKE`. '
                                 'Escribe el SQL que:\n'
                                 '\n'
                                 '1. Cree **cuatro roles sin login**: `admin_bd`, `recepcion`, '
                                 '`veterinario_rol`, `auditor`.\n'
                                 '   Usa `CREATE ROLE <nombre> NOLOGIN;` (el nombre del rol del '
                                 'veterinario lleva sufijo `_rol` para no chocar con la tabla '
                                 '`veterinario`).\n'
                                 '2. Otorgue exactamente estos privilegios:\n'
                                 '   - `recepcion`: `SELECT, INSERT, UPDATE` sobre `cita`; solo '
                                 '`SELECT` sobre `dueno`, `mascota` y `veterinario`. **Sin DELETE '
                                 'en ninguna tabla.**\n'
                                 '   - `veterinario_rol`: `SELECT` sobre `cita` y `mascota`; '
                                 '`SELECT, INSERT, UPDATE` sobre `consulta`.\n'
                                 '   - `auditor`: **solo** `SELECT` sobre `dueno`, `mascota`, '
                                 '`cita`, `consulta` y `factura`.\n'
                                 '   - `admin_bd`: `ALL PRIVILEGES` sobre `cita`, `consulta`, '
                                 '`factura`, `detalle_factura` e `insumo`.\n'
                                 '3. Ejecute un `REVOKE` **explicito y documentado** que quite '
                                 '`DELETE` sobre `cita` a `recepcion` (deja la sentencia aunque '
                                 'sea redundante: es la evidencia de la decision de diseno).\n'
                                 '4. Termine con una consulta de **verificacion** sobre '
                                 '`information_schema.role_table_grants` que muestre `grantee`, '
                                 '`table_name` y `privilege_type` para los cuatro roles, ordenada '
                                 'por `grantee, table_name, privilege_type`.\n'
                                 '\n'
                                 '**Nota tecnica importante:** ExamLab ejecuta PostgreSQL en el '
                                 'navegador con **una sola sesion de un unico usuario**. Por eso '
                                 'puedes crear roles y otorgar privilegios (es DDL real y '
                                 'verificable), pero **no** puedes conectarte simultaneamente como '
                                 '`recepcion` y comprobar en vivo que le rebotan las sentencias. '
                                 'Esa parte se analiza en la pregunta 5.',
                    'puntos': 30,
                    'rubrica': 'Los 4 roles se crean sin error y los GRANT reproducen exactamente '
                               'la matriz pedida, sin privilegios de mas ni de menos (en '
                               'particular auditor solo con SELECT y recepcion sin DELETE). Existe '
                               'el REVOKE explicito de DELETE sobre cita a recepcion. La consulta '
                               'final sobre information_schema.role_table_grants devuelve filas de '
                               'los 4 roles y permite auditar la matriz. Sintaxis PostgreSQL, sin '
                               'CREATE USER de Oracle ni GRANT de privilegios de sistema '
                               'inventados.',
                    'setup_sql': 'CREATE TABLE dueno (\n'
                                 '  id_dueno SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  telefono TEXT,\n'
                                 '  email TEXT,\n'
                                 "  ciudad TEXT DEFAULT 'Cali'\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE mascota (\n'
                                 '  id_mascota SERIAL PRIMARY KEY,\n'
                                 '  id_dueno INT NOT NULL REFERENCES dueno(id_dueno),\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especie TEXT NOT NULL,\n'
                                 '  fecha_nac DATE,\n'
                                 "  activa CHAR(1) NOT NULL DEFAULT 'S' CHECK (activa IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE veterinario (\n'
                                 '  id_veterinario SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especialidad TEXT,\n'
                                 "  activo CHAR(1) NOT NULL DEFAULT 'S' CHECK (activo IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE cita (\n'
                                 '  id_cita SERIAL PRIMARY KEY,\n'
                                 '  id_mascota INT NOT NULL REFERENCES mascota(id_mascota),\n'
                                 '  id_veterinario INT NOT NULL REFERENCES '
                                 'veterinario(id_veterinario),\n'
                                 '  fecha_hora TIMESTAMP NOT NULL,\n'
                                 "  estado TEXT NOT NULL DEFAULT 'PROGRAMADA'\n"
                                 "    CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE consulta (\n'
                                 '  id_consulta SERIAL PRIMARY KEY,\n'
                                 '  id_cita INT NOT NULL UNIQUE REFERENCES cita(id_cita),\n'
                                 '  diagnostico TEXT,\n'
                                 '  precio NUMERIC(12,2) NOT NULL CHECK (precio >= 0)\n'
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE insumo (\n'
                                 '  id_insumo SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  stock INT NOT NULL CHECK (stock >= 0),\n'
                                 '  precio_unit NUMERIC(12,2) NOT NULL\n'
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE factura (\n'
                                 '  id_factura SERIAL PRIMARY KEY,\n'
                                 '  id_consulta INT NOT NULL REFERENCES consulta(id_consulta),\n'
                                 '  fecha TIMESTAMP NOT NULL DEFAULT now(),\n'
                                 '  total NUMERIC(12,2) NOT NULL DEFAULT 0\n'
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE detalle_factura (\n'
                                 '  id_detalle SERIAL PRIMARY KEY,\n'
                                 '  id_factura INT NOT NULL REFERENCES factura(id_factura) ON '
                                 'DELETE CASCADE,\n'
                                 '  id_insumo INT NOT NULL REFERENCES insumo(id_insumo),\n'
                                 '  cantidad INT NOT NULL CHECK (cantidad > 0),\n'
                                 '  precio_unit NUMERIC(12,2) NOT NULL\n'
                                 ');\n'
                                 '\n'
                                 '-- Duenos (ids 1..6 en este orden)\n'
                                 'INSERT INTO dueno (nombre, telefono, email) VALUES\n'
                                 "  ('Ana Gomez',      '3001112233', 'ana.gomez@mail.com'),\n"
                                 "  ('Carlos Ruiz',    '3014445566', 'carlos.ruiz@mail.com'),\n"
                                 "  ('Marcela Diaz',   '3027778899', 'marcela.diaz@mail.com'),\n"
                                 "  ('Jorge Pineda',   '3105551212', 'jorge.pineda@mail.com'),\n"
                                 "  ('Luisa Cardona',  '3123334455', 'luisa.cardona@mail.com'),\n"
                                 "  ('Andres Vallejo', '3159998877', 'andres.vallejo@mail.com');\n"
                                 '\n'
                                 '-- Veterinarios (ids 1..4)\n'
                                 'INSERT INTO veterinario (nombre, especialidad) VALUES\n'
                                 "  ('Laura Restrepo', 'General'),\n"
                                 "  ('Diego Moreno',   'Cirugia'),\n"
                                 "  ('Paula Salazar',  'Dermatologia'),\n"
                                 "  ('Ivan Ortiz',     'General');\n"
                                 '\n'
                                 '-- Mascotas (ids 1..8). Rocky (3) y Kiara (8) estan INACTIVAS.\n'
                                 'INSERT INTO mascota (id_dueno, nombre, especie, fecha_nac, '
                                 'activa) VALUES\n'
                                 "  (1, 'Firulais', 'Canino', DATE '2019-04-12', 'S'),\n"
                                 "  (1, 'Luna',     'Felino', DATE '2021-08-30', 'S'),\n"
                                 "  (2, 'Rocky',    'Canino', DATE '2015-01-20', 'N'),\n"
                                 "  (3, 'Mishi',    'Felino', DATE '2022-11-05', 'S'),\n"
                                 "  (3, 'Bobby',    'Canino', DATE '2018-06-17', 'S'),\n"
                                 "  (4, 'Nube',     'Felino', DATE '2023-02-09', 'S'),\n"
                                 "  (5, 'Toby',     'Canino', DATE '2020-09-25', 'S'),\n"
                                 "  (6, 'Kiara',    'Canino', DATE '2013-03-03', 'N');\n"
                                 '\n'
                                 '-- Citas (ids 1..10)\n'
                                 'INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                 'estado) VALUES\n'
                                 "  (1, 1, TIMESTAMP '2026-09-01 08:00:00', 'PROGRAMADA'),\n"
                                 "  (2, 1, TIMESTAMP '2026-09-01 09:00:00', 'ATENDIDA'),\n"
                                 "  (4, 2, TIMESTAMP '2026-09-01 10:00:00', 'PROGRAMADA'),\n"
                                 "  (5, 3, TIMESTAMP '2026-09-02 08:30:00', 'CANCELADA'),\n"
                                 "  (6, 2, TIMESTAMP '2026-09-02 11:00:00', 'ATENDIDA'),\n"
                                 "  (7, 4, TIMESTAMP '2026-09-03 07:45:00', 'PROGRAMADA'),\n"
                                 "  (1, 1, TIMESTAMP '2026-09-05 15:00:00', 'ATENDIDA'),\n"
                                 "  (2, 3, TIMESTAMP '2026-09-08 16:00:00', 'PROGRAMADA'),\n"
                                 "  (4, 4, TIMESTAMP '2026-09-10 08:00:00', 'PROGRAMADA'),\n"
                                 "  (6, 1, TIMESTAMP '2026-09-10 09:00:00', 'ATENDIDA');\n"
                                 '\n'
                                 '-- Consultas (ids 1..4) sobre las citas ATENDIDAS 2, 5, 7 y 10\n'
                                 'INSERT INTO consulta (id_cita, diagnostico, precio) VALUES\n'
                                 "  (2,  'Vacunacion triple felina', 40000),\n"
                                 "  (5,  'Control de peso',          38000),\n"
                                 "  (7,  'Otitis externa',           55000),\n"
                                 "  (10, 'Desparasitacion',          35000);\n"
                                 '\n'
                                 '-- Insumos (ids 1..6). Ojo: 2 y 5 tienen stock bajo a '
                                 'proposito.\n'
                                 'INSERT INTO insumo (nombre, stock, precio_unit) VALUES\n'
                                 "  ('Vacuna antirrabica',       12, 22000),\n"
                                 "  ('Vacuna triple felina',      3, 31000),\n"
                                 "  ('Antiparasitario oral',     40,  9500),\n"
                                 "  ('Suero fisiologico 500ml',  25,  7000),\n"
                                 "  ('Gasa esteril',              8,  1200),\n"
                                 "  ('Jeringa 5ml',              60,   900);\n"
                                 '\n'
                                 '-- Facturas (ids 1..3) y sus detalles\n'
                                 'INSERT INTO factura (id_consulta, fecha, total) VALUES\n'
                                 "  (1, TIMESTAMP '2026-09-01 09:40:00', 71000),\n"
                                 "  (2, TIMESTAMP '2026-09-02 11:35:00', 47000),\n"
                                 "  (3, TIMESTAMP '2026-09-05 15:50:00', 60200);\n"
                                 '\n'
                                 'INSERT INTO detalle_factura (id_factura, id_insumo, cantidad, '
                                 'precio_unit) VALUES\n'
                                 '  (1, 2, 1, 31000),\n'
                                 '  (1, 6, 1,   900),\n'
                                 '  (1, 3, 1,  9500),\n'
                                 '  (2, 3, 1,  9500),\n'
                                 '  (2, 4, 1,  7000),\n'
                                 '  (3, 1, 1, 22000),\n'
                                 '  (3, 5, 4,  1200),\n'
                                 '  (3, 6, 2,   900);\n',
                    'tipo': 'bd_sql'},
                   {'correctas': [1, 3, 4],
                    'enunciado': '## 2. Privilegio minimo en la matriz de VetCare\n'
                                 '\n'
                                 'La recepcionista de Huellitas solo agenda, reprograma y cancela '
                                 'citas, y consulta datos de duenos y mascotas para identificarlos '
                                 'por telefono.\n'
                                 '\n'
                                 'Selecciona **todas** las afirmaciones que respetan el principio '
                                 'de **privilegio minimo** (least privilege) para el rol '
                                 '`recepcion`.',
                    'opciones': ['Darle DELETE sobre cita es aceptable porque cancelar una cita es '
                                 'basicamente borrarla.',
                                 "Cancelar debe ser un UPDATE de estado a 'CANCELADA', no un "
                                 'DELETE: se conserva la historia y basta el privilegio UPDATE.',
                                 'Conviene darle ALL PRIVILEGES sobre cita para no tener que '
                                 'ajustar permisos cada vez que cambie el proceso.',
                                 'Sobre dueno y mascota le basta SELECT; no necesita INSERT ni '
                                 'UPDATE porque el alta de mascotas la hace otro rol.',
                                 'Si solo requiere telefono y nombre del dueno, es mejor exponerle '
                                 'una vista o privilegios por columna que la tabla dueno completa '
                                 'con email y direccion.',
                                 'El rol auditor deberia tener UPDATE sobre la tabla de auditoria '
                                 'para poder corregir registros erroneos.'],
                    'puntos': 10,
                    'rubrica': '10 puntos con las 3 opciones correctas y ninguna incorrecta; '
                               'puntaje proporcional por acierto parcial. Correctas: indices 1, 3 '
                               'y 4.',
                    'tipo': 'cerrada_multi'},
                   {'enunciado': '## 3. Reducir la superficie: vista de agenda y privilegios por '
                                 'columna\n'
                                 '\n'
                                 'Sobre el mismo esquema de VetCare (ya creado y poblado) y '
                                 '**asumiendo que los roles `recepcion`, `veterinario_rol` y '
                                 '`auditor` ya existen** (los crea el setup de esta pregunta), '
                                 'implementa dos mecanismos de privilegio minimo:\n'
                                 '\n'
                                 '1. **Vista para recepcion.** Crea `v_agenda_recepcion` que '
                                 'devuelva, para las citas **no canceladas**: `id_cita`, '
                                 '`fecha_hora`, `estado`, nombre de la mascota (`mascota`), nombre '
                                 'del dueno (`dueno`), telefono del dueno (`telefono`) y nombre '
                                 'del veterinario (`veterinario`). **No debe exponer el email del '
                                 'dueno.**\n'
                                 '   Luego:\n'
                                 '   - `GRANT SELECT` de la vista a `recepcion`.\n'
                                 '   - `REVOKE SELECT ON dueno FROM recepcion;` para que llegue al '
                                 'dato del dueno **solo** a traves de la vista.\n'
                                 '\n'
                                 '2. **Privilegios por columna para veterinario_rol.** En lugar de '
                                 'dar `SELECT` sobre toda la tabla `dueno`, otorga `SELECT` '
                                 '**unicamente** sobre las columnas `id_dueno` y `nombre` de '
                                 '`dueno`. La sintaxis es `GRANT SELECT (col1, col2) ON tabla TO '
                                 'rol;`\n'
                                 '\n'
                                 '3. **Verificacion (obligatoria).** Termina con dos consultas:\n'
                                 '   - un `SELECT` sobre la vista `v_agenda_recepcion` que muestre '
                                 'sus filas;\n'
                                 '   - un `SELECT grantee, table_name, column_name, privilege_type '
                                 'FROM information_schema.column_privileges WHERE grantee = '
                                 "'veterinario_rol' ORDER BY table_name, column_name;`",
                    'puntos': 20,
                    'rubrica': 'La vista se crea con las 7 columnas pedidas, excluye el email y '
                               'filtra las citas canceladas; el SELECT sobre la vista devuelve '
                               'filas. Se otorga SELECT de la vista a recepcion y se revoca SELECT '
                               'sobre dueno. Se usa GRANT SELECT (id_dueno, nombre) ON dueno TO '
                               'veterinario_rol y la consulta a column_privileges evidencia solo '
                               'esas dos columnas. Se descuenta si se expone el email o si se '
                               'otorga la tabla completa en vez de columnas.',
                    'setup_sql': 'CREATE TABLE dueno (\n'
                                 '  id_dueno SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  telefono TEXT,\n'
                                 '  email TEXT,\n'
                                 "  ciudad TEXT DEFAULT 'Cali'\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE mascota (\n'
                                 '  id_mascota SERIAL PRIMARY KEY,\n'
                                 '  id_dueno INT NOT NULL REFERENCES dueno(id_dueno),\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especie TEXT NOT NULL,\n'
                                 '  fecha_nac DATE,\n'
                                 "  activa CHAR(1) NOT NULL DEFAULT 'S' CHECK (activa IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE veterinario (\n'
                                 '  id_veterinario SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especialidad TEXT,\n'
                                 "  activo CHAR(1) NOT NULL DEFAULT 'S' CHECK (activo IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE cita (\n'
                                 '  id_cita SERIAL PRIMARY KEY,\n'
                                 '  id_mascota INT NOT NULL REFERENCES mascota(id_mascota),\n'
                                 '  id_veterinario INT NOT NULL REFERENCES '
                                 'veterinario(id_veterinario),\n'
                                 '  fecha_hora TIMESTAMP NOT NULL,\n'
                                 "  estado TEXT NOT NULL DEFAULT 'PROGRAMADA'\n"
                                 "    CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))\n"
                                 ');\n'
                                 '\n'
                                 '-- Duenos (ids 1..6 en este orden)\n'
                                 'INSERT INTO dueno (nombre, telefono, email) VALUES\n'
                                 "  ('Ana Gomez',      '3001112233', 'ana.gomez@mail.com'),\n"
                                 "  ('Carlos Ruiz',    '3014445566', 'carlos.ruiz@mail.com'),\n"
                                 "  ('Marcela Diaz',   '3027778899', 'marcela.diaz@mail.com'),\n"
                                 "  ('Jorge Pineda',   '3105551212', 'jorge.pineda@mail.com'),\n"
                                 "  ('Luisa Cardona',  '3123334455', 'luisa.cardona@mail.com'),\n"
                                 "  ('Andres Vallejo', '3159998877', 'andres.vallejo@mail.com');\n"
                                 '\n'
                                 '-- Veterinarios (ids 1..4)\n'
                                 'INSERT INTO veterinario (nombre, especialidad) VALUES\n'
                                 "  ('Laura Restrepo', 'General'),\n"
                                 "  ('Diego Moreno',   'Cirugia'),\n"
                                 "  ('Paula Salazar',  'Dermatologia'),\n"
                                 "  ('Ivan Ortiz',     'General');\n"
                                 '\n'
                                 '-- Mascotas (ids 1..8). Rocky (3) y Kiara (8) estan INACTIVAS.\n'
                                 'INSERT INTO mascota (id_dueno, nombre, especie, fecha_nac, '
                                 'activa) VALUES\n'
                                 "  (1, 'Firulais', 'Canino', DATE '2019-04-12', 'S'),\n"
                                 "  (1, 'Luna',     'Felino', DATE '2021-08-30', 'S'),\n"
                                 "  (2, 'Rocky',    'Canino', DATE '2015-01-20', 'N'),\n"
                                 "  (3, 'Mishi',    'Felino', DATE '2022-11-05', 'S'),\n"
                                 "  (3, 'Bobby',    'Canino', DATE '2018-06-17', 'S'),\n"
                                 "  (4, 'Nube',     'Felino', DATE '2023-02-09', 'S'),\n"
                                 "  (5, 'Toby',     'Canino', DATE '2020-09-25', 'S'),\n"
                                 "  (6, 'Kiara',    'Canino', DATE '2013-03-03', 'N');\n"
                                 '\n'
                                 '-- Citas (ids 1..10)\n'
                                 'INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                 'estado) VALUES\n'
                                 "  (1, 1, TIMESTAMP '2026-09-01 08:00:00', 'PROGRAMADA'),\n"
                                 "  (2, 1, TIMESTAMP '2026-09-01 09:00:00', 'ATENDIDA'),\n"
                                 "  (4, 2, TIMESTAMP '2026-09-01 10:00:00', 'PROGRAMADA'),\n"
                                 "  (5, 3, TIMESTAMP '2026-09-02 08:30:00', 'CANCELADA'),\n"
                                 "  (6, 2, TIMESTAMP '2026-09-02 11:00:00', 'ATENDIDA'),\n"
                                 "  (7, 4, TIMESTAMP '2026-09-03 07:45:00', 'PROGRAMADA'),\n"
                                 "  (1, 1, TIMESTAMP '2026-09-05 15:00:00', 'ATENDIDA'),\n"
                                 "  (2, 3, TIMESTAMP '2026-09-08 16:00:00', 'PROGRAMADA'),\n"
                                 "  (4, 4, TIMESTAMP '2026-09-10 08:00:00', 'PROGRAMADA'),\n"
                                 "  (6, 1, TIMESTAMP '2026-09-10 09:00:00', 'ATENDIDA');\n"
                                 '\n'
                                 '-- Roles ya definidos en la Clase 2 (pregunta 1)\n'
                                 'CREATE ROLE recepcion NOLOGIN;\n'
                                 'CREATE ROLE veterinario_rol NOLOGIN;\n'
                                 'CREATE ROLE auditor NOLOGIN;\n'
                                 '\n'
                                 'GRANT SELECT, INSERT, UPDATE ON cita TO recepcion;\n'
                                 'GRANT SELECT ON dueno, mascota, veterinario TO recepcion;\n'
                                 'GRANT SELECT ON cita, mascota TO veterinario_rol;\n'
                                 'GRANT SELECT ON dueno, mascota, cita TO auditor;\n',
                    'tipo': 'bd_sql'},
                   {'enunciado': '## 4. Matriz rol x objeto x privilegio de VetCare\n'
                                 '\n'
                                 'Entrega la **matriz de permisos completa** de VetCare DB (es el '
                                 'nucleo del documento `Roles_VetCare`). Usa una tabla markdown '
                                 'con una fila por objeto y una columna por rol, y en cada celda '
                                 'los privilegios (`S` = SELECT, `I` = INSERT, `U` = UPDATE, `D` = '
                                 'DELETE, `E` = EXECUTE, `-` = ninguno).\n'
                                 '\n'
                                 'Objetos que debes cubrir (8 tablas + 2 objetos de codigo):\n'
                                 '`dueno`, `mascota`, `veterinario`, `cita`, `consulta`, `insumo`, '
                                 '`factura`, `detalle_factura`, `sp_agendar_cita`, `sp_facturar`.\n'
                                 '\n'
                                 'Roles: `admin_bd`, `recepcion`, `veterinario_rol`, `auditor`.\n'
                                 '\n'
                                 'Debajo de la matriz, justifica en **4 a 6 lineas** tres '
                                 'decisiones concretas aplicando **privilegio minimo**, por '
                                 'ejemplo: por que ningun rol operativo tiene `DELETE`, por que '
                                 '`auditor` no tiene `INSERT` ni sobre la tabla de auditoria, y '
                                 'por que la app llegara a los datos por `EXECUTE` de '
                                 'procedimientos en vez de `INSERT` directo.',
                    'puntos': 25,
                    'rubrica': 'La matriz cubre los 10 objetos x 4 roles, sin celdas vacias, y es '
                               'internamente consistente con los GRANT de la pregunta 1. Los '
                               'procedimientos aparecen con EXECUTE, no con SELECT/INSERT. La '
                               'justificacion argumenta explicitamente privilegio minimo en al '
                               'menos 3 decisiones concretas (ausencia de DELETE, auditor de solo '
                               'lectura, acceso por EXECUTE). Se descuenta por roles con ALL '
                               'PRIVILEGES sin justificacion o por objetos omitidos.',
                    'tipo': 'abierta'},
                   {'enunciado': '## 5. Politica de altas y bajas de usuarios (y limites del '
                                 'entorno)\n'
                                 '\n'
                                 'Redacta la politica de gestion de usuarios de VetCare DB, maximo '
                                 'una pagina, con estas secciones:\n'
                                 '\n'
                                 '1. **Alta**: quien solicita, quien aprueba, que rol se asigna '
                                 'por defecto, como se entrega la credencial inicial y en cuanto '
                                 'tiempo caduca.\n'
                                 '2. **Cambio de rol**: que pasa cuando una recepcionista pasa a '
                                 'ser auxiliar veterinaria (que se otorga y, sobre todo, **que se '
                                 'revoca**).\n'
                                 '3. **Baja**: pasos al desvincular a una persona el mismo dia '
                                 '(revocar roles, deshabilitar login, que hacer con los objetos '
                                 'que era dueno, cuanto se conserva la traza de auditoria).\n'
                                 '4. **Revision periodica**: cada cuanto se audita la matriz, con '
                                 'que consulta de `information_schema` se saca la evidencia y '
                                 'quien firma.\n'
                                 '5. **Limite del entorno de practica**: explica por que en '
                                 'ExamLab (PostgreSQL en el navegador, **una sola sesion y un solo '
                                 'usuario**) pudiste crear roles y verificar la matriz con '
                                 '`information_schema`, pero **no** pudiste conectarte como '
                                 '`recepcion` y ver el error de permiso. Indica que comando de '
                                 'PostgreSQL usarias en un servidor real para hacer esa prueba '
                                 'negativa (por ejemplo `SET ROLE recepcion;` seguido de un '
                                 '`DELETE FROM cita ...` que debe fallar con *permission denied*), '
                                 'y por que la ausencia de esa prueba es una brecha de '
                                 'verificacion en tu entregable.',
                    'puntos': 15,
                    'rubrica': 'Estan las 5 secciones con responsables y tiempos concretos, no '
                               'genericos. La baja incluye revocar/deshabilitar y el destino de '
                               'los objetos, y la revision periodica nombra la consulta de '
                               'information_schema como evidencia. La seccion 5 reconoce '
                               'correctamente la limitacion de una sola sesion en PGlite y propone '
                               'SET ROLE (o conexion como otro usuario) como prueba negativa en un '
                               'servidor real.',
                    'tipo': 'abierta'}],
     'resumen': 'El estudiante crea y verifica los 4 roles de VetCare con GRANT/REVOKE reales en '
                'PostgreSQL, aplica privilegio minimo con vistas y privilegios por columna, y '
                'documenta la matriz de permisos y la politica de usuarios.',
     'titulo': 'Taller Clase 2 en ExamLab - Administracion de BD y roles de VetCare'},
 3: {'preguntas': [{'enunciado': '## 1. Implementar sp_agendar_cita en PL/pgSQL\n'
                                 '\n'
                                 'El esquema `dueno`, `mascota`, `veterinario`, `cita` ya esta '
                                 'creado y poblado. Datos que te interesan:\n'
                                 '\n'
                                 '- Mascotas: 1 Firulais (activa), 2 Luna (activa), 3 **Rocky '
                                 '(INACTIVA)**, 4 Mishi, 5 Bobby, 6 Nube, 7 Toby, 8 **Kiara '
                                 '(INACTIVA)**.\n'
                                 '- Veterinarios: 1 Laura Restrepo, 2 Diego Moreno, 3 Paula '
                                 'Salazar, 4 Ivan Ortiz.\n'
                                 '- Ya existe una cita del veterinario 1 el `2026-09-01 '
                                 '08:00:00`.\n'
                                 '\n'
                                 '**Crea el procedimiento** `sp_agendar_cita(p_id_mascota INT, '
                                 'p_id_veterinario INT, p_fecha_hora TIMESTAMP)` en **PL/pgSQL** '
                                 'que:\n'
                                 '\n'
                                 '1. Verifique que la mascota exista; si no, `RAISE EXCEPTION '
                                 "'ERROR: la mascota % no existe', p_id_mascota;`\n"
                                 "2. Verifique la **regla de negocio del PI**: si `activa <> 'S'`, "
                                 'lance `RAISE EXCEPTION` indicando que la mascota esta inactiva y '
                                 '**no** inserte nada.\n'
                                 '3. Verifique que el veterinario no tenga ya una cita **no '
                                 'cancelada** en esa misma `fecha_hora`; si la tiene, lance '
                                 'excepcion.\n'
                                 '4. Si todo esta bien, inserte en `cita` con estado '
                                 "`'PROGRAMADA'`.\n"
                                 '\n'
                                 'Despues de crear el procedimiento, **demuestra que funciona** '
                                 'ejecutando:\n'
                                 '\n'
                                 '```sql\n'
                                 "CALL sp_agendar_cita(1, 2, TIMESTAMP '2026-09-15 10:00:00');\n"
                                 'SELECT id_cita, id_mascota, id_veterinario, fecha_hora, estado\n'
                                 'FROM cita ORDER BY id_cita DESC LIMIT 3;\n'
                                 '```\n'
                                 '\n'
                                 '**Sintaxis PostgreSQL:** `CREATE PROCEDURE nombre(...) LANGUAGE '
                                 'plpgsql AS $proc$ DECLARE ... BEGIN ... END; $proc$;`. No uses '
                                 '`IS`/`AS` de Oracle, ni `VARCHAR2`, ni '
                                 '`RAISE_APPLICATION_ERROR`, ni `/` al final. Para detectar "no '
                                 'existe" usa `IF NOT FOUND THEN` despues del `SELECT ... INTO`.',
                    'puntos': 35,
                    'rubrica': 'El procedimiento se crea sin error con LANGUAGE plpgsql y '
                               'dollar-quoting, y recibe los 3 parametros con los tipos pedidos. '
                               'Implementa las 3 validaciones (mascota inexistente, mascota '
                               'inactiva, veterinario ocupado) con RAISE EXCEPTION y mensaje '
                               'informativo, e inserta con estado PROGRAMADA solo en el caso '
                               'valido. El CALL de ejemplo agrega exactamente una fila y el SELECT '
                               'final la evidencia. Cero sintaxis Oracle.',
                    'setup_sql': 'CREATE TABLE dueno (\n'
                                 '  id_dueno SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  telefono TEXT,\n'
                                 '  email TEXT,\n'
                                 "  ciudad TEXT DEFAULT 'Cali'\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE mascota (\n'
                                 '  id_mascota SERIAL PRIMARY KEY,\n'
                                 '  id_dueno INT NOT NULL REFERENCES dueno(id_dueno),\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especie TEXT NOT NULL,\n'
                                 '  fecha_nac DATE,\n'
                                 "  activa CHAR(1) NOT NULL DEFAULT 'S' CHECK (activa IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE veterinario (\n'
                                 '  id_veterinario SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especialidad TEXT,\n'
                                 "  activo CHAR(1) NOT NULL DEFAULT 'S' CHECK (activo IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE cita (\n'
                                 '  id_cita SERIAL PRIMARY KEY,\n'
                                 '  id_mascota INT NOT NULL REFERENCES mascota(id_mascota),\n'
                                 '  id_veterinario INT NOT NULL REFERENCES '
                                 'veterinario(id_veterinario),\n'
                                 '  fecha_hora TIMESTAMP NOT NULL,\n'
                                 "  estado TEXT NOT NULL DEFAULT 'PROGRAMADA'\n"
                                 "    CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))\n"
                                 ');\n'
                                 '\n'
                                 '-- Duenos (ids 1..6 en este orden)\n'
                                 'INSERT INTO dueno (nombre, telefono, email) VALUES\n'
                                 "  ('Ana Gomez',      '3001112233', 'ana.gomez@mail.com'),\n"
                                 "  ('Carlos Ruiz',    '3014445566', 'carlos.ruiz@mail.com'),\n"
                                 "  ('Marcela Diaz',   '3027778899', 'marcela.diaz@mail.com'),\n"
                                 "  ('Jorge Pineda',   '3105551212', 'jorge.pineda@mail.com'),\n"
                                 "  ('Luisa Cardona',  '3123334455', 'luisa.cardona@mail.com'),\n"
                                 "  ('Andres Vallejo', '3159998877', 'andres.vallejo@mail.com');\n"
                                 '\n'
                                 '-- Veterinarios (ids 1..4)\n'
                                 'INSERT INTO veterinario (nombre, especialidad) VALUES\n'
                                 "  ('Laura Restrepo', 'General'),\n"
                                 "  ('Diego Moreno',   'Cirugia'),\n"
                                 "  ('Paula Salazar',  'Dermatologia'),\n"
                                 "  ('Ivan Ortiz',     'General');\n"
                                 '\n'
                                 '-- Mascotas (ids 1..8). Rocky (3) y Kiara (8) estan INACTIVAS.\n'
                                 'INSERT INTO mascota (id_dueno, nombre, especie, fecha_nac, '
                                 'activa) VALUES\n'
                                 "  (1, 'Firulais', 'Canino', DATE '2019-04-12', 'S'),\n"
                                 "  (1, 'Luna',     'Felino', DATE '2021-08-30', 'S'),\n"
                                 "  (2, 'Rocky',    'Canino', DATE '2015-01-20', 'N'),\n"
                                 "  (3, 'Mishi',    'Felino', DATE '2022-11-05', 'S'),\n"
                                 "  (3, 'Bobby',    'Canino', DATE '2018-06-17', 'S'),\n"
                                 "  (4, 'Nube',     'Felino', DATE '2023-02-09', 'S'),\n"
                                 "  (5, 'Toby',     'Canino', DATE '2020-09-25', 'S'),\n"
                                 "  (6, 'Kiara',    'Canino', DATE '2013-03-03', 'N');\n"
                                 '\n'
                                 '-- Citas (ids 1..10)\n'
                                 'INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                 'estado) VALUES\n'
                                 "  (1, 1, TIMESTAMP '2026-09-01 08:00:00', 'PROGRAMADA'),\n"
                                 "  (2, 1, TIMESTAMP '2026-09-01 09:00:00', 'ATENDIDA'),\n"
                                 "  (4, 2, TIMESTAMP '2026-09-01 10:00:00', 'PROGRAMADA'),\n"
                                 "  (5, 3, TIMESTAMP '2026-09-02 08:30:00', 'CANCELADA'),\n"
                                 "  (6, 2, TIMESTAMP '2026-09-02 11:00:00', 'ATENDIDA'),\n"
                                 "  (7, 4, TIMESTAMP '2026-09-03 07:45:00', 'PROGRAMADA'),\n"
                                 "  (1, 1, TIMESTAMP '2026-09-05 15:00:00', 'ATENDIDA'),\n"
                                 "  (2, 3, TIMESTAMP '2026-09-08 16:00:00', 'PROGRAMADA'),\n"
                                 "  (4, 4, TIMESTAMP '2026-09-10 08:00:00', 'PROGRAMADA'),\n"
                                 "  (6, 1, TIMESTAMP '2026-09-10 09:00:00', 'ATENDIDA');\n",
                    'tipo': 'bd_sql'},
                   {'enunciado': '## 2. Bateria de pruebas del procedimiento (caso OK + casos de '
                                 'error)\n'
                                 '\n'
                                 'En esta base **el procedimiento `sp_agendar_cita(p_id_mascota, '
                                 'p_id_veterinario, p_fecha_hora)` ya esta creado** (version de '
                                 'referencia), junto con el esquema y los datos. Tambien existe la '
                                 'tabla:\n'
                                 '\n'
                                 '```sql\n'
                                 'resultado_prueba (id_prueba SERIAL, caso TEXT, esperado TEXT, '
                                 'obtenido TEXT, paso BOOLEAN)\n'
                                 '```\n'
                                 '\n'
                                 'Escribe **cuatro pruebas**, cada una dentro de su propio bloque '
                                 '`DO`, que capturen el resultado y lo registren en '
                                 '`resultado_prueba`. Plantilla:\n'
                                 '\n'
                                 '```sql\n'
                                 'DO $$\n'
                                 'BEGIN\n'
                                 "  CALL sp_agendar_cita(1, 2, TIMESTAMP '2026-09-20 08:00:00');\n"
                                 '  INSERT INTO resultado_prueba (caso, esperado, obtenido, paso)\n'
                                 "  VALUES ('P1 mascota activa', 'OK: cita creada', 'OK: cita "
                                 "creada', TRUE);\n"
                                 'EXCEPTION WHEN OTHERS THEN\n'
                                 '  INSERT INTO resultado_prueba (caso, esperado, obtenido, paso)\n'
                                 "  VALUES ('P1 mascota activa', 'OK: cita creada', SQLERRM, "
                                 'FALSE);\n'
                                 'END $$;\n'
                                 '```\n'
                                 '\n'
                                 'Los cuatro casos son:\n'
                                 '\n'
                                 '| Caso | Llamada | Resultado esperado |\n'
                                 '|---|---|---|\n'
                                 '| P1 | mascota 1 (Firulais, activa), vet 2, `2026-09-20 '
                                 '08:00:00` | se crea la cita |\n'
                                 '| P2 | mascota **3** (Rocky, **inactiva**), vet 2, `2026-09-21 '
                                 '08:00:00` | excepcion: mascota inactiva |\n'
                                 '| P3 | mascota **99** (no existe), vet 2, `2026-09-22 08:00:00` '
                                 '| excepcion: mascota no existe |\n'
                                 '| P4 | mascota 2 (Luna), vet **1**, `2026-09-01 08:00:00` '
                                 '(franja ya ocupada) | excepcion: veterinario ocupado |\n'
                                 '\n'
                                 'Termina con **dos consultas de cierre**:\n'
                                 '\n'
                                 '1. `SELECT caso, esperado, obtenido, paso FROM resultado_prueba '
                                 'ORDER BY id_prueba;`\n'
                                 '2. Un `SELECT COUNT(*)` sobre `cita` que demuestre que **solo se '
                                 'agrego una** cita (la de P1) y que las 3 pruebas negativas **no '
                                 'dejaron basura** en la tabla.',
                    'puntos': 25,
                    'rubrica': 'Los 4 bloques DO corren sin abortar el script y registran una fila '
                               'cada uno en resultado_prueba con el SQLERRM real en los casos '
                               'negativos. Las 3 pruebas negativas quedan con paso = FALSE por '
                               'excepcion capturada (o con la semantica claramente documentada) y '
                               'P1 con exito. El conteo final demuestra que cita paso de 10 a 11 '
                               'filas, evidenciando que las validaciones no insertaron nada. Se '
                               'descuenta si el script se cae por no capturar la excepcion.',
                    'setup_sql': 'CREATE TABLE dueno (\n'
                                 '  id_dueno SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  telefono TEXT,\n'
                                 '  email TEXT,\n'
                                 "  ciudad TEXT DEFAULT 'Cali'\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE mascota (\n'
                                 '  id_mascota SERIAL PRIMARY KEY,\n'
                                 '  id_dueno INT NOT NULL REFERENCES dueno(id_dueno),\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especie TEXT NOT NULL,\n'
                                 '  fecha_nac DATE,\n'
                                 "  activa CHAR(1) NOT NULL DEFAULT 'S' CHECK (activa IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE veterinario (\n'
                                 '  id_veterinario SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especialidad TEXT,\n'
                                 "  activo CHAR(1) NOT NULL DEFAULT 'S' CHECK (activo IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE cita (\n'
                                 '  id_cita SERIAL PRIMARY KEY,\n'
                                 '  id_mascota INT NOT NULL REFERENCES mascota(id_mascota),\n'
                                 '  id_veterinario INT NOT NULL REFERENCES '
                                 'veterinario(id_veterinario),\n'
                                 '  fecha_hora TIMESTAMP NOT NULL,\n'
                                 "  estado TEXT NOT NULL DEFAULT 'PROGRAMADA'\n"
                                 "    CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))\n"
                                 ');\n'
                                 '\n'
                                 '-- Duenos (ids 1..6 en este orden)\n'
                                 'INSERT INTO dueno (nombre, telefono, email) VALUES\n'
                                 "  ('Ana Gomez',      '3001112233', 'ana.gomez@mail.com'),\n"
                                 "  ('Carlos Ruiz',    '3014445566', 'carlos.ruiz@mail.com'),\n"
                                 "  ('Marcela Diaz',   '3027778899', 'marcela.diaz@mail.com'),\n"
                                 "  ('Jorge Pineda',   '3105551212', 'jorge.pineda@mail.com'),\n"
                                 "  ('Luisa Cardona',  '3123334455', 'luisa.cardona@mail.com'),\n"
                                 "  ('Andres Vallejo', '3159998877', 'andres.vallejo@mail.com');\n"
                                 '\n'
                                 '-- Veterinarios (ids 1..4)\n'
                                 'INSERT INTO veterinario (nombre, especialidad) VALUES\n'
                                 "  ('Laura Restrepo', 'General'),\n"
                                 "  ('Diego Moreno',   'Cirugia'),\n"
                                 "  ('Paula Salazar',  'Dermatologia'),\n"
                                 "  ('Ivan Ortiz',     'General');\n"
                                 '\n'
                                 '-- Mascotas (ids 1..8). Rocky (3) y Kiara (8) estan INACTIVAS.\n'
                                 'INSERT INTO mascota (id_dueno, nombre, especie, fecha_nac, '
                                 'activa) VALUES\n'
                                 "  (1, 'Firulais', 'Canino', DATE '2019-04-12', 'S'),\n"
                                 "  (1, 'Luna',     'Felino', DATE '2021-08-30', 'S'),\n"
                                 "  (2, 'Rocky',    'Canino', DATE '2015-01-20', 'N'),\n"
                                 "  (3, 'Mishi',    'Felino', DATE '2022-11-05', 'S'),\n"
                                 "  (3, 'Bobby',    'Canino', DATE '2018-06-17', 'S'),\n"
                                 "  (4, 'Nube',     'Felino', DATE '2023-02-09', 'S'),\n"
                                 "  (5, 'Toby',     'Canino', DATE '2020-09-25', 'S'),\n"
                                 "  (6, 'Kiara',    'Canino', DATE '2013-03-03', 'N');\n"
                                 '\n'
                                 '-- Citas (ids 1..10)\n'
                                 'INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                 'estado) VALUES\n'
                                 "  (1, 1, TIMESTAMP '2026-09-01 08:00:00', 'PROGRAMADA'),\n"
                                 "  (2, 1, TIMESTAMP '2026-09-01 09:00:00', 'ATENDIDA'),\n"
                                 "  (4, 2, TIMESTAMP '2026-09-01 10:00:00', 'PROGRAMADA'),\n"
                                 "  (5, 3, TIMESTAMP '2026-09-02 08:30:00', 'CANCELADA'),\n"
                                 "  (6, 2, TIMESTAMP '2026-09-02 11:00:00', 'ATENDIDA'),\n"
                                 "  (7, 4, TIMESTAMP '2026-09-03 07:45:00', 'PROGRAMADA'),\n"
                                 "  (1, 1, TIMESTAMP '2026-09-05 15:00:00', 'ATENDIDA'),\n"
                                 "  (2, 3, TIMESTAMP '2026-09-08 16:00:00', 'PROGRAMADA'),\n"
                                 "  (4, 4, TIMESTAMP '2026-09-10 08:00:00', 'PROGRAMADA'),\n"
                                 "  (6, 1, TIMESTAMP '2026-09-10 09:00:00', 'ATENDIDA');\n"
                                 '\n'
                                 'CREATE PROCEDURE sp_agendar_cita(\n'
                                 '  p_id_mascota     INT,\n'
                                 '  p_id_veterinario INT,\n'
                                 '  p_fecha_hora     TIMESTAMP\n'
                                 ')\n'
                                 'LANGUAGE plpgsql\n'
                                 'AS $proc$\n'
                                 'DECLARE\n'
                                 '  v_activa CHAR(1);\n'
                                 '  v_ocupado INT;\n'
                                 'BEGIN\n'
                                 '  SELECT activa INTO v_activa FROM mascota WHERE id_mascota = '
                                 'p_id_mascota;\n'
                                 '  IF NOT FOUND THEN\n'
                                 "    RAISE EXCEPTION 'ERROR: la mascota % no existe', "
                                 'p_id_mascota;\n'
                                 '  END IF;\n'
                                 "  IF v_activa <> 'S' THEN\n"
                                 "    RAISE EXCEPTION 'ERROR: la mascota % esta inactiva; no se "
                                 "agenda cita', p_id_mascota;\n"
                                 '  END IF;\n'
                                 '  SELECT COUNT(*) INTO v_ocupado\n'
                                 '  FROM cita\n'
                                 '  WHERE id_veterinario = p_id_veterinario\n'
                                 '    AND fecha_hora = p_fecha_hora\n'
                                 "    AND estado <> 'CANCELADA';\n"
                                 '  IF v_ocupado > 0 THEN\n'
                                 "    RAISE EXCEPTION 'ERROR: el veterinario % ya tiene cita en "
                                 "%', p_id_veterinario, p_fecha_hora;\n"
                                 '  END IF;\n'
                                 '  INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                 'estado)\n'
                                 '  VALUES (p_id_mascota, p_id_veterinario, p_fecha_hora, '
                                 "'PROGRAMADA');\n"
                                 'END;\n'
                                 '$proc$;\n'
                                 '\n'
                                 'CREATE TABLE resultado_prueba (\n'
                                 '  id_prueba SERIAL PRIMARY KEY,\n'
                                 '  caso TEXT NOT NULL,\n'
                                 '  esperado TEXT,\n'
                                 '  obtenido TEXT,\n'
                                 '  paso BOOLEAN\n'
                                 ');\n',
                    'tipo': 'bd_sql'},
                   {'correctas': [1],
                    'enunciado': '## 3. PROCEDURE o FUNCTION en PostgreSQL\n'
                                 '\n'
                                 'En VetCare necesitas una rutina que **calcule y devuelva** el '
                                 'precio sugerido de una consulta segun la especie de la mascota, '
                                 'para usarla directamente dentro de un `SELECT` sobre la tabla '
                                 '`consulta`.\n'
                                 '\n'
                                 'Cual es la opcion correcta en PostgreSQL?',
                    'opciones': ['Un PROCEDURE, porque en PostgreSQL los procedimientos pueden '
                                 'invocarse dentro de la lista de columnas de un SELECT.',
                                 'Un FUNCTION que devuelva NUMERIC, porque solo las funciones '
                                 'pueden usarse dentro de una consulta SELECT; los procedimientos '
                                 'se invocan con CALL como sentencia independiente.',
                                 'Un PROCEDURE con parametro OUT, porque en PostgreSQL es la unica '
                                 'forma de retornar un valor.',
                                 'Da exactamente lo mismo: en PostgreSQL PROCEDURE y FUNCTION son '
                                 'sinonimos y ambos se pueden llamar con SELECT o con CALL.',
                                 'Un FUNCTION, pero solo si se declara LANGUAGE sql; en plpgsql '
                                 'las funciones no pueden retornar valores.'],
                    'puntos': 10,
                    'rubrica': '10 puntos si marca la opcion 1 (indice 1). Cualquier otra '
                               'respuesta, 0.',
                    'tipo': 'cerrada'},
                   {'enunciado': '## 4. sp_registrar_consulta: el segundo procedimiento de '
                                 'negocio\n'
                                 '\n'
                                 'El esquema completo (incluidas `consulta`, `insumo`, `factura`, '
                                 '`detalle_factura`) ya esta creado y poblado. Recuerda: ya hay '
                                 'consultas registradas para las citas **2, 5, 7 y 10**, y la '
                                 'tabla `consulta` tiene `id_cita` con restriccion `UNIQUE`.\n'
                                 '\n'
                                 '**Crea el procedimiento** `sp_registrar_consulta(p_id_cita INT, '
                                 'p_diagnostico TEXT, p_precio NUMERIC)` en PL/pgSQL que:\n'
                                 '\n'
                                 '1. Valide que la cita exista; si no, lance excepcion.\n'
                                 "2. Valide que la cita **no** este en estado `'CANCELADA'`; una "
                                 'cita cancelada no puede generar consulta.\n'
                                 '3. Valide que esa cita **no tenga ya** una consulta registrada '
                                 '(usa `EXISTS` sobre `consulta`), lanzando una excepcion con '
                                 'mensaje claro en vez de dejar que reviente la restriccion '
                                 '`UNIQUE`.\n'
                                 '4. Valide que `p_precio > 0`.\n'
                                 '5. Inserte la consulta y, en la **misma** operacion, actualice '
                                 "el estado de la cita a `'ATENDIDA'`.\n"
                                 '\n'
                                 'Luego demuestra su comportamiento con tres llamadas, **la '
                                 'segunda y la tercera envueltas en un bloque `DO` con `EXCEPTION '
                                 "WHEN OTHERS THEN RAISE NOTICE '%', SQLERRM;`** para que el "
                                 'script no se detenga:\n'
                                 '\n'
                                 "- `CALL sp_registrar_consulta(1, 'Vacunacion anual antirrabica', "
                                 '45000);` (cita 1, PROGRAMADA -> debe funcionar)\n'
                                 "- `CALL sp_registrar_consulta(4, 'Revision', 30000);` (cita 4 "
                                 'esta CANCELADA -> debe fallar)\n'
                                 "- `CALL sp_registrar_consulta(2, 'Duplicada', 40000);` (cita 2 "
                                 'ya tiene consulta -> debe fallar)\n'
                                 '\n'
                                 'Cierra con `SELECT c.id_cita, c.estado, co.diagnostico, '
                                 'co.precio FROM cita c LEFT JOIN consulta co ON co.id_cita = '
                                 'c.id_cita ORDER BY c.id_cita;`',
                    'puntos': 15,
                    'rubrica': 'El procedimiento se crea y aplica las 4 validaciones con RAISE '
                               'EXCEPTION y mensajes propios (en particular detecta la consulta '
                               'duplicada con EXISTS antes de violar el UNIQUE). La llamada valida '
                               'inserta la consulta y deja la cita 1 en ATENDIDA; las dos '
                               'invalidas se capturan sin abortar el script y no modifican datos. '
                               'El SELECT final evidencia el estado resultante.',
                    'setup_sql': 'CREATE TABLE dueno (\n'
                                 '  id_dueno SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  telefono TEXT,\n'
                                 '  email TEXT,\n'
                                 "  ciudad TEXT DEFAULT 'Cali'\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE mascota (\n'
                                 '  id_mascota SERIAL PRIMARY KEY,\n'
                                 '  id_dueno INT NOT NULL REFERENCES dueno(id_dueno),\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especie TEXT NOT NULL,\n'
                                 '  fecha_nac DATE,\n'
                                 "  activa CHAR(1) NOT NULL DEFAULT 'S' CHECK (activa IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE veterinario (\n'
                                 '  id_veterinario SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especialidad TEXT,\n'
                                 "  activo CHAR(1) NOT NULL DEFAULT 'S' CHECK (activo IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE cita (\n'
                                 '  id_cita SERIAL PRIMARY KEY,\n'
                                 '  id_mascota INT NOT NULL REFERENCES mascota(id_mascota),\n'
                                 '  id_veterinario INT NOT NULL REFERENCES '
                                 'veterinario(id_veterinario),\n'
                                 '  fecha_hora TIMESTAMP NOT NULL,\n'
                                 "  estado TEXT NOT NULL DEFAULT 'PROGRAMADA'\n"
                                 "    CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE consulta (\n'
                                 '  id_consulta SERIAL PRIMARY KEY,\n'
                                 '  id_cita INT NOT NULL UNIQUE REFERENCES cita(id_cita),\n'
                                 '  diagnostico TEXT,\n'
                                 '  precio NUMERIC(12,2) NOT NULL CHECK (precio >= 0)\n'
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE insumo (\n'
                                 '  id_insumo SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  stock INT NOT NULL CHECK (stock >= 0),\n'
                                 '  precio_unit NUMERIC(12,2) NOT NULL\n'
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE factura (\n'
                                 '  id_factura SERIAL PRIMARY KEY,\n'
                                 '  id_consulta INT NOT NULL REFERENCES consulta(id_consulta),\n'
                                 '  fecha TIMESTAMP NOT NULL DEFAULT now(),\n'
                                 '  total NUMERIC(12,2) NOT NULL DEFAULT 0\n'
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE detalle_factura (\n'
                                 '  id_detalle SERIAL PRIMARY KEY,\n'
                                 '  id_factura INT NOT NULL REFERENCES factura(id_factura) ON '
                                 'DELETE CASCADE,\n'
                                 '  id_insumo INT NOT NULL REFERENCES insumo(id_insumo),\n'
                                 '  cantidad INT NOT NULL CHECK (cantidad > 0),\n'
                                 '  precio_unit NUMERIC(12,2) NOT NULL\n'
                                 ');\n'
                                 '\n'
                                 '-- Duenos (ids 1..6 en este orden)\n'
                                 'INSERT INTO dueno (nombre, telefono, email) VALUES\n'
                                 "  ('Ana Gomez',      '3001112233', 'ana.gomez@mail.com'),\n"
                                 "  ('Carlos Ruiz',    '3014445566', 'carlos.ruiz@mail.com'),\n"
                                 "  ('Marcela Diaz',   '3027778899', 'marcela.diaz@mail.com'),\n"
                                 "  ('Jorge Pineda',   '3105551212', 'jorge.pineda@mail.com'),\n"
                                 "  ('Luisa Cardona',  '3123334455', 'luisa.cardona@mail.com'),\n"
                                 "  ('Andres Vallejo', '3159998877', 'andres.vallejo@mail.com');\n"
                                 '\n'
                                 '-- Veterinarios (ids 1..4)\n'
                                 'INSERT INTO veterinario (nombre, especialidad) VALUES\n'
                                 "  ('Laura Restrepo', 'General'),\n"
                                 "  ('Diego Moreno',   'Cirugia'),\n"
                                 "  ('Paula Salazar',  'Dermatologia'),\n"
                                 "  ('Ivan Ortiz',     'General');\n"
                                 '\n'
                                 '-- Mascotas (ids 1..8). Rocky (3) y Kiara (8) estan INACTIVAS.\n'
                                 'INSERT INTO mascota (id_dueno, nombre, especie, fecha_nac, '
                                 'activa) VALUES\n'
                                 "  (1, 'Firulais', 'Canino', DATE '2019-04-12', 'S'),\n"
                                 "  (1, 'Luna',     'Felino', DATE '2021-08-30', 'S'),\n"
                                 "  (2, 'Rocky',    'Canino', DATE '2015-01-20', 'N'),\n"
                                 "  (3, 'Mishi',    'Felino', DATE '2022-11-05', 'S'),\n"
                                 "  (3, 'Bobby',    'Canino', DATE '2018-06-17', 'S'),\n"
                                 "  (4, 'Nube',     'Felino', DATE '2023-02-09', 'S'),\n"
                                 "  (5, 'Toby',     'Canino', DATE '2020-09-25', 'S'),\n"
                                 "  (6, 'Kiara',    'Canino', DATE '2013-03-03', 'N');\n"
                                 '\n'
                                 '-- Citas (ids 1..10)\n'
                                 'INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                 'estado) VALUES\n'
                                 "  (1, 1, TIMESTAMP '2026-09-01 08:00:00', 'PROGRAMADA'),\n"
                                 "  (2, 1, TIMESTAMP '2026-09-01 09:00:00', 'ATENDIDA'),\n"
                                 "  (4, 2, TIMESTAMP '2026-09-01 10:00:00', 'PROGRAMADA'),\n"
                                 "  (5, 3, TIMESTAMP '2026-09-02 08:30:00', 'CANCELADA'),\n"
                                 "  (6, 2, TIMESTAMP '2026-09-02 11:00:00', 'ATENDIDA'),\n"
                                 "  (7, 4, TIMESTAMP '2026-09-03 07:45:00', 'PROGRAMADA'),\n"
                                 "  (1, 1, TIMESTAMP '2026-09-05 15:00:00', 'ATENDIDA'),\n"
                                 "  (2, 3, TIMESTAMP '2026-09-08 16:00:00', 'PROGRAMADA'),\n"
                                 "  (4, 4, TIMESTAMP '2026-09-10 08:00:00', 'PROGRAMADA'),\n"
                                 "  (6, 1, TIMESTAMP '2026-09-10 09:00:00', 'ATENDIDA');\n"
                                 '\n'
                                 '-- Consultas (ids 1..4) sobre las citas ATENDIDAS 2, 5, 7 y 10\n'
                                 'INSERT INTO consulta (id_cita, diagnostico, precio) VALUES\n'
                                 "  (2,  'Vacunacion triple felina', 40000),\n"
                                 "  (5,  'Control de peso',          38000),\n"
                                 "  (7,  'Otitis externa',           55000),\n"
                                 "  (10, 'Desparasitacion',          35000);\n"
                                 '\n'
                                 '-- Insumos (ids 1..6). Ojo: 2 y 5 tienen stock bajo a '
                                 'proposito.\n'
                                 'INSERT INTO insumo (nombre, stock, precio_unit) VALUES\n'
                                 "  ('Vacuna antirrabica',       12, 22000),\n"
                                 "  ('Vacuna triple felina',      3, 31000),\n"
                                 "  ('Antiparasitario oral',     40,  9500),\n"
                                 "  ('Suero fisiologico 500ml',  25,  7000),\n"
                                 "  ('Gasa esteril',              8,  1200),\n"
                                 "  ('Jeringa 5ml',              60,   900);\n"
                                 '\n'
                                 '-- Facturas (ids 1..3) y sus detalles\n'
                                 'INSERT INTO factura (id_consulta, fecha, total) VALUES\n'
                                 "  (1, TIMESTAMP '2026-09-01 09:40:00', 71000),\n"
                                 "  (2, TIMESTAMP '2026-09-02 11:35:00', 47000),\n"
                                 "  (3, TIMESTAMP '2026-09-05 15:50:00', 60200);\n"
                                 '\n'
                                 'INSERT INTO detalle_factura (id_factura, id_insumo, cantidad, '
                                 'precio_unit) VALUES\n'
                                 '  (1, 2, 1, 31000),\n'
                                 '  (1, 6, 1,   900),\n'
                                 '  (1, 3, 1,  9500),\n'
                                 '  (2, 3, 1,  9500),\n'
                                 '  (2, 4, 1,  7000),\n'
                                 '  (3, 1, 1, 22000),\n'
                                 '  (3, 5, 4,  1200),\n'
                                 '  (3, 6, 2,   900);\n',
                    'tipo': 'bd_sql'},
                   {'enunciado': '## 5. Contrato de los procedimientos para la futura aplicacion\n'
                                 '\n'
                                 'Documenta el **contrato** de los dos procedimientos que '
                                 'construiste, tal como lo consumira la aplicacion de Huellitas. '
                                 'Para **cada** procedimiento (`sp_agendar_cita` y '
                                 '`sp_registrar_consulta`) entrega:\n'
                                 '\n'
                                 '1. **Firma exacta**: nombre y lista de parametros con tipo '
                                 'PostgreSQL y orden.\n'
                                 '2. **Como se invoca**: sentencia `CALL` de ejemplo con valores '
                                 'reales.\n'
                                 '3. **Precondiciones**: que debe ser verdadero antes de llamarlo '
                                 '(mascota activa, cita no cancelada, ...).\n'
                                 '4. **Postcondiciones**: que cambia en la base si la llamada '
                                 'tiene exito (que filas se insertan o actualizan).\n'
                                 '5. **Tabla de errores**: cada excepcion que puede lanzar, con el '
                                 '**texto del mensaje** y **que debe hacer la aplicacion** al '
                                 'recibirlo (mostrar aviso al usuario, ofrecer otra franja, '
                                 'bloquear el boton, etc.).\n'
                                 '6. **Una decision de diseno justificada** en 2 o 3 lineas: por '
                                 'que la validacion vive en la base de datos y no solo en la '
                                 'aplicacion.\n'
                                 '\n'
                                 'Cierra con una frase que fije la regla del PI: la aplicacion '
                                 '**nunca** hara `INSERT` directo sobre `cita` ni `consulta`; solo '
                                 'llamara estos procedimientos.',
                    'puntos': 15,
                    'rubrica': 'Ambos procedimientos documentados con los 6 puntos. Las firmas '
                               'coinciden exactamente con el codigo entregado en las preguntas 1 y '
                               '4 (nombres, orden y tipos). La tabla de errores lista todas las '
                               'excepciones implementadas con el mensaje real y una accion '
                               'concreta de la aplicacion para cada una. La justificacion menciona '
                               'que la regla debe valer para cualquier cliente que toque la base.',
                    'tipo': 'abierta'}],
     'resumen': 'El estudiante implementa y prueba sp_agendar_cita y sp_registrar_consulta en '
                'PL/pgSQL, con la validacion de negocio de mascota inactiva, y documenta el '
                'contrato del procedimiento para la futura aplicacion.',
     'titulo': 'Taller Clase 3 en ExamLab - Procedimientos almacenados de VetCare en PL/pgSQL'},
 4: {'preguntas': [{'enunciado': '## 1. Funcion de tarifas fn_precio_consulta\n'
                                 '\n'
                                 'El esquema completo de VetCare esta creado y poblado (mascotas, '
                                 'citas y consultas de las citas 2, 5, 7 y 10).\n'
                                 '\n'
                                 '**Crea la funcion** `fn_precio_consulta(p_especie TEXT, '
                                 'p_urgencia BOOLEAN)` que **retorne** `NUMERIC` con la tarifa '
                                 'base de Huellitas:\n'
                                 '\n'
                                 '| Especie | Tarifa base |\n'
                                 '|---|---|\n'
                                 '| Canino | 45000 |\n'
                                 '| Felino | 40000 |\n'
                                 '| cualquier otra | 35000 |\n'
                                 '\n'
                                 'Reglas adicionales:\n'
                                 '\n'
                                 '- La comparacion de especie debe ser **insensible a mayusculas** '
                                 "(`'CANINO'`, `'canino'` y `'Canino'` valen igual). Usa `UPPER()` "
                                 'o `lower()`.\n'
                                 '- Si `p_urgencia` es verdadero, la tarifa aumenta **35 %**.\n'
                                 '- Si `p_urgencia` llega `NULL`, se trata como falso (usa '
                                 '`COALESCE`).\n'
                                 '- Declara la funcion `LANGUAGE plpgsql` y marcala `IMMUTABLE` '
                                 '(solo depende de sus parametros).\n'
                                 '\n'
                                 'Luego **usala en dos consultas**:\n'
                                 '\n'
                                 '1. `SELECT nombre, especie, fn_precio_consulta(especie, FALSE) '
                                 'AS tarifa_normal, fn_precio_consulta(especie, TRUE) AS '
                                 'tarifa_urgencia FROM mascota ORDER BY id_mascota;`\n'
                                 '2. Una consulta que, para cada consulta ya registrada, compare '
                                 'el `precio` cobrado contra `fn_precio_consulta(m.especie, '
                                 'FALSE)` y muestre una columna `diferencia`, uniendo `consulta -> '
                                 'cita -> mascota`.\n'
                                 '\n'
                                 '**PostgreSQL:** `CREATE FUNCTION ... RETURNS NUMERIC LANGUAGE '
                                 'plpgsql IMMUTABLE AS $fn$ BEGIN ... RETURN ...; END; $fn$;`. No '
                                 'uses `RETURN NUMBER IS` de Oracle.',
                    'puntos': 20,
                    'rubrica': 'La funcion se crea con la firma pedida, RETURNS NUMERIC, LANGUAGE '
                               'plpgsql e IMMUTABLE. Devuelve 45000/40000/35000 correctamente, es '
                               'insensible a mayusculas, aplica el recargo del 35 % y trata NULL '
                               'como falso. Las dos consultas corren y muestran valores coherentes '
                               'con los datos (por ejemplo Firulais canino 45000 y 60750 en '
                               'urgencia). Sintaxis PostgreSQL.',
                    'setup_sql': 'CREATE TABLE dueno (\n'
                                 '  id_dueno SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  telefono TEXT,\n'
                                 '  email TEXT,\n'
                                 "  ciudad TEXT DEFAULT 'Cali'\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE mascota (\n'
                                 '  id_mascota SERIAL PRIMARY KEY,\n'
                                 '  id_dueno INT NOT NULL REFERENCES dueno(id_dueno),\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especie TEXT NOT NULL,\n'
                                 '  fecha_nac DATE,\n'
                                 "  activa CHAR(1) NOT NULL DEFAULT 'S' CHECK (activa IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE veterinario (\n'
                                 '  id_veterinario SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especialidad TEXT,\n'
                                 "  activo CHAR(1) NOT NULL DEFAULT 'S' CHECK (activo IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE cita (\n'
                                 '  id_cita SERIAL PRIMARY KEY,\n'
                                 '  id_mascota INT NOT NULL REFERENCES mascota(id_mascota),\n'
                                 '  id_veterinario INT NOT NULL REFERENCES '
                                 'veterinario(id_veterinario),\n'
                                 '  fecha_hora TIMESTAMP NOT NULL,\n'
                                 "  estado TEXT NOT NULL DEFAULT 'PROGRAMADA'\n"
                                 "    CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE consulta (\n'
                                 '  id_consulta SERIAL PRIMARY KEY,\n'
                                 '  id_cita INT NOT NULL UNIQUE REFERENCES cita(id_cita),\n'
                                 '  diagnostico TEXT,\n'
                                 '  precio NUMERIC(12,2) NOT NULL CHECK (precio >= 0)\n'
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE insumo (\n'
                                 '  id_insumo SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  stock INT NOT NULL CHECK (stock >= 0),\n'
                                 '  precio_unit NUMERIC(12,2) NOT NULL\n'
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE factura (\n'
                                 '  id_factura SERIAL PRIMARY KEY,\n'
                                 '  id_consulta INT NOT NULL REFERENCES consulta(id_consulta),\n'
                                 '  fecha TIMESTAMP NOT NULL DEFAULT now(),\n'
                                 '  total NUMERIC(12,2) NOT NULL DEFAULT 0\n'
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE detalle_factura (\n'
                                 '  id_detalle SERIAL PRIMARY KEY,\n'
                                 '  id_factura INT NOT NULL REFERENCES factura(id_factura) ON '
                                 'DELETE CASCADE,\n'
                                 '  id_insumo INT NOT NULL REFERENCES insumo(id_insumo),\n'
                                 '  cantidad INT NOT NULL CHECK (cantidad > 0),\n'
                                 '  precio_unit NUMERIC(12,2) NOT NULL\n'
                                 ');\n'
                                 '\n'
                                 '-- Duenos (ids 1..6 en este orden)\n'
                                 'INSERT INTO dueno (nombre, telefono, email) VALUES\n'
                                 "  ('Ana Gomez',      '3001112233', 'ana.gomez@mail.com'),\n"
                                 "  ('Carlos Ruiz',    '3014445566', 'carlos.ruiz@mail.com'),\n"
                                 "  ('Marcela Diaz',   '3027778899', 'marcela.diaz@mail.com'),\n"
                                 "  ('Jorge Pineda',   '3105551212', 'jorge.pineda@mail.com'),\n"
                                 "  ('Luisa Cardona',  '3123334455', 'luisa.cardona@mail.com'),\n"
                                 "  ('Andres Vallejo', '3159998877', 'andres.vallejo@mail.com');\n"
                                 '\n'
                                 '-- Veterinarios (ids 1..4)\n'
                                 'INSERT INTO veterinario (nombre, especialidad) VALUES\n'
                                 "  ('Laura Restrepo', 'General'),\n"
                                 "  ('Diego Moreno',   'Cirugia'),\n"
                                 "  ('Paula Salazar',  'Dermatologia'),\n"
                                 "  ('Ivan Ortiz',     'General');\n"
                                 '\n'
                                 '-- Mascotas (ids 1..8). Rocky (3) y Kiara (8) estan INACTIVAS.\n'
                                 'INSERT INTO mascota (id_dueno, nombre, especie, fecha_nac, '
                                 'activa) VALUES\n'
                                 "  (1, 'Firulais', 'Canino', DATE '2019-04-12', 'S'),\n"
                                 "  (1, 'Luna',     'Felino', DATE '2021-08-30', 'S'),\n"
                                 "  (2, 'Rocky',    'Canino', DATE '2015-01-20', 'N'),\n"
                                 "  (3, 'Mishi',    'Felino', DATE '2022-11-05', 'S'),\n"
                                 "  (3, 'Bobby',    'Canino', DATE '2018-06-17', 'S'),\n"
                                 "  (4, 'Nube',     'Felino', DATE '2023-02-09', 'S'),\n"
                                 "  (5, 'Toby',     'Canino', DATE '2020-09-25', 'S'),\n"
                                 "  (6, 'Kiara',    'Canino', DATE '2013-03-03', 'N');\n"
                                 '\n'
                                 '-- Citas (ids 1..10)\n'
                                 'INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                 'estado) VALUES\n'
                                 "  (1, 1, TIMESTAMP '2026-09-01 08:00:00', 'PROGRAMADA'),\n"
                                 "  (2, 1, TIMESTAMP '2026-09-01 09:00:00', 'ATENDIDA'),\n"
                                 "  (4, 2, TIMESTAMP '2026-09-01 10:00:00', 'PROGRAMADA'),\n"
                                 "  (5, 3, TIMESTAMP '2026-09-02 08:30:00', 'CANCELADA'),\n"
                                 "  (6, 2, TIMESTAMP '2026-09-02 11:00:00', 'ATENDIDA'),\n"
                                 "  (7, 4, TIMESTAMP '2026-09-03 07:45:00', 'PROGRAMADA'),\n"
                                 "  (1, 1, TIMESTAMP '2026-09-05 15:00:00', 'ATENDIDA'),\n"
                                 "  (2, 3, TIMESTAMP '2026-09-08 16:00:00', 'PROGRAMADA'),\n"
                                 "  (4, 4, TIMESTAMP '2026-09-10 08:00:00', 'PROGRAMADA'),\n"
                                 "  (6, 1, TIMESTAMP '2026-09-10 09:00:00', 'ATENDIDA');\n"
                                 '\n'
                                 '-- Consultas (ids 1..4) sobre las citas ATENDIDAS 2, 5, 7 y 10\n'
                                 'INSERT INTO consulta (id_cita, diagnostico, precio) VALUES\n'
                                 "  (2,  'Vacunacion triple felina', 40000),\n"
                                 "  (5,  'Control de peso',          38000),\n"
                                 "  (7,  'Otitis externa',           55000),\n"
                                 "  (10, 'Desparasitacion',          35000);\n"
                                 '\n'
                                 '-- Insumos (ids 1..6). Ojo: 2 y 5 tienen stock bajo a '
                                 'proposito.\n'
                                 'INSERT INTO insumo (nombre, stock, precio_unit) VALUES\n'
                                 "  ('Vacuna antirrabica',       12, 22000),\n"
                                 "  ('Vacuna triple felina',      3, 31000),\n"
                                 "  ('Antiparasitario oral',     40,  9500),\n"
                                 "  ('Suero fisiologico 500ml',  25,  7000),\n"
                                 "  ('Gasa esteril',              8,  1200),\n"
                                 "  ('Jeringa 5ml',              60,   900);\n"
                                 '\n'
                                 '-- Facturas (ids 1..3) y sus detalles\n'
                                 'INSERT INTO factura (id_consulta, fecha, total) VALUES\n'
                                 "  (1, TIMESTAMP '2026-09-01 09:40:00', 71000),\n"
                                 "  (2, TIMESTAMP '2026-09-02 11:35:00', 47000),\n"
                                 "  (3, TIMESTAMP '2026-09-05 15:50:00', 60200);\n"
                                 '\n'
                                 'INSERT INTO detalle_factura (id_factura, id_insumo, cantidad, '
                                 'precio_unit) VALUES\n'
                                 '  (1, 2, 1, 31000),\n'
                                 '  (1, 6, 1,   900),\n'
                                 '  (1, 3, 1,  9500),\n'
                                 '  (2, 3, 1,  9500),\n'
                                 '  (2, 4, 1,  7000),\n'
                                 '  (3, 1, 1, 22000),\n'
                                 '  (3, 5, 4,  1200),\n'
                                 '  (3, 6, 2,   900);\n',
                    'tipo': 'bd_sql'},
                   {'enunciado': '## 2. Trigger de auditoria de cambios de estado de cita\n'
                                 '\n'
                                 'Regla de negocio del PI: **todo cambio sensible queda '
                                 'auditado**. Aqui la implementas para el estado de las citas.\n'
                                 '\n'
                                 'El esquema y los datos estan creados (10 citas). Escribe el SQL '
                                 'que:\n'
                                 '\n'
                                 '1. Cree la tabla `audit_cita` con: `id_audit` autonumerico PK, '
                                 '`id_cita` INT no nulo, `accion` TEXT no nulo, `valor_anterior` '
                                 'TEXT, `valor_nuevo` TEXT, `usuario_bd` TEXT con `DEFAULT '
                                 'current_user`, `fecha_evento` TIMESTAMP con `DEFAULT now()`.\n'
                                 '2. Cree la **funcion de trigger** `fn_trg_audit_cita()` que '
                                 '`RETURNS TRIGGER` e inserte en `audit_cita` el `NEW.id_cita`, la '
                                 "accion `'CAMBIO_ESTADO'`, `OLD.estado` y `NEW.estado`.\n"
                                 '3. Cree el trigger `trg_audit_cita` **AFTER UPDATE OF estado ON '
                                 'cita FOR EACH ROW**, con la clausula `WHEN (OLD.estado IS '
                                 'DISTINCT FROM NEW.estado)` para no auditar actualizaciones que '
                                 'no cambian nada.\n'
                                 '4. **Prueba el trigger** con estas tres sentencias, en este '
                                 'orden:\n'
                                 "   - `UPDATE cita SET estado = 'CANCELADA' WHERE id_cita = 1;`\n"
                                 "   - `UPDATE cita SET estado = 'ATENDIDA' WHERE id_cita = 3;`\n"
                                 "   - `UPDATE cita SET estado = 'PROGRAMADA' WHERE id_cita = 6;`  "
                                 '(la cita 6 **ya** esta PROGRAMADA)\n'
                                 '5. Cierre con `SELECT id_audit, id_cita, accion, valor_anterior, '
                                 'valor_nuevo, usuario_bd FROM audit_cita ORDER BY id_audit;`\n'
                                 '\n'
                                 '**Debe quedar demostrado que se registran 2 filas, no 3**: el '
                                 'tercer `UPDATE` no cambia el estado y la clausula `WHEN` lo '
                                 'filtra.\n'
                                 '\n'
                                 '**PostgreSQL:** la funcion va aparte del trigger y el trigger se '
                                 'declara con `EXECUTE FUNCTION`, no con el bloque `BEGIN ... END` '
                                 'inline de Oracle. En un trigger `AFTER` puedes retornar `NULL`.',
                    'puntos': 20,
                    'rubrica': 'audit_cita se crea con las 7 columnas y los DEFAULT de '
                               'current_user y now(). La funcion RETURNS TRIGGER inserta '
                               'OLD.estado y NEW.estado, y el trigger es AFTER UPDATE OF estado '
                               'FOR EACH ROW con la clausula WHEN (OLD.estado IS DISTINCT FROM '
                               'NEW.estado). El SELECT final muestra exactamente 2 filas (citas 1 '
                               'y 3) y el estudiante evidencia por que la tercera no se audito. Se '
                               'descuenta por usar :NEW / :OLD de Oracle o por omitir EXECUTE '
                               'FUNCTION.',
                    'setup_sql': 'CREATE TABLE dueno (\n'
                                 '  id_dueno SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  telefono TEXT,\n'
                                 '  email TEXT,\n'
                                 "  ciudad TEXT DEFAULT 'Cali'\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE mascota (\n'
                                 '  id_mascota SERIAL PRIMARY KEY,\n'
                                 '  id_dueno INT NOT NULL REFERENCES dueno(id_dueno),\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especie TEXT NOT NULL,\n'
                                 '  fecha_nac DATE,\n'
                                 "  activa CHAR(1) NOT NULL DEFAULT 'S' CHECK (activa IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE veterinario (\n'
                                 '  id_veterinario SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especialidad TEXT,\n'
                                 "  activo CHAR(1) NOT NULL DEFAULT 'S' CHECK (activo IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE cita (\n'
                                 '  id_cita SERIAL PRIMARY KEY,\n'
                                 '  id_mascota INT NOT NULL REFERENCES mascota(id_mascota),\n'
                                 '  id_veterinario INT NOT NULL REFERENCES '
                                 'veterinario(id_veterinario),\n'
                                 '  fecha_hora TIMESTAMP NOT NULL,\n'
                                 "  estado TEXT NOT NULL DEFAULT 'PROGRAMADA'\n"
                                 "    CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))\n"
                                 ');\n'
                                 '\n'
                                 '-- Duenos (ids 1..6 en este orden)\n'
                                 'INSERT INTO dueno (nombre, telefono, email) VALUES\n'
                                 "  ('Ana Gomez',      '3001112233', 'ana.gomez@mail.com'),\n"
                                 "  ('Carlos Ruiz',    '3014445566', 'carlos.ruiz@mail.com'),\n"
                                 "  ('Marcela Diaz',   '3027778899', 'marcela.diaz@mail.com'),\n"
                                 "  ('Jorge Pineda',   '3105551212', 'jorge.pineda@mail.com'),\n"
                                 "  ('Luisa Cardona',  '3123334455', 'luisa.cardona@mail.com'),\n"
                                 "  ('Andres Vallejo', '3159998877', 'andres.vallejo@mail.com');\n"
                                 '\n'
                                 '-- Veterinarios (ids 1..4)\n'
                                 'INSERT INTO veterinario (nombre, especialidad) VALUES\n'
                                 "  ('Laura Restrepo', 'General'),\n"
                                 "  ('Diego Moreno',   'Cirugia'),\n"
                                 "  ('Paula Salazar',  'Dermatologia'),\n"
                                 "  ('Ivan Ortiz',     'General');\n"
                                 '\n'
                                 '-- Mascotas (ids 1..8). Rocky (3) y Kiara (8) estan INACTIVAS.\n'
                                 'INSERT INTO mascota (id_dueno, nombre, especie, fecha_nac, '
                                 'activa) VALUES\n'
                                 "  (1, 'Firulais', 'Canino', DATE '2019-04-12', 'S'),\n"
                                 "  (1, 'Luna',     'Felino', DATE '2021-08-30', 'S'),\n"
                                 "  (2, 'Rocky',    'Canino', DATE '2015-01-20', 'N'),\n"
                                 "  (3, 'Mishi',    'Felino', DATE '2022-11-05', 'S'),\n"
                                 "  (3, 'Bobby',    'Canino', DATE '2018-06-17', 'S'),\n"
                                 "  (4, 'Nube',     'Felino', DATE '2023-02-09', 'S'),\n"
                                 "  (5, 'Toby',     'Canino', DATE '2020-09-25', 'S'),\n"
                                 "  (6, 'Kiara',    'Canino', DATE '2013-03-03', 'N');\n"
                                 '\n'
                                 '-- Citas (ids 1..10)\n'
                                 'INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                 'estado) VALUES\n'
                                 "  (1, 1, TIMESTAMP '2026-09-01 08:00:00', 'PROGRAMADA'),\n"
                                 "  (2, 1, TIMESTAMP '2026-09-01 09:00:00', 'ATENDIDA'),\n"
                                 "  (4, 2, TIMESTAMP '2026-09-01 10:00:00', 'PROGRAMADA'),\n"
                                 "  (5, 3, TIMESTAMP '2026-09-02 08:30:00', 'CANCELADA'),\n"
                                 "  (6, 2, TIMESTAMP '2026-09-02 11:00:00', 'ATENDIDA'),\n"
                                 "  (7, 4, TIMESTAMP '2026-09-03 07:45:00', 'PROGRAMADA'),\n"
                                 "  (1, 1, TIMESTAMP '2026-09-05 15:00:00', 'ATENDIDA'),\n"
                                 "  (2, 3, TIMESTAMP '2026-09-08 16:00:00', 'PROGRAMADA'),\n"
                                 "  (4, 4, TIMESTAMP '2026-09-10 08:00:00', 'PROGRAMADA'),\n"
                                 "  (6, 1, TIMESTAMP '2026-09-10 09:00:00', 'ATENDIDA');\n",
                    'tipo': 'bd_sql'},
                   {'enunciado': '## 3. Trigger que impide stock negativo\n'
                                 '\n'
                                 'Regla de negocio del PI: **el stock de un insumo nunca queda '
                                 'negativo**.\n'
                                 '\n'
                                 'En esta base la tabla `insumo` fue creada **a proposito sin** '
                                 '`CHECK (stock >= 0)`, para que puedas ver el problema y '
                                 'resolverlo con un trigger. Insumos disponibles:\n'
                                 '\n'
                                 '| id | nombre | stock |\n'
                                 '|---|---|---|\n'
                                 '| 1 | Vacuna antirrabica | 12 |\n'
                                 '| 2 | Vacuna triple felina | 3 |\n'
                                 '| 3 | Antiparasitario oral | 40 |\n'
                                 '| 4 | Suero fisiologico 500ml | 25 |\n'
                                 '| 5 | Gasa esteril | 8 |\n'
                                 '| 6 | Jeringa 5ml | 60 |\n'
                                 '\n'
                                 'Escribe el SQL que:\n'
                                 '\n'
                                 '1. **Evidencie el problema**: ejecuta `UPDATE insumo SET stock = '
                                 'stock - 10 WHERE id_insumo = 2;` y muestra con un `SELECT` que '
                                 'el stock quedo en **-7**. Luego devuelvelo a 3 con otro '
                                 '`UPDATE`.\n'
                                 '2. Cree la funcion `fn_trg_stock_no_negativo()` que `RETURNS '
                                 "TRIGGER` y, si `NEW.stock < 0`, lance `RAISE EXCEPTION 'ERROR: "
                                 "el stock de % no puede quedar negativo (resultado: %)', "
                                 'OLD.nombre, NEW.stock;`. Si esta bien, `RETURN NEW`.\n'
                                 '3. Cree el trigger `trg_stock_no_negativo` **BEFORE UPDATE OF '
                                 'stock ON insumo FOR EACH ROW**.\n'
                                 '4. **Pruebe el trigger** con dos bloques `DO` que capturen la '
                                 "excepcion (`EXCEPTION WHEN OTHERS THEN RAISE NOTICE '%', "
                                 'SQLERRM;`):\n'
                                 '   - intento invalido: descontar 10 unidades del insumo 2 (solo '
                                 'hay 3) -> debe fallar;\n'
                                 '   - intento valido: descontar 2 unidades del insumo 2 -> debe '
                                 'pasar y dejar stock 1.\n'
                                 '5. Cierre con `SELECT id_insumo, nombre, stock FROM insumo ORDER '
                                 'BY id_insumo;` demostrando que ningun stock quedo negativo.',
                    'puntos': 20,
                    'rubrica': 'Se evidencia primero el stock negativo (-7) y se restaura el dato. '
                               'La funcion RETURNS TRIGGER valida NEW.stock < 0 con RAISE '
                               'EXCEPTION y retorna NEW en el caso valido; el trigger es BEFORE '
                               'UPDATE OF stock FOR EACH ROW. Las dos pruebas quedan capturadas '
                               'sin abortar el script y el estado final muestra el insumo 2 en '
                               'stock 1 y ningun valor negativo. Se penaliza usar AFTER (no impide '
                               'el cambio) o RAISE_APPLICATION_ERROR.',
                    'setup_sql': 'CREATE TABLE dueno (\n'
                                 '  id_dueno SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  telefono TEXT,\n'
                                 '  email TEXT,\n'
                                 "  ciudad TEXT DEFAULT 'Cali'\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE mascota (\n'
                                 '  id_mascota SERIAL PRIMARY KEY,\n'
                                 '  id_dueno INT NOT NULL REFERENCES dueno(id_dueno),\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especie TEXT NOT NULL,\n'
                                 '  fecha_nac DATE,\n'
                                 "  activa CHAR(1) NOT NULL DEFAULT 'S' CHECK (activa IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE veterinario (\n'
                                 '  id_veterinario SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especialidad TEXT,\n'
                                 "  activo CHAR(1) NOT NULL DEFAULT 'S' CHECK (activo IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE cita (\n'
                                 '  id_cita SERIAL PRIMARY KEY,\n'
                                 '  id_mascota INT NOT NULL REFERENCES mascota(id_mascota),\n'
                                 '  id_veterinario INT NOT NULL REFERENCES '
                                 'veterinario(id_veterinario),\n'
                                 '  fecha_hora TIMESTAMP NOT NULL,\n'
                                 "  estado TEXT NOT NULL DEFAULT 'PROGRAMADA'\n"
                                 "    CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE insumo (\n'
                                 '  id_insumo SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  stock INT NOT NULL,\n'
                                 '  precio_unit NUMERIC(12,2) NOT NULL\n'
                                 ');\n'
                                 '\n'
                                 '-- Duenos (ids 1..6 en este orden)\n'
                                 'INSERT INTO dueno (nombre, telefono, email) VALUES\n'
                                 "  ('Ana Gomez',      '3001112233', 'ana.gomez@mail.com'),\n"
                                 "  ('Carlos Ruiz',    '3014445566', 'carlos.ruiz@mail.com'),\n"
                                 "  ('Marcela Diaz',   '3027778899', 'marcela.diaz@mail.com'),\n"
                                 "  ('Jorge Pineda',   '3105551212', 'jorge.pineda@mail.com'),\n"
                                 "  ('Luisa Cardona',  '3123334455', 'luisa.cardona@mail.com'),\n"
                                 "  ('Andres Vallejo', '3159998877', 'andres.vallejo@mail.com');\n"
                                 '\n'
                                 '-- Veterinarios (ids 1..4)\n'
                                 'INSERT INTO veterinario (nombre, especialidad) VALUES\n'
                                 "  ('Laura Restrepo', 'General'),\n"
                                 "  ('Diego Moreno',   'Cirugia'),\n"
                                 "  ('Paula Salazar',  'Dermatologia'),\n"
                                 "  ('Ivan Ortiz',     'General');\n"
                                 '\n'
                                 '-- Mascotas (ids 1..8). Rocky (3) y Kiara (8) estan INACTIVAS.\n'
                                 'INSERT INTO mascota (id_dueno, nombre, especie, fecha_nac, '
                                 'activa) VALUES\n'
                                 "  (1, 'Firulais', 'Canino', DATE '2019-04-12', 'S'),\n"
                                 "  (1, 'Luna',     'Felino', DATE '2021-08-30', 'S'),\n"
                                 "  (2, 'Rocky',    'Canino', DATE '2015-01-20', 'N'),\n"
                                 "  (3, 'Mishi',    'Felino', DATE '2022-11-05', 'S'),\n"
                                 "  (3, 'Bobby',    'Canino', DATE '2018-06-17', 'S'),\n"
                                 "  (4, 'Nube',     'Felino', DATE '2023-02-09', 'S'),\n"
                                 "  (5, 'Toby',     'Canino', DATE '2020-09-25', 'S'),\n"
                                 "  (6, 'Kiara',    'Canino', DATE '2013-03-03', 'N');\n"
                                 '\n'
                                 '-- Citas (ids 1..10)\n'
                                 'INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                 'estado) VALUES\n'
                                 "  (1, 1, TIMESTAMP '2026-09-01 08:00:00', 'PROGRAMADA'),\n"
                                 "  (2, 1, TIMESTAMP '2026-09-01 09:00:00', 'ATENDIDA'),\n"
                                 "  (4, 2, TIMESTAMP '2026-09-01 10:00:00', 'PROGRAMADA'),\n"
                                 "  (5, 3, TIMESTAMP '2026-09-02 08:30:00', 'CANCELADA'),\n"
                                 "  (6, 2, TIMESTAMP '2026-09-02 11:00:00', 'ATENDIDA'),\n"
                                 "  (7, 4, TIMESTAMP '2026-09-03 07:45:00', 'PROGRAMADA'),\n"
                                 "  (1, 1, TIMESTAMP '2026-09-05 15:00:00', 'ATENDIDA'),\n"
                                 "  (2, 3, TIMESTAMP '2026-09-08 16:00:00', 'PROGRAMADA'),\n"
                                 "  (4, 4, TIMESTAMP '2026-09-10 08:00:00', 'PROGRAMADA'),\n"
                                 "  (6, 1, TIMESTAMP '2026-09-10 09:00:00', 'ATENDIDA');\n"
                                 '\n'
                                 'INSERT INTO insumo (nombre, stock, precio_unit) VALUES\n'
                                 "  ('Vacuna antirrabica',       12, 22000),\n"
                                 "  ('Vacuna triple felina',      3, 31000),\n"
                                 "  ('Antiparasitario oral',     40,  9500),\n"
                                 "  ('Suero fisiologico 500ml',  25,  7000),\n"
                                 "  ('Gasa esteril',              8,  1200),\n"
                                 "  ('Jeringa 5ml',              60,   900);\n",
                    'tipo': 'bd_sql'},
                   {'correctas': [0, 2, 4, 5],
                    'enunciado': '## 4. Donde vive cada validacion: CHECK, trigger o aplicacion\n'
                                 '\n'
                                 'Con base en lo que acabas de implementar, selecciona **todas** '
                                 'las afirmaciones correctas sobre donde conviene poner cada '
                                 'validacion en VetCare DB.',
                    'opciones': ['Si la regla depende solo de columnas de la propia fila, como '
                                 'stock >= 0, un CHECK es preferible al trigger: es declarativo, '
                                 'mas barato y no se puede olvidar.',
                                 'Un trigger AFTER UPDATE puede impedir que un UPDATE deje datos '
                                 'invalidos, igual que un BEFORE UPDATE.',
                                 'Registrar la historia de cambios de estado de una cita requiere '
                                 'trigger o codigo: ninguna restriccion declarativa guarda el '
                                 'valor anterior.',
                                 'Validar solo en la aplicacion es suficiente si quien desarrolla '
                                 'se compromete a no tocar la base con SQL directo.',
                                 'Poner la validacion en la base protege tambien a cargas masivas, '
                                 'scripts de mantenimiento y a cualquier otra aplicacion que se '
                                 'conecte despues.',
                                 'Abusar de triggers dificulta depurar: efectos ocultos, orden de '
                                 'ejecucion no evidente y costo por fila en operaciones masivas.'],
                    'puntos': 15,
                    'rubrica': '15 puntos con las 4 opciones correctas y ninguna incorrecta; '
                               'puntaje proporcional por acierto parcial. Correctas: indices 0, 2, '
                               '4 y 5.',
                    'tipo': 'cerrada_multi'},
                   {'enunciado': '## 5. Plan de respaldo de VetCare DB\n'
                                 '\n'
                                 'Redacta `Plan_Backup_VetCare` (una pagina) para la clinica '
                                 'Huellitas, asumiendo PostgreSQL y una clinica que atiende de '
                                 'lunes a sabado, 7:00 a 19:00. Debe incluir:\n'
                                 '\n'
                                 '1. **Que se respalda**: esquema (DDL), datos, '
                                 'procedimientos/funciones/triggers y scripts de migracion. Indica '
                                 'que herramienta usarias para cada cosa (por ejemplo `pg_dump` '
                                 'logico completo, `pg_dumpall` de roles, copia fisica).\n'
                                 '2. **Frecuencia y ventana**: cuando corre cada respaldo y por '
                                 'que a esa hora (relaciona con el horario de atencion).\n'
                                 '3. **Retencion**: cuantos dias/semanas/meses se guarda cada '
                                 'tipo, y donde (al menos dos ubicaciones distintas).\n'
                                 '4. **RPO y RTO objetivo**: cuanta informacion aceptas perder '
                                 'como maximo y en cuanto tiempo debes estar operando de nuevo. '
                                 'Justificalo con el impacto para la clinica.\n'
                                 '5. **Restore de prueba**: procedimiento concreto para verificar '
                                 'que el respaldo sirve, con **una consulta de validacion '
                                 'post-restauracion** (por ejemplo comparar `COUNT(*)` de `cita`, '
                                 '`consulta` y `factura` y el `MAX(fecha_hora)` contra los valores '
                                 'esperados). Indica cada cuanto se ensaya y quien firma la '
                                 'evidencia.\n'
                                 '6. **Que NO cubre este plan** y un riesgo residual asumido.\n'
                                 '\n'
                                 'Cierra actualizando el **checklist del PI**: marca como "en '
                                 'progreso" o "listo" los items de seguridad y respaldo y di que '
                                 'falta.',
                    'puntos': 25,
                    'rubrica': 'Las 6 secciones estan presentes con decisiones concretas y numeros '
                               '(frecuencias, dias de retencion, RPO/RTO justificados), no '
                               'formulas genericas. Se nombran herramientas reales de PostgreSQL, '
                               'no de Oracle. La seccion 5 incluye al menos una consulta de '
                               'validacion post-restore verificable y una periodicidad de ensayo. '
                               'Se cierra con el estado del checklist del PI y el gap pendiente.',
                    'tipo': 'abierta'}],
     'resumen': 'El estudiante entrega una funcion de tarifas, un trigger de auditoria de cambios '
                'de estado de cita, un trigger que impide stock negativo y el plan de respaldo de '
                'VetCare DB.',
     'titulo': 'Taller Clase 4 en ExamLab - Funciones, triggers y plan de respaldo de VetCare'},
 6: {'preguntas': [{'enunciado': '## 1. Reescribir la consulta de agenda del dia\n'
                                 '\n'
                                 'Esta base tiene **volumen real**: 2.006 duenos, 5.008 mascotas, '
                                 '16 veterinarios y **30.010 citas** repartidas entre el '
                                 '2026-01-05 y el 2026-07-23 (unas 150 citas por dia). Las '
                                 'estadisticas ya estan actualizadas con `ANALYZE` y **no hay '
                                 'ningun indice** mas alla de las llaves primarias.\n'
                                 '\n'
                                 'La recepcion de Huellitas usa esta consulta para imprimir la '
                                 'agenda del dia. Es la version **ANTES**, tal como la escribio '
                                 'quien la programo:\n'
                                 '\n'
                                 '```sql\n'
                                 'SELECT *\n'
                                 'FROM cita c, mascota m, dueno d, veterinario v\n'
                                 'WHERE c.id_mascota = m.id_mascota\n'
                                 '  AND m.id_dueno = d.id_dueno\n'
                                 '  AND c.id_veterinario = v.id_veterinario\n'
                                 "  AND to_char(c.fecha_hora, 'YYYY-MM-DD') = '2026-03-10'\n"
                                 "  AND UPPER(c.estado) = 'PROGRAMADA';\n"
                                 '```\n'
                                 '\n'
                                 '**Tu trabajo:**\n'
                                 '\n'
                                 '1. Ejecuta la consulta ANTES tal como esta (para tener la linea '
                                 'base).\n'
                                 '2. Escribe la version **DESPUES** que devuelva **la misma '
                                 'informacion util** pero corrigiendo, como minimo, estos **cuatro '
                                 'antipatrones**:\n'
                                 '   - `SELECT *` -> proyecta solo `c.id_cita`, `c.fecha_hora`, '
                                 '`m.nombre AS mascota`, `d.nombre AS dueno`, `v.nombre AS '
                                 'veterinario`, `c.estado`;\n'
                                 '   - joins implicitos con comas -> `JOIN ... ON` explicitos;\n'
                                 "   - `to_char(c.fecha_hora, ...) = '2026-03-10'` -> **predicado "
                                 "de rango** sobre la columna (`>= TIMESTAMP '2026-03-10 00:00:00' "
                                 "AND < TIMESTAMP '2026-03-11 00:00:00'`), para que la columna "
                                 'quede *sargable*;\n'
                                 "   - `UPPER(c.estado) = 'PROGRAMADA'` -> comparacion directa "
                                 "`c.estado = 'PROGRAMADA'` (el dominio ya esta normalizado por el "
                                 '`CHECK`).\n'
                                 '   Ordena por `c.fecha_hora`.\n'
                                 '3. Verifica con un `SELECT COUNT(*)` de cada version que **ambas '
                                 'devuelven el mismo numero de filas**. Si no coinciden, corrige '
                                 'la version DESPUES: optimizar no puede cambiar el resultado.',
                    'puntos': 30,
                    'rubrica': 'La version DESPUES corrige los 4 antipatrones exigidos '
                               '(proyeccion, JOIN explicito, predicado de rango sargable y '
                               'comparacion directa de estado) y ordena por fecha_hora. Los dos '
                               'COUNT(*) coinciden, demostrando equivalencia de resultado. Se '
                               'descuenta si queda SELECT *, si persiste una funcion sobre '
                               'fecha_hora en el WHERE o si el conteo difiere del de la version '
                               'ANTES.',
                    'setup_sql': 'CREATE TABLE dueno (\n'
                                 '  id_dueno SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  telefono TEXT,\n'
                                 '  email TEXT,\n'
                                 "  ciudad TEXT DEFAULT 'Cali'\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE mascota (\n'
                                 '  id_mascota SERIAL PRIMARY KEY,\n'
                                 '  id_dueno INT NOT NULL REFERENCES dueno(id_dueno),\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especie TEXT NOT NULL,\n'
                                 '  fecha_nac DATE,\n'
                                 "  activa CHAR(1) NOT NULL DEFAULT 'S' CHECK (activa IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE veterinario (\n'
                                 '  id_veterinario SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especialidad TEXT,\n'
                                 "  activo CHAR(1) NOT NULL DEFAULT 'S' CHECK (activo IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE cita (\n'
                                 '  id_cita SERIAL PRIMARY KEY,\n'
                                 '  id_mascota INT NOT NULL REFERENCES mascota(id_mascota),\n'
                                 '  id_veterinario INT NOT NULL REFERENCES '
                                 'veterinario(id_veterinario),\n'
                                 '  fecha_hora TIMESTAMP NOT NULL,\n'
                                 "  estado TEXT NOT NULL DEFAULT 'PROGRAMADA'\n"
                                 "    CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))\n"
                                 ');\n'
                                 '\n'
                                 '-- Duenos (ids 1..6 en este orden)\n'
                                 'INSERT INTO dueno (nombre, telefono, email) VALUES\n'
                                 "  ('Ana Gomez',      '3001112233', 'ana.gomez@mail.com'),\n"
                                 "  ('Carlos Ruiz',    '3014445566', 'carlos.ruiz@mail.com'),\n"
                                 "  ('Marcela Diaz',   '3027778899', 'marcela.diaz@mail.com'),\n"
                                 "  ('Jorge Pineda',   '3105551212', 'jorge.pineda@mail.com'),\n"
                                 "  ('Luisa Cardona',  '3123334455', 'luisa.cardona@mail.com'),\n"
                                 "  ('Andres Vallejo', '3159998877', 'andres.vallejo@mail.com');\n"
                                 '\n'
                                 '-- Veterinarios (ids 1..4)\n'
                                 'INSERT INTO veterinario (nombre, especialidad) VALUES\n'
                                 "  ('Laura Restrepo', 'General'),\n"
                                 "  ('Diego Moreno',   'Cirugia'),\n"
                                 "  ('Paula Salazar',  'Dermatologia'),\n"
                                 "  ('Ivan Ortiz',     'General');\n"
                                 '\n'
                                 '-- Mascotas (ids 1..8). Rocky (3) y Kiara (8) estan INACTIVAS.\n'
                                 'INSERT INTO mascota (id_dueno, nombre, especie, fecha_nac, '
                                 'activa) VALUES\n'
                                 "  (1, 'Firulais', 'Canino', DATE '2019-04-12', 'S'),\n"
                                 "  (1, 'Luna',     'Felino', DATE '2021-08-30', 'S'),\n"
                                 "  (2, 'Rocky',    'Canino', DATE '2015-01-20', 'N'),\n"
                                 "  (3, 'Mishi',    'Felino', DATE '2022-11-05', 'S'),\n"
                                 "  (3, 'Bobby',    'Canino', DATE '2018-06-17', 'S'),\n"
                                 "  (4, 'Nube',     'Felino', DATE '2023-02-09', 'S'),\n"
                                 "  (5, 'Toby',     'Canino', DATE '2020-09-25', 'S'),\n"
                                 "  (6, 'Kiara',    'Canino', DATE '2013-03-03', 'N');\n"
                                 '\n'
                                 '-- Citas (ids 1..10)\n'
                                 'INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                 'estado) VALUES\n'
                                 "  (1, 1, TIMESTAMP '2026-09-01 08:00:00', 'PROGRAMADA'),\n"
                                 "  (2, 1, TIMESTAMP '2026-09-01 09:00:00', 'ATENDIDA'),\n"
                                 "  (4, 2, TIMESTAMP '2026-09-01 10:00:00', 'PROGRAMADA'),\n"
                                 "  (5, 3, TIMESTAMP '2026-09-02 08:30:00', 'CANCELADA'),\n"
                                 "  (6, 2, TIMESTAMP '2026-09-02 11:00:00', 'ATENDIDA'),\n"
                                 "  (7, 4, TIMESTAMP '2026-09-03 07:45:00', 'PROGRAMADA'),\n"
                                 "  (1, 1, TIMESTAMP '2026-09-05 15:00:00', 'ATENDIDA'),\n"
                                 "  (2, 3, TIMESTAMP '2026-09-08 16:00:00', 'PROGRAMADA'),\n"
                                 "  (4, 4, TIMESTAMP '2026-09-10 08:00:00', 'PROGRAMADA'),\n"
                                 "  (6, 1, TIMESTAMP '2026-09-10 09:00:00', 'ATENDIDA');\n"
                                 '\n'
                                 '-- Volumen sintetico para que el planeador tenga con que '
                                 'trabajar\n'
                                 'INSERT INTO dueno (nombre, telefono, email)\n'
                                 "SELECT 'Dueno ' || g, '300' || LPAD(g::text, 7, '0'), 'dueno' || "
                                 "g || '@mail.com'\n"
                                 'FROM generate_series(1, 2000) AS g;\n'
                                 '\n'
                                 'INSERT INTO veterinario (nombre, especialidad)\n'
                                 "SELECT 'Veterinario ' || g,\n"
                                 "       CASE WHEN g % 3 = 0 THEN 'Cirugia'\n"
                                 "            WHEN g % 3 = 1 THEN 'General'\n"
                                 "            ELSE 'Dermatologia' END\n"
                                 'FROM generate_series(1, 12) AS g;\n'
                                 '\n'
                                 'INSERT INTO mascota (id_dueno, nombre, especie, activa)\n'
                                 'SELECT 1 + (g % 2000),\n'
                                 "       'Mascota ' || g,\n"
                                 "       CASE WHEN g % 2 = 0 THEN 'Canino' ELSE 'Felino' END,\n"
                                 "       CASE WHEN g % 17 = 0 THEN 'N' ELSE 'S' END\n"
                                 'FROM generate_series(1, 5000) AS g;\n'
                                 '\n'
                                 'INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                 'estado)\n'
                                 'SELECT 1 + (g % 5000),\n'
                                 '       1 + (g % 12),\n'
                                 "       TIMESTAMP '2026-01-05 08:00:00'\n"
                                 "         + ((g % 200) * INTERVAL '1 day')\n"
                                 "         + ((g % 9) * INTERVAL '45 minutes'),\n"
                                 "       CASE WHEN g % 11 = 0 THEN 'CANCELADA'\n"
                                 "            WHEN g % 3 = 0 THEN 'ATENDIDA'\n"
                                 "            ELSE 'PROGRAMADA' END\n"
                                 'FROM generate_series(1, 30000) AS g;\n'
                                 '\n'
                                 'ANALYZE dueno;\n'
                                 'ANALYZE mascota;\n'
                                 'ANALYZE veterinario;\n'
                                 'ANALYZE cita;\n',
                    'tipo': 'bd_sql'},
                   {'enunciado': '## 2. Medir con EXPLAIN ANALYZE: la evidencia del antes/despues\n'
                                 '\n'
                                 'Misma base con volumen (30.010 citas, sin indices adicionales, '
                                 'estadisticas actualizadas).\n'
                                 '\n'
                                 'Genera la **evidencia cuantitativa** de la optimizacion. '
                                 'Escribe, en este orden:\n'
                                 '\n'
                                 '1. `EXPLAIN (ANALYZE, BUFFERS) <consulta ANTES>` usando '
                                 'exactamente la consulta con antipatrones de la pregunta 1.\n'
                                 '2. `EXPLAIN (ANALYZE, BUFFERS) <consulta DESPUES>` con tu '
                                 'version optimizada.\n'
                                 '   *(Si tu entorno no soporta la opcion `BUFFERS`, usa `EXPLAIN '
                                 'ANALYZE` a secas y dilo en la pregunta 5.)*\n'
                                 '3. Una tercera sentencia: `EXPLAIN ANALYZE` de la version '
                                 'DESPUES **anadiendo `LIMIT 50`**, que es lo que realmente '
                                 'necesita la pantalla de agenda.\n'
                                 '\n'
                                 'Despues de los tres `EXPLAIN`, escribe **como comentarios SQL** '
                                 '(lineas que empiezan con `--`) una mini tabla con lo que leiste '
                                 'del plan, con estos campos por version:\n'
                                 '\n'
                                 '```\n'
                                 '-- VERSION | nodo mas costoso | filas estimadas vs reales | '
                                 'tiempo total (ms)\n'
                                 '-- ANTES   | ...\n'
                                 '-- DESPUES | ...\n'
                                 '```\n'
                                 '\n'
                                 'Y una linea final `-- CONCLUSION:` indicando el factor de mejora '
                                 'aproximado.\n'
                                 '\n'
                                 '**Como leer el plan:** busca `Seq Scan` (recorrido completo de '
                                 'tabla), `Hash Join` / `Nested Loop`, el `cost=` estimado, '
                                 '`rows=` estimadas frente a `actual rows=`, y `Execution Time`.',
                    'puntos': 20,
                    'rubrica': 'Los tres EXPLAIN corren y corresponden a las consultas indicadas. '
                               'La tabla en comentarios reporta nodo mas costoso, filas estimadas '
                               'vs reales y tiempo de ejecucion para ANTES y DESPUES, con valores '
                               'tomados del plan real y no inventados. La conclusion cuantifica la '
                               'mejora. Se descuenta si solo se pega el plan sin interpretarlo o '
                               'si falta la variante con LIMIT 50.',
                    'setup_sql': 'CREATE TABLE dueno (\n'
                                 '  id_dueno SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  telefono TEXT,\n'
                                 '  email TEXT,\n'
                                 "  ciudad TEXT DEFAULT 'Cali'\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE mascota (\n'
                                 '  id_mascota SERIAL PRIMARY KEY,\n'
                                 '  id_dueno INT NOT NULL REFERENCES dueno(id_dueno),\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especie TEXT NOT NULL,\n'
                                 '  fecha_nac DATE,\n'
                                 "  activa CHAR(1) NOT NULL DEFAULT 'S' CHECK (activa IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE veterinario (\n'
                                 '  id_veterinario SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especialidad TEXT,\n'
                                 "  activo CHAR(1) NOT NULL DEFAULT 'S' CHECK (activo IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE cita (\n'
                                 '  id_cita SERIAL PRIMARY KEY,\n'
                                 '  id_mascota INT NOT NULL REFERENCES mascota(id_mascota),\n'
                                 '  id_veterinario INT NOT NULL REFERENCES '
                                 'veterinario(id_veterinario),\n'
                                 '  fecha_hora TIMESTAMP NOT NULL,\n'
                                 "  estado TEXT NOT NULL DEFAULT 'PROGRAMADA'\n"
                                 "    CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))\n"
                                 ');\n'
                                 '\n'
                                 '-- Duenos (ids 1..6 en este orden)\n'
                                 'INSERT INTO dueno (nombre, telefono, email) VALUES\n'
                                 "  ('Ana Gomez',      '3001112233', 'ana.gomez@mail.com'),\n"
                                 "  ('Carlos Ruiz',    '3014445566', 'carlos.ruiz@mail.com'),\n"
                                 "  ('Marcela Diaz',   '3027778899', 'marcela.diaz@mail.com'),\n"
                                 "  ('Jorge Pineda',   '3105551212', 'jorge.pineda@mail.com'),\n"
                                 "  ('Luisa Cardona',  '3123334455', 'luisa.cardona@mail.com'),\n"
                                 "  ('Andres Vallejo', '3159998877', 'andres.vallejo@mail.com');\n"
                                 '\n'
                                 '-- Veterinarios (ids 1..4)\n'
                                 'INSERT INTO veterinario (nombre, especialidad) VALUES\n'
                                 "  ('Laura Restrepo', 'General'),\n"
                                 "  ('Diego Moreno',   'Cirugia'),\n"
                                 "  ('Paula Salazar',  'Dermatologia'),\n"
                                 "  ('Ivan Ortiz',     'General');\n"
                                 '\n'
                                 '-- Mascotas (ids 1..8). Rocky (3) y Kiara (8) estan INACTIVAS.\n'
                                 'INSERT INTO mascota (id_dueno, nombre, especie, fecha_nac, '
                                 'activa) VALUES\n'
                                 "  (1, 'Firulais', 'Canino', DATE '2019-04-12', 'S'),\n"
                                 "  (1, 'Luna',     'Felino', DATE '2021-08-30', 'S'),\n"
                                 "  (2, 'Rocky',    'Canino', DATE '2015-01-20', 'N'),\n"
                                 "  (3, 'Mishi',    'Felino', DATE '2022-11-05', 'S'),\n"
                                 "  (3, 'Bobby',    'Canino', DATE '2018-06-17', 'S'),\n"
                                 "  (4, 'Nube',     'Felino', DATE '2023-02-09', 'S'),\n"
                                 "  (5, 'Toby',     'Canino', DATE '2020-09-25', 'S'),\n"
                                 "  (6, 'Kiara',    'Canino', DATE '2013-03-03', 'N');\n"
                                 '\n'
                                 '-- Citas (ids 1..10)\n'
                                 'INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                 'estado) VALUES\n'
                                 "  (1, 1, TIMESTAMP '2026-09-01 08:00:00', 'PROGRAMADA'),\n"
                                 "  (2, 1, TIMESTAMP '2026-09-01 09:00:00', 'ATENDIDA'),\n"
                                 "  (4, 2, TIMESTAMP '2026-09-01 10:00:00', 'PROGRAMADA'),\n"
                                 "  (5, 3, TIMESTAMP '2026-09-02 08:30:00', 'CANCELADA'),\n"
                                 "  (6, 2, TIMESTAMP '2026-09-02 11:00:00', 'ATENDIDA'),\n"
                                 "  (7, 4, TIMESTAMP '2026-09-03 07:45:00', 'PROGRAMADA'),\n"
                                 "  (1, 1, TIMESTAMP '2026-09-05 15:00:00', 'ATENDIDA'),\n"
                                 "  (2, 3, TIMESTAMP '2026-09-08 16:00:00', 'PROGRAMADA'),\n"
                                 "  (4, 4, TIMESTAMP '2026-09-10 08:00:00', 'PROGRAMADA'),\n"
                                 "  (6, 1, TIMESTAMP '2026-09-10 09:00:00', 'ATENDIDA');\n"
                                 '\n'
                                 '-- Volumen sintetico para que el planeador tenga con que '
                                 'trabajar\n'
                                 'INSERT INTO dueno (nombre, telefono, email)\n'
                                 "SELECT 'Dueno ' || g, '300' || LPAD(g::text, 7, '0'), 'dueno' || "
                                 "g || '@mail.com'\n"
                                 'FROM generate_series(1, 2000) AS g;\n'
                                 '\n'
                                 'INSERT INTO veterinario (nombre, especialidad)\n'
                                 "SELECT 'Veterinario ' || g,\n"
                                 "       CASE WHEN g % 3 = 0 THEN 'Cirugia'\n"
                                 "            WHEN g % 3 = 1 THEN 'General'\n"
                                 "            ELSE 'Dermatologia' END\n"
                                 'FROM generate_series(1, 12) AS g;\n'
                                 '\n'
                                 'INSERT INTO mascota (id_dueno, nombre, especie, activa)\n'
                                 'SELECT 1 + (g % 2000),\n'
                                 "       'Mascota ' || g,\n"
                                 "       CASE WHEN g % 2 = 0 THEN 'Canino' ELSE 'Felino' END,\n"
                                 "       CASE WHEN g % 17 = 0 THEN 'N' ELSE 'S' END\n"
                                 'FROM generate_series(1, 5000) AS g;\n'
                                 '\n'
                                 'INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                 'estado)\n'
                                 'SELECT 1 + (g % 5000),\n'
                                 '       1 + (g % 12),\n'
                                 "       TIMESTAMP '2026-01-05 08:00:00'\n"
                                 "         + ((g % 200) * INTERVAL '1 day')\n"
                                 "         + ((g % 9) * INTERVAL '45 minutes'),\n"
                                 "       CASE WHEN g % 11 = 0 THEN 'CANCELADA'\n"
                                 "            WHEN g % 3 = 0 THEN 'ATENDIDA'\n"
                                 "            ELSE 'PROGRAMADA' END\n"
                                 'FROM generate_series(1, 30000) AS g;\n'
                                 '\n'
                                 'ANALYZE dueno;\n'
                                 'ANALYZE mascota;\n'
                                 'ANALYZE veterinario;\n'
                                 'ANALYZE cita;\n',
                    'tipo': 'bd_sql'},
                   {'enunciado': '## 3. Matar la subconsulta correlacionada del reporte de duenos\n'
                                 '\n'
                                 'Misma base con volumen (2.006 duenos, 5.008 mascotas, 30.010 '
                                 'citas).\n'
                                 '\n'
                                 'Huellitas quiere el ranking de duenos por cantidad de citas. La '
                                 'version **ANTES** ejecuta una subconsulta **por cada fila** de '
                                 '`dueno` (2.006 veces):\n'
                                 '\n'
                                 '```sql\n'
                                 'SELECT d.id_dueno,\n'
                                 '       d.nombre,\n'
                                 '       (SELECT COUNT(*)\n'
                                 '          FROM cita c\n'
                                 '          JOIN mascota m ON m.id_mascota = c.id_mascota\n'
                                 '         WHERE m.id_dueno = d.id_dueno) AS total_citas\n'
                                 'FROM dueno d\n'
                                 'ORDER BY total_citas DESC;\n'
                                 '```\n'
                                 '\n'
                                 '**Tu trabajo:**\n'
                                 '\n'
                                 '1. Ejecuta la version ANTES y luego `EXPLAIN ANALYZE` de la '
                                 'misma para registrar la linea base.\n'
                                 '2. Escribe la version **DESPUES** que obtenga el mismo resultado '
                                 'con **una sola pasada**: `dueno LEFT JOIN mascota LEFT JOIN '
                                 'cita` + `GROUP BY d.id_dueno, d.nombre` + `COUNT(c.id_cita)`.\n'
                                 '   Debe conservar a los duenos con **cero** citas (por eso `LEFT '
                                 'JOIN` y `COUNT(c.id_cita)`, no `COUNT(*)`).\n'
                                 '   Agrega `ORDER BY total_citas DESC, d.id_dueno` y `LIMIT 20`.\n'
                                 '3. Ejecuta `EXPLAIN ANALYZE` de la version DESPUES.\n'
                                 '4. Demuestra la equivalencia: una consulta que compare las dos '
                                 'versiones y devuelva **cero filas** si coinciden. Sugerencia: '
                                 'usa `EXCEPT` entre los dos conjuntos completos (`id_dueno, '
                                 'total_citas`), en ambos sentidos, sin `LIMIT`.',
                    'puntos': 20,
                    'rubrica': 'La version DESPUES elimina la subconsulta correlacionada usando '
                               'LEFT JOIN + GROUP BY y conserva los duenos con cero citas (COUNT '
                               'de la columna, no COUNT(*)). Se ejecutan los dos EXPLAIN ANALYZE y '
                               'se aprecia la diferencia de plan. La prueba de equivalencia con '
                               'EXCEPT en ambos sentidos devuelve cero filas. Se descuenta por '
                               'usar INNER JOIN (pierde duenos sin citas) o por omitir la '
                               'verificacion.',
                    'setup_sql': 'CREATE TABLE dueno (\n'
                                 '  id_dueno SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  telefono TEXT,\n'
                                 '  email TEXT,\n'
                                 "  ciudad TEXT DEFAULT 'Cali'\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE mascota (\n'
                                 '  id_mascota SERIAL PRIMARY KEY,\n'
                                 '  id_dueno INT NOT NULL REFERENCES dueno(id_dueno),\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especie TEXT NOT NULL,\n'
                                 '  fecha_nac DATE,\n'
                                 "  activa CHAR(1) NOT NULL DEFAULT 'S' CHECK (activa IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE veterinario (\n'
                                 '  id_veterinario SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especialidad TEXT,\n'
                                 "  activo CHAR(1) NOT NULL DEFAULT 'S' CHECK (activo IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE cita (\n'
                                 '  id_cita SERIAL PRIMARY KEY,\n'
                                 '  id_mascota INT NOT NULL REFERENCES mascota(id_mascota),\n'
                                 '  id_veterinario INT NOT NULL REFERENCES '
                                 'veterinario(id_veterinario),\n'
                                 '  fecha_hora TIMESTAMP NOT NULL,\n'
                                 "  estado TEXT NOT NULL DEFAULT 'PROGRAMADA'\n"
                                 "    CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))\n"
                                 ');\n'
                                 '\n'
                                 '-- Duenos (ids 1..6 en este orden)\n'
                                 'INSERT INTO dueno (nombre, telefono, email) VALUES\n'
                                 "  ('Ana Gomez',      '3001112233', 'ana.gomez@mail.com'),\n"
                                 "  ('Carlos Ruiz',    '3014445566', 'carlos.ruiz@mail.com'),\n"
                                 "  ('Marcela Diaz',   '3027778899', 'marcela.diaz@mail.com'),\n"
                                 "  ('Jorge Pineda',   '3105551212', 'jorge.pineda@mail.com'),\n"
                                 "  ('Luisa Cardona',  '3123334455', 'luisa.cardona@mail.com'),\n"
                                 "  ('Andres Vallejo', '3159998877', 'andres.vallejo@mail.com');\n"
                                 '\n'
                                 '-- Veterinarios (ids 1..4)\n'
                                 'INSERT INTO veterinario (nombre, especialidad) VALUES\n'
                                 "  ('Laura Restrepo', 'General'),\n"
                                 "  ('Diego Moreno',   'Cirugia'),\n"
                                 "  ('Paula Salazar',  'Dermatologia'),\n"
                                 "  ('Ivan Ortiz',     'General');\n"
                                 '\n'
                                 '-- Mascotas (ids 1..8). Rocky (3) y Kiara (8) estan INACTIVAS.\n'
                                 'INSERT INTO mascota (id_dueno, nombre, especie, fecha_nac, '
                                 'activa) VALUES\n'
                                 "  (1, 'Firulais', 'Canino', DATE '2019-04-12', 'S'),\n"
                                 "  (1, 'Luna',     'Felino', DATE '2021-08-30', 'S'),\n"
                                 "  (2, 'Rocky',    'Canino', DATE '2015-01-20', 'N'),\n"
                                 "  (3, 'Mishi',    'Felino', DATE '2022-11-05', 'S'),\n"
                                 "  (3, 'Bobby',    'Canino', DATE '2018-06-17', 'S'),\n"
                                 "  (4, 'Nube',     'Felino', DATE '2023-02-09', 'S'),\n"
                                 "  (5, 'Toby',     'Canino', DATE '2020-09-25', 'S'),\n"
                                 "  (6, 'Kiara',    'Canino', DATE '2013-03-03', 'N');\n"
                                 '\n'
                                 '-- Citas (ids 1..10)\n'
                                 'INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                 'estado) VALUES\n'
                                 "  (1, 1, TIMESTAMP '2026-09-01 08:00:00', 'PROGRAMADA'),\n"
                                 "  (2, 1, TIMESTAMP '2026-09-01 09:00:00', 'ATENDIDA'),\n"
                                 "  (4, 2, TIMESTAMP '2026-09-01 10:00:00', 'PROGRAMADA'),\n"
                                 "  (5, 3, TIMESTAMP '2026-09-02 08:30:00', 'CANCELADA'),\n"
                                 "  (6, 2, TIMESTAMP '2026-09-02 11:00:00', 'ATENDIDA'),\n"
                                 "  (7, 4, TIMESTAMP '2026-09-03 07:45:00', 'PROGRAMADA'),\n"
                                 "  (1, 1, TIMESTAMP '2026-09-05 15:00:00', 'ATENDIDA'),\n"
                                 "  (2, 3, TIMESTAMP '2026-09-08 16:00:00', 'PROGRAMADA'),\n"
                                 "  (4, 4, TIMESTAMP '2026-09-10 08:00:00', 'PROGRAMADA'),\n"
                                 "  (6, 1, TIMESTAMP '2026-09-10 09:00:00', 'ATENDIDA');\n"
                                 '\n'
                                 '-- Volumen sintetico para que el planeador tenga con que '
                                 'trabajar\n'
                                 'INSERT INTO dueno (nombre, telefono, email)\n'
                                 "SELECT 'Dueno ' || g, '300' || LPAD(g::text, 7, '0'), 'dueno' || "
                                 "g || '@mail.com'\n"
                                 'FROM generate_series(1, 2000) AS g;\n'
                                 '\n'
                                 'INSERT INTO veterinario (nombre, especialidad)\n'
                                 "SELECT 'Veterinario ' || g,\n"
                                 "       CASE WHEN g % 3 = 0 THEN 'Cirugia'\n"
                                 "            WHEN g % 3 = 1 THEN 'General'\n"
                                 "            ELSE 'Dermatologia' END\n"
                                 'FROM generate_series(1, 12) AS g;\n'
                                 '\n'
                                 'INSERT INTO mascota (id_dueno, nombre, especie, activa)\n'
                                 'SELECT 1 + (g % 2000),\n'
                                 "       'Mascota ' || g,\n"
                                 "       CASE WHEN g % 2 = 0 THEN 'Canino' ELSE 'Felino' END,\n"
                                 "       CASE WHEN g % 17 = 0 THEN 'N' ELSE 'S' END\n"
                                 'FROM generate_series(1, 5000) AS g;\n'
                                 '\n'
                                 'INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                 'estado)\n'
                                 'SELECT 1 + (g % 5000),\n'
                                 '       1 + (g % 12),\n'
                                 "       TIMESTAMP '2026-01-05 08:00:00'\n"
                                 "         + ((g % 200) * INTERVAL '1 day')\n"
                                 "         + ((g % 9) * INTERVAL '45 minutes'),\n"
                                 "       CASE WHEN g % 11 = 0 THEN 'CANCELADA'\n"
                                 "            WHEN g % 3 = 0 THEN 'ATENDIDA'\n"
                                 "            ELSE 'PROGRAMADA' END\n"
                                 'FROM generate_series(1, 30000) AS g;\n'
                                 '\n'
                                 'ANALYZE dueno;\n'
                                 'ANALYZE mascota;\n'
                                 'ANALYZE veterinario;\n'
                                 'ANALYZE cita;\n',
                    'tipo': 'bd_sql'},
                   {'correctas': [0, 1, 3, 5],
                    'enunciado': '## 4. Antipatrones de consulta en VetCare\n'
                                 '\n'
                                 'Selecciona **todas** las afirmaciones correctas sobre '
                                 'optimizacion de consultas en PostgreSQL, en el contexto de '
                                 'VetCare DB.',
                    'opciones': ['Envolver la columna en una funcion (to_char(fecha_hora,...) o '
                                 'EXTRACT) impide que el motor use un indice sobre esa columna: se '
                                 'pierde la sargabilidad.',
                                 'SELECT * en un join de 4 tablas transporta columnas que nadie '
                                 'usa y encarece el ordenamiento y la red.',
                                 'Optimizar una consulta puede cambiar el numero de filas que '
                                 'devuelve, siempre que sea mas rapida.',
                                 'Una subconsulta correlacionada en la lista de columnas se evalua '
                                 'una vez por fila del exterior; reescribirla como JOIN con GROUP '
                                 'BY suele bajar el costo un orden de magnitud.',
                                 'Cambiar la coma por JOIN ... ON por si solo hace la consulta mas '
                                 'rapida, porque el motor usa otro algoritmo.',
                                 'EXPLAIN muestra el plan estimado y EXPLAIN ANALYZE lo ejecuta de '
                                 'verdad y reporta filas y tiempos reales; comparar estimado vs '
                                 'real revela estadisticas desactualizadas.'],
                    'puntos': 10,
                    'rubrica': '10 puntos con las 4 opciones correctas y ninguna incorrecta; '
                               'puntaje proporcional por acierto parcial. Correctas: indices 0, 1, '
                               '3 y 5.',
                    'tipo': 'cerrada_multi'},
                   {'enunciado': '## 5. Justificacion tecnica del antes/despues (media pagina)\n'
                                 '\n'
                                 'Escribe la justificacion que ira al informe del PI, con esta '
                                 'estructura:\n'
                                 '\n'
                                 '1. **Consulta elegida y para que sirve en Huellitas**: en una '
                                 'frase, que pantalla o reporte la usa y con que frecuencia.\n'
                                 '2. **Tres cambios concretos** que hiciste en el par '
                                 'antes/despues. Para cada uno: que cambiaste, **por que** mejora '
                                 '(habla de sargabilidad, proyeccion, cardinalidad, numero de '
                                 'pasadas sobre la tabla) y **que evidencia** del `EXPLAIN '
                                 'ANALYZE` lo respalda (nodo que desaparecio, tiempo que bajo, '
                                 'filas que dejaron de leerse).\n'
                                 '3. **Que NO cambio**: confirma que el resultado es equivalente y '
                                 'di como lo verificaste (`COUNT(*)` igual, `EXCEPT` vacio).\n'
                                 '4. **Que sigue**: que indice propondrias en la Clase 7 para esta '
                                 'misma consulta y por que crees que ayudaria.\n'
                                 '5. **Limites de la medicion**: reconoce que mediste sobre '
                                 'PostgreSQL en el navegador con 30.010 filas y sin concurrencia, '
                                 'y di que cambiaria en un servidor real con millones de citas y '
                                 'varios usuarios.\n'
                                 '\n'
                                 'Recuerda guardar tus scripts como `06_opt_antes.sql` y '
                                 '`06_opt_despues.sql` en tu carpeta del PI.',
                    'puntos': 20,
                    'rubrica': 'Las 5 secciones estan presentes. Los tres cambios estan '
                               'justificados con vocabulario tecnico correcto (sargabilidad, '
                               'proyeccion, numero de pasadas) y cada uno se ancla a una evidencia '
                               'concreta del plan de ejecucion. Se afirma y se demuestra la '
                               'equivalencia del resultado. La seccion 5 reconoce honestamente los '
                               'limites del entorno de medicion.',
                    'tipo': 'abierta'}],
     'resumen': 'El estudiante reescribe dos consultas reales del PI con antipatrones, mide la '
                'mejora con EXPLAIN ANALYZE sobre 30.000 citas y justifica cada cambio en el '
                'informe del proyecto.',
     'titulo': 'Taller Clase 6 en ExamLab - Optimizacion de consultas de VetCare (antes / '
               'despues)'},
 7: {'preguntas': [{'enunciado': '## 1. Crear los indices de las tablas calientes y probar que se '
                                 'usan\n'
                                 '\n'
                                 'Base con volumen: **30.010 citas** (2026-01-05 a 2026-07-23), '
                                 '5.008 mascotas, 2.006 duenos, 16 veterinarios. Estadisticas '
                                 'actualizadas y **sin indices** salvo las PK.\n'
                                 '\n'
                                 'Las dos consultas frecuentes del PI son:\n'
                                 '\n'
                                 '- **C1 (agenda del dia):** citas `PROGRAMADA` de un dia '
                                 'concreto, filtrando `fecha_hora` por rango.\n'
                                 '- **C2 (mascotas de un dueno):** todas las mascotas de un '
                                 '`id_dueno` dado.\n'
                                 '\n'
                                 '**Escribe el SQL que:**\n'
                                 '\n'
                                 '1. Muestre la linea base: `EXPLAIN ANALYZE` de C1 y de C2 '
                                 '**antes** de crear indices. Debes ver `Seq Scan`.\n'
                                 '   - C1: `SELECT id_cita, fecha_hora, estado FROM cita WHERE '
                                 "fecha_hora >= TIMESTAMP '2026-03-10 00:00:00' AND fecha_hora < "
                                 "TIMESTAMP '2026-03-11 00:00:00' AND estado = 'PROGRAMADA';`\n"
                                 '   - C2: `SELECT id_mascota, nombre, especie FROM mascota WHERE '
                                 'id_dueno = 1234;`\n'
                                 '2. Cree **tres indices** con nombres exactos:\n'
                                 '   - `idx_cita_fecha_hora` sobre `cita (fecha_hora)`\n'
                                 '   - `idx_mascota_dueno` sobre `mascota (id_dueno)`\n'
                                 '   - `idx_cita_programada_fecha`: indice **parcial** sobre `cita '
                                 "(fecha_hora)` `WHERE estado = 'PROGRAMADA'`\n"
                                 '3. Ejecute `ANALYZE cita;` y `ANALYZE mascota;` para refrescar '
                                 'estadisticas.\n'
                                 '4. Repita `EXPLAIN ANALYZE` de C1 y C2 y muestre que el plan '
                                 'cambio a `Index Scan` / `Bitmap Index Scan`.\n'
                                 '5. Termine con una consulta que liste los indices creados: '
                                 '`SELECT indexname, tablename, indexdef FROM pg_indexes WHERE '
                                 "tablename IN ('cita','mascota') ORDER BY tablename, indexname;`\n"
                                 '\n'
                                 '**Nota:** un indice parcial ocupa menos y solo sirve si la '
                                 'consulta incluye la misma condicion del `WHERE` del indice. '
                                 'Comprueba en el plan cual de los dos indices sobre `fecha_hora` '
                                 'eligio el planeador para C1.',
                    'puntos': 30,
                    'rubrica': 'Se muestra la linea base con Seq Scan antes de indexar. Se crean '
                               'los 3 indices con los nombres exactos, incluido el parcial con su '
                               'clausula WHERE. Tras ANALYZE, los EXPLAIN posteriores evidencian '
                               'Index Scan o Bitmap Index Scan en al menos C1 y C2. La consulta a '
                               'pg_indexes lista los 3 indices. Se descuenta si falta el indice '
                               'parcial, si no se re-ejecutan los EXPLAIN o si no se comenta cual '
                               'indice eligio el planeador.',
                    'setup_sql': 'CREATE TABLE dueno (\n'
                                 '  id_dueno SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  telefono TEXT,\n'
                                 '  email TEXT,\n'
                                 "  ciudad TEXT DEFAULT 'Cali'\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE mascota (\n'
                                 '  id_mascota SERIAL PRIMARY KEY,\n'
                                 '  id_dueno INT NOT NULL REFERENCES dueno(id_dueno),\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especie TEXT NOT NULL,\n'
                                 '  fecha_nac DATE,\n'
                                 "  activa CHAR(1) NOT NULL DEFAULT 'S' CHECK (activa IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE veterinario (\n'
                                 '  id_veterinario SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especialidad TEXT,\n'
                                 "  activo CHAR(1) NOT NULL DEFAULT 'S' CHECK (activo IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE cita (\n'
                                 '  id_cita SERIAL PRIMARY KEY,\n'
                                 '  id_mascota INT NOT NULL REFERENCES mascota(id_mascota),\n'
                                 '  id_veterinario INT NOT NULL REFERENCES '
                                 'veterinario(id_veterinario),\n'
                                 '  fecha_hora TIMESTAMP NOT NULL,\n'
                                 "  estado TEXT NOT NULL DEFAULT 'PROGRAMADA'\n"
                                 "    CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))\n"
                                 ');\n'
                                 '\n'
                                 '-- Duenos (ids 1..6 en este orden)\n'
                                 'INSERT INTO dueno (nombre, telefono, email) VALUES\n'
                                 "  ('Ana Gomez',      '3001112233', 'ana.gomez@mail.com'),\n"
                                 "  ('Carlos Ruiz',    '3014445566', 'carlos.ruiz@mail.com'),\n"
                                 "  ('Marcela Diaz',   '3027778899', 'marcela.diaz@mail.com'),\n"
                                 "  ('Jorge Pineda',   '3105551212', 'jorge.pineda@mail.com'),\n"
                                 "  ('Luisa Cardona',  '3123334455', 'luisa.cardona@mail.com'),\n"
                                 "  ('Andres Vallejo', '3159998877', 'andres.vallejo@mail.com');\n"
                                 '\n'
                                 '-- Veterinarios (ids 1..4)\n'
                                 'INSERT INTO veterinario (nombre, especialidad) VALUES\n'
                                 "  ('Laura Restrepo', 'General'),\n"
                                 "  ('Diego Moreno',   'Cirugia'),\n"
                                 "  ('Paula Salazar',  'Dermatologia'),\n"
                                 "  ('Ivan Ortiz',     'General');\n"
                                 '\n'
                                 '-- Mascotas (ids 1..8). Rocky (3) y Kiara (8) estan INACTIVAS.\n'
                                 'INSERT INTO mascota (id_dueno, nombre, especie, fecha_nac, '
                                 'activa) VALUES\n'
                                 "  (1, 'Firulais', 'Canino', DATE '2019-04-12', 'S'),\n"
                                 "  (1, 'Luna',     'Felino', DATE '2021-08-30', 'S'),\n"
                                 "  (2, 'Rocky',    'Canino', DATE '2015-01-20', 'N'),\n"
                                 "  (3, 'Mishi',    'Felino', DATE '2022-11-05', 'S'),\n"
                                 "  (3, 'Bobby',    'Canino', DATE '2018-06-17', 'S'),\n"
                                 "  (4, 'Nube',     'Felino', DATE '2023-02-09', 'S'),\n"
                                 "  (5, 'Toby',     'Canino', DATE '2020-09-25', 'S'),\n"
                                 "  (6, 'Kiara',    'Canino', DATE '2013-03-03', 'N');\n"
                                 '\n'
                                 '-- Citas (ids 1..10)\n'
                                 'INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                 'estado) VALUES\n'
                                 "  (1, 1, TIMESTAMP '2026-09-01 08:00:00', 'PROGRAMADA'),\n"
                                 "  (2, 1, TIMESTAMP '2026-09-01 09:00:00', 'ATENDIDA'),\n"
                                 "  (4, 2, TIMESTAMP '2026-09-01 10:00:00', 'PROGRAMADA'),\n"
                                 "  (5, 3, TIMESTAMP '2026-09-02 08:30:00', 'CANCELADA'),\n"
                                 "  (6, 2, TIMESTAMP '2026-09-02 11:00:00', 'ATENDIDA'),\n"
                                 "  (7, 4, TIMESTAMP '2026-09-03 07:45:00', 'PROGRAMADA'),\n"
                                 "  (1, 1, TIMESTAMP '2026-09-05 15:00:00', 'ATENDIDA'),\n"
                                 "  (2, 3, TIMESTAMP '2026-09-08 16:00:00', 'PROGRAMADA'),\n"
                                 "  (4, 4, TIMESTAMP '2026-09-10 08:00:00', 'PROGRAMADA'),\n"
                                 "  (6, 1, TIMESTAMP '2026-09-10 09:00:00', 'ATENDIDA');\n"
                                 '\n'
                                 '-- Volumen sintetico para que el planeador tenga con que '
                                 'trabajar\n'
                                 'INSERT INTO dueno (nombre, telefono, email)\n'
                                 "SELECT 'Dueno ' || g, '300' || LPAD(g::text, 7, '0'), 'dueno' || "
                                 "g || '@mail.com'\n"
                                 'FROM generate_series(1, 2000) AS g;\n'
                                 '\n'
                                 'INSERT INTO veterinario (nombre, especialidad)\n'
                                 "SELECT 'Veterinario ' || g,\n"
                                 "       CASE WHEN g % 3 = 0 THEN 'Cirugia'\n"
                                 "            WHEN g % 3 = 1 THEN 'General'\n"
                                 "            ELSE 'Dermatologia' END\n"
                                 'FROM generate_series(1, 12) AS g;\n'
                                 '\n'
                                 'INSERT INTO mascota (id_dueno, nombre, especie, activa)\n'
                                 'SELECT 1 + (g % 2000),\n'
                                 "       'Mascota ' || g,\n"
                                 "       CASE WHEN g % 2 = 0 THEN 'Canino' ELSE 'Felino' END,\n"
                                 "       CASE WHEN g % 17 = 0 THEN 'N' ELSE 'S' END\n"
                                 'FROM generate_series(1, 5000) AS g;\n'
                                 '\n'
                                 'INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                 'estado)\n'
                                 'SELECT 1 + (g % 5000),\n'
                                 '       1 + (g % 12),\n'
                                 "       TIMESTAMP '2026-01-05 08:00:00'\n"
                                 "         + ((g % 200) * INTERVAL '1 day')\n"
                                 "         + ((g % 9) * INTERVAL '45 minutes'),\n"
                                 "       CASE WHEN g % 11 = 0 THEN 'CANCELADA'\n"
                                 "            WHEN g % 3 = 0 THEN 'ATENDIDA'\n"
                                 "            ELSE 'PROGRAMADA' END\n"
                                 'FROM generate_series(1, 30000) AS g;\n'
                                 '\n'
                                 'ANALYZE dueno;\n'
                                 'ANALYZE mascota;\n'
                                 'ANALYZE veterinario;\n'
                                 'ANALYZE cita;\n',
                    'tipo': 'bd_sql'},
                   {'enunciado': '## 2. Orden de columnas en un indice compuesto\n'
                                 '\n'
                                 'Misma base con volumen (30.010 citas, sin indices adicionales).\n'
                                 '\n'
                                 'Vas a demostrar experimentalmente que **el orden de las columnas '
                                 'de un indice compuesto importa**.\n'
                                 '\n'
                                 '1. Crea los dos indices compuestos:\n'
                                 '   - `idx_cita_estado_fecha` sobre `cita (estado, fecha_hora)`\n'
                                 '   - `idx_cita_fecha_estado` sobre `cita (fecha_hora, estado)`\n'
                                 '   y ejecuta `ANALYZE cita;`\n'
                                 '2. Ejecuta `EXPLAIN ANALYZE` de estas **tres** consultas y '
                                 'observa que indice elige el planeador en cada caso:\n'
                                 '   - **Q1** (filtro por estado + rango de fecha):\n'
                                 '     `SELECT id_cita, fecha_hora FROM cita WHERE estado = '
                                 "'PROGRAMADA' AND fecha_hora >= TIMESTAMP '2026-03-10 00:00:00' "
                                 "AND fecha_hora < TIMESTAMP '2026-03-11 00:00:00';`\n"
                                 '   - **Q2** (solo rango de fecha):\n'
                                 '     `SELECT id_cita, fecha_hora FROM cita WHERE fecha_hora >= '
                                 "TIMESTAMP '2026-03-10 00:00:00' AND fecha_hora < TIMESTAMP "
                                 "'2026-03-11 00:00:00';`\n"
                                 '   - **Q3** (solo estado, muy poco selectivo):\n'
                                 "     `SELECT COUNT(*) FROM cita WHERE estado = 'PROGRAMADA';`\n"
                                 '3. Fuerza el experimento: elimina `idx_cita_fecha_estado` con '
                                 '`DROP INDEX`, vuelve a ejecutar `EXPLAIN ANALYZE` de **Q2** y '
                                 'compara. Explica en comentarios `--` si `(estado, fecha_hora)` '
                                 'sirve o no para una consulta que **no** filtra por estado.\n'
                                 '4. Cierra con `-- CONCLUSION:` en una o dos lineas: cual es la '
                                 'regla practica sobre el orden de columnas (columna de igualdad '
                                 'primero, columna de rango despues) y por que un indice cuya '
                                 'primera columna no aparece en el `WHERE` normalmente no se usa.',
                    'puntos': 20,
                    'rubrica': 'Se crean los dos indices compuestos y se ejecutan los EXPLAIN de '
                               'Q1, Q2 y Q3 identificando el indice elegido en cada uno. Se hace '
                               'el DROP INDEX y se vuelve a medir Q2, comparando el resultado. La '
                               'conclusion enuncia correctamente la regla de '
                               'igualdad-antes-de-rango y explica por que un indice cuya columna '
                               'lider no aparece en el filtro suele quedar sin usar (o solo servir '
                               'para Index Only Scan de barrido completo).',
                    'setup_sql': 'CREATE TABLE dueno (\n'
                                 '  id_dueno SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  telefono TEXT,\n'
                                 '  email TEXT,\n'
                                 "  ciudad TEXT DEFAULT 'Cali'\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE mascota (\n'
                                 '  id_mascota SERIAL PRIMARY KEY,\n'
                                 '  id_dueno INT NOT NULL REFERENCES dueno(id_dueno),\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especie TEXT NOT NULL,\n'
                                 '  fecha_nac DATE,\n'
                                 "  activa CHAR(1) NOT NULL DEFAULT 'S' CHECK (activa IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE veterinario (\n'
                                 '  id_veterinario SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especialidad TEXT,\n'
                                 "  activo CHAR(1) NOT NULL DEFAULT 'S' CHECK (activo IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE cita (\n'
                                 '  id_cita SERIAL PRIMARY KEY,\n'
                                 '  id_mascota INT NOT NULL REFERENCES mascota(id_mascota),\n'
                                 '  id_veterinario INT NOT NULL REFERENCES '
                                 'veterinario(id_veterinario),\n'
                                 '  fecha_hora TIMESTAMP NOT NULL,\n'
                                 "  estado TEXT NOT NULL DEFAULT 'PROGRAMADA'\n"
                                 "    CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))\n"
                                 ');\n'
                                 '\n'
                                 '-- Duenos (ids 1..6 en este orden)\n'
                                 'INSERT INTO dueno (nombre, telefono, email) VALUES\n'
                                 "  ('Ana Gomez',      '3001112233', 'ana.gomez@mail.com'),\n"
                                 "  ('Carlos Ruiz',    '3014445566', 'carlos.ruiz@mail.com'),\n"
                                 "  ('Marcela Diaz',   '3027778899', 'marcela.diaz@mail.com'),\n"
                                 "  ('Jorge Pineda',   '3105551212', 'jorge.pineda@mail.com'),\n"
                                 "  ('Luisa Cardona',  '3123334455', 'luisa.cardona@mail.com'),\n"
                                 "  ('Andres Vallejo', '3159998877', 'andres.vallejo@mail.com');\n"
                                 '\n'
                                 '-- Veterinarios (ids 1..4)\n'
                                 'INSERT INTO veterinario (nombre, especialidad) VALUES\n'
                                 "  ('Laura Restrepo', 'General'),\n"
                                 "  ('Diego Moreno',   'Cirugia'),\n"
                                 "  ('Paula Salazar',  'Dermatologia'),\n"
                                 "  ('Ivan Ortiz',     'General');\n"
                                 '\n'
                                 '-- Mascotas (ids 1..8). Rocky (3) y Kiara (8) estan INACTIVAS.\n'
                                 'INSERT INTO mascota (id_dueno, nombre, especie, fecha_nac, '
                                 'activa) VALUES\n'
                                 "  (1, 'Firulais', 'Canino', DATE '2019-04-12', 'S'),\n"
                                 "  (1, 'Luna',     'Felino', DATE '2021-08-30', 'S'),\n"
                                 "  (2, 'Rocky',    'Canino', DATE '2015-01-20', 'N'),\n"
                                 "  (3, 'Mishi',    'Felino', DATE '2022-11-05', 'S'),\n"
                                 "  (3, 'Bobby',    'Canino', DATE '2018-06-17', 'S'),\n"
                                 "  (4, 'Nube',     'Felino', DATE '2023-02-09', 'S'),\n"
                                 "  (5, 'Toby',     'Canino', DATE '2020-09-25', 'S'),\n"
                                 "  (6, 'Kiara',    'Canino', DATE '2013-03-03', 'N');\n"
                                 '\n'
                                 '-- Citas (ids 1..10)\n'
                                 'INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                 'estado) VALUES\n'
                                 "  (1, 1, TIMESTAMP '2026-09-01 08:00:00', 'PROGRAMADA'),\n"
                                 "  (2, 1, TIMESTAMP '2026-09-01 09:00:00', 'ATENDIDA'),\n"
                                 "  (4, 2, TIMESTAMP '2026-09-01 10:00:00', 'PROGRAMADA'),\n"
                                 "  (5, 3, TIMESTAMP '2026-09-02 08:30:00', 'CANCELADA'),\n"
                                 "  (6, 2, TIMESTAMP '2026-09-02 11:00:00', 'ATENDIDA'),\n"
                                 "  (7, 4, TIMESTAMP '2026-09-03 07:45:00', 'PROGRAMADA'),\n"
                                 "  (1, 1, TIMESTAMP '2026-09-05 15:00:00', 'ATENDIDA'),\n"
                                 "  (2, 3, TIMESTAMP '2026-09-08 16:00:00', 'PROGRAMADA'),\n"
                                 "  (4, 4, TIMESTAMP '2026-09-10 08:00:00', 'PROGRAMADA'),\n"
                                 "  (6, 1, TIMESTAMP '2026-09-10 09:00:00', 'ATENDIDA');\n"
                                 '\n'
                                 '-- Volumen sintetico para que el planeador tenga con que '
                                 'trabajar\n'
                                 'INSERT INTO dueno (nombre, telefono, email)\n'
                                 "SELECT 'Dueno ' || g, '300' || LPAD(g::text, 7, '0'), 'dueno' || "
                                 "g || '@mail.com'\n"
                                 'FROM generate_series(1, 2000) AS g;\n'
                                 '\n'
                                 'INSERT INTO veterinario (nombre, especialidad)\n'
                                 "SELECT 'Veterinario ' || g,\n"
                                 "       CASE WHEN g % 3 = 0 THEN 'Cirugia'\n"
                                 "            WHEN g % 3 = 1 THEN 'General'\n"
                                 "            ELSE 'Dermatologia' END\n"
                                 'FROM generate_series(1, 12) AS g;\n'
                                 '\n'
                                 'INSERT INTO mascota (id_dueno, nombre, especie, activa)\n'
                                 'SELECT 1 + (g % 2000),\n'
                                 "       'Mascota ' || g,\n"
                                 "       CASE WHEN g % 2 = 0 THEN 'Canino' ELSE 'Felino' END,\n"
                                 "       CASE WHEN g % 17 = 0 THEN 'N' ELSE 'S' END\n"
                                 'FROM generate_series(1, 5000) AS g;\n'
                                 '\n'
                                 'INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                 'estado)\n'
                                 'SELECT 1 + (g % 5000),\n'
                                 '       1 + (g % 12),\n'
                                 "       TIMESTAMP '2026-01-05 08:00:00'\n"
                                 "         + ((g % 200) * INTERVAL '1 day')\n"
                                 "         + ((g % 9) * INTERVAL '45 minutes'),\n"
                                 "       CASE WHEN g % 11 = 0 THEN 'CANCELADA'\n"
                                 "            WHEN g % 3 = 0 THEN 'ATENDIDA'\n"
                                 "            ELSE 'PROGRAMADA' END\n"
                                 'FROM generate_series(1, 30000) AS g;\n'
                                 '\n'
                                 'ANALYZE dueno;\n'
                                 'ANALYZE mascota;\n'
                                 'ANALYZE veterinario;\n'
                                 'ANALYZE cita;\n',
                    'tipo': 'bd_sql'},
                   {'enunciado': '## 3. Particionar el historico de citas por rango de fecha\n'
                                 '\n'
                                 'Esta base tiene **5.010 citas repartidas entre enero de 2025 y '
                                 'diciembre de 2026** en la tabla `cita`. Huellitas quiere '
                                 'archivar la historia en una tabla particionada por ano para que '
                                 'las consultas de un ano no toquen los datos del otro.\n'
                                 '\n'
                                 'Escribe el SQL que:\n'
                                 '\n'
                                 '1. Cree la tabla **particionada** `cita_hist` con las columnas '
                                 '`id_cita INT`, `id_mascota INT`, `id_veterinario INT`, '
                                 '`fecha_hora TIMESTAMP NOT NULL`, `estado TEXT`, usando '
                                 '`PARTITION BY RANGE (fecha_hora)`.\n'
                                 '   **Ojo:** en una tabla particionada la PK debe incluir la '
                                 'columna de particion, asi que declara `PRIMARY KEY (id_cita, '
                                 'fecha_hora)`.\n'
                                 '2. Cree **dos particiones**:\n'
                                 "   - `cita_hist_2025` para `FROM ('2025-01-01') TO "
                                 "('2026-01-01')`\n"
                                 "   - `cita_hist_2026` para `FROM ('2026-01-01') TO "
                                 "('2027-01-01')`\n"
                                 '   Sintaxis: `CREATE TABLE cita_hist_2025 PARTITION OF cita_hist '
                                 "FOR VALUES FROM (TIMESTAMP '2025-01-01') TO (TIMESTAMP "
                                 "'2026-01-01');`\n"
                                 '3. Migre **todas** las citas: `INSERT INTO cita_hist SELECT '
                                 'id_cita, id_mascota, id_veterinario, fecha_hora, estado FROM '
                                 'cita;`\n'
                                 '4. **Demuestre el enrutamiento**: `SELECT tableoid::regclass AS '
                                 'particion, COUNT(*), MIN(fecha_hora), MAX(fecha_hora) FROM '
                                 'cita_hist GROUP BY 1 ORDER BY 1;`\n'
                                 '   Debes ver las filas repartidas entre las dos particiones, con '
                                 'rangos de fecha que no se solapan.\n'
                                 '5. **Demuestre la poda de particiones** (*partition pruning*): '
                                 '`EXPLAIN ANALYZE SELECT COUNT(*) FROM cita_hist WHERE fecha_hora '
                                 ">= TIMESTAMP '2026-01-01' AND fecha_hora < TIMESTAMP "
                                 "'2027-01-01';` y verifica en el plan que **solo** aparece "
                                 '`cita_hist_2026`.\n'
                                 '6. Cierra con un comentario `--` explicando que operacion de '
                                 'mantenimiento se vuelve trivial con esta estructura (pista: '
                                 'archivar o eliminar un ano completo con `DROP TABLE` de la '
                                 'particion en vez de un `DELETE` masivo).',
                    'puntos': 20,
                    'rubrica': 'cita_hist se crea con PARTITION BY RANGE (fecha_hora) y PRIMARY '
                               'KEY que incluye la columna de particion; las dos particiones '
                               'cubren 2025 y 2026 sin solaparse. La migracion inserta las 5.010 '
                               'filas y la consulta con tableoid::regclass evidencia el reparto. '
                               'El EXPLAIN de la consulta de 2026 muestra poda (solo la particion '
                               '2026). El comentario final identifica correctamente el beneficio '
                               'de mantenimiento (DROP de particion vs DELETE masivo).',
                    'setup_sql': 'CREATE TABLE dueno (\n'
                                 '  id_dueno SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  telefono TEXT,\n'
                                 '  email TEXT,\n'
                                 "  ciudad TEXT DEFAULT 'Cali'\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE mascota (\n'
                                 '  id_mascota SERIAL PRIMARY KEY,\n'
                                 '  id_dueno INT NOT NULL REFERENCES dueno(id_dueno),\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especie TEXT NOT NULL,\n'
                                 '  fecha_nac DATE,\n'
                                 "  activa CHAR(1) NOT NULL DEFAULT 'S' CHECK (activa IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE veterinario (\n'
                                 '  id_veterinario SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especialidad TEXT,\n'
                                 "  activo CHAR(1) NOT NULL DEFAULT 'S' CHECK (activo IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE cita (\n'
                                 '  id_cita SERIAL PRIMARY KEY,\n'
                                 '  id_mascota INT NOT NULL REFERENCES mascota(id_mascota),\n'
                                 '  id_veterinario INT NOT NULL REFERENCES '
                                 'veterinario(id_veterinario),\n'
                                 '  fecha_hora TIMESTAMP NOT NULL,\n'
                                 "  estado TEXT NOT NULL DEFAULT 'PROGRAMADA'\n"
                                 "    CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))\n"
                                 ');\n'
                                 '\n'
                                 '-- Duenos (ids 1..6 en este orden)\n'
                                 'INSERT INTO dueno (nombre, telefono, email) VALUES\n'
                                 "  ('Ana Gomez',      '3001112233', 'ana.gomez@mail.com'),\n"
                                 "  ('Carlos Ruiz',    '3014445566', 'carlos.ruiz@mail.com'),\n"
                                 "  ('Marcela Diaz',   '3027778899', 'marcela.diaz@mail.com'),\n"
                                 "  ('Jorge Pineda',   '3105551212', 'jorge.pineda@mail.com'),\n"
                                 "  ('Luisa Cardona',  '3123334455', 'luisa.cardona@mail.com'),\n"
                                 "  ('Andres Vallejo', '3159998877', 'andres.vallejo@mail.com');\n"
                                 '\n'
                                 '-- Veterinarios (ids 1..4)\n'
                                 'INSERT INTO veterinario (nombre, especialidad) VALUES\n'
                                 "  ('Laura Restrepo', 'General'),\n"
                                 "  ('Diego Moreno',   'Cirugia'),\n"
                                 "  ('Paula Salazar',  'Dermatologia'),\n"
                                 "  ('Ivan Ortiz',     'General');\n"
                                 '\n'
                                 '-- Mascotas (ids 1..8). Rocky (3) y Kiara (8) estan INACTIVAS.\n'
                                 'INSERT INTO mascota (id_dueno, nombre, especie, fecha_nac, '
                                 'activa) VALUES\n'
                                 "  (1, 'Firulais', 'Canino', DATE '2019-04-12', 'S'),\n"
                                 "  (1, 'Luna',     'Felino', DATE '2021-08-30', 'S'),\n"
                                 "  (2, 'Rocky',    'Canino', DATE '2015-01-20', 'N'),\n"
                                 "  (3, 'Mishi',    'Felino', DATE '2022-11-05', 'S'),\n"
                                 "  (3, 'Bobby',    'Canino', DATE '2018-06-17', 'S'),\n"
                                 "  (4, 'Nube',     'Felino', DATE '2023-02-09', 'S'),\n"
                                 "  (5, 'Toby',     'Canino', DATE '2020-09-25', 'S'),\n"
                                 "  (6, 'Kiara',    'Canino', DATE '2013-03-03', 'N');\n"
                                 '\n'
                                 '-- Citas (ids 1..10)\n'
                                 'INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                 'estado) VALUES\n'
                                 "  (1, 1, TIMESTAMP '2026-09-01 08:00:00', 'PROGRAMADA'),\n"
                                 "  (2, 1, TIMESTAMP '2026-09-01 09:00:00', 'ATENDIDA'),\n"
                                 "  (4, 2, TIMESTAMP '2026-09-01 10:00:00', 'PROGRAMADA'),\n"
                                 "  (5, 3, TIMESTAMP '2026-09-02 08:30:00', 'CANCELADA'),\n"
                                 "  (6, 2, TIMESTAMP '2026-09-02 11:00:00', 'ATENDIDA'),\n"
                                 "  (7, 4, TIMESTAMP '2026-09-03 07:45:00', 'PROGRAMADA'),\n"
                                 "  (1, 1, TIMESTAMP '2026-09-05 15:00:00', 'ATENDIDA'),\n"
                                 "  (2, 3, TIMESTAMP '2026-09-08 16:00:00', 'PROGRAMADA'),\n"
                                 "  (4, 4, TIMESTAMP '2026-09-10 08:00:00', 'PROGRAMADA'),\n"
                                 "  (6, 1, TIMESTAMP '2026-09-10 09:00:00', 'ATENDIDA');\n"
                                 '\n'
                                 '-- Volumen con historia repartida entre 2025 y 2026 (para '
                                 'particionar)\n'
                                 'INSERT INTO dueno (nombre, telefono, email)\n'
                                 "SELECT 'Dueno ' || g, '300' || LPAD(g::text, 7, '0'), 'dueno' || "
                                 "g || '@mail.com'\n"
                                 'FROM generate_series(1, 800) AS g;\n'
                                 '\n'
                                 'INSERT INTO veterinario (nombre, especialidad)\n'
                                 "SELECT 'Veterinario ' || g, 'General'\n"
                                 'FROM generate_series(1, 10) AS g;\n'
                                 '\n'
                                 'INSERT INTO mascota (id_dueno, nombre, especie, activa)\n'
                                 "SELECT 1 + (g % 800), 'Mascota ' || g,\n"
                                 "       CASE WHEN g % 2 = 0 THEN 'Canino' ELSE 'Felino' END, 'S'\n"
                                 'FROM generate_series(1, 2000) AS g;\n'
                                 '\n'
                                 'INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                 'estado)\n'
                                 'SELECT 1 + (g % 2000),\n'
                                 '       1 + (g % 10),\n'
                                 "       TIMESTAMP '2025-01-06 08:00:00'\n"
                                 "         + ((g % 700) * INTERVAL '1 day')\n"
                                 "         + ((g % 8) * INTERVAL '1 hour'),\n"
                                 "       CASE WHEN g % 11 = 0 THEN 'CANCELADA'\n"
                                 "            WHEN g % 3 = 0 THEN 'ATENDIDA'\n"
                                 "            ELSE 'PROGRAMADA' END\n"
                                 'FROM generate_series(1, 5000) AS g;\n'
                                 '\n'
                                 'ANALYZE dueno;\n'
                                 'ANALYZE mascota;\n'
                                 'ANALYZE veterinario;\n'
                                 'ANALYZE cita;\n',
                    'tipo': 'bd_sql'},
                   {'correctas': [0, 2, 3, 5],
                    'enunciado': '## 4. Riesgos de sobre-indexar VetCare\n'
                                 '\n'
                                 'Alguien propone crear un indice sobre **cada** columna de '
                                 '`cita`, `mascota` y `factura` "por si acaso". Selecciona '
                                 '**todas** las afirmaciones correctas.',
                    'opciones': ['Cada indice adicional encarece INSERT, UPDATE y DELETE, porque '
                                 'el motor debe mantenerlo sincronizado con la tabla.',
                                 'Un indice sobre una columna de baja cardinalidad como estado, '
                                 'con solo 3 valores posibles, es siempre la mejor inversion.',
                                 'Los indices ocupan espacio en disco y en memoria cache, '
                                 'compitiendo con los datos que si se consultan.',
                                 "Un indice parcial (WHERE estado = 'PROGRAMADA') puede dar el "
                                 'mismo beneficio que uno completo ocupando una fraccion del '
                                 'tamano, cuando las consultas siempre traen ese filtro.',
                                 'Como las FOREIGN KEY crean su indice automaticamente en '
                                 'PostgreSQL, indexar id_dueno en mascota es redundante.',
                                 'Antes de crear un indice hay que tener la consulta concreta que '
                                 'lo va a usar y medir con EXPLAIN; indexar por intuicion produce '
                                 'indices muertos.'],
                    'puntos': 10,
                    'rubrica': '10 puntos con las 4 opciones correctas y ninguna incorrecta; '
                               'puntaje proporcional por acierto parcial. Correctas: indices 0, 2, '
                               '3 y 5.',
                    'tipo': 'cerrada_multi'},
                   {'enunciado': '## 5. Tabla de justificacion consulta -> indice\n'
                                 '\n'
                                 'Entrega la tabla de justificacion del entregable de la clase. '
                                 'Una fila por indice (minimo **3**, los que creaste en las '
                                 'preguntas 1 y 2), con estas columnas:\n'
                                 '\n'
                                 '| Indice | Tabla y columnas | Consulta del PI que lo usa | '
                                 'Cardinalidad estimada de la columna lider | Evidencia en EXPLAIN '
                                 '| Costo de mantenimiento | Veredicto |\n'
                                 '|---|---|---|---|---|---|---|\n'
                                 '\n'
                                 'Para cada indice explica:\n'
                                 '\n'
                                 '- **Cardinalidad**: si la columna lider tiene muchos valores '
                                 'distintos (`fecha_hora`, `id_dueno`) o pocos (`estado`), y como '
                                 'eso afecta la utilidad del indice.\n'
                                 '- **Evidencia**: el nodo concreto que viste en el plan (`Index '
                                 'Scan using idx_...`, `Bitmap Heap Scan`) y la caida de tiempo.\n'
                                 '- **Costo**: sobre que operaciones de escritura de VetCare pesa '
                                 '(por ejemplo, cada cita agendada mantiene los indices de '
                                 '`cita`).\n'
                                 '- **Veredicto**: se queda, se cambia por un indice parcial o '
                                 'compuesto, o se descarta.\n'
                                 '\n'
                                 'Cierra con dos parrafos cortos:\n'
                                 '\n'
                                 '1. **Regla de sobre-indexacion** que adoptas tu (por '
                                 'ejemplo: ningun indice sin consulta documentada y sin evidencia '
                                 'de `EXPLAIN`).\n'
                                 '2. **Particionamiento: veredicto para VetCare.** Con el volumen '
                                 'real que espera Huellitas, tiene sentido particionar `cita`? '
                                 'Justifica con numeros aproximados (citas por dia x dias de '
                                 'operacion) y reconoce que en ExamLab lo demostraste '
                                 'sintacticamente con 5.010 filas, volumen en el que la ganancia '
                                 'de rendimiento **no** es apreciable: el beneficio comprobado fue '
                                 'la **poda de particiones** en el plan y la facilidad de '
                                 'archivado, no la velocidad.',
                    'puntos': 20,
                    'rubrica': 'La tabla cubre al menos 3 indices con las 7 columnas, y cada fila '
                               'trae cardinalidad, evidencia real del plan, costo de escritura y '
                               'veredicto. La regla de sobre-indexacion es operativa y '
                               'verificable. El veredicto sobre particionamiento usa una '
                               'estimacion de volumen propia y reconoce explicitamente que con '
                               '5.010 filas la ganancia de rendimiento no es medible, '
                               'distinguiendo poda de particiones y archivado de la mejora de '
                               'velocidad.',
                    'tipo': 'abierta'}],
     'resumen': 'El estudiante crea y valida con EXPLAIN al menos tres indices sobre las tablas '
                'calientes de VetCare, construye una tabla historica particionada por rango de '
                'fecha y justifica cada indice frente al riesgo de sobre-indexar.',
     'titulo': 'Taller Clase 7 en ExamLab - Indices y particionamiento de VetCare'},
 8: {'preguntas': [{'enunciado': '## 1. sp_facturar: factura + detalle + descuento de stock, todo '
                                 'o nada\n'
                                 '\n'
                                 'Esquema completo de VetCare creado y poblado. Datos que '
                                 'necesitas:\n'
                                 '\n'
                                 '- Consultas registradas: `id_consulta` 1, 2, 3 y 4.\n'
                                 '- Facturas ya existentes: 1, 2 y 3 (de las consultas 1, 2 y 3).\n'
                                 '- Insumos: 1 Vacuna antirrabica **stock 12** ($22.000), 2 Vacuna '
                                 'triple felina **stock 3** ($31.000), 3 Antiparasitario oral '
                                 '**stock 40** ($9.500), 4 Suero fisiologico **stock 25** '
                                 '($7.000), 5 Gasa esteril **stock 8** ($1.200), 6 Jeringa 5ml '
                                 '**stock 60** ($900).\n'
                                 '\n'
                                 '**Crea el procedimiento** `sp_facturar(p_id_consulta INT, '
                                 'p_insumos INT[], p_cantidades INT[])` en PL/pgSQL que, de forma '
                                 '**atomica**:\n'
                                 '\n'
                                 '1. Valide que los dos arreglos tengan la misma longitud; si no, '
                                 '`RAISE EXCEPTION`.\n'
                                 '2. Inserte la cabecera en `factura (id_consulta, total)` con '
                                 'total `0` y recupere el id generado con `RETURNING id_factura '
                                 'INTO v_id_factura`.\n'
                                 '3. Recorra las lineas con `FOR i IN 1 .. array_length(p_insumos, '
                                 '1) LOOP`. Para **cada** linea:\n'
                                 '   - obtenga `precio_unit` del insumo (si el insumo no existe, '
                                 '`RAISE EXCEPTION`);\n'
                                 '   - descuente stock con el **patron de UPDATE condicional**:\n'
                                 '     ```sql\n'
                                 '     UPDATE insumo SET stock = stock - p_cantidades[i]\n'
                                 '      WHERE id_insumo = p_insumos[i] AND stock >= '
                                 'p_cantidades[i];\n'
                                 '     GET DIAGNOSTICS v_filas = ROW_COUNT;\n'
                                 "     IF v_filas = 0 THEN RAISE EXCEPTION 'ERROR: stock "
                                 "insuficiente del insumo %', p_insumos[i]; END IF;\n"
                                 '     ```\n'
                                 '   - inserte la linea en `detalle_factura` con el `precio_unit` '
                                 'vigente;\n'
                                 '   - acumule el total.\n'
                                 '4. Al final, `UPDATE factura SET total = v_total WHERE '
                                 'id_factura = v_id_factura;`\n'
                                 '\n'
                                 'Luego **ejecuta el caso exitoso**:\n'
                                 '\n'
                                 '```sql\n'
                                 'CALL sp_facturar(4, ARRAY[1, 6, 5], ARRAY[1, 2, 3]);\n'
                                 'SELECT f.id_factura, f.id_consulta, f.total FROM factura f ORDER '
                                 'BY f.id_factura;\n'
                                 'SELECT id_insumo, nombre, stock FROM insumo ORDER BY id_insumo;\n'
                                 '```\n'
                                 '\n'
                                 'El total esperado es `22000*1 + 900*2 + 1200*3 = 27.400`, y los '
                                 'stocks de los insumos 1, 6 y 5 deben bajar a 11, 58 y 5.\n'
                                 '\n'
                                 '**PostgreSQL:** no existe `SQL%ROWCOUNT`; se usa `GET '
                                 'DIAGNOSTICS v_filas = ROW_COUNT;`. Tampoco pongas `COMMIT` '
                                 'dentro del procedimiento: cada sentencia de nivel superior ya es '
                                 'su propia transaccion, y si el procedimiento lanza una excepcion '
                                 '**todo** lo que hizo se deshace.',
                    'puntos': 35,
                    'rubrica': 'El procedimiento se crea con la firma pedida y usa RETURNING ... '
                               'INTO, el bucle sobre los arreglos, el UPDATE condicional con GET '
                               'DIAGNOSTICS ROW_COUNT y RAISE EXCEPTION ante stock insuficiente. '
                               'La llamada exitosa crea la factura 4 con total 27.400 y deja los '
                               'stocks en 11, 58 y 5. No aparece COMMIT dentro del procedimiento '
                               'ni SQL%ROWCOUNT. Los SELECT finales evidencian el resultado.',
                    'setup_sql': 'CREATE TABLE dueno (\n'
                                 '  id_dueno SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  telefono TEXT,\n'
                                 '  email TEXT,\n'
                                 "  ciudad TEXT DEFAULT 'Cali'\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE mascota (\n'
                                 '  id_mascota SERIAL PRIMARY KEY,\n'
                                 '  id_dueno INT NOT NULL REFERENCES dueno(id_dueno),\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especie TEXT NOT NULL,\n'
                                 '  fecha_nac DATE,\n'
                                 "  activa CHAR(1) NOT NULL DEFAULT 'S' CHECK (activa IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE veterinario (\n'
                                 '  id_veterinario SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especialidad TEXT,\n'
                                 "  activo CHAR(1) NOT NULL DEFAULT 'S' CHECK (activo IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE cita (\n'
                                 '  id_cita SERIAL PRIMARY KEY,\n'
                                 '  id_mascota INT NOT NULL REFERENCES mascota(id_mascota),\n'
                                 '  id_veterinario INT NOT NULL REFERENCES '
                                 'veterinario(id_veterinario),\n'
                                 '  fecha_hora TIMESTAMP NOT NULL,\n'
                                 "  estado TEXT NOT NULL DEFAULT 'PROGRAMADA'\n"
                                 "    CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE consulta (\n'
                                 '  id_consulta SERIAL PRIMARY KEY,\n'
                                 '  id_cita INT NOT NULL UNIQUE REFERENCES cita(id_cita),\n'
                                 '  diagnostico TEXT,\n'
                                 '  precio NUMERIC(12,2) NOT NULL CHECK (precio >= 0)\n'
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE insumo (\n'
                                 '  id_insumo SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  stock INT NOT NULL CHECK (stock >= 0),\n'
                                 '  precio_unit NUMERIC(12,2) NOT NULL\n'
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE factura (\n'
                                 '  id_factura SERIAL PRIMARY KEY,\n'
                                 '  id_consulta INT NOT NULL REFERENCES consulta(id_consulta),\n'
                                 '  fecha TIMESTAMP NOT NULL DEFAULT now(),\n'
                                 '  total NUMERIC(12,2) NOT NULL DEFAULT 0\n'
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE detalle_factura (\n'
                                 '  id_detalle SERIAL PRIMARY KEY,\n'
                                 '  id_factura INT NOT NULL REFERENCES factura(id_factura) ON '
                                 'DELETE CASCADE,\n'
                                 '  id_insumo INT NOT NULL REFERENCES insumo(id_insumo),\n'
                                 '  cantidad INT NOT NULL CHECK (cantidad > 0),\n'
                                 '  precio_unit NUMERIC(12,2) NOT NULL\n'
                                 ');\n'
                                 '\n'
                                 '-- Duenos (ids 1..6 en este orden)\n'
                                 'INSERT INTO dueno (nombre, telefono, email) VALUES\n'
                                 "  ('Ana Gomez',      '3001112233', 'ana.gomez@mail.com'),\n"
                                 "  ('Carlos Ruiz',    '3014445566', 'carlos.ruiz@mail.com'),\n"
                                 "  ('Marcela Diaz',   '3027778899', 'marcela.diaz@mail.com'),\n"
                                 "  ('Jorge Pineda',   '3105551212', 'jorge.pineda@mail.com'),\n"
                                 "  ('Luisa Cardona',  '3123334455', 'luisa.cardona@mail.com'),\n"
                                 "  ('Andres Vallejo', '3159998877', 'andres.vallejo@mail.com');\n"
                                 '\n'
                                 '-- Veterinarios (ids 1..4)\n'
                                 'INSERT INTO veterinario (nombre, especialidad) VALUES\n'
                                 "  ('Laura Restrepo', 'General'),\n"
                                 "  ('Diego Moreno',   'Cirugia'),\n"
                                 "  ('Paula Salazar',  'Dermatologia'),\n"
                                 "  ('Ivan Ortiz',     'General');\n"
                                 '\n'
                                 '-- Mascotas (ids 1..8). Rocky (3) y Kiara (8) estan INACTIVAS.\n'
                                 'INSERT INTO mascota (id_dueno, nombre, especie, fecha_nac, '
                                 'activa) VALUES\n'
                                 "  (1, 'Firulais', 'Canino', DATE '2019-04-12', 'S'),\n"
                                 "  (1, 'Luna',     'Felino', DATE '2021-08-30', 'S'),\n"
                                 "  (2, 'Rocky',    'Canino', DATE '2015-01-20', 'N'),\n"
                                 "  (3, 'Mishi',    'Felino', DATE '2022-11-05', 'S'),\n"
                                 "  (3, 'Bobby',    'Canino', DATE '2018-06-17', 'S'),\n"
                                 "  (4, 'Nube',     'Felino', DATE '2023-02-09', 'S'),\n"
                                 "  (5, 'Toby',     'Canino', DATE '2020-09-25', 'S'),\n"
                                 "  (6, 'Kiara',    'Canino', DATE '2013-03-03', 'N');\n"
                                 '\n'
                                 '-- Citas (ids 1..10)\n'
                                 'INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                 'estado) VALUES\n'
                                 "  (1, 1, TIMESTAMP '2026-09-01 08:00:00', 'PROGRAMADA'),\n"
                                 "  (2, 1, TIMESTAMP '2026-09-01 09:00:00', 'ATENDIDA'),\n"
                                 "  (4, 2, TIMESTAMP '2026-09-01 10:00:00', 'PROGRAMADA'),\n"
                                 "  (5, 3, TIMESTAMP '2026-09-02 08:30:00', 'CANCELADA'),\n"
                                 "  (6, 2, TIMESTAMP '2026-09-02 11:00:00', 'ATENDIDA'),\n"
                                 "  (7, 4, TIMESTAMP '2026-09-03 07:45:00', 'PROGRAMADA'),\n"
                                 "  (1, 1, TIMESTAMP '2026-09-05 15:00:00', 'ATENDIDA'),\n"
                                 "  (2, 3, TIMESTAMP '2026-09-08 16:00:00', 'PROGRAMADA'),\n"
                                 "  (4, 4, TIMESTAMP '2026-09-10 08:00:00', 'PROGRAMADA'),\n"
                                 "  (6, 1, TIMESTAMP '2026-09-10 09:00:00', 'ATENDIDA');\n"
                                 '\n'
                                 '-- Consultas (ids 1..4) sobre las citas ATENDIDAS 2, 5, 7 y 10\n'
                                 'INSERT INTO consulta (id_cita, diagnostico, precio) VALUES\n'
                                 "  (2,  'Vacunacion triple felina', 40000),\n"
                                 "  (5,  'Control de peso',          38000),\n"
                                 "  (7,  'Otitis externa',           55000),\n"
                                 "  (10, 'Desparasitacion',          35000);\n"
                                 '\n'
                                 '-- Insumos (ids 1..6). Ojo: 2 y 5 tienen stock bajo a '
                                 'proposito.\n'
                                 'INSERT INTO insumo (nombre, stock, precio_unit) VALUES\n'
                                 "  ('Vacuna antirrabica',       12, 22000),\n"
                                 "  ('Vacuna triple felina',      3, 31000),\n"
                                 "  ('Antiparasitario oral',     40,  9500),\n"
                                 "  ('Suero fisiologico 500ml',  25,  7000),\n"
                                 "  ('Gasa esteril',              8,  1200),\n"
                                 "  ('Jeringa 5ml',              60,   900);\n"
                                 '\n'
                                 '-- Facturas (ids 1..3) y sus detalles\n'
                                 'INSERT INTO factura (id_consulta, fecha, total) VALUES\n'
                                 "  (1, TIMESTAMP '2026-09-01 09:40:00', 71000),\n"
                                 "  (2, TIMESTAMP '2026-09-02 11:35:00', 47000),\n"
                                 "  (3, TIMESTAMP '2026-09-05 15:50:00', 60200);\n"
                                 '\n'
                                 'INSERT INTO detalle_factura (id_factura, id_insumo, cantidad, '
                                 'precio_unit) VALUES\n'
                                 '  (1, 2, 1, 31000),\n'
                                 '  (1, 6, 1,   900),\n'
                                 '  (1, 3, 1,  9500),\n'
                                 '  (2, 3, 1,  9500),\n'
                                 '  (2, 4, 1,  7000),\n'
                                 '  (3, 1, 1, 22000),\n'
                                 '  (3, 5, 4,  1200),\n'
                                 '  (3, 6, 2,   900);\n',
                    'tipo': 'bd_sql'},
                   {'enunciado': '## 2. Probar la atomicidad: fallo a mitad de la factura\n'
                                 '\n'
                                 'En esta base **`sp_facturar(p_id_consulta INT, p_insumos INT[], '
                                 'p_cantidades INT[])` ya esta creado** (version de referencia), '
                                 'junto al esquema y los datos. Estado inicial relevante: '
                                 '`factura` tiene 3 filas, `detalle_factura` tiene 8, y el insumo '
                                 '2 (Vacuna triple felina) tiene **stock 3**.\n'
                                 '\n'
                                 'Escribe el SQL que demuestre la atomicidad:\n'
                                 '\n'
                                 '1. **Foto inicial**: una consulta que muestre en una sola fila '
                                 '`COUNT(*)` de `factura`, `COUNT(*)` de `detalle_factura` y el '
                                 '`stock` de los insumos 3 y 2. Guarda esos numeros; son tu punto '
                                 'de comparacion.\n'
                                 '2. **Intento que debe fallar a mitad de camino**, capturando la '
                                 'excepcion para que el script no se detenga:\n'
                                 '   ```sql\n'
                                 '   DO $$\n'
                                 '   BEGIN\n'
                                 '     CALL sp_facturar(4, ARRAY[3, 2], ARRAY[2, 10]);\n'
                                 "     RAISE NOTICE 'No deberia llegar aqui';\n"
                                 '   EXCEPTION WHEN OTHERS THEN\n'
                                 "     RAISE NOTICE 'Fallo esperado: %', SQLERRM;\n"
                                 '   END $$;\n'
                                 '   ```\n'
                                 '   La primera linea (2 unidades del insumo 3, que tiene 40) '
                                 '**si** alcanza; la segunda (10 unidades del insumo 2, que solo '
                                 'tiene 3) **no**.\n'
                                 '3. **Foto final**: repite exactamente la consulta del punto 1.\n'
                                 '4. Escribe como comentarios `--` la comparacion y la conclusion. '
                                 'Debe quedar demostrado que:\n'
                                 '   - **no** quedo una factura huerfana en `factura`,\n'
                                 '   - **no** quedo ninguna linea en `detalle_factura`,\n'
                                 '   - y sobre todo que el **stock del insumo 3 volvio a 40**: el '
                                 'descuento que si habia alcanzado se deshizo.\n'
                                 '5. Finalmente, **haz que la misma factura funcione** con una '
                                 'cantidad viable del insumo 2 (`CALL sp_facturar(4, ARRAY[3, 2], '
                                 'ARRAY[2, 3]);`) y muestra el resultado, evidenciando el '
                                 'contraste entre la transaccion abortada y la exitosa.',
                    'puntos': 25,
                    'rubrica': 'Se toman foto inicial y final con la misma consulta y se comparan '
                               'explicitamente. El intento invalido se captura sin abortar el '
                               'script y se demuestra con datos que factura y detalle_factura no '
                               'crecieron y que el stock del insumo 3 volvio a 40, es decir que la '
                               'operacion parcial se deshizo. La segunda llamada viable se ejecuta '
                               'y se muestra el contraste. Se descuenta si no se evidencia la '
                               'reversion del stock del primer insumo.',
                    'setup_sql': 'CREATE TABLE dueno (\n'
                                 '  id_dueno SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  telefono TEXT,\n'
                                 '  email TEXT,\n'
                                 "  ciudad TEXT DEFAULT 'Cali'\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE mascota (\n'
                                 '  id_mascota SERIAL PRIMARY KEY,\n'
                                 '  id_dueno INT NOT NULL REFERENCES dueno(id_dueno),\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especie TEXT NOT NULL,\n'
                                 '  fecha_nac DATE,\n'
                                 "  activa CHAR(1) NOT NULL DEFAULT 'S' CHECK (activa IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE veterinario (\n'
                                 '  id_veterinario SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especialidad TEXT,\n'
                                 "  activo CHAR(1) NOT NULL DEFAULT 'S' CHECK (activo IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE cita (\n'
                                 '  id_cita SERIAL PRIMARY KEY,\n'
                                 '  id_mascota INT NOT NULL REFERENCES mascota(id_mascota),\n'
                                 '  id_veterinario INT NOT NULL REFERENCES '
                                 'veterinario(id_veterinario),\n'
                                 '  fecha_hora TIMESTAMP NOT NULL,\n'
                                 "  estado TEXT NOT NULL DEFAULT 'PROGRAMADA'\n"
                                 "    CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE consulta (\n'
                                 '  id_consulta SERIAL PRIMARY KEY,\n'
                                 '  id_cita INT NOT NULL UNIQUE REFERENCES cita(id_cita),\n'
                                 '  diagnostico TEXT,\n'
                                 '  precio NUMERIC(12,2) NOT NULL CHECK (precio >= 0)\n'
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE insumo (\n'
                                 '  id_insumo SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  stock INT NOT NULL CHECK (stock >= 0),\n'
                                 '  precio_unit NUMERIC(12,2) NOT NULL\n'
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE factura (\n'
                                 '  id_factura SERIAL PRIMARY KEY,\n'
                                 '  id_consulta INT NOT NULL REFERENCES consulta(id_consulta),\n'
                                 '  fecha TIMESTAMP NOT NULL DEFAULT now(),\n'
                                 '  total NUMERIC(12,2) NOT NULL DEFAULT 0\n'
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE detalle_factura (\n'
                                 '  id_detalle SERIAL PRIMARY KEY,\n'
                                 '  id_factura INT NOT NULL REFERENCES factura(id_factura) ON '
                                 'DELETE CASCADE,\n'
                                 '  id_insumo INT NOT NULL REFERENCES insumo(id_insumo),\n'
                                 '  cantidad INT NOT NULL CHECK (cantidad > 0),\n'
                                 '  precio_unit NUMERIC(12,2) NOT NULL\n'
                                 ');\n'
                                 '\n'
                                 '-- Duenos (ids 1..6 en este orden)\n'
                                 'INSERT INTO dueno (nombre, telefono, email) VALUES\n'
                                 "  ('Ana Gomez',      '3001112233', 'ana.gomez@mail.com'),\n"
                                 "  ('Carlos Ruiz',    '3014445566', 'carlos.ruiz@mail.com'),\n"
                                 "  ('Marcela Diaz',   '3027778899', 'marcela.diaz@mail.com'),\n"
                                 "  ('Jorge Pineda',   '3105551212', 'jorge.pineda@mail.com'),\n"
                                 "  ('Luisa Cardona',  '3123334455', 'luisa.cardona@mail.com'),\n"
                                 "  ('Andres Vallejo', '3159998877', 'andres.vallejo@mail.com');\n"
                                 '\n'
                                 '-- Veterinarios (ids 1..4)\n'
                                 'INSERT INTO veterinario (nombre, especialidad) VALUES\n'
                                 "  ('Laura Restrepo', 'General'),\n"
                                 "  ('Diego Moreno',   'Cirugia'),\n"
                                 "  ('Paula Salazar',  'Dermatologia'),\n"
                                 "  ('Ivan Ortiz',     'General');\n"
                                 '\n'
                                 '-- Mascotas (ids 1..8). Rocky (3) y Kiara (8) estan INACTIVAS.\n'
                                 'INSERT INTO mascota (id_dueno, nombre, especie, fecha_nac, '
                                 'activa) VALUES\n'
                                 "  (1, 'Firulais', 'Canino', DATE '2019-04-12', 'S'),\n"
                                 "  (1, 'Luna',     'Felino', DATE '2021-08-30', 'S'),\n"
                                 "  (2, 'Rocky',    'Canino', DATE '2015-01-20', 'N'),\n"
                                 "  (3, 'Mishi',    'Felino', DATE '2022-11-05', 'S'),\n"
                                 "  (3, 'Bobby',    'Canino', DATE '2018-06-17', 'S'),\n"
                                 "  (4, 'Nube',     'Felino', DATE '2023-02-09', 'S'),\n"
                                 "  (5, 'Toby',     'Canino', DATE '2020-09-25', 'S'),\n"
                                 "  (6, 'Kiara',    'Canino', DATE '2013-03-03', 'N');\n"
                                 '\n'
                                 '-- Citas (ids 1..10)\n'
                                 'INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                 'estado) VALUES\n'
                                 "  (1, 1, TIMESTAMP '2026-09-01 08:00:00', 'PROGRAMADA'),\n"
                                 "  (2, 1, TIMESTAMP '2026-09-01 09:00:00', 'ATENDIDA'),\n"
                                 "  (4, 2, TIMESTAMP '2026-09-01 10:00:00', 'PROGRAMADA'),\n"
                                 "  (5, 3, TIMESTAMP '2026-09-02 08:30:00', 'CANCELADA'),\n"
                                 "  (6, 2, TIMESTAMP '2026-09-02 11:00:00', 'ATENDIDA'),\n"
                                 "  (7, 4, TIMESTAMP '2026-09-03 07:45:00', 'PROGRAMADA'),\n"
                                 "  (1, 1, TIMESTAMP '2026-09-05 15:00:00', 'ATENDIDA'),\n"
                                 "  (2, 3, TIMESTAMP '2026-09-08 16:00:00', 'PROGRAMADA'),\n"
                                 "  (4, 4, TIMESTAMP '2026-09-10 08:00:00', 'PROGRAMADA'),\n"
                                 "  (6, 1, TIMESTAMP '2026-09-10 09:00:00', 'ATENDIDA');\n"
                                 '\n'
                                 '-- Consultas (ids 1..4) sobre las citas ATENDIDAS 2, 5, 7 y 10\n'
                                 'INSERT INTO consulta (id_cita, diagnostico, precio) VALUES\n'
                                 "  (2,  'Vacunacion triple felina', 40000),\n"
                                 "  (5,  'Control de peso',          38000),\n"
                                 "  (7,  'Otitis externa',           55000),\n"
                                 "  (10, 'Desparasitacion',          35000);\n"
                                 '\n'
                                 '-- Insumos (ids 1..6). Ojo: 2 y 5 tienen stock bajo a '
                                 'proposito.\n'
                                 'INSERT INTO insumo (nombre, stock, precio_unit) VALUES\n'
                                 "  ('Vacuna antirrabica',       12, 22000),\n"
                                 "  ('Vacuna triple felina',      3, 31000),\n"
                                 "  ('Antiparasitario oral',     40,  9500),\n"
                                 "  ('Suero fisiologico 500ml',  25,  7000),\n"
                                 "  ('Gasa esteril',              8,  1200),\n"
                                 "  ('Jeringa 5ml',              60,   900);\n"
                                 '\n'
                                 '-- Facturas (ids 1..3) y sus detalles\n'
                                 'INSERT INTO factura (id_consulta, fecha, total) VALUES\n'
                                 "  (1, TIMESTAMP '2026-09-01 09:40:00', 71000),\n"
                                 "  (2, TIMESTAMP '2026-09-02 11:35:00', 47000),\n"
                                 "  (3, TIMESTAMP '2026-09-05 15:50:00', 60200);\n"
                                 '\n'
                                 'INSERT INTO detalle_factura (id_factura, id_insumo, cantidad, '
                                 'precio_unit) VALUES\n'
                                 '  (1, 2, 1, 31000),\n'
                                 '  (1, 6, 1,   900),\n'
                                 '  (1, 3, 1,  9500),\n'
                                 '  (2, 3, 1,  9500),\n'
                                 '  (2, 4, 1,  7000),\n'
                                 '  (3, 1, 1, 22000),\n'
                                 '  (3, 5, 4,  1200),\n'
                                 '  (3, 6, 2,   900);\n'
                                 '\n'
                                 'CREATE PROCEDURE sp_facturar(\n'
                                 '  p_id_consulta INT,\n'
                                 '  p_insumos     INT[],\n'
                                 '  p_cantidades  INT[]\n'
                                 ')\n'
                                 'LANGUAGE plpgsql\n'
                                 'AS $proc$\n'
                                 'DECLARE\n'
                                 '  v_id_factura INT;\n'
                                 '  v_total NUMERIC(12,2) := 0;\n'
                                 '  v_precio NUMERIC(12,2);\n'
                                 '  v_filas INT;\n'
                                 '  i INT;\n'
                                 'BEGIN\n'
                                 '  IF array_length(p_insumos, 1) IS DISTINCT FROM '
                                 'array_length(p_cantidades, 1) THEN\n'
                                 "    RAISE EXCEPTION 'ERROR: insumos y cantidades deben tener la "
                                 "misma longitud';\n"
                                 '  END IF;\n'
                                 '\n'
                                 '  INSERT INTO factura (id_consulta, total) VALUES '
                                 '(p_id_consulta, 0)\n'
                                 '  RETURNING id_factura INTO v_id_factura;\n'
                                 '\n'
                                 '  FOR i IN 1 .. array_length(p_insumos, 1) LOOP\n'
                                 '    SELECT precio_unit INTO v_precio FROM insumo WHERE id_insumo '
                                 '= p_insumos[i];\n'
                                 '    IF NOT FOUND THEN\n'
                                 "      RAISE EXCEPTION 'ERROR: el insumo % no existe', "
                                 'p_insumos[i];\n'
                                 '    END IF;\n'
                                 '\n'
                                 '    UPDATE insumo\n'
                                 '       SET stock = stock - p_cantidades[i]\n'
                                 '     WHERE id_insumo = p_insumos[i]\n'
                                 '       AND stock >= p_cantidades[i];\n'
                                 '    GET DIAGNOSTICS v_filas = ROW_COUNT;\n'
                                 '    IF v_filas = 0 THEN\n'
                                 "      RAISE EXCEPTION 'ERROR: stock insuficiente del insumo % "
                                 "(se pidieron %)',\n"
                                 '        p_insumos[i], p_cantidades[i];\n'
                                 '    END IF;\n'
                                 '\n'
                                 '    INSERT INTO detalle_factura (id_factura, id_insumo, '
                                 'cantidad, precio_unit)\n'
                                 '    VALUES (v_id_factura, p_insumos[i], p_cantidades[i], '
                                 'v_precio);\n'
                                 '\n'
                                 '    v_total := v_total + (v_precio * p_cantidades[i]);\n'
                                 '  END LOOP;\n'
                                 '\n'
                                 '  UPDATE factura SET total = v_total WHERE id_factura = '
                                 'v_id_factura;\n'
                                 "  RAISE NOTICE 'Factura % creada por %', v_id_factura, v_total;\n"
                                 'END;\n'
                                 '$proc$;\n',
                    'tipo': 'bd_sql'},
                   {'enunciado': '## 3. El patron de descuento seguro como funcion reutilizable\n'
                                 '\n'
                                 'Mismo esquema y datos (insumo 2 con stock 3, insumo 5 con stock '
                                 '8).\n'
                                 '\n'
                                 'Encapsula el patron de descuento en una funcion reutilizable:\n'
                                 '\n'
                                 '1. Crea `fn_descontar_stock(p_id_insumo INT, p_cantidad INT)` '
                                 'que **retorne** `BOOLEAN` y:\n'
                                 '   - valide `p_cantidad > 0` (si no, `RAISE EXCEPTION`);\n'
                                 '   - ejecute el `UPDATE insumo SET stock = stock - p_cantidad '
                                 'WHERE id_insumo = p_id_insumo AND stock >= p_cantidad;`\n'
                                 '   - obtenga las filas afectadas con `GET DIAGNOSTICS v_filas = '
                                 'ROW_COUNT;`\n'
                                 '   - retorne `TRUE` si `v_filas = 1` y `FALSE` si `v_filas = 0` '
                                 '(**sin** lanzar excepcion: aqui el "no hay stock" es una '
                                 'respuesta, no un error).\n'
                                 '2. Pruebala en una sola consulta que devuelva las tres '
                                 'respuestas en columnas:\n'
                                 '   ```sql\n'
                                 '   SELECT fn_descontar_stock(5, 3) AS caso_ok,\n'
                                 '          fn_descontar_stock(2, 10) AS caso_sin_stock,\n'
                                 '          fn_descontar_stock(2, 3)  AS caso_limite;\n'
                                 '   ```\n'
                                 '   Esperado: `true`, `false`, `true`.\n'
                                 '3. Muestra `SELECT id_insumo, nombre, stock FROM insumo ORDER BY '
                                 'id_insumo;` y confirma que **ningun** stock quedo negativo '
                                 '(insumo 5 en 5, insumo 2 en 0).\n'
                                 '4. Explica en un comentario `--` la diferencia clave entre este '
                                 'patron y `SELECT stock ... ; IF stock >= cantidad THEN UPDATE '
                                 '...`: por que leer primero y decidir despues es inseguro cuando '
                                 'hay varios usuarios facturando a la vez, y por que el `UPDATE` '
                                 'con la condicion en el `WHERE` resuelve la comprobacion y la '
                                 'escritura en **una sola** sentencia atomica.',
                    'puntos': 15,
                    'rubrica': 'La funcion retorna BOOLEAN, valida cantidad positiva, usa el '
                               'UPDATE condicional con GET DIAGNOSTICS y devuelve FALSE en vez de '
                               'excepcion cuando no hay stock. La consulta de prueba arroja '
                               'true/false/true y el estado final deja el insumo 5 en 5 y el 2 en '
                               '0, sin negativos. El comentario explica correctamente por que el '
                               'patron leer-luego-decidir es vulnerable y por que la condicion en '
                               'el WHERE lo evita.',
                    'setup_sql': 'CREATE TABLE dueno (\n'
                                 '  id_dueno SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  telefono TEXT,\n'
                                 '  email TEXT,\n'
                                 "  ciudad TEXT DEFAULT 'Cali'\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE mascota (\n'
                                 '  id_mascota SERIAL PRIMARY KEY,\n'
                                 '  id_dueno INT NOT NULL REFERENCES dueno(id_dueno),\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especie TEXT NOT NULL,\n'
                                 '  fecha_nac DATE,\n'
                                 "  activa CHAR(1) NOT NULL DEFAULT 'S' CHECK (activa IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE veterinario (\n'
                                 '  id_veterinario SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  especialidad TEXT,\n'
                                 "  activo CHAR(1) NOT NULL DEFAULT 'S' CHECK (activo IN "
                                 "('S','N'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE cita (\n'
                                 '  id_cita SERIAL PRIMARY KEY,\n'
                                 '  id_mascota INT NOT NULL REFERENCES mascota(id_mascota),\n'
                                 '  id_veterinario INT NOT NULL REFERENCES '
                                 'veterinario(id_veterinario),\n'
                                 '  fecha_hora TIMESTAMP NOT NULL,\n'
                                 "  estado TEXT NOT NULL DEFAULT 'PROGRAMADA'\n"
                                 "    CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))\n"
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE consulta (\n'
                                 '  id_consulta SERIAL PRIMARY KEY,\n'
                                 '  id_cita INT NOT NULL UNIQUE REFERENCES cita(id_cita),\n'
                                 '  diagnostico TEXT,\n'
                                 '  precio NUMERIC(12,2) NOT NULL CHECK (precio >= 0)\n'
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE insumo (\n'
                                 '  id_insumo SERIAL PRIMARY KEY,\n'
                                 '  nombre TEXT NOT NULL,\n'
                                 '  stock INT NOT NULL CHECK (stock >= 0),\n'
                                 '  precio_unit NUMERIC(12,2) NOT NULL\n'
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE factura (\n'
                                 '  id_factura SERIAL PRIMARY KEY,\n'
                                 '  id_consulta INT NOT NULL REFERENCES consulta(id_consulta),\n'
                                 '  fecha TIMESTAMP NOT NULL DEFAULT now(),\n'
                                 '  total NUMERIC(12,2) NOT NULL DEFAULT 0\n'
                                 ');\n'
                                 '\n'
                                 'CREATE TABLE detalle_factura (\n'
                                 '  id_detalle SERIAL PRIMARY KEY,\n'
                                 '  id_factura INT NOT NULL REFERENCES factura(id_factura) ON '
                                 'DELETE CASCADE,\n'
                                 '  id_insumo INT NOT NULL REFERENCES insumo(id_insumo),\n'
                                 '  cantidad INT NOT NULL CHECK (cantidad > 0),\n'
                                 '  precio_unit NUMERIC(12,2) NOT NULL\n'
                                 ');\n'
                                 '\n'
                                 '-- Duenos (ids 1..6 en este orden)\n'
                                 'INSERT INTO dueno (nombre, telefono, email) VALUES\n'
                                 "  ('Ana Gomez',      '3001112233', 'ana.gomez@mail.com'),\n"
                                 "  ('Carlos Ruiz',    '3014445566', 'carlos.ruiz@mail.com'),\n"
                                 "  ('Marcela Diaz',   '3027778899', 'marcela.diaz@mail.com'),\n"
                                 "  ('Jorge Pineda',   '3105551212', 'jorge.pineda@mail.com'),\n"
                                 "  ('Luisa Cardona',  '3123334455', 'luisa.cardona@mail.com'),\n"
                                 "  ('Andres Vallejo', '3159998877', 'andres.vallejo@mail.com');\n"
                                 '\n'
                                 '-- Veterinarios (ids 1..4)\n'
                                 'INSERT INTO veterinario (nombre, especialidad) VALUES\n'
                                 "  ('Laura Restrepo', 'General'),\n"
                                 "  ('Diego Moreno',   'Cirugia'),\n"
                                 "  ('Paula Salazar',  'Dermatologia'),\n"
                                 "  ('Ivan Ortiz',     'General');\n"
                                 '\n'
                                 '-- Mascotas (ids 1..8). Rocky (3) y Kiara (8) estan INACTIVAS.\n'
                                 'INSERT INTO mascota (id_dueno, nombre, especie, fecha_nac, '
                                 'activa) VALUES\n'
                                 "  (1, 'Firulais', 'Canino', DATE '2019-04-12', 'S'),\n"
                                 "  (1, 'Luna',     'Felino', DATE '2021-08-30', 'S'),\n"
                                 "  (2, 'Rocky',    'Canino', DATE '2015-01-20', 'N'),\n"
                                 "  (3, 'Mishi',    'Felino', DATE '2022-11-05', 'S'),\n"
                                 "  (3, 'Bobby',    'Canino', DATE '2018-06-17', 'S'),\n"
                                 "  (4, 'Nube',     'Felino', DATE '2023-02-09', 'S'),\n"
                                 "  (5, 'Toby',     'Canino', DATE '2020-09-25', 'S'),\n"
                                 "  (6, 'Kiara',    'Canino', DATE '2013-03-03', 'N');\n"
                                 '\n'
                                 '-- Citas (ids 1..10)\n'
                                 'INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                 'estado) VALUES\n'
                                 "  (1, 1, TIMESTAMP '2026-09-01 08:00:00', 'PROGRAMADA'),\n"
                                 "  (2, 1, TIMESTAMP '2026-09-01 09:00:00', 'ATENDIDA'),\n"
                                 "  (4, 2, TIMESTAMP '2026-09-01 10:00:00', 'PROGRAMADA'),\n"
                                 "  (5, 3, TIMESTAMP '2026-09-02 08:30:00', 'CANCELADA'),\n"
                                 "  (6, 2, TIMESTAMP '2026-09-02 11:00:00', 'ATENDIDA'),\n"
                                 "  (7, 4, TIMESTAMP '2026-09-03 07:45:00', 'PROGRAMADA'),\n"
                                 "  (1, 1, TIMESTAMP '2026-09-05 15:00:00', 'ATENDIDA'),\n"
                                 "  (2, 3, TIMESTAMP '2026-09-08 16:00:00', 'PROGRAMADA'),\n"
                                 "  (4, 4, TIMESTAMP '2026-09-10 08:00:00', 'PROGRAMADA'),\n"
                                 "  (6, 1, TIMESTAMP '2026-09-10 09:00:00', 'ATENDIDA');\n"
                                 '\n'
                                 '-- Consultas (ids 1..4) sobre las citas ATENDIDAS 2, 5, 7 y 10\n'
                                 'INSERT INTO consulta (id_cita, diagnostico, precio) VALUES\n'
                                 "  (2,  'Vacunacion triple felina', 40000),\n"
                                 "  (5,  'Control de peso',          38000),\n"
                                 "  (7,  'Otitis externa',           55000),\n"
                                 "  (10, 'Desparasitacion',          35000);\n"
                                 '\n'
                                 '-- Insumos (ids 1..6). Ojo: 2 y 5 tienen stock bajo a '
                                 'proposito.\n'
                                 'INSERT INTO insumo (nombre, stock, precio_unit) VALUES\n'
                                 "  ('Vacuna antirrabica',       12, 22000),\n"
                                 "  ('Vacuna triple felina',      3, 31000),\n"
                                 "  ('Antiparasitario oral',     40,  9500),\n"
                                 "  ('Suero fisiologico 500ml',  25,  7000),\n"
                                 "  ('Gasa esteril',              8,  1200),\n"
                                 "  ('Jeringa 5ml',              60,   900);\n"
                                 '\n'
                                 '-- Facturas (ids 1..3) y sus detalles\n'
                                 'INSERT INTO factura (id_consulta, fecha, total) VALUES\n'
                                 "  (1, TIMESTAMP '2026-09-01 09:40:00', 71000),\n"
                                 "  (2, TIMESTAMP '2026-09-02 11:35:00', 47000),\n"
                                 "  (3, TIMESTAMP '2026-09-05 15:50:00', 60200);\n"
                                 '\n'
                                 'INSERT INTO detalle_factura (id_factura, id_insumo, cantidad, '
                                 'precio_unit) VALUES\n'
                                 '  (1, 2, 1, 31000),\n'
                                 '  (1, 6, 1,   900),\n'
                                 '  (1, 3, 1,  9500),\n'
                                 '  (2, 3, 1,  9500),\n'
                                 '  (2, 4, 1,  7000),\n'
                                 '  (3, 1, 1, 22000),\n'
                                 '  (3, 5, 4,  1200),\n'
                                 '  (3, 6, 2,   900);\n',
                    'tipo': 'bd_sql'},
                   {'correctas': [2],
                    'enunciado': '## 4. Que pasa con el bloque EXCEPTION en PL/pgSQL\n'
                                 '\n'
                                 'En la pregunta 2 el `CALL sp_facturar(...)` fallo despues de '
                                 'haber insertado la cabecera de la factura y de haber descontado '
                                 'el stock del primer insumo, y sin embargo la base quedo '
                                 'exactamente como antes.\n'
                                 '\n'
                                 'Cual es la explicacion correcta en PostgreSQL?',
                    'opciones': ['Porque el procedimiento incluia un ROLLBACK explicito en su '
                                 'bloque EXCEPTION, igual que en Oracle.',
                                 'Porque PostgreSQL guarda automaticamente una copia de seguridad '
                                 'de cada tabla antes de cada CALL.',
                                 'Porque la sentencia CALL de nivel superior es su propia '
                                 'transaccion: al propagarse la excepcion, todo el trabajo hecho '
                                 'dentro del procedimiento se deshace. Ademas, un bloque BEGIN ... '
                                 'EXCEPTION en PL/pgSQL crea un savepoint implicito, asi que al '
                                 'capturar el error se revierte solo lo hecho dentro de ese '
                                 'bloque.',
                                 'Porque los UPDATE sobre insumo no se aplican hasta que el '
                                 'procedimiento termina; PL/pgSQL los acumula en memoria y los '
                                 'escribe al final.',
                                 'Porque el trigger de stock deshizo los cambios anteriores al '
                                 'detectar la excepcion.'],
                    'puntos': 10,
                    'rubrica': '10 puntos si marca la opcion 2 (indice 2). Cualquier otra '
                               'respuesta, 0.',
                    'tipo': 'cerrada'},
                   {'enunciado': '## 5. Checklist de tuning y transacciones del PI\n'
                                 '\n'
                                 'Entrega la seccion "Transacciones y tuning" del informe del PI '
                                 '(una pagina), con:\n'
                                 '\n'
                                 '1. **Inventario de transacciones de negocio de VetCare**: al '
                                 'menos **tres** operaciones que deben ser todo-o-nada (facturar y '
                                 'descontar stock, registrar consulta y cerrar cita, cancelar cita '
                                 'y liberar franja, ...). Para cada una: que tablas toca, cual es '
                                 'el paso que puede fallar y que debe pasar si falla.\n'
                                 '2. **Checklist de tuning**, con estado (`listo` / `parcial` / '
                                 '`pendiente`) y evidencia para cada item:\n'
                                 '   - [ ] indices creados sobre las columnas de filtro y join de '
                                 'las consultas frecuentes\n'
                                 '   - [ ] consultas sin `SELECT *` en los reportes del PI\n'
                                 '   - [ ] predicados sargables (sin funciones sobre columnas '
                                 'filtradas)\n'
                                 '   - [ ] transacciones cortas: nada de esperar entrada del '
                                 'usuario con la transaccion abierta\n'
                                 '   - [ ] validaciones criticas en la base (`CHECK`, trigger, '
                                 'procedimiento), no solo en la aplicacion\n'
                                 '   - [ ] `ANALYZE` / estadisticas al dia despues de cargas '
                                 'masivas\n'
                                 '   - [ ] plan de respaldo con restore probado (viene de la Clase '
                                 '4)\n'
                                 '3. **Decision documentada**: por que el descuento de stock se '
                                 'hace con `UPDATE ... WHERE stock >= cantidad` y no leyendo '
                                 'primero. Escribe la conclusion en una frase que puedas defender '
                                 'en la sustentacion.\n'
                                 '4. **Gap honesto**: que no pudiste comprobar en ExamLab porque '
                                 'PostgreSQL en el navegador corre con **una sola sesion** (por '
                                 'ejemplo el comportamiento con dos recepcionistas facturando el '
                                 'mismo insumo al mismo tiempo) y como lo abordaras en la Clase '
                                 '10.',
                    'puntos': 15,
                    'rubrica': 'El inventario trae al menos 3 transacciones con tablas, punto de '
                               'fallo y comportamiento esperado ante el fallo. El checklist tiene '
                               'los 7 items con estado y evidencia concreta (nombre de indice, '
                               'archivo, consulta), no solo casillas marcadas. La decision sobre '
                               'el UPDATE condicional esta bien argumentada y el gap de '
                               'concurrencia se reconoce explicitamente con su plan de abordaje.',
                    'tipo': 'abierta'}],
     'resumen': 'El estudiante implementa la transaccion atomica de facturacion que descuenta '
                'stock, demuestra el rollback cuando el stock es insuficiente y entrega el '
                'checklist de tuning del PI.',
     'titulo': 'Taller Clase 8 en ExamLab - Transacciones de facturacion y tuning de VetCare'},
 10: {'preguntas': [{'enunciado': '## 1. Escenario de doble reserva con linea de tiempo T1/T2\n'
                                  '\n'
                                  '**Clase autonoma: no hay docente en vivo, asi que sigue el '
                                  'guion al pie de la letra.**\n'
                                  '\n'
                                  'En Huellitas hay **dos recepcionistas** atendiendo el telefono '
                                  'al mismo tiempo. Ambas quieren agendar una cita con la '
                                  '**veterinaria Laura Restrepo (id 1)** el **2026-10-12 a las '
                                  '09:00**. Una llama por Firulais (mascota 1) y la otra por Luna '
                                  '(mascota 2).\n'
                                  '\n'
                                  'El procedimiento `sp_agendar_cita` valida asi: primero hace '
                                  '`SELECT COUNT(*) FROM cita WHERE id_veterinario = 1 AND '
                                  "fecha_hora = '2026-10-12 09:00' AND estado <> 'CANCELADA'`, y "
                                  'si el conteo es 0, inserta.\n'
                                  '\n'
                                  '**Redacta el escenario como una linea de tiempo**, con una '
                                  'tabla de al menos **6 pasos** y estas columnas:\n'
                                  '\n'
                                  '| Momento | Transaccion T1 (Recepcion A) | Transaccion T2 '
                                  '(Recepcion B) | Estado de la tabla cita | Comentario |\n'
                                  '|---|---|---|---|---|\n'
                                  '\n'
                                  'Debe quedar explicito el momento exacto en que **las dos** '
                                  'transacciones leyeron `COUNT(*) = 0` antes de que cualquiera '
                                  'insertara, y por que ninguna de las dos validaciones detecto el '
                                  'conflicto.\n'
                                  '\n'
                                  'Luego responde, en 3 a 5 lineas cada punto:\n'
                                  '\n'
                                  '1. **Nombre de la anomalia**: como se llama este fenomeno en la '
                                  'teoria de concurrencia y por que el nivel de aislamiento `READ '
                                  'COMMITTED` (el predeterminado de PostgreSQL) **no** lo evita.\n'
                                  '2. **Que pasaria** en el negocio si esto ocurre: impacto para '
                                  'la clinica, la veterinaria y los dos duenos.\n'
                                  '3. **Tres mitigaciones posibles**, de la mas fuerte a la mas '
                                  'debil: (a) restriccion `UNIQUE` sobre `(id_veterinario, '
                                  'fecha_hora)`, (b) `SELECT ... FOR UPDATE` sobre la fila del '
                                  'veterinario o de la franja antes de validar, (c) `SET '
                                  'TRANSACTION ISOLATION LEVEL SERIALIZABLE` con reintento en la '
                                  'aplicacion. Para cada una: que garantiza, que cuesta y que debe '
                                  'hacer la aplicacion cuando la base rechace la operacion.',
                     'puntos': 25,
                     'rubrica': 'La linea de tiempo tiene al menos 6 pasos e identifica con '
                                'precision el intervalo en que ambas transacciones leyeron '
                                'COUNT(*) = 0 antes de insertar. Se nombra correctamente la '
                                'anomalia (lectura fantasma / write skew sobre un predicado) y se '
                                'explica por que READ COMMITTED no la evita. Las 3 mitigaciones se '
                                'presentan con garantia, costo y accion de la aplicacion, '
                                'ordenadas por fortaleza. Se descuenta si la narrativa no '
                                'distingue el instante de la lectura del de la escritura.',
                     'tipo': 'abierta'},
                    {'enunciado': '## 2. Reproducir la doble reserva y cerrarla con una '
                                  'restriccion\n'
                                  '\n'
                                  '**Limite del entorno que debes tener presente:** ExamLab '
                                  'ejecuta PostgreSQL **real** en el navegador, pero con **una '
                                  'sola sesion**. No puedes abrir dos conexiones y ver a T2 '
                                  'bloqueada esperando a T1. Lo que **si** puedes hacer, y es lo '
                                  'que se te pide, es demostrar que sin restriccion la base '
                                  '**acepta** el dato invalido, y que con la restriccion correcta '
                                  'lo **rechaza** siempre, sin importar el orden ni la velocidad '
                                  'de las transacciones. Esa es la mitigacion estructural.\n'
                                  '\n'
                                  'La base trae `cita` **sin** ninguna restriccion de unicidad de '
                                  'franja, mas una tabla `evidencia (id_evidencia SERIAL, paso '
                                  'TEXT, resultado TEXT)`.\n'
                                  '\n'
                                  'Escribe el SQL que, en este orden:\n'
                                  '\n'
                                  '1. **Muestre el problema.** Inserta las dos citas del escenario '
                                  'de la pregunta 1:\n'
                                  "   - `(id_mascota 1, id_veterinario 1, '2026-10-12 09:00:00', "
                                  "'PROGRAMADA')`\n"
                                  "   - `(id_mascota 2, id_veterinario 1, '2026-10-12 09:00:00', "
                                  "'PROGRAMADA')`\n"
                                  '   Ambas se insertan **sin error**. Registra en `evidencia` el '
                                  "paso `'sin restriccion'` con el resultado.\n"
                                  '2. **Evidencie el dato invalido** con una consulta de '
                                  'deteccion:\n'
                                  '   `SELECT id_veterinario, fecha_hora, COUNT(*) AS '
                                  "citas_en_la_misma_franja FROM cita WHERE estado <> 'CANCELADA' "
                                  'GROUP BY id_veterinario, fecha_hora HAVING COUNT(*) > 1;`\n'
                                  '   Debe devolver la franja duplicada.\n'
                                  '3. **Limpie el duplicado** (borra una de las dos citas recien '
                                  'creadas, la de mayor `id_cita`).\n'
                                  '4. **Aplique la mitigacion**: un **indice unico parcial**, que '
                                  'es la forma correcta aqui porque las citas canceladas si pueden '
                                  'repetir franja:\n'
                                  '   `CREATE UNIQUE INDEX uq_cita_vet_franja ON cita '
                                  "(id_veterinario, fecha_hora) WHERE estado <> 'CANCELADA';`\n"
                                  '5. **Pruebe que ahora la base rechaza el conflicto**, '
                                  'capturando el error para que el script no se detenga:\n'
                                  '   ```sql\n'
                                  '   DO $$\n'
                                  '   BEGIN\n'
                                  '     INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                  'estado)\n'
                                  "     VALUES (4, 1, TIMESTAMP '2026-10-12 09:00:00', "
                                  "'PROGRAMADA');\n"
                                  "     INSERT INTO evidencia (paso, resultado) VALUES ('con "
                                  "restriccion', 'FALLO: se permitio la doble reserva');\n"
                                  '   EXCEPTION WHEN unique_violation THEN\n'
                                  "     INSERT INTO evidencia (paso, resultado) VALUES ('con "
                                  "restriccion', 'OK rechazada: ' || SQLERRM);\n"
                                  '   END $$;\n'
                                  '   ```\n'
                                  '6. **Pruebe que la excepcion es correcta**, no excesiva: '
                                  "inserta la **misma franja** pero con estado `'CANCELADA'`, que "
                                  '**debe** ser aceptada por el indice parcial. Registra el '
                                  'resultado en `evidencia`.\n'
                                  '7. Cierre con `SELECT paso, resultado FROM evidencia ORDER BY '
                                  'id_evidencia;` y con la consulta de deteccion del paso 2, que '
                                  'ahora debe devolver **cero filas**.',
                     'puntos': 25,
                     'rubrica': 'Se demuestra primero que sin restriccion la doble reserva se '
                                'inserta sin error y la consulta de deteccion la encuentra. Se '
                                'crea el indice unico PARCIAL sobre (id_veterinario, fecha_hora) '
                                "con la condicion estado <> 'CANCELADA'. El intento posterior se "
                                'rechaza y queda capturado como unique_violation en evidencia, y '
                                'la insercion con estado CANCELADA si es aceptada, probando que la '
                                'restriccion no es excesiva. La deteccion final devuelve cero '
                                'filas y el script no aborta.',
                     'setup_sql': 'CREATE TABLE dueno (\n'
                                  '  id_dueno SERIAL PRIMARY KEY,\n'
                                  '  nombre TEXT NOT NULL,\n'
                                  '  telefono TEXT,\n'
                                  '  email TEXT,\n'
                                  "  ciudad TEXT DEFAULT 'Cali'\n"
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE mascota (\n'
                                  '  id_mascota SERIAL PRIMARY KEY,\n'
                                  '  id_dueno INT NOT NULL REFERENCES dueno(id_dueno),\n'
                                  '  nombre TEXT NOT NULL,\n'
                                  '  especie TEXT NOT NULL,\n'
                                  '  fecha_nac DATE,\n'
                                  "  activa CHAR(1) NOT NULL DEFAULT 'S' CHECK (activa IN "
                                  "('S','N'))\n"
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE veterinario (\n'
                                  '  id_veterinario SERIAL PRIMARY KEY,\n'
                                  '  nombre TEXT NOT NULL,\n'
                                  '  especialidad TEXT,\n'
                                  "  activo CHAR(1) NOT NULL DEFAULT 'S' CHECK (activo IN "
                                  "('S','N'))\n"
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE cita (\n'
                                  '  id_cita SERIAL PRIMARY KEY,\n'
                                  '  id_mascota INT NOT NULL REFERENCES mascota(id_mascota),\n'
                                  '  id_veterinario INT NOT NULL REFERENCES '
                                  'veterinario(id_veterinario),\n'
                                  '  fecha_hora TIMESTAMP NOT NULL,\n'
                                  "  estado TEXT NOT NULL DEFAULT 'PROGRAMADA'\n"
                                  "    CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))\n"
                                  ');\n'
                                  '\n'
                                  '-- Duenos (ids 1..6 en este orden)\n'
                                  'INSERT INTO dueno (nombre, telefono, email) VALUES\n'
                                  "  ('Ana Gomez',      '3001112233', 'ana.gomez@mail.com'),\n"
                                  "  ('Carlos Ruiz',    '3014445566', 'carlos.ruiz@mail.com'),\n"
                                  "  ('Marcela Diaz',   '3027778899', 'marcela.diaz@mail.com'),\n"
                                  "  ('Jorge Pineda',   '3105551212', 'jorge.pineda@mail.com'),\n"
                                  "  ('Luisa Cardona',  '3123334455', 'luisa.cardona@mail.com'),\n"
                                  "  ('Andres Vallejo', '3159998877', 'andres.vallejo@mail.com');\n"
                                  '\n'
                                  '-- Veterinarios (ids 1..4)\n'
                                  'INSERT INTO veterinario (nombre, especialidad) VALUES\n'
                                  "  ('Laura Restrepo', 'General'),\n"
                                  "  ('Diego Moreno',   'Cirugia'),\n"
                                  "  ('Paula Salazar',  'Dermatologia'),\n"
                                  "  ('Ivan Ortiz',     'General');\n"
                                  '\n'
                                  '-- Mascotas (ids 1..8). Rocky (3) y Kiara (8) estan INACTIVAS.\n'
                                  'INSERT INTO mascota (id_dueno, nombre, especie, fecha_nac, '
                                  'activa) VALUES\n'
                                  "  (1, 'Firulais', 'Canino', DATE '2019-04-12', 'S'),\n"
                                  "  (1, 'Luna',     'Felino', DATE '2021-08-30', 'S'),\n"
                                  "  (2, 'Rocky',    'Canino', DATE '2015-01-20', 'N'),\n"
                                  "  (3, 'Mishi',    'Felino', DATE '2022-11-05', 'S'),\n"
                                  "  (3, 'Bobby',    'Canino', DATE '2018-06-17', 'S'),\n"
                                  "  (4, 'Nube',     'Felino', DATE '2023-02-09', 'S'),\n"
                                  "  (5, 'Toby',     'Canino', DATE '2020-09-25', 'S'),\n"
                                  "  (6, 'Kiara',    'Canino', DATE '2013-03-03', 'N');\n"
                                  '\n'
                                  '-- Citas (ids 1..10)\n'
                                  'INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                  'estado) VALUES\n'
                                  "  (1, 1, TIMESTAMP '2026-09-01 08:00:00', 'PROGRAMADA'),\n"
                                  "  (2, 1, TIMESTAMP '2026-09-01 09:00:00', 'ATENDIDA'),\n"
                                  "  (4, 2, TIMESTAMP '2026-09-01 10:00:00', 'PROGRAMADA'),\n"
                                  "  (5, 3, TIMESTAMP '2026-09-02 08:30:00', 'CANCELADA'),\n"
                                  "  (6, 2, TIMESTAMP '2026-09-02 11:00:00', 'ATENDIDA'),\n"
                                  "  (7, 4, TIMESTAMP '2026-09-03 07:45:00', 'PROGRAMADA'),\n"
                                  "  (1, 1, TIMESTAMP '2026-09-05 15:00:00', 'ATENDIDA'),\n"
                                  "  (2, 3, TIMESTAMP '2026-09-08 16:00:00', 'PROGRAMADA'),\n"
                                  "  (4, 4, TIMESTAMP '2026-09-10 08:00:00', 'PROGRAMADA'),\n"
                                  "  (6, 1, TIMESTAMP '2026-09-10 09:00:00', 'ATENDIDA');\n"
                                  '\n'
                                  'CREATE TABLE evidencia (\n'
                                  '  id_evidencia SERIAL PRIMARY KEY,\n'
                                  '  paso TEXT NOT NULL,\n'
                                  '  resultado TEXT NOT NULL,\n'
                                  '  registrado_en TIMESTAMP NOT NULL DEFAULT now()\n'
                                  ');\n',
                     'tipo': 'bd_sql'},
                    {'enunciado': '## 3. Doble descuento de stock: bloqueo explicito y '
                                  'actualizacion condicional\n'
                                  '\n'
                                  'Esquema completo de VetCare poblado. Insumo 2 (Vacuna triple '
                                  'felina) tiene **stock 3**; insumo 5 (Gasa esteril) tiene '
                                  '**stock 8**.\n'
                                  '\n'
                                  'Dos auxiliares facturan al mismo tiempo y ambas quieren 3 '
                                  'unidades del insumo 2. Hay para una sola. Vas a implementar y '
                                  'comparar **dos** mecanismos de PostgreSQL que resuelven esto.\n'
                                  '\n'
                                  '**Parte A - Actualizacion condicional (sin bloqueo '
                                  'explicito).**\n'
                                  '\n'
                                  '1. Escribe una funcion `fn_tomar_stock(p_id_insumo INT, '
                                  'p_cantidad INT)` que retorne `BOOLEAN`, haga `UPDATE insumo SET '
                                  'stock = stock - p_cantidad WHERE id_insumo = p_id_insumo AND '
                                  'stock >= p_cantidad;`, lea `GET DIAGNOSTICS v_filas = '
                                  'ROW_COUNT;` y retorne `v_filas = 1`.\n'
                                  '2. Ejecuta `SELECT fn_tomar_stock(2, 3) AS primera, '
                                  'fn_tomar_stock(2, 3) AS segunda;` y muestra que la primera '
                                  'devuelve `true` y la segunda `false`: la segunda "auxiliar" se '
                                  'queda sin insumo, pero el stock **nunca** baja de 0.\n'
                                  '3. Muestra `SELECT id_insumo, nombre, stock FROM insumo WHERE '
                                  'id_insumo IN (2, 5);`\n'
                                  '\n'
                                  '**Parte B - Bloqueo explicito de fila.**\n'
                                  '\n'
                                  '4. Escribe un bloque `DO` que simule la parte critica de una '
                                  'transaccion: primero `SELECT stock INTO v_stock FROM insumo '
                                  'WHERE id_insumo = 5 FOR UPDATE;` (esto **bloquea esa fila** '
                                  'hasta el final de la transaccion), luego valide `IF v_stock >= '
                                  '4 THEN UPDATE ... END IF;`, y registre con `RAISE NOTICE` lo '
                                  'que hizo.\n'
                                  '5. Escribe otro bloque `DO` identico pero pidiendo `FOR UPDATE '
                                  'NOWAIT` o `FOR UPDATE SKIP LOCKED` sobre el insumo 5, y comenta '
                                  'con `--` en que se diferencian los tres comportamientos (`FOR '
                                  'UPDATE` espera, `NOWAIT` falla de inmediato, `SKIP LOCKED` '
                                  'ignora la fila bloqueada).\n'
                                  '6. Cierra con un comentario `--` de 3 o 4 lineas respondiendo: '
                                  '**por que en esta sesion unica los tres se comportan igual** '
                                  '(nadie mas tiene la fila tomada, asi que nunca hay espera), '
                                  '**que veriamos en un servidor real** con dos sesiones, y **cual '
                                  'de los dos mecanismos (A o B) elegis para VetCare y por que** '
                                  '(pista: A resuelve la comprobacion y la escritura en una sola '
                                  'sentencia atomica; B es necesario cuando hay que leer, calcular '
                                  'con datos de varias tablas y despues escribir).',
                     'puntos': 20,
                     'rubrica': 'fn_tomar_stock usa el UPDATE condicional con GET DIAGNOSTICS y la '
                                'prueba arroja true y luego false, con el stock del insumo 2 en 0 '
                                'y nunca negativo. Se escriben los bloques DO con SELECT ... FOR '
                                'UPDATE y con NOWAIT o SKIP LOCKED, y se explica correctamente la '
                                'diferencia entre los tres. El comentario final reconoce que en '
                                'una sola sesion no hay espera observable, describe que ocurriria '
                                'con dos sesiones y elige un mecanismo con argumento tecnico.',
                     'setup_sql': 'CREATE TABLE dueno (\n'
                                  '  id_dueno SERIAL PRIMARY KEY,\n'
                                  '  nombre TEXT NOT NULL,\n'
                                  '  telefono TEXT,\n'
                                  '  email TEXT,\n'
                                  "  ciudad TEXT DEFAULT 'Cali'\n"
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE mascota (\n'
                                  '  id_mascota SERIAL PRIMARY KEY,\n'
                                  '  id_dueno INT NOT NULL REFERENCES dueno(id_dueno),\n'
                                  '  nombre TEXT NOT NULL,\n'
                                  '  especie TEXT NOT NULL,\n'
                                  '  fecha_nac DATE,\n'
                                  "  activa CHAR(1) NOT NULL DEFAULT 'S' CHECK (activa IN "
                                  "('S','N'))\n"
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE veterinario (\n'
                                  '  id_veterinario SERIAL PRIMARY KEY,\n'
                                  '  nombre TEXT NOT NULL,\n'
                                  '  especialidad TEXT,\n'
                                  "  activo CHAR(1) NOT NULL DEFAULT 'S' CHECK (activo IN "
                                  "('S','N'))\n"
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE cita (\n'
                                  '  id_cita SERIAL PRIMARY KEY,\n'
                                  '  id_mascota INT NOT NULL REFERENCES mascota(id_mascota),\n'
                                  '  id_veterinario INT NOT NULL REFERENCES '
                                  'veterinario(id_veterinario),\n'
                                  '  fecha_hora TIMESTAMP NOT NULL,\n'
                                  "  estado TEXT NOT NULL DEFAULT 'PROGRAMADA'\n"
                                  "    CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))\n"
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE consulta (\n'
                                  '  id_consulta SERIAL PRIMARY KEY,\n'
                                  '  id_cita INT NOT NULL UNIQUE REFERENCES cita(id_cita),\n'
                                  '  diagnostico TEXT,\n'
                                  '  precio NUMERIC(12,2) NOT NULL CHECK (precio >= 0)\n'
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE insumo (\n'
                                  '  id_insumo SERIAL PRIMARY KEY,\n'
                                  '  nombre TEXT NOT NULL,\n'
                                  '  stock INT NOT NULL CHECK (stock >= 0),\n'
                                  '  precio_unit NUMERIC(12,2) NOT NULL\n'
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE factura (\n'
                                  '  id_factura SERIAL PRIMARY KEY,\n'
                                  '  id_consulta INT NOT NULL REFERENCES consulta(id_consulta),\n'
                                  '  fecha TIMESTAMP NOT NULL DEFAULT now(),\n'
                                  '  total NUMERIC(12,2) NOT NULL DEFAULT 0\n'
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE detalle_factura (\n'
                                  '  id_detalle SERIAL PRIMARY KEY,\n'
                                  '  id_factura INT NOT NULL REFERENCES factura(id_factura) ON '
                                  'DELETE CASCADE,\n'
                                  '  id_insumo INT NOT NULL REFERENCES insumo(id_insumo),\n'
                                  '  cantidad INT NOT NULL CHECK (cantidad > 0),\n'
                                  '  precio_unit NUMERIC(12,2) NOT NULL\n'
                                  ');\n'
                                  '\n'
                                  '-- Duenos (ids 1..6 en este orden)\n'
                                  'INSERT INTO dueno (nombre, telefono, email) VALUES\n'
                                  "  ('Ana Gomez',      '3001112233', 'ana.gomez@mail.com'),\n"
                                  "  ('Carlos Ruiz',    '3014445566', 'carlos.ruiz@mail.com'),\n"
                                  "  ('Marcela Diaz',   '3027778899', 'marcela.diaz@mail.com'),\n"
                                  "  ('Jorge Pineda',   '3105551212', 'jorge.pineda@mail.com'),\n"
                                  "  ('Luisa Cardona',  '3123334455', 'luisa.cardona@mail.com'),\n"
                                  "  ('Andres Vallejo', '3159998877', 'andres.vallejo@mail.com');\n"
                                  '\n'
                                  '-- Veterinarios (ids 1..4)\n'
                                  'INSERT INTO veterinario (nombre, especialidad) VALUES\n'
                                  "  ('Laura Restrepo', 'General'),\n"
                                  "  ('Diego Moreno',   'Cirugia'),\n"
                                  "  ('Paula Salazar',  'Dermatologia'),\n"
                                  "  ('Ivan Ortiz',     'General');\n"
                                  '\n'
                                  '-- Mascotas (ids 1..8). Rocky (3) y Kiara (8) estan INACTIVAS.\n'
                                  'INSERT INTO mascota (id_dueno, nombre, especie, fecha_nac, '
                                  'activa) VALUES\n'
                                  "  (1, 'Firulais', 'Canino', DATE '2019-04-12', 'S'),\n"
                                  "  (1, 'Luna',     'Felino', DATE '2021-08-30', 'S'),\n"
                                  "  (2, 'Rocky',    'Canino', DATE '2015-01-20', 'N'),\n"
                                  "  (3, 'Mishi',    'Felino', DATE '2022-11-05', 'S'),\n"
                                  "  (3, 'Bobby',    'Canino', DATE '2018-06-17', 'S'),\n"
                                  "  (4, 'Nube',     'Felino', DATE '2023-02-09', 'S'),\n"
                                  "  (5, 'Toby',     'Canino', DATE '2020-09-25', 'S'),\n"
                                  "  (6, 'Kiara',    'Canino', DATE '2013-03-03', 'N');\n"
                                  '\n'
                                  '-- Citas (ids 1..10)\n'
                                  'INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                  'estado) VALUES\n'
                                  "  (1, 1, TIMESTAMP '2026-09-01 08:00:00', 'PROGRAMADA'),\n"
                                  "  (2, 1, TIMESTAMP '2026-09-01 09:00:00', 'ATENDIDA'),\n"
                                  "  (4, 2, TIMESTAMP '2026-09-01 10:00:00', 'PROGRAMADA'),\n"
                                  "  (5, 3, TIMESTAMP '2026-09-02 08:30:00', 'CANCELADA'),\n"
                                  "  (6, 2, TIMESTAMP '2026-09-02 11:00:00', 'ATENDIDA'),\n"
                                  "  (7, 4, TIMESTAMP '2026-09-03 07:45:00', 'PROGRAMADA'),\n"
                                  "  (1, 1, TIMESTAMP '2026-09-05 15:00:00', 'ATENDIDA'),\n"
                                  "  (2, 3, TIMESTAMP '2026-09-08 16:00:00', 'PROGRAMADA'),\n"
                                  "  (4, 4, TIMESTAMP '2026-09-10 08:00:00', 'PROGRAMADA'),\n"
                                  "  (6, 1, TIMESTAMP '2026-09-10 09:00:00', 'ATENDIDA');\n"
                                  '\n'
                                  '-- Consultas (ids 1..4) sobre las citas ATENDIDAS 2, 5, 7 y 10\n'
                                  'INSERT INTO consulta (id_cita, diagnostico, precio) VALUES\n'
                                  "  (2,  'Vacunacion triple felina', 40000),\n"
                                  "  (5,  'Control de peso',          38000),\n"
                                  "  (7,  'Otitis externa',           55000),\n"
                                  "  (10, 'Desparasitacion',          35000);\n"
                                  '\n'
                                  '-- Insumos (ids 1..6). Ojo: 2 y 5 tienen stock bajo a '
                                  'proposito.\n'
                                  'INSERT INTO insumo (nombre, stock, precio_unit) VALUES\n'
                                  "  ('Vacuna antirrabica',       12, 22000),\n"
                                  "  ('Vacuna triple felina',      3, 31000),\n"
                                  "  ('Antiparasitario oral',     40,  9500),\n"
                                  "  ('Suero fisiologico 500ml',  25,  7000),\n"
                                  "  ('Gasa esteril',              8,  1200),\n"
                                  "  ('Jeringa 5ml',              60,   900);\n"
                                  '\n'
                                  '-- Facturas (ids 1..3) y sus detalles\n'
                                  'INSERT INTO factura (id_consulta, fecha, total) VALUES\n'
                                  "  (1, TIMESTAMP '2026-09-01 09:40:00', 71000),\n"
                                  "  (2, TIMESTAMP '2026-09-02 11:35:00', 47000),\n"
                                  "  (3, TIMESTAMP '2026-09-05 15:50:00', 60200);\n"
                                  '\n'
                                  'INSERT INTO detalle_factura (id_factura, id_insumo, cantidad, '
                                  'precio_unit) VALUES\n'
                                  '  (1, 2, 1, 31000),\n'
                                  '  (1, 6, 1,   900),\n'
                                  '  (1, 3, 1,  9500),\n'
                                  '  (2, 3, 1,  9500),\n'
                                  '  (2, 4, 1,  7000),\n'
                                  '  (3, 1, 1, 22000),\n'
                                  '  (3, 5, 4,  1200),\n'
                                  '  (3, 6, 2,   900);\n',
                     'tipo': 'bd_sql'},
                    {'correctas': [0, 1, 3, 5],
                     'enunciado': '## 4. Niveles de aislamiento y anomalias en PostgreSQL\n'
                                  '\n'
                                  'Selecciona **todas** las afirmaciones correctas sobre '
                                  'aislamiento y concurrencia en PostgreSQL, pensando en VetCare.',
                     'opciones': ['El nivel por defecto en PostgreSQL es READ COMMITTED: cada '
                                  'sentencia ve una foto nueva de los datos confirmados, asi que '
                                  'dos lecturas dentro de la misma transaccion pueden dar '
                                  'resultados distintos.',
                                  'READ COMMITTED evita las lecturas sucias (dirty reads), pero no '
                                  'las lecturas no repetibles ni los fantasmas sobre un predicado.',
                                  'En PostgreSQL, READ UNCOMMITTED permite leer datos no '
                                  'confirmados de otras transacciones.',
                                  'Con SERIALIZABLE, PostgreSQL puede abortar una transaccion con '
                                  'un error de serializacion; la aplicacion debe estar preparada '
                                  'para reintentarla.',
                                  'Una restriccion UNIQUE resuelve el problema solo si las '
                                  'transacciones se ejecutan una despues de otra; si son '
                                  'simultaneas, la restriccion no aplica.',
                                  'Mantener las transacciones cortas reduce la ventana de '
                                  'conflicto: nunca hay que dejar una transaccion abierta '
                                  'esperando que el usuario llene un formulario.'],
                     'puntos': 10,
                     'rubrica': '10 puntos con las 4 opciones correctas y ninguna incorrecta; '
                                'puntaje proporcional por acierto parcial. Correctas: indices 0, '
                                '1, 3 y 5.',
                     'tipo': 'cerrada_multi'},
                    {'enunciado': '## 5. Informe de concurrencia del PI y limites de la '
                                  'verificacion\n'
                                  '\n'
                                  'Redacta la seccion "Control de concurrencia" del informe del '
                                  'PI, con:\n'
                                  '\n'
                                  '1. **Escenario 2: doble descuento de stock**, con linea de '
                                  'tiempo T1/T2 de al menos 5 pasos, igual que hiciste con la '
                                  'doble reserva. Contexto: dos auxiliares facturan la ultima '
                                  'Vacuna triple felina (stock 3, ambas piden 3). Marca el '
                                  'instante del `SELECT stock` de cada una y el del `UPDATE`.\n'
                                  '2. **Mitigacion elegida para cada escenario**, con la sentencia '
                                  'SQL exacta que la implementa: cual es para la doble reserva '
                                  '(indice unico parcial) y cual para el stock (`UPDATE ... WHERE '
                                  'stock >= cantidad` o `SELECT ... FOR UPDATE`), y por que '
                                  'descartaste las otras.\n'
                                  '3. **Contrato con la aplicacion**: que error recibe la '
                                  'aplicacion en cada caso (violacion de unicidad, funcion que '
                                  'devuelve `false`, error de serializacion) y **que debe hacer**: '
                                  'mostrar mensaje, ofrecer otra franja, reintentar '
                                  'automaticamente, o abortar. Una fila por caso.\n'
                                  '4. **Limitacion del entorno, explicitamente.** Escribe por que '
                                  '**no** fue posible reproducir un bloqueo ni un deadlock reales '
                                  'en ExamLab: PostgreSQL corre compilado a WebAssembly dentro del '
                                  'navegador con **una unica conexion**, asi que no existen dos '
                                  'transacciones concurrentes que puedan esperarse. Indica que '
                                  'herramientas usarias en un servidor real para hacer esa prueba '
                                  '(dos sesiones de `psql`, `pgbench`, las vistas `pg_locks` y '
                                  '`pg_stat_activity`) y que evidencia concreta capturarias.\n'
                                  '5. **Riesgo residual**: que escenario de concurrencia de '
                                  'VetCare queda sin mitigar y como lo vigilarias.',
                     'puntos': 20,
                     'rubrica': 'El escenario 2 tiene linea de tiempo de al menos 5 pasos con los '
                                'instantes de lectura y escritura marcados. Cada mitigacion viene '
                                'con su sentencia SQL exacta y con el descarte razonado de las '
                                'alternativas. La tabla del contrato cubre los tres tipos de error '
                                'con la accion de la aplicacion. La seccion 4 reconoce con '
                                'precision la limitacion de sesion unica de PGlite y nombra '
                                'herramientas reales de verificacion. Se identifica al menos un '
                                'riesgo residual con su forma de vigilancia.',
                     'tipo': 'abierta'}],
      'resumen': 'El estudiante documenta los dos escenarios de concurrencia del PI (doble reserva '
                 'de franja y doble descuento de stock), implementa y prueba las mitigaciones que '
                 'si son verificables en una sola sesion y explica el limite del entorno.',
      'titulo': 'Taller Clase 10 en ExamLab - Control de concurrencia en VetCare (clase autonoma)'},
 11: {'preguntas': [{'enunciado': '## 1. ER consolidado de VetCare DB (version del hito)\n'
                                  '\n'
                                  'Entrega el **ER definitivo** de VetCare DB tal como quedo '
                                  'despues de las Clases 1 a 8, en `erDiagram` de Mermaid. Debe '
                                  'reflejar el estado **real** de tu base, no el borrador de la '
                                  'Clase 1. Incluye:\n'
                                  '\n'
                                  '- Las 8 entidades del dominio: `dueno`, `mascota`, '
                                  '`veterinario`, `cita`, `consulta`, `insumo`, `factura`, '
                                  '`detalle_factura`.\n'
                                  '- La entidad de **auditoria** `audit_cita`, que aparecio en la '
                                  'Clase 4, dibujada sin relacion de FK (es una bitacora '
                                  'historica: guarda el `id_cita` pero no debe impedir borrar ni '
                                  'cambiar la cita).\n'
                                  '- Para cada entidad, la PK, las FK y al menos dos atributos '
                                  'mas, con los **nombres exactos** que usaste en tu DDL.\n'
                                  '- Las cardinalidades: `dueno` 1-N `mascota`, `mascota` 1-N '
                                  '`cita`, `veterinario` 1-N `cita`, `cita` 1-1 `consulta`, '
                                  '`consulta` 1-N `factura`, `factura` 1-N `detalle_factura`, '
                                  '`insumo` 1-N `detalle_factura`.\n'
                                  '\n'
                                  'Este diagrama es el que proyectas en la demo de 3 a 5 minutos, '
                                  'asi que debe ser legible.',
                     'mermaid_esperado': 'erDiagram\n'
                                         '    dueno {\n'
                                         '        int id_dueno PK\n'
                                         '        text nombre\n'
                                         '        text telefono\n'
                                         '        text email\n'
                                         '    }\n'
                                         '    mascota {\n'
                                         '        int id_mascota PK\n'
                                         '        int id_dueno FK\n'
                                         '        text nombre\n'
                                         '        text especie\n'
                                         '        char activa\n'
                                         '    }\n'
                                         '    veterinario {\n'
                                         '        int id_veterinario PK\n'
                                         '        text nombre\n'
                                         '        text especialidad\n'
                                         '    }\n'
                                         '    cita {\n'
                                         '        int id_cita PK\n'
                                         '        int id_mascota FK\n'
                                         '        int id_veterinario FK\n'
                                         '        timestamp fecha_hora\n'
                                         '        text estado\n'
                                         '    }\n'
                                         '    consulta {\n'
                                         '        int id_consulta PK\n'
                                         '        int id_cita FK\n'
                                         '        text diagnostico\n'
                                         '        numeric precio\n'
                                         '    }\n'
                                         '    factura {\n'
                                         '        int id_factura PK\n'
                                         '        int id_consulta FK\n'
                                         '        timestamp fecha\n'
                                         '        numeric total\n'
                                         '    }\n'
                                         '    detalle_factura {\n'
                                         '        int id_detalle PK\n'
                                         '        int id_factura FK\n'
                                         '        int id_insumo FK\n'
                                         '        int cantidad\n'
                                         '        numeric precio_unit\n'
                                         '    }\n'
                                         '    insumo {\n'
                                         '        int id_insumo PK\n'
                                         '        text nombre\n'
                                         '        int stock\n'
                                         '        numeric precio_unit\n'
                                         '    }\n'
                                         '    audit_cita {\n'
                                         '        int id_audit PK\n'
                                         '        int id_cita\n'
                                         '        text accion\n'
                                         '        text valor_anterior\n'
                                         '        text valor_nuevo\n'
                                         '        timestamp fecha_evento\n'
                                         '    }\n'
                                         '    dueno ||--o{ mascota : tiene\n'
                                         '    mascota ||--o{ cita : genera\n'
                                         '    veterinario ||--o{ cita : atiende\n'
                                         '    cita ||--|| consulta : produce\n'
                                         '    consulta ||--o{ factura : facturada_en\n'
                                         '    factura ||--o{ detalle_factura : contiene\n'
                                         '    insumo ||--o{ detalle_factura : aparece_en',
                     'puntos': 20,
                     'rubrica': 'El diagrama renderiza sin errores y contiene las 8 entidades del '
                                'dominio mas audit_cita. Las 7 relaciones llevan la cardinalidad '
                                'correcta y audit_cita aparece sin FK, con la razon evidente. Los '
                                'nombres de tablas y columnas coinciden con el DDL entregado en '
                                'las clases anteriores. Se descuenta por entidades o relaciones '
                                'faltantes y por nombres que no correspondan al codigo real.',
                     'tipo': 'diagrama'},
                    {'enunciado': '## 2. Bateria de verificacion del avance del PI\n'
                                  '\n'
                                  'Esta base trae **el avance completo de VetCare** tal como '
                                  'deberia estar en este hito: las 8 tablas con datos, la tabla '
                                  '`audit_cita` con su trigger `trg_audit_cita`, el procedimiento '
                                  '`sp_agendar_cita` y el procedimiento `sp_facturar`.\n'
                                  '\n'
                                  'Tu trabajo es escribir el **script de verificacion** que se '
                                  'ejecuta en la demo. Son **cinco pruebas**; cada una debe '
                                  'registrar su resultado en la tabla `checklist_pi (id_item '
                                  'SERIAL, item TEXT, resultado TEXT, cumple BOOLEAN)` que ya '
                                  'existe.\n'
                                  '\n'
                                  '**Prueba 1 - Integridad referencial.** Intenta insertar una '
                                  'cita con `id_mascota = 999` (no existe) dentro de un bloque '
                                  '`DO` que capture `foreign_key_violation`. Registra en '
                                  "`checklist_pi` el item `'Integridad referencial cita->mascota'` "
                                  'con `cumple = TRUE` si la base **rechazo** la insercion.\n'
                                  '\n'
                                  '**Prueba 2 - Regla: mascota inactiva no agenda.** Llama `CALL '
                                  "sp_agendar_cita(3, 2, TIMESTAMP '2026-11-05 09:00:00');` (la "
                                  'mascota 3, Rocky, esta inactiva) dentro de un `DO` con '
                                  "`EXCEPTION WHEN OTHERS`. Registra el item `'Regla: mascota "
                                  "inactiva no agenda'` con `cumple = TRUE` si el procedimiento "
                                  '**lanzo** excepcion, guardando el `SQLERRM` en `resultado`.\n'
                                  '\n'
                                  '**Prueba 3 - Regla: stock nunca negativo.** Llama `CALL '
                                  'sp_facturar(4, ARRAY[2], ARRAY[10]);` (el insumo 2 tiene stock '
                                  "3) dentro de un `DO` con captura. Registra el item `'Regla: "
                                  "stock nunca negativo'` con `cumple = TRUE` si fallo, y **anade "
                                  'en `resultado` el stock actual del insumo 2** para probar que '
                                  'no se movio.\n'
                                  '\n'
                                  '**Prueba 4 - Auditoria activa.** Ejecuta `UPDATE cita SET '
                                  "estado = 'CANCELADA' WHERE id_cita = 1;` y luego verifica que "
                                  '`audit_cita` tenga la fila correspondiente con `valor_anterior '
                                  "= 'PROGRAMADA'` y `valor_nuevo = 'CANCELADA'`. Registra el item "
                                  "`'Auditoria de cambios de estado'` con el `cumple` que "
                                  'corresponda.\n'
                                  '\n'
                                  '**Prueba 5 - Coherencia de facturacion.** Escribe una consulta '
                                  'que compare, para cada factura, el `total` guardado contra la '
                                  'suma de `cantidad * precio_unit` de su `detalle_factura`, y '
                                  "registra el item `'Total de factura coincide con sus detalles'` "
                                  'con `cumple = TRUE` **solo si no hay ninguna factura '
                                  'descuadrada**. Sugerencia: usa `NOT EXISTS` sobre la consulta '
                                  'de descuadres.\n'
                                  '\n'
                                  'Cierra con `SELECT id_item, item, cumple, resultado FROM '
                                  'checklist_pi ORDER BY id_item;`',
                     'puntos': 35,
                     'rubrica': 'Las 5 pruebas se ejecutan sin abortar el script y cada una '
                                'inserta exactamente una fila en checklist_pi con su veredicto. La '
                                'prueba 1 captura foreign_key_violation, las 2 y 3 capturan la '
                                'excepcion del procedimiento y la 3 evidencia que el stock del '
                                'insumo 2 sigue en 3. La prueba 4 confirma la fila de audit_cita '
                                'con los valores anterior y nuevo. La prueba 5 calcula el '
                                'descuadre con la suma de los detalles y solo marca cumple si no '
                                'hay ninguno. El SELECT final muestra las 5 filas.',
                     'setup_sql': 'CREATE TABLE dueno (\n'
                                  '  id_dueno SERIAL PRIMARY KEY,\n'
                                  '  nombre TEXT NOT NULL,\n'
                                  '  telefono TEXT,\n'
                                  '  email TEXT,\n'
                                  "  ciudad TEXT DEFAULT 'Cali'\n"
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE mascota (\n'
                                  '  id_mascota SERIAL PRIMARY KEY,\n'
                                  '  id_dueno INT NOT NULL REFERENCES dueno(id_dueno),\n'
                                  '  nombre TEXT NOT NULL,\n'
                                  '  especie TEXT NOT NULL,\n'
                                  '  fecha_nac DATE,\n'
                                  "  activa CHAR(1) NOT NULL DEFAULT 'S' CHECK (activa IN "
                                  "('S','N'))\n"
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE veterinario (\n'
                                  '  id_veterinario SERIAL PRIMARY KEY,\n'
                                  '  nombre TEXT NOT NULL,\n'
                                  '  especialidad TEXT,\n'
                                  "  activo CHAR(1) NOT NULL DEFAULT 'S' CHECK (activo IN "
                                  "('S','N'))\n"
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE cita (\n'
                                  '  id_cita SERIAL PRIMARY KEY,\n'
                                  '  id_mascota INT NOT NULL REFERENCES mascota(id_mascota),\n'
                                  '  id_veterinario INT NOT NULL REFERENCES '
                                  'veterinario(id_veterinario),\n'
                                  '  fecha_hora TIMESTAMP NOT NULL,\n'
                                  "  estado TEXT NOT NULL DEFAULT 'PROGRAMADA'\n"
                                  "    CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))\n"
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE consulta (\n'
                                  '  id_consulta SERIAL PRIMARY KEY,\n'
                                  '  id_cita INT NOT NULL UNIQUE REFERENCES cita(id_cita),\n'
                                  '  diagnostico TEXT,\n'
                                  '  precio NUMERIC(12,2) NOT NULL CHECK (precio >= 0)\n'
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE insumo (\n'
                                  '  id_insumo SERIAL PRIMARY KEY,\n'
                                  '  nombre TEXT NOT NULL,\n'
                                  '  stock INT NOT NULL CHECK (stock >= 0),\n'
                                  '  precio_unit NUMERIC(12,2) NOT NULL\n'
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE factura (\n'
                                  '  id_factura SERIAL PRIMARY KEY,\n'
                                  '  id_consulta INT NOT NULL REFERENCES consulta(id_consulta),\n'
                                  '  fecha TIMESTAMP NOT NULL DEFAULT now(),\n'
                                  '  total NUMERIC(12,2) NOT NULL DEFAULT 0\n'
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE detalle_factura (\n'
                                  '  id_detalle SERIAL PRIMARY KEY,\n'
                                  '  id_factura INT NOT NULL REFERENCES factura(id_factura) ON '
                                  'DELETE CASCADE,\n'
                                  '  id_insumo INT NOT NULL REFERENCES insumo(id_insumo),\n'
                                  '  cantidad INT NOT NULL CHECK (cantidad > 0),\n'
                                  '  precio_unit NUMERIC(12,2) NOT NULL\n'
                                  ');\n'
                                  '\n'
                                  '-- Duenos (ids 1..6 en este orden)\n'
                                  'INSERT INTO dueno (nombre, telefono, email) VALUES\n'
                                  "  ('Ana Gomez',      '3001112233', 'ana.gomez@mail.com'),\n"
                                  "  ('Carlos Ruiz',    '3014445566', 'carlos.ruiz@mail.com'),\n"
                                  "  ('Marcela Diaz',   '3027778899', 'marcela.diaz@mail.com'),\n"
                                  "  ('Jorge Pineda',   '3105551212', 'jorge.pineda@mail.com'),\n"
                                  "  ('Luisa Cardona',  '3123334455', 'luisa.cardona@mail.com'),\n"
                                  "  ('Andres Vallejo', '3159998877', 'andres.vallejo@mail.com');\n"
                                  '\n'
                                  '-- Veterinarios (ids 1..4)\n'
                                  'INSERT INTO veterinario (nombre, especialidad) VALUES\n'
                                  "  ('Laura Restrepo', 'General'),\n"
                                  "  ('Diego Moreno',   'Cirugia'),\n"
                                  "  ('Paula Salazar',  'Dermatologia'),\n"
                                  "  ('Ivan Ortiz',     'General');\n"
                                  '\n'
                                  '-- Mascotas (ids 1..8). Rocky (3) y Kiara (8) estan INACTIVAS.\n'
                                  'INSERT INTO mascota (id_dueno, nombre, especie, fecha_nac, '
                                  'activa) VALUES\n'
                                  "  (1, 'Firulais', 'Canino', DATE '2019-04-12', 'S'),\n"
                                  "  (1, 'Luna',     'Felino', DATE '2021-08-30', 'S'),\n"
                                  "  (2, 'Rocky',    'Canino', DATE '2015-01-20', 'N'),\n"
                                  "  (3, 'Mishi',    'Felino', DATE '2022-11-05', 'S'),\n"
                                  "  (3, 'Bobby',    'Canino', DATE '2018-06-17', 'S'),\n"
                                  "  (4, 'Nube',     'Felino', DATE '2023-02-09', 'S'),\n"
                                  "  (5, 'Toby',     'Canino', DATE '2020-09-25', 'S'),\n"
                                  "  (6, 'Kiara',    'Canino', DATE '2013-03-03', 'N');\n"
                                  '\n'
                                  '-- Citas (ids 1..10)\n'
                                  'INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                  'estado) VALUES\n'
                                  "  (1, 1, TIMESTAMP '2026-09-01 08:00:00', 'PROGRAMADA'),\n"
                                  "  (2, 1, TIMESTAMP '2026-09-01 09:00:00', 'ATENDIDA'),\n"
                                  "  (4, 2, TIMESTAMP '2026-09-01 10:00:00', 'PROGRAMADA'),\n"
                                  "  (5, 3, TIMESTAMP '2026-09-02 08:30:00', 'CANCELADA'),\n"
                                  "  (6, 2, TIMESTAMP '2026-09-02 11:00:00', 'ATENDIDA'),\n"
                                  "  (7, 4, TIMESTAMP '2026-09-03 07:45:00', 'PROGRAMADA'),\n"
                                  "  (1, 1, TIMESTAMP '2026-09-05 15:00:00', 'ATENDIDA'),\n"
                                  "  (2, 3, TIMESTAMP '2026-09-08 16:00:00', 'PROGRAMADA'),\n"
                                  "  (4, 4, TIMESTAMP '2026-09-10 08:00:00', 'PROGRAMADA'),\n"
                                  "  (6, 1, TIMESTAMP '2026-09-10 09:00:00', 'ATENDIDA');\n"
                                  '\n'
                                  '-- Consultas (ids 1..4) sobre las citas ATENDIDAS 2, 5, 7 y 10\n'
                                  'INSERT INTO consulta (id_cita, diagnostico, precio) VALUES\n'
                                  "  (2,  'Vacunacion triple felina', 40000),\n"
                                  "  (5,  'Control de peso',          38000),\n"
                                  "  (7,  'Otitis externa',           55000),\n"
                                  "  (10, 'Desparasitacion',          35000);\n"
                                  '\n'
                                  '-- Insumos (ids 1..6). Ojo: 2 y 5 tienen stock bajo a '
                                  'proposito.\n'
                                  'INSERT INTO insumo (nombre, stock, precio_unit) VALUES\n'
                                  "  ('Vacuna antirrabica',       12, 22000),\n"
                                  "  ('Vacuna triple felina',      3, 31000),\n"
                                  "  ('Antiparasitario oral',     40,  9500),\n"
                                  "  ('Suero fisiologico 500ml',  25,  7000),\n"
                                  "  ('Gasa esteril',              8,  1200),\n"
                                  "  ('Jeringa 5ml',              60,   900);\n"
                                  '\n'
                                  '-- Facturas (ids 1..3) y sus detalles\n'
                                  'INSERT INTO factura (id_consulta, fecha, total) VALUES\n'
                                  "  (1, TIMESTAMP '2026-09-01 09:40:00', 71000),\n"
                                  "  (2, TIMESTAMP '2026-09-02 11:35:00', 47000),\n"
                                  "  (3, TIMESTAMP '2026-09-05 15:50:00', 60200);\n"
                                  '\n'
                                  'INSERT INTO detalle_factura (id_factura, id_insumo, cantidad, '
                                  'precio_unit) VALUES\n'
                                  '  (1, 2, 1, 31000),\n'
                                  '  (1, 6, 1,   900),\n'
                                  '  (1, 3, 1,  9500),\n'
                                  '  (2, 3, 1,  9500),\n'
                                  '  (2, 4, 1,  7000),\n'
                                  '  (3, 1, 1, 22000),\n'
                                  '  (3, 5, 4,  1200),\n'
                                  '  (3, 6, 2,   900);\n'
                                  '\n'
                                  'CREATE PROCEDURE sp_agendar_cita(\n'
                                  '  p_id_mascota     INT,\n'
                                  '  p_id_veterinario INT,\n'
                                  '  p_fecha_hora     TIMESTAMP\n'
                                  ')\n'
                                  'LANGUAGE plpgsql\n'
                                  'AS $proc$\n'
                                  'DECLARE\n'
                                  '  v_activa CHAR(1);\n'
                                  '  v_ocupado INT;\n'
                                  'BEGIN\n'
                                  '  SELECT activa INTO v_activa FROM mascota WHERE id_mascota = '
                                  'p_id_mascota;\n'
                                  '  IF NOT FOUND THEN\n'
                                  "    RAISE EXCEPTION 'ERROR: la mascota % no existe', "
                                  'p_id_mascota;\n'
                                  '  END IF;\n'
                                  "  IF v_activa <> 'S' THEN\n"
                                  "    RAISE EXCEPTION 'ERROR: la mascota % esta inactiva; no se "
                                  "agenda cita', p_id_mascota;\n"
                                  '  END IF;\n'
                                  '  SELECT COUNT(*) INTO v_ocupado\n'
                                  '  FROM cita\n'
                                  '  WHERE id_veterinario = p_id_veterinario\n'
                                  '    AND fecha_hora = p_fecha_hora\n'
                                  "    AND estado <> 'CANCELADA';\n"
                                  '  IF v_ocupado > 0 THEN\n'
                                  "    RAISE EXCEPTION 'ERROR: el veterinario % ya tiene cita en "
                                  "%', p_id_veterinario, p_fecha_hora;\n"
                                  '  END IF;\n'
                                  '  INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                  'estado)\n'
                                  '  VALUES (p_id_mascota, p_id_veterinario, p_fecha_hora, '
                                  "'PROGRAMADA');\n"
                                  'END;\n'
                                  '$proc$;\n'
                                  '\n'
                                  'CREATE PROCEDURE sp_facturar(\n'
                                  '  p_id_consulta INT,\n'
                                  '  p_insumos     INT[],\n'
                                  '  p_cantidades  INT[]\n'
                                  ')\n'
                                  'LANGUAGE plpgsql\n'
                                  'AS $proc$\n'
                                  'DECLARE\n'
                                  '  v_id_factura INT;\n'
                                  '  v_total NUMERIC(12,2) := 0;\n'
                                  '  v_precio NUMERIC(12,2);\n'
                                  '  v_filas INT;\n'
                                  '  i INT;\n'
                                  'BEGIN\n'
                                  '  IF array_length(p_insumos, 1) IS DISTINCT FROM '
                                  'array_length(p_cantidades, 1) THEN\n'
                                  "    RAISE EXCEPTION 'ERROR: insumos y cantidades deben tener la "
                                  "misma longitud';\n"
                                  '  END IF;\n'
                                  '\n'
                                  '  INSERT INTO factura (id_consulta, total) VALUES '
                                  '(p_id_consulta, 0)\n'
                                  '  RETURNING id_factura INTO v_id_factura;\n'
                                  '\n'
                                  '  FOR i IN 1 .. array_length(p_insumos, 1) LOOP\n'
                                  '    SELECT precio_unit INTO v_precio FROM insumo WHERE '
                                  'id_insumo = p_insumos[i];\n'
                                  '    IF NOT FOUND THEN\n'
                                  "      RAISE EXCEPTION 'ERROR: el insumo % no existe', "
                                  'p_insumos[i];\n'
                                  '    END IF;\n'
                                  '\n'
                                  '    UPDATE insumo\n'
                                  '       SET stock = stock - p_cantidades[i]\n'
                                  '     WHERE id_insumo = p_insumos[i]\n'
                                  '       AND stock >= p_cantidades[i];\n'
                                  '    GET DIAGNOSTICS v_filas = ROW_COUNT;\n'
                                  '    IF v_filas = 0 THEN\n'
                                  "      RAISE EXCEPTION 'ERROR: stock insuficiente del insumo % "
                                  "(se pidieron %)',\n"
                                  '        p_insumos[i], p_cantidades[i];\n'
                                  '    END IF;\n'
                                  '\n'
                                  '    INSERT INTO detalle_factura (id_factura, id_insumo, '
                                  'cantidad, precio_unit)\n'
                                  '    VALUES (v_id_factura, p_insumos[i], p_cantidades[i], '
                                  'v_precio);\n'
                                  '\n'
                                  '    v_total := v_total + (v_precio * p_cantidades[i]);\n'
                                  '  END LOOP;\n'
                                  '\n'
                                  '  UPDATE factura SET total = v_total WHERE id_factura = '
                                  'v_id_factura;\n'
                                  "  RAISE NOTICE 'Factura % creada por %', v_id_factura, "
                                  'v_total;\n'
                                  'END;\n'
                                  '$proc$;\n'
                                  '\n'
                                  'CREATE TABLE audit_cita (\n'
                                  '  id_audit SERIAL PRIMARY KEY,\n'
                                  '  id_cita INT NOT NULL,\n'
                                  '  accion TEXT NOT NULL,\n'
                                  '  valor_anterior TEXT,\n'
                                  '  valor_nuevo TEXT,\n'
                                  '  usuario_bd TEXT NOT NULL DEFAULT current_user,\n'
                                  '  fecha_evento TIMESTAMP NOT NULL DEFAULT now()\n'
                                  ');\n'
                                  '\n'
                                  'CREATE FUNCTION fn_trg_audit_cita() RETURNS TRIGGER\n'
                                  'LANGUAGE plpgsql\n'
                                  'AS $fn$\n'
                                  'BEGIN\n'
                                  '  INSERT INTO audit_cita (id_cita, accion, valor_anterior, '
                                  'valor_nuevo)\n'
                                  "  VALUES (NEW.id_cita, 'CAMBIO_ESTADO', OLD.estado, "
                                  'NEW.estado);\n'
                                  '  RETURN NULL;\n'
                                  'END;\n'
                                  '$fn$;\n'
                                  '\n'
                                  'CREATE TRIGGER trg_audit_cita\n'
                                  'AFTER UPDATE OF estado ON cita\n'
                                  'FOR EACH ROW\n'
                                  'WHEN (OLD.estado IS DISTINCT FROM NEW.estado)\n'
                                  'EXECUTE FUNCTION fn_trg_audit_cita();\n'
                                  '\n'
                                  'CREATE TABLE checklist_pi (\n'
                                  '  id_item SERIAL PRIMARY KEY,\n'
                                  '  item TEXT NOT NULL,\n'
                                  '  resultado TEXT,\n'
                                  '  cumple BOOLEAN\n'
                                  ');\n',
                     'tipo': 'bd_sql'},
                    {'enunciado': '## 3. Los tres reportes de la demo\n'
                                  '\n'
                                  'Misma base con el avance completo de VetCare. Para la demo de 3 '
                                  'a 5 minutos necesitas **tres consultas de reporte** listas para '
                                  'proyectar. Escribelas en este orden:\n'
                                  '\n'
                                  '**R1 - Agenda operativa.** Para las citas **no canceladas** de '
                                  'septiembre de 2026: `fecha_hora`, nombre de la mascota, '
                                  'especie, nombre del dueno, telefono del dueno, nombre del '
                                  'veterinario y `estado`. Filtra `fecha_hora` por **rango** (`>= '
                                  "'2026-09-01'` y `< '2026-10-01'`) y ordena por `fecha_hora`.\n"
                                  '\n'
                                  '**R2 - Historia clinica y facturacion por dueno.** Una fila por '
                                  'dueno con: `id_dueno`, nombre, cuantas mascotas tiene, cuantas '
                                  'citas suman todas sus mascotas, cuantas consultas se le '
                                  'registraron y el **total facturado** (suma de `factura.total`). '
                                  'Los duenos sin actividad deben aparecer con `0`, no '
                                  'desaparecer: usa `LEFT JOIN` y `COALESCE`. Ordena por total '
                                  'facturado descendente.\n'
                                  '*Cuidado con el conteo duplicado*: si unes varias tablas en '
                                  'cadena, los `COUNT` se inflan. Resuelvelo con `COUNT(DISTINCT '
                                  '...)` o con subconsultas agregadas por dueno.\n'
                                  '\n'
                                  '**R3 - Insumos en riesgo.** Para cada insumo: `nombre`, `stock` '
                                  'actual, total de unidades consumidas segun `detalle_factura` y '
                                  "una columna `alerta` que diga `'CRITICO'` si el stock es menor "
                                  "a 5, `'BAJO'` si esta entre 5 y 10, y `'OK'` en los demas casos "
                                  '(usa `CASE`). Ordena poniendo primero los criticos.\n'
                                  '\n'
                                  'Al final, escribe en comentarios `--` una linea por reporte '
                                  'indicando **que decision del negocio** habilita cada uno.',
                     'puntos': 20,
                     'rubrica': 'Los 3 reportes corren y devuelven datos coherentes con la base. '
                                'R1 filtra por rango de fecha y excluye canceladas. R2 conserva '
                                'los duenos sin actividad con ceros y evita el conteo inflado '
                                'usando COUNT(DISTINCT) o subconsultas agregadas. R3 clasifica '
                                'correctamente con CASE los tres niveles de alerta y ordena por '
                                'criticidad. Los comentarios finales asocian cada reporte a una '
                                'decision concreta del negocio.',
                     'setup_sql': 'CREATE TABLE dueno (\n'
                                  '  id_dueno SERIAL PRIMARY KEY,\n'
                                  '  nombre TEXT NOT NULL,\n'
                                  '  telefono TEXT,\n'
                                  '  email TEXT,\n'
                                  "  ciudad TEXT DEFAULT 'Cali'\n"
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE mascota (\n'
                                  '  id_mascota SERIAL PRIMARY KEY,\n'
                                  '  id_dueno INT NOT NULL REFERENCES dueno(id_dueno),\n'
                                  '  nombre TEXT NOT NULL,\n'
                                  '  especie TEXT NOT NULL,\n'
                                  '  fecha_nac DATE,\n'
                                  "  activa CHAR(1) NOT NULL DEFAULT 'S' CHECK (activa IN "
                                  "('S','N'))\n"
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE veterinario (\n'
                                  '  id_veterinario SERIAL PRIMARY KEY,\n'
                                  '  nombre TEXT NOT NULL,\n'
                                  '  especialidad TEXT,\n'
                                  "  activo CHAR(1) NOT NULL DEFAULT 'S' CHECK (activo IN "
                                  "('S','N'))\n"
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE cita (\n'
                                  '  id_cita SERIAL PRIMARY KEY,\n'
                                  '  id_mascota INT NOT NULL REFERENCES mascota(id_mascota),\n'
                                  '  id_veterinario INT NOT NULL REFERENCES '
                                  'veterinario(id_veterinario),\n'
                                  '  fecha_hora TIMESTAMP NOT NULL,\n'
                                  "  estado TEXT NOT NULL DEFAULT 'PROGRAMADA'\n"
                                  "    CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))\n"
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE consulta (\n'
                                  '  id_consulta SERIAL PRIMARY KEY,\n'
                                  '  id_cita INT NOT NULL UNIQUE REFERENCES cita(id_cita),\n'
                                  '  diagnostico TEXT,\n'
                                  '  precio NUMERIC(12,2) NOT NULL CHECK (precio >= 0)\n'
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE insumo (\n'
                                  '  id_insumo SERIAL PRIMARY KEY,\n'
                                  '  nombre TEXT NOT NULL,\n'
                                  '  stock INT NOT NULL CHECK (stock >= 0),\n'
                                  '  precio_unit NUMERIC(12,2) NOT NULL\n'
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE factura (\n'
                                  '  id_factura SERIAL PRIMARY KEY,\n'
                                  '  id_consulta INT NOT NULL REFERENCES consulta(id_consulta),\n'
                                  '  fecha TIMESTAMP NOT NULL DEFAULT now(),\n'
                                  '  total NUMERIC(12,2) NOT NULL DEFAULT 0\n'
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE detalle_factura (\n'
                                  '  id_detalle SERIAL PRIMARY KEY,\n'
                                  '  id_factura INT NOT NULL REFERENCES factura(id_factura) ON '
                                  'DELETE CASCADE,\n'
                                  '  id_insumo INT NOT NULL REFERENCES insumo(id_insumo),\n'
                                  '  cantidad INT NOT NULL CHECK (cantidad > 0),\n'
                                  '  precio_unit NUMERIC(12,2) NOT NULL\n'
                                  ');\n'
                                  '\n'
                                  '-- Duenos (ids 1..6 en este orden)\n'
                                  'INSERT INTO dueno (nombre, telefono, email) VALUES\n'
                                  "  ('Ana Gomez',      '3001112233', 'ana.gomez@mail.com'),\n"
                                  "  ('Carlos Ruiz',    '3014445566', 'carlos.ruiz@mail.com'),\n"
                                  "  ('Marcela Diaz',   '3027778899', 'marcela.diaz@mail.com'),\n"
                                  "  ('Jorge Pineda',   '3105551212', 'jorge.pineda@mail.com'),\n"
                                  "  ('Luisa Cardona',  '3123334455', 'luisa.cardona@mail.com'),\n"
                                  "  ('Andres Vallejo', '3159998877', 'andres.vallejo@mail.com');\n"
                                  '\n'
                                  '-- Veterinarios (ids 1..4)\n'
                                  'INSERT INTO veterinario (nombre, especialidad) VALUES\n'
                                  "  ('Laura Restrepo', 'General'),\n"
                                  "  ('Diego Moreno',   'Cirugia'),\n"
                                  "  ('Paula Salazar',  'Dermatologia'),\n"
                                  "  ('Ivan Ortiz',     'General');\n"
                                  '\n'
                                  '-- Mascotas (ids 1..8). Rocky (3) y Kiara (8) estan INACTIVAS.\n'
                                  'INSERT INTO mascota (id_dueno, nombre, especie, fecha_nac, '
                                  'activa) VALUES\n'
                                  "  (1, 'Firulais', 'Canino', DATE '2019-04-12', 'S'),\n"
                                  "  (1, 'Luna',     'Felino', DATE '2021-08-30', 'S'),\n"
                                  "  (2, 'Rocky',    'Canino', DATE '2015-01-20', 'N'),\n"
                                  "  (3, 'Mishi',    'Felino', DATE '2022-11-05', 'S'),\n"
                                  "  (3, 'Bobby',    'Canino', DATE '2018-06-17', 'S'),\n"
                                  "  (4, 'Nube',     'Felino', DATE '2023-02-09', 'S'),\n"
                                  "  (5, 'Toby',     'Canino', DATE '2020-09-25', 'S'),\n"
                                  "  (6, 'Kiara',    'Canino', DATE '2013-03-03', 'N');\n"
                                  '\n'
                                  '-- Citas (ids 1..10)\n'
                                  'INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                  'estado) VALUES\n'
                                  "  (1, 1, TIMESTAMP '2026-09-01 08:00:00', 'PROGRAMADA'),\n"
                                  "  (2, 1, TIMESTAMP '2026-09-01 09:00:00', 'ATENDIDA'),\n"
                                  "  (4, 2, TIMESTAMP '2026-09-01 10:00:00', 'PROGRAMADA'),\n"
                                  "  (5, 3, TIMESTAMP '2026-09-02 08:30:00', 'CANCELADA'),\n"
                                  "  (6, 2, TIMESTAMP '2026-09-02 11:00:00', 'ATENDIDA'),\n"
                                  "  (7, 4, TIMESTAMP '2026-09-03 07:45:00', 'PROGRAMADA'),\n"
                                  "  (1, 1, TIMESTAMP '2026-09-05 15:00:00', 'ATENDIDA'),\n"
                                  "  (2, 3, TIMESTAMP '2026-09-08 16:00:00', 'PROGRAMADA'),\n"
                                  "  (4, 4, TIMESTAMP '2026-09-10 08:00:00', 'PROGRAMADA'),\n"
                                  "  (6, 1, TIMESTAMP '2026-09-10 09:00:00', 'ATENDIDA');\n"
                                  '\n'
                                  '-- Consultas (ids 1..4) sobre las citas ATENDIDAS 2, 5, 7 y 10\n'
                                  'INSERT INTO consulta (id_cita, diagnostico, precio) VALUES\n'
                                  "  (2,  'Vacunacion triple felina', 40000),\n"
                                  "  (5,  'Control de peso',          38000),\n"
                                  "  (7,  'Otitis externa',           55000),\n"
                                  "  (10, 'Desparasitacion',          35000);\n"
                                  '\n'
                                  '-- Insumos (ids 1..6). Ojo: 2 y 5 tienen stock bajo a '
                                  'proposito.\n'
                                  'INSERT INTO insumo (nombre, stock, precio_unit) VALUES\n'
                                  "  ('Vacuna antirrabica',       12, 22000),\n"
                                  "  ('Vacuna triple felina',      3, 31000),\n"
                                  "  ('Antiparasitario oral',     40,  9500),\n"
                                  "  ('Suero fisiologico 500ml',  25,  7000),\n"
                                  "  ('Gasa esteril',              8,  1200),\n"
                                  "  ('Jeringa 5ml',              60,   900);\n"
                                  '\n'
                                  '-- Facturas (ids 1..3) y sus detalles\n'
                                  'INSERT INTO factura (id_consulta, fecha, total) VALUES\n'
                                  "  (1, TIMESTAMP '2026-09-01 09:40:00', 71000),\n"
                                  "  (2, TIMESTAMP '2026-09-02 11:35:00', 47000),\n"
                                  "  (3, TIMESTAMP '2026-09-05 15:50:00', 60200);\n"
                                  '\n'
                                  'INSERT INTO detalle_factura (id_factura, id_insumo, cantidad, '
                                  'precio_unit) VALUES\n'
                                  '  (1, 2, 1, 31000),\n'
                                  '  (1, 6, 1,   900),\n'
                                  '  (1, 3, 1,  9500),\n'
                                  '  (2, 3, 1,  9500),\n'
                                  '  (2, 4, 1,  7000),\n'
                                  '  (3, 1, 1, 22000),\n'
                                  '  (3, 5, 4,  1200),\n'
                                  '  (3, 6, 2,   900);\n',
                     'tipo': 'bd_sql'},
                    {'enunciado': '## 4. Checklist de avance del PI (firmada)\n'
                                  '\n'
                                  'Entrega el checklist del hito con el estado real de tu PI. '
                                  'Para **cada** item indica `SI` / `NO` / `PARCIAL`, la '
                                  '**evidencia** (nombre de archivo, de objeto de base de datos o '
                                  'numero de pregunta de ExamLab donde quedo) y una linea de '
                                  'observacion:\n'
                                  '\n'
                                  '1. Modelo ER actualizado y coherente con el DDL real.\n'
                                  '2. DDL completo de las 8 tablas con PK, FK y restricciones de '
                                  'dominio (`CHECK`).\n'
                                  '3. Plan de roles y privilegios documentado, con la matriz rol x '
                                  'objeto.\n'
                                  '4. Al menos un procedimiento de negocio con validacion '
                                  '(`sp_agendar_cita`).\n'
                                  '5. Al menos una funcion util al PI (`fn_precio_consulta` u '
                                  'otra).\n'
                                  '6. Al menos un trigger de auditoria funcionando.\n'
                                  '7. Regla de negocio "mascota inactiva no agenda" verificada con '
                                  'una prueba que falla a proposito.\n'
                                  '8. Regla de negocio "stock nunca negativo" verificada con una '
                                  'prueba que falla a proposito.\n'
                                  '9. Transaccion de facturacion atomica con rollback demostrado.\n'
                                  '10. Par de consultas antes/despues con evidencia de `EXPLAIN`.\n'
                                  '11. Al menos dos indices justificados.\n'
                                  '12. Plan de respaldo con procedimiento de restore de prueba.\n'
                                  '13. Escenarios de concurrencia documentados con su mitigacion.\n'
                                  '14. Scripts organizados y ejecutables en orden en tu carpeta '
                                  'del PI.\n'
                                  '\n'
                                  'Cierra con: **porcentaje de avance** que declaras '
                                  '(cuenta los `SI` como 1, los `PARCIAL` como 0,5), **el item mas '
                                  'debil** y una frase de compromiso firmada con tu nombre y la '
                                  'fecha (y los de los demas integrantes, si trabajas en equipo '
                                  'autorizado).',
                     'puntos': 15,
                     'rubrica': 'Los 14 items tienen estado, evidencia nombrada (archivo u objeto '
                                'concreto) y observacion. La evidencia es rastreable, no generica. '
                                'El porcentaje declarado es aritmeticamente coherente con los '
                                'estados marcados. Se identifica el item mas debil y aparece la '
                                'firma con nombre y fecha. Se descuenta por items sin evidencia o '
                                'por porcentajes que no cuadran con el checklist.',
                     'tipo': 'abierta'},
                    {'enunciado': '## 5. Lista de gaps con responsable y fecha\n'
                                  '\n'
                                  'Convierte los `NO` y `PARCIAL` de tu checklist en un **plan de '
                                  'cierre**. Entrega una tabla con **minimo 4 y maximo 8 filas**:\n'
                                  '\n'
                                  '| # | Gap (que falta exactamente) | Item del checklist | '
                                  'Impacto si no se cierra | Responsable (nombre real) | Fecha de '
                                  'cierre | Como se verificara que quedo cerrado |\n'
                                  '|---|---|---|---|---|---|---|\n'
                                  '\n'
                                  'Reglas:\n'
                                  '\n'
                                  '- El gap debe estar redactado como una tarea **verificable** '
                                  '("crear el trigger `trg_stock_no_negativo` y probarlo con dos '
                                  'casos"), no como un deseo ("mejorar los triggers").\n'
                                  '- Cada gap debe tener **un** responsable con nombre real (si '
                                  'trabajas solo, seras tu en todas las filas; si hay equipo '
                                  'autorizado, reparte, pero nunca escribas "el equipo").\n'
                                  '- Las fechas deben ser anteriores a la sustentacion final del '
                                  'PI.\n'
                                  '- La columna de verificacion debe nombrar la **evidencia '
                                  'concreta** (una consulta, un script, una captura de `EXPLAIN`, '
                                  'una fila en `audit_cita`).\n'
                                  '\n'
                                  'Debajo de la tabla, responde en 3 a 5 lineas: **cual es el '
                                  'riesgo mas grande** para llegar a la sustentacion y cual es tu '
                                  '**plan B** si ese gap no se cierra (por ejemplo: documentar el '
                                  'limite y presentar la mitigacion en papel en lugar de '
                                  'ejecutada).',
                     'puntos': 10,
                     'rubrica': 'La tabla tiene entre 4 y 8 gaps, cada uno redactado como tarea '
                                'verificable, con un unico responsable nombrado, fecha anterior a '
                                'la sustentacion y evidencia concreta de cierre. Los gaps '
                                'corresponden efectivamente a los NO y PARCIAL del checklist de la '
                                'pregunta 4. El plan B es realista y especifico.',
                     'tipo': 'abierta'}],
      'resumen': 'El estudiante ejecuta la bateria de verificacion del avance de VetCare '
                 '(integridad, reglas de negocio y auditoria), entrega el ER consolidado, los '
                 'reportes de la demo, el checklist firmado y la lista de gaps.',
      'titulo': 'Taller Clase 11 en ExamLab - Avance del PI VetCare DB (hito formal)'},
 12: {'preguntas': [{'enunciado': '## 1. La capa de API de VetCare: tres operaciones con contrato '
                                  'uniforme\n'
                                  '\n'
                                  'Regla de oro del PI: **la aplicacion nunca hace `INSERT`, '
                                  '`UPDATE` ni `DELETE` directo** sobre `cita`, `consulta` o '
                                  '`factura`. Solo invoca funciones publicadas por la base. Aqui '
                                  'construyes esa capa.\n'
                                  '\n'
                                  'Esquema completo de VetCare creado y poblado. Recuerda: '
                                  'mascotas 3 (Rocky) y 8 (Kiara) estan **inactivas**; el '
                                  'veterinario 1 tiene cita el `2026-09-01 08:00:00`; las citas 2, '
                                  '5, 7 y 10 ya tienen consulta; la cita 4 esta `CANCELADA`; el '
                                  'insumo 2 tiene stock 3.\n'
                                  '\n'
                                  'Crea **tres funciones** que comparten el **mismo contrato de '
                                  'retorno**:\n'
                                  '\n'
                                  '```sql\n'
                                  'RETURNS TABLE (ok BOOLEAN, mensaje TEXT, id_generado INT)\n'
                                  '```\n'
                                  '\n'
                                  'Cada funcion debe **capturar sus propios errores** con un '
                                  'bloque `EXCEPTION WHEN OTHERS THEN RETURN QUERY SELECT FALSE, '
                                  'SQLERRM, NULL::INT;` para que la aplicacion **nunca** reciba '
                                  'una excepcion cruda, sino siempre una fila con `ok`, `mensaje` '
                                  'e `id_generado`.\n'
                                  '\n'
                                  '1. **`api_agendar_cita(p_id_mascota INT, p_id_veterinario INT, '
                                  'p_fecha_hora TIMESTAMP)`**\n'
                                  '   Valida: mascota existe, mascota activa, franja del '
                                  "veterinario libre (estado distinto de `'CANCELADA'`). Inserta "
                                  'la cita y devuelve `TRUE`, un mensaje de exito y el `id_cita` '
                                  'generado (usa `RETURNING id_cita INTO`).\n'
                                  '\n'
                                  '2. **`api_registrar_consulta(p_id_cita INT, p_diagnostico TEXT, '
                                  'p_precio NUMERIC)`**\n'
                                  '   Valida: cita existe, cita no `CANCELADA`, cita sin consulta '
                                  'previa, precio mayor que 0. Inserta la consulta, pasa la cita a '
                                  "`'ATENDIDA'` y devuelve el `id_consulta`.\n"
                                  '\n'
                                  '3. **`api_facturar(p_id_consulta INT, p_id_insumo INT, '
                                  'p_cantidad INT)`** (una linea por llamada, para simplificar)\n'
                                  '   Valida: consulta existe, cantidad mayor que 0 y stock '
                                  'suficiente usando `UPDATE insumo SET stock = stock - p_cantidad '
                                  'WHERE id_insumo = p_id_insumo AND stock >= p_cantidad` con `GET '
                                  'DIAGNOSTICS ... ROW_COUNT`. Crea la `factura`, su '
                                  '`detalle_factura` y devuelve el `id_factura`.\n'
                                  '\n'
                                  '**Demuestra el contrato** ejecutando las seis llamadas '
                                  'siguientes, **todas con `SELECT`** (nunca deben lanzar error, '
                                  'siempre devuelven una fila):\n'
                                  '\n'
                                  '```sql\n'
                                  "SELECT * FROM api_agendar_cita(1, 2, TIMESTAMP '2026-10-01 "
                                  "09:00:00');   -- ok = true\n"
                                  "SELECT * FROM api_agendar_cita(3, 2, TIMESTAMP '2026-10-01 "
                                  "10:00:00');   -- ok = false, inactiva\n"
                                  "SELECT * FROM api_registrar_consulta(1, 'Vacunacion anual', "
                                  '45000);      -- ok = true\n'
                                  "SELECT * FROM api_registrar_consulta(4, 'Revision', "
                                  '30000);              -- ok = false, cancelada\n'
                                  'SELECT * FROM api_facturar(1, 6, '
                                  '2);                                     -- ok = true\n'
                                  'SELECT * FROM api_facturar(1, 2, '
                                  '10);                                    -- ok = false, sin '
                                  'stock\n'
                                  '```',
                     'puntos': 28,
                     'rubrica': 'Las 3 funciones se crean con el contrato exacto RETURNS TABLE (ok '
                                'BOOLEAN, mensaje TEXT, id_generado INT) y capturan sus errores '
                                'para no propagar excepciones. Cada una aplica sus validaciones y '
                                'devuelve el id generado con RETURNING en el caso exitoso. Las 6 '
                                'llamadas devuelven fila sin lanzar error, con ok true/false segun '
                                'corresponde y mensaje informativo. api_facturar usa el UPDATE '
                                'condicional con GET DIAGNOSTICS ROW_COUNT.',
                     'setup_sql': 'CREATE TABLE dueno (\n'
                                  '  id_dueno SERIAL PRIMARY KEY,\n'
                                  '  nombre TEXT NOT NULL,\n'
                                  '  telefono TEXT,\n'
                                  '  email TEXT,\n'
                                  "  ciudad TEXT DEFAULT 'Cali'\n"
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE mascota (\n'
                                  '  id_mascota SERIAL PRIMARY KEY,\n'
                                  '  id_dueno INT NOT NULL REFERENCES dueno(id_dueno),\n'
                                  '  nombre TEXT NOT NULL,\n'
                                  '  especie TEXT NOT NULL,\n'
                                  '  fecha_nac DATE,\n'
                                  "  activa CHAR(1) NOT NULL DEFAULT 'S' CHECK (activa IN "
                                  "('S','N'))\n"
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE veterinario (\n'
                                  '  id_veterinario SERIAL PRIMARY KEY,\n'
                                  '  nombre TEXT NOT NULL,\n'
                                  '  especialidad TEXT,\n'
                                  "  activo CHAR(1) NOT NULL DEFAULT 'S' CHECK (activo IN "
                                  "('S','N'))\n"
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE cita (\n'
                                  '  id_cita SERIAL PRIMARY KEY,\n'
                                  '  id_mascota INT NOT NULL REFERENCES mascota(id_mascota),\n'
                                  '  id_veterinario INT NOT NULL REFERENCES '
                                  'veterinario(id_veterinario),\n'
                                  '  fecha_hora TIMESTAMP NOT NULL,\n'
                                  "  estado TEXT NOT NULL DEFAULT 'PROGRAMADA'\n"
                                  "    CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))\n"
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE consulta (\n'
                                  '  id_consulta SERIAL PRIMARY KEY,\n'
                                  '  id_cita INT NOT NULL UNIQUE REFERENCES cita(id_cita),\n'
                                  '  diagnostico TEXT,\n'
                                  '  precio NUMERIC(12,2) NOT NULL CHECK (precio >= 0)\n'
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE insumo (\n'
                                  '  id_insumo SERIAL PRIMARY KEY,\n'
                                  '  nombre TEXT NOT NULL,\n'
                                  '  stock INT NOT NULL CHECK (stock >= 0),\n'
                                  '  precio_unit NUMERIC(12,2) NOT NULL\n'
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE factura (\n'
                                  '  id_factura SERIAL PRIMARY KEY,\n'
                                  '  id_consulta INT NOT NULL REFERENCES consulta(id_consulta),\n'
                                  '  fecha TIMESTAMP NOT NULL DEFAULT now(),\n'
                                  '  total NUMERIC(12,2) NOT NULL DEFAULT 0\n'
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE detalle_factura (\n'
                                  '  id_detalle SERIAL PRIMARY KEY,\n'
                                  '  id_factura INT NOT NULL REFERENCES factura(id_factura) ON '
                                  'DELETE CASCADE,\n'
                                  '  id_insumo INT NOT NULL REFERENCES insumo(id_insumo),\n'
                                  '  cantidad INT NOT NULL CHECK (cantidad > 0),\n'
                                  '  precio_unit NUMERIC(12,2) NOT NULL\n'
                                  ');\n'
                                  '\n'
                                  '-- Duenos (ids 1..6 en este orden)\n'
                                  'INSERT INTO dueno (nombre, telefono, email) VALUES\n'
                                  "  ('Ana Gomez',      '3001112233', 'ana.gomez@mail.com'),\n"
                                  "  ('Carlos Ruiz',    '3014445566', 'carlos.ruiz@mail.com'),\n"
                                  "  ('Marcela Diaz',   '3027778899', 'marcela.diaz@mail.com'),\n"
                                  "  ('Jorge Pineda',   '3105551212', 'jorge.pineda@mail.com'),\n"
                                  "  ('Luisa Cardona',  '3123334455', 'luisa.cardona@mail.com'),\n"
                                  "  ('Andres Vallejo', '3159998877', 'andres.vallejo@mail.com');\n"
                                  '\n'
                                  '-- Veterinarios (ids 1..4)\n'
                                  'INSERT INTO veterinario (nombre, especialidad) VALUES\n'
                                  "  ('Laura Restrepo', 'General'),\n"
                                  "  ('Diego Moreno',   'Cirugia'),\n"
                                  "  ('Paula Salazar',  'Dermatologia'),\n"
                                  "  ('Ivan Ortiz',     'General');\n"
                                  '\n'
                                  '-- Mascotas (ids 1..8). Rocky (3) y Kiara (8) estan INACTIVAS.\n'
                                  'INSERT INTO mascota (id_dueno, nombre, especie, fecha_nac, '
                                  'activa) VALUES\n'
                                  "  (1, 'Firulais', 'Canino', DATE '2019-04-12', 'S'),\n"
                                  "  (1, 'Luna',     'Felino', DATE '2021-08-30', 'S'),\n"
                                  "  (2, 'Rocky',    'Canino', DATE '2015-01-20', 'N'),\n"
                                  "  (3, 'Mishi',    'Felino', DATE '2022-11-05', 'S'),\n"
                                  "  (3, 'Bobby',    'Canino', DATE '2018-06-17', 'S'),\n"
                                  "  (4, 'Nube',     'Felino', DATE '2023-02-09', 'S'),\n"
                                  "  (5, 'Toby',     'Canino', DATE '2020-09-25', 'S'),\n"
                                  "  (6, 'Kiara',    'Canino', DATE '2013-03-03', 'N');\n"
                                  '\n'
                                  '-- Citas (ids 1..10)\n'
                                  'INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                  'estado) VALUES\n'
                                  "  (1, 1, TIMESTAMP '2026-09-01 08:00:00', 'PROGRAMADA'),\n"
                                  "  (2, 1, TIMESTAMP '2026-09-01 09:00:00', 'ATENDIDA'),\n"
                                  "  (4, 2, TIMESTAMP '2026-09-01 10:00:00', 'PROGRAMADA'),\n"
                                  "  (5, 3, TIMESTAMP '2026-09-02 08:30:00', 'CANCELADA'),\n"
                                  "  (6, 2, TIMESTAMP '2026-09-02 11:00:00', 'ATENDIDA'),\n"
                                  "  (7, 4, TIMESTAMP '2026-09-03 07:45:00', 'PROGRAMADA'),\n"
                                  "  (1, 1, TIMESTAMP '2026-09-05 15:00:00', 'ATENDIDA'),\n"
                                  "  (2, 3, TIMESTAMP '2026-09-08 16:00:00', 'PROGRAMADA'),\n"
                                  "  (4, 4, TIMESTAMP '2026-09-10 08:00:00', 'PROGRAMADA'),\n"
                                  "  (6, 1, TIMESTAMP '2026-09-10 09:00:00', 'ATENDIDA');\n"
                                  '\n'
                                  '-- Consultas (ids 1..4) sobre las citas ATENDIDAS 2, 5, 7 y 10\n'
                                  'INSERT INTO consulta (id_cita, diagnostico, precio) VALUES\n'
                                  "  (2,  'Vacunacion triple felina', 40000),\n"
                                  "  (5,  'Control de peso',          38000),\n"
                                  "  (7,  'Otitis externa',           55000),\n"
                                  "  (10, 'Desparasitacion',          35000);\n"
                                  '\n'
                                  '-- Insumos (ids 1..6). Ojo: 2 y 5 tienen stock bajo a '
                                  'proposito.\n'
                                  'INSERT INTO insumo (nombre, stock, precio_unit) VALUES\n'
                                  "  ('Vacuna antirrabica',       12, 22000),\n"
                                  "  ('Vacuna triple felina',      3, 31000),\n"
                                  "  ('Antiparasitario oral',     40,  9500),\n"
                                  "  ('Suero fisiologico 500ml',  25,  7000),\n"
                                  "  ('Gasa esteril',              8,  1200),\n"
                                  "  ('Jeringa 5ml',              60,   900);\n"
                                  '\n'
                                  '-- Facturas (ids 1..3) y sus detalles\n'
                                  'INSERT INTO factura (id_consulta, fecha, total) VALUES\n'
                                  "  (1, TIMESTAMP '2026-09-01 09:40:00', 71000),\n"
                                  "  (2, TIMESTAMP '2026-09-02 11:35:00', 47000),\n"
                                  "  (3, TIMESTAMP '2026-09-05 15:50:00', 60200);\n"
                                  '\n'
                                  'INSERT INTO detalle_factura (id_factura, id_insumo, cantidad, '
                                  'precio_unit) VALUES\n'
                                  '  (1, 2, 1, 31000),\n'
                                  '  (1, 6, 1,   900),\n'
                                  '  (1, 3, 1,  9500),\n'
                                  '  (2, 3, 1,  9500),\n'
                                  '  (2, 4, 1,  7000),\n'
                                  '  (3, 1, 1, 22000),\n'
                                  '  (3, 5, 4,  1200),\n'
                                  '  (3, 6, 2,   900);\n',
                     'tipo': 'bd_sql'},
                    {'enunciado': '## 2. El cliente de la aplicacion: consumir la API con '
                                  'parametros ligados\n'
                                  '\n'
                                  'Escribe el modulo de acceso a datos de la aplicacion de '
                                  'Huellitas en **Python** con `psycopg2`. No se ejecuta contra la '
                                  'base: se evalua el **codigo**, y sobre todo que respete el '
                                  'contrato y las buenas practicas.\n'
                                  '\n'
                                  'Requisitos obligatorios:\n'
                                  '\n'
                                  '1. Una funcion por operacion: `agendar_cita(conn, id_mascota, '
                                  'id_veterinario, fecha_hora)`, `registrar_consulta(conn, '
                                  'id_cita, diagnostico, precio)` y `facturar(conn, id_consulta, '
                                  'id_insumo, cantidad)`.\n'
                                  '2. **Parametros ligados siempre**: `cur.execute("SELECT ok, '
                                  'mensaje, id_generado FROM api_agendar_cita(%s, %s, %s)", '
                                  '(id_mascota, id_veterinario, fecha_hora))`. **Prohibido** '
                                  'construir SQL concatenando cadenas o con f-strings: es la '
                                  'puerta de la inyeccion SQL.\n'
                                  '3. Cada funcion lee la unica fila del resultado y **devuelve el '
                                  'contrato como un objeto propio de la aplicacion**: un '
                                  '`dataclass` `Resultado(ok: bool, mensaje: str, id_generado: int '
                                  '| None)`.\n'
                                  '4. **Ningun `INSERT` directo** a `cita`, `consulta` o `factura` '
                                  'en todo el archivo.\n'
                                  '5. Manejo de transaccion y de errores: `conn.commit()` cuando '
                                  '`ok` es verdadero, `conn.rollback()` cuando es falso o cuando '
                                  '`psycopg2` lanza una excepcion; usa `with conn.cursor() as '
                                  'cur:` y captura `psycopg2.Error`.\n'
                                  '6. Una funcion `flujo_atencion(conn, id_mascota, '
                                  'id_veterinario, fecha_hora, diagnostico, precio, id_insumo, '
                                  'cantidad)` que orqueste el caso de uso completo (agendar -> '
                                  'registrar consulta -> facturar) y que **se detenga en el primer '
                                  '`ok = False`** devolviendo el mensaje al usuario, sin continuar '
                                  'los pasos siguientes.\n'
                                  '7. Un `if __name__ == "__main__":` que muestre en consola un '
                                  'caso exitoso y un caso rechazado (mascota inactiva), '
                                  'imprimiendo el mensaje que le llegaria al usuario final.',
                     'lenguaje': 'python',
                     'puntos': 17,
                     'rubrica': 'Las 3 funciones existen con la firma pedida y usan exclusivamente '
                                'parametros ligados con %s; no hay concatenacion ni f-strings en '
                                'el SQL, ni INSERT directo a cita/consulta/factura. El dataclass '
                                'Resultado traduce el contrato de la base. Hay commit/rollback '
                                'segun ok y captura de psycopg2.Error. flujo_atencion corta en el '
                                'primer ok = False y el bloque main muestra un caso exitoso y uno '
                                'rechazado.',
                     'starter': '"""Capa de acceso a datos de la app VetCare (Huellitas).\n'
                                'Regla del PI: la app NUNCA hace INSERT/UPDATE/DELETE directo '
                                'sobre\n'
                                'cita, consulta ni factura. Solo invoca las funciones api_*.\n'
                                '"""\n'
                                'from dataclasses import dataclass\n'
                                '\n'
                                'import psycopg2\n'
                                '\n'
                                '\n'
                                '@dataclass\n'
                                'class Resultado:\n'
                                '    ok: bool\n'
                                '    mensaje: str\n'
                                '    id_generado: int | None\n'
                                '\n'
                                '\n'
                                'def agendar_cita(conn, id_mascota: int, id_veterinario: int, '
                                'fecha_hora) -> Resultado:\n'
                                '    # TODO: SELECT ok, mensaje, id_generado FROM '
                                'api_agendar_cita(%s, %s, %s)\n'
                                '    #       parametros ligados, commit si ok, rollback si no\n'
                                '    ...\n'
                                '\n'
                                '\n'
                                'def registrar_consulta(conn, id_cita: int, diagnostico: str, '
                                'precio) -> Resultado:\n'
                                '    ...\n'
                                '\n'
                                '\n'
                                'def facturar(conn, id_consulta: int, id_insumo: int, cantidad: '
                                'int) -> Resultado:\n'
                                '    ...\n'
                                '\n'
                                '\n'
                                'def flujo_atencion(conn, id_mascota, id_veterinario, fecha_hora,\n'
                                '                   diagnostico, precio, id_insumo, cantidad) -> '
                                'Resultado:\n'
                                '    # TODO: agendar -> registrar consulta -> facturar, cortando '
                                'en el primer ok = False\n'
                                '    ...\n'
                                '\n'
                                '\n'
                                'if __name__ == "__main__":\n'
                                '    ...\n',
                     'tipo': 'codigo'},
                    {'enunciado': '## 3. Flujo app -> BD del caso de uso "atender una mascota"\n'
                                  '\n'
                                  'Dibuja con `sequenceDiagram` de Mermaid el flujo completo del '
                                  'caso de uso, mostrando **quien llama a quien** y **que '
                                  'devuelve**. Participantes obligatorios: la recepcionista, la '
                                  'aplicacion, la capa de API de la base (las funciones `api_*`) y '
                                  'las tablas.\n'
                                  '\n'
                                  'El diagrama debe mostrar, como minimo:\n'
                                  '\n'
                                  '1. La recepcionista pide una cita y la aplicacion invoca '
                                  '`api_agendar_cita(...)` con **parametros ligados**.\n'
                                  '2. La base responde con el contrato `(ok, mensaje, '
                                  'id_generado)`.\n'
                                  '3. Una **rama de error**: cuando `ok = false` (mascota inactiva '
                                  'o franja ocupada), la aplicacion muestra el mensaje y **no** '
                                  'contina. Usa `alt` / `else` de Mermaid.\n'
                                  '4. El camino feliz siguiendo con `api_registrar_consulta(...)` '
                                  'y `api_facturar(...)`, indicando que `api_facturar` descuenta '
                                  'stock de forma atomica.\n'
                                  '5. Una nota (`Note over`) que deje escrita la regla del PI: la '
                                  'aplicacion no hace `INSERT` directo.',
                     'mermaid_esperado': 'sequenceDiagram\n'
                                         '    actor R as Recepcionista\n'
                                         '    participant APP as App VetCare\n'
                                         '    participant API as Capa api_* (PL/pgSQL)\n'
                                         '    participant DB as Tablas VetCare\n'
                                         '    Note over APP,API: La app NUNCA hace INSERT directo: '
                                         'solo llama api_*\n'
                                         '    R->>APP: Solicita cita para Firulais con Diego '
                                         'Moreno\n'
                                         '    APP->>API: SELECT * FROM api_agendar_cita($1, $2, '
                                         '$3)\n'
                                         '    API->>DB: valida mascota activa y franja libre\n'
                                         '    DB-->>API: resultado de las validaciones\n'
                                         '    API-->>APP: (ok, mensaje, id_generado)\n'
                                         '    alt ok = false\n'
                                         '        APP-->>R: Muestra mensaje y ofrece otra franja\n'
                                         '    else ok = true\n'
                                         '        APP-->>R: Cita confirmada con id_generado\n'
                                         '        R->>APP: Registra atencion del veterinario\n'
                                         '        APP->>API: SELECT * FROM '
                                         'api_registrar_consulta($1, $2, $3)\n'
                                         '        API->>DB: INSERT consulta + UPDATE cita a '
                                         'ATENDIDA\n'
                                         '        API-->>APP: (ok, mensaje, id_consulta)\n'
                                         '        R->>APP: Cobra insumos utilizados\n'
                                         '        APP->>API: SELECT * FROM api_facturar($1, $2, '
                                         '$3)\n'
                                         '        API->>DB: INSERT factura y detalle + UPDATE '
                                         'stock atomico\n'
                                         '        API-->>APP: (ok, mensaje, id_factura)\n'
                                         '        APP-->>R: Factura impresa\n'
                                         '    end',
                     'puntos': 12,
                     'rubrica': 'El sequenceDiagram renderiza sin error e incluye los 4 '
                                'participantes. Se ven las 3 invocaciones api_* con sus parametros '
                                'y el retorno del contrato (ok, mensaje, id_generado). Existe un '
                                'bloque alt/else que representa el corte cuando ok es falso. '
                                'Aparece la nota con la regla de no hacer INSERT directo. Se '
                                'descuenta si el diagrama muestra a la aplicacion escribiendo '
                                'directamente en las tablas.',
                     'tipo': 'diagrama'},
                    {'enunciado': '## 4. Blindar la API: la aplicacion solo puede EXECUTE\n'
                                  '\n'
                                  'Esta base ya trae las tres funciones `api_agendar_cita`, '
                                  '`api_registrar_consulta` y `api_facturar` creadas, junto con el '
                                  'esquema y los datos.\n'
                                  '\n'
                                  'Vas a aplicar privilegio minimo al usuario que usara la '
                                  'aplicacion. Escribe el SQL que:\n'
                                  '\n'
                                  '1. Cree el rol `app_vetcare` con `NOLOGIN`.\n'
                                  '2. **Cierre la puerta grande**: revoca de `app_vetcare` '
                                  'cualquier privilegio de escritura directa sobre las tablas de '
                                  'negocio:\n'
                                  '   `REVOKE INSERT, UPDATE, DELETE ON cita, consulta, factura, '
                                  'detalle_factura, insumo FROM app_vetcare;`\n'
                                  '   (Aunque sea redundante porque nunca se otorgo, la sentencia '
                                  'queda como evidencia explicita de la decision de diseno.)\n'
                                  '3. **Punto clave que casi todos olvidan**: en PostgreSQL las '
                                  'funciones nuevas quedan con `EXECUTE` otorgado a `PUBLIC` por '
                                  'defecto. Revocalo para las tres funciones:\n'
                                  '   `REVOKE EXECUTE ON FUNCTION api_agendar_cita(INT, INT, '
                                  'TIMESTAMP) FROM PUBLIC;` y lo equivalente para las otras dos, '
                                  'respetando su firma exacta (`api_registrar_consulta(INT, TEXT, '
                                  'NUMERIC)`, `api_facturar(INT, INT, INT)`).\n'
                                  '4. Otorgue `EXECUTE` de las tres funciones **solo** a '
                                  '`app_vetcare`.\n'
                                  '5. Otorgue a `app_vetcare` unicamente el `SELECT` que necesita '
                                  'para pintar pantallas: sobre `dueno`, `mascota`, `veterinario` '
                                  'y `cita`. Nada mas.\n'
                                  '6. **Verifique** con dos consultas:\n'
                                  '   - `SELECT grantee, routine_name, privilege_type FROM '
                                  'information_schema.routine_privileges WHERE routine_name LIKE '
                                  "'api_%' ORDER BY routine_name, grantee;`\n"
                                  '   - `SELECT grantee, table_name, privilege_type FROM '
                                  'information_schema.role_table_grants WHERE grantee = '
                                  "'app_vetcare' ORDER BY table_name, privilege_type;`\n"
                                  '7. Cierre con un comentario `--` de dos lineas explicando por '
                                  'que este esquema de permisos hace **imposible** que un error de '
                                  'la aplicacion salte las validaciones de negocio.',
                     'puntos': 13,
                     'rubrica': 'Se crea el rol app_vetcare y se ejecutan el REVOKE de escritura '
                                'sobre las tablas, el REVOKE EXECUTE ... FROM PUBLIC de las tres '
                                'funciones con su firma correcta y el GRANT EXECUTE solo a '
                                'app_vetcare. Los SELECT otorgados se limitan a las 4 tablas de '
                                'lectura pedidas. Las dos consultas de verificacion devuelven '
                                'filas que evidencian la configuracion. El comentario final '
                                'explica correctamente por que la app no puede saltar las '
                                'validaciones.',
                     'setup_sql': 'CREATE TABLE dueno (\n'
                                  '  id_dueno SERIAL PRIMARY KEY,\n'
                                  '  nombre TEXT NOT NULL,\n'
                                  '  telefono TEXT,\n'
                                  '  email TEXT,\n'
                                  "  ciudad TEXT DEFAULT 'Cali'\n"
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE mascota (\n'
                                  '  id_mascota SERIAL PRIMARY KEY,\n'
                                  '  id_dueno INT NOT NULL REFERENCES dueno(id_dueno),\n'
                                  '  nombre TEXT NOT NULL,\n'
                                  '  especie TEXT NOT NULL,\n'
                                  '  fecha_nac DATE,\n'
                                  "  activa CHAR(1) NOT NULL DEFAULT 'S' CHECK (activa IN "
                                  "('S','N'))\n"
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE veterinario (\n'
                                  '  id_veterinario SERIAL PRIMARY KEY,\n'
                                  '  nombre TEXT NOT NULL,\n'
                                  '  especialidad TEXT,\n'
                                  "  activo CHAR(1) NOT NULL DEFAULT 'S' CHECK (activo IN "
                                  "('S','N'))\n"
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE cita (\n'
                                  '  id_cita SERIAL PRIMARY KEY,\n'
                                  '  id_mascota INT NOT NULL REFERENCES mascota(id_mascota),\n'
                                  '  id_veterinario INT NOT NULL REFERENCES '
                                  'veterinario(id_veterinario),\n'
                                  '  fecha_hora TIMESTAMP NOT NULL,\n'
                                  "  estado TEXT NOT NULL DEFAULT 'PROGRAMADA'\n"
                                  "    CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))\n"
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE consulta (\n'
                                  '  id_consulta SERIAL PRIMARY KEY,\n'
                                  '  id_cita INT NOT NULL UNIQUE REFERENCES cita(id_cita),\n'
                                  '  diagnostico TEXT,\n'
                                  '  precio NUMERIC(12,2) NOT NULL CHECK (precio >= 0)\n'
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE insumo (\n'
                                  '  id_insumo SERIAL PRIMARY KEY,\n'
                                  '  nombre TEXT NOT NULL,\n'
                                  '  stock INT NOT NULL CHECK (stock >= 0),\n'
                                  '  precio_unit NUMERIC(12,2) NOT NULL\n'
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE factura (\n'
                                  '  id_factura SERIAL PRIMARY KEY,\n'
                                  '  id_consulta INT NOT NULL REFERENCES consulta(id_consulta),\n'
                                  '  fecha TIMESTAMP NOT NULL DEFAULT now(),\n'
                                  '  total NUMERIC(12,2) NOT NULL DEFAULT 0\n'
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE detalle_factura (\n'
                                  '  id_detalle SERIAL PRIMARY KEY,\n'
                                  '  id_factura INT NOT NULL REFERENCES factura(id_factura) ON '
                                  'DELETE CASCADE,\n'
                                  '  id_insumo INT NOT NULL REFERENCES insumo(id_insumo),\n'
                                  '  cantidad INT NOT NULL CHECK (cantidad > 0),\n'
                                  '  precio_unit NUMERIC(12,2) NOT NULL\n'
                                  ');\n'
                                  '\n'
                                  '-- Duenos (ids 1..6 en este orden)\n'
                                  'INSERT INTO dueno (nombre, telefono, email) VALUES\n'
                                  "  ('Ana Gomez',      '3001112233', 'ana.gomez@mail.com'),\n"
                                  "  ('Carlos Ruiz',    '3014445566', 'carlos.ruiz@mail.com'),\n"
                                  "  ('Marcela Diaz',   '3027778899', 'marcela.diaz@mail.com'),\n"
                                  "  ('Jorge Pineda',   '3105551212', 'jorge.pineda@mail.com'),\n"
                                  "  ('Luisa Cardona',  '3123334455', 'luisa.cardona@mail.com'),\n"
                                  "  ('Andres Vallejo', '3159998877', 'andres.vallejo@mail.com');\n"
                                  '\n'
                                  '-- Veterinarios (ids 1..4)\n'
                                  'INSERT INTO veterinario (nombre, especialidad) VALUES\n'
                                  "  ('Laura Restrepo', 'General'),\n"
                                  "  ('Diego Moreno',   'Cirugia'),\n"
                                  "  ('Paula Salazar',  'Dermatologia'),\n"
                                  "  ('Ivan Ortiz',     'General');\n"
                                  '\n'
                                  '-- Mascotas (ids 1..8). Rocky (3) y Kiara (8) estan INACTIVAS.\n'
                                  'INSERT INTO mascota (id_dueno, nombre, especie, fecha_nac, '
                                  'activa) VALUES\n'
                                  "  (1, 'Firulais', 'Canino', DATE '2019-04-12', 'S'),\n"
                                  "  (1, 'Luna',     'Felino', DATE '2021-08-30', 'S'),\n"
                                  "  (2, 'Rocky',    'Canino', DATE '2015-01-20', 'N'),\n"
                                  "  (3, 'Mishi',    'Felino', DATE '2022-11-05', 'S'),\n"
                                  "  (3, 'Bobby',    'Canino', DATE '2018-06-17', 'S'),\n"
                                  "  (4, 'Nube',     'Felino', DATE '2023-02-09', 'S'),\n"
                                  "  (5, 'Toby',     'Canino', DATE '2020-09-25', 'S'),\n"
                                  "  (6, 'Kiara',    'Canino', DATE '2013-03-03', 'N');\n"
                                  '\n'
                                  '-- Citas (ids 1..10)\n'
                                  'INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                  'estado) VALUES\n'
                                  "  (1, 1, TIMESTAMP '2026-09-01 08:00:00', 'PROGRAMADA'),\n"
                                  "  (2, 1, TIMESTAMP '2026-09-01 09:00:00', 'ATENDIDA'),\n"
                                  "  (4, 2, TIMESTAMP '2026-09-01 10:00:00', 'PROGRAMADA'),\n"
                                  "  (5, 3, TIMESTAMP '2026-09-02 08:30:00', 'CANCELADA'),\n"
                                  "  (6, 2, TIMESTAMP '2026-09-02 11:00:00', 'ATENDIDA'),\n"
                                  "  (7, 4, TIMESTAMP '2026-09-03 07:45:00', 'PROGRAMADA'),\n"
                                  "  (1, 1, TIMESTAMP '2026-09-05 15:00:00', 'ATENDIDA'),\n"
                                  "  (2, 3, TIMESTAMP '2026-09-08 16:00:00', 'PROGRAMADA'),\n"
                                  "  (4, 4, TIMESTAMP '2026-09-10 08:00:00', 'PROGRAMADA'),\n"
                                  "  (6, 1, TIMESTAMP '2026-09-10 09:00:00', 'ATENDIDA');\n"
                                  '\n'
                                  '-- Consultas (ids 1..4) sobre las citas ATENDIDAS 2, 5, 7 y 10\n'
                                  'INSERT INTO consulta (id_cita, diagnostico, precio) VALUES\n'
                                  "  (2,  'Vacunacion triple felina', 40000),\n"
                                  "  (5,  'Control de peso',          38000),\n"
                                  "  (7,  'Otitis externa',           55000),\n"
                                  "  (10, 'Desparasitacion',          35000);\n"
                                  '\n'
                                  '-- Insumos (ids 1..6). Ojo: 2 y 5 tienen stock bajo a '
                                  'proposito.\n'
                                  'INSERT INTO insumo (nombre, stock, precio_unit) VALUES\n'
                                  "  ('Vacuna antirrabica',       12, 22000),\n"
                                  "  ('Vacuna triple felina',      3, 31000),\n"
                                  "  ('Antiparasitario oral',     40,  9500),\n"
                                  "  ('Suero fisiologico 500ml',  25,  7000),\n"
                                  "  ('Gasa esteril',              8,  1200),\n"
                                  "  ('Jeringa 5ml',              60,   900);\n"
                                  '\n'
                                  '-- Facturas (ids 1..3) y sus detalles\n'
                                  'INSERT INTO factura (id_consulta, fecha, total) VALUES\n'
                                  "  (1, TIMESTAMP '2026-09-01 09:40:00', 71000),\n"
                                  "  (2, TIMESTAMP '2026-09-02 11:35:00', 47000),\n"
                                  "  (3, TIMESTAMP '2026-09-05 15:50:00', 60200);\n"
                                  '\n'
                                  'INSERT INTO detalle_factura (id_factura, id_insumo, cantidad, '
                                  'precio_unit) VALUES\n'
                                  '  (1, 2, 1, 31000),\n'
                                  '  (1, 6, 1,   900),\n'
                                  '  (1, 3, 1,  9500),\n'
                                  '  (2, 3, 1,  9500),\n'
                                  '  (2, 4, 1,  7000),\n'
                                  '  (3, 1, 1, 22000),\n'
                                  '  (3, 5, 4,  1200),\n'
                                  '  (3, 6, 2,   900);\n'
                                  '\n'
                                  'CREATE FUNCTION api_agendar_cita(p_id_mascota INT, '
                                  'p_id_veterinario INT, p_fecha_hora TIMESTAMP)\n'
                                  'RETURNS TABLE (ok BOOLEAN, mensaje TEXT, id_generado INT)\n'
                                  'LANGUAGE plpgsql\n'
                                  'AS $fn$\n'
                                  'DECLARE\n'
                                  '  v_activa CHAR(1);\n'
                                  '  v_ocupado INT;\n'
                                  '  v_id INT;\n'
                                  'BEGIN\n'
                                  '  SELECT activa INTO v_activa FROM mascota WHERE id_mascota = '
                                  'p_id_mascota;\n'
                                  '  IF NOT FOUND THEN\n'
                                  "    RETURN QUERY SELECT FALSE, 'La mascota no existe', "
                                  'NULL::INT;\n'
                                  '    RETURN;\n'
                                  '  END IF;\n'
                                  "  IF v_activa <> 'S' THEN\n"
                                  "    RETURN QUERY SELECT FALSE, 'La mascota esta inactiva', "
                                  'NULL::INT;\n'
                                  '    RETURN;\n'
                                  '  END IF;\n'
                                  '  SELECT COUNT(*) INTO v_ocupado FROM cita\n'
                                  '   WHERE id_veterinario = p_id_veterinario AND fecha_hora = '
                                  "p_fecha_hora AND estado <> 'CANCELADA';\n"
                                  '  IF v_ocupado > 0 THEN\n'
                                  "    RETURN QUERY SELECT FALSE, 'Franja ocupada', NULL::INT;\n"
                                  '    RETURN;\n'
                                  '  END IF;\n'
                                  '  INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                  'estado)\n'
                                  '  VALUES (p_id_mascota, p_id_veterinario, p_fecha_hora, '
                                  "'PROGRAMADA')\n"
                                  '  RETURNING id_cita INTO v_id;\n'
                                  "  RETURN QUERY SELECT TRUE, 'Cita agendada', v_id;\n"
                                  'EXCEPTION WHEN OTHERS THEN\n'
                                  '  RETURN QUERY SELECT FALSE, SQLERRM, NULL::INT;\n'
                                  'END;\n'
                                  '$fn$;\n'
                                  '\n'
                                  'CREATE FUNCTION api_registrar_consulta(p_id_cita INT, '
                                  'p_diagnostico TEXT, p_precio NUMERIC)\n'
                                  'RETURNS TABLE (ok BOOLEAN, mensaje TEXT, id_generado INT)\n'
                                  'LANGUAGE plpgsql\n'
                                  'AS $fn$\n'
                                  'DECLARE\n'
                                  '  v_estado TEXT;\n'
                                  '  v_id INT;\n'
                                  'BEGIN\n'
                                  '  SELECT estado INTO v_estado FROM cita WHERE id_cita = '
                                  'p_id_cita;\n'
                                  '  IF NOT FOUND THEN\n'
                                  "    RETURN QUERY SELECT FALSE, 'La cita no existe', NULL::INT;\n"
                                  '    RETURN;\n'
                                  '  END IF;\n'
                                  "  IF v_estado = 'CANCELADA' THEN\n"
                                  "    RETURN QUERY SELECT FALSE, 'La cita esta cancelada', "
                                  'NULL::INT;\n'
                                  '    RETURN;\n'
                                  '  END IF;\n'
                                  '  IF EXISTS (SELECT 1 FROM consulta WHERE id_cita = p_id_cita) '
                                  'THEN\n'
                                  "    RETURN QUERY SELECT FALSE, 'La cita ya tiene consulta', "
                                  'NULL::INT;\n'
                                  '    RETURN;\n'
                                  '  END IF;\n'
                                  '  IF p_precio IS NULL OR p_precio <= 0 THEN\n'
                                  "    RETURN QUERY SELECT FALSE, 'Precio invalido', NULL::INT;\n"
                                  '    RETURN;\n'
                                  '  END IF;\n'
                                  '  INSERT INTO consulta (id_cita, diagnostico, precio)\n'
                                  '  VALUES (p_id_cita, p_diagnostico, p_precio)\n'
                                  '  RETURNING id_consulta INTO v_id;\n'
                                  "  UPDATE cita SET estado = 'ATENDIDA' WHERE id_cita = "
                                  'p_id_cita;\n'
                                  "  RETURN QUERY SELECT TRUE, 'Consulta registrada', v_id;\n"
                                  'EXCEPTION WHEN OTHERS THEN\n'
                                  '  RETURN QUERY SELECT FALSE, SQLERRM, NULL::INT;\n'
                                  'END;\n'
                                  '$fn$;\n'
                                  '\n'
                                  'CREATE FUNCTION api_facturar(p_id_consulta INT, p_id_insumo '
                                  'INT, p_cantidad INT)\n'
                                  'RETURNS TABLE (ok BOOLEAN, mensaje TEXT, id_generado INT)\n'
                                  'LANGUAGE plpgsql\n'
                                  'AS $fn$\n'
                                  'DECLARE\n'
                                  '  v_precio NUMERIC(12,2);\n'
                                  '  v_filas INT;\n'
                                  '  v_id INT;\n'
                                  'BEGIN\n'
                                  '  IF NOT EXISTS (SELECT 1 FROM consulta WHERE id_consulta = '
                                  'p_id_consulta) THEN\n'
                                  "    RETURN QUERY SELECT FALSE, 'La consulta no existe', "
                                  'NULL::INT;\n'
                                  '    RETURN;\n'
                                  '  END IF;\n'
                                  '  IF p_cantidad IS NULL OR p_cantidad <= 0 THEN\n'
                                  "    RETURN QUERY SELECT FALSE, 'Cantidad invalida', NULL::INT;\n"
                                  '    RETURN;\n'
                                  '  END IF;\n'
                                  '  SELECT precio_unit INTO v_precio FROM insumo WHERE id_insumo '
                                  '= p_id_insumo;\n'
                                  '  IF NOT FOUND THEN\n'
                                  "    RETURN QUERY SELECT FALSE, 'El insumo no existe', "
                                  'NULL::INT;\n'
                                  '    RETURN;\n'
                                  '  END IF;\n'
                                  '  UPDATE insumo SET stock = stock - p_cantidad\n'
                                  '   WHERE id_insumo = p_id_insumo AND stock >= p_cantidad;\n'
                                  '  GET DIAGNOSTICS v_filas = ROW_COUNT;\n'
                                  '  IF v_filas = 0 THEN\n'
                                  "    RETURN QUERY SELECT FALSE, 'Stock insuficiente', "
                                  'NULL::INT;\n'
                                  '    RETURN;\n'
                                  '  END IF;\n'
                                  '  INSERT INTO factura (id_consulta, total) VALUES '
                                  '(p_id_consulta, v_precio * p_cantidad)\n'
                                  '  RETURNING id_factura INTO v_id;\n'
                                  '  INSERT INTO detalle_factura (id_factura, id_insumo, cantidad, '
                                  'precio_unit)\n'
                                  '  VALUES (v_id, p_id_insumo, p_cantidad, v_precio);\n'
                                  "  RETURN QUERY SELECT TRUE, 'Factura generada', v_id;\n"
                                  'EXCEPTION WHEN OTHERS THEN\n'
                                  '  RETURN QUERY SELECT FALSE, SQLERRM, NULL::INT;\n'
                                  'END;\n'
                                  '$fn$;\n',
                     'tipo': 'bd_sql'},
                    {'enunciado': '## 5. Contrato de integracion app <-> BD (documento del '
                                  'entregable)\n'
                                  '\n'
                                  'Redacta el **contrato de integracion** de VetCare DB, el '
                                  'documento que le entregarias a un equipo de desarrollo que '
                                  'nunca ha visto tu base. Una seccion por operacion, para las '
                                  '**tres** (`api_agendar_cita`, `api_registrar_consulta`, '
                                  '`api_facturar`), y cada seccion con:\n'
                                  '\n'
                                  '1. **Proposito** en una frase de negocio.\n'
                                  '2. **Firma exacta**: nombre, parametros en orden con tipo '
                                  'PostgreSQL, y forma de invocacion (`SELECT * FROM '
                                  'api_...(...)`).\n'
                                  '3. **Contrato de retorno**: las tres columnas `ok`, `mensaje`, '
                                  '`id_generado`, con el significado de cada una y que valor trae '
                                  '`id_generado` cuando `ok` es falso.\n'
                                  '4. **Precondiciones** que debe cumplir el llamador.\n'
                                  '5. **Efectos en la base** si `ok` es verdadero: exactamente que '
                                  'filas se insertan o actualizan, en que tablas.\n'
                                  '6. **Tabla de casos de rechazo**: cada `mensaje` posible, la '
                                  'causa y la **accion de la interfaz** (mostrar aviso, sugerir '
                                  'otra franja, deshabilitar el boton de cobrar, reintentar).\n'
                                  '7. **Idempotencia y reintentos**: que pasa si la aplicacion, '
                                  'por un timeout de red, vuelve a llamar la misma operacion. Di '
                                  'honestamente si tu API es segura ante reintentos y, si no lo '
                                  'es, que le agregarias (por ejemplo una clave de idempotencia o '
                                  'una restriccion unica que absorba el duplicado).\n'
                                  '\n'
                                  'Cierra con dos reglas del contrato, escritas para que un '
                                  'desarrollador las cumpla sin discutir:\n'
                                  '\n'
                                  '- **Regla de acceso**: la aplicacion solo tiene `EXECUTE` de '
                                  'las funciones `api_*` y `SELECT` de lectura; no tiene '
                                  '`INSERT`/`UPDATE`/`DELETE` sobre las tablas de negocio.\n'
                                  '- **Regla de parametros**: todo valor que venga del usuario '
                                  'viaja como **parametro ligado**; nunca concatenado en la cadena '
                                  'SQL.',
                     'puntos': 18,
                     'rubrica': 'Las 3 operaciones estan documentadas con los 7 puntos. Las firmas '
                                'coinciden exactamente con las funciones implementadas en la '
                                'pregunta 1. La tabla de rechazos cubre todos los mensajes que '
                                'devuelve el codigo, cada uno con su accion de interfaz. La '
                                'seccion de idempotencia da un veredicto honesto y una propuesta '
                                'concreta si la API no es segura ante reintentos. Las dos reglas '
                                'de cierre aparecen redactadas de forma imperativa.',
                     'tipo': 'abierta'},
                    {'enunciado': '## 6. Guion de la sustentacion (5 a 8 minutos)\n'
                                  '\n'
                                  'Prepara el **outline de la sustentacion final** de VetCare DB. '
                                  'Entrega:\n'
                                  '\n'
                                  '1. **Storyboard de 6 diapositivas**, una fila por diapositiva:\n'
                                  '\n'
                                  '| # | Titulo de la diapositiva | Que se muestra en pantalla | '
                                  'Quien habla | Minutos |\n'
                                  '|---|---|---|---|---|\n'
                                  '\n'
                                  'Cubre obligatoriamente: (1) problema y alcance de Huellitas, '
                                  '(2) modelo ER, (3) reglas de negocio y como las hace cumplir la '
                                  'base, (4) demo en vivo de una operacion `api_*` con su caso de '
                                  'rechazo, (5) rendimiento (antes/despues e indices con evidencia '
                                  'de `EXPLAIN`), (6) seguridad, respaldo y cierre con lecciones '
                                  'aprendidas. La suma de minutos debe quedar entre **5 y 8**.\n'
                                  '\n'
                                  '2. **Guion de la demo en vivo**, paso a paso: las **sentencias '
                                  'exactas** que vas a ejecutar y en que orden, incluyendo **un '
                                  'caso que falla a proposito** (agendar la mascota inactiva o '
                                  'facturar sin stock). Indica el resultado que espera el publico '
                                  'ver en cada paso.\n'
                                  '\n'
                                  '3. **Plan B de la demo**: que haces si la base no carga o una '
                                  'sentencia falla en vivo (capturas de pantalla preparadas, '
                                  'script alterno, video corto).\n'
                                  '\n'
                                  '4. **Tres preguntas dificiles** que crees que hara el jurado, '
                                  'con tu respuesta en 2 o 3 lineas cada una. Al menos una debe '
                                  'ser sobre concurrencia o sobre respaldo.\n'
                                  '\n'
                                  '5. **Checklist de empaquetado** del entregable: que archivos '
                                  'van en el ZIP, en que orden se ejecutan los scripts y como se '
                                  'llama cada uno.',
                     'puntos': 12,
                     'rubrica': 'El storyboard tiene 6 filas con contenido, responsable nombrado y '
                                'minutos que suman entre 5 y 8. El guion de la demo lista '
                                'sentencias concretas en orden e incluye al menos un caso de fallo '
                                'intencional con el resultado esperado. Hay plan B especifico y 3 '
                                'preguntas del jurado con respuesta, al menos una de concurrencia '
                                'o respaldo. El checklist de empaquetado nombra archivos y su '
                                'orden de ejecucion.',
                     'tipo': 'abierta'}],
      'resumen': 'El estudiante publica la capa de API de VetCare (tres funciones con contrato de '
                 'retorno uniforme), la consume desde codigo con parametros ligados, la blinda con '
                 'privilegios de EXECUTE y prepara el guion de la sustentacion.',
      'titulo': 'Taller Clase 12 en ExamLab - Contrato de integracion app <-> BD y preparacion de '
                'la sustentacion'},
 13: {'preguntas': [{'enunciado': '## 1. El caso: que paso, por que y que aprendemos\n'
                                  '\n'
                                  '**Clase autonoma: no hay docente en vivo. Todo lo que necesitas '
                                  'para responder esta en este enunciado.**\n'
                                  '\n'
                                  'Elige **uno** de estos tres casos reales de fallos de bases de '
                                  'datos (o propon otro documentado, citando la fuente):\n'
                                  '\n'
                                  '- **A. Perdida de datos por respaldo no verificado.** GitLab, '
                                  'enero de 2017: durante un incidente de carga, un ingeniero '
                                  'ejecuto un borrado sobre el directorio de datos del servidor '
                                  'equivocado. De cinco mecanismos de respaldo, **ninguno** '
                                  'funciono como se esperaba; se recuperaron datos de una copia de '
                                  'seguridad de casi seis horas antes y se perdio informacion de '
                                  'forma definitiva.\n'
                                  '- **B. Rendimiento que tumba el servicio.** Una consulta de '
                                  'reporte sin indice y con `SELECT *` sobre una tabla de decenas '
                                  'de millones de filas, ejecutada cada minuto por un panel de '
                                  'control, agota la memoria y las conexiones del servidor y deja '
                                  'fuera de servicio a toda la aplicacion en hora pico.\n'
                                  '- **C. Seguridad: inyeccion de SQL.** Una aplicacion construye '
                                  'sus consultas concatenando lo que el usuario escribe en un '
                                  'formulario de busqueda. Un atacante envia una cadena con '
                                  "comillas y `OR '1'='1'` y obtiene el listado completo de la "
                                  'base, incluidos datos personales de los clientes.\n'
                                  '\n'
                                  'Redacta **media pagina** con esta estructura:\n'
                                  '\n'
                                  '1. **Contexto**: que organizacion o tipo de sistema, que hacia '
                                  'y que estaba en juego.\n'
                                  '2. **Que fallo**: la secuencia de hechos, en orden. Se lo mas '
                                  'concreto que puedas.\n'
                                  '3. **Causa raiz**, distinguiendola de la causa aparente. La '
                                  'causa aparente suele ser "alguien se equivoco"; la raiz suele '
                                  'ser "no habia un control que detuviera ese error".\n'
                                  '4. **Impacto**: datos, dinero, tiempo, confianza.\n'
                                  '5. **Leccion en una frase**, redactada como regla accionable '
                                  '("un respaldo que no se ha restaurado no es un respaldo").\n'
                                  '6. **Traduccion a VetCare**: cual de las tablas o procesos de '
                                  'tu proyecto (`cita`, `insumo`, `factura`, `audit_cita`, tu capa '
                                  '`api_*`) es vulnerable al **mismo** tipo de fallo, y por que.\n'
                                  '\n'
                                  'Si eliges un caso propio, incluye la fuente (enlace o '
                                  'publicacion) al final.',
                     'puntos': 25,
                     'rubrica': 'Las 6 secciones estan presentes. La causa raiz se distingue '
                                'explicitamente de la causa aparente y apunta a un control '
                                'ausente, no a la culpa de una persona. El impacto es concreto. La '
                                'leccion esta redactada como regla accionable. La traduccion a '
                                'VetCare nombra tablas o procesos reales del proyecto y explica el '
                                'mecanismo de la vulnerabilidad, no una analogia vaga. Si el caso '
                                'es propio, trae fuente.',
                     'tipo': 'abierta'},
                    {'enunciado': '## 2. Mejora implementada 1: cerrar la inyeccion de SQL en '
                                  'VetCare\n'
                                  '\n'
                                  'El esquema `dueno`, `mascota`, `veterinario`, `cita` esta '
                                  'creado y poblado (8 mascotas; **Rocky** y **Kiara** inactivas). '
                                  'La base trae, a proposito, una funcion **vulnerable** que el '
                                  'desarrollador de turno escribio en su momento para el buscador '
                                  'de mascotas:\n'
                                  '\n'
                                  '```sql\n'
                                  'CREATE FUNCTION buscar_mascota_insegura(p_nombre TEXT)\n'
                                  'RETURNS TABLE (id_mascota INT, nombre TEXT, especie TEXT, '
                                  'activa CHAR(1))\n'
                                  'LANGUAGE plpgsql AS $fn$\n'
                                  'BEGIN\n'
                                  '  RETURN QUERY EXECUTE\n'
                                  "    'SELECT id_mascota, nombre, especie, activa FROM mascota "
                                  "WHERE nombre = ''' || p_nombre || '''';\n"
                                  'END;\n'
                                  '$fn$;\n'
                                  '```\n'
                                  '\n'
                                  'Escribe el SQL que:\n'
                                  '\n'
                                  '1. **Demuestre el uso normal**: `SELECT * FROM '
                                  "buscar_mascota_insegura('Firulais');` -> debe devolver 1 fila.\n"
                                  '2. **Demuestre el ataque**: `SELECT * FROM '
                                  "buscar_mascota_insegura('Firulais'' OR ''1''=''1');`\n"
                                  '   (en SQL, para escribir una comilla simple dentro de una '
                                  'cadena se duplica). Debe devolver **las 8 mascotas**: la '
                                  'concatenacion dejo que el usuario reescribiera el `WHERE`.\n'
                                  '3. **Cuantifique la fuga**: `SELECT COUNT(*) FROM '
                                  "buscar_mascota_insegura('x'' OR ''1''=''1');` y compara con "
                                  '`SELECT COUNT(*) FROM mascota;`. Deben coincidir: eso es la '
                                  'evidencia del incidente.\n'
                                  '4. **Implemente la version segura** '
                                  '`buscar_mascota_segura(p_nombre TEXT)` con la misma firma de '
                                  'retorno, usando **parametros ligados** en el SQL dinamico:\n'
                                  '   ```sql\n'
                                  '   RETURN QUERY EXECUTE\n'
                                  "     'SELECT id_mascota, nombre, especie, activa FROM mascota "
                                  "WHERE nombre = $1'\n"
                                  '     USING p_nombre;\n'
                                  '   ```\n'
                                  '   (Mejor aun: como aqui no hace falta SQL dinamico, escribe '
                                  '**tambien** una variante `buscar_mascota_directa(p_nombre '
                                  'TEXT)` que use una consulta estatica `SELECT ... WHERE nombre = '
                                  'p_nombre`, sin `EXECUTE`.)\n'
                                  '5. **Pruebe que el agujero quedo cerrado**: repite el ataque '
                                  'contra la version segura,\n'
                                  "   `SELECT * FROM buscar_mascota_segura('Firulais'' OR "
                                  "''1''=''1');` -> debe devolver **0 filas**, porque ahora esa "
                                  'cadena completa se compara como un **valor**, no como codigo.\n'
                                  '6. **Elimine la funcion vulnerable** con `DROP FUNCTION '
                                  'buscar_mascota_insegura(TEXT);` y deje un comentario `--` con '
                                  'la regla que adoptas sobre SQL dinamico y parametros '
                                  'ligados.',
                     'puntos': 25,
                     'rubrica': 'Se demuestra el uso normal y el ataque, evidenciando con COUNT '
                                'que la funcion insegura devuelve todas las mascotas. Se crea la '
                                'version segura con EXECUTE ... USING (y opcionalmente la variante '
                                'estatica) manteniendo la firma de retorno. El mismo ataque contra '
                                'la version segura devuelve 0 filas. Se hace DROP de la funcion '
                                'vulnerable y se enuncia la regla propia. Se descuenta si no '
                                'se muestra el contraste cuantitativo antes/despues.',
                     'setup_sql': 'CREATE TABLE dueno (\n'
                                  '  id_dueno SERIAL PRIMARY KEY,\n'
                                  '  nombre TEXT NOT NULL,\n'
                                  '  telefono TEXT,\n'
                                  '  email TEXT,\n'
                                  "  ciudad TEXT DEFAULT 'Cali'\n"
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE mascota (\n'
                                  '  id_mascota SERIAL PRIMARY KEY,\n'
                                  '  id_dueno INT NOT NULL REFERENCES dueno(id_dueno),\n'
                                  '  nombre TEXT NOT NULL,\n'
                                  '  especie TEXT NOT NULL,\n'
                                  '  fecha_nac DATE,\n'
                                  "  activa CHAR(1) NOT NULL DEFAULT 'S' CHECK (activa IN "
                                  "('S','N'))\n"
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE veterinario (\n'
                                  '  id_veterinario SERIAL PRIMARY KEY,\n'
                                  '  nombre TEXT NOT NULL,\n'
                                  '  especialidad TEXT,\n'
                                  "  activo CHAR(1) NOT NULL DEFAULT 'S' CHECK (activo IN "
                                  "('S','N'))\n"
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE cita (\n'
                                  '  id_cita SERIAL PRIMARY KEY,\n'
                                  '  id_mascota INT NOT NULL REFERENCES mascota(id_mascota),\n'
                                  '  id_veterinario INT NOT NULL REFERENCES '
                                  'veterinario(id_veterinario),\n'
                                  '  fecha_hora TIMESTAMP NOT NULL,\n'
                                  "  estado TEXT NOT NULL DEFAULT 'PROGRAMADA'\n"
                                  "    CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))\n"
                                  ');\n'
                                  '\n'
                                  '-- Duenos (ids 1..6 en este orden)\n'
                                  'INSERT INTO dueno (nombre, telefono, email) VALUES\n'
                                  "  ('Ana Gomez',      '3001112233', 'ana.gomez@mail.com'),\n"
                                  "  ('Carlos Ruiz',    '3014445566', 'carlos.ruiz@mail.com'),\n"
                                  "  ('Marcela Diaz',   '3027778899', 'marcela.diaz@mail.com'),\n"
                                  "  ('Jorge Pineda',   '3105551212', 'jorge.pineda@mail.com'),\n"
                                  "  ('Luisa Cardona',  '3123334455', 'luisa.cardona@mail.com'),\n"
                                  "  ('Andres Vallejo', '3159998877', 'andres.vallejo@mail.com');\n"
                                  '\n'
                                  '-- Veterinarios (ids 1..4)\n'
                                  'INSERT INTO veterinario (nombre, especialidad) VALUES\n'
                                  "  ('Laura Restrepo', 'General'),\n"
                                  "  ('Diego Moreno',   'Cirugia'),\n"
                                  "  ('Paula Salazar',  'Dermatologia'),\n"
                                  "  ('Ivan Ortiz',     'General');\n"
                                  '\n'
                                  '-- Mascotas (ids 1..8). Rocky (3) y Kiara (8) estan INACTIVAS.\n'
                                  'INSERT INTO mascota (id_dueno, nombre, especie, fecha_nac, '
                                  'activa) VALUES\n'
                                  "  (1, 'Firulais', 'Canino', DATE '2019-04-12', 'S'),\n"
                                  "  (1, 'Luna',     'Felino', DATE '2021-08-30', 'S'),\n"
                                  "  (2, 'Rocky',    'Canino', DATE '2015-01-20', 'N'),\n"
                                  "  (3, 'Mishi',    'Felino', DATE '2022-11-05', 'S'),\n"
                                  "  (3, 'Bobby',    'Canino', DATE '2018-06-17', 'S'),\n"
                                  "  (4, 'Nube',     'Felino', DATE '2023-02-09', 'S'),\n"
                                  "  (5, 'Toby',     'Canino', DATE '2020-09-25', 'S'),\n"
                                  "  (6, 'Kiara',    'Canino', DATE '2013-03-03', 'N');\n"
                                  '\n'
                                  '-- Citas (ids 1..10)\n'
                                  'INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                  'estado) VALUES\n'
                                  "  (1, 1, TIMESTAMP '2026-09-01 08:00:00', 'PROGRAMADA'),\n"
                                  "  (2, 1, TIMESTAMP '2026-09-01 09:00:00', 'ATENDIDA'),\n"
                                  "  (4, 2, TIMESTAMP '2026-09-01 10:00:00', 'PROGRAMADA'),\n"
                                  "  (5, 3, TIMESTAMP '2026-09-02 08:30:00', 'CANCELADA'),\n"
                                  "  (6, 2, TIMESTAMP '2026-09-02 11:00:00', 'ATENDIDA'),\n"
                                  "  (7, 4, TIMESTAMP '2026-09-03 07:45:00', 'PROGRAMADA'),\n"
                                  "  (1, 1, TIMESTAMP '2026-09-05 15:00:00', 'ATENDIDA'),\n"
                                  "  (2, 3, TIMESTAMP '2026-09-08 16:00:00', 'PROGRAMADA'),\n"
                                  "  (4, 4, TIMESTAMP '2026-09-10 08:00:00', 'PROGRAMADA'),\n"
                                  "  (6, 1, TIMESTAMP '2026-09-10 09:00:00', 'ATENDIDA');\n"
                                  '\n'
                                  '-- Funcion VULNERABLE a proposito: concatena la entrada del '
                                  'usuario en SQL dinamico.\n'
                                  'CREATE FUNCTION buscar_mascota_insegura(p_nombre TEXT)\n'
                                  'RETURNS TABLE (id_mascota INT, nombre TEXT, especie TEXT, '
                                  'activa CHAR(1))\n'
                                  'LANGUAGE plpgsql\n'
                                  'AS $fn$\n'
                                  'BEGIN\n'
                                  '  RETURN QUERY EXECUTE\n'
                                  "    'SELECT id_mascota, nombre, especie, activa FROM mascota "
                                  "WHERE nombre = ''' || p_nombre || '''';\n"
                                  'END;\n'
                                  '$fn$;\n',
                     'tipo': 'bd_sql'},
                    {'enunciado': '## 3. Mejora implementada 2: ningun borrado sin traza ni sin '
                                  'vuelta atras\n'
                                  '\n'
                                  'El esquema `dueno`, `mascota`, `veterinario`, `cita` esta '
                                  'creado y poblado con **10 citas**. Esta base **no** tiene las '
                                  'tablas `consulta` ni `factura`, para que el `DELETE` del '
                                  'incidente pueda ejecutarse sin tropezar con llaves foraneas.\n'
                                  '\n'
                                  'Vas a implementar el control que le falto al caso del respaldo '
                                  'no verificado. Escribe el SQL que:\n'
                                  '\n'
                                  '1. **Respaldo logico previo y su bitacora.** Crea '
                                  '`respaldo_cita` como copia exacta de `cita` (`CREATE TABLE '
                                  'respaldo_cita AS SELECT * FROM cita;`) y una tabla '
                                  '`bitacora_respaldo (id_bitacora SERIAL, tabla TEXT, '
                                  'filas_respaldadas INT, hecho_en TIMESTAMP DEFAULT now())`. '
                                  'Inserta en la bitacora el conteo real de filas respaldadas '
                                  '(obtenlo con una subconsulta `SELECT COUNT(*) FROM '
                                  'respaldo_cita`, no lo escribas a mano).\n'
                                  '2. **Archivo de borrados + trigger.** Crea `cita_borrada` con '
                                  'las mismas columnas que `cita` mas `borrado_en TIMESTAMP '
                                  'DEFAULT now()` y `usuario_bd TEXT DEFAULT current_user`. Crea '
                                  'la funcion `fn_trg_archivar_cita()` que `RETURNS TRIGGER`, '
                                  'inserte en `cita_borrada` los valores de `OLD` (columna por '
                                  'columna) y haga `RETURN OLD` para permitir el borrado. Asocia '
                                  'el trigger `trg_archivar_cita` **BEFORE DELETE ON cita FOR EACH '
                                  'ROW**.\n'
                                  '3. **Reproduce el incidente.** Ejecuta `DELETE FROM cita;` (el '
                                  'borrado accidental sin `WHERE`). Muestra con dos consultas que '
                                  '`cita` quedo en **0 filas** y que `cita_borrada` tiene las '
                                  '**10**.\n'
                                  '4. **Restaura.** Repuebla `cita` desde `cita_borrada` (o desde '
                                  '`respaldo_cita`) con un `INSERT INTO cita (...) SELECT ...` de '
                                  'columnas explicitas.\n'
                                  '5. **Verifica la restauracion como se debe.** Escribe **una** '
                                  'consulta de validacion post-restauracion que devuelva, en una '
                                  'sola fila: filas esperadas (de `bitacora_respaldo`), filas '
                                  'actuales en `cita`, `MIN(fecha_hora)`, `MAX(fecha_hora)` y una '
                                  "columna `veredicto` con `'RESTAURACION OK'` o `'REVISAR'` segun "
                                  'coincidan o no los conteos (usa `CASE`). Esta consulta es la '
                                  'que faltaba en el caso real: **un respaldo que no se ha '
                                  'restaurado y verificado no es un respaldo**.\n'
                                  '6. Cierra con un comentario `--` de dos o tres lineas '
                                  'explicando por que el trigger de archivo y la consulta de '
                                  'verificacion son controles **distintos** y por que hacen falta '
                                  'los dos.',
                     'puntos': 25,
                     'rubrica': 'Se crean respaldo_cita, bitacora_respaldo (con el conteo '
                                'calculado, no literal), cita_borrada y el trigger BEFORE DELETE '
                                'que archiva OLD y retorna OLD. El DELETE sin WHERE deja cita en 0 '
                                'y cita_borrada en 10. La restauracion repone las 10 filas con '
                                'columnas explicitas. La consulta de validacion devuelve una sola '
                                'fila con esperadas, actuales, min, max y el veredicto calculado '
                                'con CASE. El comentario final distingue correctamente los dos '
                                'controles.',
                     'setup_sql': 'CREATE TABLE dueno (\n'
                                  '  id_dueno SERIAL PRIMARY KEY,\n'
                                  '  nombre TEXT NOT NULL,\n'
                                  '  telefono TEXT,\n'
                                  '  email TEXT,\n'
                                  "  ciudad TEXT DEFAULT 'Cali'\n"
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE mascota (\n'
                                  '  id_mascota SERIAL PRIMARY KEY,\n'
                                  '  id_dueno INT NOT NULL REFERENCES dueno(id_dueno),\n'
                                  '  nombre TEXT NOT NULL,\n'
                                  '  especie TEXT NOT NULL,\n'
                                  '  fecha_nac DATE,\n'
                                  "  activa CHAR(1) NOT NULL DEFAULT 'S' CHECK (activa IN "
                                  "('S','N'))\n"
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE veterinario (\n'
                                  '  id_veterinario SERIAL PRIMARY KEY,\n'
                                  '  nombre TEXT NOT NULL,\n'
                                  '  especialidad TEXT,\n'
                                  "  activo CHAR(1) NOT NULL DEFAULT 'S' CHECK (activo IN "
                                  "('S','N'))\n"
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE cita (\n'
                                  '  id_cita SERIAL PRIMARY KEY,\n'
                                  '  id_mascota INT NOT NULL REFERENCES mascota(id_mascota),\n'
                                  '  id_veterinario INT NOT NULL REFERENCES '
                                  'veterinario(id_veterinario),\n'
                                  '  fecha_hora TIMESTAMP NOT NULL,\n'
                                  "  estado TEXT NOT NULL DEFAULT 'PROGRAMADA'\n"
                                  "    CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))\n"
                                  ');\n'
                                  '\n'
                                  '-- Duenos (ids 1..6 en este orden)\n'
                                  'INSERT INTO dueno (nombre, telefono, email) VALUES\n'
                                  "  ('Ana Gomez',      '3001112233', 'ana.gomez@mail.com'),\n"
                                  "  ('Carlos Ruiz',    '3014445566', 'carlos.ruiz@mail.com'),\n"
                                  "  ('Marcela Diaz',   '3027778899', 'marcela.diaz@mail.com'),\n"
                                  "  ('Jorge Pineda',   '3105551212', 'jorge.pineda@mail.com'),\n"
                                  "  ('Luisa Cardona',  '3123334455', 'luisa.cardona@mail.com'),\n"
                                  "  ('Andres Vallejo', '3159998877', 'andres.vallejo@mail.com');\n"
                                  '\n'
                                  '-- Veterinarios (ids 1..4)\n'
                                  'INSERT INTO veterinario (nombre, especialidad) VALUES\n'
                                  "  ('Laura Restrepo', 'General'),\n"
                                  "  ('Diego Moreno',   'Cirugia'),\n"
                                  "  ('Paula Salazar',  'Dermatologia'),\n"
                                  "  ('Ivan Ortiz',     'General');\n"
                                  '\n'
                                  '-- Mascotas (ids 1..8). Rocky (3) y Kiara (8) estan INACTIVAS.\n'
                                  'INSERT INTO mascota (id_dueno, nombre, especie, fecha_nac, '
                                  'activa) VALUES\n'
                                  "  (1, 'Firulais', 'Canino', DATE '2019-04-12', 'S'),\n"
                                  "  (1, 'Luna',     'Felino', DATE '2021-08-30', 'S'),\n"
                                  "  (2, 'Rocky',    'Canino', DATE '2015-01-20', 'N'),\n"
                                  "  (3, 'Mishi',    'Felino', DATE '2022-11-05', 'S'),\n"
                                  "  (3, 'Bobby',    'Canino', DATE '2018-06-17', 'S'),\n"
                                  "  (4, 'Nube',     'Felino', DATE '2023-02-09', 'S'),\n"
                                  "  (5, 'Toby',     'Canino', DATE '2020-09-25', 'S'),\n"
                                  "  (6, 'Kiara',    'Canino', DATE '2013-03-03', 'N');\n"
                                  '\n'
                                  '-- Citas (ids 1..10)\n'
                                  'INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                  'estado) VALUES\n'
                                  "  (1, 1, TIMESTAMP '2026-09-01 08:00:00', 'PROGRAMADA'),\n"
                                  "  (2, 1, TIMESTAMP '2026-09-01 09:00:00', 'ATENDIDA'),\n"
                                  "  (4, 2, TIMESTAMP '2026-09-01 10:00:00', 'PROGRAMADA'),\n"
                                  "  (5, 3, TIMESTAMP '2026-09-02 08:30:00', 'CANCELADA'),\n"
                                  "  (6, 2, TIMESTAMP '2026-09-02 11:00:00', 'ATENDIDA'),\n"
                                  "  (7, 4, TIMESTAMP '2026-09-03 07:45:00', 'PROGRAMADA'),\n"
                                  "  (1, 1, TIMESTAMP '2026-09-05 15:00:00', 'ATENDIDA'),\n"
                                  "  (2, 3, TIMESTAMP '2026-09-08 16:00:00', 'PROGRAMADA'),\n"
                                  "  (4, 4, TIMESTAMP '2026-09-10 08:00:00', 'PROGRAMADA'),\n"
                                  "  (6, 1, TIMESTAMP '2026-09-10 09:00:00', 'ATENDIDA');\n",
                     'tipo': 'bd_sql'},
                    {'correctas': [0, 2, 4, 5],
                     'enunciado': '## 4. Que control habria evitado el incidente\n'
                                  '\n'
                                  'Selecciona **todas** las afirmaciones correctas sobre los '
                                  'controles que previenen los fallos analizados.',
                     'opciones': ['Un respaldo solo cuenta como valido cuando se ha restaurado en '
                                  'un entorno de prueba y una consulta de verificacion confirmo '
                                  'conteos y rangos de datos esperados.',
                                  'Escapar manualmente las comillas de la entrada del usuario '
                                  'antes de concatenarla es equivalente a usar parametros ligados.',
                                  'Usar parametros ligados (EXECUTE ... USING, o %s desde la '
                                  'aplicacion) elimina la inyeccion porque la entrada viaja como '
                                  'valor y nunca se interpreta como codigo SQL.',
                                  'Tener cinco mecanismos de respaldo garantiza la recuperacion, '
                                  'aunque ninguno se haya probado.',
                                  'Un trigger que archiva las filas antes de borrarlas convierte '
                                  'un borrado accidental en un incidente recuperable, aunque no '
                                  'evita el error humano.',
                                  'Un indice adecuado mas la eliminacion de SELECT * en un reporte '
                                  'que corre cada minuto pueden ser la diferencia entre un panel '
                                  'util y una caida del servicio en hora pico.'],
                     'puntos': 10,
                     'rubrica': '10 puntos con las 4 opciones correctas y ninguna incorrecta; '
                                'puntaje proporcional por acierto parcial. Correctas: indices 0, '
                                '2, 4 y 5.',
                     'tipo': 'cerrada_multi'},
                    {'enunciado': '## 5. Tres mejoras priorizadas para VetCare\n'
                                  '\n'
                                  'Cierra el informe con el plan de mejoras que adoptas a '
                                  'partir del caso. Entrega una tabla de **exactamente tres** '
                                  'filas:\n'
                                  '\n'
                                  '| # | Mejora concreta | Objeto de VetCare que cambia | Riesgo '
                                  'que mitiga | Esfuerzo (bajo/medio/alto) | Impacto '
                                  '(bajo/medio/alto) | Como se verifica | Estado |\n'
                                  '|---|---|---|---|---|---|---|---|\n'
                                  '\n'
                                  'Reglas:\n'
                                  '\n'
                                  '- **Dos** de las tres mejoras deben ser las que **ya '
                                  'implementaste** en las preguntas 2 y 3; su estado es '
                                  '`IMPLEMENTADA` y en la columna de verificacion debes citar la '
                                  'prueba concreta que corriste (por ejemplo: "el ataque contra '
                                  '`buscar_mascota_segura` devuelve 0 filas").\n'
                                  '- La tercera es una mejora **pendiente**, derivada del caso, '
                                  'con estado `PENDIENTE`, responsable y fecha.\n'
                                  '- Cada mejora debe nombrar un objeto real de tu base (tabla, '
                                  'funcion, trigger, indice, rol), no una intencion general.\n'
                                  '\n'
                                  'Debajo de la tabla, responde en 4 a 6 lineas:\n'
                                  '\n'
                                  '1. **Priorizacion**: cual de las tres harias primero si solo '
                                  'tuvieras un dia y por que, usando la relacion '
                                  'esfuerzo/impacto.\n'
                                  '2. **Que dice esto de tu diseno**: que supuesto de tu PI quedo '
                                  'en evidencia con el caso analizado.\n'
                                  '3. **Actualizacion del informe del PI**: en que seccion del '
                                  'informe final entra este analisis y que frase agregas a las '
                                  'lecciones aprendidas.',
                     'puntos': 15,
                     'rubrica': 'La tabla tiene exactamente 3 filas con las 8 columnas; dos '
                                'mejoras estan marcadas IMPLEMENTADA y citan la prueba real '
                                'ejecutada en las preguntas 2 y 3, y la tercera es PENDIENTE con '
                                'responsable y fecha. Cada fila nombra un objeto real de la base. '
                                'La priorizacion argumenta con esfuerzo/impacto y se identifica el '
                                'supuesto de diseno que el caso puso en evidencia.',
                     'tipo': 'abierta'}],
      'resumen': 'El estudiante analiza un incidente real de bases de datos y lo convierte en dos '
                 'mejoras implementadas y probadas sobre VetCare (blindaje de SQL dinamico y '
                 'auditoria de borrados con restauracion), mas un plan de mejoras priorizado.',
      'titulo': 'Taller Clase 13 en ExamLab - Analisis de casos reales aplicado a VetCare (clase '
                'autonoma)'},
 15: {'preguntas': [{'enunciado': '## 1. Script maestro de entrega: VetCare DB de cero, en una '
                                  'sola corrida\n'
                                  '\n'
                                  '**Evaluacion final del PI (20 % del Corte 3). Debe quedar '
                                  'entregado ANTES de tu turno de sustentacion en vivo. Lee el '
                                  'enunciado completo antes de escribir.**\n'
                                  '\n'
                                  'Esta base esta **vacia**: solo existe la tabla `entrega_final` '
                                  'donde registras tu paquete. Debes entregar aqui el '
                                  '**script maestro** de VetCare DB, el mismo que va en el ZIP: se '
                                  'ejecuta **una sola vez, de arriba abajo, sobre una base '
                                  'limpia**, y debe correr **sin un solo error**.\n'
                                  '\n'
                                  'Ese script debe contener, en este orden:\n'
                                  '\n'
                                  '**Bloque 0 - Registro.** Un `INSERT INTO entrega_final '
                                  '(estudiante, codigo, proyecto, enlace_zip)` con tus datos '
                                  'reales. Si el docente autorizo equipo, llena tambien la columna '
                                  'opcional `integrantes`; si trabajas solo, dejala nula.\n'
                                  '\n'
                                  '**Bloque 1 - DDL completo.** Las **8 tablas** del PI: `dueno`, '
                                  '`mascota`, `veterinario`, `cita`, `consulta`, `insumo`, '
                                  '`factura`, `detalle_factura`, con PK, todas las FK y las '
                                  'restricciones de dominio (`CHECK` de `mascota.activa`, `CHECK` '
                                  'de `cita.estado`, `CHECK (stock >= 0)`, `CHECK (cantidad > 0)`, '
                                  '`CHECK (precio >= 0)`). Incluye tambien la tabla de auditoria '
                                  '`audit_cita`.\n'
                                  '\n'
                                  '**Bloque 2 - Datos semilla.** Minimo **5 duenos, 3 '
                                  'veterinarios, 8 mascotas (al menos 2 inactivas), 8 citas en '
                                  'distintos estados, 4 insumos (al menos uno con stock menor a 5) '
                                  'y 2 facturas con sus detalles**. Nombres en espanol, coherentes '
                                  'con una veterinaria de Cali.\n'
                                  '\n'
                                  '**Bloque 3 - Logica de negocio.** Como minimo:\n'
                                  '- una funcion (por ejemplo `fn_precio_consulta`),\n'
                                  '- un procedimiento de negocio con validacion (por ejemplo '
                                  '`sp_agendar_cita`, que rechace mascota inactiva),\n'
                                  '- un trigger de auditoria de cambio de estado de cita sobre '
                                  '`audit_cita`.\n'
                                  '\n'
                                  '**Bloque 4 - Indices.** Al menos **dos** indices con nombre '
                                  'claro sobre las columnas de filtro de tus reportes.\n'
                                  '\n'
                                  '**Bloque 5 - Pruebas de aceptacion de las tres reglas del PI.** '
                                  'Tres bloques `DO` que capturen la excepcion (`EXCEPTION WHEN '
                                  "OTHERS THEN RAISE NOTICE '%', SQLERRM;`) y demuestren que:\n"
                                  '1. una mascota inactiva **no** puede agendar cita;\n'
                                  '2. el stock de un insumo **no** puede quedar negativo;\n'
                                  '3. un cambio de estado de cita **queda** auditado en '
                                  '`audit_cita`.\n'
                                  '\n'
                                  '**Bloque 6 - Consulta de cierre.** Una unica consulta que '
                                  'devuelva el inventario de la entrega: nombre de tabla y numero '
                                  'de filas para las 8 tablas mas `audit_cita`. Puedes construirla '
                                  "con `UNION ALL` de `SELECT 'cita', COUNT(*) FROM cita`, etc.\n"
                                  '\n'
                                  'Sintaxis **PostgreSQL** en todo el script. Nada de `NUMBER`, '
                                  '`VARCHAR2`, `RAISE_APPLICATION_ERROR`, `DUAL`, `SQL%ROWCOUNT` '
                                  'ni `/` de terminacion.',
                     'puntos': 35,
                     'rubrica': 'El script corre completo sin errores sobre la base limpia. Estan '
                                'los 7 bloques: registro, DDL de las 8 tablas mas audit_cita con '
                                'PK/FK/CHECK, datos semilla con los minimos exigidos, funcion + '
                                'procedimiento con validacion + trigger de auditoria, dos indices '
                                'nombrados, las 3 pruebas de aceptacion capturadas y la consulta '
                                'de inventario. Las tres reglas de negocio quedan efectivamente '
                                'demostradas. Cero sintaxis Oracle.',
                     'setup_sql': '-- Base limpia para la entrega final del PI.\n'
                                  'CREATE TABLE entrega_final (\n'
                                  '  id_entrega SERIAL PRIMARY KEY,\n'
                                  '  estudiante TEXT NOT NULL,\n'
                                  '  codigo TEXT NOT NULL,\n'
                                  '  proyecto TEXT NOT NULL,\n'
                                  '  integrantes TEXT,  -- opcional: solo si el docente autorizo '
                                  'equipo\n'
                                  '  enlace_zip TEXT,\n'
                                  '  fecha_entrega DATE NOT NULL DEFAULT CURRENT_DATE\n'
                                  ');\n'
                                  '\n'
                                  'INSERT INTO entrega_final (estudiante, codigo, proyecto, '
                                  'enlace_zip)\n'
                                  "VALUES ('Ejemplo del docente', '000000', 'VetCare-Demo', "
                                  "'https://ejemplo.uniajc/entrega-demo.zip');\n",
                     'tipo': 'bd_sql'},
                    {'enunciado': '## 2. Los KPIs que se proyectan en la sustentacion\n'
                                  '\n'
                                  'Esta base trae el **VetCare completo** poblado (8 tablas con '
                                  'datos: 6 duenos, 4 veterinarios, 8 mascotas, 10 citas, 4 '
                                  'consultas, 6 insumos, 3 facturas con 8 lineas de detalle).\n'
                                  '\n'
                                  'Escribe las **cuatro consultas** que vas a proyectar en la '
                                  'diapositiva de resultados. Cada una en una sola sentencia:\n'
                                  '\n'
                                  '**K1 - Carga por veterinario.** Nombre del veterinario, total '
                                  'de citas, cuantas atendidas, cuantas canceladas y el '
                                  '**porcentaje de cancelacion** redondeado a un decimal. Los '
                                  'veterinarios sin citas deben aparecer con ceros y **sin '
                                  'division por cero** (usa `NULLIF` o `CASE`). Ordena por total '
                                  'de citas descendente.\n'
                                  '\n'
                                  '**K2 - Ingresos por mes.** Para cada mes con facturacion: el '
                                  "mes (usa `date_trunc('month', f.fecha)`), numero de facturas y "
                                  'total facturado. Ordena cronologicamente.\n'
                                  '\n'
                                  '**K3 - Top insumos consumidos.** Nombre del insumo, unidades '
                                  'totales vendidas segun `detalle_factura`, valor total generado '
                                  '(`SUM(cantidad * precio_unit)`) y stock restante. Incluye los '
                                  'insumos que **nunca** se han vendido, con 0 (usa `LEFT JOIN` y '
                                  '`COALESCE`). Ordena por unidades vendidas descendente.\n'
                                  '\n'
                                  '**K4 - Ficha de un dueno (historia clinica resumida).** Para el '
                                  'dueno `Ana Gomez`: una fila por cita de cualquiera de sus '
                                  'mascotas, con nombre de la mascota, `fecha_hora`, `estado`, '
                                  'veterinario, diagnostico (puede venir vacio si la cita no '
                                  'genero consulta) y el total facturado de esa consulta (tambien '
                                  'puede venir vacio). Usa `LEFT JOIN` para no perder las citas '
                                  'sin consulta y filtra el dueno por nombre.\n'
                                  '\n'
                                  'Al final, escribe en comentarios `--` una linea por KPI '
                                  'diciendo **que decision de la clinica** habilita cada numero y '
                                  '**que numero concreto** te salio.',
                     'puntos': 20,
                     'rubrica': 'Las 4 consultas corren y devuelven resultados coherentes con los '
                                'datos entregados. K1 evita la division por cero y conserva '
                                'veterinarios sin citas. K2 agrupa por mes con date_trunc y ordena '
                                'cronologicamente. K3 incluye los insumos nunca vendidos con '
                                'ceros. K4 usa LEFT JOIN de modo que aparecen tambien las citas '
                                'sin consulta ni factura, filtrando por el dueno indicado. Los '
                                'comentarios reportan el numero real obtenido y la decision que '
                                'habilita.',
                     'setup_sql': 'CREATE TABLE dueno (\n'
                                  '  id_dueno SERIAL PRIMARY KEY,\n'
                                  '  nombre TEXT NOT NULL,\n'
                                  '  telefono TEXT,\n'
                                  '  email TEXT,\n'
                                  "  ciudad TEXT DEFAULT 'Cali'\n"
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE mascota (\n'
                                  '  id_mascota SERIAL PRIMARY KEY,\n'
                                  '  id_dueno INT NOT NULL REFERENCES dueno(id_dueno),\n'
                                  '  nombre TEXT NOT NULL,\n'
                                  '  especie TEXT NOT NULL,\n'
                                  '  fecha_nac DATE,\n'
                                  "  activa CHAR(1) NOT NULL DEFAULT 'S' CHECK (activa IN "
                                  "('S','N'))\n"
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE veterinario (\n'
                                  '  id_veterinario SERIAL PRIMARY KEY,\n'
                                  '  nombre TEXT NOT NULL,\n'
                                  '  especialidad TEXT,\n'
                                  "  activo CHAR(1) NOT NULL DEFAULT 'S' CHECK (activo IN "
                                  "('S','N'))\n"
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE cita (\n'
                                  '  id_cita SERIAL PRIMARY KEY,\n'
                                  '  id_mascota INT NOT NULL REFERENCES mascota(id_mascota),\n'
                                  '  id_veterinario INT NOT NULL REFERENCES '
                                  'veterinario(id_veterinario),\n'
                                  '  fecha_hora TIMESTAMP NOT NULL,\n'
                                  "  estado TEXT NOT NULL DEFAULT 'PROGRAMADA'\n"
                                  "    CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))\n"
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE consulta (\n'
                                  '  id_consulta SERIAL PRIMARY KEY,\n'
                                  '  id_cita INT NOT NULL UNIQUE REFERENCES cita(id_cita),\n'
                                  '  diagnostico TEXT,\n'
                                  '  precio NUMERIC(12,2) NOT NULL CHECK (precio >= 0)\n'
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE insumo (\n'
                                  '  id_insumo SERIAL PRIMARY KEY,\n'
                                  '  nombre TEXT NOT NULL,\n'
                                  '  stock INT NOT NULL CHECK (stock >= 0),\n'
                                  '  precio_unit NUMERIC(12,2) NOT NULL\n'
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE factura (\n'
                                  '  id_factura SERIAL PRIMARY KEY,\n'
                                  '  id_consulta INT NOT NULL REFERENCES consulta(id_consulta),\n'
                                  '  fecha TIMESTAMP NOT NULL DEFAULT now(),\n'
                                  '  total NUMERIC(12,2) NOT NULL DEFAULT 0\n'
                                  ');\n'
                                  '\n'
                                  'CREATE TABLE detalle_factura (\n'
                                  '  id_detalle SERIAL PRIMARY KEY,\n'
                                  '  id_factura INT NOT NULL REFERENCES factura(id_factura) ON '
                                  'DELETE CASCADE,\n'
                                  '  id_insumo INT NOT NULL REFERENCES insumo(id_insumo),\n'
                                  '  cantidad INT NOT NULL CHECK (cantidad > 0),\n'
                                  '  precio_unit NUMERIC(12,2) NOT NULL\n'
                                  ');\n'
                                  '\n'
                                  '-- Duenos (ids 1..6 en este orden)\n'
                                  'INSERT INTO dueno (nombre, telefono, email) VALUES\n'
                                  "  ('Ana Gomez',      '3001112233', 'ana.gomez@mail.com'),\n"
                                  "  ('Carlos Ruiz',    '3014445566', 'carlos.ruiz@mail.com'),\n"
                                  "  ('Marcela Diaz',   '3027778899', 'marcela.diaz@mail.com'),\n"
                                  "  ('Jorge Pineda',   '3105551212', 'jorge.pineda@mail.com'),\n"
                                  "  ('Luisa Cardona',  '3123334455', 'luisa.cardona@mail.com'),\n"
                                  "  ('Andres Vallejo', '3159998877', 'andres.vallejo@mail.com');\n"
                                  '\n'
                                  '-- Veterinarios (ids 1..4)\n'
                                  'INSERT INTO veterinario (nombre, especialidad) VALUES\n'
                                  "  ('Laura Restrepo', 'General'),\n"
                                  "  ('Diego Moreno',   'Cirugia'),\n"
                                  "  ('Paula Salazar',  'Dermatologia'),\n"
                                  "  ('Ivan Ortiz',     'General');\n"
                                  '\n'
                                  '-- Mascotas (ids 1..8). Rocky (3) y Kiara (8) estan INACTIVAS.\n'
                                  'INSERT INTO mascota (id_dueno, nombre, especie, fecha_nac, '
                                  'activa) VALUES\n'
                                  "  (1, 'Firulais', 'Canino', DATE '2019-04-12', 'S'),\n"
                                  "  (1, 'Luna',     'Felino', DATE '2021-08-30', 'S'),\n"
                                  "  (2, 'Rocky',    'Canino', DATE '2015-01-20', 'N'),\n"
                                  "  (3, 'Mishi',    'Felino', DATE '2022-11-05', 'S'),\n"
                                  "  (3, 'Bobby',    'Canino', DATE '2018-06-17', 'S'),\n"
                                  "  (4, 'Nube',     'Felino', DATE '2023-02-09', 'S'),\n"
                                  "  (5, 'Toby',     'Canino', DATE '2020-09-25', 'S'),\n"
                                  "  (6, 'Kiara',    'Canino', DATE '2013-03-03', 'N');\n"
                                  '\n'
                                  '-- Citas (ids 1..10)\n'
                                  'INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, '
                                  'estado) VALUES\n'
                                  "  (1, 1, TIMESTAMP '2026-09-01 08:00:00', 'PROGRAMADA'),\n"
                                  "  (2, 1, TIMESTAMP '2026-09-01 09:00:00', 'ATENDIDA'),\n"
                                  "  (4, 2, TIMESTAMP '2026-09-01 10:00:00', 'PROGRAMADA'),\n"
                                  "  (5, 3, TIMESTAMP '2026-09-02 08:30:00', 'CANCELADA'),\n"
                                  "  (6, 2, TIMESTAMP '2026-09-02 11:00:00', 'ATENDIDA'),\n"
                                  "  (7, 4, TIMESTAMP '2026-09-03 07:45:00', 'PROGRAMADA'),\n"
                                  "  (1, 1, TIMESTAMP '2026-09-05 15:00:00', 'ATENDIDA'),\n"
                                  "  (2, 3, TIMESTAMP '2026-09-08 16:00:00', 'PROGRAMADA'),\n"
                                  "  (4, 4, TIMESTAMP '2026-09-10 08:00:00', 'PROGRAMADA'),\n"
                                  "  (6, 1, TIMESTAMP '2026-09-10 09:00:00', 'ATENDIDA');\n"
                                  '\n'
                                  '-- Consultas (ids 1..4) sobre las citas ATENDIDAS 2, 5, 7 y 10\n'
                                  'INSERT INTO consulta (id_cita, diagnostico, precio) VALUES\n'
                                  "  (2,  'Vacunacion triple felina', 40000),\n"
                                  "  (5,  'Control de peso',          38000),\n"
                                  "  (7,  'Otitis externa',           55000),\n"
                                  "  (10, 'Desparasitacion',          35000);\n"
                                  '\n'
                                  '-- Insumos (ids 1..6). Ojo: 2 y 5 tienen stock bajo a '
                                  'proposito.\n'
                                  'INSERT INTO insumo (nombre, stock, precio_unit) VALUES\n'
                                  "  ('Vacuna antirrabica',       12, 22000),\n"
                                  "  ('Vacuna triple felina',      3, 31000),\n"
                                  "  ('Antiparasitario oral',     40,  9500),\n"
                                  "  ('Suero fisiologico 500ml',  25,  7000),\n"
                                  "  ('Gasa esteril',              8,  1200),\n"
                                  "  ('Jeringa 5ml',              60,   900);\n"
                                  '\n'
                                  '-- Facturas (ids 1..3) y sus detalles\n'
                                  'INSERT INTO factura (id_consulta, fecha, total) VALUES\n'
                                  "  (1, TIMESTAMP '2026-09-01 09:40:00', 71000),\n"
                                  "  (2, TIMESTAMP '2026-09-02 11:35:00', 47000),\n"
                                  "  (3, TIMESTAMP '2026-09-05 15:50:00', 60200);\n"
                                  '\n'
                                  'INSERT INTO detalle_factura (id_factura, id_insumo, cantidad, '
                                  'precio_unit) VALUES\n'
                                  '  (1, 2, 1, 31000),\n'
                                  '  (1, 6, 1,   900),\n'
                                  '  (1, 3, 1,  9500),\n'
                                  '  (2, 3, 1,  9500),\n'
                                  '  (2, 4, 1,  7000),\n'
                                  '  (3, 1, 1, 22000),\n'
                                  '  (3, 5, 4,  1200),\n'
                                  '  (3, 6, 2,   900);\n',
                     'tipo': 'bd_sql'},
                    {'correctas': [0, 1, 3, 5],
                     'enunciado': '## 3. Checklist de empaquetado del ZIP final\n'
                                  '\n'
                                  'Vas a subir el paquete final al modulo de Proyectos de '
                                  'ExamLab. Selecciona **todas** las afirmaciones correctas sobre '
                                  'como debe quedar armado el entregable.',
                     'opciones': ['Los scripts deben ir numerados en su orden de ejecucion '
                                  '(01_ddl.sql, 02_datos.sql, 03_logica.sql, ...) para que '
                                  'cualquiera pueda reconstruir la base de cero.',
                                  'Debe incluirse un README que diga en que motor se probo '
                                  '(PostgreSQL), como ejecutar los scripts y en que orden, y quien '
                                  'hizo que.',
                                  'Basta con adjuntar capturas de pantalla de las consultas '
                                  'funcionando; el codigo fuente es opcional si la demo salio '
                                  'bien.',
                                  'El ER debe ir tanto en imagen (PNG o el diagrama Mermaid) como '
                                  'reflejado en el DDL: si no coinciden, el entregable es '
                                  'inconsistente.',
                                  'Conviene incluir las credenciales de tu base de datos en '
                                  'el README para que el docente pueda entrar.',
                                  'El informe debe traer las secciones que se fueron construyendo '
                                  'en el semestre: roles y privilegios, respaldo, optimizacion '
                                  'antes/despues, indices, transacciones, concurrencia y lecciones '
                                  'de casos reales.'],
                     'puntos': 10,
                     'rubrica': '10 puntos con las 4 opciones correctas y ninguna incorrecta; '
                                'puntaje proporcional por acierto parcial. Correctas: indices 0, '
                                '1, 3 y 5.',
                     'tipo': 'cerrada_multi'},
                    {'enunciado': '## 4. Acta de entrega y reparto de la sustentacion\n'
                                  '\n'
                                  'Entrega el acta que acompana el paquete final. Debe contener:\n'
                                  '\n'
                                  '1. **Identificacion**: tu nombre completo y codigo, nombre del '
                                  'proyecto, asignatura (Bases de Datos II, FI303215), '
                                  'periodo 2026-2 y fecha de entrega. Si el docente autorizo '
                                  'equipo, lista tambien a los demas integrantes.\n'
                                  '2. **Inventario del paquete**: tabla con cada archivo del ZIP, '
                                  'su proposito y su orden de ejecucion. Deben aparecer como '
                                  'minimo el DDL, los datos semilla, la logica (funciones, '
                                  'procedimientos, triggers), los indices, el par antes/despues de '
                                  'optimizacion, el script de pruebas de las tres reglas de '
                                  'negocio, el informe y el ER.\n'
                                  '3. **Trazabilidad hito por hito**: una fila por clase del '
                                  'semestre (1, 2, 3, 4, 6, 7, 8, 10, 11, 12, 13) indicando **que '
                                  'artefacto del paquete** contiene el avance de esa clase. Si '
                                  'algo quedo sin cerrar, dilo aqui.\n'
                                  '4. **Guion de la sustentacion (5 a 8 minutos)**: que bloque '
                                  'expones en cada tramo y cuantos minutos, sumando entre 5 y 8. '
                                  'Si trabajas en equipo autorizado, indica quien habla en cada '
                                  'bloque: **todos los integrantes deben hablar**.\n'
                                  '5. **Declaracion de autoria y uso de herramientas**: que hiciste '
                                  'tu (y cada integrante, si hubo equipo), y si usaste asistentes '
                                  'de IA o codigo de terceros, en que parte y como lo '
                                  'verificaste.\n'
                                  '6. **Estado final declarado**: `COMPLETO`, `COMPLETO CON '
                                  'OBSERVACIONES` o `INCOMPLETO`, con una justificacion de dos '
                                  'lineas y tu firma (y la de los demas integrantes, si hubo '
                                  'equipo).',
                     'puntos': 20,
                     'rubrica': 'Las 6 secciones estan completas. El inventario nombra archivos '
                                'concretos con su orden de ejecucion y cubre los minimos exigidos. '
                                'La trazabilidad asocia cada una de las 11 clases con un artefacto '
                                'real del paquete y reconoce lo que quedo abierto. El guion de '
                                'sustentacion suma entre 5 y 8 minutos y cubre todos los bloques; '
                                'si hubo equipo autorizado, asigna voz a todos los integrantes. '
                                'Hay '
                                'declaracion de autoria y uso de herramientas, y un estado final '
                                'justificado y firmado.',
                     'tipo': 'abierta'},
                    {'enunciado': '## 5. Autoevaluacion de cierre: que harias distinto\n'
                                  '\n'
                                  'Cierra el curso con una autoevaluacion honesta. Responde cada '
                                  'punto en 3 a 6 lineas:\n'
                                  '\n'
                                  '1. **La decision de diseno de la que estas mas orgulloso**: '
                                  'cual fue, por que la tomaste y que evidencia tienes de que fue '
                                  'acertada (una prueba que pasa, una consulta que bajo de X a Y '
                                  'milisegundos, un error que la base rechazo).\n'
                                  '2. **La decision que cambiarias**: que harias diferente si '
                                  'empezaras VetCare de nuevo desde la Clase 1. Se especifico: un '
                                  'tipo de dato, una tabla que falta, una regla que dejaste en la '
                                  'aplicacion y debio estar en la base, un indice que no servia.\n'
                                  '3. **El concepto que mas te costo** de todo el semestre '
                                  '(transacciones, concurrencia, planes de ejecucion, privilegios, '
                                  'triggers) y **como lo desatascaste**. Si todavia no lo tienes '
                                  'claro, dilo: reconocerlo vale mas que fingir.\n'
                                  '4. **De Oracle a PostgreSQL**: durante el curso pasaste de '
                                  'material escrito en PL/SQL a resolver todo en PL/pgSQL sobre '
                                  'PostgreSQL. Nombra **tres diferencias concretas de sintaxis o '
                                  'de comportamiento** que tuviste que aprender (por ejemplo '
                                  '`RAISE EXCEPTION` frente a `RAISE_APPLICATION_ERROR`, `GET '
                                  'DIAGNOSTICS ... ROW_COUNT` frente a `SQL%ROWCOUNT`, funcion de '
                                  'trigger separada del trigger, ausencia de `DUAL`) y por que '
                                  'importan.\n'
                                  '5. **Lo que se queda sin verificar**: que parte de tu diseno '
                                  '**no** pudiste probar en este entorno (concurrencia real con '
                                  'dos sesiones, roles con usuarios conectados de verdad, '
                                  'particionamiento con volumen real, respaldo fisico) y como lo '
                                  'verificarias en un servidor de produccion.\n'
                                  '6. **Nota que te pondrias** a tu propio trabajo en el PI, de 1 a '
                                  '5, con una linea de justificacion. Si trabajaste en equipo '
                                  'autorizado, agrega en una linea aparte la nota que le pondrias '
                                  'al aporte de cada integrante.',
                     'puntos': 15,
                     'rubrica': 'Los 6 puntos estan respondidos con especificidad y evidencia, no '
                                'con generalidades. El punto 1 cita una evidencia concreta y el 2 '
                                'nombra un cambio de diseno preciso. El punto 4 lista tres '
                                'diferencias reales entre PL/SQL y PL/pgSQL explicando por que '
                                'importan. El punto 5 identifica correctamente los limites del '
                                'entorno de practica y propone como verificarlos en produccion. La '
                                'autonota viene justificada.',
                     'tipo': 'abierta'}],
      'resumen': 'El estudiante entrega el script maestro de VetCare que se ejecuta de cero y '
                 'prueba sus tres reglas de negocio, los KPIs de la sustentacion, el acta de '
                 'entrega y la autoevaluacion de cierre.',
      'titulo': 'Taller Clase 15 en ExamLab - Entrega final y cierre de VetCare DB '
                '(previo a la sustentacion en vivo)'}}
