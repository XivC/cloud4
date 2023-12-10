from rest_framework.exceptions import ValidationError

from library.models import Book
from library.services.genre_creator import GenreCreator


class BookUpdater:

    def update(self, book: Book, data: dict) -> Book:
        genre_name = data.pop('genre_name', None)

        if genre_name:
            genre = GenreCreator().create(genre_name)
            data['genre'] = genre

        for attr, value in data.items():
            setattr(book, attr, value)

        book.save()

        return book
