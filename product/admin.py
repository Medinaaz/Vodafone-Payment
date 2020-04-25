from django.contrib import admin
from product.models import ProductCategory, Product, ProductImages, PropertyOption, ProductProperty


class InlineProductImagesAdmin(admin.TabularInline):
    model = ProductImages
    prepopulated_fields = {"slug": ("title",)}


class InlineProductPropertyAdmin(admin.TabularInline):
    model = ProductProperty
    autocomplete_fields = ("option",)


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'template_icon', 'modified_at')
    list_filter = ('modified_at',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [InlineProductImagesAdmin, InlineProductPropertyAdmin]
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


@admin.register(PropertyOption)
class PropertyOptionAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(ProductProperty)
class ProductPropertyAdmin(admin.ModelAdmin):
    list_display = ("pk", "option", "value", "is_main_property", "product")
    search_fields = ("value",)
    autocomplete_fields = ("product", "option")
