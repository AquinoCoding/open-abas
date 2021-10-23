from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium.webdriver.common.keys import Keys


class Boot:
    def __init__(self):
        self.driver = webdriver.Firefox(
            executable_path=GeckoDriverManager().install())
        self.condition = 10

    def acesso(self, condition):

        driver = self.driver
        condition = self.condition

        if condition == 1:
            acesso = 'Gabriel.cunha'
            return acesso
        if condition == 2:
            senha = 'Neto2133@'
            return senha

    def sgo(self):
        driver = self.driver
        driver.get('https://sgo.basis.com.br/')

        acesso = 'Gabriel.cunha'
        senha = 'Neto2133@'

        time.sleep(5)
        clickLogin = driver.find_element_by_xpath(
            "//input[@id='username']").send_keys(acesso)

        clickSenha = driver.find_element_by_xpath(
            "//input[@id='password']").send_keys(senha)

        clickButton = driver.find_element_by_xpath(
            "//input[@type='submit']").click()
        time.sleep(1)
        self.rocket()

    def rocket(self):
        driver = self.driver
        acesso = 'Gabriel.cunha'
        senha = 'Neto2133@'

        body = driver.find_element_by_tag_name("body")
        body.send_keys(Keys.CONTROL + 't')

        time.sleep(7)

        driver.get("https://chat.basis.com.br")
        #driver.execute_script("window.open('https://chat.basis.com.br', '_blank')")

        time.sleep(30)
        clickLogin = driver.find_element_by_xpath(
            "//input[@id='emailOrUsername']").send_keys(acesso)

        clickSenha = driver.find_element_by_xpath(
            "//input[@id='pass']").send_keys(senha)

        clickButton = driver.find_element_by_xpath(
            "//button[@class='rc-button rc-button--primary login']").click()


iniciaBoot = Boot()
iniciaBoot.sgo()