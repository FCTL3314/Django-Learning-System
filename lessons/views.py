from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from users.models import UserLessonAccess
from users.paginators import UserLessonAccessPageNumberPagination
from users.serializers import UserLessonAccessSerializer


class UserLessonAccessListView(ListAPIView):
    model = UserLessonAccess
    serializer_class = UserLessonAccessSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = UserLessonAccessPageNumberPagination

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
