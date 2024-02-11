from django.contrib import admin
from . models import UserOrder

@admin.register(UserOrder)
class UserOrderAdmin(admin.ModelAdmin):
    list_display = ('users', 'productB', 'number', 'random_number', 'created')
