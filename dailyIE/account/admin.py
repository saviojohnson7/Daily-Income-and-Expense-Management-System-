from django.contrib import admin

# Register your models here.

from income.models import Income
from expense.models import Expense
from expense.models import Payment


class IncomeAdmin(admin.ModelAdmin):
    list_display=['id','income','income_type','income_date','description','user']

    

class ExpenseAdmin(admin.ModelAdmin):
    list_display=['id','expense','expense_type','expense_date','description','user_id']

    
class PaymentAdmin(admin.ModelAdmin):
    list_display=['id','user','amount','razorpay_id','razorpay_payment_status','razorpay_payment_id','paid']


admin.site.register(Income,IncomeAdmin)
admin.site.register(Payment,PaymentAdmin)

