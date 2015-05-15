# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json

objetivo = Blueprint('objetivo', __name__)


@objetivo.route('/objetivo/ACrearObjetivo', methods=['POST'])
def ACrearObjetivo():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Objetivo creado']}, {'label':'/VCrearObjetivo', 'msg':['Error al crear objetivo']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    obj=clsObjetivo(session=session)
    obj.insertarObj(params['idObjetivo'],params['descripcion'])
    
    #idPila = 1
    #res['label'] = res['label'] + '/' + str(idPila)

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
    
    obj = clsObjetivo()
    obj.modificarObj(params['idObjetivo'], params['descripcion'])        
   
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
    
    idObjetivo = int(request.args['idObjetivo'])
    obj = objetivo.query.filter_by(idObjetivo=idObjetivo).first()
    res['objetivo'] =  {'idObjetivo':obj.idObjetivo, 'descripcion':obj.descripcion}
    
    
    
    #Action code ends here
    return json.dumps(res)





#Use case code starts here
class clsObjetivo():
    
    def __init__(self,engine=None,session=None):
            self.engine  = engine
            self.session = session
    
    def insertarObj(self, idObjetivo, descripcion):
        
        newObj = base.Objetivo(idObjetivo, descripcion) 
        session.add(newObj)
        session.commit()
        
    def modificarObj(self,idObjetivo,descripcion):
        session.query(base.Objetivo).filter(base.Objetivo.idobjetivo == idObjetivo).\
             update({'descripcion' : (descripcion) })
        session.commit()
        
    def obtenerObjProd(self, idProducto):
        res = []
        result = self.engine.execute("select * from \"Objetivos\" where idProducto = \"+str(idProducto)\" ;")
        if result!="":
            for row in result:
                res.append({'idObjetivo':row.idProducto,'descripcion':row.descripcion})
            else:
                print("Empty query!")
            
        return res
    
    def obtenerObj(self, idProducto):
        res = []
        result = self.engine.execute("select * from \"Objetivos\";")
        if result!="":
            for row in result:
                res.append({'idObjetivo':row.idProducto,'descripcion':row.descripcion})
            else:
                print("Empty query!")
            
        return res
    

#Use case code ends here