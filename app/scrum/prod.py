# -*- coding: utf-8 -*-

#Agregando proyect root
import sys
import os
dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../..'))
print(dir)
sys.path.append(dir)

#Dependencias flask
from flask import request, session, Blueprint, json
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

#Definicion de blueprint y bd
prod = Blueprint('prod', __name__)
from base import Producto


from flask import Flask, request, session
from flask.ext.script import Manager, Server
from random import SystemRandom
from datetime import timedelta
import os
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, ForeignKey

from flask.ext.migrate import Migrate, MigrateCommand
####
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, PrimaryKeyConstraint, UniqueConstraint, Sequence


app = Flask(__name__, static_url_path='')
manager = Manager(app)
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '127.0.0.1')
)


app.config['DATABASE'] = {
            'drivername': 'postgres',
            'host': 'localhost',
            'port': '5432',
            'username': 'apmwsc',
            'password': 'safepassword',
            'database': 'apmwsc'
            }



#engine = create_engine(URL(**data.settings.DATABASE))
#DBSession h= sessionmaker(bind = engine)
#s = DBSession()

engine = create_engine(URL(**app.config['DATABASE']))
DBSession = sessionmaker(bind = engine)

session = DBSession()

@prod.route('/prod/ACrearProducto', methods=['POST'])
def ACrearProducto():
    #POST/PUT parameters
    params = request.get_json()

    results = [{'label':'/VProductos', 'msg':['Producto creado']}, {'label':'/VCrearProducto', 'msg':['Error al crear producto']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message
    newProd = Producto(params['descripcion'])
    session.add(newProd)
    session.commit()
    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@prod.route('/prod/AModifProducto', methods=['POST'])
def AModifProducto():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProductos', 'msg':['Producto actualizado']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message
    print(params) #Borrar
    
    session.query(Producto).filter(Producto.idProducto == int(params['idProducto'])).\
        update({'descripcion' : (params['descripcion']) })
    session.commit()
        
    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@prod.route('/prod/VCrearProducto')
def VCrearProducto():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    params = request.get_json()
    print(params)
    #Action code ends here
    return json.dumps(res)



@prod.route('/prod/VProducto')
def VProducto():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    idPila = int(request.args.get('idPila', 1))
    pilas = [{'idPila':1, 'nombre':'Pagos en línea', 'descripcion':'Pagos usando tarjeta de débito'}, {'idPila':2, 'nombre':'Recomendaciones de playas', 'descripcion':'Red social para playeros consumados'}, {'idPila':3, 'nombre':'Tu taxi seguro', 'descripcion':'Toma un taxi privado de forma segura'}, ]
    res['fPila'] = pilas[idPila-1]
    res['data3'] = [{'idActor':1, 'descripcion':'Actor 1'}, {'idActor':2, 'descripcion':'Actor 2'}, {'idActor':3, 'descripcion':'Actor 3'},  ]
    res['data5'] = [{'idAccion':1, 'descripcion':'Accion 1'}, {'idAccion':2, 'descripcion':'Accion 2'}, {'idAccion':3, 'descripcion':'Accion 3'}, {'idAccion':4, 'descripcion':'Accion 4'}, ]
    res['data7'] = [{'idObjetivo':1, 'descripcion':'Objetivo 1'}, {'idObjetivo':2, 'descripcion':'Objetivo 2'}, {'idObjetivo':3, 'descripcion':'Objetivo 3'}, {'idObjetivo':4, 'descripcion':'Objetivo 4'}, {'idObjetivo':5, 'descripcion':'Objetivo 5'},  ]
    res['idPila'] = idPila    

    #Action code ends here
    return json.dumps(res)



@prod.route('/prod/VProductos')
def VProductos():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #res['data0'] = [{'idPila':1, 'nombre':'Pagos en línea'}, {'idPila':2, 'nombre':'Recomendaciones de playas'}, {'idPila':3, 'nombre':'Tu taxi seguro'}, ]
    

     #cAUSANTE DEL CONFICLTO
    #res['actor']=session['actor'] #Forzado de actor

    res['data0'] = []
    result = engine.execute("select * from \"Products\";")
    if result!="":
        for row in result:
            res['data0'].append({'idPila':row.idProducto,'nombre':row.descripcion})
    else:
            print("Empty query!")
    
    #res['data0'].append({'idPila':"WTF",'nombre':"otroWTF"})
    #Action code ends here'''
    return json.dumps(res)





#Use case code starts here

#Use case code ends here