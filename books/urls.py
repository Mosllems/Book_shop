from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<int:pk>/", views.book_detail, name="book_detail"),
    path("category/<int:pk>/", views.category_book, name="category_book"),

]
