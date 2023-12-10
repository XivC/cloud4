from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255)
    parent_genre = models.ForeignKey('library.Genre', null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.name