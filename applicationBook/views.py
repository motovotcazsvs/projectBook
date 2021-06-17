
#from .models import *

from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from .forms import BookForm
from .models import Book
from django.http import HttpResponseRedirect

class Home(TemplateView):
    template_name = 'home.html'

"""
def addBook(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'applicationBook/addBook.html', context)
"""

def upload_file(request): 
    objects = Book.objects.all()
    return render(request, 'applicationBook/home.html', context={'cnt': objects})

def addBook(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm() 
    return render(request, 'applicationBook/addBook.html', {'form': form})

def delete_book(request, pk):
    if request.method == 'POST':
        b = Book.objects.get(pk = pk)
        b.delete()
    return redirect('home')

"""
def upload(request):
    objects1 = Book.objects.id(0)
    return render(request, 'applicationBook/home.html', context={'objects1': objects1})
    """

