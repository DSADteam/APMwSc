from flask import Flask, request, session
from flask.ext.script import Manager, Server
from random import SystemRandom
from datetime import timedelta
import os
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, ForeignKey

from flask.ext.migrate import Migrate, MigrateCommand
####
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

#



@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=45)
    session.modified = True

@app.route('/')
def root():
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
    idProducto  = db.Column(Integer, primary_key = True) #autoincremento
    nombre      = db.Column(String(500),  unique = True, nullable = False)
    descripcion = db.Column(String(500),  unique = False)

    #Backrefs
    # roles      = relationship('ProductRoles'     ,backref='Products')
    # actions    = relationship('ProductActions'   ,backref='Products')
    # objectives = relationship('ProductObjectives',backref='Products')

    def __init__(self,nombre,descripcion=None):
        self.nombre = nombre
        self.descripcion = descripcion
        
    def getALL(self):
        return engine.execute("select * from \"Products\";")

# Clase Accion

class Accion(db.Model):
    
    __tablename__ = 'Acciones'
    idAccion      = db.Column(db.Integer, primary_key = True)
    descripcion   = db.Column(db.String(500), unique = False, nullable=False)
    idProducto    = db.Column(db.Integer, db.ForeignKey('Productos.idProducto'))
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
    idActor       = db.Column(db.Integer    , primary_key = True)
    nombre        = db.Column(db.String(50) , unique = False, nullable=False)
    descripcion   = db.Column(db.String(500), unique = False)
    idProducto    = db.Column(db.Integer, db.ForeignKey('Productos.idProducto'))
    producto      = db.relationship('Producto', backref = db.backref('actores', lazy = 'dynamic'))
    ''' Metodo init
        Constructor del actor
    ''' 
    
    def __init__(self, nombre, descripcion, idProducto):
        self.nombre      = nombre
        self.descripcion = descripcion
        self.idProducto  = idProducto
     
# Clase Usuario

class Objetivo(db.Model):
    __tablename__ = 'Objetivos'
    idObjetivo    = db.Column(db.Integer, primary_key = True)
    descripcion   = db.Column(db.String(500), unique = False, nullable=False)
    idProducto    = db.Column(db.Integer, db.ForeignKey('Productos.idProducto'))
    producto      = db.relationship('Producto', backref = db.backref('objetivos', lazy = 'dynamic'))
    
    ''' Metodo init
        Constructor del objetivo
    ''' 
    
    def __init__(self, idObjetivo, descripcion, idProducto):
        self.idObjetivo  = idObjetivo
        self.descripcion = descripcion
        self.idProducto  = idProducto

# Class User, used at login for now.

class dbuser(db.Model):
    
    __tablename__ = 'dbuser'
    fullname = Column(String(50))
    username = Column(String(16), primary_key = True)
    password = Column(String(100)) #para que pueda aceptar hash
    email = Column(String(30))
    idActor = Column(Integer, ForeignKey('Actores.idActor'))
    
    ''' Metodo init
        Constructor del usuario
    ''' 
    
    def __init__(self, fullname, username, password, email, idActor):
        
        self.fullname = fullname
        self.username = username
        self.password = password
        self.email = email
        self.iddpt = iddpt 
        self.idActor = idActor


if __name__ == '__main__':
    app.config.update(
      SECRET_KEY = repr(SystemRandom().random())
    )
    manager.run()

