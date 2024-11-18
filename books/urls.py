from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("books/", views.BookListView.as_view(), name="books"),
    path("create/", views.BookCreateView.as_view(), name="book_create"),
    path("books/<int:pk>/update/", views.BookUpdateView.as_view(), name="book_update"),
    path("books/<int:pk>/delete/", views.BookDeleteView.as_view(), name="book_delete"),
    path("books/<int:pk>/", views.book_detail, name="book_detail"),
    path("category/", views.category, name="category"),
    path("category/<int:pk>", views.category_book, name="category_book"),
    path("search", views.book_search, name="search"),

]
