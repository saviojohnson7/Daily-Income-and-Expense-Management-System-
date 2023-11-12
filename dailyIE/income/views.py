from django.shortcuts import render,redirect
from .models import IncomeForm,Income
from django.contrib.auth.models import User
# Create your views here.


def addincome2(request):
    uid=request.session.get('uid')
    if request.method=='POST':
        income=request.POST.get('income')
        income_type=request.POST.get('income_type')
        income_date=request.POST.get('income_date')
        description=request.POST.get('description')
        incs=Income()
        incs.income=income
        incs.income_type=income_type
        incs.income_date=income_date
        incs.description=description
        incs.user=User.objects.get(id=uid)
        incs.save()
        return redirect('/')

    else:
        f=IncomeForm
        y={'h':f}
        return render(request,"addincome1.html",y)
    


# def data1(request):
#     uid=request.session.get('uid')
#     elist=Income.objects.filter(user=uid)   #object is the manager for emp and for all the data of all users. user will be assigned uid i.e user=uid
#     d={'s':elist}
#     return render(request,'dbb.html',d)

def data1(request):
    uid=request.session.get('uid')
    elist=Income.objects.filter(user=uid)       #object is the manager for emp and for all the data of all users. user will be assigned uid i.e user=uid
    ixpt=set()
    for i in elist:
        ixpt.add(i.income_type)

    d={'s':elist,'ixpt':ixpt}                    # s has all the data
    return render(request,'dbb.html',d) 


def delete_emp(request,id):
    x=Income.objects.get(id=id)
    x.delete()
    return redirect('/incomelist')


def edit1(request,id):
    m=Income.objects.get(id=id)
    if request.method=='POST':
        f=IncomeForm(request.POST,instance=m)  
        f.save()
        return redirect('/incomelist')
    
    else:
        f=IncomeForm(instance=m)
        context={'s':f}
        return render(request,"addincome1.html",context)
    



def income_search2(request):
    uid=request.session.get('uid')
    srch=request.POST.get('srchs')
    expl=Income.objects.filter(user=uid,description__icontains=srch)
    context={'s':expl}
    return render(request,"dbb.html",context)


def sort_data1(request,ixt):
    uid=request.session.get('uid')
    elist=Income.objects.filter(user=uid)   
    ixpt=set()
    for i in elist:
        ixpt.add(i.income_type)

    elist=Income.objects.filter(user=uid,income_type=ixt) # to filter category wise

    d={'s':elist,'ixpt':ixpt}                # s has all the data
    return render(request,'dbb.html',d) 