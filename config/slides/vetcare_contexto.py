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
- **Huellitas** es la clinica: el CLIENTE, quien tiene el problema.
- **VetCare** es el sistema que se le construye. En BD II, **VetCare DB** es
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
    "Se **extravían fichas** de pacientes: el expediente existe en un solo papel.",
    "Buscar un historial en el archivo físico **genera filas** en la sala de espera.",
    "**No hay métricas**: no saben cuántas especies atienden al mes.",
]

#: Los tres interesados y lo que espera cada uno. Texto reusado del guion de
#: Seminario, donde ya estaba redactado: sirve para que el estudiante entienda que
#: los intereses ENTRAN EN CONFLICTO y por eso hay decisiones de diseno que tomar.
INTERESADOS = [
    "**Dueño de la clínica:** quiere métricas del negocio.",
    "**Recepcionista:** quiere agendar rápido y con pocos clics.",
    "**Veterinario:** quiere el historial del paciente a la mano durante la consulta.",
]

#: Frontera de cada asignatura sobre el mismo cliente, para que el estudiante no
#: crea que tiene que construir el sistema entero.
ALCANCE_POR_CURSO = {
    "bd2": "En **Bases de Datos II** usted construye la **capa de datos** de VetCare: "
           "el modelo, la integridad, la seguridad y el rendimiento. No se le pide la "
           "aplicación ni la interfaz.",
    "prog2": "En **Programación II** usted construye la **aplicación Java** de VetCare.",
    "seminario": "En **Seminario de Sistemas** usted diseña los **planos** de VetCare: "
                 "requisitos, UML y wireframes.",
}
