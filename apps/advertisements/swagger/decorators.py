from django.utils.decorators import method_decorator

from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from apps.advertisements.serializers import AdvertisementSerializer
from apps.advertisements.swagger.serializers import AdvertUpdateSerializer


def adverts_swagger():
    return method_decorator(
        swagger_auto_schema(responses={
            status.HTTP_200_OK: AdvertisementSerializer(many=True)
        }),
        'get'
    )


def advert_swagger():
    return method_decorator(
        swagger_auto_schema(responses={
            status.HTTP_201_CREATED: AdvertisementSerializer()
        }),
        'post'
    )


def adverts_partial_update_swagger():
    return method_decorator(
        swagger_auto_schema(request_body=AdvertUpdateSerializer, responses={
            status.HTTP_200_OK: AdvertisementSerializer()
        }),
        'patch'
    )
