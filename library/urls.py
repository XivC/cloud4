from rest_framework.routers import SimpleRouter

from library.views import BookStaffViewSet, BookViewSet, CollectionViewSet

router = SimpleRouter()

router.register('staff/books', BookStaffViewSet)
router.register('books', BookViewSet)
router.register('collection/books', CollectionViewSet)

urlpatterns = router.urls
