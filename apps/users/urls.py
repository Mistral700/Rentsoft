from django.urls import path

from apps.users.views import UserListView, UserAdvertisementsListView, UserAddAvatarView


urlpatterns = [
    path('', UserListView.as_view(), name='users_list'),
    path('/avatars', UserAddAvatarView.as_view(), name='add_avatar'),
    path('/<int:pk>/advertisements', UserAdvertisementsListView.as_view(), name='retrieve_advertisements_by_user'),
]
