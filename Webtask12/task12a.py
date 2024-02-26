from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Task:
    def __init__(self, url):
        self.url = url

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

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

    def openfaqandpartnerpage(self):
        faq_locator = "/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[4]/a"
        partner_locator = "/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a"
        self.driver.find_element(by=By.XPATH, value=faq_locator).click()
        self.driver.find_element(by=By.XPATH, value=partner_locator).click()
        # Fetch and display the opened windows
        all_windows = self.driver.window_handles
        print("Opened Windows:", all_windows)

        # Switch to the first new window (FAQ)
        self.driver.switch_to.window(all_windows[1])
        sleep(2)  # Adding a delay to visually observe the window switch

        # Switch to the second new window (Partners)
        self.driver.switch_to.window(all_windows[2])
        sleep(2)  # Adding a delay to visually observe the window switch

        # Switch back to the original window (Home page)
        self.driver.switch_to.window(all_windows[0])


url = "https://www.cowin.gov.in/"

execute = Task(url)
execute.booting_function()
execute.openfaqandpartnerpage()
execute.shutdown()