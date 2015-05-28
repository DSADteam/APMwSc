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
        
        self.act=clsActor(engine,sessionDB)
        prod=clsProducto(engine,sessionDB)
        prod.insertar("nombreprod","unadescripcion")
        self.prodId = prod.idProd("nombreprod")

#casos frontera

    def testInsertar500(self):
        pnombre = "pedro" * 10
        pdescripcion = "holfittt"
        self.act.insertar(pnombre,pdescripcion,self.prodId)
        self.assertTrue(self.act.existeActor(nombre=pnombre,descripcion=pdescripcion))
    
    def testDescripcion501(self):
        pnombre = 'justAno123' * 500
        pnombre += 's'
        pIdProducto = 4
        pdescripcion = 'Haciendo una prueba donde el espacio de lineas es tan largo que debe dar 500 palabras en la descripcion del modulo accion y ya me canse de escribir tanto asi que a partir de ahora pondre puro HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR y el fin'
        self.act.insertar(pnombre,pdescripcion,self.prodId)
        self.assertFalse(self.act.existeActor(pnombre))

    def testWrongProdId(self):
        pnombre = 'justAnotherTest'
        pdescripcion = 'descripcionNormal'
        self.act.insertar(pnombre,pdescripcion,-1)
        self.assertFalse(self.act.existeActor(pnombre))
    

    #Casos Esquina

    def testTodosVacios(self):
        pnombre = ''
        pIdProducto = None
        pdescripcion = ''
        a = self.act.insertar(pnombre,pdescripcion,self.prodId)
        self.assertFalse(self.act.existeActor(pnombre))
    
    def testIdNuloyDescripNum(self):
      
        pnombre = 'jeanCarlos'
        pIdProducto = None
        pdescripcion = 6589
        self.act.insertar(pnombre,pdescripcion,self.prodId)
        self.assertFalse(self.act.existeActor(pnombre))
    
    def testCharEnIdyDecripNum(self):
  
        pnombre = ''
        pIdProducto = 'bruxw'
        pdescripcion = 345346
        self.act.insertar(pnombre,pdescripcion,self.prodId)
        self.assertFalse(self.act.existeActor(nombre=pnombre))


    def testDescripcion501(self):
   
        pnombre = 'perro'
        pIdProducto = 3
        pdescripcion = 'El Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of WA'
        self.act.insertar(pnombre,pdescripcion,self.prodId)
        self.assertFalse(self.act.existeActor(pnombre))
        
    def testNumEnDescrip(self):
       
        pnombre = 'chiabe'
        pIdProducto = 4
        pdescripcion = 234
        self.act.insertar(pnombre,pdescripcion,self.prodId)
        self.assertFalse(self.act.existeActor(pnombre))

#TEST MODIFICAR
#casos regulares

    def testModificar1(self):
     
        pnombre = 'nabil'
        pdescripcion = 'Actor1'
        self.act.insertar(pnombre,pdescripcion,self.prodId)
        
        pnombre2= 'coki'
        pdescripcion2 = 'Actor N1'
        test = self.act.modificar(self.prodId,pnombre2, pdescripcion2)
        self.assertTrue(self.act.existeActor(pnombre2))

#Casos fronteras
    
    def testDescrip500(self):
       
        pnombre = 'cristina'
        pdescripcion = 'W'
        self.act.insertar(pnombre,pdescripcion,self.prodId)

        pnombre2= 'oil'
        pdescripcion2 = 'holaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholahoholaholaho'
        test = self.act.modificar(self.prodId,pnombre2, pdescripcion2)
        self.assertTrue(self.act.existeActor(pnombre2))

    
    def testDescripAlMin(self):

        pnombre = 'roberto'
        pIdProducto = 1
        pdescripcion = 'Actor 1'
        self.act.insertar(pnombre,pdescripcion,self.prodId)
        
        pnombre2= 'nuevo'
        pIdProducto2 = 1
        pdescripcion2 = 'A'
        test = self.act.modificar(self.prodId,pnombre2,pdescripcion2)
        self.assertTrue(self.act.existeActor(nombre=pnombre2))

#Casos Esquina

    def testModifTodoNul(self):
    
        pnombre = 'meggie'
        pIdProducto = 1
        pdescripcion = 'Actor 1'
        self.act.insertar(pnombre,pdescripcion,self.prodId)
        
        
        pnombre2= ''
        pdescripcion2 = ''
        test = self.act.modificar(self.prodId,pnombre2,pdescripcion2)
        self.assertFalse(self.act.existeActor(nombre=pnombre2))

    def testModifIdNulyDescripNum(self):
      
        pnombre = 'latigresa'
        pIdProducto = 1
        pdescripcion = 'Actor 1'
        self.act.insertar(pnombre,pdescripcion,self.prodId)
        
        pnombre2= 'chiabz'
        pIdProducto2 = None
        
        test = self.act.modificar(pIdProducto2,pnombre2,pdescripcion)
        self.assertFalse(self.act.existeActor(nombre=pnombre2))

    def testModifIdCharyDecripNum(self):
        
        pIdProducto = 'hola'
        pnombre2= 'estenombre'
        
        pdescripcion2 = 4567
        test = self.act.modificar(pIdProducto,pnombre2,pdescripcion2)
        self.assertFalse(self.act.existeActor(nombre=pnombre2))
    
    def testModifIdCharyDescripNul(self):
      
        pnombre = 'unnombre'
        pIdProducto = 1
        pdescripcion = 'Actor1'
        self.act.insertar(pnombre,pdescripcion,self.prodId)
        
        pnombre2= 'yyyyyy'
      
        pdescripcion2 = ''
        test = self.act.modificar(self.prodId,pnombre2,pdescripcion2)
        self.assertFalse(self.act.existeActor(nombre=pnombre2))


#Casos Malicia

    def testModifCharEnId(self):
    
        pIdProducto2 = 'hola'
        pdescripcion2 = 'Actor p'
        pnombre2= 'estem'
        test = self.act.modificar(pIdProducto2,pnombre2,pdescripcion2)
        self.assertFalse(self.act.existeActor(nombre=pnombre2))


    def testModifDescripVacio(self):
    
        pIdProducto2 = 1
        pnombre2= 'nombredos'
        pdescripcion2 = ''
        test = self.act.modificar(self.prodId,pnombre2,pdescripcion2)
        self.assertFalse(self.act.existeActor(nombre=pnombre2))

    def testModifDescripNum(self):
 
        pIdProducto2 = 1
        pnombre2= 'nabil'
        pdescripcion2 = 123
        test = self.act.modificar(self.prodId,pnombre2,pdescripcion2)
        self.assertFalse(self.act.existeActor(descripcion=pdescripcion2))
    
    def testModifIdNulo(self):
 
        pIdProducto2 = None
        pnombre2= 'nombrecuatro'
        pdescripcion2 = 'Actor nulo'
        test = self.act.modificar(pIdProducto2,pnombre2,pdescripcion2)
        self.assertFalse(self.act.existeActor(nombre=pnombre2))



if __name__ == "__main__":
    unittest.main()

