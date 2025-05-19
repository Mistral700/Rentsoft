import requests

from .diia_variables import (
    ACQUIRER_TOKEN,
    AUTH_ACQUIRER_TOKEN,
    DIIA_HOST,
    REQUEST_HEADERS,
)


def get_session_token():
    session_token_url = f'https://{DIIA_HOST}/v1/auth/acquirer/{ACQUIRER_TOKEN}'
    REQUEST_HEADERS["Authorization"] = f"Basic {AUTH_ACQUIRER_TOKEN}"

    try:
        response = requests.get(session_token_url, headers=REQUEST_HEADERS, timeout=15)
        response.raise_for_status()
        session_token = response.json()["token"]
        return session_token

    except requests.RequestException as err:
        print(
            {
                "HTTP error occurred: ": err.response.text,
                "status_code: ": err.response.status_code,
            }
        )
        return None
