import time
from page_objects.admin_page import AdminPage
from page_objects.messages_page import MessagesPage
from common.logger import log


def test_hybrid_booking_flow(driver, config, api_actions):
    log.info("--- Start executing the hybrid test flow: API creation + UI verification ---")
    # 1. API constructs data
    unique_name = f"Auto{int(time.time())}"
    api_actions.create_custom_booking(unique_name, "Tester")
    log.info(f"Test data preparation complete, unique identifier: {unique_name}")

    # 2. UI Verification steps
    log.info(f"Redirecting to the backend management page: {config['base_url']}")
    driver.get(f"{config['base_url']}/admin")
    admin_page = AdminPage(driver)
    admin_page.login(config['admin_user'], config['admin_pass'])
    time.sleep(2)

    driver.get(f'{config['base_url']}/admin/message')
    time.sleep(2)
    messages_page = MessagesPage(driver)

    result = messages_page.is_booking_visible(unique_name)
    if result:
        log.info("✅ Successfully found the data created by the API on the UI.")
    else:
        log.info("❌ The UI could not find the data created by the API.")



    assert result
    log.info("--- Test case execution completed! ---")
    messages_page.logout()