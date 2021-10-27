from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from interface import Interface
import time


class Boot:
    def __init__(self):
        self.Interface = Interface.main()

        self.driver = webdriver.Firefox(
            executable_path=r'/usr/local/bin/geckodriver')
        self.condition = 0

    def Controladora(self):
        Interface = self.Interface

        if Interface['Sgo'] == True:
            self.sgo()
            time.sleep(10)
        if Interface['Linkedin'] == True:
            self.linkedin()
            time.sleep(10)
        if Interface['Rocket'] == True:
            self.rocket()
            time.sleep(10)
        if Interface['Email'] == True:
            self.email()
            time.sleep(10)
        if Interface['Youtube'] == True:
            self.youtube()
            time.sleep(10)

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
        #acesso = 'Gabriel.cunha'
        #senha = 'Neto2133@'

        time.sleep(5)
        clickLogin = driver.find_element_by_xpath(
            "//input[@id='username']").send_keys(acesso)

        clickSenha = driver.find_element_by_xpath(
            "//input[@id='password']").send_keys(senha)

        clickButton = driver.find_element_by_xpath(
            "//input[@type='submit']").click()
        return

    def rocket(self):
        driver = self.driver
        #acesso = 'Gabriel.cunha'
        #senha = 'Neto2133@'

        driver.execute_script(
            "window.open('https://chat.basis.com.br', '_blank')")

        driver.switch_to.window(driver.window_handles[-1])

        time.sleep(10)

        clickLogin = driver.find_element_by_xpath(
            "//input[@id='emailOrUsername']").send_keys(acesso)

        clickSenha = driver.find_element_by_xpath(
            "//input[@id='pass']").send_keys(senha)

        clickButton = driver.find_element_by_xpath(
            "//button[@class='rc-button rc-button--primary login']").click()
        return

    def linkedin(self):
        driver = self.driver
        #acesso = 'gabrielcatvalhoneto@gmail.com'
        #senha = 'neto2133'

        driver.execute_script(
            "window.open('https://www.linkedin.com/login/pt?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin', '_blank')"
        )
        driver.switch_to.window(driver.window_handles[-1])

        time.sleep(1)

        clickLogin = driver.find_element_by_xpath(
            "//input[@id='username']").send_keys(acesso)

        clickSenha = driver.find_element_by_xpath(
            "//input[@id='password']").send_keys(senha)

        clickButton = driver.find_element_by_xpath(
            "//button[@class='btn_primary--large from_button--floating']"
        ).click()
        return

    def email(self):
        driver = self.driver
        driver.execute_script(
            "window.open('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin', '_blank')"
        )
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(2)
        #email = 'gabriel.cunha@basis.com.br'
        #senha = 'g25443215'
        time.sleep(5)
        clickinicie = driver.find_element_by_xpath(
            "//input[@id='identifierId']").send_keys(email, Keys.ENTER)
        time.sleep(2)
        clicksenha = driver.find_element_by_xpath(
            "//input[@class='whsOnd zHQkBf']").send_keys(senha, Keys.ENTER)
        time.sleep(2)
        return

    def youtube(self):
        driver = self.driver
        driver.execute_script(
            "window.open('https://www.youtube.com/', '_blank')")
        driver.switch_to.window(driver.window_handles[-1])

        time.sleep(5)
        musica = 'Mc Ryan sp'
        clickmusica = driver.find_element_by_xpath(
            "//input[@id='search']").send_keys(musica)
        time.sleep(2)
        clickPesquisamusica = driver.find_element_by_xpath(
            "//button[@id='search-icon-legacy']").click()
        time.sleep(4)
        clickseleciona = driver.find_element_by_xpath(
            "//yt-formatted-string[@class='style-scope ytd-video-renderer']"
        ).click()
        time.sleep(6)
        clickpular = driver.find_element_by_xpath(
            "//button[@class='ytp-ad-skip-button ytp-button']").click()

        return


iniciaBoot = Boot()
iniciaBoot.Controladora()