from django.shortcuts import render
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
