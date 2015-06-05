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

	# Insertar de producto 

    """
        Casos frontera
    """
    #Insert con limite interno en maximo de caracteres
    def testInsertAlmostBig(self):

        string = 'a' * 500
        descripcion = 'jejeps'
        escala = 'cuantitativo'
        self.prod.insertar(nombre=string, descripcion=descripcion, escala=escala)
        self.assertTrue(self.prod.existeProducto(nombre=string),"Error, no se encontro el producto")
    
    def testInsertAlmostBig2(self):

        string = 'u' * 500
        descripcion = 'jejepssusu'
        escala = 'scrum cuantitativo'
        self.prod.insertar(nombre=string, descripcion=descripcion, escala=escala)
        self.assertFalse(self.prod.existeProducto(nombre=string),"Error, no se encontro el producto")
    
    #Insert con limite externo de maximo de caracteres
    def testInsertNoWayTooBig(self):

        string = 'o' * 501
        descripcion = 'jejeps2'
        escala = 'cualitativo'
        self.prod.insertar(string, descripcion=descripcion, escala=escala)
        self.assertFalse(self.prod.existeProducto(nombre=string),"Error, producto insertado y encontrado")

    def testInsertNoWayTooBig2(self):

        string = 'o' * 501
        descripcion = 'jejeps3'
        escala = 'hola'
        self.prod.insertar(string, descripcion=descripcion, escala=escala)
        self.assertFalse(self.prod.existeProducto(nombre=string),"Error, producto insertado y encontrado")

    #Insert con caracteres de utf-8
    def testInsertNiangara(self):

        string = "Producto de investigación de ñandúes y pingüinos para ñiños que usan las letras áéíóúü y @!$*& 888"
        descripcion = 'jejeps3'
        escala = 'cualitativo'
        self.prod.insertar(string, descripcion=descripcion, escala=escala)
        self.assertTrue(self.prod.existeProducto(nombre=string),"Error, no se encontro el producto")

    """
        Casos esquina
    """

    # Insert con 500 a acentuadas.
    # descripcion del mismo tam
    def testTildeToTheSquare(self):

        string = "ó" * 500
        descripcion = "ó" * 500
        escala = 'cuantit'
        self.prod.insertar(string, descripcion=descripcion, escala=escala)
        self.assertFalse(self.prod.existeProducto(nombre=string),"Error, no se encontro el producto")
    
    def testTildeToTheSquare2(self):

        string = "á" * 500
        descripcion = "á" * 500
        escala = 'cuantitativo'
        self.prod.insertar(string, descripcion=descripcion, escala=escala)
        self.assertTrue(self.prod.existeProducto(nombre=string),"Error, no se encontro el producto")

    """
        Casos maliciosos
    """

    #Chequeo de proteccion contra inyecciones sql
    def testDontMessMyDb(self):

        string = "\" DROP TABLE \"PRODUCTOS\";";
        descripcion = 'jejeps4'
        escala = 'cualitativo'
        self.prod.insertar(string, descripcion=descripcion, escala=escala)
        self.assertTrue(self.prod.existeProducto(nombre=string),"Error, string peligroso encontrado en el sistema")

    def testTildeToTheSquare3(self):

        string = "ó" * 500
        descripcion = "ó" * 500
        escala = 123
        self.prod.insertar(string, descripcion=descripcion, escala=escala)
        self.assertFalse(self.prod.existeProducto(nombre=string),"Error, no se encontro el producto")

    def testTildeToTheSquare4(self):

        string = "ó" * 500
        descripcion = "ó" * 500
        escala = None
        self.prod.insertar(string, descripcion=descripcion, escala=escala)
        self.assertFalse(self.prod.existeProducto(nombre=string),"Error, no se encontro el producto")

    

    def testDescripcionNumber(self):
        
        string = 'Holaaaa'
        descripcion = 1234
        escala = 'cualitativo'
        self.prod.insertar(string, descripcion=descripcion, escala=escala)
        self.assertFalse(self.prod.existeProducto(nombre=string),"Error, no se encontro el producto")

    # Modificar de producto
    #Valido
    def testModif1(self):
        string = "cualquiernombre"
        descripcion = 'holas'
        escala = 'cualitativo'
        self.prod.modificar(1,string, descripcion=descripcion, escala=escala)
        self.assertTrue(self.prod.existeProducto(nombre=string),"Error, no se encontro el producto")
    #Fronteras   
    def testModif2(self):
        string = "o"*500
        descripcion = 'holas'
        escala = 'cualitativo'
        self.prod.modificar(1,string, descripcion=descripcion, escala=escala)
        self.assertTrue(self.prod.existeProducto(nombre=string),"Error, no se encontro el producto")
         
    def testModif3(self):
        string = "cualquiernombredos"
        descripcion = "o"*500
        escala = 'cualitativo'
        self.prod.modificar(1,string, descripcion=descripcion, escala=escala)
        self.assertTrue(self.prod.existeProducto(nombre=string),"Error, no se encontro el producto")
    
    def testModif4(self):
        string = "cualquiernombretres"
        descripcion = 'u'*501
        escala = 'cualitativo'
        self.prod.modificar(1,string, descripcion=descripcion, escala=escala)
        self.assertFalse(self.prod.existeProducto(nombre=string),"Error, no se encontro el producto")
    
    def testModif8(self):
        string = "unstring"
        descripcion = 'holas'
        escala = 'no es cualitativo ok'
        self.prod.modificar(1,string, descripcion=descripcion, escala=escala)
        self.assertFalse(self.prod.existeProducto(nombre=string),"Error, no se encontro el producto")
    #Esquina     
    def testModif5(self):
        string = 'k'*501
        descripcion = 'z'*501
        escala = 'cualitativo'
        self.prod.modificar(1,string, descripcion=descripcion, escala=escala)
        self.assertFalse(self.prod.existeProducto(nombre=string),"Error, no se encontro el producto")
    #Malicia    
    def testModif6(self):
        string = None
        descripcion = 'holas'
        escala = 'cualitativo'
        self.prod.modificar(1,string, descripcion=descripcion, escala=escala)
        self.assertFalse(self.prod.existeProducto(nombre=string),"Error, no se encontro el producto")
        
    def testModif7(self):
        string = "holahola"
        descripcion = 454545
        escala = 'cualitativo'
        self.prod.modificar(1,string, descripcion=descripcion, escala=escala)
        self.assertFalse(self.prod.existeProducto(nombre=string),"Error, no se encontro el producto")
    
    def testModif88(self):
        string = "unstring"
        descripcion = 'holas'
        escala = 78787878
        self.prod.modificar(1,string, descripcion=descripcion, escala=escala)
        self.assertFalse(self.prod.existeProducto(nombre=string),"Error, no se encontro el producto")
        
    def testModif9(self):
        string = "unstring"
        descripcion = 'holas'
        escala = None
        self.prod.modificar(1,string, descripcion=descripcion, escala=escala)
        self.assertFalse(self.prod.existeProducto(nombre=string),"Error, no se encontro el producto")
        
   

unittest.main()
