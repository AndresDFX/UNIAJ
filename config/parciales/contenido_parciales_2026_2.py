# -*- coding: utf-8 -*-
"""Contenido de los 12 parciales UNIAJC 2026-2 (4 cursos x 3 cortes).

SEMESTRE ACORTADO 2026-2 (inicio 24/08/2026, fin 22/11/2026) = 13 SESIONES por curso.
Los 15 temas del microcurriculo se conservan: 2 sesiones son DOBLES. Por eso hay que
distinguir dos numeraciones (fuente de verdad: config/calendario/semestre_2026_2.json):

  - SESION (1..13): la clase real del calendario. Es el numero que se muestra al
    estudiante en la portada del parcial (`meta['clase']` = numero de sesion).
  - CLASE DE MATERIAL (1..15): la carpeta «Clase N» del material, que NO se renumera.
    Es lo que se lista en `temas=[_tema(n, dd/mm, ...)]`; la fecha dd/mm es la fecha de
    la SESION en la que esa Clase de material se dicta.

Mapeo sesion -> clase(s) de material:
  - Prog II (mie) y Seminario (jue): S1-S4 = C1-C4 · S5 PARCIAL 1 (C5) · S6 = C6 ·
    S7 = C7 · S8 DOBLE = C8+C9 · S9 PARCIAL 2 (C10) · S10 DOBLE = C11+C12 ·
    S11 = C13 · S12 = C14 · S13 PARCIAL 3 (C15).
  - BD II y Arquitectura (lun): S1-S4 = C1-C4 · S5 PARCIAL 1 (C5) · S6 = C6 ·
    S7 DOBLE = C7+C8 · S8 autonoma (festivo 12/10) = C10 · S9 PARCIAL 2 (C9) ·
    S10 DOBLE = C11+C12 · S11 autonoma (festivo 02/11) = C13 · S12 PARCIAL 3 (C14) ·
    S13 sustentaciones del PI (C15).

Regla de cobertura (obligatoria): solo Clases de material efectivamente dictadas antes
del parcial (fecha de su sesion < fecha del parcial). Resultado:
  - Parcial 1 (los 4 cursos): Clases 1-4 (la C5 es el parcial mismo).
  - Parcial 2: Prog II / Seminario -> Clases 6, 7, 8, 9 (la sesion doble S8 dio C8+C9).
               BD II / Arquitectura -> Clases 6, 7, 8, 10 (la autonoma S8 del 12/10 fue
               la C10; la C9 es el parcial mismo).
  - Parcial 3: Prog II / Seminario -> Clases 11, 12, 13, 14 (C14 se dicta en S12).
               BD II / Arquitectura -> Clases 11, 12, 13 (la C14 es el parcial mismo y la
               C15 es la sustentacion del PI, posterior).

Otras reglas:
  - Clase 1: se evalua el arranque tematico (no la logistica de Presentacion del curso).
  - Formato en portada: «Clase N · DD/MM · Tema» (N = Clase de material).
  - Día de parcial = solo evaluación: la cobertura lista los temas en la clase
    donde se impartieron (no inventa tema técnico en la fila del parcial).
  - Dominio narrativo unico por curso: BD II = VetCare · Arquitectura = CloudLite.
"""
from __future__ import annotations

ROOT = r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos"


def _tema(n: int, fecha_dd_mm: str, tema: str) -> str:
    return f"Clase {n} · {fecha_dd_mm} · {tema}"


def _meta(**kw):
    return kw


def _sec(titulo, pts, items, intro=""):
    return {"titulo": titulo, "pts": pts, "items": items, "intro": intro}


PROG2_P1 = {
    "meta": _meta(
        curso_dir='Programacion II',
        asignatura='Programación II',
        codigo='FI303204',
        grupo='341C',
        periodo='2026-2',
        horario='Miércoles 18:00 – 20:00',
        n=1,
        corte=1,
        valor_corte='10% del Corte 1 (30%)',
        fecha='23/09/2026',
        clase=5,  # Sesion 5 del calendario (material: Clase 5 = dia del parcial)
        tiempo='90–100 minutos',
        titulo_parcial='Parcial 1 — POO, colecciones e interfaces GUI',
        secciones_resumen=['A. Selección múltiple — 20 pts',
 'B. Verdadero / Falso — 20 pts',
 'C. Desarrollo conceptual — 25 pts',
 'D. Práctica (Java / GUI) — 35 pts'],
        archivo='Parcial 1 - POO colecciones e interfaces GUI',
        cobertura=('Corte 1 (Sesiones 1-5) · Únicamente clases dictadas antes del 23/09/2026 '
 '(Clases 1, 2, 3 y 4 del material). La Clase 5 es la sesión del parcial:'),
        temas=[
            _tema(1, '26/08', 'Introducción a POO'),
            _tema(2, '02/09', 'Colecciones dinámicas ArrayList'),
            _tema(3, '09/09', 'Pilas y colas'),
            _tema(4, '16/09', 'Mapas y conjuntos · Interfaces gráficas GUI'),
        ],
    ),
    "secciones": [{'intro': '',
  'items': [{'clave': 'c',
             'id': 'A1',
             'nota': 'Polimorfismo: misma interfaz, comportamientos distintos.',
             'opciones': ['a) Encapsulamiento', 'b) Herencia', 'c) Polimorfismo', 'd) Abstracción'],
             'pregunta': 'En POO, ¿qué principio permite que una misma operación se comporte de '
                         'forma distinta según el tipo concreto del objeto?',
             'pts': 5,
             'tipo': 'mcq'},
            {'clave': 'b',
             'id': 'A2',
             'opciones': ['a) Tiene tamaño fijo al crearse, igual que un arreglo primitivo',
                          'b) Crece dinámicamente y permite acceso por índice',
                          'c) Solo almacena tipos primitivos',
                          'd) No permite duplicados'],
             'pregunta': '¿Cuál es una característica correcta de ArrayList en Java?',
             'pts': 5,
             'tipo': 'mcq'},
            {'clave': 'b',
             'id': 'A3',
             'opciones': ['a) FIFO', 'b) LIFO', 'c) Aleatoria', 'd) Por prioridad'],
             'pregunta': 'Una pila (Stack) opera preferentemente con la política:',
             'pts': 5,
             'tipo': 'mcq'},
            {'clave': 'b',
             'id': 'A4',
             'opciones': ['a) JLabel / Label',
                          'b) JTextField / TextField',
                          'c) JTable',
                          'd) JProgressBar'],
             'pregunta': 'En una interfaz gráfica Swing/JavaFX típica de clase, el componente más '
                         'adecuado para capturar un texto corto del usuario es:',
             'pts': 5,
             'tipo': 'mcq'}],
  'pts': 20,
  'titulo': 'SECCIÓN A — Selección múltiple'},
 {'intro': 'Indique V o F y justifique en una línea.',
  'items': [{'clave': 'F',
             'enunciado': 'Un HashSet garantiza el orden de inserción de sus elementos.',
             'id': 'B1',
             'justificacion': 'HashSet no garantiza orden; LinkedHashSet sí mantiene orden de '
                              'inserción.',
             'pts': 5,
             'tipo': 'vf'},
            {'clave': 'V',
             'enunciado': 'Una cola (Queue) procesa primero el elemento que llegó primero (FIFO).',
             'id': 'B2',
             'justificacion': 'Definición estándar de cola.',
             'pts': 5,
             'tipo': 'vf'},
            {'clave': 'V',
             'enunciado': 'En un Map, cada clave puede asociarse a lo sumo a un valor (en un '
                          'instante dado).',
             'id': 'B3',
             'justificacion': 'Modelo clave→valor; la clave es única.',
             'pts': 5,
             'tipo': 'vf'},
            {'clave': 'F',
             'enunciado': 'El encapsulamiento consiste en exponer todos los atributos como public '
                          'para facilitar el acceso.',
             'id': 'B4',
             'justificacion': 'Encapsulamiento oculta estado interno y expone acceso controlado.',
             'pts': 5,
             'tipo': 'vf'}],
  'pts': 20,
  'titulo': 'SECCIÓN B — Verdadero / Falso'},
 {'intro': '',
  'items': [{'enunciado': 'Compare ArrayList, HashMap y HashSet. Indique para cada uno: (1) qué '
                          'almacena, (2) si permite duplicados y (3) un caso de uso del Proyecto '
                          'Integrador / dominio académico.',
             'id': 'C1',
             'lineas': 5,
             'pts': 12,
             'solucion': ['ArrayList: secuencia indexada; permite duplicados; ej. lista de '
                          'pacientes/mascotas.',
                          'HashMap: pares clave-valor; claves únicas; ej. id→objeto, '
                          'código→precio.',
                          'HashSet: conjunto sin duplicados; no indexado; ej. etiquetas únicas, '
                          'ids ya procesados.',
                          'Rúbrica: 4 pts por estructura correcta + 4 pts casos de uso + 4 pts '
                          'claridad.'],
             'tipo': 'desarrollo'},
            {'enunciado': 'Explique con un ejemplo breve cuándo usaría una pila y cuándo una cola '
                          'en una aplicación con interfaz gráfica (por ejemplo, deshacer acciones '
                          'vs. atención de turnos).',
             'id': 'C2',
             'lineas': 5,
             'pts': 13,
             'solucion': ['Pila: Ctrl+Z / historial de pantallas (LIFO).',
                          'Cola: turnos de atención, cola de eventos a procesar (FIFO).',
                          'Rúbrica: 6 pts ejemplo pila + 6 pts ejemplo cola + 1 pt redacción.'],
             'tipo': 'desarrollo'}],
  'pts': 25,
  'titulo': 'SECCIÓN C — Desarrollo conceptual'},
 {'intro': '',
  'items': [{'enunciado': 'Diseñe (en código o pseudocódigo Java claro) una clase Producto con '
                          'atributos encapsulados (codigo, nombre, precio) y un '
                          'ArrayList<Producto> que permita: agregar, buscar por código y listar.',
             'id': 'D1',
             'lineas': 8,
             'pts': 20,
             'requerimientos': ['Constructores / getters-setters o métodos equivalentes.',
                                'Método buscarPorCodigo(String) que retorne el producto o '
                                'null/Optional.',
                                'Indique brevemente qué componentes GUI usaría para capturar datos '
                                'y mostrar el listado (sin implementar toda la GUI).'],
             'solucion': ['Clase Producto con private + getters/setters (6 pts).',
                          'Gestión con ArrayList: add, for/stream buscar, listar (8 pts).',
                          'GUI: JTextField/JButton para captura; JTextArea o JTable para listado '
                          '(6 pts).'],
             'tipo': 'practica'},
            {'codigo': 'Map<String,Integer> stock = ...;\n'
                       'int contador = 0;\n'
                       '// complete aquí\n'
                       'System.out.println(contador);',
             'enunciado': 'Dado el siguiente fragmento incompleto, complete la lógica para contar '
                          'cuántas claves de un Map<String,Integer> tienen valor mayor que 10:',
             'id': 'D2',
             'lineas': 4,
             'pts': 15,
             'solucion': ['for (Integer v : stock.values()) if (v != null && v > 10) contador++;',
                          'o entrySet/stream filter. 15 pts si correcto; 8 si idea parcial.'],
             'tipo': 'practica'}],
  'pts': 35,
  'titulo': 'SECCIÓN D — Práctica (Java / GUI)'}],
}

PROG2_P2 = {
    "meta": _meta(
        curso_dir='Programacion II',
        asignatura='Programación II',
        codigo='FI303204',
        grupo='341C',
        periodo='2026-2',
        horario='Miércoles 18:00 – 20:00',
        n=2,
        corte=2,
        valor_corte='10% del Corte 2 (30%)',
        fecha='21/10/2026',
        clase=9,  # Sesion 9 del calendario (material: Clase 10 = dia del parcial)
        tiempo='90–100 minutos',
        titulo_parcial='Parcial 2 — Eventos, patrones, QA y persistencia',
        secciones_resumen=['A. Selección múltiple — 20 pts',
 'B. Emparejamiento — 20 pts',
 'C. Desarrollo — 25 pts',
 'D. Práctica (eventos / archivos) — 35 pts'],
        archivo='Parcial 2 - Eventos patrones QA y persistencia',
        cobertura=('Corte 2 (Sesiones 6-9) · Únicamente clases dictadas antes del 21/10/2026 '
 '(Clases 6, 7, 8 y 9 del material; la sesión doble del 14/10 cubrió las Clases 8 y 9). '
 'No evalúa POO/ArrayList/GUI del Corte 1:'),
        temas=[
            _tema(6, '30/09', 'Eventos y controladores'),
            _tema(7, '07/10', 'Patrones de diseño'),
            _tema(8, '14/10', 'Documentación y QA (sesión doble)'),
            _tema(9, '14/10', 'Refactorización con IA · Persistencia de archivos (sesión doble)'),
        ],
    ),
    "secciones": [{'intro': '',
  'items': [{'clave': 'b',
             'id': 'A1',
             'opciones': ['a) Solo herencia múltiple',
                          'b) Eventos y controladores (listeners / handlers)',
                          'c) Serialización binaria obligatoria',
                          'd) Compilación JIT'],
             'pregunta': 'En una GUI, el patrón de separación típico donde la vista dispara '
                         'acciones y un controlador responde se relaciona con:',
             'pts': 5,
             'tipo': 'mcq'},
            {'clave': 'b',
             'id': 'A2',
             'opciones': ['a) Crear muchas instancias idénticas',
                          'b) Garantizar una única instancia con acceso global controlado',
                          'c) Separar interfaz de implementación de red',
                          'd) Ordenar colecciones'],
             'pregunta': 'El patrón Singleton busca:',
             'pts': 5,
             'tipo': 'mcq'},
            {'clave': 'b',
             'id': 'A3',
             'opciones': ['a) No comentar nunca el código',
                          'b) Pruebas, criterios de aceptación y documentación clara de métodos '
                          'públicos',
                          'c) Dejar warnings sin revisar',
                          'd) Duplicar lógica en cada clase'],
             'pregunta': 'Una buena práctica de QA / documentación de código incluye:',
             'pts': 5,
             'tipo': 'mcq'},
            {'clave': 'b',
             'id': 'A4',
             'opciones': ['a) Solo System.out.println en consola',
                          'b) Lectura/escritura con flujos (Files/BufferedWriter) serializando '
                          'campos',
                          'c) Usar únicamente variables static',
                          'd) Compilar a bytecode a mano'],
             'pregunta': 'Para persistir una lista de objetos en un archivo de texto/CSV en Java, '
                         'una opción válida del corte es:',
             'pts': 5,
             'tipo': 'mcq'}],
  'pts': 20,
  'titulo': 'SECCIÓN A — Selección múltiple'},
 {'intro': '',
  'items': [{'clave': '1-c, 2-b, 3-a, 4-d (5 pts c/u)',
             'col_a': ['1) Observer / Listener',
                       '2) MVC (idea)',
                       '3) Refactorización',
                       '4) Factory (idea)'],
             'col_b': ['a) Mejora estructura del código sin cambiar el comportamiento observable',
                       'b) Separa modelo, vista y control de la interacción',
                       'c) Reacciona a un evento (clic, cambio) cuando ocurre',
                       'd) Centraliza la creación de objetos según un criterio'],
             'id': 'B1',
             'instruccion': 'Empareje el concepto (Columna A) con su descripción (Columna B).',
             'pts': 20,
             'tipo': 'match'}],
  'pts': 20,
  'titulo': 'SECCIÓN B — Emparejamiento'},
 {'intro': '',
  'items': [{'enunciado': 'Describa un flujo de evento en GUI: componente → evento → '
                          'listener/controlador → actualización de modelo/vista. Use un ejemplo '
                          '(botón Guardar).',
             'id': 'C1',
             'lineas': 5,
             'pts': 12,
             'solucion': ['Botón genera ActionEvent; listener ejecuta guardar(); valida modelo; '
                          'persiste; refresca vista.',
                          'Rúbrica: secuencia completa 8 pts + ejemplo coherente 4 pts.'],
             'tipo': 'desarrollo'},
            {'enunciado': 'Indique 3 criterios para aceptar una refactorización asistida por IA '
                          '(qué revisar antes de fusionar el cambio).',
             'id': 'C2',
             'lineas': 4,
             'pts': 13,
             'solucion': ['Compila/pruebas pasan; comportamiento preservado; estilo legible; sin '
                          'secretos; cambios mínimos justificados.',
                          'Rúbrica: 4 pts por criterio válido (máx 12) + 1 pt claridad.'],
             'tipo': 'desarrollo'}],
  'pts': 25,
  'titulo': 'SECCIÓN C — Desarrollo'},
 {'intro': '',
  'items': [{'enunciado': 'Escriba un método Java (o pseudocódigo estricto) '
                          'guardarProductos(List<Producto> lista, Path archivo) que escriba '
                          'codigo;nombre;precio por línea, y otro cargarProductos que reconstruya '
                          'la lista.',
             'id': 'D1',
             'lineas': 8,
             'pts': 20,
             'requerimientos': ['Manejo básico de IOException (try/catch o throws).',
                                'Indique qué validaciones mínimas haría al cargar (línea mal '
                                'formada).'],
             'solucion': ['Escritura con BufferedWriter/Files.writeString línea a línea (8 pts).',
                          "Lectura split(';') y parseo (8 pts).",
                          'Validación campos/NumberFormat (4 pts).'],
             'tipo': 'practica'},
            {'enunciado': 'Proponga (texto + bosquejo) cómo conectaría un botón «Exportar» de la '
                          'GUI con el método de persistencia, sin bloquear indefinidamente la idea '
                          'de controlador.',
             'id': 'D2',
             'lineas': 5,
             'pts': 15,
             'solucion': ['Listener del botón llama al servicio/controlador exportar(); este '
                          'invoca guardarProductos; muestra mensaje éxito/error.',
                          'Rúbrica: separación vista/control 8 pts + manejo error 7 pts.'],
             'tipo': 'practica'}],
  'pts': 35,
  'titulo': 'SECCIÓN D — Práctica'}],
}

PROG2_P3 = {
    "meta": _meta(
        curso_dir='Programacion II',
        asignatura='Programación II',
        codigo='FI303204',
        grupo='341C',
        periodo='2026-2',
        horario='Miércoles 18:00 – 20:00',
        n=3,
        corte=3,
        valor_corte='15% del Corte 3 (40%)',
        fecha='18/11/2026',
        clase=13,  # Sesion 13 del calendario (material: Clase 15 = dia del parcial)
        tiempo='90–100 minutos',
        titulo_parcial='Parcial 3 — Integración, excepciones y cierre de proyecto',
        secciones_resumen=['A. Selección múltiple — 20 pts',
 'B. Verdadero / Falso — 20 pts',
 'C. Caso de integración — 25 pts',
 'D. Práctica (excepciones / revisión) — 35 pts'],
        archivo='Parcial 3 - Integracion excepciones y cierre de proyecto',
        cobertura=('Corte 3 (Sesiones 10-13) · Únicamente clases dictadas antes del 18/11/2026 '
 '(Clases 11, 12, 13 y 14 del material; la sesión doble del 28/10 cubrió las Clases 11 y 12). '
 'La Clase 15 es la sesión del parcial:'),
        temas=[
            _tema(11, '28/10', 'Revisión de código cruzada (sesión doble)'),
            _tema(12, '28/10', 'Integración de módulos (sesión doble)'),
            _tema(13, '04/11', 'Control de excepciones'),
            _tema(14, '11/11', 'Preparación de la presentación final'),
        ],
    ),
    "secciones": [{'intro': '',
  'items': [{'clave': 'b',
             'id': 'A1',
             'opciones': ['a) Reemplazar por completo las pruebas',
                          'b) Detectar defectos, mejorar calidad y compartir criterio técnico',
                          'c) Eliminar la documentación',
                          'd) Evitar el control de versiones'],
             'pregunta': 'Una revisión de código cruzada (peer review) busca principalmente:',
             'pts': 5,
             'tipo': 'mcq'},
            {'clave': 'a',
             'id': 'A2',
             'opciones': ['a) Que las interfaces entre módulos no coincidan (contratos rotos)',
                          'b) Que Java deje de ser tipado',
                          'c) Que el compilador ignore sintaxis',
                          'd) Que ArrayList se convierta en Map automáticamente'],
             'pregunta': 'Al integrar módulos, un riesgo frecuente es:',
             'pts': 5,
             'tipo': 'mcq'},
            {'clave': 'b',
             'id': 'A3',
             'opciones': ['a) Error de hardware irreversible',
                          'b) Excepción comprobada (checked)',
                          'c) Anotación de compilación',
                          'd) Tipo primitivo'],
             'pregunta': 'checked vs unchecked en Java (idea del corte): IOException es '
                         'típicamente:',
             'pts': 5,
             'tipo': 'mcq'},
            {'clave': 'b',
             'id': 'A4',
             'opciones': ['a) Ocultar los requisitos incumplidos sin mención',
                          'b) Demostrar funcionalidades, decisiones de diseño y lecciones '
                          'aprendidas',
                          'c) Solo leer el código línea por línea sin contexto',
                          'd) Entregar sin criterios de aceptación'],
             'pregunta': 'En la preparación de la presentación/evaluación del proyecto, un '
                         'elemento esencial es:',
             'pts': 5,
             'tipo': 'mcq'}],
  'pts': 20,
  'titulo': 'SECCIÓN A — Selección múltiple'},
 {'intro': '',
  'items': [{'clave': 'V',
             'enunciado': 'try/catch permite manejar errores recuperables sin terminar '
                          'abruptamente toda la aplicación.',
             'id': 'B1',
             'justificacion': 'Manejo controlado de excepciones.',
             'pts': 5,
             'tipo': 'vf'},
            {'clave': 'F',
             'enunciado': 'Integrar módulos solo consiste en copiar/pegar clases en un único '
                          'archivo .java.',
             'id': 'B2',
             'justificacion': 'Implica contratos, dependencias, pruebas de integración y '
                              'estructura de paquetes.',
             'pts': 5,
             'tipo': 'vf'},
            {'clave': 'V',
             'enunciado': 'finally se ejecuta (salvo casos extremos de aborto de JVM) tanto si '
                          'hubo excepción como si no.',
             'id': 'B3',
             'justificacion': 'Bloque de limpieza típico.',
             'pts': 5,
             'tipo': 'vf'},
            {'clave': 'V',
             'enunciado': 'Una buena checklist de code review incluye legibilidad, nombres, manejo '
                          'de errores y cobertura de casos límite.',
             'id': 'B4',
             'justificacion': 'Práctica estándar de revisión cruzada.',
             'pts': 5,
             'tipo': 'vf'}],
  'pts': 20,
  'titulo': 'SECCIÓN B — Verdadero / Falso'},
 {'intro': '',
  'items': [{'enunciado': 'Su Proyecto Integrador tiene módulos: (1) dominio/modelo, (2) '
                          'persistencia en archivo, (3) GUI. Describa un plan de integración de 4 '
                          'pasos y 2 pruebas de integración que ejecutaría antes de la '
                          'sustentación.',
             'id': 'C1',
             'lineas': 7,
             'pts': 25,
             'solucion': ['Pasos posibles: contratos de interfaces → integrar modelo+persistencia '
                          '→ conectar GUI → prueba end-to-end.',
                          'Pruebas: guardar/cargar desde GUI; flujo completo CRUD; manejo de '
                          'archivo inexistente.',
                          'Rúbrica: 12 pts plan + 10 pts pruebas + 3 pts claridad.'],
             'tipo': 'desarrollo'}],
  'pts': 25,
  'titulo': 'SECCIÓN C — Caso de integración'},
 {'intro': '',
  'items': [{'codigo': 'public List<Producto> cargar(Path p) {\n'
                       '  // proponga try/catch/finally o try-with-resources\n'
                       '}',
             'enunciado': 'Complete un manejo de excepciones adecuado para lectura de archivo. '
                          'Indique qué mensaje mostraría al usuario y qué registraría para '
                          'depuración.',
             'id': 'D1',
             'lineas': 6,
             'pts': 20,
             'solucion': ['try-with-resources; capturar IOException; mensaje amigable; log/print '
                          'stack en consola docente.',
                          'No tragar excepción vacía. 20 pts completo; 10 parcial.'],
             'tipo': 'practica'},
            {'enunciado': 'Redacte 5 ítems de una checklist de revisión de código cruzada '
                          'aplicables a un PR/módulo Java del curso.',
             'id': 'D2',
             'lineas': 5,
             'pts': 15,
             'solucion': ['Compila; nombres claros; sin código muerto; excepciones manejadas; '
                          'pruebas/manual smoke; encapsulamiento; sin secretos.',
                          '3 pts por ítem válido (máx 15).'],
             'tipo': 'practica'}],
  'pts': 35,
  'titulo': 'SECCIÓN D — Práctica'}],
}

SEM_P1 = {
    "meta": _meta(
        curso_dir='Seminario de Sistemas',
        asignatura='Seminario de Sistemas',
        codigo='FI303301',
        grupo='341C',
        periodo='2026-2',
        horario='Jueves 18:00 – 20:00',
        n=1,
        corte=1,
        valor_corte='10% del Corte 1 (30%)',
        fecha='24/09/2026',
        clase=5,  # Sesion 5 del calendario (material: Clase 5 = dia del parcial)
        tiempo='90–100 minutos',
        titulo_parcial='Parcial 1 — Ciclos de vida y metodologías',
        secciones_resumen=['A. Selección múltiple — 20 pts',
 'B. Emparejamiento — 20 pts',
 'C. Desarrollo — 25 pts',
 'D. Caso de estudio — 35 pts'],
        archivo='Parcial 1 - Ciclos de vida y metodologias',
        cobertura=('Corte 1 (Sesiones 1-5) · Únicamente clases dictadas antes del 24/09/2026 '
 '(Clases 1, 2, 3 y 4 del material). La Clase 5 es la sesión del parcial:'),
        temas=[
            _tema(1, '27/08', 'Conceptos iniciales'),
            _tema(2, '03/09', 'Ciclos de vida'),
            _tema(3, '10/09', 'Metodologías tradicionales'),
            _tema(4, '17/09', 'Metodologías ágiles'),
        ],
    ),
    "secciones": [{'intro': '',
  'items': [{'clave': 'b',
             'id': 'A1',
             'opciones': ['a) Solo la fase de codificación',
                          'b) Las etapas desde la concepción hasta el retiro/mantenimiento',
                          'c) Únicamente las pruebas de caja negra',
                          'd) El diseño gráfico de interfaces'],
             'pregunta': 'El ciclo de vida del software describe:',
             'pts': 5,
             'tipo': 'mcq'},
            {'clave': 'b',
             'id': 'A2',
             'opciones': ['a) Iteraciones cortas con entrega continua obligatoria',
                          'b) Fases secuenciales con poca vuelta atrás formal',
                          'c) Ausencia total de documentación',
                          'd) No definir requisitos'],
             'pregunta': 'El modelo en cascada se caracteriza por:',
             'pts': 5,
             'tipo': 'mcq'},
            {'clave': 'b',
             'id': 'A3',
             'opciones': ['a) Rechazar todo contacto con el cliente',
                          'b) Entregas incrementales, feedback frecuente y adaptación al cambio',
                          'c) Prohibir las pruebas',
                          'd) Eliminar roles del equipo'],
             'pregunta': 'Una diferencia clave de las metodologías ágiles frente a las '
                         'tradicionales es:',
             'pts': 5,
             'tipo': 'mcq'},
            {'clave': 'b',
             'id': 'A4',
             'opciones': ['a) Cascadas anuales fijas',
                          'b) Sprints / iteraciones cortas',
                          'c) Un único hito final sin revisión',
                          'd) Solo diagramas ER'],
             'pregunta': 'Scrum, como marco ágil, organiza el trabajo típicamente en:',
             'pts': 5,
             'tipo': 'mcq'}],
  'pts': 20,
  'titulo': 'SECCIÓN A — Selección múltiple'},
 {'intro': '',
  'items': [{'clave': '1-c, 2-b, 3-a, 4-d',
             'col_a': ['1) Cascada',
                       '2) Prototipado',
                       '3) Scrum',
                       '4) Extreme Programming (XP) — idea'],
             'col_b': ['a) Iteraciones con Product Backlog, Sprint y roles definidos',
                       'b) Construcción temprana de versiones para validar requisitos',
                       'c) Secuencia lineal de fases',
                       'd) Énfasis en prácticas técnicas (pruebas, integración frecuente, '
                       'simplicidad)'],
             'id': 'B1',
             'instruccion': 'Empareje metodología/modelo con su rasgo distintivo.',
             'pts': 20,
             'tipo': 'match'}],
  'pts': 20,
  'titulo': 'SECCIÓN B — Emparejamiento'},
 {'intro': '',
  'items': [{'enunciado': 'Defina ciclo de vida del software y nombre al menos 4 fases típicas, '
                          'explicando el propósito de cada una en una línea.',
             'id': 'C1',
             'lineas': 5,
             'pts': 12,
             'solucion': ['Definición + fases: requisitos, diseño, implementación, pruebas, '
                          'despliegue, mantenimiento.',
                          'Rúbrica: 4 definición + 8 fases (2 c/u).'],
             'tipo': 'desarrollo'},
            {'enunciado': 'Compare en una tabla mental (texto) metodologías tradicionales vs '
                          'ágiles en: cambio de requisitos, documentación y frecuencia de entrega.',
             'id': 'C2',
             'lineas': 5,
             'pts': 13,
             'solucion': ['Tradicional: cambio costoso, docs extensas, entrega tardía.',
                          'Ágil: cambio esperado, docs suficientes, entregas frecuentes.',
                          'Rúbrica: 4 pts por dimensión (máx 12) + 1 claridad.'],
             'tipo': 'desarrollo'}],
  'pts': 25,
  'titulo': 'SECCIÓN C — Desarrollo'},
 {'intro': '',
  'items': [{'contexto': 'Justifique con argumentos del Corte 1 (ciclos de vida y metodologías).',
             'enunciado': 'Caso: una clínica veterinaria necesita un sistema de citas. Los '
                          'requisitos aún son inciertos y el cliente quiere ver avances cada 2 '
                          'semanas.',
             'id': 'D1',
             'lineas': 9,
             'pts': 35,
             'requerimientos': ['a) ¿Qué enfoque metodológico recomendaría y por qué? (10 pts)',
                                'b) ¿Qué riesgos tendría usar cascada pura aquí? (10 pts)',
                                'c) Proponga un ciclo de 3 sprints con objetivo de cada uno (15 '
                                'pts)'],
             'solucion': ['Ágil/Scrum por incertidumbre y feedback (10).',
                          'Cascada: retrabajo tardío, poca validación temprana (10).',
                          'Sprints: backlog citas; CRUD/agenda; notificaciones/reporte (15).'],
             'tipo': 'practica'}],
  'pts': 35,
  'titulo': 'SECCIÓN D — Caso de estudio'}],
}

SEM_P2 = {
    "meta": _meta(
        curso_dir='Seminario de Sistemas',
        asignatura='Seminario de Sistemas',
        codigo='FI303301',
        grupo='341C',
        periodo='2026-2',
        horario='Jueves 18:00 – 20:00',
        n=2,
        corte=2,
        valor_corte='10% del Corte 2 (30%)',
        fecha='22/10/2026',
        clase=9,  # Sesion 9 del calendario (material: Clase 10 = dia del parcial)
        tiempo='90–100 minutos',
        titulo_parcial='Parcial 2 — Requerimientos, UML y casos de uso',
        secciones_resumen=['A. Selección múltiple — 20 pts',
 'B. Verdadero / Falso — 20 pts',
 'C. Historias y requerimientos — 25 pts',
 'D. Caso UML / casos de uso — 35 pts'],
        archivo='Parcial 2 - Requerimientos UML y casos de uso',
        cobertura=('Corte 2 (Sesiones 6-9) · Únicamente clases dictadas antes del 22/10/2026 '
 '(Clases 6, 7, 8 y 9 del material; la sesión doble del 15/10 cubrió las Clases 8 y 9). '
 'No evalúa ciclos de vida/metodologías del Corte 1:'),
        temas=[
            _tema(6, '01/10', 'Requerimientos de software'),
            _tema(7, '08/10', 'Historias de usuario'),
            _tema(8, '15/10', 'Introducción a UML (sesión doble)'),
            _tema(9, '15/10', 'Casos de uso (sesión doble)'),
        ],
    ),
    "secciones": [{'intro': '',
  'items': [{'clave': 'b',
             'id': 'A1',
             'opciones': ['a) El color corporativo únicamente',
                          'b) Una capacidad o comportamiento que el sistema debe ofrecer',
                          'c) Solo el presupuesto del proyecto',
                          'd) La marca del computador del desarrollador'],
             'pregunta': 'Un requerimiento funcional describe:',
             'pts': 5,
             'tipo': 'mcq'},
            {'clave': 'a',
             'id': 'A2',
             'opciones': ['a) Como <rol>, quiero <objetivo>, para <beneficio>',
                          'b) SELECT * FROM historia',
                          'c) Solo un diagrama de clases',
                          'd) Un contrato legal notariado'],
             'pregunta': 'El formato típico de historia de usuario es:',
             'pts': 5,
             'tipo': 'mcq'},
            {'clave': 'b',
             'id': 'A3',
             'opciones': ['a) Un lenguaje de programación compilado',
                          'b) Un lenguaje de modelado para visualizar y documentar sistemas',
                          'c) Un motor de base de datos',
                          'd) Un protocolo de red'],
             'pregunta': 'UML es:',
             'pts': 5,
             'tipo': 'mcq'},
            {'clave': 'b',
             'id': 'A4',
             'opciones': ['a) Una clase abstracta interna obligatoria',
                          'b) Un rol externo que interactúa con el sistema',
                          'c) Un servidor físico',
                          'd) Un caso de prueba unitaria'],
             'pregunta': 'En un diagrama de casos de uso, un actor representa:',
             'pts': 5,
             'tipo': 'mcq'}],
  'pts': 20,
  'titulo': 'SECCIÓN A — Selección múltiple'},
 {'intro': '',
  'items': [{'clave': 'V',
             'enunciado': 'Los requerimientos no funcionales incluyen aspectos como rendimiento, '
                          'seguridad y usabilidad.',
             'id': 'B1',
             'justificacion': 'Calidad del servicio / restricciones.',
             'pts': 5,
             'tipo': 'vf'},
            {'clave': 'F',
             'enunciado': 'Una historia de usuario no necesita criterios de aceptación.',
             'id': 'B2',
             'justificacion': 'Los criterios de aceptación definen «terminado».',
             'pts': 5,
             'tipo': 'vf'},
            {'clave': 'V',
             'enunciado': 'include en casos de uso indica comportamiento común reutilizado por '
                          'otros casos.',
             'id': 'B3',
             'justificacion': 'Relación include de UML.',
             'pts': 5,
             'tipo': 'vf'},
            {'clave': 'F',
             'enunciado': 'UML solo sirve para dibujar pantallas (wireframes) y no modela '
                          'comportamiento.',
             'id': 'B4',
             'justificacion': 'UML cubre estructura y comportamiento (casos de uso, secuencia, '
                              'etc.).',
             'pts': 5,
             'tipo': 'vf'}],
  'pts': 20,
  'titulo': 'SECCIÓN B — Verdadero / Falso'},
 {'intro': '',
  'items': [{'enunciado': 'Escriba 2 requerimientos funcionales y 2 no funcionales para un sistema '
                          'de préstamo de equipos en la universidad.',
             'id': 'C1',
             'lineas': 5,
             'pts': 12,
             'solucion': ['RF: registrar préstamo; consultar disponibilidad.',
                          'RNF: respuesta < 2s; autenticación; disponibilidad 99%.',
                          '3 pts c/u bien clasificado (máx 12).'],
             'tipo': 'desarrollo'},
            {'enunciado': 'Redacte 2 historias de usuario con criterios de aceptación (al menos 2 '
                          'criterios por historia).',
             'id': 'C2',
             'lineas': 5,
             'pts': 13,
             'solucion': ['Formato rol/quiero/para + criterios Given/When/Then o lista '
                          'verificable.',
                          'Rúbrica: 6 y 7 pts por historia completa.'],
             'tipo': 'desarrollo'}],
  'pts': 25,
  'titulo': 'SECCIÓN C — Historias y requerimientos'},
 {'intro': '',
  'items': [{'enunciado': 'Para un sistema de inscripción a electivas:',
             'id': 'D1',
             'lineas': 9,
             'pts': 35,
             'requerimientos': ['a) Liste 3 actores y 5 casos de uso (10 pts)',
                                'b) Describa textual un caso de uso (nombre, actor, '
                                'precondiciones, flujo principal, postcondiciones) (15 pts)',
                                'c) Indique un include o extend justificado (10 pts)'],
             'solucion': ['Actores: Estudiante, Coordinador, Sistema pagos…',
                          'CU: Inscribir electiva, Consultar cupos, Cancelar, etc.',
                          'Descripción completa del flujo; include Autenticar.'],
             'tipo': 'practica'}],
  'pts': 35,
  'titulo': 'SECCIÓN D — Caso UML / casos de uso'}],
}

SEM_P3 = {
    "meta": _meta(
        curso_dir='Seminario de Sistemas',
        asignatura='Seminario de Sistemas',
        codigo='FI303301',
        grupo='341C',
        periodo='2026-2',
        horario='Jueves 18:00 – 20:00',
        n=3,
        corte=3,
        valor_corte='15% del Corte 3 (40%)',
        fecha='19/11/2026',
        clase=13,  # Sesion 13 del calendario (material: Clase 15 = dia del parcial + sustentacion)
        tiempo='90–100 minutos',
        titulo_parcial='Parcial 3 — UML avanzado, interfaces y proyecto',
        secciones_resumen=['A. Selección múltiple — 20 pts',
 'B. Emparejamiento — 20 pts',
 'C. Diseño UML / UI — 25 pts',
 'D. Caso de sustentación de proyecto — 35 pts'],
        archivo='Parcial 3 - UML avanzado interfaces y proyecto',
        cobertura=('Corte 3 (Sesiones 10-13) · Únicamente clases dictadas antes del 19/11/2026 '
 '(Clases 11, 12, 13 y 14 del material; la sesión doble del 29/10 cubrió las Clases 11 y 12). '
 'La Clase 15 es la sesión del parcial + sustentación:'),
        temas=[
            _tema(11, '29/10', 'Avance proyecto integrador (sesión doble)'),
            _tema(12, '29/10', 'Diagramas UML avanzados (sesión doble)'),
            _tema(13, '05/11', 'Diseño de interfaces'),
            _tema(14, '12/11', 'Preparación de la sustentación y cierre'),
        ],
    ),
    "secciones": [{'intro': '',
  'items': [{'clave': 'b',
             'id': 'A1',
             'opciones': ['a) Solo la herencia entre clases',
                          'b) El intercambio de mensajes entre objetos a lo largo del tiempo',
                          'c) El modelo entidad-relación',
                          'd) La topología de red física'],
             'pregunta': 'Un diagrama de secuencia UML enfatiza:',
             'pts': 5,
             'tipo': 'mcq'},
            {'clave': 'b',
             'id': 'A2',
             'opciones': ['a) Cero instancias exactamente',
                          'b) Una o muchas instancias',
                          'c) Herencia múltiple obligatoria',
                          'd) Un paquete cerrado'],
             'pregunta': 'En un diagrama de clases, la multiplicidad 1..* en una asociación '
                         'indica:',
             'pts': 5,
             'tipo': 'mcq'},
            {'clave': 'b',
             'id': 'A3',
             'opciones': ['a) Saturar la pantalla con todas las funciones a la vez',
                          'b) Claridad, consistencia, feedback al usuario y flujos simples',
                          'c) Ocultar mensajes de error siempre',
                          'd) Evitar etiquetas en los campos'],
             'pregunta': 'Una buena práctica de diseño de interfaces (UI) es:',
             'pts': 5,
             'tipo': 'mcq'},
            {'clave': 'b',
             'id': 'A4',
             'opciones': ['a) Improvisar sin trazabilidad a requisitos',
                          'b) Demostrar avance, artefactos (UML/UI) y decisiones frente a los '
                          'objetivos',
                          'c) Entregar solo código sin explicación',
                          'd) Omitir limitaciones conocidas'],
             'pregunta': 'En la sustentación del proyecto integrador se espera principalmente:',
             'pts': 5,
             'tipo': 'mcq'}],
  'pts': 20,
  'titulo': 'SECCIÓN A — Selección múltiple'},
 {'intro': '',
  'items': [{'clave': '1-a, 2-b, 3-c, 4-d',
             'col_a': ['1) Diagrama de clases',
                       '2) Diagrama de secuencia',
                       '3) Wireframe / mockup UI',
                       '4) Diagrama de estados (idea)'],
             'col_b': ['a) Muestra estructura estática (atributos, operaciones, relaciones)',
                       'b) Muestra interacción temporal entre objetos',
                       'c) Bosqueja pantallas y disposición de controles',
                       'd) Muestra ciclos de vida/estados de un objeto'],
             'id': 'B1',
             'instruccion': 'Relacione el artefacto con su propósito.',
             'pts': 20,
             'tipo': 'match'}],
  'pts': 20,
  'titulo': 'SECCIÓN B — Emparejamiento'},
 {'intro': '',
  'items': [{'enunciado': 'Proponga 3 clases del dominio de su proyecto (nombre + 2 atributos + 1 '
                          'relación entre ellas).',
             'id': 'C1',
             'lineas': 5,
             'pts': 12,
             'solucion': ['Clases coherentes al dominio + relación (asociación/composición) '
                          'justificada.',
                          '4 pts por clase/relación bien planteada (máx 12).'],
             'tipo': 'desarrollo'},
            {'enunciado': 'Liste 4 principios o heurísticas de UI aplicables a la pantalla '
                          'principal de su sistema y explique cada una en una línea.',
             'id': 'C2',
             'lineas': 5,
             'pts': 13,
             'solucion': ['Visibilidad de estado; correspondencia con mundo real; consistencia; '
                          'prevención de errores; feedback.',
                          'Rúbrica: ~3 pts c/u.'],
             'tipo': 'desarrollo'}],
  'pts': 25,
  'titulo': 'SECCIÓN C — Diseño UML / UI'},
 {'intro': '',
  'items': [{'enunciado': 'Elabore un guion breve de sustentación (máx. estructura pedida) para el '
                          'Proyecto Integrador del Seminario:',
             'id': 'D1',
             'lineas': 10,
             'pts': 35,
             'requerimientos': ['a) Problema y objetivo (5 pts)',
                                'b) Alcance / fuera de alcance (5 pts)',
                                'c) 2 artefactos UML que mostraría y qué demuestran (10 pts)',
                                'd) 1 flujo UI crítico paso a paso (10 pts)',
                                'e) Riesgos o trabajo futuro (5 pts)'],
             'solucion': ['Coherencia problema-objetivo-alcance; UML con propósito; UI navegable; '
                          'riesgos realistas.',
                          'Asignar pts según rúbrica del enunciado.'],
             'tipo': 'practica'}],
  'pts': 35,
  'titulo': 'SECCIÓN D — Caso de sustentación'}],
}

BD2_P1 = {
    "meta": _meta(
        curso_dir='Bases de Datos II',
        asignatura='Bases de Datos II',
        codigo='FI303215',
        grupo='641A-2',
        periodo='2026-2',
        horario='Lunes 18:00 – 20:00',
        n=1,
        corte=1,
        valor_corte='10% del Corte 1 (30%)',
        fecha='21/09/2026',
        clase=5,  # Sesion 5 del calendario (material: Clase 5 = dia del parcial)
        tiempo='90–100 minutos',
        titulo_parcial='Parcial 1 — Administración, procedimientos y seguridad',
        secciones_resumen=['A. Selección múltiple — 20 pts',
 'B. Verdadero / Falso — 20 pts',
 'C. SQL / objetos programables — 25 pts',
 'D. Caso seguridad y respaldo — 35 pts'],
        archivo='Parcial 1 - Administracion procedimientos y seguridad',
        cobertura=('Corte 1 (Sesiones 1-5) · Únicamente clases dictadas antes del 21/09/2026 '
 '(Clases 1, 2, 3 y 4 del material). La Clase 5 es la sesión del parcial:'),
        temas=[
            _tema(1, '24/08', 'Revisión de Bases de Datos I (VetCare)'),
            _tema(2, '31/08', 'Administración de bases de datos'),
            _tema(3, '07/09', 'Procedimientos almacenados'),
            _tema(4, '14/09', 'Funciones y disparadores · Seguridad y respaldo'),
        ],
    ),
    "secciones": [{'intro': '',
  'items': [{'clave': 'b',
             'id': 'A1',
             'opciones': ['a) Un índice clusterizado',
                          'b) Un programa SQL persistido en el SGBD que puede recibir parámetros y '
                          'ejecutar lógica',
                          'c) Un archivo CSV externo',
                          'd) Una vista materializada obligatoria'],
             'pregunta': 'Un procedimiento almacenado es:',
             'por_que': {
                 'a)': 'Un indice es una estructura de acceso a datos; no contiene logica ni '
                       'recibe parametros. Se ve en la Clase 7.',
                 'b)': 'CORRECTA. Es la definicion de la Clase 3: codigo que vive en el '
                       'catalogo del motor, recibe parametros y se invoca con CALL.',
                 'c)': 'Un CSV es un archivo de datos fuera del motor; no se ejecuta.',
                 'd)': 'Una vista materializada guarda el resultado de una consulta, no logica '
                       'con parametros, y nada la vuelve obligatoria.',
             },
             'pts': 5,
             'tipo': 'mcq'},
            {'clave': 'b',
             'id': 'A2',
             'opciones': ['a) Solo al iniciar el sistema operativo',
                          'b) Ante eventos DML/DDL definidos (INSERT/UPDATE/DELETE, según SGBD)',
                          'c) Únicamente con SELECT',
                          'd) Nunca de forma automática'],
             'pregunta': 'Un trigger (disparador) se ejecuta:',
             'por_que': {
                 'a)': 'Nada en el motor se dispara por el arranque del sistema operativo.',
                 'b)': 'CORRECTA. En la Clase 4 se vio el trigger DML por fila: INSERT, UPDATE '
                       'o DELETE sobre una tabla. El «segun SGBD» cubre los triggers de DDL, '
                       'que en PostgreSQL son otro objeto (event trigger) y NO se pidieron.',
                 'c)': 'Un SELECT no modifica filas, asi que no hay evento DML que disparar.',
                 'd)': 'Al contrario: automatico es precisamente su razon de ser —nadie tiene '
                       'que acordarse de llamarlo—.',
             },
             'pts': 5,
             'tipo': 'mcq'},
            {'clave': 'b',
             'id': 'A3',
             'opciones': ['a) No poder existir en el catálogo',
                          'b) Retornar un valor y usarse en expresiones SQL',
                          'c) Reemplazar al motor de transacciones',
                          'd) Eliminar la necesidad de permisos'],
             'pregunta': 'Una función almacenada, a diferencia típica de un procedimiento, suele:',
             'por_que': {
                 'a)': 'Las dos existen en el catalogo; eso no las distingue.',
                 'b)': 'CORRECTA. Es la diapositiva «PROCEDURE o FUNCTION: cual se puede usar '
                       'dentro de un SELECT» de la Clase 3: la funcion devuelve un valor y se '
                       'invoca DENTRO de una expresion; el procedimiento es sentencia suelta '
                       '(CALL). El criterio es donde se invoca, no el LANGUAGE.',
                 'c)': 'Ninguna reemplaza al motor de transacciones. El matiz real es el '
                       'contrario: un procedimiento puede abrir y cerrar transacciones y una '
                       'funcion corre dentro de la del que la llama.',
                 'd)': 'Los privilegios se siguen necesitando: hace falta EXECUTE, y ademas los '
                       'privilegios sobre las tablas que toca.',
             },
             'pts': 5,
             'tipo': 'mcq'},
            {'clave': 'b',
             'id': 'A4',
             'opciones': ['a) Usar un único usuario root/sa para todas las apps',
                          'b) Principio de mínimo privilegio y roles/permisos acotados',
                          'c) Compartir contraseñas en el chat del curso',
                          'd) Desactivar respaldos para ganar espacio'],
             'pregunta': 'Una práctica de seguridad en BD es:',
             'por_que': {
                 'a)': 'Es el antipatron que abre la Clase 2: un solo usuario compartido deja '
                       'sin trazabilidad y da a la app permisos que no necesita.',
                 'b)': 'CORRECTA. Minimo privilegio con roles acotados: es lo que se construyo '
                       'en la Clase 2 con los 4 roles de VetCare y sus GRANT/REVOKE.',
                 'c)': 'Compartir contrasenas por chat destruye la trazabilidad; no queda nada '
                       'que auditar despues.',
                 'd)': 'Desactivar respaldos cambia unos gigas por la perdida total. Es lo '
                       'contrario de la Clase 4.',
             },
             'pts': 5,
             'tipo': 'mcq'}],
  'pts': 20,
  'titulo': 'SECCIÓN A — Selección múltiple'},
 {'intro': '',
  'items': [{'clave': 'V',
             'enunciado': 'Un respaldo (backup) completo permite recuperar la BD ante pérdida o '
                          'corrupción, según la política definida.',
             'id': 'B1',
             'justificacion': 'V. Es el objetivo del respaldo, y la coletilla «segun la '
                              'politica definida» es lo que la hace verdadera: recupera hasta '
                              'el ultimo respaldo valido, no hasta el segundo anterior a la '
                              'perdida. Aceptar tambien la respuesta que precise que se pierde '
                              'lo ocurrido entre el ultimo respaldo y la falla (el RPO de la '
                              'Clase 4): es mas correcta, no menos.',
             'pts': 5,
             'tipo': 'vf'},
            {'clave': 'F',
             'enunciado': 'GRANT y REVOKE no tienen relación con el control de acceso en SQL.',
             'id': 'B2',
             'justificacion': 'F. GRANT y REVOKE SON el mecanismo estandar de control de acceso '
                              'en SQL: son las dos sentencias con las que se construyeron los 4 '
                              'roles de VetCare en la Clase 2. La afirmacion niega justo eso.',
             'pts': 5,
             'tipo': 'vf'},
            {'clave': 'V',
             'enunciado': 'Los disparadores pueden usarse para auditar cambios (registrar quién '
                          'modificó qué).',
             'id': 'B3',
             'justificacion': 'V. Es la demo de la Clase 4: fn_trg_audit_cita mas su CREATE '
                              'TRIGGER, que escribe quien y cuando usando OLD y NEW. La ventaja '
                              'es que nadie tiene que acordarse de registrarlo, ni siquiera '
                              'quien entra por fuera de la aplicacion.',
             'pts': 5,
             'tipo': 'vf'},
            {'clave': 'V',
             'enunciado': 'La administración de BD incluye usuarios, espacios, mantenimiento y '
                          'monitoreo, no solo escribir SELECT.',
             'id': 'B4',
             'justificacion': 'V. Es el alcance que abre la Clase 2: quien puede hacer que sobre '
                              'cada objeto, mas mantenimiento, monitoreo y respaldo. Escribir '
                              'consultas es la parte que ya traian de Bases de Datos I.',
             'pts': 5,
             'tipo': 'vf'}],
  'pts': 20,
  'titulo': 'SECCIÓN B — Verdadero / Falso'},
 {'intro': 'El dominio de esta sección no es VetCare a propósito: se evalúa el mecanismo, no '
           'la memoria del esquema del proyecto. Asuma y declare las tablas que necesite. La '
           'sintaxis es PL/pgSQL sobre PostgreSQL, que es el motor del curso.',
  'items': [{'enunciado': 'Escriba un procedimiento almacenado en PL/pgSQL (PostgreSQL, el motor '
                          'del curso) sp_registrar_prestamo que reciba id_usuario e id_equipo y '
                          'valide que el equipo esté disponible antes de insertar.',
             'id': 'C1',
             'lineas': 6,
             'pts': 15,
             'solucion': [
                 'Desglose: firma con los 2 parametros y LANGUAGE plpgsql 3 · leer el estado del '
                 'equipo con SELECT ... INTO 3 · IF NOT FOUND para el equipo que no existe 3 · '
                 'abortar con RAISE EXCEPTION cuando no esta disponible 3 · INSERT del prestamo '
                 '3. Total 15.',
                 'La clave conceptual: el enunciado pide validar contra OTRA tabla (el equipo), y '
                 'por eso no sirve un CHECK, que solo puede mirar columnas de su propia fila. Es '
                 'el argumento con el que la Clase 3 justifica el procedimiento.',
                 'El UPDATE que marca el equipo como no disponible NO se pidio: si aparece es '
                 'correcto y no se descuenta, pero tampoco suma por encima de 15.',
             ],
             'solucion_codigo': '-- Esquema minimo, para ejecutar la respuesta tal cual en ExamLab\n'
                                'CREATE TABLE equipo (\n'
                                '    id_equipo  INT PRIMARY KEY,\n'
                                '    nombre     TEXT NOT NULL,\n'
                                '    disponible BOOLEAN NOT NULL DEFAULT TRUE\n'
                                ');\n'
                                'CREATE TABLE prestamo (\n'
                                '    id_prestamo SERIAL PRIMARY KEY,\n'
                                '    id_usuario  INT NOT NULL,\n'
                                '    id_equipo   INT NOT NULL REFERENCES equipo(id_equipo),\n'
                                '    fecha       TIMESTAMP NOT NULL DEFAULT now()\n'
                                ');\n'
                                '\n'
                                'CREATE OR REPLACE PROCEDURE sp_registrar_prestamo(\n'
                                '    p_id_usuario INT,\n'
                                '    p_id_equipo  INT\n'
                                ')\n'
                                'LANGUAGE plpgsql\n'
                                'AS $$\n'
                                'DECLARE\n'
                                '    v_disponible BOOLEAN;\n'
                                'BEGIN\n'
                                '    SELECT disponible INTO v_disponible\n'
                                '      FROM equipo\n'
                                '     WHERE id_equipo = p_id_equipo;\n'
                                '\n'
                                '    IF NOT FOUND THEN\n'
                                "        RAISE EXCEPTION 'El equipo % no existe', p_id_equipo;\n"
                                '    END IF;\n'
                                '\n'
                                '    IF v_disponible IS NOT TRUE THEN\n'
                                "        RAISE EXCEPTION 'El equipo % no esta disponible', p_id_equipo;\n"
                                '    END IF;\n'
                                '\n'
                                '    INSERT INTO prestamo (id_usuario, id_equipo)\n'
                                '    VALUES (p_id_usuario, p_id_equipo);\n'
                                'END;\n'
                                '$$;',
             'errores': [
                 'SELECT ... INTO sin IF NOT FOUND: si el equipo no existe, la variable queda en '
                 'nulo, comparar nulo no da verdadero pero tampoco entra por el IF, y el '
                 'prestamo se inserta igual. Es el error mas frecuente: cuesta los 3 puntos de '
                 'ese IF, no los 15.',
                 'Avisar en vez de abortar (RAISE NOTICE en lugar de RAISE EXCEPTION): el '
                 'prestamo queda creado. Se descuentan los 3 puntos del aborto.',
                 'Sintaxis de otro motor (DELIMITER, EXEC, o el molde de MySQL): el enunciado '
                 'dice PL/pgSQL. Si la logica esta bien, descontar solo los 3 de la firma; no se '
                 'anula la pregunta.',
                 'Cuidado al calificar «yo lo corri y no dio error»: el CREATE pasa aunque los '
                 'nombres de tabla esten mal, porque PostgreSQL no los resuelve hasta la primera '
                 'ejecucion. En papel no se descuenta por eso, pero la evidencia es el CALL.',
             ],
             'tipo': 'desarrollo'},
            {'enunciado': 'Proponga un trigger AFTER UPDATE sobre una tabla Prestamo que inserte '
                          'un registro en Auditoria_Prestamo con fecha y valores relevantes.',
             'id': 'C2',
             'lineas': 4,
             'pts': 10,
             'solucion': [
                 'Desglose: los DOS objetos —la funcion y el CREATE TRIGGER que la asocia— 4 · '
                 'evento correcto (AFTER UPDATE ON prestamo FOR EACH ROW) 3 · cuerpo que escribe '
                 'con OLD y NEW mas la fecha 3. Total 10.',
                 'Es la diapositiva «Un trigger son DOS objetos» de la Clase 4: en PostgreSQL la '
                 'funcion RETURNS TRIGGER se escribe aparte y el CREATE TRIGGER solo la asocia a '
                 'la tabla y al evento.',
             ],
             'solucion_codigo': 'CREATE TABLE auditoria_prestamo (\n'
                                '    id_auditoria SERIAL PRIMARY KEY,\n'
                                '    id_prestamo  INT  NOT NULL,\n'
                                '    campo        TEXT NOT NULL,\n'
                                '    valor_viejo  TEXT,\n'
                                '    valor_nuevo  TEXT,\n'
                                '    quien        TEXT      NOT NULL DEFAULT current_user,\n'
                                '    cuando       TIMESTAMP NOT NULL DEFAULT now()\n'
                                ');\n'
                                '\n'
                                '-- Objeto 1 de 2: la funcion\n'
                                'CREATE OR REPLACE FUNCTION fn_trg_audit_prestamo()\n'
                                'RETURNS TRIGGER\n'
                                'LANGUAGE plpgsql\n'
                                'AS $$\n'
                                'BEGIN\n'
                                '    IF NEW.id_equipo IS DISTINCT FROM OLD.id_equipo THEN\n'
                                '        INSERT INTO auditoria_prestamo\n'
                                '               (id_prestamo, campo, valor_viejo, valor_nuevo)\n'
                                "        VALUES (NEW.id_prestamo, 'id_equipo',\n"
                                '                OLD.id_equipo::TEXT, NEW.id_equipo::TEXT);\n'
                                '    END IF;\n'
                                '    RETURN NULL;  -- en un AFTER el valor de retorno se ignora\n'
                                'END;\n'
                                '$$;\n'
                                '\n'
                                '-- Objeto 2 de 2: la asociacion\n'
                                'CREATE TRIGGER trg_audit_prestamo\n'
                                'AFTER UPDATE ON prestamo\n'
                                'FOR EACH ROW\n'
                                'EXECUTE FUNCTION fn_trg_audit_prestamo();',
             'errores': [
                 'Un solo objeto: el CREATE TRIGGER sin la funcion, o la funcion sin el CREATE '
                 'TRIGGER. Falta la mitad del mecanismo: son los 4 puntos.',
                 'BEFORE UPDATE en vez de AFTER: para auditar da igual en la practica, pero el '
                 'enunciado pide AFTER. Descontar solo 1 de los 3 del evento.',
                 'EXECUTE PROCEDURE en lugar de EXECUTE FUNCTION: PostgreSQL lo sigue aceptando '
                 'por compatibilidad. No descontar.',
                 'RETURN NEW al final de un trigger AFTER: es inofensivo, el valor se ignora. No '
                 'descontar.',
                 'Escribir solo el valor nuevo: el enunciado pide «valores relevantes», y una '
                 'auditoria sin el valor viejo no permite reconstruir el cambio. Descontar 1 de '
                 'los 3 del cuerpo.',
             ],
             'tipo': 'desarrollo'}],
  'pts': 25,
  'titulo': 'SECCIÓN C — SQL / objetos programables'},
 {'intro': '',
  'items': [{'enunciado': 'Una pyme pierde datos por borrado accidental. Diseñe una política '
                          'mínima de seguridad y respaldo:',
             'id': 'D1',
             'lineas': 9,
             'pts': 35,
             'requerimientos': ['a) 3 controles de acceso (roles/privilegios) (9 pts)',
                                'b) Tipo de respaldo (lógico, físico, registro continuo de '
                                'transacciones) y frecuencia justificada (10 pts)',
                                'c) Prueba de restauración: qué validaría (8 pts)',
                                'd) Relacione cómo un procedimiento podría restringir operaciones '
                                'sensibles (8 pts)'],
             'solucion': [
                 'Desglose de los 35: (a) 3 controles x 3 = 9 · (b) tipos con la herramienta real '
                 '4 + frecuencia justificada con la operacion del negocio 3 + donde se guarda y '
                 'cuanto se conserva 3 = 10 · (c) que se restaura y donde 3 + consulta de '
                 'verificacion con valores esperados 3 + cada cuanto se ensaya 2 = 8 · (d) '
                 'EXECUTE sobre el procedimiento en vez del DML directo 4 + la validacion se '
                 'cumple aunque no entre por la app 2 + SECURITY DEFINER nombrado 2 = 8.',
                 '(a) Se piden CONTROLES, no nombres de rol: cada uno vale 3 solo si dice el '
                 'privilegio concreto sobre el objeto concreto. «Rol de lectura» sin el SELECT '
                 'vale 1. Tres roles razonables: app_lectura (SELECT), app_escritura (SELECT, '
                 'INSERT, UPDATE y sin DELETE) y un dba con la gestion de roles.',
                 '(b) Los tres tipos que se vieron en la Clase 4, con su herramienta: respaldo '
                 'logico con pg_dump -Fc (diario, fuera del horario de atencion), copia fisica '
                 'con pg_basebackup (semanal, para un RTO corto), y archivado de WAL (continuo, '
                 'es lo unico que recupera lo hecho DESPUES del ultimo dump). Se acepta cualquier '
                 'frecuencia que este justificada con la operacion del negocio; no hay una '
                 'respuesta unica. Y falta un cuarto que casi nadie pone: pg_dumpall '
                 '--globals-only para los roles. No exigirlo aqui, pero premiar si aparece.',
                 '(c) La prueba se hace en una base APARTE, nunca sobre produccion, y termina en '
                 'una consulta con valores esperados —conteos por tabla, la fila mas reciente— '
                 'que pueda fallar sola. «Revisar que los datos esten» no es una prueba: no es '
                 'verificable ni automatizable.',
                 '(d) Es el amarre de la Clase 3 con la Clase 2: se le quita el INSERT directo al '
                 'rol de la aplicacion y se le da EXECUTE sobre el procedimiento, de modo que la '
                 'unica forma de crear un prestamo es la que pasa por la validacion. El matiz que '
                 'vale 2 puntos: en PostgreSQL el cuerpo corre con los privilegios de QUIEN LLAMA '
                 'salvo que el procedimiento se declare SECURITY DEFINER; sin esa clausula, dar '
                 'EXECUTE no alcanza y la puerta no funciona.',
                 'El caso es una pyme generica, no Huellitas, a proposito: aqui se evalua el '
                 'criterio, y el plan de la clinica ya se califico en el taller de la Clase 4.',
             ],
             'solucion_codigo': '-- (a) Tres controles de acceso con minimo privilegio\n'
                                'CREATE ROLE app_lectura;\n'
                                'GRANT SELECT ON prestamo, equipo TO app_lectura;\n'
                                '\n'
                                'CREATE ROLE app_escritura;\n'
                                '-- SIN DELETE a proposito: el borrado no lo hace la aplicacion\n'
                                'GRANT SELECT, INSERT, UPDATE ON prestamo TO app_escritura;\n'
                                '\n'
                                'CREATE ROLE dba_prestamos;\n'
                                'GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public\n'
                                '   TO dba_prestamos;\n'
                                '\n'
                                '-- (d) El procedimiento como unica puerta a la operacion sensible\n'
                                'REVOKE INSERT ON prestamo FROM app_escritura;\n'
                                'GRANT EXECUTE ON PROCEDURE sp_registrar_prestamo(INT, INT)\n'
                                '   TO app_escritura;\n'
                                '-- Sin esto el cuerpo corre con los privilegios de quien llama y\n'
                                '-- el EXECUTE no alcanza: la puerta quedaria cerrada por dentro.\n'
                                'ALTER PROCEDURE sp_registrar_prestamo(INT, INT) SECURITY DEFINER;',
             'errores': [
                 'Creer que pg_dump respalda los roles y los permisos. No los respalda: pg_dump '
                 'es de UNA base y los roles son del cluster. Es el error tecnico mas comun de '
                 'esta pregunta; se corrige aunque el resto del plan este bien.',
                 'Herramientas de otro motor: RMAN, exp/imp o Data Pump son de Oracle y el curso '
                 'corre PostgreSQL. Descontar 2 de los 4 puntos de (b).',
                 'RPO y RTO como definiciones. Si el estudiante los menciona, la pregunta es '
                 'cuanto —en minutos u horas— y por que ese numero y no el doble. Aqui no se '
                 'exigen explicitamente, asi que no descontar por su ausencia, pero sirven para '
                 'decidir entre un 8 y un 10 en (b).',
                 'Un plan con solo un dump diario que declara un RPO de 15 minutos: el RPO ES de '
                 'hasta 24 horas, lo diga o no el documento. Un numero honesto y grande vale mas '
                 'que uno bonito que el plan no puede cumplir.',
                 'Tres roles con nombre y sin privilegios. Es la mitad de (a): 3 de 9.',
                 'Responder (d) con «el procedimiento valida» sin tocar los privilegios. La '
                 'pregunta es como se RESTRINGE: si el rol conserva el INSERT directo, la '
                 'validacion se puede saltar. Sin la parte de privilegios son 2 de 8.',
             ],
             'tipo': 'practica'}],
  'pts': 35,
  'titulo': 'SECCIÓN D — Caso seguridad y respaldo'}],
}

BD2_P2 = {
    "meta": _meta(
        curso_dir='Bases de Datos II',
        asignatura='Bases de Datos II',
        codigo='FI303215',
        grupo='641A-2',
        periodo='2026-2',
        horario='Lunes 18:00 – 20:00',
        n=2,
        corte=2,
        valor_corte='10% del Corte 2 (30%)',
        fecha='19/10/2026',
        clase=9,  # Sesion 9 del calendario (material: Clase 9 = dia del parcial)
        tiempo='90–100 minutos',
        titulo_parcial='Parcial 2 — Optimización, índices, transacciones y concurrencia',
        secciones_resumen=['A. Selección múltiple — 20 pts',
 'B. Emparejamiento — 20 pts',
 'C. Optimización SQL — 25 pts',
 'D. Caso transacciones, tuning y concurrencia — 35 pts'],
        archivo='Parcial 2 - Optimizacion indices y transacciones',
        cobertura=('Corte 2 (Sesiones 6-9) · Únicamente clases dictadas antes del 19/10/2026 '
 '(Clases 6, 7, 8 y 10 del material; la sesión doble del 05/10 cubrió las Clases 7 y 8 y la '
 'sesión autónoma del 12/10 fue la Clase 10). La Clase 9 es la sesión del parcial:'),
        temas=[
            _tema(6, '28/09', 'Optimización de consultas'),
            _tema(7, '05/10', 'Índices y particionamiento (sesión doble)'),
            _tema(8, '05/10', 'Tuning de bases de datos · Gestión de transacciones (sesión doble)'),
            _tema(10, '12/10', 'Control de concurrencia (sesión autónoma)'),
        ],
    ),
    "secciones": [{'intro': '',
  'items': [{'clave': 'b',
             'id': 'A1',
             'opciones': ['a) Eliminar la necesidad de WHERE',
                          'b) Acelerar búsquedas/filtros/ordenamientos sobre columnas indexadas',
                          'c) Reemplazar las transacciones',
                          'd) Garantizar normalización 5FN'],
             'pregunta': 'Un índice B-Tree típico ayuda principalmente a:',
             'pts': 4,
             'tipo': 'mcq'},
            {'clave': 'b',
             'id': 'A2',
             'opciones': ['a) Borrar tablas rápidamente',
                          'b) Analizar cómo el optimizador accederá a los datos',
                          'c) Crear usuarios',
                          'd) Compactar el sistema operativo'],
             'pregunta': 'EXPLAIN / plan de ejecución se usa para:',
             'pts': 4,
             'tipo': 'mcq'},
            {'clave': 'b',
             'id': 'A3',
             'opciones': ['a) Que las transacciones son visibles a medias',
                          'b) Todo o nada: o se confirman todos los cambios o ninguno',
                          'c) Que no hay aislamiento',
                          'd) Que el disco no puede fallar'],
             'pregunta': 'ACID: la «A» (Atomicity) significa:',
             'pts': 4,
             'tipo': 'mcq'},
            {'clave': 'a',
             'id': 'A4',
             'opciones': ['a) Dividir grandes volúmenes para administración y rendimiento',
                          'b) Eliminar claves primarias',
                          'c) Prohibir índices',
                          'd) Convertir SQL en NoSQL automáticamente'],
             'pregunta': 'El particionamiento de tablas busca, entre otros:',
             'pts': 4,
             'tipo': 'mcq'},
            {'clave': 'c',
             'id': 'A5',
             'nota': 'Clase 10 — Control de concurrencia: solo SERIALIZABLE evita lecturas '
                     'fantasma; READ COMMITTED las permite.',
             'opciones': ['a) READ UNCOMMITTED',
                          'b) READ COMMITTED',
                          'c) SERIALIZABLE',
                          'd) Ninguno: el nivel de aislamiento no influye en las lecturas'],
             'pregunta': 'En VetCare, un reporte de facturación mensual no debe ver consultas '
                         'veterinarias insertadas por otras transacciones mientras se ejecuta '
                         '(lectura fantasma). El nivel de aislamiento que lo garantiza es:',
             'pts': 4,
             'tipo': 'mcq'}],
  'pts': 20,
  'titulo': 'SECCIÓN A — Selección múltiple'},
 {'intro': '',
  'items': [{'clave': '1-a, 2-b, 3-c, 4-d, 5-e, 6-f',
             'col_a': ['1) COMMIT', '2) ROLLBACK', '3) Índice compuesto', '4) Full table scan',
                       '5) Deadlock', '6) MVCC'],
             'col_b': ['a) Confirma definitivamente los cambios de la transacción',
                       'b) Deshace cambios no confirmados',
                       'c) Índice sobre varias columnas',
                       'd) Lectura completa de la tabla; a menudo costosa en tablas grandes',
                       'e) Dos transacciones se bloquean mutuamente esperando recursos que la otra '
                       'retiene',
                       'f) Cada lectura ve una versión consistente de la fila sin bloquear a los '
                       'escritores'],
             'id': 'B1',
             'instruccion': 'Empareje concepto de transacciones, tuning y control de concurrencia '
                            '(1-4: Clases 7-8 · 5-6: Clase 10). Cada pareja vale 3,33 pts.',
             'pts': 20,
             'tipo': 'match'}],
  'pts': 20,
  'titulo': 'SECCIÓN B — Emparejamiento'},
 {'intro': '',
  'items': [{'enunciado': "Dada la consulta: SELECT * FROM Pedido WHERE fecha >= '2026-01-01' AND "
                          'cliente_id = 45; proponga 3 mejoras de optimización (índices, '
                          'proyección de columnas, etc.) y justifique.',
             'id': 'C1',
             'lineas': 5,
             'pts': 15,
             'solucion': ['Evitar SELECT *; índice (cliente_id, fecha); estadísticas actualizadas; '
                          'evitar funciones sobre columna filtrada.',
                          '5 pts por mejora válida justificada (máx 15).'],
             'tipo': 'desarrollo'},
            {'enunciado': 'Explique una ventaja y un costo/riesgo de crear muchos índices en una '
                          'tabla de alta escritura.',
             'id': 'C2',
             'lineas': 3,
             'pts': 10,
             'solucion': ['Ventaja: lecturas más rápidas. Costo: más espacio y escrituras más '
                          'lentas (mantenimiento de índices).'],
             'tipo': 'desarrollo'}],
  'pts': 25,
  'titulo': 'SECCIÓN C — Optimización SQL'},
 {'intro': '',
  'items': [{'enunciado': 'VetCare: al facturar una consulta se debe descontar el lote de vacuna '
                          'del inventario y registrar el movimiento contable. Las dos escrituras '
                          'deben ser atómicas.',
             'id': 'D1',
             'lineas': 8,
             'pts': 25,
             'requerimientos': ['a) Escriba pseudocódigo/SQL transaccional (BEGIN/COMMIT/ROLLBACK) '
                                '(10 pts)',
                                'b) Indique qué pasa si falla el movimiento contable tras '
                                'descontar el inventario, sin transacción (8 pts)',
                                'c) Mencione 2 acciones de tuning si el reporte mensual de '
                                'facturación se vuelve lento (7 pts)'],
             'solucion': ['BEGIN; UPDATE inventario_lote SET cantidad = cantidad - 1 …; INSERT INTO '
                          'movimiento_contable …; COMMIT; ROLLBACK ante error.',
                          'Inventario descontado sin respaldo contable: descuadre permanente '
                          '(pérdida de atomicidad).',
                          'Índices en (fecha, sede); particionar por mes; tabla/vista materializada '
                          'de resumen.'],
             'tipo': 'practica'},
            {'enunciado': 'Control de concurrencia en VetCare (Clase 10): dos recepcionistas '
                          'facturan al mismo tiempo y cada transacción actualiza el lote de vacuna '
                          'y la ficha del paciente, pero en orden inverso. El motor aborta una con '
                          'error de deadlock.',
             'id': 'D2',
             'lineas': 6,
             'pts': 10,
             'requerimientos': ['a) Explique por qué se produce el deadlock en este escenario '
                                '(4 pts)',
                                'b) Proponga 2 medidas para evitarlo (orden fijo de acceso a los '
                                'recursos, transacciones cortas, bloqueo explícito con FOR UPDATE, '
                                'reintento controlado) (4 pts)',
                                'c) Diga qué nivel de aislamiento usaría y qué anomalía evita '
                                '(2 pts)'],
             'solucion': ['Espera circular: T1 retiene el bloqueo del lote y pide la ficha; T2 '
                          'retiene la ficha y pide el lote. Ninguna puede avanzar y el motor '
                          'sacrifica una (víctima del deadlock).',
                          '2 pts por medida válida: ordenar siempre los UPDATE por el mismo '
                          'recurso, mantener las transacciones cortas (no esperar entrada del '
                          'usuario dentro de la transacción), SELECT … FOR UPDATE sobre el lote, '
                          'reintento con backoff en la aplicación.',
                          'READ COMMITTED evita lecturas sucias; SERIALIZABLE (o SELECT FOR UPDATE '
                          'sobre el lote) evita la actualización perdida del inventario. Se acepta '
                          'cualquiera de las dos con justificación coherente.'],
             'tipo': 'practica'}],
  'pts': 35,
  'titulo': 'SECCIÓN D — Caso transacciones, tuning y concurrencia'}],
}

BD2_P3 = {
    "meta": _meta(
        curso_dir='Bases de Datos II',
        asignatura='Bases de Datos II',
        codigo='FI303215',
        grupo='641A-2',
        periodo='2026-2',
        horario='Lunes 18:00 – 20:00',
        n=3,
        corte=3,
        valor_corte='15% del Corte 3 (40%)',
        fecha='09/11/2026',
        clase=12,  # Sesion 12 del calendario (material: Clase 14 = dia del parcial)
        tiempo='90–100 minutos',
        titulo_parcial='Parcial 3 — Integración, casos y cierre de proyecto',
        secciones_resumen=['A. Selección múltiple — 20 pts',
 'B. Verdadero / Falso — 20 pts',
 'C. Integración de aplicaciones — 25 pts',
 'D. Caso / preparación de sustentación BD — 35 pts'],
        archivo='Parcial 3 - Integracion casos y cierre de proyecto',
        cobertura=('Corte 3 (Sesiones 10-13) · Únicamente clases dictadas antes del 09/11/2026 '
 '(Clases 11, 12 y 13 del material; la sesión doble del 26/10 cubrió las Clases 11 y 12 y la '
 'sesión autónoma del 02/11 fue la Clase 13). La Clase 14 es la sesión del parcial y la Clase 15 '
 '(16/11) es la sustentación del Proyecto Integrador, posterior:'),
        temas=[
            _tema(11, '26/10', 'Avance del proyecto final (sesión doble)'),
            _tema(12, '26/10', 'Integración de aplicaciones externas · Preparación de presentación final (sesión doble)'),
            _tema(13, '02/11', 'Análisis de casos reales (sesión autónoma)'),
        ],
    ),
    "secciones": [{'intro': '',
  'items': [{'clave': 'b',
             'id': 'A1',
             'opciones': ['a) Ignorar autenticación',
                          'b) Contratos de acceso (API/SQL), credenciales seguras y manejo de '
                          'errores',
                          'c) Desactivar todas las FK',
                          'd) Usar solo archivos Excel locales sin control'],
             'pregunta': 'Integrar una aplicación externa con la BD típicamente requiere:',
             'pts': 5,
             'tipo': 'mcq'},
            {'clave': 'b',
             'id': 'A2',
             'opciones': ['a) Usar cuentas con privilegios mínimos',
                          'b) Embebir contraseñas en el código fuente público',
                          'c) Parametrizar consultas',
                          'd) Monitorear fallos de conexión'],
             'pregunta': 'Un anti-patrón al integrar apps con BD es:',
             'pts': 5,
             'tipo': 'mcq'},
            {'clave': 'b',
             'id': 'A3',
             'opciones': ['a) Copiar sin comprender',
                          'b) Extraer lecciones de arquitectura, rendimiento, seguridad o fallos',
                          'c) Evitar documentar',
                          'd) Eliminar el modelo relacional siempre'],
             'pregunta': 'En el análisis de casos reales de BD se busca:',
             'pts': 5,
             'tipo': 'mcq'},
            {'clave': 'b',
             'id': 'A4',
             'opciones': ['a) Solo capturas sin explicar el avance',
                          'b) Avance del PI, integración con apps, lecciones de casos y guion de '
                          'sustentación',
                          'c) Únicamente el logo del SGBD',
                          'd) Código ofuscado sin demo'],
             'pregunta': 'Para la preparación de la presentación final del proyecto de BD II es '
                         'clave mostrar:',
             'pts': 5,
             'tipo': 'mcq'}],
  'pts': 20,
  'titulo': 'SECCIÓN A — Selección múltiple'},
 {'intro': '',
  'items': [{'clave': 'V',
             'enunciado': 'Una API que consume la BD debe validar entradas para reducir inyección '
                          'SQL y datos inválidos.',
             'id': 'B1',
             'justificacion': 'Seguridad en integración.',
             'pts': 5,
             'tipo': 'vf'},
            {'clave': 'F',
             'enunciado': 'La integración externa nunca necesita considerar transacciones o '
                          'consistencia.',
             'id': 'B2',
             'justificacion': 'La consistencia sigue siendo crítica en integraciones.',
             'pts': 5,
             'tipo': 'vf'},
            {'clave': 'V',
             'enunciado': 'Documentar supuestos y limitaciones fortalece la sustentación del '
                          'proyecto.',
             'id': 'B3',
             'justificacion': 'Transparencia académica/profesional.',
             'pts': 5,
             'tipo': 'vf'},
            {'clave': 'V',
             'enunciado': 'Un avance de proyecto final debería alinear entregables con la '
                          'integración, análisis de casos y la preparación de la sustentación del '
                          'corte.',
             'id': 'B4',
             'justificacion': 'Trazabilidad con Clases 11–13 del Corte 3.',
             'pts': 5,
             'tipo': 'vf'}],
  'pts': 20,
  'titulo': 'SECCIÓN B — Verdadero / Falso'},
 {'intro': '',
  'items': [{'enunciado': 'Diseñe la integración de una app web/móvil con su BD del proyecto: '
                          'componentes, flujo de autenticación a BD (o vía API), y 3 fallos a '
                          'manejar (timeout, dato duplicado, permiso denegado).',
             'id': 'C1',
             'lineas': 7,
             'pts': 25,
             'solucion': ['App → API → BD; pool conexiones; errores mapeados a mensajes.',
                          'Rúbrica: arquitectura 10 + auth/acceso 7 + fallos 8.'],
             'tipo': 'desarrollo'}],
  'pts': 25,
  'titulo': 'SECCIÓN C — Integración'},
 {'intro': '',
  'items': [{'enunciado': 'Prepare un esquema de presentación final (guion) de su proyecto de BD '
                          'II:',
             'id': 'D1',
             'lineas': 10,
             'pts': 35,
             'requerimientos': ['a) Problema y objetivos del PI (5 pts)',
                                'b) Estado de avance y entregables listos / pendientes (10 pts)',
                                'c) Diseño de integración con aplicación externa (API/SQL, '
                                'credenciales, errores) (10 pts)',
                                'd) Una lección de un caso real aplicable a su proyecto (5 pts)',
                                'e) Guion de presentación (orden de láminas / demo) (5 pts)'],
             'solucion': ['Evaluar completitud y coherencia con temas del Corte 3 (avance, '
                          'integración, casos, prep.); pts según rúbrica.'],
             'tipo': 'practica'}],
  'pts': 35,
  'titulo': 'SECCIÓN D — Caso / sustentación'}],
}

ARQ_P1 = {
    "meta": _meta(
        curso_dir='Arquitectura de Sistemas Computacionales',
        asignatura='Arquitectura de Sistemas Computacionales',
        codigo='FI303380',
        grupo='6303C',
        periodo='2026-2',
        horario='Lunes 10:00 – 12:00',
        n=1,
        corte=1,
        valor_corte='10% del Corte 1 (30%)',
        fecha='21/09/2026',
        clase=5,  # Sesion 5 del calendario (material: Clase 5 = dia del parcial)
        tiempo='90–100 minutos',
        titulo_parcial='Parcial 1 — Cloud, virtualización y distribuidos',
        secciones_resumen=['A. Selección múltiple — 20 pts',
 'B. Emparejamiento — 20 pts',
 'C. Desarrollo arquitectónico — 25 pts',
 'D. Caso de diseño — 35 pts'],
        archivo='Parcial 1 - Cloud virtualizacion y distribuidos',
        cobertura=('Corte 1 (Sesiones 1-5) · Únicamente clases dictadas antes del 21/09/2026 '
 '(Clases 1, 2, 3 y 4 del material). La Clase 5 es la sesión del parcial:'),
        temas=[
            _tema(1, '24/08', 'Introducción a arquitecturas cloud (CloudLite)'),
            _tema(2, '31/08', 'Modelos de servicio IaaS, PaaS, SaaS'),
            _tema(3, '07/09', 'Virtualización y contenedores'),
            _tema(4, '14/09', 'Microservicios · Arquitecturas distribuidas'),
        ],
    ),
    "secciones": [{'intro': '',
  'items': [{'clave': 'b',
             'id': 'A1',
             'opciones': ['a) Solo una aplicación de correo lista para el usuario final',
                          'b) Infraestructura (cómputo, almacenamiento, red) como servicio',
                          'c) Únicamente IDEs en el navegador sin VMs',
                          'd) Un lenguaje de programación nuevo'],
             'pregunta': 'IaaS se caracteriza por ofrecer principalmente:',
             'por_que': {
                 'a)': 'Una aplicacion lista para el usuario final es SaaS, no IaaS. Es la '
                       'confusion que la diapositiva de los tres modelos (Clase 2) separa.',
                 'b)': 'CORRECTA. Computo, almacenamiento y red como servicio: el proveedor da la '
                       'infraestructura y usted administra SO, runtime y aplicacion.',
                 'c)': 'Un IDE en el navegador es una herramienta, no un modelo de servicio, y el '
                       '«sin VMs» es falso: debajo hay maquinas.',
                 'd)': 'Ningun modelo de servicio consiste en un lenguaje nuevo.',
             },
             'pts': 5,
             'tipo': 'mcq'},
            {'clave': 'b',
             'id': 'A2',
             'opciones': ['a) Son exactamente lo mismo en todos los niveles',
                          'b) Los contenedores comparten el kernel del host y suelen ser más '
                          'livianos',
                          'c) Las VM nunca aíslan recursos',
                          'd) Los contenedores requieren un hipervisor Type-1 siempre'],
             'pregunta': 'Respecto a máquinas virtuales y contenedores:',
             'por_que': {
                 'a)': 'No son lo mismo: la VM virtualiza la maquina completa con su propio '
                       'kernel; el contenedor virtualiza el proceso y reusa el del host. Es la '
                       'comparacion de la Clase 3.',
                 'b)': 'CORRECTA. Compartir el kernel del host es exactamente lo que los hace '
                       'mas livianos y mas rapidos de arrancar.',
                 'c)': 'Las VM SI aislan recursos, y de forma mas fuerte que un contenedor: es su '
                       'principal ventaja frente a el.',
                 'd)': 'Un contenedor no necesita hipervisor. En Windows y macOS hay una VM '
                       'intermedia por el kernel, pero eso es un detalle de esas plataformas, no '
                       'un requisito del modelo, y el Type-1 es de servidor.',
             },
             'pts': 5,
             'tipo': 'mcq'},
            {'clave': 'b',
             'id': 'A3',
             'opciones': ['a) Imposible de desplegar',
                          'b) Despliegue e independencia de escalado por servicio (con mayor '
                          'complejidad operativa)',
                          'c) Eliminación total de redes',
                          'd) Un solo lenguaje obligatorio en todo el sistema'],
             'pregunta': 'Una ventaja de microservicios frente a un monolito es:',
             'por_que': {
                 'a)': 'Se despliegan perfectamente; lo que cambia es que hay mas piezas que '
                       'desplegar.',
                 'b)': 'CORRECTA, y note que la opcion correcta es la unica que nombra el costo '
                       '(«con mayor complejidad operativa»). Es el criterio de la Clase 4: el '
                       'beneficio es escalar y desplegar por servicio, y se paga en operacion.',
                 'c)': 'Al contrario: aparecen mas llamadas de red, que es de donde salen los '
                       'riesgos de la diapositiva «Distribuido implica fallos».',
                 'd)': 'Es lo opuesto: cada servicio puede usar su propio lenguaje. Que eso sea '
                       'buena idea en un proyecto de un semestre es otra discusion.',
             },
             'pts': 5,
             'tipo': 'mcq'},
            {'clave': 'b',
             'id': 'A4',
             'opciones': ['a) Que no exista latencia nunca',
                          'b) Consistencia, particiones de red y coordinación entre nodos',
                          'c) Que solo haya un proceso en un solo núcleo',
                          'd) La imposibilidad de usar APIs'],
             'pregunta': 'En arquitecturas distribuidas, un desafío típico es:',
             'por_que': {
                 'a)': 'Justo al revés: la latencia siempre existe y no se puede volver cero. La '
                       'Clase 4 la cuantifica al decidir si el aviso sale por cola.',
                 'b)': 'CORRECTA. Es la diapositiva «Distribuido implica fallos»: cada flecha del '
                       'diagrama es una llamada de red que puede tardar, perderse o llegar dos '
                       'veces, y de ahi salen la consistencia y la coordinacion.',
                 'c)': 'Un solo proceso en un solo nucleo describe lo contrario de un sistema '
                       'distribuido.',
                 'd)': 'Las APIs son precisamente el medio con el que se comunican los servicios; '
                       'no son imposibles.',
             },
             'pts': 5,
             'tipo': 'mcq'}],
  'pts': 20,
  'titulo': 'SECCIÓN A — Selección múltiple'},
 {'intro': '',
  # La clave era «1-a, 2-b, 3-c, 4-d»: la permutacion identidad. Las dos columnas estaban
  # en el mismo orden, asi que el estudiante que lo notaba se llevaba los 20 puntos sin
  # saber el tema. Se reordena la columna B —el contenido no cambia— para que la clave
  # quede 1-c, 2-a, 3-d, 4-b, sin ninguna pareja en su posicion original.
  'items': [{'clave': '1-c, 2-a, 3-d, 4-b (5 pts por pareja correcta)',
             'col_a': ['1) SaaS', '2) PaaS', '3) Contenedor', '4) Hipervisor'],
             'col_b': ['a) Plataforma para desplegar apps sin gestionar todo el SO',
                       'b) Software que permite ejecutar máquinas virtuales',
                       'c) Aplicación consumida por el usuario final (p. ej. correo/oficina en '
                       'nube)',
                       'd) Empaqueta app + dependencias; comparte kernel del host'],
             'id': 'B1',
             'instruccion': 'Empareje modelo/concepto con ejemplo o rasgo.',
             'por_que': {
                 '1-c': 'SaaS es el servicio ya terminado que se consume: correo, oficina en '
                        'nube. No se despliega nada propio.',
                 '2-a': 'PaaS es la plataforma donde usted despliega SU aplicacion sin '
                        'administrar todo el SO. Es la diferencia con SaaS que mas se confunde: '
                        'en PaaS todavia hay una aplicacion suya.',
                 '3-d': 'El contenedor empaqueta la aplicacion con sus dependencias y comparte '
                        'el kernel del host. De ahi que sea liviano.',
                 '4-b': 'El hipervisor es la capa que permite ejecutar maquinas virtuales, cada '
                        'una con su propio kernel. Es lo que el contenedor NO necesita.',
             },
             'errores': [
                 'Calificacion: 5 puntos por pareja correcta, no todo-o-nada. Un estudiante con '
                 '3 de 4 saca 15.',
                 'La confusion tipica es PaaS con SaaS: si empareja 2 con la aplicacion lista, '
                 'perdio esa pareja pero suele arrastrar tambien la de SaaS, porque son '
                 'excluyentes. Se descuentan las dos que quedaron mal, no las cuatro.',
                 'Confundir contenedor con hipervisor apunta a no haber distinguido kernel '
                 'compartido de kernel propio, que es el eje de la Clase 3. Vale la pena '
                 'senalarlo en la retroalimentacion, porque reaparece en el Parcial 2.',
             ],
             'pts': 20,
             'tipo': 'match'}],
  'pts': 20,
  'titulo': 'SECCIÓN B — Emparejamiento'},
 {'intro': '',
  'items': [{'enunciado': 'Compare IaaS, PaaS y SaaS indicando qué gestiona el proveedor vs el '
                          'cliente en cada uno (visión de responsabilidad).',
             'id': 'C1',
             'lineas': 5,
             'pts': 12,
             'solucion': [
                 'Desglose: 4 puntos por modelo bien contrastado. Total 12.',
                 'Es la diapositiva de los tres modelos de la Clase 2, con estas mismas palabras: '
                 'en IaaS usted administra SO, red y runtime y el proveedor da computo, red y '
                 'disco; en PaaS usted despliega la aplicacion y el proveedor gestiona el runtime '
                 'y el escalado basico; en SaaS consume el servicio listo y solo configura.',
                 'Los 4 puntos de cada modelo se dan cuando la respuesta reparte AMBOS lados. '
                 'Decir «en PaaS el proveedor gestiona el runtime» sin decir que queda del lado '
                 'del cliente vale 2: la pregunta es de reparto, no de definicion.',
                 'Decision de calificacion que viene del taller de la Clase 2: NO se acepta que '
                 'en PaaS o SaaS el cliente «deja de responder por su aplicacion». Cambia el '
                 'operador de la infraestructura, no el dueno del sistema. Si la respuesta lo '
                 'afirma, se descuentan 2 de los 4 de ese modelo, aunque el resto este bien.',
             ],
             'tipo': 'desarrollo'},
            {'enunciado': 'Explique 2 beneficios y 2 retos de adoptar microservicios en un sistema '
                          'académico pequeño.',
             'id': 'C2',
             'lineas': 4,
             'pts': 13,
             'solucion': [
                 'Desglose: 2 beneficios x 3 = 6 · 2 retos x 3 = 6 · 1 punto por aterrizarlo al '
                 'tamano que dice el enunciado (un sistema academico pequeno). Total 13.',
                 'Beneficios que cuentan: escalar solo el servicio que lo necesita, desplegar uno '
                 'sin tocar los demas, aislar el fallo, y permitir que dos personas trabajen sin '
                 'pisarse. Retos que cuentan, todos de la diapositiva «Distribuido implica '
                 'fallos» de la Clase 4: cada llamada de red puede tardar, perderse o llegar dos '
                 'veces; hay que saber que paso sin poder leer un solo registro; y aparece '
                 'trabajo de operacion (despliegue, versiones, monitoreo) que un monolito no '
                 'tiene.',
                 'El punto del tamano se gana con una frase que reconozca que en un sistema '
                 'academico pequeno los beneficios son limitados y el costo operativo es real. '
                 'Una respuesta que concluya «para este tamano conviene un monolito modular» esta '
                 'CORRECTA y se lleva el punto: es la decision que el taller de la Clase 4 pide '
                 'tomar con criterios de equipo y acoplamiento, y no hay una respuesta unica.',
             ],
             'errores': [
                 'Listar cuatro cosas sin distinguir cuales son beneficios y cuales retos: se '
                 'califica lo que este correctamente clasificado, no la cantidad.',
                 '«Los microservicios son mas rapidos»: no lo son por si mismos. Agregan saltos '
                 'de red. Lo que mejora es escalar la parte que lo necesita. No es un beneficio '
                 'valido tal como esta escrito.',
                 'Repetir el mismo reto con dos nombres (por ejemplo «latencia» y «lentitud de la '
                 'red») cuenta como uno: 3 puntos, no 6.',
             ],
             'tipo': 'desarrollo'}],
  'pts': 25,
  'titulo': 'SECCIÓN C — Desarrollo'},
 {'intro': '',
  'items': [{'enunciado': 'Diseñe una arquitectura cloud inicial para un sistema de gestión de '
                          'laboratorios con módulos: autenticación, reservas y notificaciones.',
             'id': 'D1',
             'lineas': 9,
             'pts': 35,
             'requerimientos': ['a) Elija IaaS/PaaS/SaaS (o híbrido) por componente y justifique '
                                '(10 pts)',
                                'b) Indique si usaría VM, contenedores o ambos (10 pts)',
                                'c) Proponga 3 servicios/microservicios y 2 riesgos distribuidos '
                                '(15 pts)'],
             'solucion': [
                 'Desglose: a) 10 = 3 por componente bien asignado + 1 por la justificacion mas '
                 'clara · b) 10 = 6 por la eleccion con criterio + 4 por decir con que se compara '
                 '· c) 15 = 3 x 3 servicios + 3 x 2 riesgos. Total 35. No hay una sola '
                 'arquitectura correcta: se califica la JUSTIFICACION, no la coincidencia con esta '
                 'propuesta.',
                 'a) Referencia: autenticacion en PaaS o como identidad gestionada (es el problema '
                 'ya resuelto por otros, y equivocarse aqui cuesta caro); reservas en PaaS, porque '
                 'es la logica propia del negocio y es lo unico que hay que escribir; '
                 'notificaciones por correo en SaaS, porque nadie deberia operar un servidor de '
                 'correo para un sistema de laboratorios. Tambien es correcto poner reservas en '
                 'IaaS si el estudiante justifica una necesidad de control del SO. Los 3 puntos de '
                 'cada componente se dan por el PAR (modelo + razon): un modelo sin razon vale 1.',
                 'b) Referencia: contenedores para autenticacion y reservas, porque arrancan en '
                 'segundos, se replican por instancia y el mismo empaquetado corre en el portatil '
                 'y en el servidor; VM solo si aparece una razon real (otro sistema operativo, un '
                 'aislamiento exigido, software heredado). Los 4 puntos del contraste piden decir '
                 'contra QUE se decide: «contenedores porque comparten el kernel y no arrastran un '
                 'SO completo como la VM» los gana; «uso contenedores porque es lo moderno» no.',
                 'c) Referencia: los tres servicios naturales son identidad, reservas y '
                 'notificaciones; un cuarto (por ejemplo un worker de envios) solo se justifica si '
                 'el estudiante dice por que —«el correo tarda y no debe bloquear la reserva»—, y '
                 'ese es el criterio con el que se armo el diagrama C4 de la Clase 4.',
                 'c) Los 2 riesgos distribuidos son los de la diapositiva «Distribuido implica '
                 'fallos» de la Clase 4: la llamada entre servicios puede TARDAR (el usuario '
                 'espera por una red, no por un metodo), puede PERDERSE (la reserva quedo '
                 'guardada y el correo nunca salio: dos verdades distintas al mismo tiempo) y '
                 'puede llegar DOS VECES (el mismo correo enviado dos veces, o la misma reserva '
                 'creada dos veces si la operacion no es idempotente). Tambien se acepta «no puedo '
                 'saber que paso leyendo un solo registro». Cada riesgo vale 3 puntos: 2 por '
                 'nombrarlo y 1 por decir que se hace con el (reintento, cola, idempotencia, '
                 'trazas correlacionadas).',
             ],
             'errores': [
                 'Riesgos de seguridad —manejo de secretos, cifrado, control de acceso— NO se '
                 'piden aqui y no otorgan los 3 puntos del riesgo: el enunciado dice «riesgos '
                 'distribuidos», y la seguridad en la nube es el tema de la Clase 6, posterior a '
                 'este corte. Si el estudiante nombra uno, se le reconoce por escrito pero se '
                 'califica el riesgo distribuido que falto.',
                 'Poner los tres componentes en un solo modelo («todo PaaS», «todo IaaS») sin '
                 'distinguir: 4 de 10 en a). El ejercicio es de reparto por componente.',
                 '«Notificaciones en IaaS montando un servidor de correo propio»: es tecnicamente '
                 'posible, pero contradice el criterio de la Clase 2 (no operar lo que ya se '
                 'consume resuelto). 1 de 3 en ese componente salvo justificacion excepcional.',
                 'Listar servicios que son capas y no servicios («frontend, backend, base de '
                 'datos»): no son los 3 servicios que pide c). 3 de 9 si acierta uno.',
                 'Confundir el riesgo con su solucion («riesgo: usar una cola»): la cola es la '
                 'respuesta, no el riesgo. 1 de 3.',
                 'Una respuesta que elija monolito modular en b) y sostenga la eleccion con el '
                 'tamano del equipo puede llevarse los 10 puntos de b), pero c) sigue pidiendo los '
                 '3 servicios y los 2 riesgos: se responden como diseno objetivo, y no se '
                 'descuenta la incoherencia si el estudiante la declara.',
             ],
             'tipo': 'practica'}],
  'pts': 35,
  'titulo': 'SECCIÓN D — Caso de diseño'}],
}

ARQ_P2 = {
    "meta": _meta(
        curso_dir='Arquitectura de Sistemas Computacionales',
        asignatura='Arquitectura de Sistemas Computacionales',
        codigo='FI303380',
        grupo='6303C',
        periodo='2026-2',
        horario='Lunes 10:00 – 12:00',
        n=2,
        corte=2,
        valor_corte='10% del Corte 2 (30%)',
        fecha='19/10/2026',
        clase=9,  # Sesion 9 del calendario (material: Clase 9 = dia del parcial)
        tiempo='90–100 minutos',
        titulo_parcial='Parcial 2 — Seguridad, redes, monitoreo, CI/CD y costos',
        secciones_resumen=['A. Selección múltiple — 20 pts',
 'B. Verdadero / Falso — 20 pts',
 'C. Seguridad y operaciones — 25 pts',
 'D. Caso CI/CD, monitoreo y costos — 35 pts'],
        archivo='Parcial 2 - Seguridad redes monitoreo y CI-CD',
        cobertura=('Corte 2 (Sesiones 6-9) · Únicamente clases dictadas antes del 19/10/2026 '
 '(Clases 6, 7, 8 y 10 del material; la sesión doble del 05/10 cubrió las Clases 7 y 8 y la '
 'sesión autónoma del 12/10 fue la Clase 10). La Clase 9 es la sesión del parcial:'),
        temas=[
            _tema(6, '28/09', 'Seguridad en la nube'),
            _tema(7, '05/10', 'Redes y almacenamiento cloud (sesión doble)'),
            _tema(8, '05/10', 'Monitoreo y optimización · Integración continua y despliegue (CI/CD) (sesión doble)'),
            _tema(10, '12/10', 'Costos y sostenibilidad cloud (sesión autónoma)'),
        ],
    ),
    "secciones": [{'intro': '',
  'items': [{'clave': 'b',
             'id': 'A1',
             'opciones': ['a) Que el proveedor hace todo y el cliente nada',
                          'b) Que proveedor y cliente dividen responsabilidades de seguridad según '
                          'el servicio',
                          'c) Que no hay cifrado posible',
                          'd) Que las redes públicas no existen'],
             'pregunta': 'El modelo de responsabilidad compartida en cloud implica:',
             'pts': 4,
             'tipo': 'mcq'},
            {'clave': 'b',
             'id': 'A2',
             'opciones': ['a) Solo registros DNS',
                          'b) Almacenar objetos/archivos escalables (backups, media, logs)',
                          'c) Reemplazar CPU',
                          'd) Ejecutar el navegador web'],
             'pregunta': 'Object storage (p. ej. buckets) se usa típicamente para:',
             'pts': 4,
             'tipo': 'mcq'},
            {'clave': 'a',
             'id': 'A3',
             'opciones': ['a) Integrar cambios con frecuencia y validarlos con builds/pruebas '
                          'automáticas',
                          'b) Evitar cualquier repositorio',
                          'c) Desplegar a producción sin pruebas siempre',
                          'd) Eliminar el monitoreo'],
             'pregunta': 'CI (Integración Continua) busca principalmente:',
             'pts': 4,
             'tipo': 'mcq'},
            {'clave': 'a',
             'id': 'A4',
             'opciones': ['a) Latencia, tasa de error y uso de CPU/memoria',
                          'b) Solo el color del logo',
                          'c) El número de diapositivas del proyecto',
                          'd) La versión de Word del docente'],
             'pregunta': 'Una métrica útil de monitoreo de un servicio cloud es:',
             'pts': 4,
             'tipo': 'mcq'},
            {'clave': 'b',
             'id': 'A5',
             'nota': 'Clase 10 — Costos: right-sizing busca una utilización sostenida del 40-70 %; '
                     'por debajo se paga capacidad ociosa, por encima no queda margen de picos.',
             'opciones': ['a) Mantenerla por debajo del 10 % para tener margen',
                          'b) Entre 40 % y 70 % de utilización sostenida',
                          'c) Al 100 % de forma permanente',
                          'd) La utilización no se tiene en cuenta al dimensionar'],
             'pregunta': 'La instancia de la API de CloudLite lleva semanas al 8 % de CPU. Al hacer '
                         'right-sizing, ¿cuál es la banda de utilización objetivo recomendada?',
             'pts': 4,
             'tipo': 'mcq'}],
  'pts': 20,
  'titulo': 'SECCIÓN A — Selección múltiple'},
 {'intro': '',
  'items': [{'clave': 'V',
             'enunciado': 'Exponer puertos innecesarios en un grupo de seguridad/firewall aumenta '
                          'la superficie de ataque.',
             'id': 'B1',
             'justificacion': 'Principio de mínimo acceso de red.',
             'pts': 4,
             'tipo': 'vf'},
            {'clave': 'V',
             'enunciado': 'CD (Continuous Delivery/Deployment) automatiza la ruta hacia entornos '
                          '(con controles) tras CI.',
             'id': 'B2',
             'justificacion': 'Pipeline de entrega.',
             'pts': 4,
             'tipo': 'vf'},
            {'clave': 'F',
             'enunciado': 'El monitoreo solo sirve después de un incidente grave, no de forma '
                          'continua.',
             'id': 'B3',
             'justificacion': 'Monitoreo proactivo y alertas.',
             'pts': 4,
             'tipo': 'vf'},
            {'clave': 'V',
             'enunciado': 'VPC/redes virtuales permiten aislar recursos y controlar tráfico entre '
                          'subredes.',
             'id': 'B4',
             'justificacion': 'Aislamiento de red cloud.',
             'pts': 4,
             'tipo': 'vf'},
            {'clave': 'V',
             'enunciado': 'Apagar por horario los entornos de desarrollo y pruebas de CloudLite '
                          'fuera de la jornada laboral reduce el costo mensual sin afectar la '
                          'disponibilidad de producción.',
             'id': 'B5',
             'justificacion': 'Clase 10 — Costos: los entornos no productivos no necesitan estar '
                              'encendidos 24/7; apagarlos ~12 h diarias y fines de semana recorta '
                              'buena parte de su factura de cómputo.',
             'pts': 4,
             'tipo': 'vf'}],
  'pts': 20,
  'titulo': 'SECCIÓN B — Verdadero / Falso'},
 {'intro': '',
  'items': [{'enunciado': 'Liste 4 controles de seguridad cloud aplicables a un API desplegada en '
                          'la nube (identidad, red, secretos, logs).',
             'id': 'C1',
             'lineas': 4,
             'pts': 12,
             'solucion': ['IAM/roles; TLS; secret manager; WAF/SG; logging/auditoría.',
                          '3 pts por control válido (máx 12).'],
             'tipo': 'desarrollo'},
            {'enunciado': 'Explique la diferencia entre almacenamiento de bloques, archivos y '
                          'objetos con un ejemplo de uso cloud para cada uno.',
             'id': 'C2',
             'lineas': 5,
             'pts': 13,
             'solucion': ['Block: discos de VM; File: NFS compartido; Object: backups/media en '
                          'bucket.'],
             'tipo': 'desarrollo'}],
  'pts': 25,
  'titulo': 'SECCIÓN C — Seguridad y operaciones'},
 {'intro': '',
  'items': [{'enunciado': 'Diseñe un pipeline CI/CD sencillo (etapas) para el servicio '
                          'containerizado de CloudLite y defina 3 alertas de monitoreo '
                          'post-despliegue.',
             'id': 'D1',
             'lineas': 8,
             'pts': 25,
             'requerimientos': ['a) Etapas del pipeline (build, test, scan, deploy…) (10 pts)',
                                'b) Entornos (dev/staging/prod) y criterio de promoción (8 pts)',
                                'c) 3 alertas con umbral o condición (7 pts)'],
             'solucion': ['CI: lint/test/build image; CD: staging→prod con aprobación; alertas: '
                          '5xx, latencia p95, CPU.'],
             'tipo': 'practica'},
            {'enunciado': 'Costos y sostenibilidad de CloudLite (Clase 10): la factura mensual '
                          'subió y el equipo detecta 3 instancias al 8 % de CPU encendidas 24/7, '
                          'una imagen de contenedor de 1,2 GB y logs guardados sin límite de '
                          'retención.',
             'id': 'D2',
             'lineas': 6,
             'pts': 10,
             'requerimientos': ['a) Proponga 3 medidas concretas de reducción de costo para este '
                                'escenario e indique qué componente de la factura ataca cada una '
                                '(6 pts)',
                                'b) Explique por qué el costo se trata como atributo de calidad de '
                                'la arquitectura y qué otro atributo puede sacrificarse al '
                                'recortar (4 pts)'],
             'solucion': ['2 pts por medida válida y bien atribuida: right-sizing de las 3 '
                          'instancias a una banda de 40-70 % de utilización (cómputo); apagado por '
                          'horario de los entornos no productivos (cómputo); adelgazar la imagen '
                          'con multi-stage / base slim (almacenamiento de registro y tiempo de '
                          'despliegue); política de retención y archivado de logs a '
                          'almacenamiento frío (almacenamiento e ingesta de observabilidad).',
                          'El costo condiciona el diseño igual que rendimiento o disponibilidad: '
                          'es un requisito no funcional medible (TCO, costo por transacción) y '
                          'nube vs on-premise se compara por TCO, no por precio de lista. Al '
                          'recortar se sacrifica típicamente disponibilidad/redundancia o margen '
                          'de rendimiento ante picos; se acepta también observabilidad si se '
                          'justifica el trade-off.'],
             'tipo': 'practica'}],
  'pts': 35,
  'titulo': 'SECCIÓN D — Caso CI/CD, monitoreo y costos'}],
}

ARQ_P3 = {
    "meta": _meta(
        curso_dir='Arquitectura de Sistemas Computacionales',
        asignatura='Arquitectura de Sistemas Computacionales',
        codigo='FI303380',
        grupo='6303C',
        periodo='2026-2',
        horario='Lunes 10:00 – 12:00',
        n=3,
        corte=3,
        valor_corte='15% del Corte 3 (40%)',
        fecha='09/11/2026',
        clase=12,  # Sesion 12 del calendario (material: Clase 14 = dia del parcial)
        tiempo='90–100 minutos',
        titulo_parcial='Parcial 3 — Rendimiento, escalabilidad y cierre de proyecto',
        secciones_resumen=['A. Selección múltiple — 20 pts',
 'B. Emparejamiento — 20 pts',
 'C. Rendimiento y escalabilidad — 25 pts',
 'D. Caso de sustentación arquitectónica — 35 pts'],
        archivo='Parcial 3 - Rendimiento escalabilidad y cierre de proyecto',
        cobertura=('Corte 3 (Sesiones 10-13) · Únicamente clases dictadas antes del 09/11/2026 '
 '(Clases 11, 12 y 13 del material; la sesión doble del 26/10 cubrió las Clases 11 y 12 y la '
 'sesión autónoma del 02/11 fue la Clase 13). La Clase 14 es la sesión del parcial y la Clase 15 '
 '(16/11) es la sustentación del Proyecto Integrador, posterior:'),
        temas=[
            _tema(11, '26/10', 'Avance del proyecto final (sesión doble)'),
            _tema(12, '26/10', 'Pruebas de rendimiento · Preparación de presentación final (sesión doble)'),
            _tema(13, '02/11', 'Escalabilidad automática (sesión autónoma)'),
        ],
    ),
    "secciones": [{'intro': '',
  'items': [{'clave': 'a',
             'id': 'A1',
             'opciones': ['a) Evaluar el comportamiento bajo una carga esperada/concurrencia '
                          'definida',
                          'b) Solo revisar ortografía del README',
                          'c) Eliminar logs',
                          'd) Cambiar el color de la UI'],
             'pregunta': 'Una prueba de carga (load test) busca:',
             'pts': 5,
             'tipo': 'mcq'},
            {'clave': 'b',
             'id': 'A2',
             'opciones': ['a) Aumentar CPU de una sola máquina únicamente',
                          'b) Añadir más instancias/nodos para repartir carga',
                          'c) Reducir usuarios a la fuerza',
                          'd) Apagar el balanceador siempre'],
             'pregunta': 'Escalabilidad horizontal significa típicamente:',
             'pts': 5,
             'tipo': 'mcq'},
            {'clave': 'a',
             'id': 'A3',
             'opciones': ['a) Métricas (CPU, RPS, latencia) según políticas',
                          'b) La fase lunar',
                          'c) El número de diapositivas',
                          'd) Un único valor fijo imposible de cambiar'],
             'pregunta': 'El autoescalado (autoscaling) reacciona generalmente a:',
             'pts': 5,
             'tipo': 'mcq'},
            {'clave': 'a',
             'id': 'A4',
             'opciones': ['a) Diagrama de arquitectura, decisiones, evidencia de pruebas y '
                          'trade-offs',
                          'b) Solo el código ofuscado',
                          'c) Ningún diagrama',
                          'd) Credenciales de producción en la lámina'],
             'pregunta': 'En la preparación de la presentación final arquitectónica conviene '
                         'incluir:',
             'pts': 5,
             'tipo': 'mcq'}],
  'pts': 20,
  'titulo': 'SECCIÓN A — Selección múltiple'},
 {'intro': '',
  'items': [{'clave': '1-a, 2-b, 3-c, 4-d',
             'col_a': ['1) Stress test',
                       '2) Spike test',
                       '3) Escalabilidad vertical',
                       '4) Balanceador de carga'],
             'col_b': ['a) Empuja el sistema más allá de la capacidad normal para hallar límites',
                       'b) Evalúa picos súbitos de tráfico',
                       'c) Aumentar recursos de un mismo nodo (más CPU/RAM)',
                       'd) Distribuye peticiones entre instancias'],
             'id': 'B1',
             'instruccion': 'Empareje tipo de prueba/escalado con su definición.',
             'pts': 20,
             'tipo': 'match'}],
  'pts': 20,
  'titulo': 'SECCIÓN B — Emparejamiento'},
 {'intro': '',
  'items': [{'enunciado': 'Defina 3 métricas de rendimiento que mediría en su API y un umbral de '
                          'aceptación ejemplo para cada una.',
             'id': 'C1',
             'lineas': 4,
             'pts': 12,
             'solucion': ['p95 latencia, error rate, throughput; umbrales realistas justificados.'],
             'tipo': 'desarrollo'},
            {'enunciado': 'Explique cuándo preferiría escalado vertical vs horizontal y un límite '
                          'de cada enfoque.',
             'id': 'C2',
             'lineas': 4,
             'pts': 13,
             'solucion': ['Vertical: simple hasta techo de máquina; horizontal: más nodos, '
                          'necesita stateless/balanceo.'],
             'tipo': 'desarrollo'}],
  'pts': 25,
  'titulo': 'SECCIÓN C — Rendimiento y escalabilidad'},
 {'intro': '',
  'items': [{'enunciado': 'Elabore el guion de sustentación de su proyecto de Arquitectura '
                          '(enfoque cloud):',
             'id': 'D1',
             'lineas': 10,
             'pts': 35,
             'requerimientos': ['a) Contexto y objetivos (5 pts)',
                                'b) Diagrama lógico (describa capas/servicios) (10 pts)',
                                'c) Estrategia de pruebas de rendimiento (10 pts)',
                                'd) Política de escalado automático propuesta (5 pts)',
                                'e) Riesgos, limitaciones o trabajo futuro del avance (5 pts)'],
             'solucion': ['Coherencia arquitectura-pruebas-escalado; trade-offs claros; sin '
                          'secretos en láminas.'],
             'tipo': 'practica'}],
  'pts': 35,
  'titulo': 'SECCIÓN D — Caso de sustentación'}],
}

TODOS = [
    PROG2_P1,
    PROG2_P2,
    PROG2_P3,
    SEM_P1,
    SEM_P2,
    SEM_P3,
    BD2_P1,
    BD2_P2,
    BD2_P3,
    ARQ_P1,
    ARQ_P2,
    ARQ_P3,
]
