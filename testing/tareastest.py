# -*- coding: utf-8 -*-

'''
Created on 10/06/2015
 
@author: Samuel Rodriguez
'''

import sys
import os

dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../..'))
sys.path.append(dir)

from app.scrum.prod      import clsProducto
from app.scrum.historias import clsHistoria
from app.scrum.accion    import clsAccion
from app.scrum.objetivo  import clsObjetivo
from app.scrum.tareas    import clsTarea
from base import *

import unittest

class tareaTester(unittest.TestCase):

     # Inicializacion de casos de prueba
    def setUp(self):

        # Sesion de prueba
        self.tar = clsTarea(engine,sessionDB)
        #Tarea creada para modificaciones

        # Clase producto auxiliar para pruebas
        prod     = clsProducto(engine,sessionDB)
        prod.insertar("ProductoPruebaHistoriaTarea","Descripcion prueba","cualitativo")
        self.prodId = prod.idProd("ProductoPruebaHistoriaTarea")

        # Clase accion auxiliar para pruebas 
        accion = clsAccion(engine,sessionDB)
        accion.insertar("Accion prueba",self.prodId)
        idAccion = accion.obtenerId("Accion prueba")

        # Clase historia auxiliar para pruebas
        hist = clsHistoria(engine,sessionDB)
        hist.insertar("codhist",self.prodId,idPapa=None,tipo="Hola",idAccion=idAccion, prioridad=10)
        self.histId = hist.obtId("codhist",self.prodId)

        self.tar.insertar(self.histId,"Modificable")
        self.idTarModificable = self.tar.obtenerId("Modificable")

    #TEST INSERTAR

    #Insertar una tarea que no existe
    def testInsertarInventado(self):
        tDescripcion = 'Una tarea inventada por ahi'
        self.tar.insertar(self.histId, tDescripcion)
        self.assertTrue(self.tar.existeTarea(tDescripcion,self.histId))

    #Insertar una tarea que ya existe
    def testInsertarExistente(self):
        tDescripcion = 'Esperar la ola' #Esta tarea esta en el poblate
        self.tar.insertar(self.histId, tDescripcion)
        self.assertTrue(self.tar.existeTarea(tDescripcion,self.histId))

    #Insertar con idhistoria nulo
    def testCampoIdNulo(self):
        tDescripcion = 'Esperar las notas' 
        tIdHistoria = None
        self.tar.insertar(tIdHistoria, tDescripcion)
        self.assertFalse(self.tar.existeTarea(tDescripcion,self.histId))

    #Insertar con descripcion nula
    """
    def testDescripcionNulo(self):
        tDescripcion = ''
        self.tar.insertar(self.histId, tDescripcion)
        self.assertFalse(self.tar.existeTarea(tDescripcion,self.histId))
    """

    #Insertar con una descripcion de 500
    def testDescripcion500(self):
        tDescripcion = 'T'*500
        self.tar.insertar(self.histId, tDescripcion)
        self.assertTrue(self.tar.existeTarea(tDescripcion,self.histId))

    #Insertar numeros en la descripcion
    def testNumEnDescrip(self):
        tDescripcion = 678
        self.tar.insertar(self.histId, tDescripcion)
        self.assertFalse(self.tar.existeTarea(tDescripcion,self.histId))

    #Insertar con descripcion 501
    def testDescrip501(self):
        tDescripcion = 'Haciendo una prueba donde el espacio de lineas es dgfdgdfgdfgdfgdfgdfgdfgdfgtan largo que debe dar 500 palabras en la descripcion del modulo tareas y ya me canse de escribir tanto asi que a partir de ahora pondre puro HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR y el fin'
        self.tar.insertar(self.histId, tDescripcion)
        self.assertFalse(self.tar.existeTarea(tDescripcion,self.histId))

    #Casos Esquina

    #Insertar con campos vacios
    def testTodosVacios(self):
        tDescripcion = ''
        tIdHistoria = None
        self.tar.insertar(tIdHistoria, tDescripcion)
        res = self.tar.existeTarea(tDescripcion,self.histId)
        print("MI RES ES: ")
        print(res)
        self.assertFalse(res)

    #Insertar con id vacio y descripcion de 500
    def testIdVacioDescrip500(self):
        tDescripcion = 'A'*500
        tIdHistoria = None
        self.tar.insertar(tIdHistoria, tDescripcion)
        self.assertFalse(self.tar.existeTarea(tDescripcion,None))

    #Insertar con id nulo y descripcion con numeros
    def testIdNuloDescripNum(self):
        tDescripcion = 564
        tIdHistoria = None
        self.tar.insertar(tIdHistoria, tDescripcion)
        self.assertFalse(self.tar.existeTarea(tDescripcion,self.histId))

    #Casos Malicia

    #Insertar caracteres en el id 
    def testCharEnId(self):
        tIdHistoria = 'hola'
        tDescripcion = 'Comprar unicornios'
        self.tar.insertar(tIdHistoria, tDescripcion)
        self.assertFalse(self.tar.existeTarea(tDescripcion,self.histId))

    #Insertar caracteres en el id y descripcion con numeros
    def testCharEnIdyDescripNum(self):
        tDescripcion = 234
        tIdHistoria = 'hola'
        self.tar.insertar(tIdHistoria, tDescripcion)
        self.assertFalse(self.tar.existeTarea(tDescripcion,self.histId))

    #TEST MODIFICAR

    #Modificar una descripcion
    def testModificar(self):
        tDescripcion2 = 'Esperar la cola'
        self.tar.modificar(self.idTarModificable,tDescripcion2)
        self.assertTrue(self.tar.existeTarea(tDescripcion2,self.histId))

    #Modificar a un máximo tamaño de descripcion
    def testModif500(self):
        tDescripcion2 = 'q'*500
        self.tar.modificar(self.idTarModificable,tDescripcion2)
        self.assertTrue(self.tar.existeTarea(tDescripcion2,self.histId))

    #Modificar descripcion a 501
    def testModif501(self):
        tDescripcion2 = 'q'*501
        self.tar.modificar(self.idTarModificable,tDescripcion2)
        self.assertFalse(self.tar.existeTarea(tDescripcion2,self.histId))

    #Modificar la descripcion al minimo
    def testModif1(self):
        tDescripcion2 = 'T'
        self.tar.modificar(self.idTarModificable,tDescripcion2)
        self.assertTrue(self.tar.existeTarea(tDescripcion2,self.histId))

    #Modificar la descripcion a nulo
    def testModifDescripVacio(self):
        tDescripcion2 = ''
        self.tar.modificar(self.idTarModificable,tDescripcion2)
        self.assertFalse(self.tar.existeTarea(tDescripcion2,self.histId))

    #Modificar la descripcion con numeros
    def testModifDescripNum(self):
        tDescripcion2 = 1234
        self.tar.modificar(self.idTarModificable,tDescripcion2)
        self.assertFalse(self.tar.existeTarea(tDescripcion2,self.histId))

    #Casos Esquina

    #Modificar id y descripcion a nulos
    def testModifCamposNulo(self):
        tDescripcion2 = ''
        tIdHistoria2 = None
        self.tar.modificar(tIdHistoria2,tDescripcion2)
        self.assertFalse(self.tar.existeTarea(tDescripcion2,self.histId))

    #Modificar id a nulo y descripcion a numero
    def testModifIdNuloyDescripNum(self):
        tDescripcion2 = 89
        tIdHistoria2 = None
        self.tar.modificar(tIdHistoria2,tDescripcion2)
        self.assertFalse(self.tar.existeTarea(tDescripcion2,self.histId))

    #Modificar id a caracteres y descripcion a numeros
    def testModifIdCharyDescripNum(self):
        tDescripcion2 = 233
        tIdHistoria2 = 'idhola'
        self.tar.modificar(tIdHistoria2,tDescripcion2)
        self.assertFalse(self.tar.existeTarea(tDescripcion2,self.histId))

    #Casos Malicia

    #Modificar id a caracteres
    def testModifIdChar(self):
        tDescripcion2 = 'Surfear sin reglas'
        tIdHistoria2 = 'idhola'
        self.tar.modificar(tIdHistoria2,tDescripcion2)
        self.assertFalse(self.tar.existeTarea(tDescripcion2,self.histId))

    # TEST ELIMINAR

    # Eliminar tarea inexistente
    def testElimInexistente(self):
        pIdTarea = 190223
        pdescripcion = ''
        self.tar.eliminar(pIdTarea)
        self.assertFalse(self.tar.existeTarea(pdescripcion,self.histId))

    # Eliminar tarea que sea None
    def testElimVacio(self):
        pIdTarea = None
        pdescripcion = ''
        self.tar.eliminar(pIdTarea)
        self.assertFalse(self.tar.existeTarea(pdescripcion,self.histId))

    # Eliminar tarea existente
    def testElimExistente(self):
        pdescripcion = "Tarea de testElimExistente"
        self.tar.insertar(self.histId, pdescripcion)
        pIdTarea = self.tar.obtenerId(pdescripcion)
        print("El id de la tarea es ")
        print(pIdTarea)
        self.tar.eliminar(pIdTarea)
        self.assertFalse(self.tar.existeIdTarea(pIdTarea))

if __name__ == "__main__":
    unittest.main()
