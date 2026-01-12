from selenium.webdriver.common.by import By
from common.base_page import BasePage
import allure
import time

class MessagesPage(BasePage):

    BOOKING_ROWS = (By.CSS_SELECTOR, ".detail")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, ".btn-outline-danger")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("UI: Verify if the specified name exists in the order list: {name}")
    def is_booking_visible(self, name):
        rows = self.driver.find_elements(*self.BOOKING_ROWS)
        if any(name in row.text for row in rows):
            return True
        self.driver.refresh()
        time.sleep(2)
        return False

    @allure.step("UI: Click to log out")
    def logout(self):
        self.click_element(self.LOGOUT_BUTTON)
