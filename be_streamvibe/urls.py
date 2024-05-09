from rest_framework import routers
from .api import MovieViewSet, GenreViewSet

router = routers.DefaultRouter()

router.register('api/movies', MovieViewSet, 'movies')
router.register('api/genres', GenreViewSet, 'genres')

urlpatterns = router.urls
