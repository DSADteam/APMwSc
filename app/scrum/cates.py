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
cates = Blueprint('cates', __name__)
from base import *

@cates.route('/cates/ACrearCategoria', methods=['POST'])
def ACrearCategoria():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VCategorias', 'msg':['Categoría creada.']}, {'label':'/VCategorias', 'msg':['Error al intentar crear categoría.']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message
    cates = clsCategoria(engine,sessionDB)
    cates.insertar(params['nombre'],params['peso'])


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@cates.route('/cates/AElimCategoria')
def AElimCategoria():
    #GET parameter
    idCategoria = request.args['idCategoria']
    results = [{'label':'/VCategorias', 'msg':['Categoría eliminada.']}, {'label':'/VCategorias', 'msg':['Error al intentar eliminar categoría.']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@cates.route('/cates/AModifCategoria', methods=['POST'])
def AModifCategoria():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VCategorias', 'msg':['Categoría actualizada.']}, {'label':'/VCategorias', 'msg':['Error al intentar modificar categoría.']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@cates.route('/cates/VCategoria')
def VCategoria():
    #GET parameter
    idCategoria = request.args['idCategoria']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']
    res['idCategoria'] = int(idCategoria)
    res['fCategoria'] = {'idCategoria':1, 'peso':3, 
                         'nombre':'Reparacíon edl motor'}


    #Action code ends here
    return json.dumps(res)



@cates.route('/cates/VCategorias')
def VCategorias():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']
    res['data0'] = [
      {'idCategoria':1, 'peso':1, 'nombre':'Reparación del parachoques' },
      {'idCategoria':2, 'peso':2, 'nombre':'Reparación de la carrocería' },
      {'idCategoria':3, 'peso':3, 'nombre':'Reparación del motor' },
    ]
    cates = clsCategoria(engine,sessionDB)
    res['data0'] = cates.listarTodo()

    #Action code ends here
    return json.dumps(res)





#Use case code starts here
class clsCategoria():
    
    def __init__(self,engine=None,session=None):
        self.engine  = engine
        self.session = session
        
    def insertar(self,nombreCategoria,peso):

        tiposCorrectos = (type(nombreCategoria) is str) and \
                         (type(peso) is int)      

        if not tiposCorrectos:
            return False


       
        valoresValido = (nombreCategoria != '') and (peso >= 0) 

        if not valoresValido:
            return False
        
        producto = self.session.query(Categoria).filter(Categoria.nombreCategoria == nombreCategoria)
        existeProducto = producto.count() > 0

        longCharValido = (len(nombreCategoria) <= 50)

        if  longCharValido and (not existeProducto):
            newCat = Categoria(nombreCategoria,peso)
            self.session.add(newCat)
            self.session.commit()
            return True
        else:
            return False

    def listarTodo(self):
        res=[]
        

        result = self.session.query(Categoria)
        i=1
        for row in result:
            res+=[
                    {'idCategoria'  :row.idCategoria, 
                     'nombre'       :row.nombreCategoria, 
                     'peso'         :row.peso},
                 ]
            i=i+1
        
        return res

    def listarKeyValue(self):
        res=[]
        

        result = self.session.query(Categoria)
        i=1
        for row in result:
            res+=[
                    {'key'  :row.nombreCategoria, 
                     'value':row.nombreCategoria, 
                     'peso' :row.peso},
                 ]
            i=i+1
        
        return res

#Use case code ends here

