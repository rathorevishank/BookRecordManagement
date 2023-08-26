from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')
    search_fields = ('title', 'author')
    list_filter = ['price']
    list_editable = ['price', 'author']
    list_display_links = ['title']  # Error arising here , Set 'title' as the display link

# Register your models here.
admin.site.register(Book, BookAdmin)
