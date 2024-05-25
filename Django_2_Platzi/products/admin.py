from django.contrib import admin
from .models import Products, Favorite

@admin.register(Products)
class AdminProduct(admin.ModelAdmin):
    list_display = ("id", "name", "category", "description", "price",)
    list_filter = ("category",)


@admin.register(Favorite)
class AdminFavorite(admin.ModelAdmin):
    list_display = ('user', 'product',)
    list_filter = ('user', 'product',)

