# -*- coding: utf-8 -*-

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
  
    print(params)
    acc=clsAccion(session=session)
    acc.insertar(params['idAccion'],params['descripcion'])
   

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
    
    session.query(Accion).filter(Accion.idAccion == int(params['idAccion'])).\
        update({'descripcion' : (params['descripcion']) })
    session.commit()
    
    
    #idPila = 1
    #res['label'] = res['label'] + '/' + str(idPila)

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

    idAccion = int(request.args['idAccion'])
    acc = accion.query.filter_by(idAccion=idAccion).first()
    res['accion'] =  {'idAccion':acc.idAccion, 'descripcion':acc.descripcion}
    

    #Action code ends here
    return json.dumps(res)



@accion.route('/accion/VCrearAccion')
def VCrearAccion():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)



class clsAccion():
        def __init__(self,engine=None,session=None):
            self.engine  = engine
            self.session = session

        def insertar(self,descripcion,idAccion): #####Revisar base.py insertar lleva otro campos
            newAccion = Accion(idAccion, descripcion)
            session.add(newAccion)
            session.commit()
        
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

#Use case code starts here


#Use case code ends here