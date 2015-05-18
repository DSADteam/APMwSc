# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json
from werkzeug import check_password_hash

import sys
import os
dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../..'))
sys.path.append(dir)

from app.scrum.encrypt import clsAccessControl


ident = Blueprint('ident', __name__)

from base import *
from app.scrum.actor import clsActor

@ident.route('/ident/AIdentificar', methods=['POST'])
def AIdentificar():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProductos', 'msg':['Bienvenido dueño de producto'], "actor":"duenoProducto"}, {'label':'/VMaestroScrum', 'msg':['Bienvenido Maestro Scrum'], "actor":"maestroScrum"}, {'label':'/VDesarrollador', 'msg':['Bienvenido Desarrollador'], "actor":"desarrollador"}, {'label':'/VLogin', 'msg':['Datos de identificación incorrectos']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message
    log=clsLogin(session=sessionDB,engine=engine)
    resp=log.check_password(params.get('usuario'),params.get('clave'))
    if resp:
        res=results[0]
    else:
        res=results[3]
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
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


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
    

    #Action code ends here
    return json.dumps(res)



@ident.route('/ident/VRegistro')
def VRegistro():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)


class clsLogin():

    def __init__(self,engine=None,session=None):
        if(engine==None and session==None):
            print("Error en creacion de objeto")
        else:
            self.engine  = engine  #Necesario para realizar consultas e insertar
            self.session = session #Necesario para insertar/borrar columnas

    def encriptar(self, value):
        encri=clsAccessControl()
        return encri.encript(value)

    def longitud(self, user_password):
        longi=clsAccessControl()
        return longi.length_password(user_password)
    
    def check_password(self, username, trypass):
        decri=clsAccessControl()
        usr=clsDBUser(session=sessionDB,engine=engine)
        passw=usr.buscar(username).split() #Obteniendo el hash de la db
        if passw!=[]:
            result = self.engine.execute("select * from \"Actores\" where \"idActor\"="+passw[4]+" and nombre='Product Owner';")
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
        
    def insertar(self, fullname, username, password, email, idActor):
       cript=clsAccessControl()
       act=clsActor(engine=engine,session=sessionDB)
       passToUse=cript.encript(password)
       verif=self.buscar(username)=="" and act.existeActor(idActor=idActor)!=""
       verif=verif and 0<len(fullname)<=50 and 0<len(username)<=16 and 0<len(password)<=16
       verif=verif and 0<len(email)<=30 and passToUse!=""
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


#Use case code starts here


#Use case code ends here
