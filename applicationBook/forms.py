from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title_book', 'author_name', 'image_book', 'pdf_book', 'publication_date_book', 'description_book')
        #list_display = ('title_book', 'author_name', 'pdf_book', 'adminShowImage',)