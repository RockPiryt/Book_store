from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.db.models import Avg, Max, Min

from .models import Book

# Create your views here.

def index(request):
    all_books = Book.objects.all().order_by("-title")
    num_books = all_books.count()
    avg_rating = all_books.aggregate(Avg("rating"), Min("rating")) #rating__avg, rating__min
    return render(request, "book_outlet/index.html", {
        "html_all_books":all_books,
        "html_total_books": num_books,
        "html_average_rating": avg_rating,
    })

def book_information(request, aslug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, slug=aslug)
    return render(request, "book_outlet/book_detail.html",{
        "html_title": book.title,
        "html_author": book.author,
        "html_rating": book.rating,
        "html_is_bestseller": book.is_bestselling,
    })