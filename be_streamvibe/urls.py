from rest_framework import routers
from .api import MovieViewSet, GenreViewSet, DirectorViewSet, LanguageViewSet, ActorViewSet, MusicCreatorViewSet

router = routers.DefaultRouter()

router.register('api/movies', MovieViewSet, 'movies')
router.register('api/genres', GenreViewSet, 'genres')
router.register('api/directors', DirectorViewSet, 'directors')
router.register('api/languages', LanguageViewSet, 'languages')
router.register('api/actors', ActorViewSet, 'actors')
router.register('api/music_creator', MusicCreatorViewSet, 'music_creator')

urlpatterns = router.urls

