# -*- coding: utf-8 -*-

'''
Created on 10/06/2015
 
@author: Samuel Rodriguez
'''

import sys
import os

dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../..'))
sys.path.append(dir)

from app.scrum.historias import clsHistoria
from app.scrum.tareas import clsTarea
from base import *
import unittest

class tareaTester(unittest.TestCase):

	 # Inicializacion de casos de prueba
    def setUp(self):
        self.tar = clsTarea(engine,sessionDB)
        hist = clsHistoria(engine,sessionDB)
        hist.insertar("codhist","Opcional") #Falta
        self.histId = hist.idHistoria("codhist")

    #TEST INSERTAR

    #Insertar una tarea que no existe
    def testInsertarInventado(self):
    	tDescripcion = 'Una tarea inventada por ahi'
    	self.tar.insertar(self.histId, tDescripcion)
    	self.assertTrue(self.tar.existeTarea(tDescripcion))

    #Insertar una tarea que ya existe
    def testInsertarExistente(self0):
    	tDescripcion = 'Esperar la ola' #Esta tarea esta en el poblate
    	self.tar.insertar(self.histId, tDescripcion)
    	self.assertTrue(self.tar.existeTarea(tDescripcion))

    #Inserta con idhistoria nulo
    def testCampoIdNulo(self):
    	tDescripcion = 'Esperar las notas' 
    	tIdHistoria = None
    	self.tar.insertar(tIdHistoria, tDescripcion)
    	self.assertFalse(self.tar.existeTarea(tDescripcion))

    #Insertar con descripcion nula
    def testDescripcionNulo(self):
    	tDescripcion = ''
    	self.tar.insertar(self.histID, tDescripcion)
    	self.assertFalse(self.tar.existeTarea(tDescripcion))

    #Insertar on una descripcion de 500
    def testDescripcion500(self):
    	tDescripcion = 'T'*500
    	self.tar.insertar(self.histID, tDescripcion)
    	self.assertTrue(self.tar.existeTarea(tDescripcion))

    #Insertar numeros en la descripcion
    def testNumEnDescrip(self):
    	tDescripcion = 678
    	self.tar.insertar(self.histID, tDescripcion)
    	self.assertFalse(self.tar.existeTarea(tDescripcion))

    #Insertar con descripcion 501
    def testDescrip501(self):
    	tDescripcion = 'Haciendo una prueba donde el espacio de lineas es tan largo que debe dar 500 palabras en la descripcion del modulo tareas y ya me canse de escribir tanto asi que a partir de ahora pondre puro HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR y el fin'
    	self.tar.insertar(self.histID, tDescripcion)
    	self.assertFalse(self.tar.existeTarea(tDescripcion))

    #Casos Esquina

    #Insertar con campos vacios
    def testTodosVacios(self):
    	tDescripcion = ''
    	tIdHistoria = None
    	self.tar.insertar(tIdHistoria, tDescripcion)
    	self.assertFalse(self.tar.existeTarea(tDescripcion))

    #Insertar con id vacio y descripcion de 500
    def testIdVacioDescrip500(self):
    	tDescripcion = 'A'*500
    	tIdHistoria = None
    	self.tar.insertar(tIdHistoria, tDescripcion)
    	self.assertFalse(self.tar.existeTarea(tDescripcion))

    #Insertar con id nulo y descripcion con numeros
    def testIdNuloDescripNum(self):
    	tDescripcion = 564
    	tIdHistoria = None
    	self.tar.insertar(tIdHistoria, tDescripcion)
    	self.assertFalse(self.tar.existeTarea(tDescripcion))

    #Casos Malicia

    #Insertar caracteres en el id 
    def testCharEnId(self):
    	tIdHistoria = 'hola'
    	tDescripcion = 'Comprar unicornios'
    	self.tar.insertar(tIdHistoria, tDescripcion)
    	self.assertFalse(self.tar.existeTarea(tDescripcion))
    #Insertar caracteres en el id y descripcion con numeros
    def testCharEnIdyDescripNum(self):
    	tDescripcion = 234
    	tIdHistoria = 'hola'
    	self.tar.insertar(tIdHistoria, tDescripcion)
    	self.assertFalse(self.tar.existeTarea(tDescripcion))

    #TEST MODIFICAR

    #Modificar una descripcion
    def testModificar(self):
    	tDescripcion2 = 'Esperar la cola'
    	self.tar.modificar(self.histID,tDescripcion2)
    	self.assertTrue(self.tar.existeTarea(tDescripcion2))

    #Modificar a un máximo tamaño de descripcion
    def testModif500(self):
    	tDescripcion2 = 'q'*500
    	self.tar.modificar(self.histID,tDescripcion2)
    	self.assertTrue(self.tar.existeTarea(tDescripcion2))

    #Modificar descripcion a 501
    def testModif501(self):
    	tDescripcion2 = 'q'*501
    	self.tar.modificar(self.histID,tDescripcion2)
    	self.assertFalse(self.tar.existeTarea(tDescripcion2))

    #Modificar la descripcion al minimo
    def testModif1(self):
    	tDescripcion2 = 'T'
    	self.tar.modificar(self.histID,tDescripcion2)
    	self.assertTrue(self.tar.existeTarea(tDescripcion2))

    #Modificar la descripcion a nulo
    def testModifDescripVacio(self):
    	tDescripcion2 = ''
    	self.tar.modificar(self.histID,tDescripcion2)
    	self.assertFalse(self.tar.existeTarea(tDescripcion2))

    #Modificar la
    def testModifDescripNum(self):
    	tDescripcion2 = 1234
    	self.tar.modificar(self.histID,tDescripcion2)
    	self.assertFalse(self.tar.existeTarea(tDescripcion2))

    #Casos Esquina

    #Modificar id y descripcion a nulos

    def testModifCamposNulo(self):
    	tDescripcion2 = ''
    	tIdHistoria2 = None
    	self.tar.modificar(tIdHistoria2,tDescripcion2)
    	self.assertFalse(self.tar.existeTarea(tDescripcion2))

    #Modificar id a nulo y descripcion a numero
    def testModifIdNuloyDescripNum(self):
    	tDescripcion2 = 89
    	tIdHistoria2 = None
    	self.tar.modificar(tIdHistoria2,tDescripcion2)
    	self.assertFalse(self.tar.existeTarea(tDescripcion2))

    #Modificar id a caracteres y descripcion a numeros
    def testModifIdCharyDescripNum(self):
    	tDescripcion2 = 233
    	tIdHistoria2 = 'idhola'
    	self.tar.modificar(tIdHistoria2,tDescripcion2)
    	self.assertFalse(self.tar.existeTarea(tDescripcion2))

    #Casos Malicia

    #Modificar id a caracteres
    def testModifIdChar(self):
    	tDescripcion2 = 'Surfear sin reglas'
    	tIdHistoria2 = 'idhola'
    	self.tar.modificar(tIdHistoria2,tDescripcion2)
    	self.assertFalse(self.tar.existeTarea(tDescripcion2))

if __name__ == "__main__":
    unittest.main()
