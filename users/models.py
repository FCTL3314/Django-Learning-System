from django.contrib.auth import get_user_model
from django.db import models
from django.utils.timezone import now

User = get_user_model()


class UserLessonAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey("lessons.Lesson", on_delete=models.CASCADE)
    view_time_seconds = models.PositiveIntegerField(default=0)
    last_viewed_date = models.DateTimeField(null=True, blank=True)
    viewed = models.BooleanField(default=False)

    def set_viewed_status(self) -> None:
        """
        Mark lesson as viewed if 80% of the video
        is watched.
        """
        if self.view_time_seconds >= 0.8 * self.lesson.duration_seconds:
            self.viewed = True

    def update_last_viewed_date(self) -> None:
        self.last_viewed_date = now()
