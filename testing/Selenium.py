# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Seltest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:5000/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_sel(self):
        driver = self.driver
        driver.get(self.base_url)
        
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("HOLAhol4!")
        driver.find_element_by_id("fLogin_usuario").clear()
        driver.find_element_by_id("fLogin_usuario").send_keys("robertor")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("Nuevo").click()
        driver.find_element_by_id("fPila_nombre").clear()
        driver.find_element_by_id("fPila_nombre").send_keys("csv")
        driver.find_element_by_id("fPila_descripcion").clear()
        driver.find_element_by_id("fPila_descripcion").send_keys("dfgdfg")
        Select(driver.find_element_by_id("fPila_escala")).select_by_visible_text("Alta/Media/Baja")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        
        driver.find_element_by_link_text("Ver").click()
        driver.find_element_by_id("fPila_nombre").clear()
        driver.find_element_by_id("fPila_nombre").send_keys("dfdfdfdf")
        driver.find_element_by_id("fPila_nombre").clear()
        driver.find_element_by_id("fPila_nombre").send_keys("tiene que funcionar")
        driver.find_element_by_id("fPila_descripcion").clear()
        driver.find_element_by_id("fPila_descripcion").send_keys("una descripcion nn")
        Select(driver.find_element_by_id("fPila_escala")).select_by_visible_text("Alta/Media/Baja")
        driver.find_element_by_xpath("//button[@type='submit']").click()
     
        
        assert "No results found." not in driver.page_source
        
    
   

if __name__ == "__main__":
    unittest.main()