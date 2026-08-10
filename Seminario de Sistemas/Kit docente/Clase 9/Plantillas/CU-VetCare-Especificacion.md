# Plantilla de especificacion de casos de uso - VetCare (Clinica Huellitas)

> Regla de oro: el diagrama muestra QUE hace el sistema; esta plantilla explica COMO se comporta paso a paso. Sin la plantilla diligenciada, el caso de uso NO esta hecho.

## 1. Ficha de identificacion

| Campo | Contenido |
|---|---|
| ID | CU-01 |
| Nombre | Registrar mascota |
| Actor primario | Recepcionista |
| Actores secundarios | Ninguno |
| Requisitos que cubre | RF-03, RF-04 |
| Frecuencia estimada | 15 veces al dia |
| Prioridad | Alta |

## 2. Precondiciones

1. El usuario inicio sesion con rol Recepcionista.
2. El propietario ya existe en el sistema, o se registra dentro del flujo alterno 2a.

## 3. Postcondiciones

- Exito: queda creada una ficha de mascota con codigo unico de formato VC-0000 (por ejemplo VC-0001) asociada a un propietario, y queda registrado en la bitacora quien la creo y en que momento.
- Fracaso: no se crea ningun registro parcial; el sistema conserva los datos digitados para que el usuario corrija.

## 4. Flujo principal (camino feliz)

| Paso | Actor | Sistema |
|---|---|---|
| 1 | Selecciona la opcion Registrar mascota | Muestra el formulario con los campos obligatorios marcados |
| 2 | Digita el documento del propietario | Busca y muestra nombre y telefono del propietario |
| 3 | Digita nombre, especie, raza, fecha de nacimiento y sexo | Valida formato y habilita la accion Guardar |
| 4 | Confirma el registro | Genera el codigo de mascota, guarda la ficha y muestra la confirmacion con el codigo |

## 5. Flujos alternos

- 2a. El propietario no existe: el sistema ofrece registrarlo; se capturan documento, nombre, telefono y direccion; el flujo continua en el paso 3.
- 3a. La fecha de nacimiento es posterior a hoy: el sistema rechaza el dato, marca el campo y no permite continuar hasta corregirlo.
- 4a. Ya existe una mascota con el mismo nombre para ese propietario: el sistema advierte y exige confirmacion explicita antes de guardar.

## 6. Excepciones

- E1. Falla de conexion al guardar: el sistema informa el error, no crea la ficha y conserva el formulario diligenciado.

## 7. Reglas de negocio asociadas

- RN-01: toda mascota debe tener exactamente un propietario responsable.
- RN-02: el codigo de mascota nunca se reutiliza, ni siquiera si la ficha se inactiva.

## 8. Matriz de trazabilidad

| RF | Caso de uso | Mockup | Clases implicadas |
|---|---|---|---|
| RF-02 | CU-00 Registrar propietario | M-01 Formulario de propietario | Propietario |
| RF-03, RF-04 | CU-01 Registrar mascota | M-02 Formulario de mascota | Mascota, Propietario |
| RF-05 | CU-02 Buscar expediente | M-03 Buscador de expedientes | Mascota, Consulta |
| RF-06 | CU-03 Registrar consulta medica | M-05 Ficha de consulta | Consulta, Veterinario |
| RF-08 | CU-04 Agendar cita | M-04 Agenda | Cita, Veterinario |
| RF-07 | (todavia sin caso de uso: HUERFANO) | -- | -- |

## 9. Checklist antes de entregar en ExamLab

- [ ] Cada caso de uso se llama verbo en infinitivo + objeto del dominio.
- [ ] Ningun caso de uso se llama Guardar, Validar, Mostrar pantalla o Dar clic.
- [ ] Todo caso de uso del diagrama tiene al menos un RF que lo origina.
- [ ] Todo RF llega a un caso de uso o queda registrado por escrito como huerfano pendiente de decision.
- [ ] Cada especificacion tiene minimo dos flujos alternos numerados.
- [ ] Las postcondiciones se pueden verificar mirando el estado del sistema.
- [ ] El limite del sistema esta dibujado y rotulado VetCare.
