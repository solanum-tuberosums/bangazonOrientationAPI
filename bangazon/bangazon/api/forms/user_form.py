from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    """
    This class represents an HTML form to login and authenticate users.

    ----Fields----
    - username
    - email
    - password (widget=forms.PasswordInput())
    - first_name
    - last_name

    Author: Beve Strownlee
    """

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control'}))

    class Meta:
        model = User
        help_texts = {
            'username':None,
        }
        fields = ('username', 'email', 'password', 'first_name', 'last_name',)
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': "form-control"}),
            'first_name': forms.TextInput(attrs={'class': "form-control"}),
            'last_name': forms.TextInput(attrs={'class': "form-control"}),
            }