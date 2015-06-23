# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json

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

tareas = Blueprint('tareas', __name__)

from base import *
from app.scrum.historias import clsActor




@tareas.route('/tareas/ACrearTarea', methods=['POST'])
def ACrearTarea():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VHistoria', 'msg':['Tarea creada']}, {'label':'/VCrearTarea', 'msg':['No se pudo crear tarea.']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message
    
    idHistoria = int(session['idHistoria'])
    print(idHistoria)

    tar=clsTarea(session=sessionDB, engine = engine)
    print(params['categoria'])
    print('CATEGORIA ARRIBA')
    x=tar.insertar(idHistoria,descripcion=params['descripcion'],nombreCategoria=params['categoria'],peso=params['peso'])
    
    if not x:
        res=results[1]
    else:
        session.pop('idHistoria',None)
        session.pop('idTarea',None)
    
    res['label'] = res['label'] + '/' + str(idHistoria)
    
    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@tareas.route('/tareas/AElimTarea')
def AElimTarea():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VHistoria', 'msg':['Tarea borrada']}, {'label':'/VTarea', 'msg':['No se pudo eliminar esta tarea']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message



    tar=clsTarea(session=sessionDB, engine = engine)
    x=tar.eliminar(int(session['idTarea']))
    
    if not x:
        res=results[1]
    else:
        session.pop('idTarea',None)
    
    res['label'] = res['label'] + '/' + str(session['idHistoria'])
    print('VIVE EN UNA PINA DEBAJO DEL MAR')
    print(res)

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@tareas.route('/tareas/AModifTarea', methods=['POST'])
def AModifTarea():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VHistoria', 'msg':['Tarea modificada']}, {'label':'/VTarea', 'msg':['No se pudo modificar esta tarea.']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message
    idHistoria = int(session['idHistoria'])
    idTarea = int(session['idTarea'])
    #idHistoria = params['idHistoria']
    res['label'] = res['label'] + '/' + repr(idHistoria)

    tat=clsTarea(session=sessionDB,engine=engine)
    x=tat.modificar(idTarea,descripcion=params['descripcion'],nombreCategoria=params['categoria'],peso=params['peso'])
    if not x:
        res=results[1]
        res['label'] = res['label'] + '/' + str(params['idTarea'])
    else:
        res['label'] = res['label']
    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@tareas.route('/tareas/VCrearTarea')
def VCrearTarea():
    #GET parameter
    idHistoria = int(request.args['idHistoria'])
    res = {}
    tar=clsTarea(session=sessionDB, engine = engine)
    if "actor" in session:
        res['actor']=session['actor']   
    #Action code goes here, res should be a JSON structure

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']['nombre']
    res['idHistoria']=idHistoria
    res['fTarea_opcionesCategoria'] = tar.listarCategorias()
    aux=sessionDB.query(Historia).filter(Historia.idHistoria == idHistoria)
    for u in aux:
        aux=u.codigo
        break
    res['codHistoria'] = aux
    print('ASDASDASDASDA')
    print(res)

    session['idHistoria']=idHistoria
    #Action code ends here
    return json.dumps(res)



@tareas.route('/tareas/VTarea')
def VTarea():
    #GET parameter
    idTarea = request.args['idTarea']
    res = {}
    tar=clsTarea(session=sessionDB, engine = engine)
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
     
    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']
    res['codHistoria'] = session['codHistoria']
    res['fTarea_opcionesCategoria'] = tar.listarCategorias()
    tat=clsTarea(session=sessionDB,engine=engine)
    res['fTarea']  = tat.mostraTarea(idTarea)
    session['idTarea'] = idTarea

    
    #Action code ends here
    return json.dumps(res)


#Use case code starts here
class clsTarea():
    
    def __init__(self,engine=None,session=None):
        
        self.engine  = engine
        self.session = session

    def insertar(self,idHistoria,descripcion,nombreCategoria, peso):

        if(descripcion==''):
            return False

       
        tiposCorrectos = (type(descripcion) is str) and \
                         (type(idHistoria)  is int) and \
                         (type(nombreCategoria) is str) and \
                         (type(peso)  is int)
        #unless tipos correctos
        if not tiposCorrectos:
            return False
        

        #Dos tareas identicas de una historia no tiene sentido
        estaEnBd       = self.existeTarea(descripcion,idHistoria)
        longCharValido = (len(descripcion) <= 500)
        
        if (not estaEnBd) and (longCharValido):
       
            newObj = Tarea(descripcion,idHistoria,nombreCategoria, peso)
            self.session.add(newObj)
            self.session.commit()
            return True
        else:
            return False

    def getDescript(self,idTarea):
        
        if not((type(idTarea) is int)):
            return False
        
        if(idTarea!=None):
            result = self.session.query(Tarea).\
            filter(Tarea.idTarea == idTarea)
        else:
            return False
        for i in result:
            return i.descripcion

    def existeTarea(self,descripcion,idHistoria):
       
        if not((type(descripcion) is str) and (type(idHistoria) is int)) :
            return False
        
        
        result = self.session.query(Tarea).\
        filter(Tarea.descripcion == descripcion).\
        filter(Tarea.idHistoria  == idHistoria)
        
        
        return result.count() > 0

    def obtenerId(self,descripcion):
        if not(type(descripcion) is str):
            return False

        result = self.session.query(Tarea).filter(Tarea.descripcion == descripcion)

        return result.first().idTarea

    def existeIdTarea(self,idTarea):
        if not((type(idTarea) is int)) :
            return False
        
        
        result = self.session.query(Tarea).\
        filter(Tarea.idTarea == idTarea)
        
        
        return result.count() > 0

                    
    def listarTareasHistoria(self,idHistoria):
        
        res = []
        result = self.session.query(Tarea).filter(Tarea.idHistoria  == idHistoria)
        if result!="":
            for row in result:
                #Conjeturas, no se que lleva esto en historias
                res.append({'idTarea':row.idTarea,'descripcion':row.descripcion,'nombreCategoria' : row.nombreCategoria ,'peso' : row.peso})
            else:
                print("Empty query!")
        
        return res
    '''
    def listarCategorias(self):
        res=[]
        

        result = self.session.query(Categoria)
        for row in result:
            res+=[ {'key':row.nombreCategoria, 'value':row.nombreCategoria, 'peso':row.peso},]
        
        return res
    '''
    def eliminar(self,idTarea=None):
        
        if not(type(idTarea) is int):
            return False

        if (self.existeIdTarea(idTarea)):
            self.session.query(Tarea).filter(Tarea.idTarea  == idTarea).delete()
            self.session.commit()
            return True
        else:
            return False


    #Funcion que permite actualizar la descripcion
    def modificar(self,idTarea=None,descripcion=None,nombreCategoria=None, peso=None):
        
        tipoid=(idTarea!=None) and (type(idTarea) is int) 
        otrostipos= (type(descripcion) is str) and (type(nombreCategoria) is str) and (type(peso) is int)

        if not (tipoid and otrostipos):
            return False
        
        if(len(descripcion)>500): 
            return False

        if(descripcion==''):
            return False

        self.session.query(Tarea).filter(Tarea.idTarea == idTarea).\
            update({'descripcion' : descripcion ,'nombreCategoria' : nombreCategoria ,'peso' : peso })
        self.session.commit()
        return True


    #Use case code ends here
    def mostraTarea(self,idTarea):
        result = self.session.query(Tarea).filter(Tarea.idTarea == idTarea)
        res = {}
        if result!="":
            for row in result:
                res = {'idTarea':row.idTarea,'descripcion':row.descripcion,'idHistoria':row.idHistoria}
            else:
                print("Empty query!")
        return res

