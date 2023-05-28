from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from .models import quotation, QuotationProduct

class CreateQuotationForm(forms.Form):
    quotation_number = forms.CharField(max_length=20,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Quotation Number'}))
    valid_date = forms.DateField(label="Valid Date",
                                 widget=forms.SelectDateWidget(attrs={'class': 'form-control'}))
    product_name = forms.CharField(max_length=50,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Product Name'}))
    product_description = forms.CharField(max_length=100,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Description'}))
    product_price = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.TextInput({'class': 'form-control','placeholder': 'Price'}))
    product_quantity =forms.IntegerField(min_value=0,widget=forms.NumberInput({'class': 'form-control','placeholder': 'Quantity'}))
 
class selectedQuantityForm(forms.ModelForm):
    selected_quantity = forms.IntegerField()
    class Meta:
        model = QuotationProduct
        fields =['selected_quantity']

