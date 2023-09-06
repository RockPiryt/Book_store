from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<slug:aslug>", views.book_information, name="book-info"),
]
