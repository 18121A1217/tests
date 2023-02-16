from django.db import models
from products.models import ProductMain


class User(models.Model):
    phone_number = models.CharField(max_length=254, unique=True)
    email = models.EmailField()
    is_customer = models.BooleanField()
    is_admin = models.BooleanField()


class UserProfile(models.Model):
    GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
        ('OTHERS', 'OTHERS'),
    )
    gender = models.CharField(max_length=254, choices=GENDER)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='owner')
    name = models.CharField(max_length=254)
    date_of_birth = models.DateField()
    image = models.ImageField(max_length=254, upload_to='users')


class UserLoginOtp(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.IntegerField()
    active = models.BooleanField()


class UserCartProduct(models.Model):
    STATUS = (
        ('pending', 'pending'),
        ('completed', 'completed'),
    )
    status = models.CharField(max_length=254, choices=STATUS)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductMain, on_delete=models.CASCADE)


class UserCart(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(UserCartProduct)
    price = models.IntegerField()
