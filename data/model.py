import os
import data.settings
from flask import Flask
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, PrimaryKeyConstraint, UniqueConstraint, Sequence



db = declarative_base()


"""
    Entidad producto y relaciones afines 
"""
#Clase para pila de productos
class product(db):
    __tablename__ = 'Products'
    idproduct     = Column(Integer, primary_key = True) #autoincremento
    description   = Column(String(255),  unique = True)

    #Backrefs
    # roles      = relationship('ProductRoles'     ,backref='Products')
    # actions    = relationship('ProductActions'   ,backref='Products')
    # objectives = relationship('ProductObjectives',backref='Products')

    def __init__(self,description):
        #self.idproduct   = idproduct
        self.description = description


#Clase para relacion 1 a muchos entre productos y roles(actores) 
class productRoles(db):
    __tablename__ = 'ProductRoles'
    idproduct     = Column(Integer, ForeignKey('Products.idproduct'))    
    idrole        = Column(Integer, nullable=False)                     #Sustituir
    #idrole        = Column(Integer, ForeignKey('idrole.role'))         #Agregar despues de crear las otras db
    __table_args__= (
                        PrimaryKeyConstraint("idproduct","idrole"),
                        UniqueConstraint("idproduct","idrole")
                    )

    def __init__(self,idproduct,idrole):
        self.idproduct  = idproduct
        self.idrole     = idrole

#Clase para relacion 1 a muchos entre productos y acciones
class productActions(db):
    __tablename__ = 'ProductActions'
    idproduct     = Column(Integer, ForeignKey('Products.idproduct'))
    idaction      = Column(Integer, nullable=False)                 #Sustituir
    #idaction      = Column(Integer, ForeignKey('idaction.action')) #Agregar despues de crear las otras db
    __table_args__= (
                      PrimaryKeyConstraint("idproduct","idaction"),
                      UniqueConstraint("idproduct","idaction")
                    )


    def __init__(self,idproduct,idaccion):
        self.idproduct   = idproduct
        self.idaction = idaction

#Clase para relacion 1 a muchos entre productos y objetivos
class productObjectives(db):
    __tablename__ = 'ProductObjectives'
    idproduct     = Column(Integer, ForeignKey('Products.idproduct'))
    idobjective   = Column(Integer, nullable=False)                       #Sustituir
    #idobjective   = Column(Integer, ForeignKey('idobjective.objective')) #Agregar despues de crear las otras db
    __table_args__= (
                        PrimaryKeyConstraint("idproduct","idobjective"),
                        UniqueConstraint("idproduct","idobjective")
                    )

    def __init__(self,idproduct,idobjective):
        self.idproduct   = idproduct
        self.idobjective = idobjective



def main():
    engine = create_engine(URL(**data.settings.DATABASE))
    db.metadata.drop_all(engine)
    db.metadata.create_all(engine)

    DBSession = sessionmaker(bind = engine)
    session = DBSession()
    for i in range(1,5):
        mensaje = "Soy el producto "+ str(i)
        producto = product(description=mensaje)
        session.add(producto)
        session.commit()

if __name__ == "__main__":
   main()