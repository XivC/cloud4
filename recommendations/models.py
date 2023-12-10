from django.db import models


class Recommendation(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='recommendations')
    book = models.ForeignKey('library.Book', on_delete=models.CASCADE)
    revision = models.PositiveIntegerField(default=0, null=False)


class RecommendationSettings(models.Model):

    refresh_rate = models.PositiveIntegerField(default=60)
    max_books = models.PositiveIntegerField(default=5)
