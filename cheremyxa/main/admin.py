from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Product_K)
@admin.register(Product_B)
@admin.register(Product_C)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight', 'price','composition','image')
    search_fields = ('name',)

admin.site.site_title = "MENU"
admin.site.site_header = "MENU"