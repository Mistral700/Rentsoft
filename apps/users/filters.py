from django_filters import rest_framework as filters


class AdvertisementFilter(filters.FilterSet):
    status = filters.CharFilter('status__name', 'iexact')
