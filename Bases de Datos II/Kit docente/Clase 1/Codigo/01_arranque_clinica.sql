-- VetCare DB · Clase 1 · DDL minimo demo (DB Fiddle / PostgreSQL o MySQL)
-- Objetivo PI: dejar entidades base para el ER.

CREATE TABLE dueno (
  id_dueno INT PRIMARY KEY,
  nombre VARCHAR(80) NOT NULL,
  telefono VARCHAR(30),
  email VARCHAR(120)
);

CREATE TABLE mascota (
  id_mascota INT PRIMARY KEY,
  id_dueno INT NOT NULL REFERENCES dueno(id_dueno),
  nombre VARCHAR(60) NOT NULL,
  especie VARCHAR(40),
  activa CHAR(1) DEFAULT 'S' CHECK (activa IN ('S','N'))
);

CREATE TABLE cita (
  id_cita INT PRIMARY KEY,
  id_mascota INT NOT NULL REFERENCES mascota(id_mascota),
  fecha_hora TIMESTAMP NOT NULL,
  estado VARCHAR(20) DEFAULT 'PROGRAMADA'
);

INSERT INTO dueno VALUES (1, 'Ana Perez', '3001112233', 'ana@mail.com');
INSERT INTO mascota VALUES (10, 1, 'Luna', 'Canino', 'S');
INSERT INTO cita VALUES (100, 10, '2026-09-01 09:00:00', 'PROGRAMADA');
SELECT m.nombre, d.nombre AS dueno, c.fecha_hora
FROM cita c JOIN mascota m ON m.id_mascota=c.id_mascota
JOIN dueno d ON d.id_dueno=m.id_dueno;
