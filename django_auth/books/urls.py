from django.urls import path
from .views import ArticleListView, BookDetailView, BookListView


urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<uuid:pk>', BookDetailView.as_view(), name='book_detail'),
    path('listd', ArticleListView.as_view(), name='article-list'),
]
