from django.urls import path

from apps.diia.views import DiiaAuthTokenView


urlpatterns = [
    path('/auth', DiiaAuthTokenView.as_view(), name='diia_auth_token'),
]
