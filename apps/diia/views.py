from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.services.diia_api.session_token import get_session_token
from core.services.diia_api.branch import get_branch
from core.services.diia_api.offer import get_offer


class DiiaAuthTokenView(APIView):
    def get(self, request):
        session_token = get_session_token()
        branch_id = get_branch(session_token=session_token) if session_token else None
        offer_id = get_offer(session_token=session_token, branch_id=branch_id) if branch_id else None

        return Response({
            "token": session_token,
            "branch": branch_id,
            "offer_id": offer_id,
        }, status=status.HTTP_200_OK)
