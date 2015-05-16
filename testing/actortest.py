import unittest
import os
import sys
dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../..'))
sys.path.append(dir)
from app.scrum.actor import clsActor
from base import *


class actorTester(unittest.TestCase):
     
#TEST INSERTAR
#Casos regulares

    def testinsertar1(self):
        act = clsActor()
        pIdActor = 1
        pnombre = 'pepe'
        pdescripcion = 'Actor 1'
        test = acc.insertar(pIdActor,pnombre,pdescripcion)
        self.assertTrue(test)

    def testinsertar2(self):
        act = clsActor()
        pIdActor = 2
        pnombre = 'juan'
        pdescripcion = 'Actor 2'
        test = acc.insertar(pIdActor,pnombre,pdescripcion)
        self.assertTrue(test)

#Casos fronteras

    def testnombre50(self):
        act = clsActor()
        pIdActor = 1
        pnombre = 'AuS2CaV9lq8GbkJi174Af6hYDJ49ywbcx0Mf3rziTS9cJVfOja'
        pdescripcion = 'Actor 1'
        test = acc.insertar(pIdActor,pnombre,pdescripcion)
        self.assertTrue(test)

    def testdescripcion500(self):
        act = clsActor()
        pIdActor = 4
        pnombre = 'brace yourself'
        pdescripcion = 'Haciendo una prueba donde el espacio de lineas es tan largo que debe dar 500 palabras en la descripcion del modulo actor y ya me canse de escribir tanto asi que a partir de ahora pondre puro HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR y el fin!'
        test = acc.insertar(pIdActor,pnombre,pdescripcion)
        self.assertTrue(test)

    def testCampoIdNulo(self):
        act = clsActor()
        pIdActor = None
        pnombre = 'juancho'
        pdescripcion = 'Actor 2'
        test = acc.insertar(pIdActor,pnombre,pdescripcion)
        self.assertFalse(test)

    def testNombreNulo(self):
        act = clsActor()
        pIdActor = 4
        pnombre = ''
        pdescripcion = 'Actor 2'
        test = acc.insertar(pIdActor,pnombre,pdescripcion)
        self.assertFalse(test)

    def testDescripNulo(self):
        act = clsActor()
        pIdActor = 1
        pnombre = 'carlos'
        pdescripcion = ''
        test = acc.insertar(pIdActor,pnombre,pdescripcion)
        self.assertFalse(test)

    def testNombreNum(self):
        act = clsActor()
        pIdActor = 4
        pnombre = 232
        pdescripcion = 'Actor 4'
        test = acc.insertar(pIdActor,pnombre,pdescripcion)
        self.assertFalse(test)

    def testDescripNum(self):
        act = clsActor()
        pIdActor = 2
        pnombre = 'fred'
        pdescripcion = 44444
        test = acc.insertar(pIdActor,pnombre,pdescripcion)
        self.assertFalse(test)

#Caso Esquina

    def testtodosVacios(self):
        act = clsActor()
        pIdActor = None
        pnombre = ''
        pdescripcion = ''
        test = acc.insertar(pIdActor,pnombre,pdescripcion)
        self.assertFalse(test)

    def testNombreyDescripNum(self)
        act = clsActor()
        pIdActor = 3
        pnombre = 3333
        pdescripcion = 44444
        test = acc.insertar(pIdActor,pnombre,pdescripcion)
        self.assertFalse(test)

    def testidVacioyDescrip500(self):
        act = clsActor()
        pIdActor = None
        pnombre = 'too long'
        pdescripcion = 'El Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of W'
        test = acc.insertar(pIdActor,pnombre,pdescripcion)
        self.assertFalse(test)
        
#Casos Malicia

    def testCharEnId(self):
        act = clsActor()
        pIdActor = 'idviteh'
        pnombre = 'el viejo'
        pdescripcion = 'Actor 5'
        test = acc.insertar(pIdActor,pnombre,pdescripcion)
        self.assertFalse(test)

    def testNombre51(self):
        act = clsActor()
        pIdActor = 2
        pnombre = 'AuS2CaV9lq8GbkJi174Af6hYDJ49ywbcx0Mf3rziTS9cJVfOjab'
        pdescripcion = 'Actor 2'
        test = acc.insertar(pIdActor,pnombre,pdescripcion)
        self.assertFalse(test)

    def testDescrip501(self):
        act = clsActor()
        pIdActor = 1
        pnombre = 'Alberto'
        pdescripcion = 'El Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of WA'
        test = acc.insertar(pIdActor,pnombre,pdescripcion)
        self.assertFalse(test)

#TEST MODIFICAR
#caso regular

    def testModificar1(self):
        act = clsActor()
        pIdActor = 1
        pnombre = 'pepe'
        pdescripcion = 'Actor 1'
        act.insertar(pIdActor,pnombre,pdescripcion)

        pIdActor2 = 1
        pnombre2 = 'pablo'
        pdescripcion2 = 'Actor N1'
        test = act.modificar(pIdActor2,pnombre2,pdescripcion2)
        self.assertTrue(test)

#Casos fronteras

    def testModifnombre50(self):        
        act = clsActor()
        pIdActor = 1
        pnombre = 'pepe'
        pdescripcion = 'Actor 1'
        act.insertar(pIdActor,pnombre,pdescripcion)

        pIdActor2 = 1
        pnombre2 = 'AuS2CaV9lq8GbkJi174Af6hYDJ49ywbcx0Mf3rziTS9cJVfOja'
        pdescripcion2 = 'Actor N1'
        test = act.modificar(pIdActor,pnombre2,pdescripcion2)
        self.assertTrue(test)


    def testModifDescrip500(self):        
        act = clsActor()
        pIdActor = 3
        pnombre = 'harold'
        pdescripcion = 'Actor 3'
        act.insertar(pIdActor,pnombre,pdescripcion)

        pIdActor2 = 3
        pnombre2 = 'harold'
        pdescripcion2 = 'Haciendo una prueba donde el espacio de lineas es tan largo que debe dar 500 palabras en la descripcion del modulo actor y ya me canse de escribir tanto asi que a partir de ahora pondre puro HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR y el fin!'
        test = act.modificar(pIdActor2,pnombre2,pdescripcion2)
        self.assertTrue(test)

    def testModifNoValid(self):
        act = clsActor()
        test = act.modificar(123,'carlos','Accion 123')
        self.assertFalse(test)

    def testNombreMin(self):
        act = clsActor()
        pIdActor = 1
        pnombre = 'pepe'
        pdescripcion = 'Actor 1'
        act.insertar(pIdActor,pnombre,pdescripcion)

        pIdActor2 = 1
        pnombre2 = 'p'
        pdescripcion2 = 'Actor N1'
        test = act.modificar(pIdActor2,pnombre2,pdescripcion2)
        self.assertTrue(test)

    def testDescripMin(self):
        act = clsActor()
        pIdActor = 1
        pnombre = 'pepe'
        pdescripcion = 'Actor 1'
        act.insertar(pIdActor,pnombre,pdescripcion)

        pIdActor2 = 1
        pnombre2 = 'pepe'
        pdescripcion2 = 'A'
        test = act.modificar(pIdActor2,pnombre2,pdescripcion2)
        self.assertTrue(test)

#Casos Esquinas

    def testModifTodosNull(self):
        act = clsActor()
        pIdActor = 1
        pnombre = 'pepe'
        pdescripcion = 'Actor 1'
        act.insertar(pIdActor,pnombre,pdescripcion)

        pIdActor2 = None
        pnombre2 = ''
        pdescripcion2 = ''
        test = act.modificar(pIdActor2,pnombre2,pdescripcion2)
        self.assertFalse(test)
    
    def testModifIdNulyDescripNum(self):
        act = clsActor()
        pIdActor = 1
        pnombre = 'pepe'
        pdescripcion = 'Actor 1'
        act.insertar(pIdActor,pnombre,pdescripcion)

        pIdActor2 = None
        pnombre2 = 'laura'
        pdescripcion2 = 985
        test = act.modificar(pIdActor2,pnombre2,pdescripcion2)
        self.assertFalse(test)
    
    def testModifIdNulyNombreNum(self):
        act = clsActor()
        pIdActor = 1
        pnombre = 'pepe'
        pdescripcion = 'Acctor 3'
        act.insertar(pIdActor,pnombre,pdescripcion)

        pIdActor2 = None
        pnombre2 = 69
        pdescripcion2 = 'Actor 3'
        test = act.modificar(pIdActor2,pnombre2,pdescripcion2)
        self.assertFalse(test)

    def testModifNombreyDescripNum(self):
        act = clsActor()
        pIdActor = 1
        pnombre = 'pepe'
        pdescripcion = 'Actor 1'
        act.insertar(pIdActor,pnombre,pdescripcion)

        pIdActor2 = 1
        pnombre2 = 69
        pdescripcion2 = 985
        test = act.modificar(pIdActor2,pnombre2,pdescripcion2)
        self.assertFalse(test)
    
    def testModifIdCharyDescripNum(self):
        act = clsActor()
        pIdActor = 1
        pnombre = 'pepe'
        pdescripcion = 'Actor 1'
        act.insertar(pIdActor,pnombre,pdescripcion)

        pIdActor2 = 'idx'
        pnombre2 = 'laura'
        pdescripcion2 = 985
        test = act.modificar(pIdActor2,pnombre2,pdescripcion2)
        self.assertFalse(test)
    
    def testModifIdCharyNombreNum(self):
        act = clsActor()
        pIdActor = 2
        pnombre = 'pepe'
        pdescripcion = 'Actor 2'
        act.insertar(pIdActor,pnombre,pdescripcion)

        pIdActor2 = 'idx'
        pnombre2 = 42
        pdescripcion2 = 'Actor 2'
        test = act.modificar(pIdActor2,pnombre2,pdescripcion2)
        self.assertFalse(test)

#Casos Malicia

    def testModifCharEnId(self):
        act = clsActor()
        pIdActor = 2
        pnombre = 'pepe'
        pdescripcion = 'Actor 2'
        act.insertar(pIdActor,pnombre,pdescripcion)

        pIdActor2 = 'idx'
        pnombre2 = 'pepe'
        pdescripcion2 = 'Actor 2'
        test = act.modificar(pIdActor2,pnombre2,pdescripcion2)
        self.assertFalse(test)

    def testModifDescrip501(self):        
        act = clsActor()
        pIdActor = 1
        pnombre = 'harold'
        pdescripcion = 'Actor 1'
        act.insertar(pIdActor,pnombre,pdescripcion)

        pIdActor2 = 1
        pnombre2 = 'hordor'
        pdescripcion2 = 'Haciendo una prueba donde el espacio de lineas es tan largo que debe dar 500 palabras en la descripcion del modulo actor y ya me canse de escribir tanto asi que a partir de ahora pondre puro HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR y el ¡fin!'
        test = act.modificar(pIdActor2,pnombre2,pdescripcion2)
        self.assertFalse(test)

    def testModifnombre51(self):        
        act = clsActor()
        pIdActor = 1
        pnombre = 'pepe'
        pdescripcion = 'Actor 1'
        act.insertar(pIdActor,pnombre,pdescripcion)

        pIdActor2 = 1
        pnombre2 = 'AuS2CaV9lq8GbkJi174Af6hYDJ49ywbcx0Mf3rziTS9cJVfOjab'
        pdescripcion2 = 'Actor N1'
        test = act.modificar(pIdActor2,pnombre2,pdescripcion2)
        self.assertFalse(test)

    def testModifDescripVacio(self):
        act = clsActor()
        pIdActor2 = 1
        pnombre = 'julio'
        pdescripcion2 = ''
        test = act.modificar(pIdActor2,pdescripcion2)
        self.assertFalse(test)

    def testModifNombreVacio(self):
        act = clsActor()
        pIdActor2 = 1
        pnombre = ''
        pdescripcion2 = 'Actor 1'
        test = act.modificar(pIdActor2,pdescripcion2)
        self.assertFalse(test)

    def testModifNombreNum(self):
        act = clsActor()
        pIdActor2 = 1
        pnombre = 986
        pdescripcion2 = 'Actor 1'
        test = act.modificar(pIdActor2,pdescripcion2)
        self.assertFalse(test)

    def testModifDescripNum(self):
        act = clsActor()
        pIdActor2 = 1
        pnombre = 'fabio'
        pdescripcion2 = 865
        test = act.modificar(pIdActor2,pdescripcion2)
        self.assertFalse(test)

    def testModifIdNulo(self):
        act = clsActor()
        pIdActor2 = None
        pnombre = 'rod'
        pdescripcion2 = 'Actor 3'
        test = act.modificar(pIdActor2,pdescripcion2)
        self.assertFalse(test)


unittest.main()
        