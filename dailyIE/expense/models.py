from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Expense(models.Model):
    expense=models.IntegerField()
    expense_type=models.CharField(max_length=30)
    expense_date=models.DateField()
    description=models.TextField(max_length=30)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table='Expense'


from django import forms

class ExpenseForm(forms.ModelForm):
    class Meta:
        model=Expense
        fields='__all__'



class Payment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.FloatField()
    razorpay_id=models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_status=models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_id=models.CharField(max_length=100,blank=True,null=True)
    paid=models.BooleanField(default=False)
