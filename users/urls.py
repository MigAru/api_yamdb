from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, get_confirmation_code, get_token

router = DefaultRouter()

router.register('users', UserViewSet, basename='users')
urlpatterns = [
    path('v1/auth/email/', get_confirmation_code),
    path('v1/auth/token/', get_token),
    path('v1/', include(router.urls))
]
