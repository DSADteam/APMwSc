import sys
import os
dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../..'))
sys.path.append(dir)

from app.scrum.prod      import clsProducto
from app.scrum.historias import clsHistoria
from app.scrum.accion    import clsAccion
from app.scrum.objetivo  import clsObjetivo
from base import *
import unittest


class TestHistoria(unittest.TestCase):
    
    def setUp(self):
        #Sesion de prueba
        self.his = clsHistoria(engine,sessionDB)

        #Clase producto auxiliar para pruebas
        prod     = clsProducto(engine,sessionDB)
        prod.insertar("ProductoPruebaHistoria","Descripcion prueba")
        self.prodId = prod.idProd("ProductoPruebaHistoria")

       
    def tearDown(self):
        #self.historia.borrarFilas()
        pass
        
# TEST INSERTAR

# Casos fronteras

    def testInsertar500(self):
        accion          = clsAccion(engine,sessionDB)
        accion.insertar("Accion prueba 500",self.prodId)
        idAccion = accion.obtenerId("Accion prueba 500")

        hCodigo   = "a" * 500
        hTipo     = "Historia de test500"
        self.his.insertar(hCodigo,self.prodId,idPapa=None,tipo=hTipo,idAccion=idAccion)
        self.assertTrue(self.his.existeHistoria(codigo=hCodigo,idProducto=self.prodId))    
    
    def testInsertar500SinAccion(self):
        hCodigo   = "c" * 500
        hTipo     = "Historia de test 501"
        self.his.insertar(hCodigo,self.prodId,idPapa=None,tipo=hTipo,idAccion=None)
        self.assertFalse(self.his.existeHistoria(codigo=hCodigo,idProducto=self.prodId))
    
    def testInsertar501Codigo(self):
        accion   = clsAccion(engine,sessionDB)
        accion.insertar("Accion prueba 501",self.prodId)
        idAccion = accion.obtenerId("Accion prueba 501")

        hCodigo   = "b" * 501
        hTipo     = "Historia de test 501"
        self.his.insertar(hCodigo,self.prodId,idPapa=None,tipo=hTipo,idAccion=idAccion)
        self.assertFalse(self.his.existeHistoria(codigo=hCodigo,idProducto=self.prodId))


    def testCodigoVacio(self):
        accion   = clsAccion(engine,sessionDB)
        accion.insertar("Accion codigo vacio",self.prodId)
        idAccion = accion.obtenerId("Accion codigo vacio")

        hCodigo = ''
        hTipo     = "Otro tipo de historia"
        self.his.insertar(hCodigo,self.prodId,idPapa=None,tipo=hTipo,idAccion=idAccion)
        self.assertFalse(self.his.existeHistoria(codigo=hCodigo,idProducto=self.prodId))


    def testCampoIdNulo(self):
        accion   = clsAccion(engine,sessionDB)
        accion.insertar("Accion para IdProductoNulo",self.prodId)
        idAccion = accion.obtenerId("Accion para IdProductoNulo")

        his = clsHistoria()
        pIdProducto = None
        hCodigo  = 'Just Pepe'
        hTipo    = "Otro tipo de historia"
        self.his.insertar(hCodigo,self.prodId,idPapa=None,tipo=hTipo,idAccion=idAccion)
        self.assertFalse(self.his.existeHistoria(codigo=hCodigo,idProducto=pIdProducto))

    def testProductoInexistente(self):
        accion   = clsAccion(engine,sessionDB)
        accion.insertar("Accion para testProductoInexistente",self.prodId)
        idAccion = accion.obtenerId("Accion para testProductoInexistente")

        his = clsHistoria()
        pIdProducto = 666
        hCodigo  = 'Just Pepe with product that doesnt exists'
        hTipo    = "The number of the beast"
        self.his.insertar(hCodigo,pIdProducto,idPapa=None,tipo=hTipo,idAccion=idAccion)
        self.assertFalse(self.his.existeHistoria(codigo=hCodigo,idProducto=pIdProducto))
    
    def testNumEnDescrip(self):
        accion   = clsAccion(engine,sessionDB)
        accion.insertar("Accion para testNumEnDescrip",self.prodId)
        idAccion = accion.obtenerId("Accion para testNumEnDescrip")

        his = clsHistoria(engine,sessionDB)
        hCodigo = 234
        hTipo   = "So much tipe, and wow"
        self.his.insertar(hCodigo,self.prodId,idPapa=None,tipo=hTipo,idAccion=idAccion)
        self.assertFalse(self.his.existeHistoria(codigo=hCodigo,idProducto=self.prodId))

    def testTwoHistsOneAct(self):
        accion   = clsAccion(engine,sessionDB)
        accion.insertar("Accion para compartir entre dos historias",self.prodId)
        idAccion = accion.obtenerId("Accion para compartir entre dos historias")

        #Historia a agregar
        his = clsHistoria(engine,sessionDB)
        hCodigo = "Soy Historia 1 y pasare"
        hTipo   = "Tipo"
        self.his.insertar(hCodigo,self.prodId,idPapa=None,tipo=hTipo,idAccion=idAccion)
        self.assertTrue(self.his.existeHistoria(codigo=hCodigo,idProducto=self.prodId))

        #Historia que falla al agregar
        hCodigo = "Soy Historia 2 y pasare tambien"
        hTipo   = "Tipo"
        self.his.insertar(hCodigo,self.prodId,idPapa=None,tipo=hTipo,idAccion=idAccion)
        self.assertTrue(self.his.existeHistoria(codigo=hCodigo,idProducto=self.prodId))


# Casos Esquinas

    def testTodosVacios(self):
        his = clsHistoria(engine,sessionDB)
        pIdProducto = None
        hCodigo = ''
        hTipo   = ''
        self.his.insertar(hCodigo,self.prodId,idPapa=None,tipo=hTipo,idAccion=None)
        self.assertFalse(self.his.existeHistoria(codigo=hCodigo,idProducto=pIdProducto))

    def testProdidVacioyDescrip500(self):
        accion   = clsAccion(engine,sessionDB)
        accion.insertar("testProdidVacioyDescrip500",self.prodId)
        idAccion = accion.obtenerId("testProdidVacioyDescrip500")

        his = clsHistoria(engine,sessionDB)
        pIdProducto = None
        hCodigo     = 'El Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of W'
        hTipo       = "Drai gual. yust anoder bric in de gual"
        self.his.insertar(hCodigo,self.prodId,idPapa=None,tipo=hTipo,idAccion=None)
        self.assertFalse(self.his.existeHistoria(codigo=hCodigo,idProducto=pIdProducto))

    def testCharEnIdyDecripNum(self):
        accion   = clsAccion(engine,sessionDB)
        accion.insertar("testCharEnIdyDecripNum",self.prodId)
        idAccion = accion.obtenerId("testCharEnIdyDecripNum")
        
        his = clsHistoria(engine,sessionDB)
        pIdProducto = 'bruxw'
        hCodigo     = 345346
        hTipo       = 'el sue~o desorienta'
        self.his.insertar(hCodigo,self.prodId,idPapa=None,tipo=hTipo,idAccion=None)
        self.assertFalse(self.his.existeHistoria(codigo=hCodigo,idProducto=pIdProducto))
        
    """
# Casos malicias

    def testcharEnId(self):
        
        his = clsHistoria(engine,sessionDB)
        pIdProducto = 'idpepe'
        pcodigo = 'Historia 2'
        self.his.insertar(pcodigo,pIdProducto)
        self.assertTrue(self.his.existeHistoria(codigo=pcodigo))
    
    def testcodigo501(self):
        
        his = clsHistoria(engine,sessionDB)
        pIdProducto = 3
        pcodigo = 'El Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of WA'
        self.his.insertar(pcodigo,pIdProducto)
        self.assertTrue(self.his.existeHistoria(codigo=pcodigo))
        
# TEST MODIFICAR

# Casos Regulares

    def testModificar1(self):
        
        his = clsHistoria(engine,sessionDB)
        pIdProducto = 1
        pcodigo = 'Historia 1'
        self.his.insertar(pcodigo,pIdProducto)

        pIdProducto2 = 1
        pcodigo2 = 'Historia N1'
        test = his.modificar(pIdProducto2, pcodigo2)
        self.assertTrue(self.his.existeHistoria(codigo=pcodigo2))

# Casos fronteras
    
    def testDescrip500(self):
    
        his = clsHistoria(engine,sessionDB)
        pIdProducto = 2
        pcodigo = 'El Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of W'
        self.his.insertar(pcodigo,pIdProducto)

        pIdProducto2 = 2
        pcodigo2 = 'el Mall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of W'
        test = his.modificar(pIdProducto2, pcodigo2)
        self.assertTrue(self.his.existeHistoria(codigo=pcodigo2))

    def testModifNoValid(self):
        
        his = clsHistoria(engine,sessionDB)
        pIdProducto = 123
        pcodigo = 'Historia 123'
        test = his.modificar(pIdProducto,pcodigo)
        self.assertFalse(self.his.existeHistoria(codigo=pcodigo))

    def testDescripAlMin(self):
        
        his = clsHistoria(engine,sessionDB)
        pIdProducto = 1
        pcodigo = 'Historia 1'
        self.his.insertar(pcodigo,pIdProducto)

        pIdProducto2 = 1
        pcodigo2 = 'A'
        test = his.modificar(pIdProducto2,pcodigo2)
        self.assertTrue(self.his.existeHistoria(codigo=pcodigo2))

# Casos Esquinas

    def testModifTodoNul(self):
        
        his = clsHistoria(engine,sessionDB)
        pIdProducto = 1
        pcodigo = 'Historia 1'
        self.his.insertar(pcodigo,pIdProducto)

        pIdProducto2 = None
        pcodigo2 = ''
        test = his.modificar(pIdProducto2,pcodigo2)
        self.assertFalse(self.his.existeHistoria(codigo=pcodigo2))

    def testModifIdNulyDescripNum(self):
        
        his = clsHistoria(engine,sessionDB)
        pIdProducto = 1
        pcodigo = 'Historia 1'
        self.his.insertar(pcodigo,pIdProducto)

        pIdProducto2 = None
        pcodigo2 = 345
        test = his.modificar(pIdProducto2,pcodigo2)
        self.assertFalse(self.his.existeHistoria(codigo=pcodigo2))

    def testModifIdCharyDecripNum(self):
        
        his = clsHistoria(engine,sessionDB)
        pIdProducto = 1
        pcodigo = 'Historia 1'
        self.his.insertar(pcodigo,pIdProducto)

        pIdProducto2 = 'idpepe'
        pcodigo2 = 4567
        test = his.modificar(pIdProducto2,pcodigo2)
        self.assertFalse(self.his.existeHistoria(codigo=pcodigo2))
    
    def testModifIdCharyDescripNul(self):
       
        his = clsHistoria(engine,sessionDB)
        pIdProducto = 1
        pcodigo = 'Historia 1'
        self.his.insertar(pcodigo,pIdProducto)

        pIdProducto2 = 'idpepe'
        pcodigo2 = ''
        test = his.modificar(pIdProducto2,pcodigo2)
        self.assertFalse(self.his.existeHistoria(codigo=pcodigo2))

# Casos Malicias

    def testModifCharEnId(self):
        
        his = clsHistoria(engine,sessionDB)
        pIdProducto2 = 'hola'
        pcodigo2 = 'Historia p'
        test = self.his.modificar(pIdProducto2,pcodigo2)
        self.assertFalse(self.his.existeHistoria(codigo=pcodigo2))

    def testModifDescrip501(self):
        
        his = clsHistoria(engine,sessionDB)
        pIdProducto2 = 2
        pcodigo2 = 'El Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of Wall of TEXT of WA'
        test = his.modificar(pIdProducto2,pcodigo2)
        self.assertFalse(self.his.existeHistoria(codigo=pcodigo2))

    def testModifDescripVacio(self):
        
        his = clsHistoria(engine,sessionDB)
        pIdProducto2 = 1
        pcodigo2 = ''
        test = self.his.modificar(pIdProducto2,pcodigo2)
        self.assertFalse(self.his.existeHistoria(codigo=pcodigo2))

    def testModifDescripNum(self):
        
        his = clsHistoria(engine,sessionDB)
        pIdProducto2 = 3
        pcodigo2 = 123
        test = self.his.modificar(pIdProducto2,pcodigo2)
        self.assertFalse(self.his.existeHistoria(codigo=pcodigo2))
    
    def testModifIdNulo(self):
        
        his = clsHistoria(engine,sessionDB)
        pIdProducto2 = None
        pcodigo2 = 'Historia nula'
        test = self.his.modificar(pIdProducto2,pcodigo2)
        self.assertFalse(self.his.existeHistoria(codigo=pcodigo2))
    """
    
if __name__ == "__main__":
    unittest.main()