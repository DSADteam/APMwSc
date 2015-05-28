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
    print(session)
    idPila = str(session['idPila'])
    session.pop("idPila",None)

    obj=clsObjetivo(session=sessionDB, engine = engine)
    obj.insertar(descripcion = params['descripcion'], idProducto=idPila)
    res['label'] = res['label'] + '/' + idPila

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
    
    idObjetivo = params['idObjetivo']

    obj=clsObjetivo(session=sessionDB,engine=engine)
    obj.modificar(idObjetivo,params['descripcion'])
    res['label'] = res['label'] + '/' + str(session['idPila'])

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

    
    #session['idPila'] = request.args['idPila']
    res['idPila'] = session['idPila']
    print(session)

    #Action code ends here
    return json.dumps(res)

@objetivo.route('/objetivo/VObjetivo')
def VObjetivo():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    obj=clsObjetivo(engine=engine,session=sessionDB)

    idObjetivo        = request.args.get('idObjetivo', 1)
    res['idObjetivo'] = idObjetivo
    res['fObjetivo']  = obj.mostrarObjetivo(int(idObjetivo))
    #idObjetivo=idPila
    
    #Action code ends here
    return json.dumps(res)


#Use case code starts here
class clsObjetivo():
    
    def __init__(self,engine=None,session=None):
        
        self.engine  = engine
        self.session = session

    def insertar(self,idProducto=None,descripcion=None):
        
        if type(descripcion) is int:
            return False
        if isinstance(idProducto, str):
            return False
        
        comentarioNulo = (descripcion == None) or\
        (idProducto)==None
        if comentarioNulo:
            return False

        estaEnBd       = self.existeObjetivo(descripcion=descripcion)
        #pr = clsProducto()
        #estaEnBd = estaEnBd and pr.existeProducto(idProducto)
        longCharValido = (len(descripcion) <= 500)

        if (not estaEnBd) and (longCharValido) and (not comentarioNulo):
            newObj = Objetivo(descripcion,idProducto)
            self.session.add(newObj)
            self.session.commit()
            return True
        else:
            return False
            
    def existeObjetivo(self,descripcion=None):
        
        if type(descripcion) is int:
            return False
        
        if(descripcion!=None):
            result  = self.engine.execute("select * from \"Objetivos\" where \'descripcion\'=\'"+descripcion+"\';")
        else:
            return False
        
        contador = 0
        for row in result:
            contador += 1

        return contador != 0

    def mostrarObjetivo(self,idObjetivo):
        result = self.session.query(Objetivo).filter(Objetivo.idObjetivo == idObjetivo)
        if result!="":
            for row in result:
                res = {'idObjetivo':row.idObjetivo,'descripcion':row.descripcion}
            else:
                print("Empty query!")
        return res

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
        
        if type(descripcion) is int:
            return False
        if type(id) is str:
            return False
        
        if(id==None):
            return False
        
        if id and descripcion:
            
            self.session.query(Objetivo).filter(Objetivo.idObjetivo == id).\
                update({'descripcion' : descripcion })
            self.session.commit()
            return True
        else:
            return False
        
       
    
#Use case code ends here