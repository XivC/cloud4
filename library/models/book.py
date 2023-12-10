from django.db import models


class BookQuerySet(models.QuerySet):

    def for_viewset(self) -> 'BookQuerySet':
        return self.select_related('genre')


class Book(models.Model):
    objects = models.Manager.from_queryset(BookQuerySet)()

    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255, null=True)
    published_at = models.DateField(null=True)
    description = models.TextField(null=True)
    content_url = models.URLField()
    genre = models.ForeignKey('library.Genre', on_delete=models.PROTECT)
