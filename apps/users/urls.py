from django.urls import path

from apps.users.views import GetAllUsersView, UserAdvertisementsListView


urlpatterns = [
    path('', GetAllUsersView.as_view(), name='retrieve_users'),
    path('/<int:pk>/advertisements', UserAdvertisementsListView.as_view(), name='retrieve_advertisements_by_user'),
]
