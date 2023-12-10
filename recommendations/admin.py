from django.contrib import admin

from recommendations.models import RecommendationSettings


class SettingsAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(RecommendationSettings, SettingsAdmin)