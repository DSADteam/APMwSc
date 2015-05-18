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
    #Action code goes here, res should be a list with a label and a message
    idPila = int(request.args.get('idPila', 1))
    acc=clsAccion(session=sessionDB,engine=engine)
    acc.insertar(descripcion=params['descripcion'],idProducto=int(request.args.get('idPila', 1)))
    res['label'] = res['label'] + '/' + str(idPila)
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
    idPila = int(request.args.get('idPila', 1))
    acc=clsAccion(session=sessionDB,engine=engine)
    acc.modificar(int(request.args.get('idPila', 1)),params['descripcion'])
    
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
    acc=clsAccion(engine=engine,session=sessionDB)
    
    idPila = int(request.args.get('idPila', 1))
    pilas = acc.listarAcciones()
    res['fAccion'] = pilas[idPila-1]
    
    
    idAccion = idPila
    #Action code ends here
    return json.dumps(res)



@accion.route('/accion/VCrearAccion')
def VCrearAccion():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    params = request.get_json()
    #Action code ends here
    return json.dumps(res)



class clsAccion():
        def __init__(self,engine=None,session=None):
            self.engine  = engine
            self.session = session
            
        def insertar(self,descripcion=None,idProducto=None):
            comentarioNulo = (descripcion == None) or\
            (idProducto)==None
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
            if(descripcion!=None):
                result  = self.engine.execute("select * from \"Acciones\" where \'descripcion\'=\'"+descripcion+"\';")
            else:
                return False
            
            contador = 0
            for row in result:
                contador += 1

            return contador != 0

        
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
            if id and descripcion:
                
                self.session.query(Accion).filter(Accion.idAccion == id).\
                    update({'descripcion' : descripcion })
                self.session.commit()
                return True
            else:
                return False

#Use case code starts here


#Use case code ends here