from django.db import models
from django.db.models import Subquery, Count, Sum, FloatField, OuterRef

from users.models import UserLessonAccess


class ProductManager(models.Manager):
    def statistics(self):
        def get_outer_queryset():
            return UserLessonAccess.objects.filter(lesson__in=OuterRef("lessons"))

        return self.annotate(
            total_lessons_viewed=Count(
                Subquery(get_outer_queryset().filter(viewed=True).values("lesson"))
            ),
            total_viewing_time=Sum(
                Subquery(get_outer_queryset().values("view_time_seconds"))
            ),
            total_students=Count(Subquery(get_outer_queryset().values("user"))),
            acquisition_percentage=Count(
                Subquery(get_outer_queryset().values("user")),
                output_field=FloatField(),
            )
            / Count(
                Subquery(get_outer_queryset().values("user").distinct()),
                output_field=FloatField(),
            )
            * 100,
        )
