# -*- coding: utf-8 -*-

'''
Created on 15/05/2015
 
@author: Meggie Sanchez y Cristina Betancourt
'''

import os
import sys
dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../..'))
sys.path.append(dir)

from app.scrum.objetivo import *

import base

import unittest

class TestObjetivo(unittest.TestCase):

    # Insertar de objetivo 
    
    # Casos interiores
    
    # Insertar un objetivo que no existe
    def TestInsertar1(self):
        
        objs = clsObjetivo()
        pIdObjetivo = 1
        pDescripcion = 'Terminar tarea'
        r = objs.insertarObj(pIdObjetivo, pDescripcion)
        self.assertTrue(r) 

     # Insertar un objetivo que existe
    def TestInsertar2(self):
        
        objs = clsObjetivo()
        pIdObjetivo = 1
        pDescripcion = 'Terminar tarea'
        r = objs.insertarObj(pIdObjetivo, pDescripcion)
        self.assertFalse(r) 
         
    # Casos fronteras
    
    # Insertar un objetivo con el minimo numero de caracteres en descripcion
    def TestInsertar3(self):
        
        objs = clsObjetivo()
        pIdObjetivo = 2
        pDescripcion = 'T'
        r = objs.insertarObj(pIdObjetivo, pDescripcion)
        self.assertTrue(r) 

    # Insertar un objetivo con el maximo numero de caracteres en descripcion
    def TestInsertar4(self):
        
        objs = clsObjetivo()
        pIdObjetivo = 3
        pDescripcion = 'd'*500
        r = objs.insertarObj(pIdObjetivo, pDescripcion)
        self.assertTrue(r) 
        
    # Insertar un objetivp con el minimo numero en idObjetivo
    def TestInsertar5(self):
        
        objs = clsObjetivo()
        pIdObjetivo = 4
        pDescripcion = 'e'*500
        r = objs.insertarObj(pIdObjetivo, pDescripcion)
        self.assertTrue(r) 
     
    # Insertar un objetivo con el maximo numero en idObjetivo
    def TestInsertar6(self):
        
        objs = clsObjetivo()
        pIdObjetivo = (2**31)-1
        pDescripcion = 'h'*500
        r = objs.insertarObj(pIdObjetivo, pDescripcion)
        self.assertTrue(r) 

    # Casos esquinas
    
    # Insertar un objetivo con el minimo numero en idObjetivo y el minimo de caracteres en descripcion
    def TestInsertar7(self):
        
        objs = clsObjetivo()
        pIdObjetivo = 5
        pDescripcion = 'r'
        r = objs.insertarObj(pIdObjetivo, pDescripcion)
        self.assertTrue(r) 
        
    # Insertar un objetivo con el minimo numero en idObjetivo y el maximo de caracteres en descripcion
    def TestInsertar8(self):
        
        objs = clsObjetivo()
        pIdObjetivo = 6
        pDescripcion = 'g'*500
        r = objs.insertarObj(pIdObjetivo, pDescripcion)
        self.assertTrue(r) 

    # Insertar un objetivo con el maximo numero en idObjetivo y el mínimo de caracteres en descripcion
    def TestInsertar9(self):
        
        objs = clsObjetivo()
        pIdObjetivo = (2**31)-1
        pDescripcion = 'a'
        r = objs.insertarObj(pIdObjetivo, pDescripcion)
        self.assertTrue(r) 

    # Insertar un objetivo con el maximo numero en idObjetivo y el maximo de caracteres en descripcion
    def TestInsertar10(self):
        
        objs = clsObjetivo()
        pIdObjetivo = (2**31)-1
        pDescripcion = 'b'*500
        r = objs.insertarObj(pIdObjetivo, pDescripcion)
        self.assertTrue(r) 

    # Casos maliciosos
    
    # Insertar un objetivo con cadena vacia en descripcion
    def TestInsertar11(self):

        objs = clsObjetivo()
        pIdObjetivo = 7
        pDescripcion = ''
        r = objs.insertarObj(pIdObjetivo, pDescripcion)
        self.assertFalse(r)

    # Insertar un objetivo que excede los 500 caracteres en descripcion
    def TestInsertar12(self):
        
        objs = clsObjetivo()
        pIdObjetivo = 8
        pDescripcion = 'l'*501
        r = objs.insertarObj(pIdObjetivo, pDescripcion)
        self.assertFalse(r)
        
    # Insertar un objetivo con enteros en descripcion
    def TestInsertar13(self):
        
        objs = clsObjetivo()
        pIdObjetivo = 356456
        pDescripcion = 3245345
        r = objs.insertarObj(pIdObjetivo, pDescripcion)
        self.assertFalse(r)
       
    # Insertar un objetivo con string en idObjetivo
    def TestInsertar14(self):
        
        objs = clsObjetivo()
        pIdObjetivo = 'fghfgh'
        pDescripcion = 32
        r = objs.insertarObj(pIdObjetivo, pDescripcion)
        self.assertFalse(r)
        
    # Insertar un objetivo con nada como idrole
    def TestInsertar15(self):
        
        objs = clsObjetivo()
        pIdObjetivo = None
        pDescripcion = 'dfghjj'
        r = objs.insertarObj(pIdObjetivo, pDescripcion)
        self.assertFalse(r)
        
    # Modificar de objetivo
        
    # Casos interiores
    
    

    # Modificar un objetivo que ya existe
    
    def TestModificar1(self):

        objs = clsObjetivo()
        pIdObjetivo = 9
        pDescripcion = 'holaaa'
        objs.insertarObj(pIdObjetivo, pDescripcion)
        
        pIdObjetivo2 = 9
        pDescripcion2 = 'holaaa22'
        r = objs.modificarObj(pIdObjetivo2, pDescripcion2)
        self.assertTrue(r)         
    
    # Modificar un objetivo que no existe
    def TestModificar2(self):
        
        objs = clsObjetivo()
        r = objs.modificarObj(45356456, 'holapa')
        self.assertFalse(r)  
    
    # Casos Fronteras
    
    # Modificar un objetivo que tiene el minimo numero en idObjetivo
    def TestModificar3(self):
  
        objs = clsObjetivo()
        pIdObjetivo = 1 
        pDescripcion = 'holaaajejeps'
        objs.insertarObj(pIdObjetivo, pDescripcion)
        
        pIdObjetivo2 = 1 
        pDescripcion2 = 'holaaajejeps23'
        r = objs.modificarObj(pIdObjetivo2, pDescripcion2)
        self.assertTrue(r)  
    
    # Modificar un objetivo que tiene el maximo numero en idObjetivo
    def TestModificar4(self):

        objs = clsObjetivo()
        pIdObjetivo = (2**31)-1
        pDescripcion = 'holaaajejeps12'
        objs.insertarObj(pIdObjetivo, pDescripcion)
        
        pIdObjetivo2 = (2**31)-1
        pDescripcion2 = 'holaaajejeps234'
        r = objs.modificarObj(pIdObjetivo2, pDescripcion2)
        self.assertTrue(r) 
        
    # Modificar un objetivo que tiene el maximo de caracteres en descripcion
    def TestModificar5(self):
        
        objs = clsObjetivo()
        pIdObjetivo = 76
        pDescripcion = 'ñ'*500
        objs.insertarObj(pIdObjetivo, pDescripcion)
        
        pIdObjetivo2 = 76
        pDescripcion2 = 'v'*500
        r = objs.modificarObj(pIdObjetivo2, pDescripcion2)
        self.assertTrue(r) 
    
    # Modificar un objetivo que tiene el minimo de caracteres en descripcion
    def TestModificar6(self):
        
        objs = clsObjetivo()
        pIdObjetivo = 00
        pDescripcion = 'dgbdfb'
        objs.insertarObj(pIdObjetivo, pDescripcion)
        
        pIdObjetivo2 = 00
        pDescripcion2 = 'v'
        r = objs.modificarObj(pIdObjetivo2, pDescripcion2)
        self.assertTrue(r) 
    
    # Casos Esquinas
    
    # Modificar un objetivo que tiene el minimo numero en idObjetivo y el maximo de caracteres en descripcion
    def TestModificar7(self): 
        
        objs = clsObjetivo()
        pIdObjetivo = 0
        pDescripcion = 'z'*500
        objs.insertarObj(pIdObjetivo, pDescripcion)
        
        pIdObjetivo2 = 0
        pDescripcion2 = '6'*500
        r = objs.modificarObj(pIdObjetivo2, pDescripcion2)
        self.assertTrue(r) 
        
    # Modificar un objetivo que tiene el minimo numero en idObjetivo y el minimo de caracteres en descripcion
    def TestModificar8(self):
        
        objs = clsObjetivo()
        pIdObjetivo = 8
        pDescripcion = 'rdf'
        objs.insertarObj(pIdObjetivo, pDescripcion)
        
        pIdObjetivo2 = 8
        pDescripcion2 = 'g'
        r = objs.modificarObj(pIdObjetivo2, pDescripcion2)
        self.assertTrue(r) 
    
    # Modificar un objetivo que tiene el maximo numero en idObjetivo y el minimo de caracteres en descripcion
    def TestModificar9(self):
        
        objs = clsObjetivo()
        pIdObjetivo = (2**31)-1
        pDescripcion = 'cgfhjhj'
        objs.insertarObj(pIdObjetivo, pDescripcion)
        
        pIdObjetivo2 = (2**31)-1
        pDescripcion2 = 'g'
        r = objs.modificarObj(pIdObjetivo2, pDescripcion2)
        self.assertTrue(r) 

    # Modificar un objetivo que tiene el maximo numero en idObjetivo y el maximo de caracteres en descripcion
    def TestModificar10(self):
        
        objs = clsObjetivo()
        pIdObjetivo = (2**31)-1
        pDescripcion = 'j'
        objs.insertarObj(pIdObjetivo, pDescripcion)
        
        pIdObjetivo2 = (2**31)-1
        pDescripcion2 = 'g'*500
        r = objs.modificarObj(pIdObjetivo2, pDescripcion2)
        self.assertTrue(r) 

    # Casos maliciosos

    # Modificar un objetivo que tiene como idObjetivo un string
    def TestModificar11(self):     
        
        objs = clsObjetivo()
        pIdObjetivo2 = '234'
        pDescripcion2 = 'g'*500
        r = objs.modificarObj(pIdObjetivo2, pDescripcion2)
        self.assertFalse(r)      
    
    # Modificar un objetivo que tiene como descripcion una cadena vacia
    def TestModificar13(self):  
        
        objs = clsObjetivo()
        pIdObjetivo2 = 1
        pDescripcion2 = ''
        r = objs.modificarObj(pIdObjetivo2, pDescripcion2)
        self.assertFalse(r)    
          
    # Modificar un objetivo que excede los 500 caracteres en descripcion
    def TestModificar14(self):      
        
        objs = clsObjetivo()
        pIdObjetivo2 = 1
        pDescripcion2 = 'o'*501
        r = objs.modificarObj(pIdObjetivo2, pDescripcion2)
        self.assertFalse(r)     

    # Modificar un objetivo que tiene enteros en descripcion
    def TestModificar15(self):        
        
        objs = clsObjetivo()
        pIdObjetivo2 = 1
        pDescripcion2 = 501
        r = objs.modificarObj(pIdObjetivo2, pDescripcion2)
        self.assertFalse(r)    
        