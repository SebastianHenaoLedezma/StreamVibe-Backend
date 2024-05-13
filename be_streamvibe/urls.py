from rest_framework import routers
from .api import MovieViewSet, GenreViewSet, DirectorViewSet, LanguageViewSet, ActorViewSet, UserViewSet, FaqViewSet, SupportRequestViewSet, ReviewViewSet, RatingViewSet

router = routers.DefaultRouter()

router.register('api/movies', MovieViewSet, 'movies')
router.register('api/genres', GenreViewSet, 'genres')
router.register('api/directors', DirectorViewSet, 'directors')
router.register('api/languages', LanguageViewSet, 'languages')
router.register('api/actors', ActorViewSet, 'actors')
router.register('api/users', UserViewSet, 'users' )
router.register('api/faqs', FaqViewSet, 'faqs' )
router.register('api/supportRequest', SupportRequestViewSet, 'supportRequests' )
router.register('api/reviews', ReviewViewSet)
router.register('api/rating', RatingViewSet, 'ratings')

urlpatterns = router.urls

