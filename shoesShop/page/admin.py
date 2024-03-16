from django.contrib import admin
from .models import Communication
@admin.register(Communication)
class CommunicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']
