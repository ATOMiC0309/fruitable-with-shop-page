from django.urls import path
from .views import ProductList, AllProductList, product_by_category

urlpatterns = [
    path('', ProductList.as_view(), name='index'),
    path('shop/', AllProductList.as_view(), name="shop"),
    path('product-by/<int:pk>/', product_by_category, name="product_by_category"),
]