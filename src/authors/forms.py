from django import forms
from . import models

class BookForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = '__all__'
    
    
    