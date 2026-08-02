from django.contrib import admin

from .models import (
    Attribute,
    Category,
    Product,
    ProductAttributeValue,
    ProductImage,
)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ('image', 'alt_text', 'is_primary', 'sort_order')


class ProductAttributeValueInline(admin.TabularInline):
    model = ProductAttributeValue
    extra = 1
    autocomplete_fields = ('attribute',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'is_active', 'sort_order')
    list_filter = ('is_active',)
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('is_active', 'sort_order')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
        'category',
        'price',
        'is_active',
        'is_featured',
        'created_at',
    )
    list_filter = ('is_active', 'is_featured', 'category')
    search_fields = ('name', 'sku', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('is_active', 'is_featured', 'price')
    autocomplete_fields = ('category',)
    inlines = (ProductImageInline, ProductAttributeValueInline)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': (
                'category',
                'name',
                'slug',
                'sku',
                'short_description',
                'description',
            ),
        }),
        ('Pricing', {
            'fields': ('price', 'compare_at_price'),
        }),
        ('Status', {
            'fields': ('is_active', 'is_featured', 'created_at', 'updated_at'),
        }),
    )


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'attribute_type', 'is_filterable', 'sort_order')
    list_filter = ('attribute_type', 'is_filterable')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('is_filterable', 'sort_order')


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'is_primary', 'sort_order', 'created_at')
    list_filter = ('is_primary',)
    search_fields = ('product__name', 'alt_text')
    autocomplete_fields = ('product',)
