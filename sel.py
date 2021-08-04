from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
import time

class ws:
    def __init__(self, driver):
        self.__driver = webdriver.Firefox(executable_path=driver)
        self.__timeout = 30
 
    def navegaPara(self, url):
        try:
            self.__driver.get(url)
            time.sleep(2)
        except:
            print('tentei abrir a url e falhei ', url)

    def procura_xpath_clica(self, xpath):
        try:
            elemento = WebDriverWait(self.__driver, self.__timeout).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            elemento.click()
        except:
            print('tentei clicar e falhei pelo xpath ', xpath)

    def procura_xpath_escreve(self, xpath, texto):
        try:
            elemento = WebDriverWait(self.__driver, self.__timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            elemento.clear()
            elemento.send_keys(texto)
        except:
            print('tentei inserir o texto e falhei pelo xpath ', xpath, ' ', texto)

    def fechaGuia(self):
            self.__driver.close()