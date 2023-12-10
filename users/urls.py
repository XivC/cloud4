from django.urls import path
from rest_framework.routers import SimpleRouter

from library.views import BookStaffViewSet
from users.views import UserRegistrationView

urlpatterns = [
    path('users/register/', UserRegistrationView.as_view())
]
