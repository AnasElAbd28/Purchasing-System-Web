from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .forms import CreateQuotationForm, selectedQuantityForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, Group
from .models import Seller, quotation, QuotationProduct
from django.contrib.auth.decorators import login_required
from django.urls import reverse

#Seller - Adam
def sview_Quotation(request):
    seller=Seller.objects.get(seller_user=request.user)
    quotation.objects.all().filter(Quotation_Number= None).delete()
    quotation_list = quotation.objects.all().filter(seller_ID=seller)
    status =[]
    for q in quotation_list:
        if q.status == True:
            status.append("Selected")
        else: 
            status.append("Not Selected")
    context ={'quotation_list': quotation_list,
              'status': status}
    return render(request,'app/sellerviewquotation.html',context)

def slquotation(request, pk):
  products = QuotationProduct.objects.all().filter(quotation_id=pk) 
  total = 0
  for p in products:
    total+= p.Total_Price
  q = quotation.objects.get(Quotation_ID=pk)
  seller = Seller.objects.get(seller_user=request.user)

  context = {'products': products,
             'quotation': q,
             'seller': seller,
             'total': total}
  return render(request, 'app/sellerquotation.html',context)


@login_required
def create_quotationID(request):
    current_user = Seller.objects.get(seller_user=request.user)
    thisquotation = quotation(seller_ID=current_user)
    thisquotation.save()
    pk=thisquotation.Quotation_ID
    return redirect(reverse(create_quotation,args=[pk]))

def create_quotation(request,pk):


    quotation_form = CreateQuotationForm(request.POST) 

    if request.method == 'POST':                       
        if quotation_form.is_valid() :
            quotation.objects.filter(Quotation_ID=pk).update(Quotation_Number=quotation_form.cleaned_data['quotation_number'],
                                                            Valid_Date=quotation_form.cleaned_data['valid_date'])

            product= QuotationProduct(name=quotation_form.cleaned_data['product_name'],
                                        description=quotation_form.cleaned_data['product_description'],
                                        price=quotation_form.cleaned_data['product_price'],
                                        proposed_quantity=quotation_form.cleaned_data['product_quantity'],
                                        Total_Price=quotation_form.cleaned_data['product_price'] * quotation_form.cleaned_data['product_quantity'],
                                        quotation_id=quotation.objects.get(Quotation_ID=pk))
            product.save()
    
    products=QuotationProduct.objects.all().filter(quotation_id=pk)
    totalPrice=0

    for product in products:
        totalPrice+=product.Total_Price
    context = {'quotationform':quotation_form,
                'products':products,
                'totalPrice':totalPrice}
    return render(request,'app/create_quotation.html',context)



# Staff -Anas
product_list = QuotationProduct.objects.all()
quotation_list = quotation.objects.all()
quotation_list_selected = quotation.objects.filter(status=True)


def view_Quotation(request):
    status =[]
    for q in quotation_list:
        if q.status == True:
            status.append("Selected")
        else: 
            status.append("Not Selected")
    return render(request,'app/viewqcon.html',{'quotation_list': quotation_list})

def view_sQuotation(request):
    status =[]
    for q in quotation_list_selected:
        if q.status == True:
            status.append("Selected")
        else: 
            status.append("Not Selected")
    return render(request,'app/viewqsec.html', {'quotation_list': quotation_list_selected})

def lquotation(request, pk):
    products = QuotationProduct.objects.all().filter(quotation_id=pk)
    q = quotation.objects.get(Quotation_ID=pk)
    # seller = Seller.objects.get(seller_user=request.user)

    if request.method == 'POST':
        for product in products:
            selected_quantity = request.POST.get('selected_quantity_{}'.format(product.Product_ID))
            product.selected_quantity = selected_quantity
            product.save()
        return HttpResponseRedirect(reverse('menu'))
    context = {'data':products,
                'quotation':q,
                }
    return render(request, 'app/quotation.html',context)

# def update_status(request, pk):
#     # Get the object that you want to update
#     qs = quotation.objects.all().filter(Quotation_ID=pk)
#     if request.method == 'POST':
#         # Update the boolean value
#         qs.status = not qs.status
#         qs.save()
#         # Redirect the user or display a confirmation message
#         return redirect('/success/')
#     return render(request, 'viewqcon.html', {'qs': qs})

# def update_status(request):
#     if request.method == 'POST':
#         task_id = request.POST['Quotation_ID']
#         task = quotation.objects.get(id=task_id)
#         task.status = True
#         task.save()
#         return redirect('vieWqcon')
#     else:
#         return render(request, 'vieWqcon.html')

def confirm_changes(request):
    return render(request, 'app/confirm_change.html')

# def confirm_changes(request):
#     if request.method == 'POST':
#         qs = quotation.objects.get(Quotation_ID=id)
#         qs.status = request.POST.get('change_value')
#         qs.save()
#         return redirect('confirm_change')
#     return render(request, 'viewqcon.html')

def confirm_change(request):
    if request.method == 'POST':
        quotation_id = request.POST.get('quotation_id')
        change_value = request.POST.get('change_value')
        quotation_obj = quotation.objects.get(Quotation_ID=quotation_id)
        quotation_obj.status = change_value
        quotation_obj.save()
        return HttpResponseRedirect(reverse('menu'))
    return render(request, 'app/viewqcon.html')

#Iskanth
def listQ(request):
   
    quotations = quotation.objects.all()
    
    return render(request, 'app/quotationR.html', {'quotations': quotations} )


