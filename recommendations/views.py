from django.db.models import QuerySet
from django.shortcuts import render
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from library.models import Book
from library.serializers import BookSerializer
from recommendations.models import Recommendation
from users.models import User


class RecommendationsViewSet(
    mixins.ListModelMixin,
    GenericViewSet,
):

    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer
    queryset = Book.objects.for_viewset()

    @property
    def user(self) -> User:
        return self.request.user

    def get_queryset(self) -> QuerySet[Book]:
        last_recommendation = Recommendation.objects.filter(user=self.user).order_by('-revision').first()
        if not last_recommendation:
            return Book.objects.none()

        last_revision = last_recommendation.revision

        return Book.objects.for_viewset().filter(id__in=Recommendation.objects.filter(user=self.user, revision=last_revision).values_list('book_id', flat=True))
