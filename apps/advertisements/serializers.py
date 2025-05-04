from rest_framework import serializers

from apps.advertisements.models import (
    AdvertisementModel,
    AdvertisementPhotoModel,
    CategoryModel,
    TransmissionModel,
    FuelTypeModel,
    StatusModel,
)

from core.dataclasses.user_dataclasses import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ('id', 'name',)


class TransmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransmissionModel
        fields = ('id', 'name',)


class FuelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelTypeModel
        fields = ('id', 'name',)


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusModel
        fields = ('id', 'name',)


class UserAdvertisementSerializer(serializers.RelatedField):
    def to_representation(self, value: User):
        return {'id': value.id, 'email': value.email}


class AdvertPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertisementPhotoModel
        fields = ('photo',)

    def to_representation(self, instance):
        return {'id': instance.id, 'url': instance.photo.url}


class AdvertisementSerializer(serializers.ModelSerializer):
    fuel_type = serializers.PrimaryKeyRelatedField(
        queryset=FuelTypeModel.objects.all(),
        many=True
    )
    transmission = serializers.PrimaryKeyRelatedField(
        queryset=TransmissionModel.objects.all(),
    )
    category = serializers.PrimaryKeyRelatedField(
        queryset=CategoryModel.objects.all(),
    )
    user = UserAdvertisementSerializer(read_only=True)
    photos = AdvertPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = AdvertisementModel
        fields = ('id', 'car_brand', 'car_model', 'engine', 'vin',
                  'insurance', 'price', 'price_period', 'mileage',
                  'pledge', 'purpose', 'driver', 'comment',
                  'location', 'fuel_type', 'transmission', 'category',
                  'user', 'status', 'photos', 'created_at', 'updated_at',)

        read_only_fields = ('id', 'created_at', 'updated_at', 'user', 'status')
