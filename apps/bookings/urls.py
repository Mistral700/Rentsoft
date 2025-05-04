from django.urls import path

from apps.bookings.views import (
    BookingListCreateView,
    ClientsBaseForAdvertsList,
    BookingRetrieveUpdateRejectView,
)


urlpatterns = [
    path('', BookingListCreateView.as_view(), name='booking_list_create'),
    path('/<int:pk>', BookingRetrieveUpdateRejectView.as_view(), name='booking_retrieve_update_reject'),
    path('/clients', ClientsBaseForAdvertsList.as_view(), name='clients_base_list'),
]
