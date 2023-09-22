from django.urls import path

from lessons.views import UserLessonAccessListView

app_name = "lessons"

urlpatterns = [
    path("all/", UserLessonAccessListView.as_view(), name="all"),
]
