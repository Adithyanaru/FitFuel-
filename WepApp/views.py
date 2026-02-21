from django.shortcuts import render,redirect
from AdminApp.models import *

# Create your views here.
def home(request):
    categories=Category.objects.all()
    our_products=ProductDb.objects.all()
    return render(request,'Home.html',{'categories':categories,'our_products':our_products})
    
def shop(request):
    products=ProductDb.objects.all()
    available=Category.objects.all()
    return render(request,'Shop.html',{'products':products,
                                    'available':available})

def filtered_product(request,cat_name):
    available=Category.objects.all()
    category=Category.objects.all()
    filtered_product=ProductDb.objects.filter(Pro_Category=cat_name)
    return render(request,'Filtered_product.html',{'filtered_product':filtered_product,
                                                    'available':available,
                                                    'category':category,
                                                    'cat_name':cat_name})


def single_page(request,product_id):
    single_product=ProductDb.objects.get(id=product_id)
    category=Category.objects.all()
    return render(request,'Single_page.html',{'single_product':single_product,
                                            'category':category,
                                            'product_id':product_id})
