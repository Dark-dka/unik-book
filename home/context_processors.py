from home.models import Book
from django.db.models import Q

from .forms import SearchForm

def search_form(request):
    search_post = request.GET.get('search')
    if search_post:
        posts = Book.objects.filter(Q(title__icontains=search_post))
    else:
        # If not searched, return default posts
        posts = Book.objects.all().order_by("-id")
    return {'results': posts}

