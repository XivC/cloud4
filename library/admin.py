from django.contrib import admin

from library.models import Book, Genre


class BookAdmin(admin.ModelAdmin):

    fields = (
        'name',
        'author',
        'published_at',
        'description',
        'content_url',
        'genre',
    )

    list_display = (
        'name',
        'author',
        'published_at',
        'genre',
    )

    list_select_related = ('genre',)


class GenreAdmin(admin.ModelAdmin):

    fields = (
        'name',
        'parent_genre',
    )

    list_display = (
        'id',
        'name',
    )

    list_select_related = ('parent_genre',)


admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)