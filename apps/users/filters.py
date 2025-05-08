from django_filters import rest_framework as filters


class AdvertisementFilter(filters.FilterSet):
    status = filters.CharFilter('status__name', 'iexact')
    brand = filters.CharFilter('car_brand', 'icontains')
    model = filters.CharFilter('car_model', 'icontains')
    engine = filters.CharFilter('engine', 'iexact')
    vin = filters.CharFilter('vin', 'iexact')
    price_lt = filters.NumberFilter('price', 'lt')
    price_gt = filters.NumberFilter('price', 'gt')
    location = filters.CharFilter('location', 'icontains')
    fuel_type = filters.CharFilter('fuel_type__name', 'iexact')
    category = filters.CharFilter('category__name', 'iexact')
    transmission = filters.CharFilter('transmission__name', 'iexact')
    pledge = filters.CharFilter('pledge', 'iexact')
    driver = filters.CharFilter('driver', 'iexact')
    insurance = filters.CharFilter('insurance', 'icontains')
