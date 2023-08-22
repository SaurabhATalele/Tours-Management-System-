from unicodedata import name
from django.shortcuts import redirect, render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Packages,Orders
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import OrderForm,PackageForm, CreateUserForm,SubmitContactForm
import random,datetime


@csrf_exempt
def home(request):
    contactform = SubmitContactForm()
    pack = Packages.objects.all()[:3]

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
                print("SAved")
                user = form.cleaned_data.get('username')
                messages.success(request,'Account was created for ' + user)

                return redirect('Login')
            else:
                print("form is not valid")
        context = {'form' : form}
        
        return render(request,'Signup.html',context)


    # return render(request,'Signup.html')


@login_required(login_url='/login')
def book_now(request,name):
    
    return render(request,'index.html')



def search_book_now(request):
    if request.method == "POST":
        
        pack = Packages.objects.filter(destination = request.POST["Place-name"])
        print(request.POST["Place-name"])
        det = request.POST
        print(pack)
        
        return render(request,'Search.html',{'package':pack,"det":det})

    return redirect('/')

@login_required(login_url='/login')
def profile_info(request):
    orders = Orders.objects.filter(username = request.user.username)
    return render(request,'Profile.html',{"orders" : orders})


@login_required(login_url='login')
def Logout(request):
    logout(request)
    return redirect('home')

@login_required(login_url="/login")
def book_now_package(request,name,num,date):

    
    price = Packages.objects.filter(pack_name = name)
    
    order = Orders.objects.create(order_id = random.randint(1,100000),
    username= request.user.username,
    people = num,
    order_date = str(datetime.datetime.now())[:10],
    cost = int(num)*int(price[0].price),
    pack_name =name,
    trip_date = date)
    order.save()
    url = "/success/"+str((int(num)*int(price[0].price)))
    return redirect(url)

def cancle_order(request,id):
    order =Orders.objects.filter(order_id = int(id))
    order.delete()
    return redirect("/profile",{"Message":"Successfully cancled the order..."})

def success(request,total):

    return render(request,"success.html",{"total":total})

def update_profile(request):


    return render(request,"Update.html")


@login_required(login_url="login")
def users(request):
    users = User.objects.all()
    staff = User.objects.filter(username = request.user.username)[0].is_staff
    if staff:
        return render(request,"users.html",{"users":users})
    else:
        return HttpResponse("ou are Not a staff")


@login_required(login_url="login")
def orders(request):
    orders = Orders.objects.all()
    staff = User.objects.filter(username = request.user.username)[0].is_staff
    if staff:
        return render(request,"orders.html",{"orders":orders})
    else:
        return HttpResponse("ou are Not a staff")


@login_required(login_url="login")
def packages(request):
    packages = Packages.objects.all()
    staff = User.objects.filter(username = request.user.username)[0].is_staff
    if staff:
        return render(request,"packages.html",{"orders":packages})
    else:
        return HttpResponse("ou are Not a staff")

        
@login_required(login_url="login")
def addpackages(request):
    form = PackageForm
    staff = User.objects.filter(username = request.user.username)[0].is_staff
    if staff:
        if request.method == "POST":
            form = PackageForm(request.POST)
            packname= request.POST["pack_name"]
            dur = request.POST["tripduration"]
            dest = request.POST["destination"]
            price = request.POST["price"]
            img = request.POST["image"]
            cat = request.POST["category"]

            pck = Packages.objects.create(pack_name =packname,tripduration = dur,destination=dest,price = price,image = img,category= cat)
            pck.save()
            return redirect("/pc")
           
            
            if form.is_valid():
                print("VAlid")
                form.save()
                return redirect("/pc")
            

        return render(request,"AddPackage.html",{"form":form})
    else:
        return HttpResponse("You are Not a staff")