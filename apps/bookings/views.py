from django.contrib.auth import get_user_model
from django.db.transaction import atomic
from django.utils.timezone import now

from rest_framework.generics import(
    ListCreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)

from apps.advertisements.models import StatusModel
from apps.bookings.models import BookingModel
from apps.bookings.serializers import BookingSerializer, ClientBookingSerializer

UserModel = get_user_model()


class BookingListCreateView(ListCreateAPIView):
    """
    get:
        Return a list of bookings made by the authenticated user.
    post:
        Create a new booking for the authenticated user.
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

    @atomic
    def perform_create(self, serializer):
        user = self.request.user
        booking = serializer.save(user=user)

        # Update advert status after booking creation
        advert = booking.advert
        booked_status = StatusModel.get_booked_status()
        advert.status = booked_status
        advert.save(update_fields=["status"])


class BookingRetrieveUpdateRejectView(RetrieveUpdateDestroyAPIView):
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

    @atomic
    def perform_destroy(self, instance):
        instance.date_to = now()
        instance.is_active = False
        instance.save(update_fields=["date_to", "is_active"])

        # Update advert status after booking rejection
        available_status = StatusModel.get_available_status()
        instance.advert.status = available_status
        instance.advert.save(update_fields=["status"])


class ClientsBaseForAdvertsList(ListAPIView):
    """
    List a customer base
    """
    serializer_class = ClientBookingSerializer

    def get_queryset(self):
        return UserModel.objects.filter(
            booking_user__advert__user=self.request.user
        ).distinct().select_related(
            'profile',
        ).prefetch_related(
            'booking_user__advert__user',
            'booking_user__advert__fuel_type',
        )
