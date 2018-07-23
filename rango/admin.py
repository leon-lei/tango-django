from django.contrib import admin
from .models import Category, Page, UserProfile


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'slug', 'views', 'likes')


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'views', 'category', 'url')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)