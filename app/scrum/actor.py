# -*- coding: utf-8 -*-
#yyession, Blueprint, json
#from base import *
from flask import request, session, Blueprint, json
actor = Blueprint('actor', __name__)


@actor.route('/actor/ACrearActor', methods=['POST'])
def ACrearActor():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Actor creado']}, {'label':'/VCrearActor', 'msg':['Error al crear actor']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message
    from base import db, Actor
    #oActor = actor(params['nombre'],params['descripcion'],params['idActor'], params['idPila'])
    #session.add(oActor)
    #session.commit()
    print(params)
    act=clsActor(session=session)
    act.insertar(params['idActor'],params['descripcion'])
    #res['label'] = res['label'] + '/' + str(idPila)

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
    from base import db, Actor
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
    from base import db, Actor

    idActor = int(request.args['idActor'])
    act = actor.query.filter_by(idActor=idActor).first()
    res['actor'] =  {'idActor':act.idActor, 'descripcion':act.descripcion}

    #Action code ends here
    return json.dumps(res)



@actor.route('/actor/VCrearActor')
def VCrearActor():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    from base import db, Actor


    #Action code ends here
    return json.dumps(res)



class clsActor():
        def __init__(self,engine=None,session=None):
            self.engine  = engine
            self.session = session

        def insertar(self,idActor, nombre,descripcion):
            
            newActor = Actor(idActor,nombre,descripcion)
            session.add(newActor)
            session.commit()
        
        def listarActores(self):
            res = []
            result = self.engine.execute("select * from \"Actores\";")
            if result!="":
                for row in result:
                    res.append({'idActor':row.idActor,'descripcion':row.descripcion})
                else:
                    print("Empty query!")
                    
        def listarActoresprod(self,idProducto):
            res = []
            result = self.engine.execute("select * from \"Actores\" where idProducto= "+str(idProducto)+" ;")
            if result!="":
                for row in result:
                    res.append({'idActor':row.idActor,'descripcion':row.descripcion})
                else:
                    print("Empty query!")
            
            return res

#Use case code starts here

#Use case code ends here