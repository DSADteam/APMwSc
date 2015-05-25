import sys
import os
dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../..'))
sys.path.append(dir)

from app.scrum.prod import clsProducto
from app.scrum.historias import clsHistoria
from base import *
import unittest

class TestHistoria(unittest.TestCase):
    
    def setUp(self):
        self.his = clsHistoria(engine,sessionDB)
        
    def tearDown(self):
        self.historia.borrarFilas()
        
# TEST INSERTAR

#Casos regulares

    def testinsertar1(self):
        
        pIdProducto = 1
        pdescripcion = 'Historia 1'
        self.his.insertar(pdescripcion,pIdProducto)
        self.assertTrue(self.his.existeHistoria(descripcion=pdescripcion))

    def testinsertar2(self):
      
        pIdProducto = 2
        pdescripcion = 'Historia 2'
        self.his.insertar(pdescripcion,pIdProducto)
        self.assertTrue(self.his.existeHistoria(pdescripcion==descripcion))
        
# Casos fronteras

    def testCampoIdNulo(self):
        
        his = clsHistoria()
        pIdProducto = None
        pdescripcion = 'Historyyyy'
        self.his.insertar(pdescripcion,pIdProducto)
        self.assertTrue(self.his.existeHistoria(descripcion=pdescripcion))

    def testDescripcionNulo(self):
        
        his = clsHistoria()
        pIdProducto = 1
        pdescripcion = ''
        self.his.insertar(pdescripcion,pIdProducto)
        self.assertTrue(self.his.existeHistoria(descripcion=pdescripcion))

    def testdescripcion500(self):
        
        his = clsHistoria()
        pIdProducto = 4
        pdescripcion = 'Haciendo una prueba donde el espacio de lineas es tan largo que debe dar 500 palabras en la descripcion del modulo accion y ya me canse de escribir tanto asi que a partir de ahora pondre puro HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR HODOR y el fin'
        self.his.insertar(pdescripcion,pIdProducto)
        self.assertTrue(self.his.existeHistoria(descripcion=pdescripcion))

    def testNumEnDescrip(self):
        
        his = clsHistoria()
        pIdProducto = 5
        pdescripcion = 234
        self.his.insertar(pdescripcion,pIdProducto)
        self.assertTrue(self.his.existeHistoria(descripcion=pdescripcion))

# Casos Esquinas

    def todosVacios(self):
        
        his = clsHistoria()
        pIdProducto = None
        pdescripcion = ''
        self.his.insertar(pdescripcion,pIdProducto)
        self.assertTrue(self.his.existeHistoria(descripcion=pdescripcion))

    def idVacioyDescrip500(self):
        
        his = clsHistoria()
        pIdProducto = None
        pdescripcion = 'El Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of W'
        self.his.insertar(pdescripcion,pIdProducto)
        self.assertTrue(self.his.existeHistoria(descripcion=pdescripcion))

    def testIdNuloyDescripNum(self):
        
        his = clsHistoria()
        pIdProducto = None
        pdescripcion = 6589
        self.his.insertar(pdescripcion,pIdProducto)
        self.assertTrue(self.his.existeHistoria(descripcion=pdescripcion))

    def testCharEnIdyDecripNum(self):
        
        his = clsHistoria()
        pIdProducto = 'bruxw'
        pdescripcion = 345346
        self.his.insertar(pdescripcion,pIdProducto)
        self.assertTrue(self.his.existeHistoria(descripcion=pdescripcion))
        
# Casos malicias

    def testcharEnId(self):
        
        his = clsHistoria()
        pIdProducto = 'idpepe'
        pdescripcion = 'Historia 2'
        self.his.insertar(pdescripcion,pIdProducto)
        self.assertTrue(self.his.existeHistoria(descripcion=pdescripcion))
    
    def testdescripcion501(self):
        
        his = clsHistoria()
        pIdProducto = 3
        pdescripcion = 'El Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of WA'
        self.his.insertar(pdescripcion,pIdProducto)
        self.assertTrue(self.his.existeHistoria(descripcion=pdescripcion))
        
# TEST MODIFICAR

# Casos Regulares

    def testModificar1(self):
        
        his = clsHistoria()
        pIdProducto = 1
        pdescripcion = 'Historia 1'
        self.his.insertar(pdescripcion,pIdProducto)

        pIdProducto2 = 1
        pdescripcion2 = 'Historia N1'
        test = his.modificar(pIdProducto2, pdescripcion2)
        self.assertTrue(self.his.existeHistoria(descripcion=pdescripcion2))

# Casos fronteras
    
    def testDescrip500(self):
    
        his = clsHistoria()
        pIdProducto = 2
        pdescripcion = 'El Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of W'
        self.his.insertar(pdescripcion,pIdProducto)

        pIdProducto2 = 2
        pdescripcion2 = 'el Mall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of W'
        test = his.modificar(pIdProducto2, pdescripcion2)
        self.assertTrue(self.his.existeHistoria(descripcion=pdescripcion2))

    def testModifNoValid(self):
        
        his = clsHistoria()
        pIdProducto = 123
        pdescripcion = 'Historia 123'
        test = his.modificar(pIdProducto,pdescripcion)
        self.assertFalse(self.his.existeHistoria(descripcion=pdescripcion))

    def testDescripAlMin(self):
        
        his = clsHistoria()
        pIdProducto = 1
        pdescripcion = 'Historia 1'
        self.his.insertar(pdescripcion,pIdProducto)

        pIdProducto2 = 1
        pdescripcion2 = 'A'
        test = his.modificar(pIdProducto2,pdescripcion2)
        self.assertTrue(self.his.existeHistoria(descripcion=pdescripcion2))

# Casos Esquinas

    def testModifTodoNul(self):
        
        his = clsHistoria()
        pIdProducto = 1
        pdescripcion = 'Historia 1'
        self.his.insertar(pdescripcion,pIdProducto)

        pIdProducto2 = None
        pdescripcion2 = ''
        test = his.modificar(pIdProducto2,pdescripcion2)
        self.assertFalse(self.his.existeHistoria(descripcion=pdescripcion2))

    def testModifIdNulyDescripNum(self):
        
        his = clsHistoria()
        pIdProducto = 1
        pdescripcion = 'Historia 1'
        self.his.insertar(pdescripcion,pIdProducto)

        pIdProducto2 = None
        pdescripcion2 = 345
        test = his.modificar(pIdProducto2,pdescripcion2)
        self.assertFalse(self.his.existeHistoria(descripcion=pdescripcion2))

    def testModifIdCharyDecripNum(self):
        
        his = clsHistoria()
        pIdProducto = 1
        pdescripcion = 'Historia 1'
        self.his.insertar(pdescripcion,pIdProducto)

        pIdProducto2 = 'idpepe'
        pdescripcion2 = 4567
        test = his.modificar(pIdProducto2,pdescripcion2)
        self.assertFalse(self.his.existeHistoria(descripcion=pdescripcion2))
    
    def testModifIdCharyDescripNul(self):
       
        his = clsHistoria()
        pIdProducto = 1
        pdescripcion = 'Historia 1'
        self.his.insertar(pdescripcion,pIdProducto)

        pIdProducto2 = 'idpepe'
        pdescripcion2 = ''
        test = his.modificar(pIdProducto2,pdescripcion2)
        self.assertFalse(self.his.existeHistoria(descripcion=pdescripcion2))

# Casos Malicias

    def testModifCharEnId(self):
        
        his = clsHistoria()
        pIdProducto2 = 'hola'
        pdescripcion2 = 'Historia p'
        test = self.his.modificar(pIdProducto2,pdescripcion2)
        self.assertFalse(self.his.existeHistoria(descripcion=pdescripcion2))

    def testModifDescrip501(self):
        
        his = clsHistoria()
        pIdProducto2 = 2
        pdescripcion2 = 'El Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of WA'
        test = his.modificar(pIdProducto2,pdescripcion2)
        self.assertFalse(self.his.existeHistoria(descripcion=pdescripcion2))

    def testModifDescripVacio(self):
        
        his = clsHistoria()
        pIdProducto2 = 1
        pdescripcion2 = ''
        test = self.his.modificar(pIdProducto2,pdescripcion2)
        self.assertFalse(self.his.existeHistoria(descripcion=pdescripcion2))

    def testModifDescripNum(self):
        
        his = clsHistoria()
        pIdProducto2 = 3
        pdescripcion2 = 123
        test = self.his.modificar(pIdProducto2,pdescripcion2)
        self.assertFalse(self.his.existeHistoria(descripcion=pdescripcion2))
    
    def testModifIdNulo(self):
        
        his = clsHistoria()
        pIdProducto2 = None
        pdescripcion2 = 'Historia nula'
        test = self.his.modificar(pIdProducto2,pdescripcion2)
        self.assertFalse(self.his.existeHistoria(descripcion=pdescripcion2))
    
if __name__ == "__main__":
    unittest.main()