CREATE DATABASE book_search;

-- Switch connection to a new database
\c book_search

-- create table books
CREATE TABLE books(
    id bigserial NOT NULL,
    isbn varchar(50),
    title varchar(150),
    description varchar(250),
    author varchar(150),
    PRIMARY KEY (id)
);


-- inserts of examples

INSERT INTO books (id, isbn, title, description, author) VALUES (1, '973-2-1234-5680-3', 'Sin miedo a triunfar', 'Lo que no te dan para emprender es un podcast pensado, especialmente, para todas aquellas personas emprendedoras.','Karla Huerta');
INSERT INTO books (id, isbn, title, description, author) VALUES (2, '945-2-1234-5680-4', 'De cero a uno', 'Peter Thiel, gran inversionista y emprendedor, narra a partir de su experiencia qué tipo de interrogantes debe hacerse una startup.','Peter Thiel');
INSERT INTO books (id, isbn, title, description, author) VALUES (3, '912-2-1234-5680-5', 'El método Lean Startup', 'El método Lean Startupde Eric Ries, un libro que abre la puerta a un nueva mentalidad.','Eric Ries');
INSERT INTO books (id, isbn, title, description, author) VALUES (4, '874-2-1234-5680-6', 'Hyperfocus', 'Hyperfocus de Chris Bailey, una guía práctica para administrar su atención.','Chris Bailey');