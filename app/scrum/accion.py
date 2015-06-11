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
accion = Blueprint('accion', __name__)
from base import *

@accion.route('/accion/ACrearAccion', methods=['POST'])
def ACrearAccion():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Acción creada']}, {'label':'/VCrearAccion', 'msg':['Error al crear acción']}, ]
    res = results[0]

    idPila = session['idPila']

    acc=clsAccion(session=sessionDB,engine=engine)
    x=acc.insertar(descripcion=params['descripcion'],idProducto=idPila)
    if not x:
        res=results[1]
    res['label'] = res['label'] + '/' + str(idPila)
    res['idPila'] = idPila

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

@accion.route('/accion/AModifAccion', methods=['POST'])
def AModifAccion():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Acción actualizada']}, {'label':'/VAccion', 'msg':['Error al modificar acción']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    idAccion = params['idAccion']
    idPila = session['idPila']

    acc=clsAccion(session=sessionDB,engine=engine)
    x = acc.modificar(idAccion,params['descripcion'])
    if not x:
        res=results[1]
        res['label'] = res['label'] + '/' + str(params['idAccion'])
    else:
        res['label'] = res['label'] + '/' + str(session['idPila'])

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

@accion.route('/accion/AElimAccion')
def AElimAccion():
    #GET parameter
    results = [{'label':'/VProducto', 'msg':['Accion eliminada']}, {'label':'/VAccion', 'msg':['No se pudo eliminar esta acción']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    idAccion = session['idAccion']
    idPila = session['idPila']

    acc = clsAccion(session=sessionDB,engine=engine)
    acc.eliminar(idAccion)
    res['label'] = res['label'] + '/' + str(idPila)

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

@accion.route('/accion/VAccion')
def VAccion():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']

    acc=clsAccion(engine=engine,session=sessionDB)
    
    idAccion            = request.args.get('idAccion', 1)
    res['fAccion']      = acc.mostrarAccion(int(idAccion))
    res['idPila']       = session['idPila']
    session['idAccion'] = idAccion
    
    
    #idAccion = idPila

    #Action code ends here
    return json.dumps(res)

@accion.route('/accion/VCrearAccion')
def VCrearAccion():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']

    res['idPila'] = session['idPila']

    return json.dumps(res)


#Use case code starts here

class clsAccion():
    
    def __init__(self,engine=None,session=None):
        
        self.engine  = engine
        self.session = session
        
    def insertar(self,descripcion=None,idProducto=None):
        
        if type(descripcion) is int:
            return False
        if isinstance(idProducto, str):
            return False
        
        comentarioNulo = (descripcion == None) or\
        (idProducto==None) or (descripcion == '')
        if comentarioNulo:
            return False

        estaEnBd       = self.existeAccion(descripcion=descripcion)
        #pr = clsProducto()
        #estaEnBd = estaEnBd and pr.existeProducto(idProducto)
        longCharValido = (len(descripcion) <= 500)

        if (not estaEnBd) and (longCharValido) and (not comentarioNulo):
            newAcc = Accion(descripcion,idProducto)
            self.session.add(newAcc)
            self.session.commit()
            return True
        else:
            return False
        
    def existeAccion(self,descripcion=None):
        if type(descripcion) is int:
            return False
        if (descripcion==''):
            return False
        
        if(descripcion!=None):
            result = self.session.query(Accion).filter(Accion.descripcion == descripcion)
        else:
            return False
        
        return result.count() > 0

    def mostrarAccion(self,idAccion):
        result = self.session.query(Accion).filter(Accion.idAccion == idAccion)
        if result!="":
            for row in result:
                res = {'idAccion':row.idAccion,'descripcion':row.descripcion}
            else:
                print("Empty query!")
        return res    

    def obtenerId(self,descripcion):
        res = -1

        result = self.session.query(Accion).filter(Accion.descripcion == descripcion)
        if result!="":
            for row in result:
                res = row.idAccion
            
        return res

    def listarAcciones(self):
        
        res = []
        result = self.engine.execute("select * from \"Acciones\";")
        if result!="":
            for row in result:
                res.append({'idAccion':row.idAccion,'descripcion':row.descripcion})
            else:
                print("Empty query!")
                
    def listarAccionesprod(self,idProducto):
        
        res = []
        #result = self.engine.execute("select * from \"Acciones\" where idProducto= "+str(idProducto)+" ;")
        result = self.session.query(Accion).filter(Accion.idProducto == idProducto)
        if result!="":
            for row in result:
                res.append({'idAccion':row.idAccion,'descripcion':row.descripcion})
            else:
                print("Empty query!")
        
        return res
    
    def borrarFilas(self):
        
        self.session.query(Accion).delete()
        self.session.commit()

    #Funcion que permite actualizar la descripcion
    def modificar(self,id=None,descripcion=None):
        
        
        if type(descripcion) is int:
            return False
        if isinstance(id, str):
            return False
        
        if(id==None):
            return False
        if (len(descripcion)>500):
            return False
    

        if id and descripcion:
            a= self.session.query(Accion).filter(Accion.idAccion == id).\
                update({'descripcion' : descripcion })
            self.session.commit()
            return True
        else:
            return False
    #Funcion que permite eliminar la accion
    def eliminar(self,idAccion):

        if (idAccion==None):
            return False
            
        result = self.session.query(Historia).filter(Historia.idAccion == idAccion)

        for i in result:

            idHistoria = i.idHistoria
            # Desasociando viejos
            res  = self.session.query(ActoresHistoria).filter(ActoresHistoria.idHistoria == idHistoria)
            res.delete()
            self.session.commit()

            # Desasociando viejos
            res  = self.session.query(ObjetivosHistoria).filter(ObjetivosHistoria.idHistoria == idHistoria)
            res.delete()
            self.session.commit()

            self.session.query(Historia).filter(Historia.idHistoria == idHistoria).delete()

        result = self.session.query(Accion).filter(Accion.idAccion == idAccion).delete()
        if result:
            return True
        else:
            return False

#Use case code ends here
