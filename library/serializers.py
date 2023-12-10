from rest_framework import serializers

from library.models import Book


class BookCreateSerializer(serializers.ModelSerializer):

    name = serializers.CharField(required=True, allow_null=False, trim_whitespace=True)
    author = serializers.CharField(required=False, allow_blank=False, allow_null=True, trim_whitespace=True)
    published_at = serializers.DateField(required=False, allow_null=True)
    description = serializers.CharField(required=False, allow_null=True)
    content_url = serializers.URLField(required=True, allow_null=False)
    genre_name = serializers.CharField(required=False, allow_null=False)

    class Meta:
        model = Book

        fields = [
            'name',
            'author',
            'published_at',
            'description',
            'content_url',
            'genre_name',
        ]


class BookUpdateSerializer(serializers.ModelSerializer):

    name = serializers.CharField(required=False, allow_null=False, trim_whitespace=True)
    author = serializers.CharField(required=False, allow_blank=False, allow_null=True, trim_whitespace=True)
    published_at = serializers.DateField(required=False, allow_null=True)
    description = serializers.CharField(required=False, allow_null=True)
    content_url = serializers.URLField(required=False, allow_null=False)
    genre_name = serializers.CharField(required=False, allow_null=False)

    class Meta:
        model = Book

        fields = [
            'name',
            'author',
            'published_at',
            'description',
            'content_url',
            'genre_name',
        ]


class BookSerializer(serializers.ModelSerializer):

    genre_name = serializers.CharField(source='genre.name', allow_null=True)

    class Meta:
        model = Book

        fields = [
            'name',
            'author',
            'published_at',
            'description',
            'content_url',
            'genre_name',
        ]
