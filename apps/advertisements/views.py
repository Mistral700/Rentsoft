from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser

from apps.advertisements.models import (
    AdvertisementModel,
    CategoryModel,
    TransmissionModel,
    FuelTypeModel, StatusModel
)
from apps.advertisements.serializers import (
    AdvertisementSerializer,
    CategorySerializer,
    TransmissionSerializer,
    FuelTypeSerializer, StatusSerializer
)


class CategoryListCreateView(ListCreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUser,)


class TransmissionListCreateView(ListCreateAPIView):
    queryset = TransmissionModel.objects.all()
    serializer_class = TransmissionSerializer
    permission_classes = (IsAdminUser,)


class FuelTypeListCreateView(ListCreateAPIView):
    queryset = FuelTypeModel.objects.all()
    serializer_class = FuelTypeSerializer
    permission_classes = (IsAdminUser,)


class StatusListCreateView(ListCreateAPIView):
    queryset = StatusModel.objects.all()
    serializer_class = StatusSerializer
    permission_classes = (IsAdminUser,)


class AdvertisementsListView(ListAPIView):
    queryset = AdvertisementModel.objects.select_related(
        'user',
        'transmission',
        'category',
        'status'
    ).prefetch_related('fuel_type').all()
    serializer_class = AdvertisementSerializer


class MineAdvertisementListCreateView(ListCreateAPIView):
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


class MineAdvertisementGetUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = AdvertisementSerializer

    def get_queryset(self):
        return AdvertisementModel.objects.select_related(
            'transmission',
            'category',
            'user',
            'status'
        ).prefetch_related('fuel_type').filter(user=self.request.user)
