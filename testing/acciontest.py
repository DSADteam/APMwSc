import sys
import os
dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../..'))
sys.path.append(dir)

from app.scrum.prod  import clsProducto
from app.scrum.accion import clsAccion
from base import *
import unittest

class accionTester(unittest.TestCase):
    
    def setUp(self):
        self.acc=clsAccion(engine,sessionDB)
        prod=clsProducto(engine,sessionDB)
        prod.insertar("nombreprod","unadescripcion")
        self.prodId = prod.idProd("nombreprod")
        
#TEST INSERTAR

# Casos regulares

    def testinsertar1(self):
        
        pdescripcion = 'Accion 1'
        self.acc.insertar(pdescripcion,self.prodId)
        self.assertTrue(self.acc.existeAccion(descripcion=pdescripcion))

    
    def testinsertar2(self):
        
        pIdProducto = 2
        pdescripcion = 'A'
        self.acc.insertar(pdescripcion,pIdProducto)
        self.assertTrue(self.acc.existeAccion(descripcion=pdescripcion))
     
# casos frontera
    
    def testCampoIdNulo(self):
        
        pIdProducto = None
        pdescripcion = 'Accion 3'
        self.acc.insertar(pdescripcion,pIdProducto)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion))
    
    def testDescripcionNulo(self):
        
        pdescripcion = ''
        self.acc.insertar(pdescripcion,self.prodId)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion))
    
    def testdescripcion500(self):
        
        pdescripcion = 'A'*500
        self.acc.insertar(pdescripcion,self.prodId)
        self.assertTrue(self.acc.existeAccion(pdescripcion))
    
    def testNumEnDescrip(self):
        
        pdescripcion = 234
        self.acc.insertar(pdescripcion,self.prodId)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion))
    
#Caso Esquina
    
    def testTodosVacios(self):
        pIdProducto = None
        pdescripcion = ''
        self.acc.insertar(pdescripcion,pIdProducto)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion))
        
    
    def testIdVacioyDescrip500(self):
        
        
        pIdProducto = None
        pdescripcion = 'B'*500
        self.acc.insertar(pdescripcion,pIdProducto)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion))
    
    def testIdNuloyDescripNum(self):
       
        pIdProducto = None
        pdescripcion = 6589
        self.acc.insertar(pdescripcion,pIdProducto)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion))
    
     
#Caso malicia
   
    def testCharEnIdyDecripNum(self):
        
        pIdProducto = 'bruxw'
        pdescripcion = 345346
        self.acc.insertar(pdescripcion,pIdProducto)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion))

    def testcharEnId(self):
       
        pIdProducto = 'idpepe'
        pdescripcion = 'Accion 2'
        self.acc.insertar(pdescripcion,pIdProducto)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion))
    
    
    def testdescripcion501(self):
        
        pdescripcion = 'X'*501
        self.acc.insertar(pdescripcion,self.prodId)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion))

#TEST MODIFICAR
#casos regulares
    
    def testModificar1(self):
        
        pdescripcion = 'Accion 1'
        self.acc.insertar(pdescripcion,self.prodId)

        pdescripcion2 = 'Accion N1'
        test = self.acc.modificar(self.prodId, pdescripcion2)
        self.assertTrue(self.acc.existeAccion(descripcion=pdescripcion2))
    
#Casos fronteras
    
    def testDescrip500(self):
    
        pdescripcion = 'l'
        self.acc.insertar(pdescripcion,self.prodId)

        pdescripcion2 = 'P'*500
        test = self.acc.modificar(self.prodId, pdescripcion2)
        self.assertTrue(self.acc.existeAccion(descripcion=pdescripcion2))
    
    
    def testDescripAlMin(self):
        
        pdescripcion = 'Accion 1'
        self.acc.insertar(pdescripcion,self.prodId)

        pdescripcion2 = 'A'
        test = self.acc.modificar(self.prodId,pdescripcion2)
        self.assertTrue(self.acc.existeAccion(descripcion=pdescripcion2))

#Casos Esquina
    
    def testModifTodoNul(self):

        pIdProducto2 = None
        pdescripcion2 = ''
        test = self.acc.modificar(pIdProducto2,pdescripcion2)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion2))

    
    def testModifIdNulyDescripNum(self):

        pIdProducto2 = None
        pdescripcion2 = 345
        test = self.acc.modificar(pIdProducto2,pdescripcion2)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion2))
    
    def testModifIdCharyDecripNum(self):

        pIdProducto2 = 'idpepe'
        pdescripcion2 = 4567
        test = self.acc.modificar(pIdProducto2,pdescripcion2)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion2))
    
    def testModifIdCharyDescripNul(self):
    
        pIdProducto2 = 'idpepe'
        pdescripcion2 = ''
        test = self.acc.modificar(pIdProducto2,pdescripcion2)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion2))

#Casos Malicia

    
    def testModifCharEnId(self):
        
        pIdProducto2 = 'hola'
        pdescripcion2 = 'Accion p'
        test = self.acc.modificar(pIdProducto2,pdescripcion2)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion2))
    
    
    def testModifDescrip501(self):

        pdescripcion2 = 'U'*501
        test = self.acc.modificar(self.prodId,pdescripcion2)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion2))
    
    
    def testModifDescripVacio(self):
       
        pdescripcion2 = ''
        test = self.acc.modificar(self.prodId,pdescripcion2)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion2))
    
    def testModifDescripNum(self):
        
        pdescripcion2 = 123
        test = self.acc.modificar(self.prodId,pdescripcion2)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion2))
    
    def testModifIdNulo(self):
        
        pIdProducto2 = None
        pdescripcion2 = 'Accion nula'
        test = self.acc.modificar(pIdProducto2,pdescripcion2)
        self.assertFalse(self.acc.existeAccion(descripcion=pdescripcion2))
    

unittest.main()
    