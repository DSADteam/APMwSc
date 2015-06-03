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

#Modulos locales
from app.scrum.actor import clsActor
from app.scrum.accion import clsAccion
from app.scrum.objetivo import clsObjetivo

@prod.route('/prod/ACrearProducto', methods=['POST'])
def ACrearProducto():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProductos', 'msg':['Producto creado']}, {'label':'/VCrearProducto', 'msg':['Error al crear producto']}, ]
    res = results[0]
    
    #Action code goes here, res should be a list with a label and a message

    print(params)
    print("AQUI FUE")

    escala = "cualitativo" if (params['escala'] == 1) else "cuantitativo"
    print(escala)
    prd=clsProducto(session=sessionDB,engine=engine)

    # Fuck my life, why? esta como volteado jejeps
    itWorked = prd.insertar(nombre=params['descripcion'],escala=escala,descripcion=params['nombre'])
    res = results[0] if itWorked else results[1]

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

    res['fPila_opcionesEscala'] = [
      {'key':1,'value':'Alta/Media/Baja'},
      {'key':2,'value':'Entre 1 y 20'}]

    params = request.get_json()
    #Action code ends here
    return json.dumps(res)


@prod.route('/prod/AModifProducto', methods=['POST'])
def AModifProducto():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProductos', 'msg':['Producto actualizado']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message
    prd=clsProducto(session=sessionDB,engine=engine)
    prd.modificar(params['idPila'],params['descripcion'])
        
    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)






@prod.route('/prod/VProducto')
def VProducto():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    prd=clsProducto(engine=engine,session=sessionDB)
    
    idPila = int(request.args.get('idPila', 1))

    pilas = prd.listarProductos()


    
    res['idPila'] = idPila
    session['idPila'] = int(idPila)   
    print(session)

    oActor    = clsActor(engine,sessionDB)
    oAccion   = clsAccion(engine,sessionDB)
    oObjetivo = clsObjetivo(engine,sessionDB)
    pilas = pilas = [{'idPila':1, 'nombre':'Pagos en línea', 'descripcion':'Pagos usando tarjeta de débito'}, {'idPila':2, 'nombre':'Recomendaciones de playas', 'descripcion':'Red social para playeros consumados'}, {'idPila':3, 'nombre':'Tu taxi seguro', 'descripcion':'Toma un taxi privado de forma segura'}, ]
    i=0
    for x in pilas:
        print('el magico numero: '+str(i))
        i+=1
        print(x)
        if x['idPila']==idPila:
            res['fPila'] = x
            break
    
    res['data3'] = oActor.listarActoresprod(idPila)
    res['data5'] = oAccion.listarAccionesprod(idPila)
    res['data7'] = oObjetivo.listarObjetivosprod(idPila)

    res['fPila_opcionesEscala'] = [
      {'key':1,'value':'Alta/Media/Baja'},
      {'key':2,'value':'Entre 1 y 20'}]

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
    #Action code ends here'''
    return json.dumps(res)

class clsProducto():
        #Inicializacion 
        def __init__(self,engine=None,session=None):
            if(engine==None and session==None):
                print("Error en creacion de objeto")
            else:
                self.engine  = engine  #Necesario para realizar consultas e insertar
                self.session = session #Necesario para insertar/borrar columnas

        #Funcion para insertar un producto. Indice agregado automaticamente
        def insertar(self,nombre,descripcion,escala):

            tiposCorrectos = (type(nombre) is str) and (type(escala) is str) and\
                             ((type(descripcion) is str) or descripcion == None)             

            formatoEscala  = (escala == "cualitativo" or escala == "cuantitativo")
            estaEnBd       = self.existeProducto(nombre=nombre)
            longCharValido = len(nombre) <= 500 #agregar el de la otra variable


            valido = tiposCorrectos and formatoEscala and (not estaEnBd) \
                     and longCharValido

            if valido:
                # Un campo none no deberia representar ningun problema
                # if not descripcion:
                    # descripcion=""
                newProd = Producto(nombre,escala,descripcion)
                self.session.add(newProd)
                self.session.commit()
                return True
            else:
                return False

        #Funcion booleana, dada un id o descripcion, o ambos, se indica si el objeto esta en la tabla
        def existeProducto(self,id=None,nombre=None):
            if(id != None and nombre==None):
                result  = self.engine.execute("select * from \"Productos\" where \'idProducto\'="+str(id)+";")
            elif(id ==None and nombre!=None):
                result  = self.engine.execute("select * from \"Productos\" where nombre=\'"+nombre+"\';")
            elif(id !=None and nombre!=None):
                result  = self.engine.execute("select * from \"Productos\" where \'idProducto\'="+str(id)+" and nombre=\'"+nombre+"\';")
            else:
                return False
            
            contador = 0
            for row in result:
                contador += 1

            return contador != 0

        #Funcion que entrega el id de un producto, dado su nombre
        def idProd(self,nombre):
            if self.existeProducto(nombre=nombre):
                result = self.engine.execute("select * from \"Productos\" where nombre=\'"+nombre+"\';")
                for row in result:
                    resId = row[0]

                return resId

            else: 
                return -1

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
                return True
            else:
                return False
