from django.contrib import admin
from .models import Category, Book


class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ["title", "author", "price", "category"]


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ["name"]


admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
