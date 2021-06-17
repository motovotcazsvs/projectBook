from django.contrib import admin

from .models import Book

class BookAdmin(admin.ModelAdmin):
    fields = ['title_book', 'author_name', 'image_book', 'pdf_book', 'description_book', 'publication_date_book',]
    list_display = ('title_book', 'author_name', 'pdf_book', 'adminShowImage',)
 
admin.site.register(Book, BookAdmin)

#admin.site.register(Book)