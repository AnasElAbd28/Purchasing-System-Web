from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from quotation.forms import CreateQuotationForm, selectedQuantityForm
from PurchaseOrder.forms import CreatePurchaseOrderForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, Group
from app.models import Seller, Finance
from quotation.models import quotation, QuotationProduct
from PurchaseOrder.models import purchaseOrder, PurchaseOrderProduct
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.

#Iskanth and Emad
@login_required
def create_POID(request):
    current_user = Finance.objects.get(Finance_user=request.user)
    thispurchaseorder = purchaseOrder(finance_ID=current_user)
    thispurchaseorder.save()
    pk=thispurchaseorder.PO_ID
    return redirect(reverse(create_PurchaseOrder,args=[pk]))

#Emad
def create_PurchaseOrder(request,pk):


    purchaseorder_form = CreatePurchaseOrderForm(request.POST) 

    if request.method == 'POST':                       
        if purchaseorder_form.is_valid() :
            purchaseOrder.objects.filter(PO_ID=pk).update(Purchaseorder_Number=purchaseorder_form.cleaned_data['PurchaseOrder_number'],
                                                          Quotation_Number=purchaseorder_form.cleaned_data['quotation_Number'],
                                                            Valid_Date=purchaseorder_form.cleaned_data['valid_date'],
                                                            Seller_Name=purchaseorder_form.cleaned_data['sellername'],
                                                            Seller_Address=purchaseorder_form.cleaned_data['selleraddress'])

            product= PurchaseOrderProduct(name=purchaseorder_form.cleaned_data['product_name'],
                                        description=purchaseorder_form.cleaned_data['product_description'],
                                        price=purchaseorder_form.cleaned_data['product_price'],
                                        proposed_quantity=purchaseorder_form.cleaned_data['product_quantity'],
                                        Total_Price=purchaseorder_form.cleaned_data['product_price'] * purchaseorder_form.cleaned_data['product_quantity'],
                                        purchaseorder_id=purchaseOrder.objects.get(PO_ID=pk))
            product.save()
    
    products=PurchaseOrderProduct.objects.all().filter(purchaseorder_id=pk)
    totalPrice=0

    for product in products:
        totalPrice+=product.Total_Price
    context = {'purchaseorderform':purchaseorder_form,
                'products':products,
                'totalPrice':totalPrice}
    return render(request,'app/create_PO.html',context)

#Emad
def view_PurchaseOrders(request):
    finance=Finance.objects.get(Finance_user=request.user)
    purchaseOrder.objects.all().filter(Purchaseorder_Number= None).delete()
    purchaseorder_list = purchaseOrder.objects.all().filter(finance_ID=finance)
    context ={'purchaseorder_list': purchaseorder_list,}
    return render(request,'app/View_PO.html',context)

#Emad
def financeOrders(request, pk):
  products = PurchaseOrderProduct.objects.all().filter(purchaseorder_id=pk) 
  total = 0
  for p in products:
    total+= p.Total_Price
  p = purchaseOrder.objects.get(PO_ID=pk)
  finance = Finance.objects.get(Finance_user=request.user)

  context = {'products': products,
             'PurchaseOrder': p,
             'finance': finance,
             'total': total}
  return render(request, 'app/View_POdetails.html',context)


#Iskanth
def listPOs(request):

    purchasorders = purchaseOrder.objects.all()


    return render(request, 'app/View_POReport.html', {'purchaseorders': purchasorders} )