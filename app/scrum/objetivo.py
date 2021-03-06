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
    
    print(params)
    idPila = str(session['idPila'])

    transversalidad = "transversal" if params['transversal'] else "no transversal"

    obj=clsObjetivo(session=sessionDB, engine = engine)
    x=obj.insertar(int(idPila),params['descripcion'],transversalidad)
    if not x:
        res=results[1]
    res['label'] = res['label'] + '/' + idPila

    #Action code ends here
    
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

@objetivo.route('/objetivo/AElimObjetivo')
def AElimObjetivo():
    
    #GET parameter
    results = [{'label':'/VProducto', 'msg':['Objetivo eliminado']}, {'label':'/VObjetivo', 'msg':['No se pudo eliminar este objetivo']}, ]
    res = results[0]
    
    #Action code goes here, res should be a list with a label and a message

    idObjetivo = session['idObjetivo']
    idPila = session['idPila']

    obj = clsObjetivo(session=sessionDB,engine=engine)
    obj.eliminar(idObjetivo)
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

    transversalidad = "transversal" if params['transversal'] else "no transversal"

    obj=clsObjetivo(session=sessionDB,engine=engine)
    x=obj.modificar(params['idObjetivo'],params['descripcion'], transversalidad)
    if not x:
        res=results[1]
        res['label'] = res['label'] + '/' + str(params['idObjetivo'])
    else:
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
    
    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']

    res['idPila'] = session['idPila']
    res['fObjetivo_opcionesTransversalidad'] = [
      {'key':True, 'value':'transversal'},{'key':False, 'value':'no transversal'},
    ]

    params = request.get_json()

    #Action code ends here
    
    return json.dumps(res)

@objetivo.route('/objetivo/VObjetivo')
def VObjetivo():
    
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    
    #Action code goes here, res should be a JSON structure
    
    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']

    obj=clsObjetivo(engine=engine,session=sessionDB)

    idObjetivo            = request.args.get('idObjetivo', 1)
    res['fObjetivo']      = obj.mostrarObjetivo(int(idObjetivo))
    res['idPila']         = session['idPila']
    session['idObjetivo'] = idObjetivo
    res['fObjetivo_opcionesTransversalidad'] = [
      {'key':True, 'value':'transversal'},{'key':False, 'value':'no transversal'},
    ]
    
    #Action code ends here
    
    return json.dumps(res)


#Use case code starts here

#Clase objetivo
class clsObjetivo():
    
    def __init__(self,engine=None,session=None):
        
        self.engine  = engine
        self.session = session

    ''' Metodo insertar
        Inserta un objetivo en la base de datos
    '''
    def insertar(self,idProducto,descripcion,trans):

        #Verificaciones de entrada
        tiposCorrectos = (type(descripcion) is str) and (type(idProducto) is int) and (type(trans) is str)\
                         and (trans!=None)

        if not tiposCorrectos:
            return False
        if not((trans=="transversal") or (trans=="no transversal")):
            return False

        comentarioNulo = (descripcion == None) or\
        (idProducto)==None or (descripcion == '') or (trans==None)
        if comentarioNulo:
            return False

        estaEnBd       = self.existeObjetivo(descripcion=descripcion)
        
        longCharValido = (len(descripcion) <= 500)

        if (not estaEnBd) and (longCharValido) and (not comentarioNulo):
            newObj = Objetivo(descripcion,idProducto,trans)
            self.session.add(newObj)
            self.session.commit()
            return True
        else:
            return False
            
    ''' Funcion exiteObjetivo
        Verifica la existencia de un objetivo en la base de datos
    '''
    def existeObjetivo(self,descripcion=None):
        
        # Verificacion de entrada
        if type(descripcion) is int:
            return False
        if (descripcion==''):
            return False
        
        if(descripcion!=None):
            result = self.session.query(Objetivo).filter(Objetivo.descripcion == descripcion)
        else:
            return False
        
        return result.count() > 0

    ''' Funcion mostrarObjetivo
        Muestra la informacion de un objetivo 
    '''
    def mostrarObjetivo(self,idObjetivo):
        result = self.session.query(Objetivo).filter(Objetivo.idObjetivo == idObjetivo)
        if result!="":
            for row in result:
                res = {'idObjetivo':row.idObjetivo,'descripcion':row.descripcion, 'transversal':row.transversal}
            else:
                print("Empty query!")
        return res

    ''' Funcion listarObjetivos
        Lista todos los objetivos
    '''
    def listarObjetivos(self):
        
        res = []
        result = self.engine.execute("select * from \"Objetivos\";")
        if result!="":
            for row in result:
                res.append({'idObjetivo':row.idObjetivo,'descripcion':row.descripcion, 'transversal':row.transversal})
            else:
                print("Empty query!")
     
    ''' Funcion listarObjetivosprod
        Lista todos los objetivos asociados a un producto
    '''                
    def listarObjetivosprod(self,idProducto):
        
        res = []
        result = self.session.query(Objetivo).filter(Objetivo.idProducto == idProducto)
        if result!="":
            for row in result:
                res.append({'idObjetivo':row.idObjetivo,'descripcion':row.descripcion, 'transversal':row.transversal})
            else:
                print("Empty query!")
        
        return res

    ''' Funcion listarObjetivosprodt
        Lista todos los objetivos asociados a un producto y son no transversales
    ''' 
    def listarObjetivosprodt(self,idProducto):
        
        res = []
        #result = self.engine.execute("select * from \"Objetivos\" where idProducto= "+str(idProducto)+" ;")
        result = self.session.query(Objetivo).filter(Objetivo.idProducto == idProducto)
        if result!="":
            for row in result:
                if row.transversal=='no transversal':
                    res.append({'idObjetivo':row.idObjetivo,'descripcion':row.descripcion, 'transversal':row.transversal})
            else:
                print("Empty query!")
        
        return res
    
    ''' Funcion borrarFilas
        Limpia los objetivos de la base de datos 
    ''' 
    def borrarFilas(self):
        
        self.session.query(Objetivo).delete()
        self.session.commit()

    ''' Funcion getProdId
        Obtiene el id del producto del objetivo
    ''' 
    def getProdId(self,idObjetivo):
        
        result = self.session.query(Objetivo).filter(Objetivo.idObjetivo == idObjetivo)
        for row in result:
            x=row.idObjetivo
        return x
    

    ''' Funcion modificar
        Funcion que permite actualizar la descripcion
    '''
    def modificar(self,id=None,descripcion=None,trans=None):
        
        #Verificaciones de entrada
        tipoid=(id!=None) and (type(id) is int) 
        tipodesc= (type(descripcion) is str) 

        tipotransv=(type(trans) is str)
        
        if tipoid and tipodesc and tipotransv and ((trans=="transversal") or (trans=="no transversal")):
            if(len(descripcion)>500): 
                return False
            self.session.query(Objetivo).filter(Objetivo.idObjetivo == id).\
                update({'descripcion' : descripcion })
            self.session.commit()
            
            self.session.query(Objetivo).filter(Objetivo.idObjetivo == id).\
                update({'transversal' : trans })
            self.session.commit()
            return True
        else:
            return False
       
    ''' Funcion eliminar
        Funcion que permite eliminar un objetivo
    '''
    def eliminar(self,idObjetivo):

        if (idObjetivo==None):
            return False
        
        #Desasociando de las historias
        self.session.query(ObjetivosHistoria).filter(ObjetivosHistoria.idObjetivo == idObjetivo).delete()

        result = self.session.query(Objetivo).filter(Objetivo.idObjetivo == idObjetivo).delete()
        if result:
            return True
        else:
            return False
        
#Use case code ends here
