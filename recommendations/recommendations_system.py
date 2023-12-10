from django.db.models import Count, Max

from library.models import Book
from recommendations.models import RecommendationSettings, Recommendation
from users.models import User


class UserRecommendationsUpdater:
    """
    Very simplified realization of re:match v2.0 recommendations system.
    Full realization docs: https://yadi.sk/i/FiwW2xe9hzpkhA
    Full realization code is private, authored by Dybov.A, Lavrov.A, Korepanov.M
    """

    def update(self, user: User, max_books: int) -> None:

        user_genres_rate = user.books.values('genre_id').annotate(count=Count('genre_id')).values('genre_id', 'count').order_by('-count')

        if not user_genres_rate:
            return

        books_from_genre = {}

        for result in user_genres_rate:
            books_from_genre[result['genre_id']] = max_books // 2 + 1
            max_books //= 2

            if max_books == 0:
                break

        new_revision = (user.recommendations.aggregate(Max('revision')).get('revision__max') or 0) + 1

        books_to_recommendate = Book.objects.none()
        for genre_id, books_count in books_from_genre.items():
            books_to_recommendate |= Book.objects.filter(genre_id=genre_id).exclude(id__in=user.books.values_list('id', flat=True)).order_by('?')[:books_count]

        recommendations = []
        for book in books_to_recommendate:
            recommendation = Recommendation(
                user=user,
                book=book,
                revision=new_revision,
            )
            recommendations.append(recommendation)

        Recommendation.objects.bulk_create(recommendations)




