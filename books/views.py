from django.shortcuts import render, get_object_or_404

from .models import Book, Category


def home(request):
    categories = Category.objects.all()
    books = Book.objects.all()
    return render(request, "home.html", {
        "categories": categories,
        "books": books,
    })


def category(request,):
    categories = Category.objects.all()
    return render(request, "_base.html", {
        "categories": categories,
    })


def category_book(request, pk):
    categories = Category.objects.all()
    category = get_object_or_404(Category, pk=pk)
    books = Book.objects.filter(category=category)
    return render(request, "_base.html", {
        "categories": categories,
        "current_category": category,
        "books": books,
    })


def book_detail(request, pk):
    books = get_object_or_404(Book, pk=pk)
    return render(request, "books/book_detail.html", {
        "books": books,
    })

