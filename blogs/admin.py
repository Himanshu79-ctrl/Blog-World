from django.contrib import admin
from .models import Category, Blog, Comment
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'status', 'author', 'is_featured')
    search_fields = ('title', 'category__category_name', 'author__username')
    list_editable = ( 'is_featured',)


admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)