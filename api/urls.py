from rest_framework.routers import DefaultRouter

from .views import GenreViewSet, BookViewSet

router = DefaultRouter()
router.register('genres', GenreViewSet, basename='genre')
router.register('books', BookViewSet, basename='book')

urlpatterns = router.urls
