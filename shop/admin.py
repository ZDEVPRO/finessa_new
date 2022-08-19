from django.contrib import admin
from shop.models import Product, Images


class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'image_tag']
    readonly_fields = ('image_tag',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProductImageInline]


admin.site.register(Product, ProductAdmin)
