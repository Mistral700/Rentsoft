from django.utils.decorators import method_decorator

from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from apps.auth.swagger.serializers import SwaggerUserSerializer


def users_swagger():
    return method_decorator(
        swagger_auto_schema(responses={
            status.HTTP_200_OK: SwaggerUserSerializer(many=True)
        }),
        'get'
    )
