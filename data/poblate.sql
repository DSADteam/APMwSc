
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

INSERT INTO "Acciones" VALUES (1,'Crear repositorio',1);
INSERT INTO "Acciones" VALUES (2,'Documentar todo',1);

INSERT INTO "Acciones" VALUES (3,'Crear repositorio divertido',2);
INSERT INTO "Acciones" VALUES (4,'Documentar tablas',2);

INSERT INTO "Acciones" VALUES (5,'Crear repositorio volador',3);
INSERT INTO "Acciones" VALUES (6,'Documentar cosas',3);

INSERT INTO "Actores" (nombre,descripcion,"idProducto") VALUES ('Developer','Desarrolador de proyecto',1);
INSERT INTO "Actores" (nombre,descripcion,"idProducto") VALUES ('Scrum Master','Guia del grupo',1);
INSERT INTO "Actores" (nombre,descripcion,"idProducto") VALUES ('Product Owner','Dueno del producto',1);

INSERT INTO "Actores" (nombre,descripcion,"idProducto") VALUES ('Developer','Desarrolador de proyecto',2);
INSERT INTO "Actores" (nombre,descripcion,"idProducto") VALUES ('Scrum Master','Guia del grupo',2);
INSERT INTO "Actores" (nombre,descripcion,"idProducto") VALUES ('Product Owner','Dueno del producto',2);

INSERT INTO "Actores" (nombre,descripcion,"idProducto") VALUES ('Developer','Desarrolador de proyecto',3);
INSERT INTO "Actores" (nombre,descripcion,"idProducto") VALUES ('Scrum Master','Guia del grupo',3);
INSERT INTO "Actores" (nombre,descripcion,"idProducto") VALUES ('Product Owner','Dueno del producto',3);

INSERT INTO "Objetivos" VALUES (1,'En tanto que hagamos codigo lo continuemos',1);
INSERT INTO "Objetivos" VALUES (2,'En tanto que todos nos divirtamos todo sera divertido',1);
INSERT INTO "Objetivos" VALUES (3,'En tanto que jejeps todos huehuehue',1);
INSERT INTO "Objetivos" VALUES (4,'En tanto que escribo esto nabil hace prod.py',2);
INSERT INTO "Objetivos" VALUES (5,'En tanto que probamos la base de datos aprendemos',2);
INSERT INTO "Objetivos" VALUES (6,'En tanto que jejeps todos huehuehue',2);
