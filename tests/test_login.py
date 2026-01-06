import pytest
from page_objects.login_page import LoginPage

def test_valid_login(driver, config):
    driver.get(config['base_url'])

    login_page = LoginPage(driver)
    login_page.login(config['standard_user'], config['pw'])

    assert "inventory.html" in driver.current_url

def test_locked_user(driver, config):
    driver.get(config['base_url'])

    login_page = LoginPage(driver)
    login_page.login(config['locked_out_user'], config['pw'])
    error_text = login_page.get_text(login_page.ERROR_MSG)

    assert "this user has been locked out" in error_text
