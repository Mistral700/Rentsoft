from django.core import validators as V
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from apps.users.managers import UserManager

from core.services.upload_user_photo_service import upload_avatar


class UserModel(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(unique=True)
    password = models.CharField(validators=[V.RegexValidator(
        regex=r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>])[^\s]{8,}$',
        message="The password must contain at least 8 characters,\
        at least one letter, one number, one special character, and no spaces."
    )])
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()


class ProfileModel(models.Model):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    avatar = models.ImageField(upload_to=upload_avatar, blank=True, validators=(
        V.FileExtensionValidator(['gif', 'jpeg', 'png', 'jpg']),
    ))
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
