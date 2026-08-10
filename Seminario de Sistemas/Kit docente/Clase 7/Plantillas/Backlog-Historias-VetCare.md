# VetCare - Backlog inicial de historias de usuario

Proyecto Integrador: Clinica Veterinaria Huellitas.
Asignatura: Seminario de Sistemas. Entrega: ExamLab.

---

## 1. Epicas

| ID | Epica | Objetivo en una linea | RF que agrupa |
|---|---|---|---|
| E-01 | Gestion de pacientes | Que ninguna ficha se pierda y cada mascota tenga un dueno identificado | RF-01, RF-02 |
| E-02 | Historial y agenda | Que el historial se consulte en segundos y la agenda no dependa del veterinario | RF-03 a RF-08 |

---

## 2. Plantilla de historia (copie una por cada HU)

**HU-00**  [Epica: ]

Como <rol concreto de Huellitas: auxiliar / veterinario / administrador>
quiero <accion que hace esa persona>
para <beneficio real para la clinica>.

**Criterios de aceptacion**

- CA-1  Dado <contexto>, cuando <accion>, entonces <resultado observable>.
- CA-2  Dado <contexto>, cuando <accion>, entonces <resultado observable>.
- CA-3  (camino alterno o error) Dado <contexto>, cuando <accion>, entonces <resultado observable>.

**Estimacion:** ___ puntos  |  **Prioridad:** Must/Should/Could  |  **Origen:** RF-__

---

## 3. Ejemplo resuelto

**HU-04**  [Epica: E-02]

Como veterinario de la clinica Huellitas
quiero consultar el historial de atenciones de una mascota por el documento del dueno
para decidir el tratamiento sin depender de la carpeta fisica.

- CA-1  Dado un dueno con 3 mascotas registradas, cuando busco por su documento, entonces el sistema lista las 3 mascotas con nombre y especie.
- CA-2  Dado que selecciono la mascota Rocky, cuando abro su historial, entonces veo sus atenciones de la mas reciente a la mas antigua.
- CA-3  Dado un documento no registrado, cuando busco, entonces el sistema muestra 'No hay duenos con ese documento' y ofrece crear uno.

**Estimacion:** 5 puntos  |  **Prioridad:** Must  |  **Origen:** RF-03

---

## 4. Tablero del backlog

| ID | Epica | Historia (resumen) | Puntos | Prioridad | RF origen | INVEST ok |
|---|---|---|---|---|---|---|
| HU-01 | E-01 | Registrar dueno | 3 | Must | RF-01 | si |
| HU-02 | | | | | | |
| HU-03 | | | | | | |
| HU-04 | E-02 | Consultar historial | 5 | Must | RF-03 | si |
| HU-05 | | | | | | |
| HU-06 | | | | | | |
| HU-07 | | | | | | |
| HU-08 | | | | | | |

---

## 5. Chequeo INVEST (marque si / no por historia)

| Letra | Pregunta de control |
|---|---|
| I - Independiente | Se puede entregar sin esperar otra historia? |
| N - Negociable | Describe la necesidad y no la solucion tecnica? |
| V - Valiosa | Alguien de Huellitas gana algo concreto? |
| E - Estimable | El equipo entiende lo suficiente para tallarla? |
| S - Pequena | Cabe en una iteracion (8 puntos o menos)? |
| T - Testeable | Tiene criterios verificables con si/no? |

---

## 6. Escala de estimacion

Referencia: **registrar un dueno = 3 puntos**.
Escala permitida: 1, 2, 3, 5, 8. Todo lo que llegue a 13 se parte.

---

## 7. Checklist antes de subir a ExamLab

- [ ] 8 historias, ninguna con el rol 'usuario'.
- [ ] Ningun 'para' repite la accion.
- [ ] Minimo 2 criterios por historia y 4 historias con camino alterno.
- [ ] Cortes verticales (nada de pantalla / logica / base de datos por separado).
- [ ] Todas estimadas y ordenadas por prioridad.
- [ ] Archivo: Backlog-VetCare-<apellidos>.pdf
