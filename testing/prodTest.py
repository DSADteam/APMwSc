import sys
import os
dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../..'))
sys.path.append(dir)

from app.scrum.prod import clsProducto
from base import *
import unittest


class MdlTest(unittest.TestCase):
    """
        Inicializacion de pruebas 
    """
    def setUp(self):
        self.prod=clsProducto(engine,sessionDB)
    
    #NOTA: correr estas pruebas unitarias con este teardown borraran todos los datos
    #      de la tabla Producto
    def tearDown(self):
        #self.prod.borrarFilas()
        print("")

    """
        Casos frontera
    """
    #Insert con limite interno en maximo de caracteres
    def testInsertAlmostBig(self):
        string = 'a' * 500
        self.prod.insertar(nombre=string)
        self.assertTrue(self.prod.existeProducto(nombre=string),"Error, no se encontro el producto")
    
    #Insert con limite externo de maximo de caracteres
    def testInsertNoWayTooBig(self):
        string = 'a' * 501
        self.prod.insertar(string)
        self.assertFalse(self.prod.existeProducto(nombre=string),"Error, producto insertado y encontrado")

    #Insert con caracteres de utf-8
    def testInsertNiangara(self):
        string = "Producto de investigación de ñandúes y pingüinos para ñiños que usan las letras áéíóúü y @!$*& 888"
        self.prod.insertar(string)
        self.assertTrue(self.prod.existeProducto(nombre=string),"Error, no se encontro el producto")

    """
        Casos esquina
    """
    # Insert con 500 a acentuadas. La a y el acento es utf-8 o multichar?
    def testTildeToTheSquare(self):
        string = "á" * 500
        self.prod.insertar(string)
        self.assertTrue(self.prod.existeProducto(nombre=string),"Error, no se encontro el producto")

    """
        Casos maliciosos
    """

    #Chequeo de proteccion contra inyecciones sql
    def testDontMessMyDb(self):
        #Si falla puede ser solucionado mas adelante con expresiones regulares!
        string = "\" DROP TABLE \"PRODUCTOS\";";
        self.prod.insertar(string)
        self.assertFalse(self.prod.existeProducto(descript=string),"Error, string peligroso encontrado en el sistema")


unittest.main()
