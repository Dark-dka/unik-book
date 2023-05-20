from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q

from .models import Book, Category

def index(request):
    search_post = request.GET.get('search')
    if search_post:
        posts = Book.objects.filter(title__icontains=search_post)
    else:
        # If not searched, return default posts
        posts = Book.objects.all().order_by("-id")

    categories = Category.objects.all()
    context = {
        "categories": categories,
    }
    return render(request, 'index.html', context)

def book_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    books = Book.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        books = books.filter(category=category)

    return render(request, 'catproducts.html', {'category': category, 'categories': categories, 'books': books})

def books(request):
    return render(request, 'catproducts.html')

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    pdf_url = book.pdf.url
    return render(request, 'book_detail.html', {'book': book, 'pdf_url': pdf_url})


def download_pdf(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    with open(book.pdf.path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(book.pdf.name)
        return response


def search(request):
    query = request.GET.get('search')
    results = Book.objects.filter(Q(title__icontains=query))
    return render(request, 'search.html', {'results': results})
