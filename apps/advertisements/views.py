from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    GenericAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from apps.advertisements.models import (
    AdvertisementModel,
    AdvertisementPhotoModel,
    CategoryModel,
    TransmissionModel,
    FuelTypeModel,
    StatusModel,
)
from apps.advertisements.serializers import (
    AdvertisementSerializer,
    AdvertPhotoSerializer,
    CategorySerializer,
    TransmissionSerializer,
    FuelTypeSerializer,
    StatusSerializer,
)
from apps.advertisements.swagger.decorators import adverts_partial_update_swagger, advert_swagger

from core.permissions import IsSuperUserOrReadOnly


class CategoryListCreateView(ListCreateAPIView):
    """
    get:
        Get categories list
    post:
        Create category
        (Only for admin)
    """
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsSuperUserOrReadOnly,)


class TransmissionListCreateView(ListCreateAPIView):
    """
    get:
        Get transmissions list
    post:
        Create transmission
        (Only for admin)
    """
    queryset = TransmissionModel.objects.all()
    serializer_class = TransmissionSerializer
    permission_classes = (IsSuperUserOrReadOnly,)


class FuelTypeListCreateView(ListCreateAPIView):
    """
    get:
        Get fuel types list
    post:
        Create fuel type
        (Only for admin)
    """
    queryset = FuelTypeModel.objects.all()
    serializer_class = FuelTypeSerializer
    permission_classes = (IsSuperUserOrReadOnly,)


class StatusListCreateView(ListCreateAPIView):
    """
    get:
        Get statuses list
    post:
        Create status
        (Only for admin)
    """
    queryset = StatusModel.objects.all()
    serializer_class = StatusSerializer
    permission_classes = (IsSuperUserOrReadOnly,)


class MineAdvertisementsListCreateView(ListCreateAPIView):
    """
    get:
        Get all mine advertisements
        (Only for business)
    post:
        Create advertisement
        (Only for business)
    """
    serializer_class = AdvertisementSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        return AdvertisementModel.objects.select_related(
            'user',
            'transmission',
            'category',
            'status',
        ).prefetch_related('fuel_type').filter(user_id=self.request.user.id)

    def perform_create(self, serializer):
        status_available = StatusModel.objects.get(name="Available")
        user = self.request.user
        serializer.save(user=user, status=status_available)


@adverts_partial_update_swagger()
class MineAdvertisementsGetUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """
    get:
        Get specific advert by id
        (Only for business)
    put:
        Update specific advert by id completely
        (Only for business)
    patch:
        Update specific advert by id partly
        (Only for business)
    delete:
        Delete specific advert by id
        (Only for business)
    """
    serializer_class = AdvertisementSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        return AdvertisementModel.objects.select_related(
            'transmission',
            'category',
            'user',
            'status'
        ).prefetch_related('fuel_type').filter(user_id=self.request.user.id)


@advert_swagger()
class AdvertAddPhotoView(GenericAPIView):
    """
    Add photo to specific advert
    """
    serializer_class = AdvertPhotoSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        return AdvertisementModel.objects.select_related(
            'transmission',
            'category',
            'user',
            'status'
        ).prefetch_related('fuel_type').filter(user_id=self.request.user.id)

    def post(self, *args, **kwargs):
        files = self.request.FILES
        advert = self.get_object()
        for key in files:
            serializer = self.get_serializer(data={'photo': files[key]})
            serializer.is_valid(raise_exception=True)
            serializer.save(advert=advert)

        serializer = AdvertisementSerializer(advert)
        return Response(serializer.data, status.HTTP_201_CREATED)


class AdvertRemovePhotoView(DestroyAPIView):
    """
    Delete photo from advert by photo id
    """
    def get_queryset(self):
        return AdvertisementPhotoModel.objects.select_related(
            'advert',
            'advert__transmission',
            'advert__category',
            'advert__user',
            'advert__status',
        ).prefetch_related('advert__fuel_type').filter(advert__user_id=self.request.user.id)

    serializer_class = AdvertisementSerializer
    permission_classes = (IsAdminUser,)

    def perform_destroy(self, instance):
        photo: AdvertisementPhotoModel = self.get_object()
        instance.photo.delete()
        photo.delete()
