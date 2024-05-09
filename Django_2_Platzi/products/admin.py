from django.contrib import admin
from .models import Products

# admin.site.register(Products)
@admin.register(Products)
class AdminProduct(admin.ModelAdmin):
    list_display = ("id", "name", "category", "description", "price",)
    list_filter = ("category",)

    
