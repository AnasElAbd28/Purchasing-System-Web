from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from PurchaseOrder.models import purchaseOrder, PurchaseOrderProduct 

class CreatePurchaseOrderForm(forms.Form):
    PurchaseOrder_number = forms.CharField(max_length=20,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Purchase Order Number'}))
    quotation_Number = forms.CharField(max_length=20,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Quotation Reference Number'}))
            
    valid_date = forms.DateField(label="Valid Date",
                                 widget=forms.SelectDateWidget(attrs={'class': 'form-control'}))
    sellername = forms.CharField(max_length=100,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Seller Name'}))

    selleraddress = forms.CharField(max_length=255,
                                widget=forms.TextInput({
                                    'class': 'form-control',
                                    'placeholder': 'SellerAddress'}))
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
        model = PurchaseOrderProduct
        fields =['selected_quantity']
