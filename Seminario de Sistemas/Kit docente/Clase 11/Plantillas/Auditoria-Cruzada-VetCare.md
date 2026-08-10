# Auditoria cruzada del paquete de diseño - VetCare (Clinica Huellitas)

> Hoy no se agrega tema nuevo. Se verifica que requisitos, casos de uso, clases y mockups describan el MISMO sistema y usen los MISMOS nombres.

## 1. Matriz de trazabilidad

Regla: toda fila debe estar completa. Fila incompleta = hallazgo.

| RF | Caso de uso | Clases implicadas | Mockup | Estado |
|---|---|---|---|---|
| RF-02 | CU-00 Registrar propietario | Propietario | M-01 | |
| RF-03, RF-04 | CU-01 Registrar mascota | Mascota, Propietario | M-02 | |
| RF-05 | CU-02 Buscar expediente | Mascota, Consulta | M-03 | |
| RF-06 | CU-03 Registrar consulta medica | Consulta, Veterinario | M-05 | |
| RF-07 | | | | |
| RF-08 | CU-04 Agendar cita | Cita, Veterinario | M-04 | |
| RF-09 | CU-05 Consultar indicadores | Consulta, Veterinario | M-06 | |

- HUERFANO: requisito que no llega a ningun caso de uso ni clase.
- VIUDO: caso de uso o clase que no nace de ningun requisito.

## 2. Glosario de nombres canonicos

| Nombre canonico | Definicion en una linea | Sinonimos prohibidos |
|---|---|---|
| Propietario | Persona responsable de una o mas mascotas ante la clinica | Dueño, Cliente, Responsable |
| Mascota | Animal atendido en la clinica, identificado con codigo unico | Paciente, Animalito |
| Cita | Reserva de un horario con un veterinario para una fecha futura | Turno, Agendamiento |
| Consulta | Registro de una atencion medica ya realizada | Visita, Atencion |
| Expediente | Vista consolidada de ficha, consultas y vacunas de una mascota (NO es una clase) | Historia, Carpeta |
| Veterinario | Profesional que atiende consultas y firma el registro clinico | Doctor, Medico |
| Vacuna | Aplicacion registrada de un biologico con fecha y refuerzo | Inyeccion |
| Bitacora | Registro de quien hizo que y cuando dentro del sistema | Log, Auditoria |

## 3. Rubrica de revision entre pares (20 minutos por paquete)

Roles: el AUTOR permanece en silencio, el REVISOR recorre la rubrica, el MODERADOR toma el tiempo y escribe.
Prohibido proponer soluciones durante la revision: solo se reportan hechos.

| # | Punto a verificar | Cumple | Observacion |
|---|---|---|---|
| 1 | Todo RF llega a un caso de uso y a una clase | | |
| 2 | Todo caso de uso nace de al menos un RF | | |
| 3 | Los nombres coinciden con el glosario canonico | | |
| 4 | Cada caso de uso tiene pre, post y minimo dos alternos | | |
| 5 | El diagrama de clases tiene multiplicidades en todas las asociaciones | | |
| 6 | Los mockups muestran los campos que exige la especificacion | | |

## 4. Acta de hallazgos

Severidad: BLOQUEANTE (impide construir) / MAYOR (obliga a rehacer un artefacto) / MENOR (cosmetico).

| ID | Ubicacion exacta | Descripcion objetiva del hallazgo | Severidad | Decision |
|---|---|---|---|---|
| H-01 | Diagrama de clases, clase Consulta | No existe relacion con Veterinario y CU-03 exige registrar quien atendio | Mayor | Aceptado / Rechazado / Aplazado |
| H-02 | Matriz de trazabilidad, fila de CU-04 | El caso de uso aparece sin RF de origen pese a que existe RF-08 | Mayor | |
| H-03 | Diagrama de clases, clase Mascota | Guarda dueño como atributo de texto en vez de asociarse con Propietario | Bloqueante | |

## 5. Backlog de deuda de diseño

| Prioridad | Item | Responsable | Criterio de cierre verificable |
|---|---|---|---|
| 1 | H-03 | Modelo estatico | Existe asociacion Propietario 1..* Mascota con multiplicidad y el atributo texto fue eliminado |
| 2 | H-01 | Modelo estatico | Existe asociacion Consulta - Veterinario con multiplicidad dibujada |
| 3 | H-02 | Requisitos | La fila de CU-04 en la matriz queda ligada a RF-08 |

## 6. Definicion de terminado del paquete VetCare

- [ ] Catalogo de RF y RNF numerado, sin huerfanos.
- [ ] Diagrama de casos de uso con limite de sistema y actores como roles.
- [ ] Especificacion textual de los casos de uso criticos con flujos alternos.
- [ ] Diagrama de clases con atributos, operaciones y multiplicidades.
- [ ] Mockups de las pantallas criticas coherentes con las especificaciones.
- [ ] Diccionario de datos alineado con los nombres canonicos.
- [ ] Matriz de trazabilidad completa y acta de revision firmada por el equipo revisor.
