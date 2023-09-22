from django.contrib import admin

from users.models import UserLessonAccess


@admin.register(UserLessonAccess)
class UserLessonAccessAdmin(admin.ModelAdmin):
    search_fields = ("lesson__name",)
    ordering = ("lesson__name",)
