from django import forms

from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields="__all__"


class ClientForm(forms.ModelForm):
    class Meta:
        model=Client
        fields="__all__"


class StaffForm(forms.ModelForm):
    class Meta:
        model=Staff
        fields="__all__"


class CartForm(forms.ModelForm):
    class Meta:
        model=Cart
        fields=("service","client","date")
