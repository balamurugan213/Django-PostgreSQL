from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView, DetailView
from .models import Book


class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'


class BookDetailView(DetailView):  # new
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'


class ArticleListView(ListView):

    model = Book
    # paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
