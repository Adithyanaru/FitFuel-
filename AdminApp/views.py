from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from AdminApp.models import *
from WepApp.models import *
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
# Create your views here.
def dashboard(request):
    return render(request,'Dashboard.html')
def add_catagory(request):
    return render(request,'Add_Catagory.html')
def view_catagory(request):
    category=Category.objects.all()
    return render(request,'View_Catagory.html',{'category':category})

def add_product(request):
    category=Category.objects.all()
    return render(request,'Add_Product.html',{'category':category})
def view_product(request):
    product=ProductDb.objects.all()
    return render(request,'View_Product.html',{'product':product})

def login_page(request):
    return render(request,'Login_Page.html')
def  admin_login(request):
    uname=request.POST.get('username')
    pswd=request.POST.get('password')
    if User.objects.filter(username__contains=uname).exists():
        user=authenticate(username=uname,password=pswd)
        if user is not None:
            # login(request,user)
           request.session['username'] = uname
           request.session['password'] = pswd
           return redirect(dashboard)
        else:
            return redirect(login_page)
    else:
        return redirect(login_page)


def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(login_page)

def save_category(request):
    if request.method =='POST':
        cat_name = request.POST.get('cname')
        cat_desc = request.POST.get('cdesc')
        cat_image = request.FILES['cimage']
        obj = Category(Name=cat_name,Description=cat_desc,Image=cat_image)
        obj.save()

        return redirect(add_catagory)
def delete_category(request,cat_id):
    cat=Category.objects.filter(id=cat_id)
    cat.delete()
    return redirect(view_catagory)
def edit_category(request,cat_id):
    category=Category.objects.get(id=cat_id)
    return render(request,'Edit_Category.html',{'category':category})
def update_category(request,catg_id):
    if request.method=='POST':
        cat_name=request.POST.get('cname')
        cat_desc=request.POST.get('cdesc')
        try:
            cat_image=request.FILES['cimage']
            fs=FileSystemStorage()
            file=fs.save(cat_image.name,cat_image)
        except MultiValueDictKeyError:
            file=Category.objects.get(id=catg_id).Image
        Category.objects.filter(id=catg_id).update(Name=cat_name,Description=cat_desc,Image=file)
        return redirect(view_catagory)
def save_product(request):
    if request.method=='POST':
        pro_name=request.POST.get('pname')
        pro_cat=request.POST.get('pcat')
        pro_prize=request.POST.get('pprize')
        pro_desc=request.POST.get('pdesc')
        pro_img=request.FILES['pimage']
        obj=ProductDb(Pro_Name=pro_name,Pro_Category=pro_cat,Pro_Prize=pro_prize, 
        Pro_Description=pro_desc,Pro_Image=pro_img) 
        obj.save() 
        return redirect(add_product)


def delete_product(request,p_id):
    pro=ProductDb.objects.filter(id=p_id)
    pro.delete()
    return redirect(view_product)
def edit_product(request,pro_id):
    product=ProductDb.objects.get(id=pro_id)
    return render(request,'Edit_Product.html',{'product':product})
def update_product(request,pro_id):
    if request.method=='POST':
        pro_name=request.POST.get('pname')
        pro_cat=request.POST.get('pcat')
        pro_prize=request.POST.get('pprize')
        pro_desc=request.POST.get('pdesc')
        try:
            pro_img=request.FILES['pimage']
            fs=FileSystemStorage()
            file=fs.save(pro_img.name,pro_img)
        except MultiValueDictKeyError:
            file=ProductDb.objects.get(id=pro_id).Pro_Image
            ProductDb.objects.filter(id=pro_id).update(Pro_Name=pro_name,Pro_Category=pro_cat,
            Pro_Prize=pro_prize,Pro_Description=pro_desc,Pro_Image=file)
        return redirect(view_product)
def contct_details(request):
    con_details=ContactDb.objects.all()
    return render(request,'Contact_Details.html',{'con_details':con_details})        