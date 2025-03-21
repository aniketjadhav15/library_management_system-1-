from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'publication_year', 'quantity']
        widgets = {
            'publication_year': forms.NumberInput(attrs={'min': 1900, 'max': 2024}),
            'quantity': forms.NumberInput(attrs={'min': 0}),
        } 