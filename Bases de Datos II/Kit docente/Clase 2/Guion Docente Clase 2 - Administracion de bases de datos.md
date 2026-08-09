# Guion docente · Clase 2 · Administracion de BD · Roles VetCare

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** AUTONOMA (festivo)
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** Plan de roles/privilegios de VetCare
- **Entregable de hoy:** Documento Roles_VetCare + script GRANT/REVOKE (o plan equivalente)
- **Herramienta:** Oracle Live SQL / DB Fiddle + Google Docs
- **Slides:** Clases/Clase 2 - Administracion de bases de datos/Presentacion.pptx

> Sin mapa completo del curso, sin bio del docente, sin fechas de periodo.
> Presentacion del Curso / Acuerdo cubren logistica global.

## Fundamento teorico para el docente (al servicio del PI)

El objetivo de la clase no es «cubrir un capitulo» aislado, sino producir evidencia
del PI VetCare. La teoria se limita a desbloquear el taller.

- Administracion de BD = gestionar QUIEN puede hacer QUE sobre CADA objeto. Tres piezas: usuario (identidad que se conecta), rol (paquete de privilegios con nombre, ej. RECEPCION), privilegio (permiso atomico: SELECT, INSERT, UPDATE, DELETE, EXECUTE sobre un objeto concreto).
- Principio de minimo privilegio: cada rol recibe solo lo que necesita para su funcion, ni un privilegio mas. No es paranoia, es reduccion de superficie de dano: si roban la sesion de un recepcionista, no debe poder borrar el historial clinico ni ver nomina.
- Separacion de funciones (segregation of duties): quien disena/modifica el esquema (DDL: CREATE/ALTER/DROP) no deberia ser la misma cuenta que opera datos del dia a dia (DML: INSERT/UPDATE/DELETE), y quien audita solo deberia leer (SELECT), nunca escribir.
- GRANT otorga un privilegio a un rol o usuario; REVOKE lo retira. Un rol se puede asignar a varios usuarios (todos los recepcionistas heredan el rol RECEPCION) y modificar en un solo lugar en vez de uno por uno.
- Error de docente que no domina el tema: crear un unico usuario 'admin' que todos comparten (rompe la trazabilidad de auditoria) o dar DBA/ALL PRIVILEGES a todo el equipo 'para que no falle nada' — exactamente lo opuesto a minimo privilegio.
- En el playground (Live SQL / DB Fiddle) el motor puede restringir CREATE ROLE o GRANT reales: cuando eso pase, el equipo redacta la matriz rol x objeto x privilegio como documento/plan, y ejecuta lo que el playground SI permita como evidencia parcial — no es escusa para omitir el analisis.

**Demo que usted debe poder repetir:** Matriz rol x objeto x privilegio sobre tablas VetCare.

## Referencias a diapositivas
1. Slide 1 portada (Clase N + titulo VetCare)
2. Slide Agenda 120 min
3. Slide Objetivo PI de la clase
4. Slide Teoria Core
5. Slide Demo del dia
6. Slide Herramientas de hoy (logos 3-4)
7. Bloque Taller ampliado: contexto / objetivo / escenario / pasos / pistas
8. Slide Criterios de exito / entregable
9. Slide Para el PI esta semana
10. Slide Cierre
11. Solucion PRIVADA: Kit docente/Clase N/Solucion Taller Clase N - VetCare.docx

## Plan minuto a minuto (120 min equivalentes — trabajo autonomo)

> El estudiante trabaja sin encuentro sincrono. Usted publica este guion resumido + taller en Campus.

### Bloque A (0-20) · Encuadre PI
**Decir/publicar:** «Hoy avanzamos el PI en: Plan de roles/privilegios de VetCare. No es un taller suelto.»
Referencia slides: Agenda + Objetivo PI.

### Bloque B (20-45) · Teoria minima
Leer Teoria Core. Tomar notas en el informe del PI.

### Bloque C (45-100) · Practica = entregable PI
Seguir el taller estudiante. Herramienta: Oracle Live SQL / DB Fiddle + Google Docs.
Salida esperada de la practica (publiquela junto al enunciado para que el
estudiante autonomo sepa si le quedo bien):
📸 Pantallazo: [CAP: demo VetCare Clase 2]

### Bloque D (100-120) · Empaquetado y cierre
Subir entregable a ExamLab. Actualizar checklist PI del equipo.


## Codigo / scripts
Carpeta Codigo/ — archivo 02_roles_vetcare.sql.

## Capturas
Carpeta Capturas/. Placeholders [CAP: ...] arriba; reemplazar por PNG reales cuando pueda
(Playwright/manual en DB Fiddle, draw.io, Live SQL).

## Criterios de exito del dia
- Equipos tienen el entregable o gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
