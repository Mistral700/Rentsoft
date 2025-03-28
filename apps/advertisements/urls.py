from django.urls import path

from apps.advertisements.views import (
    AdvertisementsListView,
    MineAdvertisementListCreateView,
    MineAdvertisementGetUpdateDestroy,
    CategoryListCreateView,
    TransmissionListCreateView,
    FuelTypeListCreateView
)


urlpatterns = [
    path('', AdvertisementsListView.as_view(), name='list_advertisements'),
    path('/mine', MineAdvertisementListCreateView.as_view(), name='list_create_mine_advertisements'),
    path('/mine/<int:pk>', MineAdvertisementGetUpdateDestroy.as_view(), name='get_update_destroy_mine_advertisements'),

    path('/categories', CategoryListCreateView.as_view(), name='list_create_categories'),
    path('/transmissions', TransmissionListCreateView.as_view(), name='list_create_transmissions'),
    path('/fuel_types', FuelTypeListCreateView.as_view(), name='list_create_fuel_types'),
]
