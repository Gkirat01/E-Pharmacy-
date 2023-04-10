from django.contrib import admin
# Register your models here.

from .models import Image, order

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['caption', 'image']

@admin.register(order)
class orderAdmin(admin.ModelAdmin):
    list_display = ['oid', 'created_at', 'name', 'address', 'medi1', 'quantity1', 'medi2', 'quantity2', 'medi3', 'quantity3', 'prescription', 'status']