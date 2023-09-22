from django.urls import path

from lessons.views import UserLessonAccessListView, ProductLessonsAccessListView

app_name = "lessons"

urlpatterns = [
    path("all/", UserLessonAccessListView.as_view(), name="all-list"),
    path("product/<int:product_id>/", ProductLessonsAccessListView.as_view(), name="product-lessons-access-list"),
]
