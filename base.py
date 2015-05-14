from flask import Flask, request, session
from flask.ext.script import Manager, Server
from random import SystemRandom
from datetime import timedelta
import os
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, ForeignKey

from flask.ext.migrate import Migrate, MigrateCommand

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
    return app.send_static_file('index.html')

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

class Producto(db.Model):
    
    __tablename__ = 'Productos'
    idPila = db.Column(db.Integer, primary_key = True)
    descripcion = db.Column(db.String(500), unique = True)
    
    
    
    ''' Metodo init
        Constructor del producto
    ''' 
    
    def __init__(self, idPila, descripcion):
        
        self.idPila = idPila
        self.descripcion = descripcion

# Clase Accion

class Accion(db.Model):
    
    __tablename__ = 'Acciones'
    idAccion = db.Column(db.Integer, primary_key = True)
    descripcion = db.Column(db.String(500), unique = True)
    idPila = db.Column(db.Integer, db.ForeignKey('Productos.idPila'))
    producto = db.relationship('Producto', backref = db.backref('acciones', lazy = 'dynamic'))
    
    ''' Metodo init
        Constructor de accion
    ''' 
    
    def __init__(self, idAccion, descripcion, idPila):
        
        self.idAccion = idAccion
        self.descripcion = descripcion
        self.idPila = idPila

# Clase Actor

class Actor(db.Model):
    
    __tablename__ = 'Actores'
    idActor = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50), unique = True)
    descripcion = db.Column(db.String(500), unique = True)
    idPila = db.Column(db.Integer, db.ForeignKey('Productos.idPila'))
    producto = db.relationship('Producto', backref = db.backref('actores', lazy = 'dynamic'))
    ''' Metodo init
        Constructor del actor
    ''' 
    
    def __init__(self, idActor, nombre, descripcion, idPila):
        
        self.idActor = idActor
        self.nombre = nombre
        self.descripcion = descripcion
        self.idPila = idPila
     
# Clase Usuario

class Objetivo(db.Model):
    
    __tablename__ = 'Objetivos'
    idObjetivo = db.Column(db.Integer, primary_key = True)
    descripcion = db.Column(db.String(500), unique = True)
    idPila = db.Column(db.Integer, db.ForeignKey('Productos.idPila'))
    producto = db.relationship('Producto', backref = db.backref('objetivos', lazy = 'dynamic'))
    
    ''' Metodo init
        Constructor del objetivo
    ''' 
    
    def __init__(self, idObjetivo, descripcion, idPila):
        
        self.idObjetivo = idObjetivo
        self.descripcion = descripcion
        self.idPila = idPila

#Application code ends here

if __name__ == '__main__':
    app.config.update(
      SECRET_KEY = repr(SystemRandom().random())
    )
    manager.run()
