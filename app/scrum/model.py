'''
Created on May 6, 2015

@author: Meggie y Cristina
'''

import os

import settings

from flask import Flask

from flask.ext.sqlalchemy import SQLAlchemy

from sqlalchemy.engine.url import URL

from sqlalchemy.orm import relationship, backref

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey

db = declarative_base()

# Clase Producto

class Producto(db):
    
    __tablename__ = 'Productos'
    idPila = Column(Integer, primary_key = True)
    descripcion = Column(String(500), unique = True)
    productos1 = relationship('Productos', backref = 'Acciones')
    productos2 = relationship('Productos', backref = 'Objetivos')
    productos3 = relationship('Productos', backref = 'Actores')
    
    ''' Metodo init
        Constructor del producto
    ''' 
    
    def __init__(self, idPila, descripcion):
        
        self.idPila = idPila
        self.descripcion = descripcion

# Clase Accion

class Accion(db):
    
    __tablename__ = 'Acciones'
    idAccion = Column(Integer, primary_key = True)
    descripcion = Column(String(500), unique = True)
    idPila = Column(Integer, ForeignKey('Productos.idPila'))
    
    ''' Metodo init
        Constructor de accion
    ''' 
    
    def __init__(self, idAccion, descripcion, idPila):
        
        self.idAccion = idAccion
        self.descripcion = descripcion
        self.idPila = idPila

# Clase Actor

class Actor(db):
    
    __tablename__ = 'Actores'
    idActor = Column(Integer, primary_key = True)
    nombre = Column(String(50), unique = True)
    descripcion = Column(String(500), unique = True)
    idPila = Column(Integer, ForeignKey('Productos.idPila'))
    
    ''' Metodo init
        Constructor del actor
    ''' 
    
    def __init__(self, idActor, nombre, descripcion, idPila):
        
        self.idActor = idActor
        self.nombre = nombre
        self.descripcion = descripcion
        self.idPila = idPila
     
# Clase Usuario

class Objetivo(db):
    
    __tablename__ = 'Objetivos'
    idObjetivo = Column(Integer, primary_key = True)
    descripcion = Column(String(500), unique = True)
    idPila = Column(Integer, ForeignKey('Productos.idPila'))
    
    ''' Metodo init
        Constructor del objetivo
    ''' 
    
    def __init__(self, idObjetivo, descripcion, idPila):
        
        self.idObjetivo = idObjetivo
        self.descripcion = descripcion
        self.idPila = idPila

engine = create_engine(URL(**settings.DATABASE))

db.metadata.drop_all(engine)
db.metadata.create_all(engine)