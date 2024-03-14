from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

class ShoesNumbers(models.Model):
    name = models.CharField(max_length=50,null=True)
    slug = models.SlugField(max_length=50,unique=True,null=True)

    def __str__(self):
        return self.name
class Color(models.Model):
    name = models.CharField(max_length=50,null=True)
    slug = models.SlugField(max_length=50,unique=True,null=True)

    def __str__(self):
        return self.name
class Genders(models.Model):
    name = models.CharField(max_length=50,null=True)
    slug = models.SlugField(max_length=50,unique=True,null=True)

    def __str__(self):
        return self.name

class ShoeHeight(models.Model):
    name = models.CharField(max_length=50,null=True)
    slug = models.SlugField(max_length=50,unique=True,null=True)

    def __str__(self):
        return self.name

class Category(MPTTModel):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayir'))
    title = models.CharField(max_length=30)
    keywords = models.CharField(blank=True, max_length=250)
    description = models.CharField(blank=True, max_length=250)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children',
                               on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.name
    class MPTTMeta:
        order_insertion_by = ['title']
    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return '/'.join(full_path)

class ShoesModel(models.Model):
    name = models.CharField(max_length=50,null=True)
    slug = models.SlugField(max_length=50,unique=True,null=True)

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=50,null=True )
    slug = models.SlugField(max_length=50,unique=True,null=True)

    def __str__(self):
        return self.name
    

class ShoesDetail(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, max_length=255)
    active = models.BooleanField(default=True)
    price = models.DecimalField(verbose_name='ürün fiyatı', decimal_places=2, max_digits=10)
    stock_count = models.PositiveSmallIntegerField()
    numbers = models.ManyToManyField(ShoesNumbers,blank=True,related_name="product_numbers")
    detail=RichTextUploadingField()
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 
    image = models.ImageField(blank=True, upload_to='images/', default="default.png")

    color = models.ManyToManyField(Color,blank=True,related_name="color")
    shoe_Height = models.ManyToManyField(ShoeHeight,blank=True,related_name="shoe_Height")
    genders = models.ManyToManyField(Genders,blank=True,related_name="genders")
    category = models.ManyToManyField(Category,blank=True,related_name="category")
    shoesC = models.ForeignKey(ShoesModel,null=True,on_delete=models.DO_NOTHING)
    product_Brand = models.ManyToManyField(Brand,blank=True,related_name="brands")
    reviewsCount = models.IntegerField(default=0)
    slug = models.SlugField(null=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'
#     urunler için resim galerisi oluşturmak için
    def img_preview(self):  # new
        return mark_safe(f'<img src = "{self.image.url}" width = "300"/>')
class Images(models.Model):
    product = models.ForeignKey(ShoesDetail, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='images/')
    def __str__(self):
        return self.title
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

class Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    product = models.ForeignKey(ShoesDetail, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True)
    comment = models.CharField(max_length=250, blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.subject
class ShopBag(models.Model):
    users = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    productB = models.CharField(max_length=50,null=True)
    number = models.CharField(max_length=50,null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
class PayDetail(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=50,null=True)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    cardNumber = models.CharField(max_length=16)
    day = models.CharField(max_length=2)
    year = models.CharField(max_length=4)
    clv = models.CharField(max_length=3)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def clean(self):
        # Türkçe standartlarına uygun bir formata dönüştürme işlemi
        if ',' in str(self.price):
            self.price = str(self.price).replace(',', '.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)