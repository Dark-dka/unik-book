from django.urls import path

from .views import download_pdf, index, books, book_list, search

app_name = "home"

urlpatterns = [
    path('', index, name='index'),
    path('books/', book_list, name='book_list'),
    path('search/', search, name='search'),
    path('books/<int:book_id>/download/', download_pdf, name='download_pdf'),
    path('books/<slug:category_slug>/', book_list, name='book_list_by_category'),
]
