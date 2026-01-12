from selenium.webdriver.common.by import By
from common.base_page import BasePage
import allure

class AdminPage(BasePage):
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "doLogin")

    BOOKING_ROWS = (By.CSS_SELECTOR, ".detail.row")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("UI: Longin as admin ")
    def login(self, username, password):
        self.input_text(self.USERNAME_FIELD, username)
        self.input_text(self.PASSWORD_FIELD, password)
        self.click_element(self.LOGIN_BUTTON)
        return self



