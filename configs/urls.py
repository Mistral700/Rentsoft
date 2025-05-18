from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.http import JsonResponse

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title='Rentsoft_API',
        default_version='v1',
        description='About cars sharing',
    ),
    public=True,
    permission_classes=[AllowAny, ]
)

urlpatterns = [
    path("api/health", lambda request: JsonResponse({"status": "ok"})),

    path('api/auth', include('apps.auth.urls')),
    path('api/advertisements', include('apps.advertisements.urls')),
    path('api/users', include('apps.users.urls')),
    path('api/bookings', include('apps.bookings.urls')),
    path('api/doc', schema_view.with_ui('swagger', cache_timeout=0), name='documentation'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
