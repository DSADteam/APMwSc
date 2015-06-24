from flask import Flask, request, session
from flask.ext.script import Manager, Server
from random import SystemRandom
from datetime import timedelta
import os
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, ForeignKey

from flask.ext.migrate import Migrate, MigrateCommand
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, PrimaryKeyConstraint, UniqueConstraint, Sequence

app = Flask(__name__, static_url_path='')
manager = Manager(app)
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '127.0.0.1')
)

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=45)
    session.modified = True

@app.route('/')
def root():
    session.pop("idPila", None)
    return app.send_static_file('index.html')

@manager.command
def createdb():
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import create_engine
    from sqlalchemy.engine.url import URL
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(URL(**app.config['DATABASE']))
    db.metadata.drop_all(engine)
    db.metadata.create_all(engine)

    DBSession = sessionmaker(bind = engine)
    session = DBSession()


#Application code starts here

app.config['DATABASE'] = {
            'drivername': 'postgres',
            'host': 'localhost',
            'port': '5432',
            'username': 'apmwsc',
            'password': 'safepassword',
            'database': 'apmwsc'
            }

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

engine = create_engine(URL(**app.config['DATABASE']))
DBSession = sessionmaker(bind = engine)
sessionDB = DBSession()

#Clase para pila de productos

class Producto(db.Model):
    
    __tablename__ = 'Productos'
    idProducto    = db.Column(Integer, primary_key = True) #autoincremento
    nombre        = db.Column(String(500),  unique = True, nullable = False)
    descripcion   = db.Column(String(500),  unique = False)
    escala        = db.Column(String(14),nullable = False)

    def __init__(self,nombre,escala,descripcion=None):
        
        self.nombre      = nombre
        self.descripcion = descripcion
        self.escala      = escala
        
    def getALL(self):
        
        return engine.execute("select * from \"Products\";")

# Clase Accion

class Accion(db.Model):
    
    __tablename__ = 'Acciones'
    idAccion      = db.Column(Integer, primary_key = True)
    descripcion   = db.Column(String(500), unique = False, nullable=False)
    idProducto    = db.Column(Integer, db.ForeignKey('Productos.idProducto'))
    producto      = db.relationship('Producto', backref = db.backref('acciones', lazy = 'dynamic'))
    
    ''' Metodo init
        Constructor de accion
    ''' 
    
    def __init__(self, descripcion, idProducto):
        
        self.descripcion = descripcion
        self.idProducto  = idProducto

# Clase Actor

class Actor(db.Model):
    
    __tablename__ = 'Actores'
    idActor       = db.Column(Integer    , primary_key = True)
    nombre        = db.Column(String(50) , unique = False, nullable=False)
    descripcion   = db.Column(String(500), unique = False, nullable=False)
    idProducto    = db.Column(Integer, db.ForeignKey('Productos.idProducto'))
    producto      = db.relationship('Producto', backref = db.backref('actores', lazy = 'dynamic'))
    
    ''' Metodo init
        Constructor del actor
    ''' 
    
    def __init__(self, nombre, descripcion, idProducto):
        
        self.nombre      = nombre
        self.descripcion = descripcion
        self.idProducto  = idProducto

    def getALL(self):
        
        return engine.execute("select * from \"Actores\";")
     
# Clase Objetivo

class Objetivo(db.Model):
    
    __tablename__ = 'Objetivos'
    idObjetivo    = db.Column(Integer, primary_key = True)
    descripcion   = db.Column(String(500), unique = False, nullable=False)
    idProducto    = db.Column(Integer, db.ForeignKey('Productos.idProducto'))
    transversal   = db.Column(String(15), unique = False, nullable=False)
    producto      = db.relationship('Producto', backref = db.backref('objetivos', lazy = 'dynamic'))
    
    ''' Metodo init
        Constructor del objetivo
    ''' 
    
    def __init__(self,descripcion, idProducto, transversal):
        
        self.descripcion = descripcion
        self.idProducto  = idProducto
        self.transversal = transversal

# Class User, used at login for now.

class dbuser(db.Model):
    
    __tablename__ = 'dbuser'
    fullname      = Column(String(50))
    username      = Column(String(16), primary_key = True)
    password      = Column(String(100)) #para que pueda aceptar hash
    email         = Column(String(30))
    idActor       = Column(Integer, ForeignKey('Actores.idActor'))
    
    ''' Metodo init
        Constructor del usuario
    ''' 
    
    def __init__(self, fullname, username, password, email, idActor):
        
        self.fullname = fullname
        self.username = username
        self.password = password
        self.email    = email
        self.idActor  = idActor
     
# Clase historias de usuarios
   
class Historia(db.Model):
    
    __tablename__   = 'Historias'
    idHistoria      = db.Column(Integer, primary_key = True)
    codigo          = db.Column(String(500), unique = False, nullable=False)
    tipo            = db.Column(String(15), nullable=False)
    idProducto      = db.Column(Integer, db.ForeignKey('Productos.idProducto'), unique = False, nullable=False)
    idAccion        = db.Column(Integer, db.ForeignKey('Acciones.idAccion'), nullable=True)
    idHistoriaPadre = db.Column(Integer, db.ForeignKey('Historias.idHistoria'), unique = False, nullable=True)
    prioridad       = db.Column(Integer, unique = False,nullable=False) #Del 1 al 20

    #accion          = db.relationship('Acciones',   backref = db.backref('accion'   , lazy = 'dynamic'))
    #producto        = db.relationship('Productos', backref = db.backref('producto', lazy = 'dynamic'))
    #historia   = db.relationship('Historias', backref = db.backref('historia', lazy = 'dynamic'))

    ''' Metodo init
        Constructor de las historias de usuarios
    ''' 

    def __init__(self,codigo, idProducto,idAccion,tipo,peso,prioridad,idHistoriaPadre=None):
        self.codigo      = codigo
        self.idProducto  = idProducto
        self.idAccion    = idAccion
        self.tipo        = tipo
        if idHistoriaPadre:
            self.idHistoriaPadre = idHistoriaPadre
        self.prioridad=prioridad
        
# Clase para objetivos de una historia

class ObjetivosHistoria(db.Model):

    __tablename__ = 'ObjetivosHistorias'
    idHistoria    = db.Column(Integer, db.ForeignKey('Historias.idHistoria'), unique = False, primary_key=True)
    idObjetivo    = db.Column(Integer, db.ForeignKey('Objetivos.idObjetivo'), unique = False, primary_key=True)   


    ''' Metodo init
        Constructor de Objetivos asociados a Historias
    ''' 
    
    def __init__(self,idHistoria,idObjetivo):

        self.idHistoria = idHistoria
        self.idObjetivo = idObjetivo

# Clase para actores de una historia

class ActoresHistoria(db.Model):

    __tablename__   = 'ActoresHistorias'
    idHistoria      = db.Column(Integer, db.ForeignKey('Historias.idHistoria'), unique = False, primary_key=True)
    idActor         = db.Column(Integer, db.ForeignKey('Actores.idActor'),     unique = False,  primary_key=True)


    ''' Metodo init
        Constructor de Actores asociados a Historias
    ''' 
    
    def __init__(self,idHistoria,idActor):
        
        self.idHistoria = idHistoria
        self.idActor    = idActor

class Tarea(db.Model):
    
    __tablename__    = 'Tareas'
    idTarea          = db.Column(Integer, primary_key = True)
    descripcion      = db.Column(String(500), unique = False, nullable=False)
    idHistoria       = db.Column(Integer, db.ForeignKey('Historias.idHistoria'), unique = False, primary_key=True)
    nombreCategoria  = db.Column(String(100), db.ForeignKey('Categorias.nombreCategoria'), unique = False)
    peso             = db.Column(Integer, nullable=False)
    ''' Metodo init
        Constructor de Tareas de una historia
    ''' 
    
    def __init__(self,descripcion,idHistoria,nombreCategoria,peso):
        
        self.descripcion = descripcion
        self.idHistoria  = idHistoria
        self.nombreCategoria  = nombreCategoria
        self.peso  = peso



class Categoria(db.Model):
    
    __tablename__    = 'Categorias'
    idCategoria      = db.Column(Integer,   primary_key = True)
    nombreCategoria  = db.Column(String(50),unique      = True,nullable=False)
    peso             = db.Column(Integer,   nullable    = False)
    
    
    ''' Metodo init
        Constructor de Categorias de Tareas
    ''' 
    
    def __init__(self,nombreCategoria,peso):
        
        self.nombreCategoria = nombreCategoria
        self.peso  = peso

from app.scrum.ident import ident
app.register_blueprint(ident)
from app.scrum.prod import prod
app.register_blueprint(prod)
from app.scrum.mast import mast
app.register_blueprint(mast)
from app.scrum.dev import dev
app.register_blueprint(dev)
from app.scrum.actor import actor
app.register_blueprint(actor)
from app.scrum.objetivo import objetivo
app.register_blueprint(objetivo)
from app.scrum.accion import accion
app.register_blueprint(accion)
from app.scrum.historias import historias
app.register_blueprint(historias)
from app.scrum.tareas import tareas
app.register_blueprint(tareas)
from app.scrum.cates import cates
app.register_blueprint(cates)

if __name__ == '__main__':
    app.config.update(
      SECRET_KEY = repr(SystemRandom().random())
    )
    manager.run()