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
from app.scrum.objetivo import clsObjetivo
from app.scrum.accion import clsAccion
#from app.scrum.prod import clsProducto

@historias.route('/historias/ACrearHistoria', methods=['POST'])
def ACrearHistoria():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VHistorias', 'msg':['Historia creada']}, {'label':'/VCrearHistoria', 'msg':['Error al crear historia']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


    idPila = int(session['idPila'])
    #session.pop("idPila",None)
    print('Putos todos................')
    print(idPila)
    print(params)
    print(session)
    his = clsHistoria(session=sessionDB,engine=engine)
    print('INSERTAREEEE: '+params['codigo']+' EN :'+str(idPila))
    y=his.insertar(codigo=params['codigo'],idAccion=int(params['accion']),tipo=params['tipo'],idProducto=idPila)
    idHistoria=his.obtId(params['codigo'], idPila)
    his.asociarActores(params['actores'], idHistoria)
    his.asociarObjetivos(params['objetivos'], idHistoria)
    print('MI RESULTADO FUE: ')
    print(y)

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

    idPila = int(session['idPila'])
    print('THIS IS THE PILAAAAAAAAA: '+str(idPila))
    his = clsHistoria(session=sessionDB,engine=engine)
    his.modificar(idPila,params['codigo'])

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
    act=clsActor(engine=engine,session=sessionDB)
    acc=clsAccion(engine=engine,session=sessionDB)
    hist=clsHistoria(engine=engine,session=sessionDB)
    obj=clsObjetivo(engine=engine,session=sessionDB)
    
    aux=act.listarActoresprod(int(session['idPila']))
    for x in aux:
        x['key']=x.pop('idActor')
        x['value']=x.pop('nombre')
    res['fHistoria_opcionesActores'] = aux
    print('actores: ')
    print(aux)
    aux=acc.listarAccionesprod(int(session['idPila']))
    for x in aux:
        x['key']=x.pop('idAccion')
        x['value']=x.pop('descripcion')
    res['fHistoria_opcionesAcciones'] = aux
    print('acciones: ')
    print(aux)
    aux=obj.listarObjetivosprod(int(session['idPila']))
    for x in aux:
        x['key']=x.pop('idObjetivo')
        x['value']=x.pop('descripcion')
    res['fHistoria_opcionesObjetivos'] = aux
    print('objetivos: ')
    print(aux)
    aux=hist.listarHistoriasprod(int(session['idPila']))
    for x in aux:
        x['key']=x.pop('idHistoria')
        x['value']=x.pop('enunciado')
    res['fHistoria_opcionesHistorias'] = [
      {'key':0,'value':'Ninguna'},
      {'key':1,'value':'Historia1'},
      {'key':2,'value':'Historia2'},
      {'key':3,'value':'Historia3'}]
    res['fHistoria_opcionesTiposHistoria'] = [
      {'key':'1','value':'Opcional'},
      {'key':'2','value':'Obligatoria'}]
    res['fHistoria'] = {'super':0}


    #Action code ends here
    return json.dumps(res)



@historias.route('/historias/VHistoria')
def VHistoria():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    params = request.get_json()
    print('MIS PARAMS')
    print(params)
    #Ejemplo de relleno de listas para selectrores
    act=clsActor(engine=engine,session=sessionDB)
    acc=clsAccion(engine=engine,session=sessionDB)
    hist=clsHistoria(engine=engine,session=sessionDB)
    obj=clsObjetivo(engine=engine,session=sessionDB)
    
    aux=act.listarActoresprod(int(session['idPila']))
    for x in aux:
        x['key']=x.pop('idActor')
        x['value']=x.pop('nombre')
    res['fHistoria_opcionesActores'] = aux

    aux=acc.listarAccionesprod(int(session['idPila']))
    for x in aux:
        x['key']=x.pop('idAccion')
        x['value']=x.pop('descripcion')
    res['fHistoria_opcionesAcciones'] = aux


    aux=obj.listarObjetivosprod(int(session['idPila']))
    for x in aux:
        x['key']=x.pop('idObjetivo')
        x['value']=x.pop('descripcion')
    res['fHistoria_opcionesObjetivos'] = aux


    aux=hist.listarHistoriasprod(int(session['idPila']))
    for x in aux:
        x['key']=x.pop('idHistoria')
        x['value']=x.pop('enunciado')
    res['fHistoria_opcionesHistorias'] = [
      {'key':0,'value':'Ninguna'},
      {'key':1,'value':'Historia1'},
      {'key':2,'value':'Historia2'},
      {'key':3,'value':'Historia3'}]
    res['fHistoria_opcionesTiposHistoria'] = [
      {'key':'1','value':'Opcional'},
      {'key':'2','value':'Obligatoria'}]
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
        
        """
        comentarioNulo = (codigo == None) or
        (idProducto!=None) or (idAccion==None)
        if comentarioNulo or codigo=='' or tipo==None:
            return False
        """

        #No nulidad
        nulidadesValidas = idProducto!=None and tipo != None and codigo != None
        if not nulidadesValidas:
            return False
        
        producto = self.session.query(Producto).filter(Producto.idProducto == idProducto)

        #Protecciones de funcion
        stringsVacios    = codigo == '' and tipo == ''
        estaEnDb         = self.existeHistoria(codigo=codigo,idProducto=idProducto)
        existeProducto   = producto.count() > 0
        longCharValido   = (len(codigo) <= 500) and (len(tipo) <= 500)
        tieneLoops       = self.tieneLoops(idProducto,idPapa,codigo)
        
        esValido = (not stringsVacios) and (not estaEnDb) and existeProducto\
                    and longCharValido   and (not tieneLoops)
        
        if esValido:
            newHis = Historia(codigo,idProducto,idAccion,tipo)
            self.session.add(newHis)
            self.session.commit()
            return True
        else:
            return False
        
    def obtId(self,codigo=None,idProducto=None):
        if codigo==None or idProducto==None:
            return -1
        
        res  = self.session.query(Historia).filter(Historia.codigo == codigo)
        res  = res.filter(Historia.idProducto == idProducto)
        for i in res:
            return i.idHistoria
        
    def asociarActores(self,idActores=None,idHistoria=None):
        if idActores==[] or idHistoria==None or idActores==None:
            return False
        
        #Desasociando viejos
        res  = self.session.query(ActoresHistoria).filter(ActoresHistoria.idHistoria == idHistoria)
        res.delete()
        self.session.commit()

        for id in idActores:
            newAH = ActoresHistoria(idHistoria,id)
            self.session.add(newAH)
            self.session.commit()
            
        return True

    def asociarObjetivos(self,idObjetivos=None,idHistoria=None):
        if idObjetivos==[] or idHistoria==None or idObjetivos==None:
            return False
        
        #Desasociando viejos
        res  = self.session.query(ObjetivosHistoria).filter(ObjetivosHistoria.idHistoria == idHistoria)
        res.delete()
        self.session.commit()

        for id in idObjetivos:
            newOH = ObjetivosHistoria(idHistoria,id)
            self.session.add(newOH)
            self.session.commit()
            
        return True

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
        
    def existeHistoria(self,codigo,idProducto):
        comentarioNulo = ((codigo == None) or (idProducto==None)) 
        if comentarioNulo:
            return False
        
        result  = self.session.query(Historia).filter(Historia.idProducto == idProducto)
        result  = result.filter(Historia.codigo == codigo)
        
        return result.count() > 0

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