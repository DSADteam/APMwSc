import sys
import os
dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../..'))
sys.path.append(dir)

from app.scrum.prod  import clsProducto
from app.scrum.actor import clsActor
from base import *
import unittest 

class actorTester(unittest.TestCase):
    def setUp(self):
        self.acc=clsActor(engine,sessionDB)
        
    def tearDown(self):
        #self.acc.borrarFilas()


     def testinsertar1(self):
      
        pnombre = 'pedrito'
        pIdProducto = 2
        pdescripcion = 'Aggg'
        self.acc.insertar(pnombre,pdescripcion,pIdProducto)
        self.assertTrue(self.acc.existeActor(pnombre))
    
#casos frontera

    def testCampoIdNulo(self):
        
        pnombre = 'jose'
        pIdProducto = None
        pdescripcion = 'Actor 3'
        self.acc.insertar(pnombre,pdescripcion,pIdProducto)
        self.assertFalse(self.acc.existeActor(pnombre))

    def testDescripcionNulo(self):
        
        pnombre = 'josue'
        pIdProducto = 1
        pdescripcion = ''
        self.acc.insertar(pnombre,pdescripcion,pIdProducto)
        self.assertFalse(self.acc.existeActor(pnombre))

    def testdescripcion500(self):
   
        pnombre = 'eli'
        pIdProducto = 4
        pdescripcion = 'Haciendo una prueba donde el espacio de lineas es tan largo que debe dar 500 palabras en la descripcion del modulo accion y ya me canse de escribir tanto asi que a partir de ahora pondre puro HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR y el fin'
        self.acc.insertar(pnombre,pdescripcion,pIdProducto)
        self.assertFalse(self.acc.existeActor(pnombre))

    def testNumEnDescrip(self):
       
        pnombre = 'chiabe'
        pIdProducto = 4
        pdescripcion = 234
        self.acc.insertar(pnombre,pdescripcion,pIdProducto)
        self.assertFalse(self.acc.existeActor(pnombre))

#Caso Esquina

    def todosVacios(self):
       
        pnombre = 'chiabes'
        pIdProducto = None
        pdescripcion = ''
        self.acc.insertar(pnombre,pdescripcion,pIdProducto)
        self.assertFalse(self.acc.existeActor(pnombre))

    def idVacioyDescrip500(self):
    
        pnombre = 'teama'
        pIdProducto = None
        pdescripcion = 'O'*500
        self.acc.insertar(pnombre,pdescripcion,pIdProducto)
        self.assertTrue(self.acc.existeActor(pnombre))

    def testIdNuloyDescripNum(self):
      
        pnombre = 'teruel'
        pIdProducto = None
        pdescripcion = 6589
        self.acc.insertar(pnombre,pdescripcion,pIdProducto)
        self.assertFalse(self.acc.existeActor(pnombre))

    def testCharEnIdyDecripNum(self):
  
        pnombre = ''
        pIdProducto = 'bruxw'
        pdescripcion = 345346
        self.acc.insertar(pnombre,pdescripcion,pIdProducto)
        self.assertFalse(self.acc.existeActor(nombre=pnombre))

#Caso malicia

    def testcharEnId(self):
 
        pnombre = 'jirafa'
        pIdProducto = 'idpepe'
        pdescripcion = 'Actor 2'
        self.acc.insertar(pnombre,pdescripcion,pIdProducto)
        self.assertFalse(self.acc.existeActor(pnombre))
    
    def testdescripcion501(self):
   
        pnombre = 'perro'
        pIdProducto = 3
        pdescripcion = 'El Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of WA'
        self.acc.insertar(pnombre,pdescripcion,pIdProducto)
        self.assertFalse(self.acc.existeActor(pnombre))

#TEST MODIFICAR
#casos regulares

    def testModificar1(self):
     
        pnombre = 'nabil'
        pIdProducto = 1
        pdescripcion = 'Actor1'
        self.acc.insertar(pnombre,pdescripcion,pIdProducto)
        
        pnombre2= 'coki'
        pIdProducto2 = 1
        pdescripcion2 = 'Actor N1'
        test = self.acc.modificar(pIdProducto,pnombre2, pdescripcion2)
        self.assertTrue(self.acc.existeActor(pnombre2))

#Casos fronteras
    
    def testDescrip500(self):
       
        pnombre = 'cristina'
        pIdProducto = 2
        pdescripcion = 'W'
        self.acc.insertar(pnombre,pdescripcion,pIdProducto)

        pnombre2= 'oil'
        pdescripcion2 = 'holaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholaho'
        test = self.acc.modificar(pIdProducto,pnombre2, pdescripcion2)
        self.assertFalse(self.acc.existeActor(pnombre2))

    def testModifNoValid(self):
       
        pIdProducto = 123
        pdescripcion = 'Actor 123'
        pnombre2= 'tini'
        test = self.acc.modificar(pIdProducto,pnombre2,pdescripcion)
        self.assertFalse(self.acc.existeActor(pnombre2))

    def testDescripAlMin(self):

        pnombre = 'roberto'
        pIdProducto = 1
        pdescripcion = 'Actor 1'
        self.acc.insertar(pnombre,pdescripcion,pIdProducto)
        
        pnombre2= 'nuevo'
        pIdProducto2 = 1
        pdescripcion2 = 'A'
        test = self.acc.modificar(pIdProducto2,pnombre2,pdescripcion2)
        self.assertTrue(self.acc.existeActor(nombre=pnombre2))

#Casos Esquina

    def testModifTodoNul(self):
    
        pnombre = 'meggie'
        pIdProducto = 1
        pdescripcion = 'Actor 1'
        self.acc.insertar(pnombre,pdescripcion,pIdProducto)
        
        
        pnombre2= ''
        pdescripcion2 = ''
        test = self.acc.modificar(pIdProducto,pnombre2,pdescripcion2)
        self.assertFalse(self.acc.existeActor(nombre=pnombre2))

    def testModifIdNulyDescripNum(self):
      
        pnombre = 'latigresa'
        pIdProducto = 1
        pdescripcion = 'Actor 1'
        self.acc.insertar(pnombre,pdescripcion,pIdProducto)
        
        pnombre2= 'chiabz'
        pIdProducto2 = None
        
        test = self.acc.modificar(pIdProducto,pnombre2,pdescripcion)
        self.assertFalse(self.acc.existeActor(nombre=pnombre2))

    def testModifIdCharyDecripNum(self):

        pnombre = 'manuela'
        pIdProducto = 1
        pdescripcion = 'Actor 1'
        self.acc.insertar(pnombre,pdescripcion,pIdProducto)
        
        pnombre2= 'estenombre'
      
        pdescripcion2 = 4567
        test = self.acc.modificar(pIdProducto,pnombre2,pdescripcion2)
        self.assertFalse(self.acc.existeActor(nombre=pnombre2))
    
    def testModifIdCharyDescripNul(self):
      
        pnombre = 'unnombre'
        pIdProducto = 1
        pdescripcion = 'Actor1'
        self.acc.insertar(pnombre,pdescripcion,pIdProducto)
        
        pnombre2= 'yyyyyy'
      
        pdescripcion2 = ''
        test = self.acc.modificar(pIdProducto,pnombre2,pdescripcion2)
        self.assertFalse(self.acc.existeActor(nombre=pnombre2))


#Casos Malicia

    def testModifCharEnId(self):
    
        pIdProducto2 = 'hola'
        pdescripcion2 = 'Actor p'
        pnombre2= 'estem'
        test = self.acc.modificar(pIdProducto2,pnombre2,pdescripcion2)
        self.assertFalse(self.acc.existeActor(nombre=pnombre2))

    def testModifDescrip501(self):
      
        pIdProducto2 = 2
        pnombre2= 'este'
        pdescripcion2 = 'El Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of WA'
        test = self.acc.modificar(pIdProducto2,pnombre2,pdescripcion2)
        self.assertFalse(self.acc.existeActor(nombre=pnombre2))

    def testModifDescripVacio(self):
    
        pIdProducto2 = 1
        pnombre2= 'nombredos'
        pdescripcion2 = ''
        test = self.acc.modificar(pIdProducto2,pnombre2,pdescripcion2)
        self.assertFalse(self.acc.existeActor(nombre=pnombre2))

    def testModifDescripNum(self):
 
        pIdProducto2 = 3
        pnombre2= 'nombretres'
        pdescripcion2 = 123
        test = self.acc.modificar(pIdProducto2,pnombre2,pdescripcion2)
        self.assertFalse(self.acc.existeActor(nombre=pnombre2))
    
    def testModifIdNulo(self):
 
        pIdProducto2 = None
        pnombre2= 'nombrecuatro'
        pdescripcion2 = 'Actor nulo'
        test = self.acc.modificar(pIdProducto2,pnombre2,pdescripcion2)
        self.assertFalse(self.acc.existeActor(nombre=pnombre2))




if __name__ == "__main__":
    unittest.main()

