from django import forms
from .models import Author, Publisher, Category, Books  # Use Books model here

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['catName']

class BookForm(forms.ModelForm):
    class Meta:
        model = Books  # Updated to Books model
        fields = ['title', 'price', 'language', 'fileFormat', 'fileSize', 'publisher']


# Custom user form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

