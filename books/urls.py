from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("books/", views.BookListView.as_view(), name="books"),
    path("books/<int:pk>/", views.book_detail, name="book_detail"),
    path("category/", views.category, name="category"),
    path("category/<int:pk>", views.category_book, name="category_book"),
]
