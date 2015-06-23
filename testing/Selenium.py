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
        input()
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("HOLAhol4!")
        input()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        input()
        driver.find_element_by_link_text("+Producto").click()
        driver.find_element_by_id("fPila_nombre").clear()
        driver.find_element_by_id("fPila_nombre").send_keys("creando")
        input()
        driver.find_element_by_id("fPila_descripcion").click()
        driver.find_element_by_id("fPila_descripcion").clear()
        driver.find_element_by_id("fPila_descripcion").send_keys("un")
        input()
        Select(driver.find_element_by_id("fPila_escala")).select_by_visible_text("Alta/Media/Baja")
        input()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        input()
        driver.find_element_by_link_text("Ver").click()
        input()
        driver.find_element_by_id("fPila_nombre").clear()
        driver.find_element_by_id("fPila_nombre").send_keys("nuevo producto")
        input()
        driver.find_element_by_id("fPila_descripcion").clear()
        driver.find_element_by_id("fPila_descripcion").send_keys("y modificandolo")
        input()
        Select(driver.find_element_by_id("fPila_escala")).select_by_visible_text("Entre 1 y 20")
        input()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        input()
        driver.find_element_by_link_text("Ver").click()
        input()
        driver.find_element_by_link_text("+Actor").click()
        input()
        driver.find_element_by_id("fActor_nombre").clear()
        driver.find_element_by_id("fActor_nombre").send_keys("creando un actor")
        input()
        driver.find_element_by_id("taTextElement").send_keys("descripcion")
        input()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        input()
        driver.find_element_by_link_text("+Accion").click()
        input()
        driver.find_element_by_id("fAccion_descripcion").clear()
        driver.find_element_by_id("fAccion_descripcion").send_keys("asdfasdf")
        input()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        input()
        driver.find_element_by_link_text("+Objetivo").click()
        input()
        driver.find_element_by_id("fObjetivo_descripcion").clear()
        driver.find_element_by_id("fObjetivo_descripcion").send_keys("creando objetivo no transversal")
        input()
        Select(driver.find_element_by_id("fObjetivo_transversal")).select_by_visible_text("no transversal")
        input()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        input()
        driver.find_element_by_link_text("Ver").click()
        input()
        driver.find_element_by_id("fActor_nombre").clear()
        driver.find_element_by_id("fActor_nombre").send_keys("fgfg")
        input()
        driver.find_element_by_id("taTextElement").send_keys("descripcion nueva")
        input()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        input()
        driver.find_element_by_xpath("(//a[contains(text(),'Ver')])[4]").click()
        input()
        driver.find_element_by_link_text("-actor").click()
        input()
        driver.find_element_by_xpath("(//a[contains(text(),'Ver')])[4]").click()
        input()
        driver.find_element_by_id("fAccion_descripcion").clear()
        driver.find_element_by_id("fAccion_descripcion").send_keys("ACCCIIIN")
        input()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        input()
        driver.find_element_by_xpath("(//a[contains(text(),'Ver')])[4]").click()
        input()
        driver.find_element_by_link_text("-accion").click()
        input()
        driver.find_element_by_xpath("(//a[contains(text(),'Ver')])[9]").click()
        input()
        driver.find_element_by_id("fObjetivo_descripcion").clear()
        driver.find_element_by_id("fObjetivo_descripcion").send_keys("jojojojo")
        input()
        Select(driver.find_element_by_id("fObjetivo_transversal")).select_by_visible_text("transversal")
        input()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        input()
        driver.find_element_by_xpath("(//a[contains(text(),'Ver')])[9]").click()
        input()
        driver.find_element_by_link_text("-objetivo").click()
        driver.find_element_by_link_text("Historias").click()
        driver.find_element_by_link_text("Detalles").click()
        input()
        
        driver.find_element_by_link_text("+tarea").click()
        input()
        driver.find_element_by_id("fTarea_descripcion").clear()
        driver.find_element_by_id("fTarea_descripcion").send_keys("una descripcion")
        input()
        Select(driver.find_element_by_id("fTarea_categoria")).select_by_visible_text("la mejor categoria")
        input()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        input()
        driver.find_element_by_link_text("detalles").click()
        input()
        driver.find_element_by_id("fTarea_descripcion").clear()
        input()
        driver.find_element_by_id("fTarea_descripcion").send_keys("Ponerle descrip")
        input()
        Select(driver.find_element_by_id("fTarea_categoria")).select_by_visible_text("Juniors")
        input()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        input()
        driver.find_element_by_link_text("Salir").click()
        
        assert "No results found." not in driver.page_source
        
    
   

if __name__ == "__main__":
    unittest.main()