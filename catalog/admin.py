from django.contrib import admin
from .models import Brand, Product, Store, PriceHistory


# Inline form for PriceHistory
class PriceHistoryInline(admin.TabularInline):
    model = PriceHistory
    extra = 1  # Number of empty forms to display
    fields = [
        'parent_product',
        'location',
        'price',
        'quantity',
    ]  # Customize fields as needed


# Custom admin class for Product
class ProductAdmin(admin.ModelAdmin):
    inlines = [PriceHistoryInline]
    list_display = (
        'product_brand',
        'product_name',
        'product_status'
    )  # Customize displayed fields


class PriceHistoryAdmin(admin.ModelAdmin):
    list_display = (
        'parent_product',
        'price',
        'date_created'
    )  # Customize displayed fields


# Register models
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)
admin.site.register(Store)
admin.site.register(PriceHistory, PriceHistoryAdmin)
