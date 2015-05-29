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

historias = Blueprint('historias', __name__)

from base import *
from app.scrum.actor import clsActor

@historias.route('/historias/ACrearHistoria', methods=['POST'])
def ACrearHistoria():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VHistorias', 'msg':['Historia creada']}, {'label':'/VCrearHistoria', 'msg':['Error al crear historia']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


    idPila = str(session['idPila'])
    session.pop("idPila",None)
    
    his = clsHistoria(session=sessionDB,engine=engine)
    his.insertar(codigo=params['codigo'],idProducto=idPila)
    

    #Datos de prueba
    res['label'] = res['label'] + '/1'

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@historias.route('/historias/AModifHistoria', methods=['POST'])
def AModifHistoria():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VHistorias', 'msg':['Historia modificada']}, {'label':'/VHistoria', 'msg':['Error al modificar historia']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    idPila = int(request.args.get('idPila', 1))
    his = clsHistoria(session=sessionDB,engine=engine)
    his.modificar(int(request.args.get('idPila', 1)),params['codigo'])

    #Datos de prueba    
    res['label'] = res['label'] + '/' + str(idPila)

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@historias.route('/historias/VCrearHistoria')
def VCrearHistoria():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    #Ejemplo de relleno de listas para selectrores
    res['fHistoria_opcionesActores'] = [
      {'key':1,'value':'Actor1'},
      {'key':2,'value':'Actor2'},
      {'key':3,'value':'Actor3'}]
    res['fHistoria_opcionesAcciones'] = [
      {'key':1,'value':'Acccion1'},
      {'key':2,'value':'Acccion2'},
      {'key':3,'value':'Acccion3'}]
    res['fHistoria_opcionesObjetivos'] = [
      {'key':1,'value':'Objetivo1'},
      {'key':2,'value':'Objetivo2'},
      {'key':3,'value':'Objetivo3'}]
    res['fHistoria_opcionesHistorias'] = [
      {'key':0,'value':'Ninguna'},
      {'key':1,'value':'Historia1'},
      {'key':2,'value':'Historia2'},
      {'key':3,'value':'Historia3'}]
    res['fHistoria_opcionesTiposHistoria'] = [
      {'key':1,'value':'Opcional'},
      {'key':2,'value':'Obligatoria'}]
    res['fHistoria'] = {'super':0}


    #Action code ends here
    return json.dumps(res)



@historias.route('/historias/VHistoria')
def VHistoria():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    #Ejemplo de relleno de listas para selectrores
    res['fHistoria_opcionesActores'] = [
      {'key':1,'value':'Actor1'},
      {'key':2,'value':'Actor2'},
      {'key':3,'value':'Actor3'}]
    res['fHistoria_opcionesAcciones'] = [
      {'key':1,'value':'Acccion1'},
      {'key':2,'value':'Acccion2'},
      {'key':3,'value':'Acccion3'}]
    res['fHistoria_opcionesObjetivos'] = [
      {'key':1,'value':'Objetivo1'},
      {'key':2,'value':'Objetivo2'},
      {'key':3,'value':'Objetivo3'}]
    res['fHistoria_opcionesHistorias'] = [
      {'key':0,'value':'Ninguna'},
      {'key':1,'value':'Historia1'},
      {'key':2,'value':'Historia2'},
      {'key':3,'value':'Historia3'}]
    res['fHistoria_opcionesTiposHistoria'] = [
      {'key':1,'value':'Opcional'},
      {'key':2,'value':'Obligatoria'}]
    res['fHistoria'] = {'super':0, 
       'actor':1, 'accion':2, 'objetivo':3, 'tipo':1} 


    #Action code ends here
    return json.dumps(res)



@historias.route('/historias/VHistorias')
def VHistorias():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    #Datos de prueba
    his=clsHistoria(engine=engine,session=sessionDB)
    res['idPila'] = session['idPila']
    res['data0'] = his.listarHistoriasprod(int(session['idPila']))
    print('DAAAAAAAAAAAAAAAAAAAAAAAA')
    print(res['data0'])
    #Action code ends here
    return json.dumps(res)





#Use case code starts here

class clsHistoria():
    
    def __init__(self,engine=None,session=None):
        self.engine  = engine
        self.session = session
        
    def insertar(self,codigo=None,idProducto=None,idPapa=None,tipo=None,idAccion=None):
        
        comentarioNulo = (codigo == None) or\
        (idProducto!=None) or (idAccion==None)
        if comentarioNulo or codigo=='' or tipo==None:
            return False

        estaEnBd       = self.existeHistoria(codigo=codigo,idProducto=idProducto)
        #pr = clsProducto()
        #estaEnBd = estaEnBd and pr.existeProducto(idProducto)
        longCharValido = (len(codigo) <= 500)
        tieneLoops = self.tieneLoops(idProducto,idPapa,codigo)
        
        if (not estaEnBd) and (longCharValido) and (not comentarioNulo) and\
            not tieneLoops:
            newHis = Historia(codigo,idProducto,idAccion,tipo)
            self.session.add(newHis)
            self.session.commit()
            return True
        else:
            return False
        
    def tieneLoops(self,idProducto=None,idPapa=None,codigo=None):
        
        if idProducto==None or codigo==None or idPapa==None:
            return False

        res  = self.session.query(Historia).filter(Historia.idProducto == idProducto and Historia.idHistoria == idPapa)
        
        while res.idHistoriaPadre!=None:
            if res.codigo!=codigo:
                return True
            else:
                res  = self.session.query(Historia).filter(Historia.idProducto == idProducto and Historia.idHistoria == idPapa)
                idPapa=res.idHistoria
        return False
        
    def existeHistoria(self,codigo=None, idHistoria=None,idProducto=None):
        comentarioNulo = ((codigo == None) and\
        (idHistoria==None)) or idProducto==None
        if comentarioNulo:
            return False
        
        if(idHistoria!=None):
            result  = self.session.query(Historia).filter(Historia.idProducto == idProducto and Historia.idHistoria == idHistoria)
        else:
            result  = self.session.query(Historia).filter(Historia.idProducto == idProducto and Historia.codigo == codigo)

        return result.count() != 0

    def listarHistorias(self):
        
        res = []
        result = self.engine.execute("select * from \"Historias\";")
        if result!="":
            for row in result:
                res.append({'idHistoria':row.idHistoria,'enunciado':row.codigo})
            else:
                print("Empty query!")
                
    def listarHistoriasprod(self,idProducto):
        
        res = []
        #result = self.engine.execute("select * from \"Historias\" where idProducto= "+str(idProducto)+" ;")
        result = self.session.query(Historia).filter(Historia.idProducto == idProducto)
        if result!="":
            for row in result:
                res.append({'idHistoria':row.idHistoria,'enunciado':row.codigo})
            else:
                print("Empty query!")
        
        return res
    
    def borrarFilas(self):
        
        self.session.query(Historia).delete()
        self.session.commit()

    #Funcion que permite actualizar la codigo
    def modificar(self,id=None,codigo=None):
        
        if id and codigo:
            
            self.session.query(Historia).filter(Historia.idHistoria == id).\
                update({'codigo' : codigo })
            self.session.commit()
            return True
        else:
            return False

#Use case code ends here