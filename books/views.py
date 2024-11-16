from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Book, Category


def home(request):
    categories = Category.objects.all()
    books = Book.objects.all()
    return render(request, "home.html", {
        "categories": categories,
        "books": books,
    })


class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
    ordering = ["-datetime_created"]
    template_name = "books/book_list.html"
    context_object_name = "books"


def category(request,):
    categories = Category.objects.all()
    return render(request, "_base.html", {
        "categories": categories,
    })


def category_book(request, pk):
    categories = Category.objects.all()
    category = get_object_or_404(Category, pk=pk)
    books = Book.objects.filter(category=category)
    paginator = Paginator(books, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "books/book_category.html", {
        "categories": categories,
        "current_category": category,
        "books": books,
        "page_obj": page_obj
    })


def book_detail(request, pk):
    books = get_object_or_404(Book, pk=pk)
    return render(request, "books/book_detail.html", {
        "books": books,
    })


class BookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Book
    fields = ["title", "description", "author", "price", "category", "image"]
    template_name = "books/book_create.html"
    success_url = reverse_lazy("books")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Book
    fields = ["title", "author", "description", "price", "image"]
    template_name = "books/book_update.html"
    success_url = reverse_lazy("books")

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = "books/book_delete.html"
    success_url = reverse_lazy("books")