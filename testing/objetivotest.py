# -*- coding: utf-8 -*-

'''
Created on 15/05/2015
 
@author: Meggie Sanchez y Cristina Betancourt
'''

import sys
import os

dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../..'))
sys.path.append(dir)

from app.scrum.prod import clsProducto
from app.scrum.objetivo import clsObjetivo
from base import *
import unittest

class objetivoTester(unittest.TestCase):
    
    # Inicializacion de casos de prueba
    def setUp(self):
        self.objetivo=clsObjetivo(engine,sessionDB)
        prod=clsProducto(engine,sessionDB)
        prod.insertar("nombreprod","unadescripcion","cualitativo")
        self.prodId = prod.idProd("nombreprod")


    # Insertar de objetivo 
    
    # Casos interiores
    
    # Insertar un objetivo que no existe
    def testInsertar1(self):
        transv= 'transversal'
        pDescripcion = 'Terminar sitarea'
        self.objetivo.insertar(self.prodId, pDescripcion, transv)
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion)) 

     # Insertar un objetivo que existe
    def testInsertar2(self):
        transv= 'transversal'
        pDescripcion = 'Terminar oktarea'
        self.objetivo.insertar(self.prodId, pDescripcion, transv)
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion)) 
    # Insertar un transversal invalido    
    def testInsertar222(self):
        transv= 'chimichurri transversal'
        pDescripcion = 'Terminar kkkkkktarea'
        self.objetivo.insertar(self.prodId, pDescripcion, transv)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion)) 
        
    def testInsertar2222(self):
        transv= 9001728888
        pDescripcion = 'Terminar l5tarea'
        self.objetivo.insertar(self.prodId, pDescripcion, transv)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion))    
    # Casos fronteras
 
    # Insertar un objetivo con el minimo numero de caracteres en descripcion
    def testInsertar3(self):
        transv= 'transversal'
        pDescripcion = 'T'
        self.objetivo.insertar(self.prodId, pDescripcion, transv )
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion)) 

    # Insertar un objetivo con el maximo numero de caracteres en descripcion
    def testInsertar4(self):
        transv= 'transversal'
        pDescripcion = 'd'*500
        self.objetivo.insertar(self.prodId, pDescripcion, transv)
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion)) 
     # Insertar un transversal invalido con descripcion frontera   
    def testInsertar44(self):
        transv= 'este no es transversal'
        pDescripcion = 'l'*500
        self.objetivo.insertar(self.prodId, pDescripcion, transv)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion)) 
    def testInsertar444(self):
        transv= 444
        pDescripcion = 'f'*500
        self.objetivo.insertar(self.prodId, pDescripcion, transv)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion))
    def testInsertar4444(self):
        transv= None
        pDescripcion = 'x'*500
        self.objetivo.insertar(self.prodId, pDescripcion, transv)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion))
        
    # Insertar un objetivp con el minimo numero en idObjetivo
    def testInsertar5(self):
        transv= 'transversal'
        pDescripcion = 'e'*500
        self.objetivo.insertar(self.prodId, pDescripcion, transv)
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion)) 
     
    # Casos esquinas
    
    # Insertar un objetivo con el minimo numero en idObjetivo y el minimo de caracteres en descripcion
    def testInsertar7(self):
        transv= 'transversal'
        pDescripcion = 'r'
        self.objetivo.insertar(self.prodId, pDescripcion, transv)
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion)) 
        
    # Casos maliciosos
    
    # Insertar un objetivo con cadena vacia en descripcion
    def testInsertar11(self):
        transv= 'transversal'
        pDescripcion = ''
        self.objetivo.insertar(self.prodId, pDescripcion, transv)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion))

    # Insertar un objetivo que excede los 500 caracteres en descripcion
    def testInsertar12(self):
        transv= 'no transversal'
        pDescripcion = 'l'*501
        self.objetivo.insertar(self.prodId, pDescripcion, transv)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion))
        
    # Insertar un objetivo con enteros en descripcion
    def testInsertar13(self):
        transv= 'no transversal'
        pDescripcion = 3245345
        self.objetivo.insertar(self.prodId, pDescripcion, transv)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion))
       
    # Insertar un objetivo con string en idObjetivo
    def testInsertar14(self):
        transv= 'JC transversal'
        pIdObjetivo = 'fghfgh'
        pDescripcion = 32
        self.objetivo.insertar(pIdObjetivo, pDescripcion, transv)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion))
       
    # Insertar un objetivo con nada como idrole
    def testInsertar15(self):
        transv= 'transversal'
        pIdObjetivo = None
        pDescripcion = 'dfghjj'
        self.objetivo.insertar(pIdObjetivo, pDescripcion, transv)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion))
        
    # Modificar de objetivo
        
    # Casos interiores
    
    

    # Modificar un objetivo que ya existe
    
    def testModificar1(self):
        transv= 'transversal'
        pDescripcion2 = 'holaaa22'
        self.objetivo.modificar(self.prodId, pDescripcion2, transv)
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion2))         
   
    # Modificar un objetivo que no existe
    def testModificar2(self):
        transv= 'transversal'
        pDescripcion='holapa'
        self.objetivo.modificar(45356456, pDescripcion, transv)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion))  
    
    # Casos Fronteras
      
    # Modificar un objetivo que tiene el maximo de caracteres en descripcion
    def testModificar5(self):
        transv= 'transversal'
        pDescripcion2 = 'v'*500
        self.objetivo.modificar(self.prodId, pDescripcion2, transv)
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion2)) 
     # Modificar un objetivo que tiene el maximo de caracteres en descripcion y trans inv
    def testModificar555(self):
        transv= 'scrum es lo mejor'
        pDescripcion2 = '.'*500
        self.objetivo.modificar(self.prodId, pDescripcion2, transv)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion2))
    
    def testModificar5555(self):
        transv= 2021
        pDescripcion2 = ','*500
        self.objetivo.modificar(self.prodId, pDescripcion2, transv)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion2))
   
    # Modificar un objetivo que tiene el minimo de caracteres en descripcion
    def testModificar6(self):
        transv= 'transversal'
        pDescripcion2 = 'v'
        self.objetivo.modificar(self.prodId, pDescripcion2, transv)
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion2)) 
    
    # Casos Esquinas
     

    #Modificar un objetivo que no existe y tiene el maximo de caracteres en la descripcion
    def testModificar10(self):
        transv= 'transversal'        
        pDescripcion2 = 'g'*500
        self.objetivo.modificar(4954789744, pDescripcion2, transv)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion2)) 

    # Casos maliciosos

    # Modificar un objetivo que tiene como idObjetivo un string
    def testModificar11(self):     
        transv= 'transversal'
        pIdObjetivo2 = '234'
        pDescripcion2 = 'g'*500
        self.objetivo.modificar(pIdObjetivo2, pDescripcion2, transv)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion2))      
    
    # Modificar un objetivo que tiene como descripcion una cadena vacia
    def testModificar13(self):  
        transv= 'transversal'
        pDescripcion2 = ''
        self.objetivo.modificar(self.prodId, pDescripcion2, transv)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion2))    
          
    # Modificar un objetivo que excede los 500 caracteres en descripcion
    def testModificar14(self):      
        transv= 'transversal'
        pDescripcion2 = 'o'*501
        self.objetivo.modificar(self.prodId, pDescripcion2, transv)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion2))     

   # Modificar un objetivo que tiene enteros en descripcion
    def testModificar15(self):        
        transv= 'transversal'
        pDescripcion2 = 501
        self.objetivo.modificar(self.prodId, pDescripcion2, transv)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion2))

    # TEST ELIMINAR

    # Eliminar objetivo inexistente
    def testElimInexistente(self):
        pIdObjetivo = 190223
        pdescripcion = ''
        self.objetivo.eliminar(pIdObjetivo)
        self.assertFalse(self.objetivo.existeObjetivo(descripcion=pdescripcion))

    # Eliminar objetivo que sea None
    def testElimVacio(self):
        pIdObjetivo = None
        pdescripcion = ''
        self.objetivo.eliminar(pIdObjetivo)
        self.assertFalse(self.objetivo.existeObjetivo(descripcion=pdescripcion))

    # Eliminar objetivo existente
    def testElimExistente(self):
        pIdObjetivo = 1
        pdescripcion = 'Objetivo 1'
        ptrans = 'transversal'
        self.objetivo.insertar(self.prodId, pdescripcion, ptrans)
        self.objetivo.eliminar(pIdObjetivo)
        self.assertTrue(self.objetivo.existeObjetivo(descripcion=pdescripcion))
    
if __name__ == "__main__": 
    unittest.main()   