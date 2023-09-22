from rest_framework import serializers

from users.models import UserLessonAccess


class UserLessonAccessSerializer(serializers.ModelSerializer):
    lesson_name = serializers.ReadOnlyField(source="lesson.name")
    lesson_video_link = serializers.ReadOnlyField(source="lesson.video_link")
    lesson_duration_seconds = serializers.ReadOnlyField(
        source="lesson.duration_seconds"
    )

    class Meta:
        model = UserLessonAccess
        fields = (
            "lesson_name",
            "lesson_video_link",
            "lesson_duration_seconds",
            "view_time_seconds",
            "viewed",
        )


class UserLessonAccessWithDateSerializer(UserLessonAccessSerializer):
    last_viewed_date = serializers.DateTimeField(read_only=True)

    class Meta(UserLessonAccessSerializer.Meta):
        fields = UserLessonAccessSerializer.Meta.fields + ("last_viewed_date",)
