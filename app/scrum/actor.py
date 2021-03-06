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
    x=act.insertar(nombre=params['nombre'],descripcion=params['descripcion'],idProducto=int(idPila))
    if not x:
        res=results[1]
    res['label'] = res['label'] + '/' + idPila

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

@actor.route('/actor/AElimActor')
def AElimActor():
    
    #GET parameter
    results = [{'label':'/VProducto', 'msg':['Actor eliminado']}, {'label':'/VActor', 'msg':['No se pudo eliminar este actor']}, {'label': '/VActor', 'msg' : ["Hay usuarios asociado al actor, no es posible eliminar"]} , ]
    res = results[0]
  
    #Action code goes here, res should be a list with a label and a message

    idActor = session['idActor']
    idPila = session['idPila']

    act = clsActor(session=sessionDB,engine=engine)
    resultado = act.eliminar(idActor)

    if not resultado:
        res = results[2]

    res['label'] = res['label'] + '/' + str(idPila)

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
    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)

    idActor = params['idActor']
    
    act=clsActor(session=sessionDB,engine=engine)
    x=act.modificar(idActor,params['nombre'],params['descripcion'])
    if not x:
        res=results[1]
        res['label'] = res['label'] + '/' + str(params['idActor'])
    else:
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

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)

    act=clsActor(engine=engine,session=sessionDB)


    idActor            = request.args.get('idActor', 1)
    res['fActor']      = act.mostrarActor(idActor)
    res['idPila']      = session['idPila']
    session['idActor'] = idActor

    #Action code ends here
   
    return json.dumps(res)



@actor.route('/actor/VCrearActor')
def VCrearActor():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
   
    #Action code goes here, res should be a JSON structure

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    
    res['idPila'] = session['idPila']

    #Action code ends here
    
    return json.dumps(res)

#Use case code starts here

# Clase Actor
class clsActor():
    
    def __init__(self,engine=None,session=None):
        
        self.engine  = engine
        self.session = session
    
    ''' Funcion insertar
         Funcion que inserta un actor    
    '''
    def insertar(self,nombre=None,descripcion=None,idProducto=None):
        
        #Verificaciones de entrada
        tiposCorrectos = (type(descripcion) is str) and \
                         (type(nombre) is str)      and \
                         (type(idProducto) is int)

        if not tiposCorrectos:
            return False
       
        comentarioNulo = (nombre == None) or (descripcion == None) or\
        (idProducto==None) or (nombre == '') or (descripcion == '') 
        if comentarioNulo:
            return False
        
        producto = self.session.query(Producto).filter(Producto.idProducto == idProducto)
        existeProducto = producto.count() > 0

        longCharValido = (len(nombre) <= 50) and (len(descripcion) <= 500)
        
        # Insertar el actor
        if (longCharValido) and (not comentarioNulo) and existeProducto:
            newAct = Actor(nombre,descripcion,idProducto)
            self.session.add(newAct)
            self.session.commit()
            return True
        else:
            return False
    
    ''' Funcion existeActor
         Funcion que verifica la existencia de un actor a partir de su descripcion o de su nombre    
    '''
    def existeActor(self,nombre=None,descripcion=None):
        
        # Verificaciones de entrada
        nombreStr   = (type(nombre) is str)      or nombre==None
        descriptStr = (type(descripcion) is str) or descripcion==None
        
        if(nombreStr and descriptStr):
            pass
        else:
            return False
        
        #Filtrar actores
        if(nombre!=None and descripcion==None):
            result = self.session.query(Actor).filter(Actor.nombre == nombre)
        elif(nombre==None and descripcion!=None):
            result = self.session.query(Actor).filter(Actor.descripcion == descripcion)
        elif(nombre!=None and descripcion!=None):
            result = self.session.query(Actor).filter(Actor.nombre == nombre).filter(Actor.descripcion == descripcion)
        else:
            return False

        return result.count() > 0

    ''' Funcion mostrarActor
        Funcion que muestra actores
    '''
    def mostrarActor(self,idActor):
        
        result = self.session.query(Actor).filter(Actor.idActor == idActor)
        if result!="":
            for row in result:
                res = {'nombre':row.nombre,'idActor':row.idActor,'descripcion':row.descripcion}
            
        return res

    ''' Funcion listarActores
        Funcion que lista actores
    '''
    def listarActores(self,showAsKeyValue=False):
        
        res = []
        result = self.engine.execute("select * from \"Actores\";")
        if result!="":
            for row in result:
                if showAsKeyValue:
                    res.append({'key':row.idActor,'value':row.descripcion})
                else:
                    res.append({'nombre':row.nombre,'idActor':row.idActor,'descripcion':row.descripcion})
            
        return res
    
    ''' Funcion listarActoresprod
        Funcion que lista los actores de un producto            
    '''
    def listarActoresprod(self,idProducto):
        
        res = []
        result = self.session.query(Actor).filter(Actor.idProducto == idProducto)
        if result!="":
            for row in result:
                res.append({'idActor':row.idActor,'nombre':row.nombre,'descripcion':row.descripcion})
            
        return res

    ''' Funcion borrarFilas
        Funcion que limpia de actores la base de datos
    '''
    def borrarFilas(self):
        
        self.session.query(Actor).delete()
        self.session.commit()
    
    ''' Funcion getProdId
        Funcion para obtener el id del producto asociado a un actor
    '''
    def getProdId(self,idActor):
        
        result = self.session.query(Actor).filter(Actor.idActor == idActor)
        for row in result:
            x=row.idProducto
        return x

    ''' Funcion modificar
        Funcion que permite actualizar un nombre y descripcion
    '''
    def modificar(self,id=None,nombre=None,descripcion=None):
        
        #Verificaciones de entrada
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

    ''' Funcion eliminar
        Funcion que permite eliminar el actor
    '''
    def eliminar(self,idActor):

        usuariosAfectados = self.session.query(dbuser).filter(dbuser.idActor == idActor)

        if (idActor==None) or (usuariosAfectados.count() > 0) :
            return False
        
        # Desasociando historias
        self.session.query(ActoresHistoria).filter(ActoresHistoria.idActor == idActor).delete()

        result = self.session.query(Actor).filter(Actor.idActor == idActor).delete()
        if result:
            return True
        else:
            return False

    ''' Funcion obtener
        Funcion que permite entrega el nombre de un actor, dado su id
    '''
    def obtenerNombre(self,idActor):
        result = self.session.query(Actor).filter(Actor.idActor == idActor)

        for row in result:
            return row.nombre

        return False

#Use case code ends here
