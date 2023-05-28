from django.urls import path , re_path
from . import views

urlpatterns = [

    path('listPOs/', views.listPOs, name='listPOs'),
    path('view_PurchaseOrders/', views.view_PurchaseOrders , name = 'view_PurchaseOrders'),
    path('financeOrders/<str:pk>/',views.financeOrders, name='financeOrders')
]