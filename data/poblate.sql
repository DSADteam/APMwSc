
-- 
-- INSERT INTO "Users" VALUES('Javier'      ,'javierlopm' ,'holahola1','javier@correo.com'  ,1,1);
-- INSERT INTO "Users" VALUES('Nabil'       ,'nabilj'     ,'holahola2','nabil@correo.com'   ,2,1);
-- INSERT INTO "Users" VALUES('Cristina'    ,'cristinab'  ,'holahola3','cristina@correo.com',3,1);
-- INSERT INTO "Users" VALUES('Samuel'      ,'samuel'     ,'holahola4','samuel@correo.com'  ,1,1);
-- INSERT INTO "Users" VALUES('Roberto'     ,'robertor'   ,'holahola5','roberto@correo.com' ,2,1);
-- INSERT INTO "Users" VALUES('Meggie'      ,'meggies'    ,'holahola6','meggie@correo.com'  ,3,1);
-- INSERT INTO "Users" VALUES('Ascander'    ,'ascander'   ,'holahola7','ascander@correo.com',1,3);
-- INSERT INTO "Users" VALUES('Jean Carlos' ,'jeanc'      ,'holahola8','jeanc@correo.com'   ,2,2);

INSERT INTO "Productos" (nombre,descripcion) VALUES ('Proyecto APMwSc','Metere la cadena de software');
INSERT INTO "Productos" (nombre,descripcion) VALUES ('Surfeadores divertido','De pana que si');
INSERT INTO "Productos" (nombre,descripcion) VALUES ('Piedreros asociados','Adoro esta materia');
INSERT INTO "Productos" (nombre,descripcion) VALUES ('Ingenieria de software','Ojala la abrieran todos los trimestres');

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

INSERT INTO "Objetivos" (descripcion,"idProducto") VALUES ('En tanto que hagamos codigo lo continuemos',1);
INSERT INTO "Objetivos" (descripcion,"idProducto") VALUES ('En tanto que todos nos divirtamos todo sera divertido',1);
INSERT INTO "Objetivos" (descripcion,"idProducto") VALUES ('En tanto que jejeps todos huehuehue',1);
INSERT INTO "Objetivos" (descripcion,"idProducto") VALUES ('En tanto que escribo esto nabil hace prod.py',2);
INSERT INTO "Objetivos" (descripcion,"idProducto") VALUES ('En tanto que probamos la base de datos aprendemos',2);
INSERT INTO "Objetivos" (descripcion,"idProducto") VALUES ('En tanto que jejeps todos huehuehue',2);

INSERT INTO "Historias" (descripcion,"idProducto") VALUES ('Historia1',1);
INSERT INTO "Historias" (descripcion,"idProducto") VALUES ('Historia2',1);
INSERT INTO "Historias" (descripcion,"idProducto") VALUES ('Historia3',1);
INSERT INTO "Historias" (descripcion,"idProducto") VALUES ('Podria escribir algo interesante y decir que todos tienen parciales esta semana y yo no :)',2);
INSERT INTO "Historias" (descripcion,"idProducto") VALUES ('Ellos estudian y yo hago esto D:',2);
INSERT INTO "Historias" (descripcion,"idProducto") VALUES ('Eso no me hace vaga o si?',2);

