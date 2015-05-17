import unittest
import os
import sys
dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../..'))
sys.path.append(dir)
from app.scrum.accion import clsAccion
from base import *

class accionTester(unittest.TestCase):
     
#TEST INSERTAR
#Casos regulares

    def testinsertar1(self):
        acc = clsAccion()
        pIdProducto = 1
        pdescripcion = 'Accion 1'
        test = acc.insertar(pdescripcion,pIdProducto)
        self.assertTrue(test)

    def testinsertar2(self):
        acc = clsAccion()
        pIdProducto = 2
        pdescripcion = 'A'
        test = acc.insertar(pdescripcion,pIdProducto)
        self.assertTrue(test)

#casos frontera

    def testCampoIdNulo(self):
        acc = clsAccion()
        pIdProducto = None
        pdescripcion = 'Accion 3'
        test = acc.insertar(pdescripcion,pIdProducto)
        self.assertFalse(test)

    def testDescripcionNulo(self):
        acc = clsAccion()
        pIdProducto = 1
        pdescripcion = ''
        test = acc.insertar(pdescripcion,pIdProducto)
        self.assertFalse(test)

    def testdescripcion500(self):
        acc = clsAccion()
        pIdProducto = 4
        pdescripcion = 'Haciendo una prueba donde el espacio de lineas es tan largo que debe dar 500 palabras en la descripcion del modulo accion y ya me canse de escribir tanto asi que a partir de ahora pondre puro HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR y el fin'
        test = acc.insertar(pdescripcion,pIdProducto)
        self.assertTrue(test)

    def testNumEnDescrip(self):
        acc = clsAccion()
        pIdProducto = 4
        pdescripcion = 234
        test = acc.insertar(pdescripcion,pIdProducto)
        self.assertFalse(test)

#Caso Esquina

    def todosVacios(self):
        acc = clsAccion()
        pIdProducto = None
        pdescripcion = ''
        test = acc.insertar(pdescripcion,pIdProducto)
        self.assertFalse(test)

    def idVacioyDescrip500(self):
        acc = clsAccion()
        pIdProducto = None
        pdescripcion = 'El Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of W'
        test = acc.insertar(pdescripcion,pIdProducto)
        self.assertFalse(test)

    def testIdNuloyDescripNum(self):
        acc = clsAccion()
        pIdProducto = None
        pdescripcion = 6589
        test = acc.insertar(pdescripcion,pIdProducto)
        self.assertFalse(test)

    def testCharEnIdyDecripNum(self):
        acc = clsAccion()
        pIdProducto = 'bruxw'
        pdescripcion = 345346
        test = acc.insertar(pdescripcion,pIdProducto)
        self.assertFalse(test)

#Caso malicia

    def testcharEnId(self):
        acc = clsAccion()
        pIdProducto = 'idpepe'
        pdescripcion = 'Accion 2'
        test = acc.insertar(pdescripcion,pIdProducto)
        self.assertFalse(test)
    
    def testdescripcion501(self):
        acc = clsAccion()
        pIdProducto = 3
        pdescripcion = 'El Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of WA'
        test = acc.insertar(pdescripcion,pIdProducto)
        self.assertFalse(test)

#TEST MODIFICAR
#casos regulares

    def testModificar1(self):
        acc = clsAccion()
        pIdProducto = 1
        pdescripcion = 'Accion 1'
        acc.insertar(pdescripcion,pIdProducto)

        pIdProducto2 = 1
        pdescripcion2 = 'Accion N1'
        test = acc.modificar(pdescripcion2,pIdProducto2)
        self.assertTrue(test)

#Casos fronteras
    
    def testDescrip500(self):
        acc = clsAccion()
        pIdProducto = 2
        pdescripcion = 'El Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of W'
        acc.insertar(pdescripcion,pIdProducto)

        pIdProducto2 = 2
        pdescripcion2 = 'el Mall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of W'
        test = acc.modificar(pdescripcion2,pIdProducto2)
        self.assertTrue(test)

    def testModifNoValid(self):
        acc = clsAccion()
        test = acc.modificar(123,"Accion 123")
        self.assertFalse(test)

    def testDescripAlMin(self):
        acc = clsAccion()
        pIdProducto = 1
        pdescripcion = 'Accion 1'
        acc.insertar(pIdAccion,pdescripcion,pIdProducto)

        pIdProducto2 = 1
        pdescripcion2 = 'A'
        test = acc.modificar(pIdProducto2,pdescripcion2)
        self.assertTrue(test)

#Casos Esquina

    def testModifTodoNul(self):
        acc = clsAccion()
        pIdProducto = 1
        pdescripcion = 'Accion 1'
        acc.insertar(pdescripcion,pIdProducto)

        pIdProducto2 = None
        pdescripcion2 = ''
        test = acc.modificar(pIdAccion2,pdescripcion2)
        self.assertFalse(test)

    def testModifIdNulyDescripNum(self):
        acc = clsAccion()
        pIdProducto = 1
        pdescripcion = 'Accion 1'
        acc.insertar(pdescripcion,pIdProducto)

        pIdProducto2 = None
        pdescripcion2 = 345
        test = acc.modificar(pIdProducto2,pdescripcion2)
        self.assertFalse(test)

    def testModifIdCharyDecripNum(self):
        acc = clsAccion()
        pIdProducto = 1
        pdescripcion = 'Accion 1'
        acc.insertar(pdescripcion,pIdProducto)

        pIdProducto2 = 'idpepe'
        pdescripcion2 = 4567
        test = acc.modificar(pIdProducto2,pdescripcion2)
        self.assertFalse(test)
    
    def testModifIdCharyDescripNul(self):
        acc = clsAccion()
        pIdProducto = 1
        pdescripcion = 'Accion 1'
        acc.insertar(pdescripcion,pIdProducto)

        pIdProducto2 = 'idpepe'
        pdescripcion2 = ''
        test = acc.modificar(pIdProducto2,pdescripcion2)
        self.assertFalse(test)


#Casos Malicia

    def testModifCharEnId(self):
        acc = clsAccion()
        pIdProducto2 = 'hola'
        pdescripcion2 = 'Accion p'
        test = acc.modificar(pIdProducto2,pdescripcion2)
        self.assertFalse(test)

    def testModifDescrip501(self):
        acc = clsAccion()
        pIdProducto2 = 2
        pdescripcion2 = 'El Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of WA'
        test = acc.modificar(pIdProducto2,pdescripcion2)
        self.assertFalse(test)

    def testModifDescripVacio(self):
        acc = clsAccion()
        pIdProducto2 = 1
        pdescripcion2 = ''
        test = acc.modificar(pIdProducto2,pdescripcion2)
        self.assertFalse(test)

    def testModifDescripNum(self):
        acc = clsAccion()
        pIdProducto2 = 3
        pdescripcion2 = 123
        test = acc.modificar(pIdProducto2,pdescripcion2)
        self.assertFalse(test)
    
    def testModifIdNulo(self):
        acc = clsAccion()
        pIdProducto2 = None
        pdescripcion2 = 'Accion nula'
        test = acc.modificar(pIdProducto2,pdescripcion2)
        self.assertFalse(test)


unittest.main()
    