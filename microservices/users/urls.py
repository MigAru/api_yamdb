from django.urls import include, path
from .views import get_confirmation_code, get_token

urlpatterns = [
    path('auth/email/', get_confirmation_code),
    path('auth/token/', get_token),
]