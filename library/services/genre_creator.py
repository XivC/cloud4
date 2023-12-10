from library.models import Genre


class GenreCreator:

    def create(self, genre_name: str) -> Genre:
        genre = Genre.objects.filter(
            name__trigram_word_similar=genre_name,
        ).first()
        if not genre:
            genre = Genre.objects.create(name=genre_name)

        return genre
