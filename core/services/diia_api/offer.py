import requests

from .diia_variables import (
    DIIA_HOST,
    REQUEST_HEADERS,
)


def get_offer_data():
    return {
        "name": "Оренда авто",
        "scopes": {
            "diiaId": [
                "hashedFilesSigning"
            ]
        }
    }


def get_offer(session_token: str, branch_id: str):
    offer_url = f'https://{DIIA_HOST}/v1/acquirers/branch/{branch_id}/offer'
    REQUEST_HEADERS["Authorization"] = f"Bearer {session_token}"

    try:
        offer_data = get_offer_data()

        response = requests.post(offer_url, json=offer_data, headers=REQUEST_HEADERS, timeout=15)
        response.raise_for_status()
        offer_id = response.json()["_id"]
        return offer_id

    except requests.exceptions.HTTPError as err:
        print(
            {
                "HTTP error occurred: ": err.response.text,
                "status_code: ": err.response.status_code,
            }
        )
        return None
