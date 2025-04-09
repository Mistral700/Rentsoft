from rest_framework import serializers

from apps.advertisements.models import AdvertisementModel
from apps.bookings.models import BookingModel


class BookingSerializer(serializers.ModelSerializer):
    advert = serializers.PrimaryKeyRelatedField(
        queryset=AdvertisementModel.objects.all(),
    )

    class Meta:
        model = BookingModel
        fields = ('id', 'date_from', 'date_to', 'advert',
                  'user', 'created_at', 'updated_at',)

        read_only_fields = ('id', 'created_at', 'updated_at', 'user',)
