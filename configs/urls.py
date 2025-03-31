from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title='RentID_API',
        default_version='v1',
        description='About cars sharing',
    ),
    public=True,
    permission_classes=[AllowAny, ]
)

urlpatterns = [
    path('auth', include('apps.auth.urls')),
    path('advertisements', include('apps.advertisements.urls')),
    path('users', include('apps.users.urls')),
    path('doc', schema_view.with_ui('swagger', cache_timeout=0)),
]
