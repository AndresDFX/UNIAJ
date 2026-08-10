# Guion de sustentacion y decisiones de diseño - VetCare
**Clinica Veterinaria Huellitas | Clase 14 - Preparacion de la sustentacion**

Equipo: ______________________  Fecha: ____________  Duracion objetivo: 12 minutos

---

## 1. Frase de apertura (se aprende de memoria, maximo 25 palabras)

> _Ejemplo:_ En Huellitas se extravian fichas, encontrar un historial toma ocho minutos y no existe una sola metrica de atencion. Estos son los planos que lo resuelven.

Nuestra frase: ______________________________________________

---

## 2. Guion cronometrado y reparto

| Bloque | Minutos | Contenido exacto que se muestra | Integrante |
|---|---|---|---|
| Problema | 00:00-01:30 | Los 3 dolores de Huellitas |  |
| Alcance | 01:30-03:00 | Que entra y que NO entra, con razon |  |
| Requisitos | 03:00-05:00 | 3 RF criticos y 2 RNF medibles |  |
| Modelo | 05:00-07:00 | Casos de uso y diagrama de clases |  |
| Interfaz | 07:00-09:00 | Prototipo en vivo, 1 flujo completo |  |
| Decisiones | 09:00-11:00 | Tabla de 3 decisiones |  |
| Riesgos y siguiente paso | 11:00-11:30 | Lo abierto y el handoff |  |
| Cierre | 11:30-12:00 | Frase de valor |  |

> Regla: ningun integrante habla menos de 2 minutos y todos deben poder responder sobre cualquier parte.

---

## 3. Tabla de decisiones de diseño (minimo 3)

| # | Decision tomada | Alternativa descartada | Criterio de eleccion | Consecuencia asumida |
|---|---|---|---|---|
| 1 | Historia_Clinica es clase aparte de Mascota | Guardar diagnosticos como campos de Mascota | Una mascota tiene muchas consultas: relacion 1 a N | Una entidad mas y una consulta extra al abrir la ficha |
| 2 | RNF-02: buscar expediente en menos de 3 s con 5.000 fichas | No fijar tiempo | El dolor declarado es la demora; sin numero no hay mejora demostrable | Obliga a indice por documento del dueño y por codigo |
| 3 | Fecha de nacimiento opcional | Campo obligatorio | Muchos dueños de rescatados no la saben; obligar genera datos inventados | La edad se muestra como aproximada cuando falta |
| 4 |  |  |  |  |

> Una decision sin alternativa descartada NO es una decision, es una costumbre.

---

## 4. Banco de preguntas del jurado (minimo 10)

| # | Pregunta esperada | Respuesta en maximo 2 frases | Quien responde |
|---|---|---|---|
| 1 | Como saben que este requisito es necesario? |  |  |
| 2 | Que pasa si dos recepcionistas registran la misma mascota al tiempo? |  |  |
| 3 | Por que esta clase existe y no es un atributo de otra? |  |  |
| 4 | Como mediria usted su RNF de tiempo de respuesta? |  |  |
| 5 | Que pasa si el sistema se cae a mitad de un registro? |  |  |
| 6 | Que dejaron fuera del alcance y por que? |  |  |
| 7 | Donde vive el RF-04 en el diagrama de clases? |  |  |
| 8 | Este campo de la pantalla, en que parte del diccionario esta? |  |  |
| 9 | Que cambiarian si Huellitas abre una segunda sede? |  |  |
| 10 | Quien hizo esta parte y por que la hizo asi? |  |  |

**Regla de oro:** si no lo sabe, no lo invente. Diga: `no lo modelamos, lo registramos como riesgo abierto y se resolveria asi...`

---

## 5. Checklist de consolidacion del documento final

- [ ] Portada con nombre del proyecto, equipo y version
- [ ] Indice con numeracion
- [ ] Problema y alcance (que entra / que no entra)
- [ ] Tabla RF y RNF con prioridad
- [ ] Diagrama de casos de uso
- [ ] Diagrama de clases
- [ ] Diagrama de secuencia del flujo critico
- [ ] Wireframes anotados y enlace al prototipo
- [ ] Diccionario de datos
- [ ] Tabla de decisiones de diseño
- [ ] Matriz de trazabilidad RF -> pantalla -> clase
- [ ] **Verificacion de nombres**: los atributos se llaman IGUAL en clases, diccionario y anotaciones de pantalla

**Inconsistencia encontrada y corregida hoy:** ______________________________________________

---

## 6. Ensayo cronometrado

| Ensayo | Tiempo real total | Bloque que se paso | Correccion aplicada |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |

**Plan B tecnico:** [ ] capturas del prototipo  [ ] documento en PDF descargado  [ ] diagramas exportados a imagen  [ ] alguien mas sabe manejar el prototipo
