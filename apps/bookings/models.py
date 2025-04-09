from django.db import models
from django.contrib.auth import get_user_model

from apps.advertisements.models import AdvertisementModel
from apps.users.models import UserModel as User

UserModel: User = get_user_model()


class BookingModel(models.Model):
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    advert = models.ForeignKey(
        AdvertisementModel,
        on_delete=models.CASCADE,
        related_name='booking_advert',
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='booking_user',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'bookings'
