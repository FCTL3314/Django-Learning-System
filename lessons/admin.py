from django.contrib import admin

from lessons.models import Lesson


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    search_fields = ("name", "video_link")
    ordering = ("name",)
