from selenium.webdriver.common.by import By
from pages.base_page import BasePage

username_input = (By.ID, 'crc-ui-input-0')
password_input = (By.ID, 'crc-ui-input-1')

class HomePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://crocobet.com/')

    def type_username(self, text):
        self.type(text, username_input)

    def type_password(self, text):
        self.type(text, password_input)
