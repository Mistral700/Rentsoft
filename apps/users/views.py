from django.contrib.auth import get_user_model

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from apps.users.models import UserModel as User
from apps.users.serializers import UserSerializer
from apps.advertisements.serializers import AdvertisementSerializer

UserModel: User = get_user_model()


class GetAllUsersView(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


class UserAdvertisementsListView(ListAPIView):
    queryset = UserModel.objects.all()

    def get(self, *args, **kwargs):
        user = self.get_object()
        serializer = AdvertisementSerializer(user.advertisement_user, many=True)
        return Response(serializer.data)
