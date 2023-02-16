from django.db import models


class ProductMain(models.Model):
    title = models.CharField(max_length=254)
    description = models.CharField(max_length=254)
    unique_id = models.CharField(max_length=254, unique=True)
    price = models.IntegerField()

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(ProductMain, on_delete=models.CASCADE)
    image = models.ImageField(max_length=254, upload_to='products')

    def __str__(self):
        return self.product, self.image
