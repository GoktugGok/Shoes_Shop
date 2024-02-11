from django.contrib import admin
from . models import Category,Shoes,Tag,Numbers,ShoesC,ShopBag,PayDetails

@admin.register(Category)
class CateoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(ShopBag)
class ShopBagAdmin(admin.ModelAdmin):
    pass

@admin.register(ShoesC)
class ShoesCAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(Numbers)
class NumbersAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(Shoes)
class ShoesAdmin(admin.ModelAdmin):
    list_display = ('name','active',)
    search_fields = ('name','category',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(PayDetails)
class PayDetailsAdmin(admin.ModelAdmin):
    list_display = ('name',)


