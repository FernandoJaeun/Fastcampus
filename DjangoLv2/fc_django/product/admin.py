from django.contrib import admin
from .models import Product

# Register your models here.
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stuck', 'register_date')

admin.site.register(Product, ProductAdmin)