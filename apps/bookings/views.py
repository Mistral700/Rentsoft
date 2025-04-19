from django.contrib.auth import get_user_model
from rest_framework.generics import ListCreateAPIView, ListAPIView

from apps.bookings.models import BookingModel
from apps.bookings.serializers import BookingSerializer, ClientBookingSerializer

UserModel = get_user_model()


class BookingListCreateView(ListCreateAPIView):
    """
    get:
        List all bookings of registered user
    post:
        Create booking
    """
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
    """
    List a customer base
    """
    serializer_class = ClientBookingSerializer

    def get_queryset(self):
        return UserModel.objects.filter(
            booking_user__advert__user=self.request.user
        ).distinct()
