from django.shortcuts import render

from . import forms, models
from django.views import generic

class CreateAuthor(generic.CreateView):
    model = models.Author
    form_class = forms.BookForm
    template_name = 'aut_create.html'

class DeleteAuthor(generic.DeleteView):
    model = models.Author
    template_name = 'aut_delete.html'

class UpdateAuthor(generic.UpdateView): 
    model = models.Author
    form_class = forms.BookForm
    template_name = 'aut_update.html'

class ShowAuthor(generic.DetailView):
    model = models.Author
    template_name = 'aut_detail.html'

class ListAuthors(generic.ListView):
    model = models.Author
    template_name = 'aut_list.html'