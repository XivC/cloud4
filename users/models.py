from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    books = models.ManyToManyField('library.Book')

