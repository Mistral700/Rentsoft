from django.urls import path

from apps.users.views import (
    UserListView,
    UserAdvertisementsListView,
    UserAddAvatarView,
    UserAdvertisementsRetrieveView,
)

urlpatterns = [
    path('', UserListView.as_view(), name='users_list'),
    path('/avatars', UserAddAvatarView.as_view(), name='add_avatar'),
    path('/<int:pk>/advertisements', UserAdvertisementsListView.as_view(), name='list_advertisements_by_user'),
    path('/<int:pk>/advertisements/<int:advert_id>', UserAdvertisementsRetrieveView.as_view(),
         name='retrieve_user_advertisement'),
]
