"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from app.models import Seller 
class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Username'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))



class RegisterSellerForm(forms.Form):
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
    seller_name =forms.CharField(max_length=30,
                                widget=forms.TextInput({
                                    'class': 'form-control',
                                    'placeholder': 'Name'}))
    seller_email = forms.EmailField(label=_("Email"),
                                    widget=forms.TextInput({
                                    'class': 'form-control',
                                    'placeholder': 'Name'})
                                    )
    seller_address =forms.CharField(max_length=255,
                                widget=forms.TextInput({
                                    'class': 'form-control',
                                    'placeholder': 'Name'}))
    seller_phone =forms.CharField(max_length=30,
                                widget=forms.TextInput({
                                    'class': 'form-control',
                                    'placeholder': 'Name'}))
                           