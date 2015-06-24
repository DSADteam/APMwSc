INSERT INTO "Productos" (nombre,descripcion,escala) VALUES ('Proyecto APMwSc','Proyecto realizado por D.S.A.D','cualitativo');
INSERT INTO "Productos" (nombre,descripcion,escala) VALUES ('Ingenieria en Computacion','Creacion de la página web del departamento','cualitativo');

INSERT INTO "Acciones" (descripcion,"idProducto") VALUES ('logearme en la pagina',1);
INSERT INTO "Acciones" (descripcion,"idProducto") VALUES ('crear un actor nuevo',1);
INSERT INTO "Acciones" (descripcion,"idProducto") VALUES ('seleccionar tareas por peso',2);

INSERT INTO "Actores" (nombre,descripcion,"idProducto") VALUES ('desarrollador','Miembro del equipo de desarrollo',1);
INSERT INTO "Actores" (nombre,descripcion,"idProducto") VALUES ('maestroScrum','Maestro Scrum',1);
INSERT INTO "Actores" (nombre,descripcion,"idProducto") VALUES ('duenoProducto','Dueño de producto',1);
INSERT INTO "Actores" (nombre,descripcion,"idProducto") VALUES ('desarrollador','Miembro del equipo de desarrollo',2);
INSERT INTO "Actores" (nombre,descripcion,"idProducto") VALUES ('maestroScrum','Maestro Scrum',2);
INSERT INTO "Actores" (nombre,descripcion,"idProducto") VALUES ('duenoProducto','Dueño de producto',2);


--Claves para todos es HOLAhol4! encriptado
INSERT INTO "dbuser" VALUES('Javier'      ,'javierlopm' ,'2e376b23934d2509220a3d98c8116e61d4a03fa33b94dfadd1f5e94d69ef340d:ff03dc0f9de44c868a6d03d252294458','javier@correo.com'  ,3);
INSERT INTO "dbuser" VALUES('Nabil'       ,'nabil'      ,'2e376b23934d2509220a3d98c8116e61d4a03fa33b94dfadd1f5e94d69ef340d:ff03dc0f9de44c868a6d03d252294458','nabil@correo.com'   ,3);
INSERT INTO "dbuser" VALUES('Cristina'    ,'cristinab'  ,'2e376b23934d2509220a3d98c8116e61d4a03fa33b94dfadd1f5e94d69ef340d:ff03dc0f9de44c868a6d03d252294458','cristina@correo.com',3);
INSERT INTO "dbuser" VALUES('Samuel'      ,'samuel'     ,'2e376b23934d2509220a3d98c8116e61d4a03fa33b94dfadd1f5e94d69ef340d:ff03dc0f9de44c868a6d03d252294458','samuel@correo.com'  ,3);
INSERT INTO "dbuser" VALUES('Roberto'     ,'robertor'   ,'2e376b23934d2509220a3d98c8116e61d4a03fa33b94dfadd1f5e94d69ef340d:ff03dc0f9de44c868a6d03d252294458','roberto@correo.com' ,3);
INSERT INTO "dbuser" VALUES('Meggie'      ,'meggies'    ,'2e376b23934d2509220a3d98c8116e61d4a03fa33b94dfadd1f5e94d69ef340d:ff03dc0f9de44c868a6d03d252294458','meggie@correo.com'  ,3);
INSERT INTO "dbuser" VALUES('Ascander'    ,'ascander'   ,'2e376b23934d2509220a3d98c8116e61d4a03fa33b94dfadd1f5e94d69ef340d:ff03dc0f9de44c868a6d03d252294458','ascander@correo.com',3);
INSERT INTO "dbuser" VALUES('Jean Carlos' ,'jeanc'      ,'2e376b23934d2509220a3d98c8116e61d4a03fa33b94dfadd1f5e94d69ef340d:ff03dc0f9de44c868a6d03d252294458','jeanc@correo.com'   ,3);
INSERT INTO "dbuser" VALUES('Javier'      ,'javierlopm2' ,'2e376b23934d2509220a3d98c8116e61d4a03fa33b94dfadd1f5e94d69ef340d:ff03dc0f9de44c868a6d03d252294458','javier@correo.com'  ,1);
INSERT INTO "dbuser" VALUES('Nabil'       ,'nabil2'      ,'2e376b23934d2509220a3d98c8116e61d4a03fa33b94dfadd1f5e94d69ef340d:ff03dc0f9de44c868a6d03d252294458','nabil@correo.com'   ,2);
INSERT INTO "dbuser" VALUES('Nabil'       ,'nabil3'      ,'2e376b23934d2509220a3d98c8116e61d4a03fa33b94dfadd1f5e94d69ef340d:ff03dc0f9de44c868a6d03d252294458','nabil@correo.com'   ,1);
INSERT INTO "dbuser" VALUES('Cristina'    ,'cristinab2'  ,'2e376b23934d2509220a3d98c8116e61d4a03fa33b94dfadd1f5e94d69ef340d:ff03dc0f9de44c868a6d03d252294458','cristina@correo.com',2);
INSERT INTO "dbuser" VALUES('Samuel'      ,'samuel2'     ,'2e376b23934d2509220a3d98c8116e61d4a03fa33b94dfadd1f5e94d69ef340d:ff03dc0f9de44c868a6d03d252294458','samuel@correo.com'  ,2);
INSERT INTO "dbuser" VALUES('Roberto'     ,'robertor2'   ,'2e376b23934d2509220a3d98c8116e61d4a03fa33b94dfadd1f5e94d69ef340d:ff03dc0f9de44c868a6d03d252294458','roberto@correo.com' ,2);
INSERT INTO "dbuser" VALUES('Meggie'      ,'meggies2'    ,'2e376b23934d2509220a3d98c8116e61d4a03fa33b94dfadd1f5e94d69ef340d:ff03dc0f9de44c868a6d03d252294458','meggie@correo.com'  ,2);
INSERT INTO "dbuser" VALUES('Ascander'    ,'ascander2'   ,'2e376b23934d2509220a3d98c8116e61d4a03fa33b94dfadd1f5e94d69ef340d:ff03dc0f9de44c868a6d03d252294458','ascander@correo.com',2);
INSERT INTO "dbuser" VALUES('Jean Carlos' ,'jeanc2'      ,'2e376b23934d2509220a3d98c8116e61d4a03fa33b94dfadd1f5e94d69ef340d:ff03dc0f9de44c868a6d03d252294458','jeanc@correo.com'   ,2);

INSERT INTO "Objetivos" (descripcion,"idProducto",transversal) VALUES ('ser reconocido como usuario valido',1,'no transversal');
INSERT INTO "Objetivos" (descripcion,"idProducto",transversal) VALUES ('realizar tareas correspondientes',1,'no transversal');


INSERT INTO "Historias" (codigo,"idProducto","idAccion",tipo,prioridad) VALUES ('Historia de de sprint 1',1,1,'opcional',1);


INSERT INTO "ObjetivosHistorias" ("idHistoria","idObjetivo") VALUES (1,1);
INSERT INTO "ObjetivosHistorias" ("idHistoria","idObjetivo") VALUES (1,2);

INSERT INTO "ActoresHistorias" ("idHistoria","idActor") VALUES (1,1);
INSERT INTO "ActoresHistorias" ("idHistoria","idActor") VALUES (1,2);
INSERT INTO "ActoresHistorias" ("idHistoria","idActor") VALUES (1,3);

INSERT INTO "Categorias" ("nombreCategoria",peso) VALUES ('implementacion',3);
INSERT INTO "Categorias" ("nombreCategoria",peso) VALUES ('integracion',4);

INSERT INTO "Tareas" (descripcion,"idHistoria","nombreCategoria",peso) VALUES ('crear scrum master',1,'implementacion',4);
