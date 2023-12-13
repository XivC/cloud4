from rest_framework.routers import SimpleRouter

from library.views import BookStaffViewSet, BookViewSet, CollectionViewSet
from recommendations.views import RecommendationsViewSet

router = SimpleRouter()

router.register('recommendations', RecommendationsViewSet)

urlpatterns = router.urls
