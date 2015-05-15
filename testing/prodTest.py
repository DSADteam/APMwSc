import sys
import os
dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../..'))
sys.path.append(dir)

from app.scrum.prod import clsProducto
import base
import unittest

class MdlTest(unittest.TestCase):
    def setUp(self):
        self.prod=clsProducto(engine,sessionDB)