import sys
import os
dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../..'))
sys.path.append(dir)

from app.scrum.prod import clsProducto
from base import *
import unittest


class MdlTest(unittest.TestCase):
    """
        Inicializacion de pruebas 
    """
    def setUp(self):
        self.prod=clsProducto(engine,sessionDB)


    def testInsert(self):
        string = 'a' * 500
        self.prod.insertar(string)
        self.assertTrue(self.prod.existeProducto(descript=string),"Error, no se encontro el producto")
        

unittest.main()
