# ERS + Matriz en V - Proyecto Integrador VetCare
**Clinica Veterinaria Huellitas** | Enfoque tradicional (cascada / modelo en V)
Equipo: ______________  Version del documento: 1.0  Fecha: __________

---

## 1. Indice del ERS (estructura minima exigida)

1. Proposito y alcance (que entra y que NO entra)
2. Glosario del dominio veterinario
3. Requisitos funcionales (RF-01 ...)
4. Requisitos no funcionales (RNF-01 ...)
5. Reglas de negocio (RN-01 ...)
6. Matriz de trazabilidad requisito - diseno - prueba
7. Control de versiones y aprobaciones

---

## 2. Ficha de requisito (copie una por cada requisito)

```
ID: RF-__            Version: ___     Estado: [Borrador|Revision|Aprobado]
Nombre:
Fuente (quien lo pidio):
Prioridad: [Alta|Media|Baja]     Estabilidad: [Alta|Media|Baja]
Descripcion:
Precondicion:
Criterio de aceptacion (MEDIBLE: tiempo, cantidad, si/no):
Depende de:
Verificado por (ID del caso de prueba):
Historial de cambios:
```

---

## 3. Matriz en V (trazabilidad requisito <-> prueba)

| Fase (bajada) | Artefacto que produce | Nivel de prueba (subida) | Caso de prueba VetCare | Requisito que verifica |
|---|---|---|---|---|
| Requisitos | ERS aprobado | Pruebas de aceptacion | CP-ACEP-07 | RF-03 |
| Diseno de arquitectura | Componentes + modelo de datos | Pruebas de integracion | CP-INT-03 | RF-02 |
| Diseno detallado | Diagrama de clases | Pruebas unitarias | CP-UNI-11 | RN-01 |
| Construccion (Prog. II) | Modulo ejecutable | -- | -- | -- |

**Regla de oro:** ningun requisito puede quedar sin fila. Si no tiene prueba, no se puede demostrar cumplido.

---

## 4. Formato de solicitud de cambio (control de cambios)

| Campo | Contenido |
|---|---|
| Codigo | SC-___ |
| Fecha / solicitante | |
| Descripcion del cambio | |
| Requisito(s) afectado(s) | |
| Impacto en diseno | |
| Impacto en pruebas | |
| Esfuerzo estimado (horas de rediseno) | |
| Decision | [ ] Aprobada  [ ] Aplazada  [ ] Rechazada |
| Justificacion de la decision | |
| Nueva linea base | version ___ del ___ |

---

## 5. Control de versiones y aprobaciones

| Version | Fecha | Cambio | Autor | Aprobado por |
|---|---|---|---|---|
| 1.0 | | Version inicial | | Administradora de Huellitas |

---

## 6. Checklist antes de subir a ExamLab

- [ ] Todos los requisitos tienen ID, version, estado y criterio MEDIBLE.
- [ ] Ningun requisito quedo sin caso de prueba en la matriz.
- [ ] El diagrama en V muestra las dos ramas y dos lineas de trazabilidad rotuladas.
- [ ] La solicitud de cambio esta diligenciada con impacto y decision justificada.
