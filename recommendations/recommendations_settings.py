from recommendations.models import RecommendationSettings


def get_settings() -> RecommendationSettings:

    settings = RecommendationSettings.objects.first()
    if not settings:
        settings = RecommendationSettings.objects.create()

    return settings
