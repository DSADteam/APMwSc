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

    # Insertar de objetivo 
    
    # Casos interiores
    
    # Insertar un objetivo que no existe
    def testInsertar1(self):
        
        pIdObjetivo = 1
        pDescripcion = 'Terminar tarea'
        self.objetivo.insertar(pIdObjetivo, pDescripcion)
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion)) 

     # Insertar un objetivo que existe
    def testInsertar2(self):
        
        pIdObjetivo = 1
        pDescripcion = 'Terminar tarea'
        self.objetivo.insertar(pIdObjetivo, pDescripcion)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion)) 
         
    # Casos fronteras
''' 
    # Insertar un objetivo con el minimo numero de caracteres en descripcion
    def testInsertar3(self):
        
        pIdObjetivo = 2
        pDescripcion = 'T'
        self.objetivo.insertar(pIdObjetivo, pDescripcion)
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion)) 

    # Insertar un objetivo con el maximo numero de caracteres en descripcion
    def testInsertar4(self):
        
        pIdObjetivo = 3
        pDescripcion = 'd'*500
        self.objetivo.insertar(pIdObjetivo, pDescripcion)
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion)) 
        
    # Insertar un objetivp con el minimo numero en idObjetivo
    def testInsertar5(self):
        
        pIdObjetivo = 4
        pDescripcion = 'e'*500
        self.objetivo.insertar(pIdObjetivo, pDescripcion)
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion)) 
     
    # Insertar un objetivo con el maximo numero en idObjetivo
    def testInsertar6(self):
        
        pIdObjetivo = (2**31)-1
        pDescripcion = 'h'*500
        self.objetivo.insertar(pIdObjetivo, pDescripcion)
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion)) 

    # Casos esquinas
    
    # Insertar un objetivo con el minimo numero en idObjetivo y el minimo de caracteres en descripcion
    def testInsertar7(self):
        
        pIdObjetivo = 5
        pDescripcion = 'r'
        self.objetivo.insertar(pIdObjetivo, pDescripcion)
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion)) 
        
    # Insertar un objetivo con el minimo numero en idObjetivo y el maximo de caracteres en descripcion
    def testInsertar8(self):
        
        pIdObjetivo = 6
        pDescripcion = 'g'*500
        self.objetivo.insertar(pIdObjetivo, pDescripcion)
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion)) 

    # Insertar un objetivo con el maximo numero en idObjetivo y el mínimo de caracteres en descripcion
    def testInsertar9(self):
        
        pIdObjetivo = (2**31)-1
        pDescripcion = 'a'
        self.objetivo.insertar(pIdObjetivo, pDescripcion)
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion)) 

    # Insertar un objetivo con el maximo numero en idObjetivo y el maximo de caracteres en descripcion
    def testInsertar10(self):
        
        pIdObjetivo = (2**31)-1
        pDescripcion = 'b'*500
        self.objetivo.insertar(pIdObjetivo, pDescripcion)
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion)) 

    # Casos maliciosos
    
    # Insertar un objetivo con cadena vacia en descripcion
    def testInsertar11(self):

        pIdObjetivo = 7
        pDescripcion = ''
        self.objetivo.insertar(pIdObjetivo, pDescripcion)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion))

    # Insertar un objetivo que excede los 500 caracteres en descripcion
    def testInsertar12(self):
        
        pIdObjetivo = 8
        pDescripcion = 'l'*501
        self.objetivo.insertar(pIdObjetivo, pDescripcion)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion))
        
    # Insertar un objetivo con enteros en descripcion
    def testInsertar13(self):
        
        pIdObjetivo = 356456
        pDescripcion = 3245345
        self.objetivo.insertar(pIdObjetivo, pDescripcion)
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

        pIdObjetivo = 9
        pDescripcion = 'holaaa'
        self.objetivo.insertar(pIdObjetivo, pDescripcion)
        
        pIdObjetivo2 = 9
        pDescripcion2 = 'holaaa22'
        self.objetivo.modificar(pIdObjetivo2, pDescripcion2)
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion))         
    
    # Modificar un objetivo que no existe
    def testModificar2(self):
        pDescripcion='holapa'
        self.objetivo.modificar(45356456, pDescripcion)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion))  
    
    # Casos Fronteras
    
    # Modificar un objetivo que tiene el minimo numero en idObjetivo
    def testModificar3(self):
  
        pIdObjetivo = 1 
        pDescripcion = 'holaaajejeps'
        self.objetivo.insertar(pIdObjetivo, pDescripcion)
        
        pIdObjetivo2 = 1 
        pDescripcion2 = 'holaaajejeps23'
        self.objetivo.modificar(pIdObjetivo2, pDescripcion2)
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion))  
    
    # Modificar un objetivo que tiene el maximo numero en idObjetivo
    def testModificar4(self):

        pIdObjetivo = (2**31)-1
        pDescripcion = 'holaaajejeps12'
        self.objetivo.insertar(pIdObjetivo, pDescripcion)
        
        pIdObjetivo2 = (2**31)-1
        pDescripcion2 = 'holaaajejeps234'
        self.objetivo.modificar(pIdObjetivo2, pDescripcion2)
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion)) 
        
    # Modificar un objetivo que tiene el maximo de caracteres en descripcion
    def testModificar5(self):
        
        pIdObjetivo = 76
        pDescripcion = 'ñ'*500
        self.objetivo.insertar(pIdObjetivo, pDescripcion)
        
        pIdObjetivo2 = 76
        pDescripcion2 = 'v'*500
        self.objetivo.modificar(pIdObjetivo2, pDescripcion2)
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion)) 
    
    # Modificar un objetivo que tiene el minimo de caracteres en descripcion
    def testModificar6(self):
        
        pIdObjetivo = 00
        pDescripcion = 'dgbdfb'
        self.objetivo.insertar(pIdObjetivo, pDescripcion)
        
        pIdObjetivo2 = 00
        pDescripcion2 = 'v'
        self.objetivo.modificar(pIdObjetivo2, pDescripcion2)
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion)) 
    
    # Casos Esquinas
    
    # Modificar un objetivo que tiene el minimo numero en idObjetivo y el maximo de caracteres en descripcion
    def testModificar7(self): 
        
        pIdObjetivo = 0
        pDescripcion = 'z'*500
        self.objetivo.insertar(pIdObjetivo, pDescripcion)
        
        pIdObjetivo2 = 0
        pDescripcion2 = '6'*500
        self.objetivo.modificar(pIdObjetivo2, pDescripcion2)
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion)) 
        
    # Modificar un objetivo que tiene el minimo numero en idObjetivo y el minimo de caracteres en descripcion
    def testModificar8(self):
        
        pIdObjetivo = 8
        pDescripcion = 'rdf'
        self.objetivo.insertar(pIdObjetivo, pDescripcion)
        
        pIdObjetivo2 = 8
        pDescripcion2 = 'g'
        self.objetivo.modificar(pIdObjetivo2, pDescripcion2)
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion)) 
    
    # Modificar un objetivo que tiene el maximo numero en idObjetivo y el minimo de caracteres en descripcion
    def testModificar9(self):
        
        pIdObjetivo = (2**31)-1
        pDescripcion = 'cgfhjhj'
        self.objetivo.insertar(pIdObjetivo, pDescripcion)
        
        pIdObjetivo2 = (2**31)-1
        pDescripcion2 = 'g'
        self.objetivo.modificar(pIdObjetivo2, pDescripcion2)
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion)) 

    # Modificar un objetivo que tiene el maximo numero en idObjetivo y el maximo de caracteres en descripcion
    def testModificar10(self):
        
        pIdObjetivo = (2**31)-1
        pDescripcion = 'j'
        self.objetivo.insertar(pIdObjetivo, pDescripcion)
        
        pIdObjetivo2 = (2**31)-1
        pDescripcion2 = 'g'*500
        self.objetivo.modificar(pIdObjetivo2, pDescripcion2)
        self.assertTrue(self.objetivo.existeObjetivo(pDescripcion)) 

    # Casos maliciosos

    # Modificar un objetivo que tiene como idObjetivo un string
    def testModificar11(self):     
        
        pIdObjetivo2 = '234'
        pDescripcion2 = 'g'*500
        self.objetivo.modificar(pIdObjetivo2, pDescripcion2)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion))      
    
    # Modificar un objetivo que tiene como descripcion una cadena vacia
    def testModificar13(self):  
        
        pIdObjetivo2 = 1
        pDescripcion2 = ''
        self.objetivo.modificar(pIdObjetivo2, pDescripcion2)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion))    
          
    # Modificar un objetivo que excede los 500 caracteres en descripcion
    def testModificar14(self):      
        
        pIdObjetivo2 = 1
        pDescripcion2 = 'o'*501
        self.objetivo.modificar(pIdObjetivo2, pDescripcion2)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion))     

    # Modificar un objetivo que tiene enteros en descripcion
    def testModificar15(self):        
        
        pIdObjetivo2 = 1
        pDescripcion2 = 501
        self.objetivo.modificar(pIdObjetivo2, pDescripcion2)
        self.assertFalse(self.objetivo.existeObjetivo(pDescripcion))    
'''
if __name__ == "__main__": 
    unittest.main()   