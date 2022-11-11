from unicodedata import name
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from .models import Packages
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import OrderForm,PackageForm, CreateUserForm,SubmitContactForm
import logging


@csrf_exempt
def home(request):
    contactform = SubmitContactForm()
    pack = Packages.objects.all()

    if request.method == "POST":

            submitted= SubmitContactForm(request.POST)
            
            if submitted.is_valid():
                submitted.save()

    return render(request,'index.html',{'pack':pack,'contact':contactform})


def Login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            print('logged in...')
            return redirect('home')
            
        else:
            messages.info(request,'Username or Password is incorrect')

        context = {}

    return render(request,'Login.html')
    # return render(request,'Login.html')



def Signup(request):
    print("Encounter")
    if request.user.is_authenticated:
        return redirect ('home')
    else:
        form = CreateUserForm()
        
        if request.method == 'POST':
            
            form = CreateUserForm(request.POST)
            
            # print(form)
            if form.is_valid():
                
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account was created for ' + user)

                return redirect('Login')
        context = {'form' : form}
        
        return render(request,'Signup.html',context)


    # return render(request,'Signup.html')


@login_required(login_url='/login')
def book_now(request,name):
        
    return render(request,'index.html')


@login_required(login_url='/login')
def profile_info(request):
    return render(request,'Profile.html')


@login_required(login_url='login')
def Logout(request):
    logout(request)
    return redirect('home')



