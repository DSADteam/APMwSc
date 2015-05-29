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
        prod.insertar("nombreprod","unadescripcion")
        self.prodId = prod.idProd("nombreprod")


    # Insertar de objetivo 
    
    # Casos interiores
    
    # Insertar un objetivo que no existe
    def testInsertar1(self):
        
        pDescripcion = 'Terminar tarea'
        self.objetivo.insertar(self.prodId, pDescripcion)
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion)) 

     # Insertar un objetivo que existe
    def testInsertar2(self):
        
        pDescripcion = 'Terminar tarea'
        self.objetivo.insertar(self.prodId, pDescripcion)
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion)) 
         
    # Casos fronteras
 
    # Insertar un objetivo con el minimo numero de caracteres en descripcion
    def testInsertar3(self):
        
        pDescripcion = 'T'
        self.objetivo.insertar(self.prodId, pDescripcion)
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion)) 

    # Insertar un objetivo con el maximo numero de caracteres en descripcion
    def testInsertar4(self):
        
        pDescripcion = 'd'*500
        self.objetivo.insertar(self.prodId, pDescripcion)
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion)) 
        
    # Insertar un objetivp con el minimo numero en idObjetivo
    def testInsertar5(self):
        
        pIdObjetivo = 4
        pDescripcion = 'e'*500
        self.objetivo.insertar(pIdObjetivo, pDescripcion)
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion)) 
     
    # Casos esquinas
    
    # Insertar un objetivo con el minimo numero en idObjetivo y el minimo de caracteres en descripcion
    def testInsertar7(self):
        
        pIdObjetivo = 5
        pDescripcion = 'r'
        self.objetivo.insertar(pIdObjetivo, pDescripcion)
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion)) 
        
    # Casos maliciosos
    
    # Insertar un objetivo con cadena vacia en descripcion
    def testInsertar11(self):

        pDescripcion = ''
        self.objetivo.insertar(self.prodId, pDescripcion)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion))

    # Insertar un objetivo que excede los 500 caracteres en descripcion
    def testInsertar12(self):
        
        pDescripcion = 'l'*501
        self.objetivo.insertar(self.prodId, pDescripcion)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion))
        
    # Insertar un objetivo con enteros en descripcion
    def testInsertar13(self):
        
        pDescripcion = 3245345
        self.objetivo.insertar(self.prodId, pDescripcion)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion))
       
    # Insertar un objetivo con string en idObjetivo
    def testInsertar14(self):
        
        pIdObjetivo = 'fghfgh'
        pDescripcion = 32
        self.objetivo.insertar(pIdObjetivo, pDescripcion)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion))
       
    # Insertar un objetivo con nada como idrole
    def testInsertar15(self):
        
        pIdObjetivo = None
        pDescripcion = 'dfghjj'
        self.objetivo.insertar(pIdObjetivo, pDescripcion)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion))
        
    # Modificar de objetivo
        
    # Casos interiores
    
    

    # Modificar un objetivo que ya existe
    
    def testModificar1(self):

        pDescripcion2 = 'holaaa22'
        self.objetivo.modificar(self.prodId, pDescripcion2)
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion2))         
   
    # Modificar un objetivo que no existe
    def testModificar2(self):
        pDescripcion='holapa'
        self.objetivo.modificar(45356456, pDescripcion)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion))  
    
    # Casos Fronteras
      
    # Modificar un objetivo que tiene el maximo de caracteres en descripcion
    def testModificar5(self):
        
        pDescripcion2 = 'v'*500
        self.objetivo.modificar(self.prodId, pDescripcion2)
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion2)) 

   
    # Modificar un objetivo que tiene el minimo de caracteres en descripcion
    def testModificar6(self):
        
        pDescripcion2 = 'v'
        self.objetivo.modificar(self.prodId, pDescripcion2)
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion2)) 
    
    # Casos Esquinas
     

    #Modificar un objetivo que no existe y tiene el maximo de caracteres en la descripcion
    def testModificar10(self):
                
        pDescripcion2 = 'g'*500
        self.objetivo.modificar(4954789744, pDescripcion2)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion2)) 

    # Casos maliciosos

    # Modificar un objetivo que tiene como idObjetivo un string
    def testModificar11(self):     
        
        pIdObjetivo2 = '234'
        pDescripcion2 = 'g'*500
        self.objetivo.modificar(pIdObjetivo2, pDescripcion2)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion2))      
    
    # Modificar un objetivo que tiene como descripcion una cadena vacia
    def testModificar13(self):  
        
        pDescripcion2 = ''
        self.objetivo.modificar(self.prodId, pDescripcion2)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion2))    
          
    # Modificar un objetivo que excede los 500 caracteres en descripcion
    def testModificar14(self):      
        
        pDescripcion2 = 'o'*501
        self.objetivo.modificar(self.prodId, pDescripcion2)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion2))     

   # Modificar un objetivo que tiene enteros en descripcion
    def testModificar15(self):        
        
        pDescripcion2 = 501
        self.objetivo.modificar(self.prodId, pDescripcion2)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion2))    

if __name__ == "__main__": 
    unittest.main()   