from django.contrib.auth import get_user_model

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from apps.users.models import UserModel as User
from apps.users.serializers import UserSerializer
from apps.advertisements.serializers import AdvertisementSerializer
from apps.users.swagger.decorators import users_swagger
from apps.advertisements.swagger.decorators import adverts_swagger

UserModel: User = get_user_model()


@users_swagger()
class GetAllUsersView(ListAPIView):
    """
    List all users
    (Only for admin)
    """
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


@adverts_swagger()
class UserAdvertisementsListView(RetrieveAPIView):
    """
    List all advertisements by user id
    """
    queryset = UserModel.objects.all()
    serializer_class = AdvertisementSerializer

    def get(self, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user.advertisement_user, many=True)
        return Response(serializer.data)
