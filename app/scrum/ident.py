# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json
from werkzeug import check_password_hash

import sys
import os
dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../..'))
sys.path.append(dir)

ident = Blueprint('ident', __name__)

from base import *

from app.scrum.encrypt import clsAccessControl
from app.scrum.actor import clsActor

@ident.route('/ident/AIdentificar', methods=['POST'])
def AIdentificar():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProductos', 'msg':['Bienvenido dueño de producto.'], "actor":"duenoProducto"}, 
               {'label':'/VMaestroScrum', 'msg':['Bienvenido Maestro Scrum.'], "actor":"maestroScrum"}, 
               {'label':'/VDesarrollador', 'msg':['Bienvenido Desarrollador.'], "actor":"desarrollador"}, 
               {'label':'/VLogin', 'msg':['Datos de identificación incorrectos.'], "actor":None},
               {'label':'/VLogin', 'msg':['Vista no definida para este actor.'], "actor":None} ]
    res = results[0]
    
    #Action code goes here, res should be a list with a label and a message
    
    log=clsLogin(session=sessionDB,engine=engine)
    resp=log.check_password(params.get('usuario'),params.get('clave'))
    

    if resp:
    #Hacer chequeo del tipo de usuario

        us = clsDBUser(engine,sessionDB)

        actor = us.obtenerActor(params.get('usuario'))

        for i in results:
            res = i
            if i["actor"] == actor:
                session['actor'] = actor
                break



        nombre = us.obtenerNombre(params.get('usuario'))
        session['usuario'] = {'nombre': nombre } 

    else:

        res = results[3]

    #Action code ends here
    
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

@ident.route('/ident/ARegistrar', methods=['POST'])
def ARegistrar():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VLogin', 'msg':['Felicitaciones, Ya estás registrado en la aplicación']}, {'label':'/VRegistro', 'msg':['Error al tratar de registrarse']}, ]
    
    #Action code goes here, res should be a list with a label and a message

    idActor =  params['actorScrum'] #Debe ser buscado el actor

    reg=clsDBUser(session=sessionDB,engine=engine)
    status = reg.insertar(params['nombre'],
                          params['usuario'], 
                          params['clave'],
                          params['clave2'], 
                          params['correo'], 
                          params['actorScrum'])

    if status:
        res = results[0]
    else:
        res = results[1]
    
    #Action code ends here
   
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

@ident.route('/ident/VLogin')
def VLogin():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    
    #Agregado en nueva version de interfaz
    session.pop('usuario', None)

    #Action code ends here
    return json.dumps(res)

@ident.route('/ident/VRegistro')
def VRegistro():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    
    #Action code goes here, res should be a JSON structure

    oActor = clsActor(engine,DBSession)

    res['fUsuario_opcionesActorScrum'] = [
      {'key':1,'value':'Miembro del equipo de desarrollo'},
      {'key':2,'value':'Maestro Scrum'},
      {'key':3,'value':'Dueño de producto'},
    ]

    #res['fUsuario_opcionesActorScrum'] = oActor.listarActores(showAsKeyValue=True)

    #Action code ends here
    
    return json.dumps(res)

#Clase Login
class clsLogin():

    def __init__(self,engine=None,session=None):
        
        if(engine==None and session==None):
            print("Error en creacion de objeto")
        else:
            self.engine  = engine  #Necesario para realizar consultas e insertar
            self.session = session #Necesario para insertar/borrar columnas

    ''' Metodo encriptar
        Encripta el password del usuario
    '''
    def encriptar(self, value):
        
        encri=clsAccessControl()
        return encri.encript(value)
    
    ''' Metodo longitud
        Retorna la longitud del password
    '''
    def longitud(self, user_password):
        
        longi=clsAccessControl()
        return longi.length_password(user_password)
    
    ''' Metodo check_password
        Verifica la correctitud del password
    '''
    def check_password(self, username, trypass):
        
        decri=clsAccessControl()
        usr=clsDBUser(session=sessionDB,engine=engine)
        passw=usr.buscar(username).split() #Obteniendo el hash de la db
        if passw!=[]:

            result = self.engine.execute("select * from \"Actores\" where \"idActor\"=\'"+passw[4]+"\';")

            count=0
            for row in result:
                count+=1
            if count>0:
                passw=passw[1]
                return decri.check_password(passw,trypass)
            else:
                return False
        else:
            return False

#Use case code starts here

# Clase Usuario        
class clsDBUser():

    def __init__(self,engine=None,session=None):
        
        if(engine==None and session==None):
            print("Error en creacion de objeto")
        else:
            self.engine  = engine  #Necesario para realizar consultas e insertar
            self.session = session #Necesario para insertar/borrar columnas

    ''' Metodo insertar
        Inserta un nuevo usuario a la base de datos
    '''    
    def insertar(self, fullname, username, password,password2, email, idActor):
       
       cript=clsAccessControl()
       act=clsActor(engine=engine,session=sessionDB)
       passToUse=cript.encript(password)
       verif=self.buscar(username)==""
       verif=verif and 0<len(fullname)<=50 and 0<len(username)<=16 and 0<len(password)<=16
       verif=verif and 0<len(email)<=30 and passToUse!=""
       verif=verif and password == password2
       if verif:
           if passToUse!="":
               newuser = dbuser(fullname, username, passToUse, email, idActor) 
               self.session.add(newuser)
               self.session.commit()
               return True
           else:
               return False
           return True
       else:
           return False
       
    ''' Metodo buscar
        Busca a traves del nombre un usuario dentro de la base de datos
    '''  
    def buscar(self, iusername):
        
        result = self.engine.execute("select * from dbuser where username=\'"+iusername+"\';")
        out=""
        if result!="":
            for u in self.session.query(dbuser).instances(result):
                out +=u.username+" "+u.password+" "+u.fullname+\
                " "+u.email+" "+str(u.idActor)+'\n'
        return out

    '''
        Metodo obtenerNombre
        Dado un usuario, busca su nombre asociado
    '''
    def obtenerNombre(self,username):
        
        query = self.session.query(dbuser).filter(dbuser.username == username).first()
        if query != None:
            return query.fullname
        else:
            return ""
        
    ''' Metodo eliminar
        Elimina dentro de la base de datos a un usuario
    '''     
    def eliminar(self, iusername):
                
        self.session.query(dbuser).filter(dbuser.username == iusername).delete()
        self.session.commit()
        
    ''' Metodo listar
        Enlista todos los usarios con su informacion (no password).
    ''' 
    def listar(self):
        
        result = self.engine.execute("select * from dbuser")
        for u in self.session.query(dbuser).instances(result):
            print(u.username, u.fullname, u.email, u.idActor)

      
    ''' Metodo modificar
        Modifica algun atributo de un usuario dentro de la base de datos
    ''' 
    def modificar(self, iusername, ifullname = None, ipassword = None, iemail = None, iidActor = None):
        
        if self.buscar(iusername)!="":
            if ifullname != None:
                self.session.query(dbuser).filter(dbuser.username == iusername).\
                    update({'fullname' : (ifullname) })
                self.session.commit()
            if ipassword != None:
                self.session.query(dbuser).filter(dbuser.username == iusername).\
                    update({'password' : (ipassword) })
                self.session.commit()
            if iemail != None:
                self.session.query(dbuser).filter(dbuser.username == iusername).\
                    update({'email' : (iemail) })
                self.session.commit()
            if iidActor != None:
                self.session.query(dbuser).filter(dbuser.username == iusername).\
                    update({'idActor' : (idActor) }) 
                self.session.commit()


    ''' Metodo obtenerActor
        Permite buscar el nombre de actor asociado al usuario dado
    ''' 
    def obtenerActor(self,username):
        res = self.session.query(dbuser).filter(dbuser.username == username)

        idActor = -1

        for row in res:
            idActor = row.idActor

        if idActor == -1:
            return "Failed"
        else:
            oActor = clsActor(self.engine,self.session)
            res = oActor.obtenerNombre(idActor)
            return res



#Use case code starts here



#Use case code ends here
