from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator
from PIL import Image

# Create your views here.
def book_list(request):
    book_list = Book.objects.all()
    book_name = request.GET.get('book_name')

    if(book_name != '' and book_name is not None):
        book_list = book_list.filter(name__icontains=book_name)
    
    paginator = Paginator(book_list, 10)
    page = request.GET.get('page')
    book_list = paginator.get_page(page)

    return render(request, 'book/book_list.html', {'book_list': book_list})