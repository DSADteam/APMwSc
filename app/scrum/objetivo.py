# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json

objetivo = Blueprint('objetivo', __name__)


@objetivo.route('/objetivo/ACrearObjetivo', methods=['POST'])
def ACrearObjetivo():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Actor creado']}, {'label':'/VCrearObjetivo', 'msg':['Error al crear objetivo']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message
    iObjetivo = model.Objetivo(params['descripcion'],params['idObjetivo'],params['idPila'])
    session.add(iObjetivo)
    session.commit()

    idPila = 1
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
    
    iObjetivo = Objetivo(params['descripcion'],params['idObjetivo'],params['idPila'])
    session.query(Objetivo).filter(Objetivo.idObjetivo == idObjetivo).\
        update({'descripcion' : (iObjetivo.descripcion) })
    session.commit()
        
    idPila = 1
    res['label'] = res['label'] + '/' + str(idPila)

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


    #Action code ends here
    return json.dumps(res)



@objetivo.route('/objetivo/VObjetivo')
def VObjetivo():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    
    iObjetivo = Objetivo(params['descripcion'],params['idObjetivo'],params['idPila'])
    vObj = session.query(Objetivo).filter(Objetivo.idObjetivo == idObjetivo).all()
    return vObj
    
    res['idPila'] = 1 

    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here