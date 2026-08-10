# VetCare - Catalogo de requisitos (plantilla de trabajo)

Proyecto Integrador: sistema VetCare para la Clinica Veterinaria Huellitas.
Asignatura: Seminario de Sistemas. Entrega: ExamLab, formato PDF.

---

## 1. Fuente de la elicitacion

Entrevista al Dr. Ramirez, medico veterinario y dueno de la clinica Huellitas.
Frases crudas registradas (necesidades, NO requisitos):

| ID | Frase textual del cliente | Dolor que revela |
|---|---|---|
| NEC-01 | 'Necesito que las fichas no se me pierdan mas.' | Extravio de fichas |
| NEC-02 | 'Cuando llega un perro quiero ver de una lo que le hemos hecho antes.' | Busqueda lenta del historial |
| NEC-03 | 'Que la auxiliar pueda agendar sin llamarme a mi.' | Cuello de botella en agenda |
| NEC-04 | 'El sistema tiene que ser rapido, aqui no hay tiempo de esperar.' | Desempeno (sin cuantificar) |
| NEC-05 | 'Quiero saber cuantas consultas hicimos en el mes.' | Ausencia de metricas |

---

## 2. Ficha de requisito funcional (copie una por cada RF)

| Campo | Contenido |
|---|---|
| ID | RF-00 |
| Nombre | |
| Actor | |
| Descripcion | El sistema debe permitir a <actor> <accion> <objeto> [bajo <condicion>] |
| Entrada | |
| Salida | |
| Regla de negocio | |
| Criterio de verificacion | (debe tener un numero o un si/no) |
| Prioridad MoSCoW | Must / Should / Could / Won't |
| Origen | NEC-00, frase del cliente |
| Estado | propuesto / aprobado / descartado |

---

## 3. Catalogo de requisitos funcionales

| ID | Requisito (plantilla) | Actor | MoSCoW | Verificacion |
|---|---|---|---|---|
| RF-01 | El sistema debe permitir registrar un dueno con documento, nombre, telefono y direccion | Auxiliar | Must | Se crea el dueno y el documento no se puede repetir |
| RF-02 | | | | |
| RF-03 | | | | |
| RF-04 | | | | |
| RF-05 | | | | |
| RF-06 | | | | |
| RF-07 | | | | |
| RF-08 | | | | |

---

## 4. Catalogo de requisitos no funcionales

| ID | Categoria | Requisito CUANTIFICADO | Como se mide |
|---|---|---|---|
| RNF-01 | Desempeno | La consulta de historial responde en maximo 3 s con 5.000 fichas y 10 usuarios concurrentes | Cronometro sobre base de prueba |
| RNF-02 | Control de acceso | | |
| RNF-03 | Usabilidad | | |
| RNF-04 | Respaldo | | |

---

## 5. Matriz de trazabilidad

| Necesidad | Requisito | Pantalla prevista | Prueba de aceptacion |
|---|---|---|---|
| NEC-02 | RF-03 | P-02 Historial de mascota | PR-07 cronometrar busqueda |
| | | | |
| | | | |

---

## 6. Lista negra de palabras (si aparecen, el requisito se devuelve)

rapido, amigable, facil, intuitivo, robusto, moderno, optimo, eficiente, seguro (sin metrica), sencillo, agil, de ultima tecnologia.

---

## 7. Checklist antes de subir a ExamLab

- [ ] Hay minimo 8 RF y 4 RNF.
- [ ] Ningun RF tiene una 'y' uniendo dos capacidades distintas.
- [ ] Todos los RNF tienen por lo menos un numero.
- [ ] Los Must no superan el 60% de la lista.
- [ ] Los Won't estan escritos y justificados (protegen el alcance).
- [ ] Cada necesidad NEC-01 a NEC-05 aparece al menos una vez en la matriz.
- [ ] El archivo se llama RF-RNF-VetCare-<apellidos>.pdf
