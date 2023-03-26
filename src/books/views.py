from django.shortcuts import render
from . import forms, models
from django.views import generic

class CreateBook(generic.CreateView):
    model = models.Book
    form_class = forms.BookForm
    template_name = 'book_create.html'

class DeleteBook(generic.DeleteView):
    model = models.Book
    template_name = 'book_delete.html'

class UpdateBook(generic.UpdateView): 
    model = models.Book
    form_class = forms.BookForm
    template_name = 'book_update.html'

class ShowBook(generic.DetailView):
    model = models.Book
    template_name = 'book_detail.html'

class ListBooks(generic.ListView):
    model = models.Book
    template_name = 'book_list.html'