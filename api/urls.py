from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoriesViewSet, GenreViewSet, TitleViewSet

router = DefaultRouter()
router.register('titles', TitleViewSet, basename='title')
router.register('genres', GenreViewSet, basename='genre')
router.register('categories', CategoriesViewSet, basename='category')

urlpatterns = [
    path('v1/', include(router.urls)),
]
