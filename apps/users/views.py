from django.contrib.auth import get_user_model

from rest_framework.generics import(
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    get_object_or_404,
)
from rest_framework.response import Response
from rest_framework import status

from apps.users.models import UserModel as User, ProfileModel
from apps.users.serializers import UserSerializer, ProfileAvatarSerializer
from apps.advertisements.models import AdvertisementModel
from apps.advertisements.serializers import AdvertisementSerializer
from apps.users.swagger.decorators import users_swagger
from apps.advertisements.swagger.decorators import adverts_swagger

from core.permissions import IsSuperUser

UserModel: User = get_user_model()


@users_swagger()
class UserListView(ListAPIView):
    """
    List all users
    (Only for admin)
    """
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)


class UserAddAvatarView(UpdateAPIView):
    """
    Add avatar for user
    """
    serializer_class = ProfileAvatarSerializer
    http_method_names = ('put',)

    def get_object(self):
        return self.request.user.profile

    def perform_update(self, serializer):
        profile: ProfileModel = self.get_object()
        profile.avatar.delete()
        super().perform_update(serializer)


@adverts_swagger()
class UserAdvertisementsListView(RetrieveAPIView):
    """
    List all advertisements by user id
    """
    queryset = UserModel.objects.all()
    serializer_class = AdvertisementSerializer

    def get(self, *args, **kwargs):
        user: UserModel = self.get_object()
        serializer = self.get_serializer(user.advertisement_user, many=True)
        return Response(serializer.data)


class UserAdvertisementsRetrieveView(RetrieveAPIView):
    """
    Retrieve user advertisement by id
    """
    queryset = UserModel.objects.all()
    serializer_class = AdvertisementSerializer

    def get(self, *args, **kwargs):
        user: UserModel = self.get_object()
        advert_id = kwargs['advert_id']
        advert = get_object_or_404(
            AdvertisementModel,
            pk=advert_id,
            user=user
        )

        serializer = self.get_serializer(advert)
        return Response(serializer.data, status=status.HTTP_200_OK)
