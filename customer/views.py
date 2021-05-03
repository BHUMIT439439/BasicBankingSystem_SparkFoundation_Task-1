from django.shortcuts import render,redirect
from .models import Customer
from django.db.models import Q
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')

def information(request):
    if 'search' in request.GET:
        query = request.GET['search']
        customer_list = Customer.objects.all().filter(Q(name__icontains = query))
        return render(request,'information.html',{'customer_list':customer_list})
    else:
        customer_list = Customer.objects.all()
        return render(request,'information.html',{'customer_list':customer_list})

def transfer_money(request):
    if request.method == 'POST':
        acc1 = request.POST['acc1']
        acc2 = request.POST['acc2']
        amount = request.POST['amount']
        c1 = Customer.objects.all().filter(account_no=acc1).first()
        c2 = Customer.objects.all().filter(account_no=acc2).first()
        if(c1.balance >= int(amount)):
            b1 = c1.balance - int(amount)  
            b2 = c2.balance + int(amount)
            c1.balance = b1
            c1.save()
            c2.balance = b2
            c2.save()
            messages.success(request,'Successfully transfer is done!')
            return render(request,'transfer_money.html')
        else:
            messages.success(request,'Not sufficient balance')
            return render(request,'transfer_money.html')
    return render(request,'transfer_money.html')




def contact(request):
    return render(request,'contact.html')