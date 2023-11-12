from django.shortcuts import render,redirect
# get_object_or_404
# from .utils import send_otp
# import pyotp
# from datetime import datetime
from django.contrib.auth.models import User


# Create your views here.
def home1(request):
    context={'bal':get_balance(request),'incb':get_income(request),'expb':get_expense(request)}
    
    return render(request,'home.html',context)

from django.contrib.auth.forms import UserCreationForm

def reg1(request):
    if request.method=="POST":
        f=UserCreationForm(request.POST)
        f.save()
        return redirect('/reg')
    
    else:
        q=UserCreationForm
        s={'k':q}
        return render(request,'form.html',s)


from .models import LoginForm
from django.contrib.auth import authenticate,login,logout
# from django.contrib import messages as m


def login12(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            # send_otp(request)
            request.session['username']=username # session id is stored in user.id. id is stored in uid
            login(request,user)
            return redirect('/')
        else:
            f=LoginForm
            context={'d':f}
            return render(request,'login.html',context)
    else:
        f=LoginForm
        context={'d':f}
        return render(request,'login.html',context)
    
# from django.contrib.auth import authenticate, login
# from django.shortcuts import redirect
# from django.http import HttpResponse
# from datetime import datetime, timedelta
# import pyotp

# def otp_view(request):
#     if request.method == 'POST':
#         try:
#             otp = request.POST['otp']
#             username = request.session['username']
#             password = request.POST.get('password')
#             otp_secret_key = request.session['otp_secret_key']
#             otp_valid_until = request.session['otp_valid_date']

#             # Check if all required keys are present
#             if otp_secret_key and otp_valid_until and otp and username:
#                 valid_until = datetime.fromisoformat(otp_valid_until)

#                 # Check if OTP is still valid
#                 if valid_until > datetime.utcnow():
#                     totp = pyotp.TOTP(otp_secret_key, interval=60)
                    
#                     # Verify OTP
#                     if totp.verify(otp):
#                         user = authenticate(request, username=username, password=password)

#                         # Check if the user is authenticated and login
#                         if user is not None:
#                             login(request, user)

#                             # Clean up session data
#                             del request.session['otp_secret_key']
#                             del request.session['otp_valid_date']

#                             return redirect('/')
#                         else:
#                             return HttpResponse("Invalid credentials")
#                     else:
#                         return HttpResponse("Invalid OTP")
#                 else:
#                     return HttpResponse("OTP has expired")
#             else:
#                 return HttpResponse("Incomplete data in session")
#         except KeyError as e:
#             return HttpResponse(f"KeyError: {e}")
#     else:
#         return HttpResponse("Invalid request method")

    
# from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from datetime import datetime
# import pyotp

# def otp_view(request):
#     if request.method == 'POST':
#         try:
#             otp = request.POST['otp']
#             username = request.session['username']
#             otp_secret_key = request.session['otp_secret_key']
#             otp_valid_until = request.session['otp_valid_date']

#             # Check if all required keys are present
#             if otp_secret_key and otp_valid_until and otp and username:
#                 valid_until = datetime.fromisoformat(otp_valid_until)

#                 # Check if OTP is still valid
#                 if valid_until > datetime.utcnow():
#                     totp = pyotp.TOTP(otp_secret_key, interval=60)

#                     # Verify OTP
#                     if totp.verify(otp):
#                         user = authenticate(request, username=username)

#                         # Check if the user is authenticated and login
#                         if user is not None:
#                             login(request, user)

#                             # Clean up session data
#                             del request.session['otp_secret_key']
#                             del request.session['otp_valid_date']

#                             return redirect('/')
#                         else:
#                             return HttpResponse("Authentication failed")
#                     else:
#                         return HttpResponse("Invalid OTP")
#                 else:
#                     return HttpResponse("OTP has expired")
#             else:
#                 return HttpResponse("Incomplete data in session")
#         except KeyError as e:
#             return HttpResponse(f"KeyError: {e}")

#     return render(request, 'otp.html')

    


    
# def otp_view(request):
#     if request.method=='POST':
#         otp=request.POST['otp']
#         username=request.session['username']
#         otp_secret_key=request.session['otp_secret_key']
#         otp_valid_until=request.session['otp_valid_date']

#         if otp_secret_key and otp_valid_until is not None:
#             valid_until=datetime.fromisoformat(otp_valid_until)

#             if valid_until>datetime.now():
#                 totp=pyotp.TOTP(otp_secret_key,interval=60)
#                 if totp.verify(otp):
#                     user=authenticate(request,username=username)
                    
#                     login(request,user)

#                     del request.session['otp_secret_key']
#                     del request.session['otp_valid_date']
#                     return redirect('/')



#     return render (request,'otp.html')




    

def logout12(request):
    logout(request)
    return redirect('/')

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


def get_income(request):
    uid=request.session.get('uid')  
    incl=Income.objects.filter(user=uid)
    

    total_income=0
    for i in incl:
        total_income=total_income + i.income
      
    return total_income 


def get_expense(request):
    uid=request.session.get('uid')  
    
    expl=Expense.objects.filter(user=uid)

    total_expense=0
    for i in expl:
        total_expense=total_expense + i.expense

    return  total_expense


from django.contrib.auth.models import User
from .models import UserForm, UserForm1
def edit1(request):
    uid=request.session.get('uid')
    u=User.objects.get(id=uid)       # object means the username
    if request.method=='POST':
        f=UserForm(request.POST,instance=u)
        f.save()
        return redirect('/')
    
    else:

        f=UserForm(instance=u)
        context={'edit2':f}
        return render(request,'updateuser.html',context)

# create model for edit profile, go to models

def change_name(request):
     uid=request.session.get('uid')
     u=User.objects.get(id=uid)       # object means the username
     if request.method=='POST':
        f=UserForm1(request.POST,instance=u)
        f.save()
        return redirect('/')
    
     else:

        f=UserForm1(instance=u)
        context={'edit3':f}
        return render(request,'upusername.html',context)
     


def about1(request):
    return render(request,'about.html')
    


