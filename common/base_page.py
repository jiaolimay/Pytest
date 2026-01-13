from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from common.logger import log

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
        log.info(f"Clicking the element: {locator}")
        self.find_element(locator).click()

    def input_text(self, locator, text):
        log.info(f"Inputting content: {text} into element: {locator}")
        ele = (self.find_element(locator))
        ele.clear()
        ele.send_keys(text)

    def get_text(self, locator):
        log.info(f"Getting content from element: {locator}")
        ele = (self.find_element(locator))
        return ele.text

    def wait_for_page_load(self):
        log.info(f"Waiting for the page to finish loading")
        self.wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )


