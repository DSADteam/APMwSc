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
objetivo = Blueprint('objetivo', __name__)
from base import *


@objetivo.route('/objetivo/ACrearObjetivo', methods=['POST'])
def ACrearObjetivo():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Objetivo creado']}, {'label':'/VCrearObjetivo', 'msg':['Error al crear objetivo']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    idPila = int(request.args.get('idPila', 1))
    obj=clsObjetivo(session=sessionDB, engine = engine)
    obj.insertar(idObjetivo = params['idObjetivo'], descripcion = params['descripcion'], idProducto=int(request.args.get('idPila', 1)) )
    res['label'] = res['label'] + '/' + str(idPila)

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

@objetivo.route('/objetivo/AModifObjetivo', methods=['POST'])
def AModifObjetivo():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Objetivo actualizado']}, {'label':'/VObjetivo', 'msg':['Error al modificar objetivo']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message
    
    session.query(Objetivo).filter(Objetivo.idObjetivo == int(params['idObjetivo'])).\
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

@objetivo.route('/objetivo/VCrearObjetivo')
def VCrearObjetivo():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    params = request.get_json()
    print(params)
    
    #res['idPila'] = [{'idPila':idPila}]

    #Action code ends here
    return json.dumps(res)

@objetivo.route('/objetivo/VObjetivo')
def VObjetivo():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    
    #Action code ends here
    return json.dumps(res)



#Use case code starts here
class clsObjetivo():
    
    def __init__(self,engine=None,session=None):
        
        self.engine  = engine
        self.session = session

    def insertar(self,descripcion=None,idProducto=None):
        
        comentarioNulo = (descripcion == None) or\
        (idProducto)==None
        if comentarioNulo:
            return False

        estaEnBd       = self.existeObjetivo(descripcion=descripcion)
        #pr = clsProducto()
        #estaEnBd = estaEnBd and pr.existeProducto(idProducto)
        longCharValido = (len(descripcion) <= 500)

        if (not estaEnBd) and (longCharValido) and (not comentarioNulo):
            newObj = Objetivo(idObjetivo,descripcion)
            self.session.add(newObj)
            self.session.commit()
            return True
        else:
            return False
            
    def existeObjetivo(self,descripcion=None):
        
        if(descripcion!=None):
            result  = self.engine.execute("select * from \"Objetivos\" where \'descripcion\'=\'"+descripcion+"\';")
        else:
            return False
        
        contador = 0
        for row in result:
            contador += 1

        return contador != 0

    def listarObjetivos(self):
        
        res = []
        result = self.engine.execute("select * from \"Objetivos\";")
        if result!="":
            for row in result:
                res.append({'idObjetivo':row.idObjetivo,'descripcion':row.descripcion})
            else:
                print("Empty query!")
                    
    def listarObjetivosprod(self,idProducto):
        
        res = []
        #result = self.engine.execute("select * from \"Objetivos\" where idProducto= "+str(idProducto)+" ;")
        result = self.session.query(Objetivo).filter(Objetivo.idProducto == idProducto)
        if result!="":
            for row in result:
                res.append({'idObjetivo':row.idObjetivo,'descripcion':row.descripcion})
            else:
                print("Empty query!")
        
        return res
    
    def borrarFilas(self):
        
        self.session.query(Objetivo).delete()
        self.session.commit()

    #Funcion que permite actualizar la descripcion
    def modificar(self,id=None,descripcion=None):
        
        if id and descripcion:
            
            self.session.query(Objetivo).filter(Objetivo.idObjetivo == id).\
                update({'descripcion' : descripcion })
            self.session.commit()
            return True
        else:
            return False
    
#Use case code ends here