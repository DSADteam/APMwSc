import sys
import os
dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../..'))
sys.path.append(dir)

from app.scrum.prod  import clsProducto
from app.scrum.actor import clsActor
from base import *
import unittest

class actorTester(unittest.TestCase):
     
    def testinsertar1(self):
        acc = clsActor()
        pnombre = 'pedro'
        pIdProducto = 1
        pdescripcion = 'Actor 1'
        acc.insertar(pnombre,pdescripcion,pIdProducto)
        self.assertTrue(existeActor(nombre=pnombre))

    def testinsertar2(self):
        acc = clsActor()
        pnombre = 'pedrito'
        pIdProducto = 2
        pdescripcion = 'A'
        acc.insertar(pnombre,pdescripcion,pIdProducto)
        self.assertTrue(existeActor(nombre=pnombre))

#casos frontera

    def testCampoIdNulo(self):
        acc = clsActor()
        pnombre = 'jose'
        pIdProducto = None
        pdescripcion = 'Actor 3'
        acc.insertar(pnombre,pdescripcion,pIdProducto)
        self.assertTrue(existeActor(nombre=pnombre))

    def testDescripcionNulo(self):
        acc = clsActor()
        pnombre = 'josue'
        pIdProducto = 1
        pdescripcion = ''
        acc.insertar(pnombre,pdescripcion,pIdProducto)
        self.assertTrue(existeActor(nombre=pnombre))

    def testdescripcion500(self):
        acc = clsActor()
        pnombre = 'eli'
        pIdProducto = 4
        pdescripcion = 'Haciendo una prueba donde el espacio de lineas es tan largo que debe dar 500 palabras en la descripcion del modulo accion y ya me canse de escribir tanto asi que a partir de ahora pondre puro HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR y el fin'
        acc.insertar(pnombre,pdescripcion,pIdProducto)
        self.assertTrue(existeActor(nombre=pnombre))

    def testNumEnDescrip(self):
        acc = clsActor()
        pnombre = 'chiabe'
        pIdProducto = 4
        pdescripcion = 234
        acc.insertar(pnombre,pdescripcion,pIdProducto)
        self.assertTrue(existeActor(nombre=pnombre))

#Caso Esquina

    def todosVacios(self):
        acc = clsActor()
        pnombre = 'chiabes'
        pIdProducto = None
        pdescripcion = ''
        acc.insertar(pnombre,pdescripcion,pIdProducto)
        self.assertTrue(existeActor(nombre=pnombre))

    def idVacioyDescrip500(self):
        acc = clsActor()
        pnombre = 'teama'
        pIdProducto = None
        pdescripcion = 'El Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of W'
        acc.insertar(pnombre,pdescripcion,pIdProducto)
        self.assertTrue(existeActor(nombre=pnombre))

    def testIdNuloyDescripNum(self):
        acc = clsActor()
        pnombre = 'teruel'
        pIdProducto = None
        pdescripcion = 6589
        acc.insertar(pnombre,pdescripcion,pIdProducto)
        self.assertTrue(existeActor(nombre=pnombre))

    def testCharEnIdyDecripNum(self):
        acc = clsActor()
        pnombre = ''
        pIdProducto = 'bruxw'
        pdescripcion = 345346
        acc.insertar(pnombre,pdescripcion,pIdProducto)
        self.assertTrue(existeActor(nombre=pnombre))

#Caso malicia

    def testcharEnId(self):
        acc = clsActor()
        pnombre = 'jirafa'
        pIdProducto = 'idpepe'
        pdescripcion = 'Actor 2'
        acc.insertar(pnombre,pdescripcion,pIdProducto)
        self.assertTrue(existeActor(nombre=pnombre))
    
    def testdescripcion501(self):
        acc = clsActor()
        pnombre = 'perro'
        pIdProducto = 3
        pdescripcion = 'El Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of WA'
        acc.insertar(pnombre,pdescripcion,pIdProducto)
        self.assertTrue(existeActor(nombre=pnombre))

#TEST MODIFICAR
#casos regulares

    def testModificar1(self):
        acc = clsActor()
        pnombre = 'nabil'
        pIdProducto = 1
        pdescripcion = 'Actor 1'
        acc.insertar(pnombre,pdescripcion,pIdProducto)
        
        pnombre2= 'coki'
        pIdProducto2 = 1
        pdescripcion2 = 'Actor N1'
        test = acc.modificar(pIdProducto2,pnombre2, pdescripcion2)
        self.assertTrue(existeActor(nombre=pnombre2))

#Casos fronteras
    
    def testDescrip500(self):
        acc = clsActor()
        pnombre = 'cristina'
        pIdProducto = 2
        pdescripcion = 'El Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of W'
        acc.insertar(pnombre,pdescripcion,pIdProducto)

        pnombre2= 'oil'
        pdescripcion2 = 'el Mall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of W'
        test = acc.modificar(pIdProducto,pnombre2, pdescripcion2)
        self.assertTrue(existeActor(nombre=pnombre2))

    def testModifNoValid(self):
        acc = clsActor()
        pIdProducto = 123
        pdescripcion = 'Actor 123'
        pnombre2= 'tini'
        test = acc.modificar(pIdProducto,pnombre2,pdescripcion)
        self.assertFalse(existeActor(nombre=pnombre2))

    def testDescripAlMin(self):
        acc = clsActor()
        pnombre = 'roberto'
        pIdProducto = 1
        pdescripcion = 'Actor 1'
        acc.insertar(pnombre,pdescripcion,pIdProducto)
        
        pnombre2= 'nuevo'
        pIdProducto2 = 1
        pdescripcion2 = 'A'
        test = acc.modificar(pIdProducto2,pnombre2,pdescripcion2)
        self.assertTrue(existeActor(nombre=pnombre2))

#Casos Esquina

    def testModifTodoNul(self):
        acc = clsActor()
        pnombre = 'meggie'
        pIdProducto = 1
        pdescripcion = 'Actor 1'
        acc.insertar(pnombre,pdescripcion,pIdProducto)
        
        
        pnombre2= ''
        pIdProducto2 = None
        pdescripcion2 = ''
        test = acc.modificar(pIdProducto2,pnombre2,pdescripcion2)
        self.assertFalse(existeActor(nombre=pnombre2))

    def testModifIdNulyDescripNum(self):
        acc = clsActor()
        pnombre = 'latigresa'
        pIdProducto = 1
        pdescripcion = 'Actor 1'
        acc.insertar(pnombre,pdescripcion,pIdProducto)
        
        pnombre2= 'chiabz'
        pIdProducto2 = None
        pdescripcion2 = 345
        test = acc.modificar(pIdProducto2,pnombre2,pdescripcion2)
        self.assertFalse(existeActor(nombre=pnombre2))

    def testModifIdCharyDecripNum(self):
        acc = clsActor()
        pnombre = 'manuela'
        pIdProducto = 1
        pdescripcion = 'Actor 1'
        acc.insertar(pnombre,pdescripcion,pIdProducto)
        
        pnombre2= 5454
        pIdProducto2 = 'idpepe'
        pdescripcion2 = 4567
        test = acc.modificar(pIdProducto2,pnombre2,pdescripcion2)
        self.assertFalse(existeActor(nombre=pnombre2))
    
    def testModifIdCharyDescripNul(self):
        acc = clsActor()
        pnombre = 'unnombre'
        pIdProducto = 1
        pdescripcion = 'Actor1'
        acc.insertar(pnombre,pdescripcion,pIdProducto)
        
        pnombre2= 'yyyyyy'
        pIdProducto2 = 'idpepe'
        pdescripcion2 = ''
        test = acc.modificar(pIdProducto2,pnombre2,pdescripcion2)
        self.assertFalse(existeActor(nombre=pnombre2))


#Casos Malicia

    def testModifCharEnId(self):
        acc = clsActor()
        pIdProducto2 = 'hola'
        pdescripcion2 = 'Actor p'
        pnombre2= 'estem'
        test = acc.modificar(pIdProducto2,pnombre2,pdescripcion2)
        self.assertFalse(existeActor(nombre=pnombre2))

    def testModifDescrip501(self):
        acc = clsActor()
        pIdProducto2 = 2
        pnombre2= 'este'
        pdescripcion2 = 'El Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of WA'
        test = acc.modificar(pIdProducto2,pnombre2,pdescripcion2)
        self.assertFalse(existeActor(nombre=pnombre2))

    def testModifDescripVacio(self):
        acc = clsActor()
        pIdProducto2 = 1
        pnombre2= 'nombredos'
        pdescripcion2 = ''
        test = acc.modificar(pIdProducto2,pnombre2,pdescripcion2)
        self.assertFalse(existeActor(nombre=pnombre2))

    def testModifDescripNum(self):
        acc = clsActor()
        pIdProducto2 = 3
        pnombre2= 'nombretres'
        pdescripcion2 = 123
        test = acc.modificar(pIdProducto2,pnombre2,pdescripcion2)
        self.assertFalse(existeActor(nombre=pnombre2))
    
    def testModifIdNulo(self):
        acc = clsActor()
        pIdProducto2 = None
        pnombre2= 'nombrecuatro'
        pdescripcion2 = 'Actor nulo'
        test = acc.modificar(pIdProducto2,pnombre2,pdescripcion2)
        self.assertFalse(existeActor(nombre=pnombre2))




if __name__ == "__main__":
    unittest.main()

