import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

class Book(models.Model):
    #id = models.AutoField(primary_key=True)
    title_book = models.CharField("Название книги", max_length = 100)
    author_name = models.CharField("Автор", max_length = 100, default = '')
    description_book = models.CharField("описание книги", max_length = 1000)
    publication_date_book = models.DateTimeField("дата публикации")
    image_book = models.ImageField(blank = True, upload_to = 'image/', verbose_name = 'изображение')
    pdf_book = models.FileField(upload_to = 'pdf/', verbose_name = 'ссылка pdf', default = '')

    def __str__(self):
        return self.title_book

    def adminShowImage(self):
        if self.image_book:
           return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image_book.url))
        else:
            return '(Нет изображения)'
    adminShowImage.short_description = 'Изображение'
    adminShowImage.allow_tags = True

    def adminShowPdf(self):
        if self.pdf_book:
           return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.pdf_book.url))
        else:
            return '(Нет файла pdf)'
    adminShowPdf.short_description = 'файл pdf'
    adminShowPdf.allow_tags = True
    
    
    def delete(self, *args, **kwargs):
        self.pdf_book.delete()
        self.image_book.delete()
        super().delete(*args, **kwargs)
    
