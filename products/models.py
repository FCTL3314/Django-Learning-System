from django.contrib.auth import get_user_model
from django.db import models

from products.managers import ProductManager

User = get_user_model()


class Product(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = ProductManager()

    def __str__(self):
        return self.name
