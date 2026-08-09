# Solución Taller Clase 1 — Arranque VetCare

> DOCUMENTO DOCENTE — PRIVADO. No publicar en Clases/.

**Resumen:** ER minimo Dueño-Mascota-Cita + 3 reglas + alcance.

## Alineacion
- Taller: `Clases/Clase 1 - Revision BD I y arranque VetCare/Taller PI - Clase 1 - VetCare.docx`
- Hito: Arranque PI: dominio, alcance y borrador ER de VetCare DB
- Entregable: Ficha de equipo + ER borrador (PNG) + lista de entidades/reglas

## Solucion paso a paso
1. Formar equipo de 2-3 y nombrarlo VetCare-<apellido del lider> para identificarlo en todas las entregas del semestre.
2. Listar las entidades minimas del dominio: Dueño (persona que trae la mascota), Mascota (paciente), Veterinario (quien atiende), Cita (agenda de una atencion). Consulta, Insumo y DetalleFactura se agregan en clases posteriores.
3. Redactar como reglas de negocio explicitas (no solo mencionarlas): "una mascota con activa=N no puede tener una cita nueva", "el stock de un insumo nunca puede quedar en negativo", "toda cancelacion de cita queda registrada con usuario y fecha".
4. Dibujar el ER borrador marcando cardinalidad en cada relacion (Dueño 1-N Mascota, Mascota 1-N Cita) y exportarlo como PNG legible, no un boceto a mano ilegible.
5. Escribir el alcance en dos listas explicitas: que SI cubre el PI este semestre (agenda, facturacion basica, roles) y que NO cubre (ej. pagos en linea, historial clinico completo) para evitar scope creep en clases futuras.

## Ejemplo / SQL / artefactos
- DDL: Kit docente/Clase 1/Codigo/01_arranque_vetcare.sql
- ER: Dueño 1-N Mascota; Mascota 1-N Cita.
- Script demo: `Kit docente/Clase 1/Codigo/01_arranque_vetcare.sql`

## Rubrica corta
- [ ] Equipo (1)
- [ ] ER (3)
- [ ] Reglas (2)
- [ ] Alcance (2)
- [ ] Entrega (2)

## Errores frecuentes
- ER genérico.
- Sin FK.
- Scope infinito.

Campus Virtual UNIAJC.
