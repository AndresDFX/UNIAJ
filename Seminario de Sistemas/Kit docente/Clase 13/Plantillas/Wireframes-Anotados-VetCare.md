# Wireframes anotados y prototipo navegable - VetCare
**Clinica Veterinaria Huellitas | Clase 13 - Diseño de interfaces**

Equipo: ______________________  Fecha: ____________  Version: 1.0

---

## 1. Usuaria de referencia

| Aspecto | Descripcion |
|---|---|
| Rol | Recepcionista de Huellitas |
| Experiencia clinica | Alta |
| Experiencia informatica | Baja: escribe lento, no usa atajos |
| Contexto de uso | Atiende telefono mientras registra, interrupciones cada 2-3 minutos |
| Meta de tiempo | Registrar un paciente nuevo en menos de 2 minutos |

---

## 2. Los tres niveles (marcar lo entregado)

- [ ] **Wireframe** (gris, sin color, sin logo): responde QUE informacion va y en que orden.
- [ ] **Mockup** (color, tipografia, iconos): responde COMO SE VE.
- [ ] **Prototipo** (con clic y transiciones): responde COMO SE SIENTE usarlo.

> Regla: no se pasa a mockup hasta que el wireframe tenga anotaciones completas.

---

## 3. Pantalla 1: Registrar mascota

Pegar aqui la imagen del wireframe con numeros de 1 a N.

### Tabla de anotaciones

| # | Elemento en pantalla | Atributo del diccionario | Tipo / Longitud | Oblig. | RF que lo exige |
|---|---|---|---|---|---|
| 1 | Campo Nombre de la mascota | Mascota.nombre | Texto(60) | Si | RF-03 |
| 2 | Lista Especie | Mascota.especie | Lista cerrada | Si | RF-03 |
| 3 | Lista Raza | Mascota.raza | Lista(40) | No | RF-03 |
| 4 | Selector Fecha de nacimiento | Mascota.fecha_nacimiento | Fecha | No | RF-03 |
| 5 | Buscador de dueño | Dueño.documento | Texto(15) | Si | RF-02 |
| 6 | Boton Guardar | operacion registrarMascota | - | - | RF-03 |
| 7 | Mensaje de confirmacion con codigo | Mascota.codigo | Texto(8) | - | RNF-02 |
| 8 |  |  |  |  |  |
| 9 |  |  |  |  |  |

> Si una fila no tiene RF, se borra el elemento o se crea el requisito. No hay campos huerfanos.

---

## 4. Pantalla 2: Buscar expediente

| Decision de diseño | Definicion del equipo |
|---|---|
| Criterios de busqueda | Documento del dueño / Nombre de la mascota / Codigo de ficha |
| Columnas de la lista de resultados | Codigo, Nombre, Especie, Edad, Dueño |
| Mensaje si hay 0 resultados | `No encontramos ninguna ficha con ese dato.` mas las acciones Buscar por otro criterio y Registrar mascota nueva |
| Que pasa con 12 resultados iguales | Se desambigua por especie, edad y nombre del dueño sin abrir la ficha |
| Tiempo maximo de respuesta | 3 segundos (RNF-02) |

---

## 5. Auditoria de los 4 principios de usabilidad

| Principio | Evidencia concreta en nuestro diseño | Pantalla |
|---|---|---|
| Visibilidad del estado | Ej: mensaje `Ficha guardada, codigo M-0421` y boton bloqueado mientras guarda |  |
| Prevencion de errores | Ej: calendario en vez de fecha tecleada; confirmacion antes de eliminar |  |
| Consistencia | Ej: el boton primario siempre se llama Guardar y va abajo a la derecha |  |
| Reconocer antes que recordar | Ej: lista cerrada de especies en vez de escribir el codigo de memoria |  |

---

## 6. Caminos alternos diseñados (minimo 2)

| # | Camino alterno | Que hace la interfaz |
|---|---|---|
| A | El dueño no esta registrado | Abre Registrar dueño y regresa conservando lo escrito de la mascota |
| B | La mascota ya tiene ficha | Avisa `Esta mascota ya tiene ficha en la clinica` y ofrece abrirla |
| C |  |  |

---

## 7. Prototipo navegable

| Transicion | Desde | Hacia | Principio que cumple |
|---|---|---|---|
| 1 | Registrar mascota (Guardar) | Confirmacion con codigo | Visibilidad del estado |
| 2 | Confirmacion (Ver ficha) | Buscar expediente precargado | Reconocer antes que recordar |
| 3 | Fila de resultados | Ficha del paciente | Consistencia |

Enlace del prototipo (Figma o Penpot, con permiso de lectura): ______________________

---

## 8. Bitacora de prueba de pasillo

| Probador (otro equipo) | Tarea asignada | Tiempo | Clics | Donde dudo | Donde se equivoco |
|---|---|---|---|---|---|
| 1 | Registrar a Luna de la señora Perez y hallar su ficha |  |  |  |  |
| 2 |  |  |  |  |  |
| 3 |  |  |  |  |  |

**Dos cambios que haremos por lo observado:**
1. ______________________________________________
2. ______________________________________________

---

## 9. Checklist antes de subir a ExamLab

- [ ] Wireframe en gris de las 2 pantallas
- [ ] Mockup de las 2 pantallas
- [ ] Tabla de anotaciones sin campos huerfanos
- [ ] Minimo 3 transiciones navegables funcionando
- [ ] Minimo 2 caminos alternos diseñados
- [ ] Auditoria de los 4 principios diligenciada
- [ ] Bitacora de prueba de pasillo con 3 personas
- [ ] Enlace del prototipo con permiso de lectura, verificado desde otro navegador
