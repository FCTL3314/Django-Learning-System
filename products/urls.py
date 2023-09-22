from django.urls import path

from products.views import ProductStatisticsListView

app_name = "products"

urlpatterns = [
    path(
        "statistics/",
        ProductStatisticsListView.as_view(),
        name="statistics",
    )
]
