from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages

from .models import *
from .forms import *




# Create your views here.

def index(request):
    return render (request,'index.html')

def com(request):
    return render (request,'Commerce.html')

def comp(request):
    return render (request,'Computer.html')

def maths(request):
    return render (request,'Maths.html')

def stati(request):
    return render (request,'Stati.html')

def mng(request):
    return render (request,'mng.html')


def login(request):
    if request.method=='POST':
        Name=request.POST['username']
        Password=request.POST['password']
        user=auth.authenticate(username=Name,password=Password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('schoolapp:New')
        else:
            messages.info(request,"Invalid Login")
            return redirect('schoolapp:login') 
    return render(request,"Login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
    
def Register(request):
    if request.method=='POST':
        user_n=request.POST['Uname']
        Pass=request.POST['Pass']
        Cpass=request.POST['Cpass']
        
        if Pass==Cpass:
            if User.objects.filter(username=user_n).exists():
                messages.info(request,"Username already Taken")
                return redirect('schoolapp:Register')
            else:
                user1=User.objects.create_user(username=user_n,password=Pass)
                user1.save()
                return redirect('schoolapp:login')
        else:
            messages.info(request,"Password not Matching")
            return redirect('schoolapp:Register')
    return render(request,"Regi.html")


    



def New(request):
    return render(request,'New.html')

def person_create_view(request):
    form = MyForm()
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,"Order confirmed")
            return redirect('schoolapp:person_add')
    return render(request, 'home.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(UserInform, pk=pk)
    form = MyForm(instance=person)
    if request.method == 'POST':
        form = MyForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('schoolapp:person_change', pk=pk)
    return render(request, 'home.html', {'form': form})


# AJAX
def load(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).all()
    return render(request, 'course_dropdown_list_options.html', {'courses': courses})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)
    
    


    