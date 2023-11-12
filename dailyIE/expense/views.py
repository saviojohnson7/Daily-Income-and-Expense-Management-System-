from django.shortcuts import render,redirect
from .models import ExpenseForm,Expense
from django.contrib.auth.models import User

# Create your views here.
def addexpense1(request):
    uid=request.session.get('uid')

    if request.method=='POST':
        expense=request.POST.get('expense')
        if get_balance(request) > int(expense): 
              #coverting the string into int
              expense_type=request.POST.get('expense_type')
              expense=request.POST.get('expense')
              expense_type=request.POST.get('expense_type')
              expense_date=request.POST.get('expense_date')
              description=request.POST.get('description')
              inc=Expense()
              inc.expense=expense
              inc.expense_type=expense_type
              inc.expense_date=expense_date
              inc.description=description
              inc.user=User.objects.get(id=uid)
              inc.save()
              return redirect('/')
        
        else:
            f=ExpenseForm
            y={'k':f,'exp_msg':'Warning : In-sufficient balance !!!'}
            return render(request,"addexpense1.html",y)

    else:
        f=ExpenseForm
        y={'k':f}
        return render(request,"addexpense1.html",y)
    
    # if request.method=='POST':
    #     f=ExpenseForm(request.POST)
    #     f.save()
    #     return redirect('/')

    # else:
    #     f=ExpenseForm
    #     o={'w':f}
    #     return render(request,'addexpense1.html',o)
    
from .models import Expense

def data2(request):
    uid=request.session.get('uid')
    elist=Expense.objects.filter(user=uid)       #object is the manager for emp and for all the data of all users. user will be assigned uid i.e user=uid
    expt=set()
    for i in elist:
        expt.add(i.expense_type)

    d={'s':elist,'expt':expt}                    # s has all the data
    return render(request,'db3.html',d) 


    # elist=Expense.objects.all()   #object is the manager for emp and "all" means retrieving all fields

    # ue={'u':elist}
    # return render(request,'db3.html',ue)


def delete_E(request,id):
    x=Expense.objects.get(id=id)
    x.delete()
    return redirect('/expenselist')


def edit_E(request,id):
    me=Expense.objects.get(id=id)
    if request.method=='POST':
        f=ExpenseForm(request.POST,instance=me)  
        f.save()
        return redirect('/')
    
    else:
        fe=ExpenseForm(instance=me)
        contexts={'s':fe}
        return render(request,"addexpense1.html",contexts)
    

    #django modelform is a helper model that create a html page by using model
    # we pass the context in the render, our key goes through the context4


def expense_search2(request):
    uid=request.session.get('uid')
    srch=request.POST.get('srch')
    expl=Expense.objects.filter(user=uid,description__icontains=srch)
    context={'s':expl}
    return render(request,"db3.html",context)


def sort_data(request,ext):
    uid=request.session.get('uid')
    elist=Expense.objects.filter(user=uid)   
    expt=set()
    for i in elist:
        expt.add(i.expense_type)

    elist=Expense.objects.filter(user=uid,expense_type=ext) # to filter category wise

    d={'s':elist,'expt':expt}                # s has all the data
    return render(request,'db3.html',d) 


from income.models import Income
from expense.models import Expense
def get_balance(request):
    uid=request.session.get('uid')  
    incl=Income.objects.filter(user=uid)
    expl=Expense.objects.filter(user=uid)

    total_income=0
    total_expense=0

    for i in incl:
        total_income=total_income + i.income
      

    for i in expl:
        total_expense=total_expense + i.expense

    return total_income - total_expense

from .models import Payment

import razorpay
from django.conf import settings

def payment1(request):
    user=request.user
    client = razorpay.Client(auth=(settings.RAZOR_KEY_ID,settings.RAZOR_KEY_SECRET))

    DATA={'amount':50000,'currency':'INR','receipt':'receipt#1'}
    payment_response=client.order.create(data=DATA)
    print(payment_response)
    id=payment_response['id']
    status=payment_response['status']
    if status == 'created':
        payment=Payment(
            user=user,
            razorpay_id=id,
            razorpay_payment_status=status
            
        )
        payment.save()
    return render(request,'payment.html')

# def get(self,request):
#         totalitem=0
#         wishitem=0
#         if request.user.is_authenticated:
#             totalitem=len(Cart.objects.filter(user=request.user))
#             wishitem=len(Wishlist.objects.filter(user=request.user))
#         user=request.user
#         add=Customer.objects.filter(user=user)
#         cart_items=Cart.objects.filter(user=user)
#         famount=0
#         for p in cart_items:
#             value = p.quantity * p.product.discounted_price
#             famount=famount+value
#         totalamount=famount+40
#         razoramount=int(totalamount*100)
#         client =razorpay.Client(auth=(settings.RAZOR_KEY_ID,settings.RAZOR_KEY_SECRET))
#         data ={'amount':razoramount,'currency':'INR','receipt':'order_rcptid_12'}
#         payment_response=client.order.create(data=data)
#         print(payment_response)
#         # {'id': 'order_MjJ3eHbbvGINOk', 'entity': 'order', 'amount': 49000, 'amount_paid': 0, 'amount_due': 49000, 'currency': 'INR', 'receipt': 'order_rcptid_12', 'offer_id': None, 'status': 'created', 'attempts': 0, 'notes': [], 'created_at': 1696242726}
#         order_id =payment_response['id']
#         order_status =payment_response['status']
       
#         if order_status =='created':
#             payment = Payment(
#                 user=user,
#                 amount=totalamount,
#                 razorpay_order_id=order_id,
#                 razorpay_payment_status=order_status
#             )
#             payment.save()
#         return render(request,'checkout.html',locals())
 

    