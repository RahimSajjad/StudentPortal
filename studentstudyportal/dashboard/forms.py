from django import forms
from django.db.models import fields
from django.db.models.enums import Choices
from django.forms import widgets
from . models import *
from django.contrib.auth.forms import User, UserCreationForm


class NoteForm(forms.ModelForm):
    class Meta:
        # Notes sob field ekhane meta class die bind kora hoiche
        model = Notes
        fields = ['title', 'description']

# Home work forms
# Date form


class DateInput(forms.DateInput):
    input_type = 'date'


class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homeworks
        # inputdate
        widgets = {'due': DateInput()}
        fields = ['subject', 'title', 'description', 'due', 'is_finished']


# Commonform input field
class CommonForms(forms.Form):
    text = forms.CharField(max_length=1000, label="Enter your Search: ")
    pass

# Todo form


class TodoForm(forms.ModelForm):
    class Meta:
        # Notes sob field ekhane meta class die bind kora hoiche
        model = Todo
        fields = ['title', 'description', 'is_finished']


# conversion form
class ConversionForm(forms.Form):
    CHOICES = [('length', 'Length'), ('mass', 'Mass')]
    measurement = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)


class ConversionLengthForm(forms.Form):
    CHOICES = [('yard', 'Yard'), ('foot', 'Foot')]
    input = forms.CharField(required=False, label=False, widget=forms.TextInput(
        attrs={'type': 'number', 'placeholder': 'Enter the Number'}

    ))
    measure1 = forms.CharField(
        label='', widget=forms.Select(choices=CHOICES)
    )
    measure2 = forms.CharField(
        label='', widget=forms.Select(choices=CHOICES)
    )

# Mass


class ConversionMassForm(forms.Form):
    CHOICES = [('pound', 'Pound'), ('kilogram', 'Kilogram')]
    input = forms.CharField(required=False, label=False, widget=forms.TextInput(
        attrs={'type': 'number', 'placeholder': 'Enter the Number'}

    ))
    measure1 = forms.CharField(
        label='', widget=forms.Select(choices=CHOICES)
    )
    measure2 = forms.CharField(
        label='', widget=forms.Select(choices=CHOICES)
    )


# User Registration form
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']
