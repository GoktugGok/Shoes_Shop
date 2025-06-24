from django.contrib import admin
from . models import Category,ShoesDetail,Brand,ShoesNumbers,ShoesModel,ShopBag,PayDetail,Images,Comment,Color,Genders,ShoeHeight
from mptt.admin import DraggableMPTTAdmin

class ProductImagesInline(admin.TabularInline):
    model = Images
    extra = 5
    readonly_fields = ['image_tag']

class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                ShoesDetail,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 ShoesDetail,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'


# admin.site.register(Category,MPTTModelAdmin)
admin.site.register(Category,CategoryAdmin2)

@admin.register(ShopBag)
class ShopBagAdmin(admin.ModelAdmin):
    pass

@admin.register(ShoesModel)
class ShoesModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(Genders)
class GendersAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(ShoeHeight)
class ShoeHeightAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    
@admin.register(ShoesNumbers)
class ShoesNumbersAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(ShoesDetail)
class ShoesDetailAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_tag', 'active']
    search_fields = ('name','category',)
    readonly_fields = ('image_tag',)
    inlines=[ProductImagesInline]
    prepopulated_fields = {"slug": ("name",)}
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(PayDetail)
class PayDetailAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title','product', 'image_tag']
    readonly_fields = ['image_tag']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user','subject']



