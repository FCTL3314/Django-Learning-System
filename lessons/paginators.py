from rest_framework.pagination import PageNumberPagination


class UserLessonAccessPageNumberPagination(PageNumberPagination):
    page_size = 8
