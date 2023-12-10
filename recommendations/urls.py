from rest_framework.routers import SimpleRouter

from library.views import BookStaffViewSet, BookViewSet, CollectionViewSet

router = SimpleRouter()

router.register('recommendations', CollectionViewSet)

urlpatterns = router.urls
