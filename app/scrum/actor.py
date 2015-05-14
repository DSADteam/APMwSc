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
    oActor = actor(params['nombre'],params['descripcion'],params['idActor'], params['idPila'])
    session.add(oActor)
    session.commit()
  
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
    from base import db, Actor
    oActor = actor(params['nombre'],params['descripcion'],params['idActor'], params['idPila'])
    session.query(actor).filter(actor.idactor == oActor.idactor).\
        update({'descripcion' : (oActor.descripcion) })
    session.commit()

    session.query(actor).filter(accion.idactor == oActor.idactor).\
        update({'nombre' : (oActor.nombre) })
    session.commit()

    res['label'] = res['label'] + '/' + str(idPila)

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





#Use case code starts here


#Use case code ends here