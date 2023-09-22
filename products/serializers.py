from django.contrib.auth import get_user_model
from rest_framework import serializers

from products.models import Product

User = get_user_model()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "owner")


class ProductStatisticsSerializer(ProductSerializer):
    total_lessons_viewed = serializers.IntegerField()
    total_viewing_time = serializers.IntegerField()
    total_students = serializers.IntegerField()
    acquisition_percentage = serializers.FloatField()

    class Meta(ProductSerializer.Meta):
        fields = ProductSerializer.Meta.fields + (
            "total_lessons_viewed",
            "total_viewing_time",
            "total_students",
            "acquisition_percentage",
        )
