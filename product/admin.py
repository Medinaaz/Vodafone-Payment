from django.contrib import admin
from product.models import ProductCategory, Product, ProductImages


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'template_icon', 'modified_at')
    list_filter = ('modified_at',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'available_quantity', 'barcode', 'status', 'modified_at')
    list_filter = ('category', 'status', 'modified_at')
    search_fields = ('name', 'barcode')
    autocomplete_fields = ('category', 'tags')
    prepopulated_fields = {"slug": ("name",)}


@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'product', 'rank', 'modified_at')
    list_filter = ('modified_at',)
    search_fields = ('title',)
    autocomplete_fields = ('product',)
    prepopulated_fields = {"slug": ("title",)}
