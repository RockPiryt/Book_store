from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Book

# Create your views here.

def index(request):
    all_books = Book.objects.all()
    return render(request, "book_outlet/index.html", {
        "html_all_books":all_books,
    })

def book_information(request, id):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, pk=id)
    return render(request, "book_outlet/book_detail.html",{
        "html_title": book.title,
        "html_author": book.author,
        "html_rating": book.rating,
        "html_is_bestseller": book.is_bestselling,
    })