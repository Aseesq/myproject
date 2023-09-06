from django.shortcuts import render,redirect
from .models import *
# Create your views here.
 
def home(request):
    dat=product.objects.all()
    cat=category.objects.all()
    
   
    data={
        'dat': dat,
        'cat':cat,
    }
    return render(request,"index.html",data)
def fashion(request):
    dat=product.objects.all()
    cat=category.objects.all()
   
    data={
        'dat': dat,
        'cat':cat,
    }
    return render(request,"fashion.html", data)
def sigup(request):
    if request.method =="POST":
        user=request.POST.get("user")
        name=request.POST.get("name")
        email=request.POST.get("Email")
        pwd=request.POST.get("pwd")
        contact=request.POST.get("number")
        dat=siginup(username=user,name=name,email=email,password=pwd,contact=contact)
        dat.save()
        return redirect("/index/")
    else:
        pass

    
    return render(request,"register.html")
