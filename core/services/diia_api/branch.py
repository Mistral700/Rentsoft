import requests

from .diia_variables import (
    DIIA_HOST,
    REQUEST_HEADERS,
)


def get_branch_data():
    return {
        "name": "Відділення 1",
        "email": "rentsoft@gmail.com",
        "region": "Львівська обл.",
        "district": "Сихівський р-н",
        "location": "м. Львів",
        "street": "вул. Цифровізації",
        "house": "25",
        "deliveryTypes": ["api"],
        "offerRequestType": "dynamic",
        "scopes": {
            "diiaId": [
                "hashedFilesSigning"
            ]
        }
    }


def get_branch(session_token: str):
    branch_url = f'https://{DIIA_HOST}/v2/acquirers/branch'
    REQUEST_HEADERS["Authorization"] = f"Bearer {session_token}"

    try:
        branch_data = get_branch_data()

        response = requests.post(branch_url, json=branch_data, headers=REQUEST_HEADERS, timeout=15)
        response.raise_for_status()
        branch_id = response.json()["_id"]
        return branch_id

    except requests.exceptions.HTTPError as err:
        print(
            {
                "HTTP error occurred: ": err.response.text,
                "status_code: ": err.response.status_code,
            }
        )
        return None
