from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.advertisements.models import AdvertisementModel
from apps.advertisements.serializers import AdvertisementSerializer
from apps.bookings.models import BookingModel
from apps.users.serializers import UserSerializer

from core.dataclasses.advertisement_dataclasses import Advertisement
from core.dataclasses.user_dataclasses import User

UserModel = get_user_model()


class AdvertSerializer(serializers.RelatedField):
    def to_representation(self, value: Advertisement):
        return AdvertisementSerializer(value).data

    def to_internal_value(self, advert_id):
        try:
            return AdvertisementModel.objects.get(id=advert_id)
        except AdvertisementModel.DoesNotExist:
            raise serializers.ValidationError('There is no object with that id.')


class UserBookingSerializer(serializers.RelatedField):
    def to_representation(self, value: User):
        return {
            'id': value.id,
            'email': value.email,
            'name': value.profile.name,
            'surname': value.profile.surname,
        }


class BookingSerializer(serializers.ModelSerializer):
    advert = AdvertSerializer(queryset=AdvertisementModel.objects.all())
    user = UserBookingSerializer(read_only=True)

    class Meta:
        model = BookingModel
        fields = ('id', 'date_from', 'date_to', 'advert',
                  'user', 'created_at', 'updated_at',)

        read_only_fields = ('id', 'created_at', 'updated_at', 'user',)


class ClientBookingSerializer(UserSerializer):
    name = serializers.CharField(source='profile.name')
    surname = serializers.CharField(source='profile.surname')
    bookings = BookingSerializer(many=True, source='booking_user')

    class Meta(UserSerializer.Meta):
        fields = ('id', 'email', 'name', 'surname', 'bookings',)
