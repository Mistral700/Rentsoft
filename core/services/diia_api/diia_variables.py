import os


DIIA_HOST = os.environ.get('DIIA_HOST')
ACQUIRER_TOKEN = os.environ.get('ACQUIRER_TOKEN')
AUTH_ACQUIRER_TOKEN = os.environ.get('AUTH_ACQUIRER_TOKEN')

REQUEST_HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}
