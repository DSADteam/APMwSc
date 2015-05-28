import sys
import os
dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../..'))
sys.path.append(dir)

from app.scrum.prod  import clsProducto
from app.scrum.accion import clsAccion
from base import *
import unittest

class accionTester(unittest.TestCase):
    def setUp(self):
        self.acc=clsAccion(engine,sessionDB)
#TEST INSERTAR
#Casos regulares
    def tearDown(self):
        #self.accion.borrarFilas()

        def testinsertar1(self):
            acc = clsAccion()
            pIdProducto = 1
            pdescripcion = 'Accion 1'
            self.acc.insertar(pdescripcion,pIdProducto)
            self.assertTrue(self.acc.existeAccion(descripcion=pdescripcion))

        def testinsertar2(self):
            acc = clsAccion()
            pIdProducto = 2
            pdescripcion = 'A'
            self.acc.insertar(pdescripcion,pIdProducto)
            self.assertTrue(self.acc.existeAccion(descripcion=pdescripcion))
        
#casos frontera

    def testCampoIdNulo(self):
        acc = clsAccion()
        pIdProducto = None
        pdescripcion = 'Accion 3'
        self.acc.insertar(pdescripcion,pIdProducto)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion))

    def testDescripcionNulo(self):
        acc = clsAccion()
        pIdProducto = 1
        pdescripcion = ''
        self.acc.insertar(pdescripcion,pIdProducto)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion))

    def testdescripcion500(self):
        acc = clsAccion()
        pIdProducto = 4
        pdescripcion = 'A'*500
        self.acc.insertar(pdescripcion,pIdProducto)
        self.assertTrue(self.acc.existeAccion(pdescripcion))

    def testNumEnDescrip(self):
        acc = clsAccion()
        pIdProducto = 4
        pdescripcion = 234
        self.acc.insertar(pdescripcion,pIdProducto)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion))

#Caso Esquina


    def todosVacios(self):
        acc = clsAccion()
        pIdProducto = None
        pdescripcion = ''
        self.acc.insertar(pdescripcion,pIdProducto)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion))

    def idVacioyDescrip500(self):
        
        acc = clsAccion()
        pIdProducto = None
        pdescripcion = 'B'*500
        self.acc.insertar(pdescripcion,pIdProducto)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion))

    def testIdNuloyDescripNum(self):
        acc = clsAccion()
        pIdProducto = None
        pdescripcion = 6589
        self.acc.insertar(pdescripcion,pIdProducto)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion))

    def testCharEnIdyDecripNum(self):
        acc = clsAccion()
        pIdProducto = 'bruxw'
        pdescripcion = 345346
        self.acc.insertar(pdescripcion,pIdProducto)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion))

#Caso malicia

    def testcharEnId(self):
        acc = clsAccion()
        pIdProducto = 'idpepe'
        pdescripcion = 'Accion 2'
        self.acc.insertar(pdescripcion,pIdProducto)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion))
    
    def testdescripcion501(self):
        acc = clsAccion()
        pIdProducto = 3
        pdescripcion = 'X'*501
        self.acc.insertar(pdescripcion,pIdProducto)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion))

#TEST MODIFICAR
#casos regulares

    def testModificar1(self):
        acc = clsAccion()
        pIdProducto = 1
        pdescripcion = 'Accion 1'
        self.acc.insertar(pdescripcion,pIdProducto)

        pIdProducto2 = 1
        pdescripcion2 = 'Accion N1'
        test = acc.modificar(pIdProducto2, pdescripcion2)
        self.assertTrue(self.acc.existeAccion(descripcion=pdescripcion2))

#Casos fronteras
    
    def testDescrip500(self):
    
        acc = clsAccion()
        pIdProducto = 2
        pdescripcion = 'l'
        self.acc.insertar(pdescripcion,pIdProducto)

        pIdProducto2 = 2
        pdescripcion2 = 'P'*500
        test = acc.modificar(pIdProducto2, pdescripcion2)
        self.assertTrue(self.acc.existeAccion(descripcion=pdescripcion2))

    def testModifNoValid(self):
        acc = clsAccion()
        pIdProducto = 123
        pdescripcion = 'Accion 123'
        test = acc.modificar(pIdProducto,pdescripcion)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion))

    def testDescripAlMin(self):
        acc = clsAccion()
        pIdProducto = 1
        pdescripcion = 'Accion 1'
        self.acc.insertar(pdescripcion,pIdProducto)

        pIdProducto2 = 1
        pdescripcion2 = 'A'
        test = acc.modificar(pIdProducto2,pdescripcion2)
        self.assertTrue(self.acc.existeAccion(descripcion=pdescripcion2))

#Casos Esquina

    def testModifTodoNul(self):
        acc = clsAccion()
        pIdProducto = 1
        pdescripcion = 'Accion 1'
        self.acc.insertar(pdescripcion,pIdProducto)

        pIdProducto2 = None
        pdescripcion2 = ''
        test = acc.modificar(pIdProducto2,pdescripcion2)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion2))

    def testModifIdNulyDescripNum(self):
        acc = clsAccion()
        pIdProducto = 1
        pdescripcion = 'Accion 1'
        self.acc.insertar(pdescripcion,pIdProducto)

        pIdProducto2 = None
        pdescripcion2 = 345
        test = acc.modificar(pIdProducto2,pdescripcion2)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion2))

    def testModifIdCharyDecripNum(self):
        acc = clsAccion()
        pIdProducto = 1
        pdescripcion = 'Accion 1'
        self.acc.insertar(pdescripcion,pIdProducto)

        pIdProducto2 = 'idpepe'
        pdescripcion2 = 4567
        test = acc.modificar(pIdProducto2,pdescripcion2)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion2))
    
    def testModifIdCharyDescripNul(self):
       
        acc = clsAccion()
        pIdProducto = 1
        pdescripcion = 'Accion 1'
        self.acc.insertar(pdescripcion,pIdProducto)

        pIdProducto2 = 'idpepe'
        pdescripcion2 = ''
        test = acc.modificar(pIdProducto2,pdescripcion2)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion2))


#Casos Malicia

    def testModifCharEnId(self):
        acc = clsAccion()
        pIdProducto2 = 'hola'
        pdescripcion2 = 'Accion p'
        test = self.acc.modificar(pIdProducto2,pdescripcion2)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion2))

    def testModifDescrip501(self):
        acc = clsAccion()
        pIdProducto2 = 2
        pdescripcion2 = 'U'*501
        test = acc.modificar(pIdProducto2,pdescripcion2)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion2))

    def testModifDescripVacio(self):
        acc = clsAccion()
        pIdProducto2 = 1
        pdescripcion2 = ''
        test = self.acc.modificar(pIdProducto2,pdescripcion2)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion2))

    def testModifDescripNum(self):
        acc = clsAccion()
        pIdProducto2 = 3
        pdescripcion2 = 123
        test = self.acc.modificar(pIdProducto2,pdescripcion2)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion2))
    
    def testModifIdNulo(self):
        acc = clsAccion()
        pIdProducto2 = None
        pdescripcion2 = 'Accion nula'
        test = self.acc.modificar(pIdProducto2,pdescripcion2)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion2))

unittest.main()
    