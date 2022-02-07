

from unicodedata import name
from django.urls import path

from books.models import Review
from . import views


urlpatterns = [
    path('',views.BookListView.as_view(), name="book.all"),
    path('book/<int:pk>',views.BookDetailView.as_view(), name="book.show"),
    path('<int:id>/review',views.review ,name="book.review"),
    path('author/<str:author>books', views.author , name='author.books')
]


