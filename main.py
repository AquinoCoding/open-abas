from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from interface import 
import time


class OpenAbasBoot:
    def __init__(self):
        self.driver = webdriver.Firefox(
            executable_path=r'/usr/local/bin/geckodriver')
        self.condition = 0

    def Acesso(self, condition):

        driver = self.driver
        condition = self.condition

        if condition == 1:
            acesso = '.'
            return acesso
        elif condition == 2:
            senha = '@'
            return senha

        elif condition == 3:
            acesso = '.'
            return acesso
        elif condition == 4:
            senha = '@'
            return senha

    def Sgo(self):

        driver = self.driver

        driver.get('https://sgo.basis.com.br/')

        login = '.'
        password = '@'

        time.sleep(5)

        clickLogin = driver.find_element_by_xpath(
            "//input[@id='username']").send_keys(login)
        clickSenha = driver.find_element_by_xpath(
            "//input[@id='password']").send_keys(password)
        clickButton = driver.find_element_by_xpath(
            "//input[@type='submit']").click()

        self.rocket()

    def rocket(self):

        driver = self.driver
        acesso = '.'
        senha = '@'

        driver.execute_script(
            "window.open('https://chat.basis.com.br', '_blank')")

        driver.switch_to_window(driver.window_handles[1])

        time.sleep(7)

        clickLogin = driver.find_element_by_xpath(
            "//input[@id='emailOrUsername']").send_keys(acesso)

        clickSenha = driver.find_element_by_xpath(
            "//input[@id='pass']").send_keys(senha)

        clickButton = driver.find_element_by_xpath(
            "//button[@class='rc-button rc-button--primary login']").click()


Inicie_Boot = OpenAbasBoot()
Inicie_Boot.Sgo()
