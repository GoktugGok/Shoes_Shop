from django.db import models
from django.contrib.auth.models import User

class Numbers(models.Model):
    name = models.CharField(max_length=50,null=True)
    slug = models.SlugField(max_length=50,unique=True,null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50,null=True)
    slug = models.SlugField(max_length=50,unique=True,null=True)

    def __str__(self):
        return self.name

class ShoesC(models.Model):
    name = models.CharField(max_length=50,null=True)
    slug = models.SlugField(max_length=50,unique=True,null=True)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=50,null=True )
    slug = models.SlugField(max_length=50,unique=True,null=True)

    def __str__(self):
        return self.name
    

class Shoes(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField(max_length=500,blank=True)
    active = models.BooleanField(default=True)
    price = models.DecimalField(verbose_name='ürün fiyatı', decimal_places=2, max_digits=10)
    stock_count = models.PositiveSmallIntegerField()
    numbers = models.ManyToManyField(Numbers,blank=True,related_name="product_numbers")
    created = models.DateTimeField(auto_now_add=True)
    image_one = models.ImageField(upload_to='images/',default="default.png")
    image_two = models.ImageField(upload_to='images/',default="default.png")
    image_three = models.ImageField(upload_to='images/',default="default.png")
    category = models.ManyToManyField(Category,blank=True,related_name="category")
    shoesC = models.ForeignKey(ShoesC,null=True,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
    

class ShopBag(models.Model):
    users = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    productB = models.CharField(max_length=50,null=True)
    number = models.CharField(max_length=50,null=True)

    
class PayDetails(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=50,null=True)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    cardNumber = models.CharField(max_length=16)
    day = models.CharField(max_length=2)
    year = models.CharField(max_length=4)
    clv = models.CharField(max_length=3)

    def clean(self):
        # Türkçe standartlarına uygun bir formata dönüştürme işlemi
        if ',' in str(self.price):
            self.price = str(self.price).replace(',', '.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)