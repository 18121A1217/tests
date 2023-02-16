from django.urls import path
from accounts.views import UserList, UserCartList

urlpatterns = [
    path('accounts/', UserList.as_view()),
    path('user/cart/', UserCartList.as_view()),
]
