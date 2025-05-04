from django.db import models
from django.core import validators as V
from django.contrib.auth import get_user_model

from apps.users.models import UserModel as User

from core.services.upload_car_photo_service import upload_to

UserModel: User = get_user_model()


class FuelTypeModel(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'fuel_types'

    def __str__(self):
        return f'{self.name}'


class TransmissionModel(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'transmissions'

    def __str__(self):
        return f'{self.name}'


class CategoryModel(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return f'{self.name}'


class StatusModel(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.name}'


class AdvertisementModel(models.Model):
    car_brand = models.CharField(max_length=128)
    car_model = models.CharField(max_length=128)
    engine = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    vin = models.CharField(max_length=17, unique=True)
    insurance = models.CharField(max_length=128)
    price = models.FloatField()
    price_period = models.CharField(max_length=128)
    mileage = models.CharField(max_length=20)
    pledge = models.BooleanField()
    purpose = models.CharField(max_length=128)
    driver = models.BooleanField()
    comment = models.TextField()
    location = models.CharField(max_length=255)
    fuel_type = models.ManyToManyField(FuelTypeModel, related_name='advertisement_fuel')
    transmission = models.ForeignKey(
        TransmissionModel,
        on_delete=models.CASCADE,
        related_name='advertisement_transmission'
    )
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.CASCADE,
        related_name='advertisement_category'
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='advertisement_user'
    )
    status = models.ForeignKey(
        StatusModel,
        on_delete=models.CASCADE,
        related_name='advertisement_status'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'advertisements'
        ordering = ("id",)


class AdvertisementPhotoModel(models.Model):
    class Meta:
        db_table = 'adverts_photo'

    photo = models.ImageField(upload_to=upload_to, blank=True, validators=(
        V.FileExtensionValidator(['gif', 'jpeg', 'png', 'jpg']),
    ))
    advert = models.ForeignKey(AdvertisementModel, on_delete=models.CASCADE, related_name='photos')
