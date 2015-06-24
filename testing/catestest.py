# -*- coding: utf-8 -*-

import sys
import os

dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../..'))
sys.path.append(dir)

from app.scrum.prod       import clsProducto
from app.scrum.historias  import clsHistoria
from app.scrum.accion     import clsAccion
from app.scrum.objetivo   import clsObjetivo
from app.scrum.tareas     import clsTarea
from app.scrum.cates      import clsCategoria
from base import *

import unittest

class CategoriaTester(unittest.TestCase):

     # Inicializacion de casos de prueba
    def setUp(self):

        # Sesion de prueba
        self.cate = clsCategoria(engine,sessionDB)

    #TEST INSERTAR

    #Insertar una categoria que no existe
    def testInsertarInventado(self):
        cNombreCategoria = 'Categoria 1'
        cPeso = 2
        self.cate.insertar(cNombreCategoria, cPeso)
        self.assertTrue(self.cate.existeCategoria(cNombreCategoria))

    #Insertar una categoria que ya existe
    def testInsertarExistente(self):
        cNombreCategoria = 'Crear interfaz'
        cPeso = 3
        self.cate.insertar(cNombreCategoria, cPeso)
        self.assertTrue(self.cate.existeCategoria(cNombreCategoria))

    #Insertar con numeros en categoria
    def testNumerosCategoria(self):
        cNombreCategoria = 34
        cPeso = 3
        self.cate.insertar(cNombreCategoria, cPeso)
        self.assertFalse(self.cate.existeCategoria(cNombreCategoria))

    #Insertar con caracteres en peso
    def testCaracPeso(self):
        cNombreCategoria = 'Crear interfacess'
        cPeso = 'holaa'
        self.cate.insertar(cNombreCategoria, cPeso)
        self.assertFalse(self.cate.existeCategoria(cNombreCategoria))

    # Casos Esquina

    #Insertar categoria vacia y caracteres en peso
    def testCateVaciaPeso(self):
        cNombreCategoria = ''
        cPeso = 'holaa'
        self.cate.insertar(cNombreCategoria, cPeso)
        self.assertFalse(self.cate.existeCategoria(cNombreCategoria))

    #Insertar numeros en categoria y caracteres en peso
    def testCaracPesoNumCate(self):
        cNombreCategoria = 567
        cPeso = 'holaa'
        self.cate.insertar(cNombreCategoria, cPeso)
        self.assertFalse(self.cate.existeCategoria(cNombreCategoria))

    # Casos Malicia

    #Insertar con categoria vacia
    def testCategoriaVacia(self):
        cNombreCategoria = ''
        cPeso = 3
        self.cate.insertar(cNombreCategoria, cPeso)
        self.assertFalse(self.cate.existeCategoria(cNombreCategoria))

    #Insertar en peso vacio
    def testPesoVacio(self):
        cNombreCategoria = 'Crear interfacess'
        cPeso = None
        self.cate.insertar(cNombreCategoria, cPeso)
        self.assertFalse(self.cate.existeCategoria(cNombreCategoria))

if __name__ == "__main__":
    unittest.main()
