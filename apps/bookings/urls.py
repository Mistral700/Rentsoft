from django.urls import path

from apps.bookings.views import BookingListCreateView


urlpatterns = [
    path('', BookingListCreateView.as_view(), name='booking_list_create'),
]
