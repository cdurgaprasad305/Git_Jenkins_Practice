import requests
import json
import allure
from utils.logger import get_logger

logger = get_logger("api")

class BaseAPI:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.session = requests.Session()
        if headers:
            self.session.headers.update(headers)

    def make_request(self, method, endpoint, **kwargs):
        url = self.base_url + endpoint
        method = method.upper()

        # Log request
        logger.info(f"📤 {method} {url}")
        if "json" in kwargs:
            logger.debug(f"🔸 Request Payload: {json.dumps(kwargs['json'], indent=2)}")
        if "params" in kwargs:
            logger.debug(f"🔹 Query Params: {kwargs['params']}")

        with allure.step(f"{method} {endpoint}"):
            if "json" in kwargs:
                allure.attach(json.dumps(kwargs["json"], indent=2),
                              name="Request JSON", attachment_type=allure.attachment_type.JSON)
            if "params" in kwargs:
                allure.attach(json.dumps(kwargs["params"], indent=2),
                              name="Query Params", attachment_type=allure.attachment_type.JSON)

        # Make request
        response = self.session.request(method, url, **kwargs)

        # Log response
        logger.info(f"📥 Status: {response.status_code}")
        try:
            response_json = response.json()
            logger.debug(f"🧾 Response: {json.dumps(response_json, indent=2)}")
            allure.attach(json.dumps(response_json, indent=2),
                          name="Response JSON", attachment_type=allure.attachment_type.JSON)
        except Exception:
            logger.warning("❗ Non-JSON response")

        return response
