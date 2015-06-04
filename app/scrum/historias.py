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
from app.scrum.prod import clsProducto

@historias.route('/historias/ACrearHistoria', methods=['POST'])
def ACrearHistoria():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VHistorias', 'msg':['Historia creada']}, {'label':'/VCrearHistoria', 'msg':['Error al crear historia']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


    idPila = int(session['idPila'])
    his = clsHistoria(session=sessionDB,engine=engine)
    y=his.insertar(codigo=params['codigo'],idAccion=int(params['accion']),tipo=params['tipo'],idProducto=idPila, prioridad = params['prioridad'])
    idHistoria=his.obtId(params['codigo'], idPila)
    his.asociarActores(params['actores'], idHistoria)
    his.asociarObjetivos(params['objetivos'], idHistoria)


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
    print("ESTOS SON MIS PARAMETTEROOORWOEFDESF")
    print(params)
    his = clsHistoria(session=sessionDB,engine=engine)
    his.modificar(
                idHistoria = "hola $:",
                codigo     = params['codigo'],
                idAccion   = int(params['accion']),
                tipo       = params['tipo'],
                idProducto = idPila,
                prioridad  = params['prioridad'])
    his.asociarActores(params['actores'], idHistoria)
    his.asociarObjetivos(params['objetivos'], idHistoria)

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
    res['fHistoria'] = {'super':0}

    res['fHistoria_opcionesPrioridad'] = [
      {'key':1, 'value':'Alta'},
      {'key':2, 'value':'Media'},
      {'key':3, 'value':'Baja'},
    ]


    #Action code ends here
    return json.dumps(res)



@historias.route('/historias/VHistoria')
def VHistoria():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    params = request.get_json()

    print("ESTOOO FUE AL ENTRAAAAAAR")
    print(params)

    #Ejemplo de relleno de listas para selectrores
    act=clsActor(engine=engine,session=sessionDB)
    acc=clsAccion(engine=engine,session=sessionDB)
    hist=clsHistoria(engine=engine,session=sessionDB)
    obj=clsObjetivo(engine=engine,session=sessionDB)
    oProd = clsProducto(engine,sessionDB)

    
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
    print(aux)
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

    if(oProd.getEscala == "cualitativo"):
        res['fHistoria_opcionesPrioridad'] = [
          {'key':20, 'value':'Alta'},
          {'key':13, 'value':'Media'},
          {'key':7, 'value':'Baja'},
        ]
    else:
        res['fHistoria_opcionesPrioridad'] = []
        for i in range(1,21):
            item = {'key':i,'value':i}
            res['fHistoria_opcionesPrioridad'].append(item)
         
    

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
    print(res)
    #Action code ends here
    return json.dumps(res)





#Use case code starts here

class clsHistoria():
    
    def __init__(self,engine=None,session=None):
        
        self.engine  = engine
        self.session = session
     
    def insertar(self,codigo=None,idProducto=None,idPapa=None,tipo=None,idAccion=None,priori=None):


        #No nulidad, estas de no nulidad no se requiere, el type() resuelve eso
        nulidadesValidas = idProducto!=None and tipo != None and codigo != None \
                           and idAccion != None and priori != None
        if not nulidadesValidas:
            return False
        
        tiposCorrectos = (type(codigo)     is str) and \
                         (type(idProducto) is int) and \
                         (type(tipo)       is str) and \
                         (type(idAccion)   is int) and \
                         (type(idPapa)     is int  or   idPapa   == None) and \
                         (type(priori)     is int or str)    
        
        
        if tiposCorrectos:
            pass
        else:
            return False
        

        producto = self.session.query(Producto).filter(Producto.idProducto == idProducto)

        #Protecciones de funcion
        stringsVacios    = codigo == '' or tipo == ''
        estaEnDb         = self.existeHistoria(codigo=codigo,idProducto=idProducto)
        existeProducto   = producto.count() > 0
        longCharValido   = (len(codigo) <= 500) and (len(tipo) <= 500)
        tieneLoops       = self.tieneLoops(idProducto,idPapa,codigo)
        
        esValido = (not stringsVacios) and (not estaEnDb) and existeProducto\
                    and longCharValido and (not tieneLoops)
        
        if esValido:
            newHis = Historia(codigo,idProducto,idAccion,tipo,priori)
            self.session.add(newHis)
            self.session.commit()
            return True
        else:
            return False
        
        if type(priori) is int:
            if ((priori<1) and (priori>20)):
                return False
        elif type(priori) is str:
            if not ((priori=='Alta')or(priori=='Media')or(priori=='Baja')):
                return False
        else:
            return False

    def modificar(self,idHistoria=None,codigo=None,idProducto=None,idPapa=None,tipo=None,idAccion=None,prioridad=None):


        #No nulidad, estas de no nulidad no se requiere, el type() resuelve eso

        
        tiposCorrectos = (type(codigo)     is str) and \
                         (type(idProducto) is int) and \
                         (type(tipo)       is str) and \
                         (type(idAccion)   is int) and \
                         (type(idPapa)     is int  or   idPapa   == None) and \
                         (type(prioridad)  is int  or str)    
        
        
        if not tiposCorrectos:
            return False

        
        
        self.session.query(Historia).filter(Historia.idHistoria == idHistoria).\
             update({'idHistoria' : idHistoria })
        self.session.commit()

        self.session.query(Historia).filter(Historia.idHistoria == idHistoria).\
            update({'codigo':codigo})
        self.session.commit()

        self.session.query(Historia).filter(Historia.idHistoria == idHistoria).\
            update({'idProducto':idProducto})
        self.session.commit()

        self.session.query(Historia).filter(Historia.idHistoria == idHistoria).\
            update({'idPapa':idPapa})
        self.session.commit()

        self.session.query(Historia).filter(Historia.idHistoria == idHistoria).\
            update({'tipo':tipo})
        self.session.commit()

        self.session.query(Historia).filter(Historia.idHistoria == idHistoria).\
            update({'idAccion':idAccion})
        self.session.commit()

        self.session.query(Historia).filter(Historia.idHistoria == idHistoria).\
            update({'prioridad':prioridad})
        self.session.commit()

        self.session.query(ActoresHistoria).filter(
                                    ActoresHistoria.idHistoria == idHistoria).\
                delete()

        self.session.query(ObjetivosHistorias).filter(
                                    ObjetivosHistorias.idHistoria == idHistoria).\
                delete()



        
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
            obj = self.session.query(Objetivo).filter(Objetivo.idObjetivo == id)
            for row in obj:
                if (row.transversal==1):
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
        #comentarioNulo = ((codigo == None) or (idProducto==None))
        tiposCorrectos = (type(codigo) is str) and (type(idProducto) is int) 
        
        if tiposCorrectos:
            result  = self.session.query(Historia).filter(Historia.idProducto == idProducto).filter(Historia.codigo == codigo)
            return result.count() > 0
        else:
            return False


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
        result = self.session.query(Historia).filter(Historia.idProducto == idProducto)
        
        for row in result:
            
            enunciado = "En tanto que "

            actoresAsoc = self.session.query(ActoresHistoria,Actor).\
                            filter(ActoresHistoria.idHistoria == row.idHistoria).\
                            filter(ActoresHistoria.idActor == Actor.idActor)
            i = 0
            for actor in actoresAsoc:
                enunciado += actor[1].nombre  
                if(i==actoresAsoc.count()-2):
                    enunciado += " y "
                elif(i < actoresAsoc.count()-2):
                    enunciado += ", "
                else:
                    pass
                i+=1

                #soon.. verificar si es la ultima columna y cambiar como por un y

            if (row.tipo == "obligatorio") :
                enunciado += " puedo "
            else:
                enunciado += " podria "


            accionEncontrada = self.session.query(Historia,Accion).\
                            filter(Historia.idHistoria == row.idHistoria).\
                            filter(Historia.idAccion == Accion.idAccion)

            for acc in accionEncontrada:
                enunciado += acc[1].descripcion + " para "

            objetivosAsoc = self.session.query(ObjetivosHistoria,Objetivo).\
                            filter(ObjetivosHistoria.idHistoria == row.idHistoria).\
                            filter(ObjetivosHistoria.idObjetivo == Objetivo.idObjetivo)
            
            i = 1
            for obj in objetivosAsoc:
                if (obj[1].transversal == "no transversal"):
                    enunciado += obj[1].descripcion
                    if (i==objetivosAsoc.count()-1):
                        enunciado += "."
                    elif(i==objetivosAsoc.count()-2):
                        enunciado += " y "
                    elif(i < objetivosAsoc.count()-2):
                        enunciado += ", "
                    i+=1

            res.append({'idHistoria':row.idHistoria,'enunciado':enunciado,'prioridad':row.prioridad})


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