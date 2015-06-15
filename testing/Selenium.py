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
        
        driver.find_element_by_id("fLogin_usuario").clear()
        driver.find_element_by_id("fLogin_usuario").send_keys("robertor")
        time.sleep(0.7)
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("HOLAhol4!")
        time.sleep(0.7)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(0.7)
        driver.find_element_by_link_text("+Producto").click()
        driver.find_element_by_id("fPila_nombre").clear()
        driver.find_element_by_id("fPila_nombre").send_keys("creando")
        time.sleep(0.7)
        driver.find_element_by_id("fPila_descripcion").click()
        driver.find_element_by_id("fPila_descripcion").clear()
        driver.find_element_by_id("fPila_descripcion").send_keys("un")
        time.sleep(0.7)
        Select(driver.find_element_by_id("fPila_escala")).select_by_visible_text("Alta/Media/Baja")
        time.sleep(0.7)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(0.7)
        driver.find_element_by_link_text("Ver").click()
        time.sleep(0.7)
        driver.find_element_by_id("fPila_nombre").clear()
        driver.find_element_by_id("fPila_nombre").send_keys("nuevo producto")
        time.sleep(0.7)
        driver.find_element_by_id("fPila_descripcion").clear()
        driver.find_element_by_id("fPila_descripcion").send_keys("y modificandolo")
        time.sleep(0.7)
        Select(driver.find_element_by_id("fPila_escala")).select_by_visible_text("Entre 1 y 20")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(0.7)
        driver.find_element_by_link_text("Ver").click()
        time.sleep(0.7)
        driver.find_element_by_link_text("+Actor").click()
        time.sleep(0.7)
        driver.find_element_by_id("fActor_nombre").clear()
        driver.find_element_by_id("fActor_nombre").send_keys("creando un actor")
        time.sleep(0.7)
        driver.find_element_by_id("taTextElement").send_keys("descripcion")
        time.sleep(0.7)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(0.7)
        driver.find_element_by_link_text("+Accion").click()
        time.sleep(0.7)
        driver.find_element_by_id("fAccion_descripcion").clear()
        driver.find_element_by_id("fAccion_descripcion").send_keys("creando accion")
        time.sleep(0.7)
        driver.find_element_by_id("taTextElement").send_keys("descripcion de accion")
        time.sleep(0.7)
        x=driver.find_element_by_xpath("//button[@type='submit']")
        x.click()
        time.sleep(0.7)
        driver.find_element_by_link_text("+Objetivo").click()
        time.sleep(0.7)
        driver.find_element_by_id("fObjetivo_descripcion").clear()
        driver.find_element_by_id("fObjetivo_descripcion").send_keys("creando objetivo no transversal")
        time.sleep(0.7)
        Select(driver.find_element_by_id("fObjetivo_transversal")).select_by_visible_text("no transversal")
        time.sleep(0.7)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(0.7)
     
        
        assert "No results found." not in driver.page_source
        
    
   

if __name__ == "__main__":
    unittest.main()