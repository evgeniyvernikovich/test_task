from django.shortcuts import render
from django.views import generic
from books import models

# Create your views here.

class HomePage(generic.TemplateView):
    template_name = 'home_page.html'
    
    

# Create your views here.
