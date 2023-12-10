from celery.utils.log import get_task_logger

from cloud4 import celery


from recommendations.models import Recommendation

import logging

from recommendations.recommendations_settings import get_settings
from recommendations.recommendations_system import UserRecommendationsUpdater
from users.models import User

logger = logging.getLogger(__name__)


@celery.task
def update_user_recommendations(user_id: int, max_books: int):
    user = User.objects.get(id=user_id)
    UserRecommendationsUpdater().update(user, max_books)


@celery.task(
    name='update_recommendations',
)
def update_recommendations():
    settings = get_settings()
    for user in User.objects.all():
        update_user_recommendations.delay(user.id, settings.max_books)


