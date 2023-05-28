from django.urls import path , re_path
from . import views

urlpatterns= [
    path('view_Quotation/', views.view_Quotation , name = 'vieWqcon'),
    path('view_sQuotation/', views.view_sQuotation , name = 'viewqsec'),
    path('quotation/<str:pk>/' , views.lquotation, name='q'),
    # path('update_status/', views.update_status, name='update_status'),
    path('confirm_change/', views.confirm_change, name='confirm_change'),
    path('listQ/' , views.listQ, name='listQ'),
]