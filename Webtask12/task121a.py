import os
from time import sleep
from urllib.robotparser import RobotFileParser

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC


class Task:
    def __init__(self, url):
        self.url = url

        # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.action = ActionChains(self.driver)

    def booting_function(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            return True
        except:
            print("ERROR : Unable to run the code !")
            return False

    def shutdown(self):
        self.driver.quit()

    def document(self):
        doc_locator = "//a[text()='Documents']"
        closepopup_locator = "/html/body/div[1]/div[3]/div/div[2]/button"
        monthlyprogress_locator = "/html/body/nav/div/div/div/ul/li[7]/ul/li[2]/a"

        downloadprogress_locator = "/html/body/section[3]/div/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[3]/a"
        self.driver.find_element(by=By.XPATH, value=closepopup_locator).click()
        try:
            self.driver.find_element(by=By.XPATH, value=doc_locator).click()
            sleep(2)
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, downloadprogress_locator)))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

            element.click()

            sleep(10)
            self.driver.switch_to.alert.accept()
            print("Report Downloaded")

        except NoSuchElementException as e:
            print("ERROR : Something went wrong with Locators !", e)

    def media(self):
        media_locator = "//a[text()='Media']"
        SwachhataHiSevaimage = "//*[@id='fontSize']/div/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/table/tbody/tr[1]/td[1]/div[2]/span/a"
        lemimage_locator = "/html/body/section[3]/div/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/table/tbody/tr[1]/td[2]/div[2]/span/a"
        ewg4_locator = "/html/body/section[3]/div/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/table/tbody/tr[1]/td[3]/div[2]/span/a"
        ewg3_locator = "/html/body/section[3]/div/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/table/tbody/tr[2]/td[1]/div[2]/span/a"
        ewg2_locator = "/html/body/section[3]/div/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/div[2]/span/a"
        self.driver.find_element(by=By.XPATH, value=media_locator).click()
        self.driver.find_element(by=By.XPATH, value=SwachhataHiSevaimage).click()
        path = './projects'

        # check whether directory already exists
        if not os.path.exists(path):
            os.mkdir(path)
            print("Folder %s created!" % path)
        else:
            print("Folder %s already exists" % path)

        self.driver.save_screenshot("swachimage.png")
        self.driver.back()
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=lemimage_locator).click()
        self.driver.save_screenshot("lemimage.png")
        self.driver.back()
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=ewg4_locator).click()
        self.driver.save_screenshot("ewg2.png")
        self.driver.back()
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=ewg3_locator).click()
        self.driver.save_screenshot("ewg3.png")
        self.driver.back()
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=ewg4_locator).click()
        self.driver.save_screenshot("ewd4.png")


url = "https://labour.gov.in/"

execute = Task(url)
execute.booting_function()
execute.document()

execute.media()

execute.shutdown()
