from django.urls import path
from products.views import ProductImageList

urlpatterns = [
    path('products/', ProductImageList.as_view()),
]
