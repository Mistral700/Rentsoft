from django.urls import path

from apps.bookings.views import BookingListCreateView, ClientsBaseForAdvertsList


urlpatterns = [
    path('', BookingListCreateView.as_view(), name='booking_list_create'),
    path('/clients', ClientsBaseForAdvertsList.as_view(), name='clients_base_list'),
]
