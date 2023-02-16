from django.shortcuts import render
from rest_framework.views import APIView
from accounts.models import User, UserCart
from accounts.serializers import UserModelSerializer, UserCartModelSerializer
from rest_framework.response import Response
from rest_framework import status


class UserList(APIView):
    def get(self, request, format=None):
        user = User.objects.all()
        serializer = UserModelSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserCartList(APIView):
    def get(self, request, format=None):
        user_cart = UserCart.objects.all()
        serializer = UserCartModelSerializer(user_cart, many=True)
        return Response(serializer.data)
