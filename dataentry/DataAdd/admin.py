#DataAdd/admin.py
from django.contrib import admin

# Register your models here.
# admin.py

from django.contrib import admin
from .models import ProductData

@admin.register(ProductData)
class ProductDataAdmin(admin.ModelAdmin):
    list_display = ('sr_no', 'date', 'product_name', 'customer_name', 'l1_price', 'gst_percent', 'gross_cost_value', 'usd')
    search_fields = ('product_name', 'customer_name')
    list_filter = ('date',)

