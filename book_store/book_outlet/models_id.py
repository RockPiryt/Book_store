from typing import Iterable, Optional
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False)#Harry Potter 1 ->harry-potter-1

    def get_absolute_url(self):
        return reverse("book-info", args=[self.id])
    
    def save(self, *args, **kwargs):
        self.slug =  slugify(self.title)
        super().save(*args, **kwargs)
    

    def __str__(self):
        return f"Book {self.title}, rating:{self.rating}"