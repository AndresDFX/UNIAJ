# Solucion Taller · Clase 8 · Introduccion a UML

> DOCUMENTO DOCENTE — PRIVADO. No publicar en Clases/.

## Solucion paso a paso
1. Paso 1 resuelto: los sustantivos que sobreviven son dueno, mascota, cita, veterinario y atencion; se descartan reporte mensual (es una salida, no un concepto), login y buscador (son pantallas) y base de datos (es tecnologia).
2. Paso 2 resuelto: quedan cinco cajas de tres compartimentos, todas en singular y con mayuscula inicial: Dueno, Mascota, Veterinario, Cita y Atencion. Se corrigen en el tablero los nombres Mascotas, tbl_duenos y CitaForm que siempre aparecen en los primeros intentos.
3. Paso 3 resuelto: Dueno con -documento: String, -nombre: String, -telefono: String, -direccion: String; Mascota con -codigo: String, -nombre: String, -especie: String, -raza: String, -fechaNacimiento: Date; Veterinario con -tarjetaProfesional: String, -nombre: String, -especialidad: String, -telefono: String; Cita con -numero: int, -fechaHora: DateTime, -motivo: String, -estado: String; Atencion con -fecha: Date, -diagnostico: String, -tratamiento: String, -observaciones: String. Se verifica que el nombre del dueno no se repita dentro de Mascota y que la especialidad no aparezca en Cita.
4. Paso 4 resuelto: Mascota +calcularEdad(): int; Cita +reprogramar(nuevaFecha: DateTime): void y +cancelar(motivo: String): void; Dueno +registrarMascota(m: Mascota): void; Veterinario +agendaDelDia(f: Date): List; Atencion +resumen(): String. Se eliminan del tablero los metodos conectarBD, guardar y abrirVentana que proponen siempre los estudiantes, porque no son responsabilidades del concepto sino de la tecnologia.
5. Paso 5 resuelto: las asociaciones quedan Dueno 1 --- 0..* Mascota (es dueno de), Mascota 1 --- 0..* Cita (tiene agendada), Veterinario 1 --- 0..* Cita (atiende) y Cita 1 --- 0..1 Atencion (genera, porque una cita cancelada no genera atencion). Cada una se lee en voz alta antes de exportar: 'un dueno puede tener cero o mas mascotas y una mascota pertenece a un unico dueno'. Verificacion final con el cliente: se confirma con el Dr. Ramirez que en esta version una mascota pertenece a un solo dueno (regla de negocio RN-02), lo cual justifica el 1 en ese extremo y evita la tabla intermedia que si tocaria si fuera 0..* en ambos lados.

## Rubrica corta
- [ ] Clases del dominio correctas, en singular y sin clases tecnicas (3)
- [ ] Atributos con visibilidad y tipo, sin duplicados entre clases (3)
- [ ] Asociaciones con multiplicidad y nombre de relacion en las cuatro lineas (3)
- [ ] Metodos propios del dominio y trazabilidad de cada clase a un RF o historia (1)

## Errores frecuentes
- Poner fechaCita como atributo dentro de Mascota: con eso cada mascota tendria una sola cita en toda su vida; la cita es una clase aparte relacionada 1 a muchos.
- Nombrar las clases en plural o como tablas (Mascotas, tbl_duenos) y dejar atributos sin tipo, con lo cual el diagrama deja de servir para derivar el diccionario de datos.
- Usar el triangulo de herencia entre Dueno y Mascota o entre Cita y Veterinario, cuando ahi no hay ningun es-un sino una simple asociacion.

Plantilla de apoyo: `Kit docente/Clase 8/Plantillas/Diagrama-Clases-VetCare.md`