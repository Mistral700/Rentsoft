from django.urls import path

from apps.advertisements.views import (
    AdvertAddPhotoView,
    AdvertRemovePhotoView,
    MineAdvertisementsGetUpdateDestroy,
    MineAdvertisementsListCreateView,
    CategoryListCreateView,
    TransmissionListCreateView,
    FuelTypeListCreateView,
    StatusListCreateView,
)


urlpatterns = [
    path('', MineAdvertisementsListCreateView.as_view(), name='list_create_mine_advertisements'),
    path('/<int:pk>', MineAdvertisementsGetUpdateDestroy.as_view(), name='get_update_destroy_advertisement'),

    path('/<int:pk>/photo', AdvertAddPhotoView.as_view(), name='add_advert_photo'),
    path('/photo/<int:pk>', AdvertRemovePhotoView.as_view(), name='remove_advert_photo'),

    path('/categories', CategoryListCreateView.as_view(), name='list_create_categories'),
    path('/transmissions', TransmissionListCreateView.as_view(), name='list_create_transmissions'),
    path('/fuel_types', FuelTypeListCreateView.as_view(), name='list_create_fuel_types'),
    path('/statuses', StatusListCreateView.as_view(), name='list_create_statuses'),
]
