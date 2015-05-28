# -*- coding: utf-8 -*-

#Agregando proyect root
import sys
import os
dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../..'))
sys.path.append(dir)

#Dependencias flask
from flask import request, session, Blueprint, json
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import text

#Definicion de blueprint y bd
actor = Blueprint('actor', __name__)
from base import *

@actor.route('/actor/ACrearActor', methods=['POST'])
def ACrearActor():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Actor creado']}, {'label':'/VCrearActor', 'msg':['Error al crear actor']}, ]
    res = results[0]


    idPila = str(session['idPila'])

    act=clsActor(session=sessionDB,engine=engine)
    act.insertar(nombre=params['nombre'],descripcion=params['descripcion'],idProducto=idPila)
    res['label'] = res['label'] + '/' + idPila

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@actor.route('/actor/AModifActor', methods=['POST'])
def AModifActor():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Actor actualizado']}, {'label':'/VActor', 'msg':['Error al modificar actor']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    idActor = params['idActor']
    
    act=clsActor(session=sessionDB,engine=engine)
    act.modificar(idActor,params['nombre'],params['descripcion'])
    
    res['label'] = res['label'] + '/' + str(session['idPila'])

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@actor.route('/actor/VActor')
def VActor():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structur
    act=clsActor(engine=engine,session=sessionDB)


    idActor        = request.args.get('idActor', 1)
    res['idActor'] = idActor
    res['fActor']  = act.mostrarActor(idActor)

    #Action code ends here
    return json.dumps(res)



@actor.route('/actor/VCrearActor')
def VCrearActor():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    res['idPila'] = session['idPila']

    #Action code ends here
    return json.dumps(res)

#Use case code starts here

class clsActor():
    
    def __init__(self,engine=None,session=None):
        
        self.engine  = engine
        self.session = session
        
    def insertar(self,nombre=None,descripcion=None,idProducto=None):
   
        if type(nombre) is int:
            return (False)
        if type(descripcion) is int:
            return (False)
        if type(idProducto) is str:
            return (False)


       
        comentarioNulo = (nombre == None) or (descripcion == None) or\
        (idProducto==None) or (nombre == '') or (descripcion == '') 
        if comentarioNulo:
            return False

        #estaEnBd       = self.existeActor(nombre=nombre)
        
        producto = self.session.query(Producto).filter(Producto.idProducto == idProducto)
        existeProducto = producto.count() > 0

        longCharValido = (len(nombre) <= 50) and (len(descripcion) <= 500)

        if (longCharValido) and (not comentarioNulo) and existeProducto:
            newAct = Actor(nombre,descripcion,idProducto)
            self.session.add(newAct)
            self.session.commit()
            return True
        else:
            return False
        
    def existeActor(self,nombre=None,descripcion=None):
        # No veo esto necesario, no en existe... solo en insertar
        nombreStr   = (type(nombre) is str)      or nombre==None
        descriptStr = (type(descripcion) is str) or descripcion==None
        
        if(nombreStr and descriptStr):
            pass
        else:
            return False

        if(nombre!=None and descripcion==None):
            result = self.session.query(Actor).filter(Actor.nombre == nombre)
        elif(nombre==None and descripcion!=None):
            result = self.session.query(Actor).filter(Actor.descripcion == descripcion)
        elif(nombre!=None and descripcion!=None):
            result = self.session.query(Actor).filter(Actor.nombre == nombre).filter(Actor.descripcion == descripcion)
        else:
            return False

        return result.count() > 0


    def mostrarActor(self,idActor):
        result = self.session.query(Actor).filter(Actor.idActor == idActor)
        print("Este es el resultado ")
        print(result)
        if result!="":
            for row in result:
                res = {'nombre':row.nombre,'idActor':row.idActor,'descripcion':row.descripcion}
            else:
                print("Empty query!")
        return res

    
    def listarActores(self):
        
        res = []
        result = self.engine.execute("select * from \"Actores\";")
        if result!="":
            for row in result:
                res.append({'nombre':row.nombre,'idActor':row.idActor,'descripcion':row.descripcion})
            else:
                print("Empty query!")
        
        return res
                
    def listarActoresprod(self,idProducto):
        
        res = []
        #result = self.engine.execute("select * from \"Actores\" where \'idProducto\'="+str(idProducto)+" ;")
        result = self.session.query(Actor).filter(Actor.idProducto == idProducto)
        if result!="":
            for row in result:
                res.append({'idActor':row.idActor,'nombre':row.nombre,'descripcion':row.descripcion})
            else:
                print("Empty query!")
        
        return res

    def borrarFilas(self):
        
        self.session.query(Actor).delete()
        self.session.commit()
    
    def getProdId(self,idActor):
        
        result = self.session.query(Actor).filter(Actor.idActor == idActor)
        for row in result:
            x=row.idProducto
        return x

    #Funcion que permite actualizar un nombre y descripcion
    def modificar(self,id=None,nombre=None,descripcion=None):
        
        if(id==None):
            return False
        if type(id) is str:
            return False
        if type(nombre) is int:
            return False
        if type(descripcion) is int:
            return False
        
        if(id!=None):
            result = self.session.query(Actor).filter(Actor.idActor == id)
            
        if ((result.count()>0) and nombre and descripcion):
            self.session.query(Actor).filter(Actor.idActor == id).\
                update({'nombre' : nombre })
            self.session.commit()
            
            self.session.query(Actor).filter(Actor.idActor == id).\
                update({'descripcion' : descripcion })
            self.session.commit()
            return True
        else:
            return False

#Use case code ends here
