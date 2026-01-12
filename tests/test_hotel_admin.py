import time
from page_objects.admin_page import AdminPage
from page_objects.messages_page import MessagesPage


def test_hybrid_booking_flow(driver, config, api_actions):
    # 1. API constructs data
    unique_name = f"Auto{int(time.time())}"
    api_actions.create_custom_booking(unique_name, "Tester")

    # 2. UI Verification steps
    driver.get(f"{config['base_url']}/admin")
    admin_page = AdminPage(driver)
    admin_page.login(config['admin_user'], config['admin_pass'])
    time.sleep(2)

    driver.get(f'{config['base_url']}/admin/message')
    time.sleep(2)
    messages_page = MessagesPage(driver)

    assert messages_page.is_booking_visible(unique_name)
    messages_page.logout()