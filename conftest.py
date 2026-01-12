import pytest
import yaml
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from common.api_client import ApiActions

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="Environment: dev or qa")

@pytest.fixture(scope="session")
def config(request):
    env = request.config.getoption("--env")
    with open(f"config/{env}_config.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="function")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    '''via yield to pass the driver to the test functions'''
    yield driver

    driver.quit()

@pytest.fixture(scope="session")
def api_actions(config):
    return ApiActions(config)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # 1. This is the preparation phase before test case execution.

    outcome = yield # 2. Here we will perform the actual tests.

    # 3. Here are the results we get after the test cases are executed.
    report = outcome.get_result()

    if report.failed:
        # If the test case fails to execute, write your logic here,

        # Check if the driver is in the fixture and if it has been instantiated.
        driver = item.funcargs.get("driver")
        if driver:
            try:
                allure.attach(
                    driver.get_screenshot_as_png(), name=f"Screenshot of failure_{item.name}",
                              attachment_type=allure.attachment_type.PNG)
            except Exception as e:
                print(f"Screenshot failed: {e}")

        browser_logs = driver.get_log('browser')
        allure.attach(str(browser_logs), name="Console Logs", attachment_type=allure.attachment_type.TEXT)






