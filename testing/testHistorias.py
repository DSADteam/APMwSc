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
    
if __name__ == "__main__":
    unittest.main()