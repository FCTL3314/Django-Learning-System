from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from users.models import UserLessonAccess
from lessons.paginators import UserLessonAccessPageNumberPagination
from users.serializers import (
    UserLessonAccessSerializer,
    UserLessonAccessWithDateSerializer,
)


class UserLessonAccessListView(ListAPIView):
    model = UserLessonAccess
    serializer_class = UserLessonAccessSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = UserLessonAccessPageNumberPagination

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class ProductLessonsAccessListView(ListAPIView):
    serializer_class = UserLessonAccessWithDateSerializer
    pagination_class = UserLessonAccessPageNumberPagination

    def get_queryset(self):
        return UserLessonAccess.objects.filter(
            user=self.request.user, lesson__products__id=self.kwargs["product_id"]
        )
