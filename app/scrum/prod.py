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
prod = Blueprint('prod', __name__)
from base import *

#engine = create_engine(URL(**data.settings.DATABASE))
#DBSession h= sessionmaker(bind = engine)
#s = DBSession()


@prod.route('/prod/ACrearProducto', methods=['POST'])
def ACrearProducto():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProductos', 'msg':['Producto creado']}, {'label':'/VCrearProducto', 'msg':['Error al crear producto']}, ]
    res = results[0]
    
    #Action code goes here, res should be a list with a label and a message
    # newProd = Producto(params['descripcion'])
    # session.add(newProd)
    # session.commit()

    print(params)
    prd=clsProducto(session=sessionDB)
    prd.insertar(nombre=params['descripcion'])
    
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
    prd=clsProducto(session=sessionDB)
    prd.modificar(params['idPila'],params['descripcion'])
        
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
    prd=clsProducto(engine=engine)
    #res['data0'] = prd.listarProductos()
    
    idPila = int(request.args.get('idPila', 1))
    pilas = prd.listarProductos()
    #pilas = [{'idPila':1, 'nombre':'Pagos en línea', 'descripcion':'Pagos usando tarjeta de débito'}, {'idPila':2, 'nombre':'Recomendaciones de playas', 'descripcion':'Red social para playeros consumados'}, {'idPila':3, 'nombre':'Tu taxi seguro', 'descripcion':'Toma un taxi privado de forma segura'}, ]
    print(pilas)
    res['fPila'] = pilas[idPila-1]
    res['data3'] = [{'idActor':1, 'descripcion':'Actor 1'}, {'idActor':2, 'descripcion':'Actor 2'}, {'idActor':3, 'descripcion':'Actor 3'},  ]
    res['data5'] = [{'idAccion':1, 'descripcion':'Accion 1'}, {'idAccion':2, 'descripcion':'Accion 2'}, {'idAccion':3, 'descripcion':'Accion 3'}, {'idAccion':4, 'descripcion':'Accion 4'}, ]
    res['data7'] = [{'idObjetivo':1, 'descripcion':'Objetivo 1'}, {'idObjetivo':2, 'descripcion':'Objetivo 2'}, {'idObjetivo':3, 'descripcion':'Objetivo 3'}, {'idObjetivo':4, 'descripcion':'Objetivo 4'}, {'idObjetivo':5, 'descripcion':'Objetivo 5'},  ]
    res['idPila'] = idPila    

    #clsActor()
    res['data3']

    #Action code ends here
    return json.dumps(res)



@prod.route('/prod/VProductos')
def VProductos():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    
    prd=clsProducto(engine=engine)
    res['data0'] = prd.listarProductos()
    
    #res['data0'].append({'idPila':"WTF",'nombre':"otroWTF"})
    #Action code ends here'''
    return json.dumps(res)

class clsProducto():
        #Inicializacion 
        def __init__(self,engine=None,session=None):

            if(engine==None and session==None):
                print("Error en creacion de objeto")
            else:
                self.engine  = engine  #Necesario para realizar consultas
                self.session = session #Necesario para insertar/borrar columnas

        #Funcion para insertar un producto. Indice agregado automaticamente
        def insertar(self,nombre,descripcion=None):
            comentarioNulo = (nombre == None)
            if comentarioNulo:
                return False

            estaEnBd       = self.existeProducto(nombre=descripcion)
            longCharValido = len(nombre) <= 500

            if (not estaEnBd) and (longCharValido) and (not comentarioNulo):
                if not descripcion:
                    descripcion=""
                newProd = Producto(nombre,descripcion)
                self.session.add(newProd)
                self.session.commit()
                return True
            else:
                return False

        #Funcion booleana, dada un id o descripcion, o ambos, se indica si el objeto esta en la tabla
        def existeProducto(self,id=None,nombre=None,descript=None):
            if(id != None and nombre==None):
                result  = self.engine.execute("select * from \"Productos\" where \'idProducto\'="+str(id)+";")
            elif(id ==None and nombre!=None):
                result  = self.engine.execute("select * from \"Productos\" where nombre=\'"+descript+"\';")
            elif(id !=None and nombre!=None):
                result  = self.engine.execute("select * from \"Productos\" where \'idProducto\'="+str(id)+" and nombre=\'"+nombre+"\';")
            else:
                return False
            
            contador = 0
            for row in result:
                contador += 1

            return contador != 0

        #Funcion que lista los productos en una lista de diccionarios
        #compatible con json
        def listarProductos(self):
            res = []
            result = self.engine.execute("select * from \"Productos\";")
            if result!="":
                for row in result:
                    if (row.descripcion):
                        res.append({'idPila':row.idProducto,'nombre':row.nombre, 'descripcion':row.descripcion})
                    else:
                        res.append({'idPila':row.idProducto,'nombre':row.nombre, 'descripcion':''})
                #else:
                #    print("Empty query!")
            
            return res

        #Funcion que elimina todas las filas
        def borrarFilas(self):
            self.session.query(Producto).delete()
            self.session.commit()
        
        #Funcion que permite actualizar una descripcion
        def modificar(self,id=None,descripcion=None):
            if (not descripcion):
                descripcion==""
            if id:
                self.session.query(Producto).filter(Producto.idProducto == id).\
                    update({'descripcion' : descripcion })
                self.session.commit()
                print(descripcion+"Oh yeahhhhhhhhhhhhhhhh")
                return True
            else:
                return False
