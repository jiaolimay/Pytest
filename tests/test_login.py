import pytest
from page_objects.login_page import LoginPage

def test_valid_login(driver, config):
    driver.get(config['base_url'])

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    assert "inventory.html" in driver.current_url
