# -*- coding: utf-8 -*-
"""Cliente ficticio del hilo VetCare: la Clinica Veterinaria «Huellitas».

Por que existe
--------------
La descripcion del cliente vivia dentro de `build_uniajc_pi_2026_2.py`, y por eso
solo la usaban los enunciados de Programacion II y Seminario. Bases de Datos II
tenia su propio parrafo generico («una clinica veterinaria necesita gestionar
mascotas, duenos...») que no nombraba al cliente ni decia cual era su problema.
El resultado medible: «Huellitas» aparecia 16 veces en lo que el estudiante de
BD II lee DENTRO de ExamLab, repartidas en 10 de las 15 clases, y una sola vez en
todo el material que recibe antes de abrir la plataforma. Conocia al cliente en el
momento en que se le calificaba.

Este modulo es la fuente unica. Lo consumen el generador del PI de los cuatro
cursos y, en BD II, la Presentacion del Curso y el material de la Clase 1.

Nomenclatura (importa mantenerla)
---------------------------------
- @@Huellitas@@ es la clinica: el CLIENTE, quien tiene el problema.
- @@VetCare@@ es el sistema que se le construye. En BD II, @@VetCare DB@@ es
  concretamente la base de datos de ese sistema.
Decir «la clinica VetCare» mezcla las dos cosas y es lo que hacia que el material
de BD II contradijera a ExamLab, a Prog II y a Seminario.
"""
from __future__ import annotations

#: El cliente, tal como se nombra en todo el material.
CLIENTE = "Clínica Veterinaria «Huellitas»"

#: Regla de nomenclatura, para pegar donde haga falta desambiguar.
NOMENCLATURA = (
    "Huellitas es la clínica (el cliente); VetCare DB es la base de datos que "
    "usted construye para ella."
)

#: Descripcion canonica del caso. Es el texto que ya usaban los enunciados de
#: Prog II y Seminario; se movio aqui sin cambiarlo para no desalinear los cursos.
CONTEXTO_VETCARE = (
    "La Clinica Veterinaria «Huellitas» atiende un alto volumen de pacientes y hoy lleva "
    "toda su gestion en carpetas de papel. La administracion reporta tres problemas: se "
    "extravian fichas de pacientes, buscar un historial en el archivo fisico genera filas "
    "en la sala de espera, y no hay metricas (no saben cuantas especies atienden al mes). "
    "Ustedes fueron contratados para resolverlo con un sistema llamado @@VetCare@@."
)

#: Los tres dolores, sueltos, para vinetas de diapositiva.
PROBLEMAS = [
    "Se @@extravían fichas@@ de pacientes: el expediente existe en un solo papel.",
    "Buscar un historial en el archivo físico @@genera filas@@ en la sala de espera.",
    "@@No hay métricas@@: no saben cuántas especies atienden al mes.",
]

#: Los tres interesados y lo que espera cada uno. Texto reusado del guion de
#: Seminario, donde ya estaba redactado: sirve para que el estudiante entienda que
#: los intereses ENTRAN EN CONFLICTO y por eso hay decisiones de diseno que tomar.
INTERESADOS = [
    "@@Dueño de la clínica:@@ quiere métricas del negocio.",
    "@@Recepcionista:@@ quiere agendar rápido y con pocos clics.",
    "@@Veterinario:@@ quiere el historial del paciente a la mano durante la consulta.",
]

#: Frontera de cada asignatura sobre el mismo cliente, para que el estudiante no
#: crea que tiene que construir el sistema entero.
ALCANCE_POR_CURSO = {
    "bd2": "En @@Bases de Datos II@@ usted construye la @@capa de datos@@ de VetCare: "
           "el modelo, la integridad, la seguridad y el rendimiento. No se le pide la "
           "aplicación ni la interfaz.",
    "prog2": "En @@Programación II@@ usted construye la @@aplicación Java@@ de VetCare.",
    "seminario": "En @@Seminario de Sistemas@@ usted diseña los @@planos@@ de VetCare: "
                 "requisitos, UML y wireframes.",
}


# ---------------------------------------------------------------------------
# Caso de estudio (anexo que el estudiante conserva todo el semestre)
# ---------------------------------------------------------------------------
# Por que existe: el cliente se presentaba en dos diapositivas y en un parrafo
# del enunciado, y a partir de ahi cada taller daba por sabidos datos que nunca
# se habian escrito juntos: las 8 entidades, las 3 reglas, el elenco de nombres y
# —sobre todo— la escala. Las Clases 6 y 7 evaluan indices sobre una base de
# 30.010 citas sin que en ningun sitio se dijera que la clinica opera a ese
# volumen. Este bloque es la fuente de esos datos y alimenta el anexo en
# `Clases/Proyecto Integrador/`.

PERFIL = [
    ("Ciudad", "Cali, Valle del Cauca"),
    ("Volumen de atención", "unas 150 citas por día"),
    ("Equipo clínico", "16 veterinarios entre General, Dermatología y Cirugía"),
    ("Pacientes registrados", "alrededor de 5.000 mascotas de unos 2.000 dueños"),
    ("Cómo opera hoy", "carpetas de papel en un archivo físico, sin sistema"),
]

#: Las 8 entidades en lenguaje de negocio. El estudiante las traduce a tablas;
#: aqui se describen por lo que significan para la clinica, no por su DDL.
ENTIDADES = [
    ("Dueño", "La persona que trae la mascota y a quien se le factura. Un dueño puede tener varias mascotas."),
    ("Mascota", "El paciente. Pertenece a un dueño y puede quedar inactiva sin que se borre su historial."),
    ("Veterinario", "Quien atiende. Tiene una especialidad y una agenda propia."),
    ("Cita", "Un espacio reservado: una mascota, un veterinario, una fecha y hora, y un estado."),
    ("Consulta", "Lo que ocurrió en una cita atendida: motivo, diagnóstico y tratamiento. No existe sin su cita."),
    ("Insumo", "Medicamentos y materiales, con precio y stock. Se descuentan al facturar."),
    ("Factura", "El cobro de una consulta, con su total."),
    ("Detalle de factura", "Cada línea de la factura: qué insumo, cuántas unidades y a qué precio se vendió ese día."),
]

#: Las tres reglas del negocio, con donde se hacen cumplir. El «donde» es lo que
#: conecta el caso con el temario: sin esto, cada clase parece un tema suelto.
REGLAS_NEGOCIO = [
    ("Una mascota inactiva no puede tener una cita nueva",
     "La clave foránea no la defiende: el identificador existe y el motor la acepta. "
     "Se resuelve con un procedimiento (Clase 3) y, si debe cumplirse aunque nadie lo llame, "
     "con un disparador (Clase 4)."),
    ("El stock de un insumo nunca queda negativo",
     "Facturar descuenta stock; si no alcanza, la factura no debe quedar a medias. "
     "Se resuelve con una transacción (Clase 8)."),
    ("Todo cambio sensible queda auditado",
     "Precios y cancelaciones de cita tienen que dejar rastro de quién y cuándo. "
     "Se resuelve con un disparador (Clase 4) y se apoya en los roles (Clase 2)."),
]

#: Como crece la base a lo largo del semestre. Es la conexion que faltaba entre
#: el arranque de la Clase 1 y el volumen que evaluan las Clases 6 y 7.
ESCALA = [
    ("Clase 1 — la primera semana",
     "6 dueños, 8 mascotas, 4 veterinarios y 10 citas. Alcanza para probar el modelo "
     "y ver un error de integridad en vivo."),
    ("Clases 6 y 7 — siete meses después",
     "2.006 dueños, 5.008 mascotas, 16 veterinarios y 30.010 citas entre el 05/01/2026 y "
     "el 23/07/2026. Es la misma clínica operando: por eso a esa altura la agenda del día "
     "ya no se puede consultar sin índices."),
    ("Clase 10 — el problema de dos recepcionistas",
     "Dos personas agendando al mismo tiempo pueden reservar el mismo veterinario en la "
     "misma franja. Con una fila no se ve; con 150 citas al día, sí."),
]

#: Elenco fijo. Existe para que los talleres, las soluciones y los enunciados de
#: ExamLab hablen de las mismas personas y no de ejemplos improvisados.
ELENCO = {
    "duenos": "Ana Gomez, Carlos Ruiz, Laura Restrepo, Luisa Cardona, Marcela Diaz, Paula Salazar",
    "mascotas": "Luna, Firulais, Rocky (inactiva), Toby, Mishi, Nube, Bobby, Kiara (inactiva)",
    "veterinarios": "Andres Vallejo, Diego Moreno, Ivan Ortiz, Jorge Pineda",
    # Literales SIN TILDE: es exactamente como estan sembrados en la base de
    # ExamLab, y el estudiante los usa en sus WHERE y sus INSERT.
    "especialidades": "General, Dermatologia, Cirugia",
    "servicios": "Revision, Desparasitacion",
}

#: Convenciones de datos del curso. Se repiten aqui porque son la causa numero uno
#: de que un script no corra a la primera en el PostgreSQL de ExamLab.
CONVENCIONES_DATOS = [
    "Identificadores en @@minúscula@@, sin tildes ni eñes y @@en singular@@: `dueno`, `mascota`, `cita`.",
    "Claves sustitutas con el patrón @@`id_<entidad>`@@, con el mismo nombre a los dos lados de la relación.",
    "Un teléfono @@no es un número@@: `VARCHAR(30)`. Una fecha no es texto: `TIMESTAMP`. El dinero no es flotante: `DECIMAL(12,2)`.",
    "Nada se borra: se marca inactivo con `activa CHAR(1) DEFAULT 'S' CHECK (activa IN ('S','N'))`.",
    "Palabras compuestas con guión bajo (`detalle_factura`, `fecha_hora`); nunca camelCase ni comillas dobles.",
]

FUERA_DE_ALCANCE = [
    "No hay pasarela de pagos ni cobro en línea.",
    "No hay aplicación de escritorio ni móvil: eso es Programación II sobre el mismo cliente.",
    "No se maneja nómina ni contabilidad de la clínica.",
    "No hay historia clínica con imágenes ni resultados de laboratorio adjuntos.",
]
