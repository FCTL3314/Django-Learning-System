from django.contrib.auth import get_user_model
from django.db import models

from lessons.models import Lesson

User = get_user_model()


class UserLessonAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    view_time_seconds = models.PositiveIntegerField(default=0)

    @property
    def viewed(self) -> bool:
        return self.view_time_seconds >= 0.8 * self.lesson.duration_seconds
