from rest_framework.exceptions import ValidationError

from library.models import Book
from library.services.genre_creator import GenreCreator


class BookCreator:

    def create(self, data: dict) -> Book:
        genre_name = data.pop('genre_name', None)

        if genre_name:
            genre = GenreCreator().create(genre_name)
            data['genre'] = genre

        book = Book(**data)
        book.save()

        return book
