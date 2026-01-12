import requests
import allure
import json
from datetime import datetime, timedelta
import random

class ApiActions:
    def __init__(self, config):
        self.api_url = config['api_url']

    @allure.step("API: Create a custom order")
    def create_custom_booking(self, firstname, lastname):
        url = f"{self.api_url}/booking/"
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

        response = requests.post(url, json=payload)

        allure.attach(f"Status Code: {response.status_code}", name="API Status")
        allure.attach(response.text, name="API Response")

        if response.status_code not in [200, 201]:
            raise Exception(f"API creation failed！status: {response.status_code}, response: {response.text}")

        return response.json()




