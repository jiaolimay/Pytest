from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"element {locator} isn't found")

    def click_element(self, locator):
        self.find_element(locator).click()

    def input_text(self, locator, text):
        ele = (self.find_element(locator))
        ele.clear()
        ele.send_keys(text)


