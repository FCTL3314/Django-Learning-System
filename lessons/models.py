from django.db import models

from products.models import Product


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    video_link = models.URLField()
    duration_seconds = models.PositiveIntegerField()
    products = models.ManyToManyField(Product, related_name="lessons")

    def __str__(self):
        return self.name
