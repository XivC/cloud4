from django.db.models import QuerySet
from django.shortcuts import render
from django.views import View
from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ReadOnlyModelViewSet

from library.models import Book
from library.serializers import BookCreateSerializer, BookUpdateSerializer, BookSerializer
from library.services import BookCreator, BookUpdater
from users.models import User


class BookStaffViewSet(mixins.CreateModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       GenericViewSet):

    queryset = Book.objects.for_viewset()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        serializer = BookCreateSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        book = BookCreator().create(serializer.validated_data)

        return Response(status=201, data=BookSerializer(instance=book).data)

    def partial_update(self, request, *args, **kwargs):
        serializer = BookUpdateSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        book = BookUpdater().update(serializer.validated_data)

        return Response(status=200, data=BookSerializer(instance=book).data)

    def update(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class BookViewSet(ReadOnlyModelViewSet):

    queryset = Book.objects.for_viewset()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


class CollectionViewSet(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
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
        if self.action == 'list':
            return self.user.books.all()
        return super().get_queryset()

    def update(self, request, *args, **kwargs):
        book = self.get_object()

        self.user.books.add(book)

        return Response(status=204)

    def partial_update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)






