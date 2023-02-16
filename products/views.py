from rest_framework.views import APIView
from products.models import ProductMain, ProductImage
from products.serializers import ProductImageModelSerializer
from rest_framework.response import Response


class ProductImageList(APIView):
    def get(self, request, format=None):
        user = ProductImage.objects.all()
        serializer = ProductImageModelSerializer(user, many=True)
        return Response(serializer.data)
