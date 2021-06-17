from django.urls import path
from . import views

urlpatterns = [
    path("", views.upload_file, name = 'home'),
    path("addBook/", views.addBook, name = 'addBook'),
    path('home/<int:pk>/', views.delete_book, name='delete_book'),
]

