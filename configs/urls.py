from django.urls import path, include


urlpatterns = [
    path('auth', include('apps.auth.urls')),
    path('advertisements', include('apps.advertisements.urls')),
    path('users', include('apps.users.urls')),
]