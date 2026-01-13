import requests
import allure
from datetime import datetime, timedelta
from common.logger import log
import json
import random

class ApiActions:
    def __init__(self, config):
        self.api_url = config['api_url']

    @allure.step("API: Create a custom order")
    def create_custom_booking(self, firstname, lastname):
        url = f"{self.api_url}/booking/"
        log.info(f"🚀Send API request: POST {url}")
        headers = {"Content-Type": "application/json"}

        random_days_in_future = random.randint(100, 500)
        checkin_date = (datetime.now() + timedelta(days=random_days_in_future)).strftime('%Y-%m-%d')
        checkout_date = (datetime.now() + timedelta(days=random_days_in_future + 1)).strftime('%Y-%m-%d')

        payload = {
            "roomid": 1,
            "firstname": firstname,
            "lastname": lastname,
            "depositpaid": False,
            "bookingdates": {
                "checkin": checkin_date,
                "checkout": checkout_date
            },
            "email": f"{firstname}@example.com",
            "phone": "12345678901"
        }

        log.debug(f"Payload: {json.dumps(payload)}")
        response = requests.post(url, json=payload, headers=headers)

        allure.attach(f"Status Code: {response.status_code}", name="API Status")
        allure.attach(response.text, name="API Response")

        log.info(f"API status code: {response.status_code}")
        if response.status_code not in [200, 201]:
            log.error(f"API failure message: {response.text}")
            raise Exception(f"API creation failed！status: {response.status_code}, response: {response.text}")

        return response.json()




