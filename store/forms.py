from django import forms
from django.contrib.auth.forms import UserCreationForm

from store.models import *


class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = (
            "name", "email", "NumberOfRooms", "ApartmentMeters", "Budget", "service", "address", "city", "state",
            "zipcode")


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email']
        # The labels attribute is optional. It is used to define the labels of the form fields created
