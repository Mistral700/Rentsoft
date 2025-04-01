from django.urls import path

from apps.advertisements.views import (
    AdvertisementsListView,
    AdvertAddPhotoView,
    AdvertRemovePhotoView,
    MineAdvertisementListCreateView,
    MineAdvertisementGetUpdateDestroy,
    CategoryListCreateView,
    TransmissionListCreateView,
    FuelTypeListCreateView,
    StatusListCreateView,
)


urlpatterns = [
    path('', AdvertisementsListView.as_view(), name='list_advertisements'),
    path('/mine', MineAdvertisementListCreateView.as_view(), name='list_create_mine_advertisements'),
    path('/mine/<int:pk>', MineAdvertisementGetUpdateDestroy.as_view(), name='get_update_destroy_mine_advertisements'),

    path('/<int:pk>/photo', AdvertAddPhotoView.as_view(), name='add_advert_photo'),
    path('/photo/<int:pk>', AdvertRemovePhotoView.as_view(), name='remove_advert_photo'),

    path('/categories', CategoryListCreateView.as_view(), name='list_create_categories'),
    path('/transmissions', TransmissionListCreateView.as_view(), name='list_create_transmissions'),
    path('/fuel_types', FuelTypeListCreateView.as_view(), name='list_create_fuel_types'),
    path('/statuses', StatusListCreateView.as_view(), name='list_create_statuses'),
]
