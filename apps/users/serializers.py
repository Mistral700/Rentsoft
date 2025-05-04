from django.contrib.auth import get_user_model
from django.core.files import File
from django.db.transaction import atomic

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ValidationError

import os, re
from apps.users.models import ProfileModel


UserModel = get_user_model()


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('id', 'name', 'surname', 'avatar')


class ProfileAvatarSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('avatar',)
        extra_kwargs = {'avatar': {'required': True}}

    def validate_avatar(self, avatar: File):
        # 100Kb
        max_size = 100 * 1024
        if avatar.size > max_size:
            raise ValidationError('max_size for avatar - 100Kb')

        return avatar


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'created_at',
            'updated_at', 'profile',
        )
        read_only_fields = ('id', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'created_at', 'updated_at',)
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def validate_password(self, value):
        pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>])[^\s]{8,}$'
        safe_password = os.environ.get("SAFE_PASSWORD_VALIDATION") == "True"

        if safe_password and not re.match(pattern, value):
            raise serializers.ValidationError(
                "The password must contain at least 8 characters, "
                "at least one letter, one number, one special character, and no spaces."
            )
        return value

    @atomic
    def create(self, validated_data: dict):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user)
        return user
