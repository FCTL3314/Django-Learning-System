from django.db import models


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    video_link = models.URLField()
    duration_seconds = models.PositiveIntegerField()
    products = models.ManyToManyField("products.Product", related_name="lessons")

    def __str__(self):
        return self.name
