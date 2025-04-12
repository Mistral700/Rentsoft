from django.urls import path

from apps.advertisements.views import (
    AdvertisementsListCreateView,
    AdvertAddPhotoView,
    AdvertRemovePhotoView,
    AdvertisementGetUpdateDestroy,
    MineAdvertisementListView,
    CategoryListCreateView,
    TransmissionListCreateView,
    FuelTypeListCreateView,
    StatusListCreateView,
)


urlpatterns = [
    path('', AdvertisementsListCreateView.as_view(), name='list_create_advertisements'),
    path('/<int:pk>', AdvertisementGetUpdateDestroy.as_view(), name='get_update_destroy_advertisement'),
    path('/mine', MineAdvertisementListView.as_view(), name='list_mine_advertisements'),

    path('/<int:pk>/photo', AdvertAddPhotoView.as_view(), name='add_advert_photo'),
    path('/photo/<int:pk>', AdvertRemovePhotoView.as_view(), name='remove_advert_photo'),

    path('/categories', CategoryListCreateView.as_view(), name='list_create_categories'),
    path('/transmissions', TransmissionListCreateView.as_view(), name='list_create_transmissions'),
    path('/fuel_types', FuelTypeListCreateView.as_view(), name='list_create_fuel_types'),
    path('/statuses', StatusListCreateView.as_view(), name='list_create_statuses'),
]
