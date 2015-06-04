
INSERT INTO "Productos" (nombre,descripcion,escala) VALUES ('Proyecto APMwSc','Metere la cadena de software','cualitativo');
INSERT INTO "Productos" (nombre,descripcion,escala) VALUES ('Surfeadores divertido','De pana que si','cualitativo');
INSERT INTO "Productos" (nombre,descripcion,escala) VALUES ('Piedreros asociados','Adoro esta materia','cuantitativo');
INSERT INTO "Productos" (nombre,descripcion,escala) VALUES ('Ingenieria de software','Ojala la abrieran todos los trimestres','cuantitativo');

INSERT INTO "Acciones" (descripcion,"idProducto") VALUES ('logearme en la pagina',1);
INSERT INTO "Acciones" (descripcion,"idProducto") VALUES ('Documentar todo',1);

INSERT INTO "Acciones" (descripcion,"idProducto") VALUES ('Crear repositorio divertido',2);
INSERT INTO "Acciones" (descripcion,"idProducto") VALUES ('Documentar tablas',2);

INSERT INTO "Acciones" (descripcion,"idProducto") VALUES ('Crear repositorio volador',3);
INSERT INTO "Acciones" (descripcion,"idProducto") VALUES ('Documentar cosas',3);

INSERT INTO "Actores" (nombre,descripcion,"idProducto") VALUES ('Developer','Desarrolador de proyecto',1);
INSERT INTO "Actores" (nombre,descripcion,"idProducto") VALUES ('Scrum Master','Guia del grupo',1);
INSERT INTO "Actores" (nombre,descripcion,"idProducto") VALUES ('Product Owner','Dueno del producto',1);

INSERT INTO "Actores" (nombre,descripcion,"idProducto") VALUES ('Developer','Desarrolador de proyecto',2);
INSERT INTO "Actores" (nombre,descripcion,"idProducto") VALUES ('Scrum Master','Guia del grupo',2);
INSERT INTO "Actores" (nombre,descripcion,"idProducto") VALUES ('Product Owner','Dueno del producto',2);

INSERT INTO "Actores" (nombre,descripcion,"idProducto") VALUES ('Developer','Desarrolador de proyecto',3);
INSERT INTO "Actores" (nombre,descripcion,"idProducto") VALUES ('Scrum Master','Guia del grupo',3);
INSERT INTO "Actores" (nombre,descripcion,"idProducto") VALUES ('Product Owner','Dueno del producto',3);

--Claves para todos es HOLAhol4! encriptado
INSERT INTO "dbuser" VALUES('Javier'      ,'javierlopm' ,'2e376b23934d2509220a3d98c8116e61d4a03fa33b94dfadd1f5e94d69ef340d:ff03dc0f9de44c868a6d03d252294458','javier@correo.com'  ,3);
INSERT INTO "dbuser" VALUES('Nabil'       ,'nabil'      ,'2e376b23934d2509220a3d98c8116e61d4a03fa33b94dfadd1f5e94d69ef340d:ff03dc0f9de44c868a6d03d252294458','nabil@correo.com'   ,3);
INSERT INTO "dbuser" VALUES('Cristina'    ,'cristinab'  ,'2e376b23934d2509220a3d98c8116e61d4a03fa33b94dfadd1f5e94d69ef340d:ff03dc0f9de44c868a6d03d252294458','cristina@correo.com',3);
INSERT INTO "dbuser" VALUES('Samuel'      ,'samuel'     ,'2e376b23934d2509220a3d98c8116e61d4a03fa33b94dfadd1f5e94d69ef340d:ff03dc0f9de44c868a6d03d252294458','samuel@correo.com'  ,3);
INSERT INTO "dbuser" VALUES('Roberto'     ,'robertor'   ,'2e376b23934d2509220a3d98c8116e61d4a03fa33b94dfadd1f5e94d69ef340d:ff03dc0f9de44c868a6d03d252294458','roberto@correo.com' ,3);
INSERT INTO "dbuser" VALUES('Meggie'      ,'meggies'    ,'2e376b23934d2509220a3d98c8116e61d4a03fa33b94dfadd1f5e94d69ef340d:ff03dc0f9de44c868a6d03d252294458','meggie@correo.com'  ,3);
INSERT INTO "dbuser" VALUES('Ascander'    ,'ascander'   ,'2e376b23934d2509220a3d98c8116e61d4a03fa33b94dfadd1f5e94d69ef340d:ff03dc0f9de44c868a6d03d252294458','ascander@correo.com',3);
INSERT INTO "dbuser" VALUES('Jean Carlos' ,'jeanc'      ,'2e376b23934d2509220a3d98c8116e61d4a03fa33b94dfadd1f5e94d69ef340d:ff03dc0f9de44c868a6d03d252294458','jeanc@correo.com'   ,3);

INSERT INTO "dbuser" VALUES('Javier'      ,'javierlopm2' ,'2e376b23934d2509220a3d98c8116e61d4a03fa33b94dfadd1f5e94d69ef340d:ff03dc0f9de44c868a6d03d252294458','javier@correo.com'  ,2);
INSERT INTO "dbuser" VALUES('Nabil'       ,'nabil2'      ,'2e376b23934d2509220a3d98c8116e61d4a03fa33b94dfadd1f5e94d69ef340d:ff03dc0f9de44c868a6d03d252294458','nabil@correo.com'   ,2);
INSERT INTO "dbuser" VALUES('Cristina'    ,'cristinab2'  ,'2e376b23934d2509220a3d98c8116e61d4a03fa33b94dfadd1f5e94d69ef340d:ff03dc0f9de44c868a6d03d252294458','cristina@correo.com',2);
INSERT INTO "dbuser" VALUES('Samuel'      ,'samuel2'     ,'2e376b23934d2509220a3d98c8116e61d4a03fa33b94dfadd1f5e94d69ef340d:ff03dc0f9de44c868a6d03d252294458','samuel@correo.com'  ,2);
INSERT INTO "dbuser" VALUES('Roberto'     ,'robertor2'   ,'2e376b23934d2509220a3d98c8116e61d4a03fa33b94dfadd1f5e94d69ef340d:ff03dc0f9de44c868a6d03d252294458','roberto@correo.com' ,2);
INSERT INTO "dbuser" VALUES('Meggie'      ,'meggies2'    ,'2e376b23934d2509220a3d98c8116e61d4a03fa33b94dfadd1f5e94d69ef340d:ff03dc0f9de44c868a6d03d252294458','meggie@correo.com'  ,2);
INSERT INTO "dbuser" VALUES('Ascander'    ,'ascander2'   ,'2e376b23934d2509220a3d98c8116e61d4a03fa33b94dfadd1f5e94d69ef340d:ff03dc0f9de44c868a6d03d252294458','ascander@correo.com',2);
INSERT INTO "dbuser" VALUES('Jean Carlos' ,'jeanc2'      ,'2e376b23934d2509220a3d98c8116e61d4a03fa33b94dfadd1f5e94d69ef340d:ff03dc0f9de44c868a6d03d252294458','jeanc@correo.com'   ,2);

INSERT INTO "Objetivos" (descripcion,"idProducto",transversal) VALUES ('hacer las cosas bien',1,'no transversal');
INSERT INTO "Objetivos" (descripcion,"idProducto",transversal) VALUES ('divertirnos en grande',1,'transversal');
INSERT INTO "Objetivos" (descripcion,"idProducto",transversal) VALUES ('commer pizza con cada sprint',1,'no transversal');
INSERT INTO "Objetivos" (descripcion,"idProducto",transversal) VALUES ('usar extreme programing de forma cuidadosa',1,'no transversal');
INSERT INTO "Objetivos" (descripcion,"idProducto",transversal) VALUES ('crear muchos muchos objetivos',1,'no transversal');
INSERT INTO "Objetivos" (descripcion,"idProducto",transversal) VALUES ('usar este software para beneficio propio',1,'transversal');

INSERT INTO "Objetivos" (descripcion,"idProducto",transversal) VALUES ('En tanto que hagamos codigo lo continuemos2',2,'no transversal');
INSERT INTO "Objetivos" (descripcion,"idProducto",transversal) VALUES ('En tanto que todos nos divirtamos todo sera divertido2',2,'transversal');
INSERT INTO "Objetivos" (descripcion,"idProducto",transversal) VALUES ('En tanto que jejeps todos huehuehue2',2,'no transversal');
INSERT INTO "Objetivos" (descripcion,"idProducto",transversal) VALUES ('En tanto que escribo esto nabil hace prod.py2',2,'no transversal');
INSERT INTO "Objetivos" (descripcion,"idProducto",transversal) VALUES ('En tanto que probamos la base de datos aprendemos2',2,'no transversal');
INSERT INTO "Objetivos" (descripcion,"idProducto",transversal) VALUES ('En tanto que jejeps todos huehuehue2',2,'transversal');

INSERT INTO "Historias" (codigo,"idProducto","idAccion",tipo,prioridad) VALUES ('Historia1',1,3,'opcional',1);
INSERT INTO "Historias" (codigo,"idProducto","idAccion",tipo,prioridad) VALUES ('Historia2',1,2,'obligatoria',4);
INSERT INTO "Historias" (codigo,"idProducto","idAccion",tipo,prioridad) VALUES ('Historia3',1,1,'opcional',9);
INSERT INTO "Historias" (codigo,"idProducto","idAccion",tipo,prioridad) VALUES ('Podria escribir algo interesante y decir que todos tienen parciales esta semana y yo no :)',2,3,'obligatoria',15);
INSERT INTO "Historias" (codigo,"idProducto","idAccion",tipo,prioridad) VALUES ('Ellos estudian y yo hago esto D:',2,2,'opcional',12);
INSERT INTO "Historias" (codigo,"idProducto","idAccion",tipo,prioridad) VALUES ('Eso no me hace vaga o si?',2,1,'obligatoria',20);

INSERT INTO "ObjetivosHistorias" ("idHistoria","idObjetivo") VALUES (1,1);
INSERT INTO "ObjetivosHistorias" ("idHistoria","idObjetivo") VALUES (3,2);
INSERT INTO "ObjetivosHistorias" ("idHistoria","idObjetivo") VALUES (1,3);
INSERT INTO "ObjetivosHistorias" ("idHistoria","idObjetivo") VALUES (2,1);
INSERT INTO "ObjetivosHistorias" ("idHistoria","idObjetivo") VALUES (3,1);
INSERT INTO "ObjetivosHistorias" ("idHistoria","idObjetivo") VALUES (3,3);
INSERT INTO "ObjetivosHistorias" ("idHistoria","idObjetivo") VALUES (1,4);
INSERT INTO "ObjetivosHistorias" ("idHistoria","idObjetivo") VALUES (1,5);
INSERT INTO "ObjetivosHistorias" ("idHistoria","idObjetivo") VALUES (1,6);
INSERT INTO "ObjetivosHistorias" ("idHistoria","idObjetivo") VALUES (3,4);
INSERT INTO "ObjetivosHistorias" ("idHistoria","idObjetivo") VALUES (2,5);
INSERT INTO "ObjetivosHistorias" ("idHistoria","idObjetivo") VALUES (2,6);

INSERT INTO "ObjetivosHistorias" ("idHistoria","idObjetivo") VALUES (4,7);
INSERT INTO "ObjetivosHistorias" ("idHistoria","idObjetivo") VALUES (4,8);
INSERT INTO "ObjetivosHistorias" ("idHistoria","idObjetivo") VALUES (5,9);
INSERT INTO "ObjetivosHistorias" ("idHistoria","idObjetivo") VALUES (6,7);
INSERT INTO "ObjetivosHistorias" ("idHistoria","idObjetivo") VALUES (5,8);
INSERT INTO "ObjetivosHistorias" ("idHistoria","idObjetivo") VALUES (6,9);
INSERT INTO "ObjetivosHistorias" ("idHistoria","idObjetivo") VALUES (5,10);
INSERT INTO "ObjetivosHistorias" ("idHistoria","idObjetivo") VALUES (4,11);
INSERT INTO "ObjetivosHistorias" ("idHistoria","idObjetivo") VALUES (4,12);
INSERT INTO "ObjetivosHistorias" ("idHistoria","idObjetivo") VALUES (6,10);
INSERT INTO "ObjetivosHistorias" ("idHistoria","idObjetivo") VALUES (5,11);
INSERT INTO "ObjetivosHistorias" ("idHistoria","idObjetivo") VALUES (6,12);

INSERT INTO "ActoresHistorias" ("idHistoria","idActor") VALUES (1,1);
INSERT INTO "ActoresHistorias" ("idHistoria","idActor") VALUES (3,3);
INSERT INTO "ActoresHistorias" ("idHistoria","idActor") VALUES (1,2);
INSERT INTO "ActoresHistorias" ("idHistoria","idActor") VALUES (2,2);
INSERT INTO "ActoresHistorias" ("idHistoria","idActor") VALUES (3,1);
INSERT INTO "ActoresHistorias" ("idHistoria","idActor") VALUES (2,3);
INSERT INTO "ActoresHistorias" ("idHistoria","idActor") VALUES (4,5);
INSERT INTO "ActoresHistorias" ("idHistoria","idActor") VALUES (4,6);
INSERT INTO "ActoresHistorias" ("idHistoria","idActor") VALUES (5,4);
INSERT INTO "ActoresHistorias" ("idHistoria","idActor") VALUES (5,5);
INSERT INTO "ActoresHistorias" ("idHistoria","idActor") VALUES (6,4);
INSERT INTO "ActoresHistorias" ("idHistoria","idActor") VALUES (6,6);
