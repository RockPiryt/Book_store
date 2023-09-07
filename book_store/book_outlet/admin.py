from django.contrib import admin
from .models import Book, Author, Address, Country

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",) # show only filed, can't edit value (Change book option), can't use with prepopulated!!!!
    prepopulated_fields = {"slug":("title",)}# prepopulated field slug with slugify title (Add new book option)
    list_filter = ("author", "rating",) # filter data by column name
    list_display = ("title", "author",)

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)
