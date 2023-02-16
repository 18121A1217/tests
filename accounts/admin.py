from django.contrib import admin
from accounts.models import User, UserCart, UserProfile, UserCartProduct, UserLoginOtp


admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(UserLoginOtp)
admin.site.register(UserCartProduct)
admin.site.register(UserCart)
