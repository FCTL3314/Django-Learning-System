from rest_framework import serializers

from users.models import UserLessonAccess


class UserLessonAccessSerializer(serializers.ModelSerializer):
    lesson_name = serializers.ReadOnlyField(source="lesson.name")
    lesson_video_link = serializers.ReadOnlyField(source="lesson.video_link")
    lesson_duration_seconds = serializers.ReadOnlyField(
        source="lesson.duration_seconds"
    )
    viewed = serializers.ReadOnlyField()

    class Meta:
        model = UserLessonAccess
        fields = (
            "lesson_name",
            "lesson_video_link",
            "lesson_duration_seconds",
            "view_time_seconds",
            "viewed",
        )
