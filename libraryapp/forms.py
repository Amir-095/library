from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models


class BookForm(forms.ModelForm):
    class Meta:
        model=models.Book
        fields=['name','avtor_name','isbn','izdatelstvo','description','vozrast','category','image']
        labels = {
            'name': 'Название книги',
            'avtor_name': 'Имя автора',
            'isbn':'ISBN',
            'category':'Категория',
            'image':'Фотография обложки',
            'izdatelstvo': 'Издательство',
            'description': 'Описание книги',
            'vozrast': 'Возраст'
        }
        widgets = {
            'description': forms.Textarea(attrs={'cols': 47, 'rows': 5}),
        }
##new
class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']

class StudentDOPForm(forms.ModelForm):
    class Meta:
        model=models.Student
        fields=['nomer']
##new

class IssuedBookForm(forms.Form):
    #to_field_name value will be stored when form is submitted.....__str__ method of book model will be shown there in html
    isbn2=forms.ModelChoiceField(queryset=models.Book.objects.all(),empty_label="Название и ISBN", to_field_name="isbn",label='Название и ISBN')
    nomer2=forms.ModelChoiceField(queryset=models.Student.objects.all(),empty_label="Имя и ID",to_field_name='nomer',label='Имя и ID')