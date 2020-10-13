from typing import Dict

import requests
from requests import Response

BASE_URL = 'https://aw3.automationintesting.online'
MESSAGE_ENDPOINT = f'{BASE_URL}/message'


def create_message(payload: Dict) -> Response:
    response = requests.post(MESSAGE_ENDPOINT, json=payload)
    if not response.ok:
        raise ConnectionError(f'Unable to create message: {response.content}')
    return response
