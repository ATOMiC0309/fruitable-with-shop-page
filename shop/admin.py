from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Product


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug', 'parent', 'get_image')
    list_display_links = ('pk', 'name')

    def get_image(self, category):
        if category.image:
            url = category.image.url
        else:
            url = "https://freshtechproduce.com/wp-content/uploads/2019/05/FT-Image-Not-Available.jpg"
        return mark_safe(f'<img src="{url}" width="75px" style="border-radius: 15px; border: 2px solid gray">')

    get_image.short_description = 'Rasmi'
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity', 'category', 'get_image')
    list_display_links = ('name',)
    list_editable = ('price', 'quantity', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')

    def get_image(self, product):
        if product.image:
            url = product.image.url
        else:
            url = "https://freshtechproduce.com/wp-content/uploads/2019/05/FT-Image-Not-Available.jpg"
        return mark_safe(f'<img src="{url}" width="75px" style="border-radius: 15px;">')

    get_image.short_description = 'Rasmi'

    prepopulated_fields = {'slug': ('name', 'quantity')}
