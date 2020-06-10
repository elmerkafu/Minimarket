CREATE TABLE usuarios(
	id_usuario serial primary key unique,
	username varchar(50),
	pwd varchar(250),
	nombre varchar(50),
	apellido varchar(50),
	edad integer,
	cargo integer
);