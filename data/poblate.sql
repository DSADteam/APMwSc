
INSERT INTO "Productos" (nombre,descripcion,escala) VALUES ('Proyecto APMwSc','Metere la cadena de software','cualitativo');
INSERT INTO "Productos" (nombre,descripcion,escala) VALUES ('Surfeadores divertido','De pana que si','cualitativo');
INSERT INTO "Productos" (nombre,descripcion,escala) VALUES ('Piedreros asociados','Adoro esta materia','cuantitativo');
INSERT INTO "Productos" (nombre,descripcion,escala) VALUES ('Ingenieria de software','Ojala la abrieran todos los trimestres','cuantitativo');

INSERT INTO "Acciones" (descripcion,"idProducto") VALUES ('Crear repositorio',1);
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

INSERT INTO "Objetivos" (descripcion,"idProducto",transversal) VALUES ('En tanto que hagamos codigo lo continuemos',1,'no transversal');
INSERT INTO "Objetivos" (descripcion,"idProducto",transversal) VALUES ('En tanto que todos nos divirtamos todo sera divertido',1,'transversal');
INSERT INTO "Objetivos" (descripcion,"idProducto",transversal) VALUES ('En tanto que jejeps todos huehuehue',1,'transversal');
INSERT INTO "Objetivos" (descripcion,"idProducto",transversal) VALUES ('En tanto que escribo esto nabil hace prod.py',2,'no transversal');
INSERT INTO "Objetivos" (descripcion,"idProducto",transversal) VALUES ('En tanto que probamos la base de datos aprendemos',2,'no transversal');
INSERT INTO "Objetivos" (descripcion,"idProducto",transversal) VALUES ('En tanto que jejeps todos huehuehue',2,'transversal');

INSERT INTO "Historias" (codigo,"idProducto","idAccion",tipo) VALUES ('Historia1',1,3,'tipo 3');
INSERT INTO "Historias" (codigo,"idProducto","idAccion",tipo) VALUES ('Historia2',1,2,'tipo 2');
INSERT INTO "Historias" (codigo,"idProducto","idAccion",tipo) VALUES ('Historia3',1,1,'tipo 1');
INSERT INTO "Historias" (codigo,"idProducto","idAccion",tipo) VALUES ('Podria escribir algo interesante y decir que todos tienen parciales esta semana y yo no :)',2,3,'tipo 3');
INSERT INTO "Historias" (codigo,"idProducto","idAccion",tipo) VALUES ('Ellos estudian y yo hago esto D:',2,2,'tipo 2');
INSERT INTO "Historias" (codigo,"idProducto","idAccion",tipo) VALUES ('Eso no me hace vaga o si?',2,1,'tipo 1');

