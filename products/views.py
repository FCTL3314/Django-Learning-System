from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView

from products.models import Product
from products.serializers import ProductStatisticsSerializer

User = get_user_model()


class ProductStatisticsListView(ListAPIView):
    queryset = Product.objects.statistics()
    serializer_class = ProductStatisticsSerializer
