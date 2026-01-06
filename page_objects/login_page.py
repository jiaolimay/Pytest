from selenium.webdriver.common.by import By
from common.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, ".error-message-container>h3")


    def login(self, username, password):
        self.input_text(self.USERNAME_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)

