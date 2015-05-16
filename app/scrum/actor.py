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
    #Action code goes here, res should be a list with a label and a message
    #from base import db, Actor
    #oActor = actor(params['nombre'],params['descripcion'],params['idActor'], params['idPila'])
    #session.add(oActor)
    #session.commit()
    idPila = int(request.args.get('idPila', 1))
    print('NIganiganiganiganigaaaaaaaaaaaaaaaaa1')
    print(params)
    print(int(request.args.get('idPila', 1)))
    act=clsActor(session=sessionDB,engine=engine)
    act.insertar(nombre=params['nombre'],descripcion=params['descripcion'],idProducto=int(request.args.get('idPila', 1)))
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
    #from base import db, Actor
    #oActor = actor(params['nombre'],params['descripcion'],params['idActor'], params['idPila'])
    session.query(Actor).filter(Actor.idActor == int(params['idActor'])).\
        update({'descripcion' : (params['descripcion']) })
    session.commit()

    session.query(Actor).filter(Actor.idActor == int(params['idActor'])).\
        update({'nombre' : (params['nombre']) })
    session.commit()

    #res['label'] = res['label'] + '/' + str(idPila)

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
    #Action code goes here, res should be a JSON structure
    #from base import db, Actor

    #idActor = int(request.args['idActor'])
    #act = actor.query.filter_by(idActor=idActor).first()
    #res['actor'] =  {'idActor':act.idActor, 'descripcion':act.descripcion}

    #Action code ends here
    return json.dumps(res)



@actor.route('/actor/VCrearActor')
def VCrearActor():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    #from base import db, Actor
    print('NIganiganiganiganigaaaaaaaaaaaaaaaaa2')
    params = request.get_json()
    print(params)
    #Action code ends here
    return json.dumps(res)


class clsActor():
        def __init__(self,engine=None,session=None):
            self.engine  = engine
            self.session = session
            
        def insertar(self,nombre=None,descripcion=None,idProducto=None):
            comentarioNulo = (nombre == None) or (descripcion == None) or\
            (idProducto)==None
            if comentarioNulo:
                return False

            estaEnBd       = self.existeActor(nombre=nombre)
            #pr = clsProducto()
            #estaEnBd = estaEnBd and pr.existeProducto(idProducto)
            longCharValido = (len(nombre) <= 500) and (len(descripcion) <= 500)

            if (not estaEnBd) and (longCharValido) and (not comentarioNulo):
                newAct = Actor(nombre,descripcion,idProducto)
                self.session.add(newAct)
                self.session.commit()
                return True
            else:
                return False
            
        def existeActor(self,nombre=None):
            if(nombre!=None):
                result  = self.engine.execute("select * from \"Actores\" where \'nombre\'=\'"+nombre+"\';")
            else:
                return False
            
            contador = 0
            for row in result:
                contador += 1

            return contador != 0
        
        def listarActores(self):
            res = []
            result = self.engine.execute("select * from \"Actores\";")
            if result!="":
                for row in result:

                    res.append({'nombre':row.nombre,'idActor':row.idActor,'descripcion':row.descripcion})
                else:
                    print("Empty query!")
                    
        def listarActoresprod(self,idProducto):
            res = []
            #result = self.engine.execute("select * from \"Actores\" where \'idProducto\'="+str(idProducto)+" ;")
            result = self.session.query(Actor).filter(Actor.idProducto == idProducto)
            if result!="":
                for row in result:
                    res.append({'idActor':row.idActor,'descripcion':row.descripcion})
                else:
                    print("Empty query!")
            
            return res

        def borrarFilas(self):
            self.session.query(Actor).delete()
            self.session.commit()

#Use case code starts here

#Use case code ends here