from rest_framework.generics import ListCreateAPIView, ListAPIView

from apps.bookings.models import BookingModel
from apps.bookings.serializers import BookingSerializer


class BookingListCreateView(ListCreateAPIView):
    serializer_class = BookingSerializer

    def get_queryset(self):
        return BookingModel.objects.select_related(
            'advert',
            'advert__transmission',
            'advert__category',
            'advert__user',
            'advert__status',
            'user',
        ).prefetch_related('advert__fuel_type').filter(user=self.request.user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class ClientsBaseForAdvertsList(ListAPIView):
    def get_queryset(self):
        return BookingModel.objects.select_related(
            'advert',
            'advert__transmission',
            'advert__category',
            'advert__user',
            'advert__status',
            'user',
        ).prefetch_related('advert__fuel_type').filter(advert__user=self.request.user)

    serializer_class = BookingSerializer
