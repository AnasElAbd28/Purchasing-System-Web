from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .forms import RegisterSellerForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, Group
from .models import Seller


from django.contrib.auth.decorators import login_required

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        return(redirect('/menu'))
    else:
        return render(
            request,
            'app/index.html',
            {
                'title':'Home Page',
                'year': datetime.now().year,
            }
        )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'Purchasing  System',
            'message':'This application helps manage the process of purchasing .',
            'year':datetime.now().year,
        }
    )

@login_required
def menu(request):
    check_employee = request.user.groups.filter(name='employee').exists()
    check_seller = request.user.groups.filter(name='Seller').exists
    check_staff = request.user.groups.filter(name='Staff').exists()
    check_finance = request.user.groups.filter(name='Finance').exists()
    check_manager = request.user.groups.filter(name='Manager').exists()
    context = {
            'title':'Main Menu',
            'is_employee': check_employee,
            'is_seller' : check_seller,
            'is_staff': check_staff,
            'is_finance':check_finance,
            'is_manager':check_manager,
            'year':datetime.now().year,
        }
    context['user'] = request.user

    return render(request,'app/menu.html',context)

def register_seller(request):

    if request.method == 'POST':
        form = RegisterSellerForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            group = Group.objects.get(name='Seller')
            user.groups.set([group])
            user.save()
            seller = Seller(
                seller_user=user,
                seller_name=form.cleaned_data['seller_name'],
                seller_email=form.cleaned_data['seller_email'],
                seller_address=form.cleaned_data['seller_address'],
                seller_phone=form.cleaned_data['seller_phone']
            )
            seller.save()
            return HttpResponseRedirect('/login')
    else:
        form=RegisterSellerForm()

    context = {'form':form}
    return render(request,'app/register_seller.html',context)
