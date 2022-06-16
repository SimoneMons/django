from django import forms
from .models import ContacIfo, Book

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ContacIfo
        fields = ('first_name', 'last_name', 'message')


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"


