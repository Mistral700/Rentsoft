from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.auth.views import AuthRegisterView


urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='token_auth'),
    path('/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('/register', AuthRegisterView.as_view(), name='auth_register'),
]