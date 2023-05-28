from django.contrib import admin
from app.models import Seller, Staff, Finance, Manager
from quotation.models import quotation, QuotationProduct
from PurchaseOrder.models import purchaseOrder, PurchaseOrderProduct


admin.site.register(Seller)
admin.site.register(Staff)
admin.site.register(Finance)
admin.site.register(Manager)
admin.site.register(quotation)
admin.site.register(QuotationProduct)
admin.site.register(purchaseOrder)
admin.site.register(PurchaseOrderProduct)

