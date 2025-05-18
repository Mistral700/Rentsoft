import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

DIIA_HOST = "api2s.diia.gov.ua"
ACQUIRER_TOKEN = "rentsoft_test_token_jcl062"
AUTH_ACQUIRER_TOKEN = "YWNxdWlyZXJfMTExNzpyZW50c29mdF90ZXN0X3Rva2VuX2pjbDA2Mg=="


class DiiaAuthTokenView(APIView):
    def get(self, request):
        url = f'https://{DIIA_HOST}/api/v1/auth/acquirer/{ACQUIRER_TOKEN}'
        headers = {
            "Authorization": f"Basic {AUTH_ACQUIRER_TOKEN}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        try:
            response = requests.get(url, headers=headers, timeout=5)
            response.raise_for_status()

            data = response.json()
            return Response(data)

        except requests.RequestException as e:
            return Response({'error': str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
