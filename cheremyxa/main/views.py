from django.urls import reverse
from django.shortcuts import render,redirect
from .models import *
from .forms import Product_K , Product_B , Product_C
from django.db.models import Q 
#from django.db.models.functions import Lower

def main_h(request):
    return render(request, 'maket_html\main.html')

def krasn(request):
    search_query = request.GET.get('query','')
    if search_query:
        products = Product_K.objects.filter(Q(name__iregex=search_query)| 
                                            Q(price__iregex=search_query)|
                                            Q(weight__iregex=search_query))
    else:
        products = Product_K.objects.all()
    
    return render(request, 'maket_html/krasnoznam.html', {'products_k': products})

def bulvar(request):
    search_query = request.GET.get('query','')
    if search_query:
        products = Product_B.objects.filter(Q(name__iregex=search_query)| 
                                            Q(price__iregex=search_query)|
                                            Q(weight__iregex=search_query))
    else:
        products = Product_B.objects.all()
    return render(request, 'maket_html/bulvar.html', {'products_b': products})

def cherema(request):
    search_query = request.GET.get('query','')
    if search_query:
        products = Product_C.objects.filter(Q(name__iregex=search_query)| 
                                            Q(price__iregex=search_query)|
                                            Q(weight__iregex=search_query))
    else:
        products = Product_C.objects.all()
    return render(request, 'maket_html/cherema.html', {'products_c': products})











