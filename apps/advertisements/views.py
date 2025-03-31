from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser

from apps.advertisements.models import (
    AdvertisementModel,
    CategoryModel,
    TransmissionModel,
    FuelTypeModel,
    StatusModel,
)
from apps.advertisements.serializers import (
    AdvertisementSerializer,
    CategorySerializer,
    TransmissionSerializer,
    FuelTypeSerializer,
    StatusSerializer,
)
from apps.advertisements.swagger.decorators import adverts_partial_update_swagger


class CategoryListCreateView(ListCreateAPIView):
    """
    get:
        Get categories list
        (Only for admin)
    post:
        Create category
        (Only for admin)
    """
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUser,)


class TransmissionListCreateView(ListCreateAPIView):
    """
    get:
        Get transmissions list
        (Only for admin)
    post:
        Create transmission
        (Only for admin)
    """
    queryset = TransmissionModel.objects.all()
    serializer_class = TransmissionSerializer
    permission_classes = (IsAdminUser,)


class FuelTypeListCreateView(ListCreateAPIView):
    """
    get:
        Get fuel types list
        (Only for admin)
    post:
        Create fuel type
        (Only for admin)
    """
    queryset = FuelTypeModel.objects.all()
    serializer_class = FuelTypeSerializer
    permission_classes = (IsAdminUser,)


class StatusListCreateView(ListCreateAPIView):
    """
    get:
        Get statuses list
        (Only for admin)
    post:
        Create status
        (Only for admin)
    """
    queryset = StatusModel.objects.all()
    serializer_class = StatusSerializer
    permission_classes = (IsAdminUser,)


class AdvertisementsListView(ListAPIView):
    """
    Get all advertisements
    """
    queryset = AdvertisementModel.objects.select_related(
        'user',
        'transmission',
        'category',
        'status'
    ).prefetch_related('fuel_type').all()
    serializer_class = AdvertisementSerializer


class MineAdvertisementListCreateView(ListCreateAPIView):
    """
    get:
        Get advertisements of registered user(mine)
    post:
        Create advertisement
    """
    serializer_class = AdvertisementSerializer

    def get_queryset(self):
        return AdvertisementModel.objects.select_related(
            'transmission',
            'category',
            'user',
            'status'
        ).prefetch_related('fuel_type').filter(user=self.request.user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


@adverts_partial_update_swagger()
class MineAdvertisementGetUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """
    get:
        Get specific advert by id
    put:
        Update specific advert by id completely
    patch:
        Update specific advert by id partly
    delete:
        Delete specific advert by id
    """
    serializer_class = AdvertisementSerializer

    def get_queryset(self):
        return AdvertisementModel.objects.select_related(
            'transmission',
            'category',
            'user',
            'status'
        ).prefetch_related('fuel_type').filter(user__pk=self.request.user.id)
