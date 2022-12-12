from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from random import randrange
from django.conf import settings
from django.core.mail import send_mail
from mainApp.models import Buyer,mashalachicken,tavadhosa

def index(request):
	return render(request,'index.html')
def loginPage(Request):
    if (Request.method == "POST"):
        username = Request.POST.get("username")
        password = Request.POST.get("password")
        user = authenticate(username=username, password=password)
        if (user is not None):
            login(Request, user)
            if (user.is_superuser):
                return redirect("/admin")
            else:
                return HttpResponse("Signed In")
        else:
        	return HttpResponse("Error")
   
    return render(Request, "login.html")
# Create your views here.
def signupPage(Request):
    if (Request.method == "POST"):
        p = Request.POST.get("password")
        cp = Request.POST.get("cpassword")
        if (p == cp):
            b = Buyer()
            b.name = Request.POST.get("name")
            b.username = Request.POST.get("username")
            b.phone = Request.POST.get("phone")
            b.email = Request.POST.get("email")
            user = User(username=b.username, email=b.email)
            if (user):
                user.set_password(p)
                user.save()
                b.save()
                return redirect("/")
            else:
                messages.error(Request, "Username Already Taken!!!!!!")
        else:
            messages.error(
                Request, "Password And Confirm Password Doesn't Matched!!!")
    return render(Request, "signup.html")
def AboutUs(request):
    return render(request,'AboutUs.html')
def order(request):
    return render(request,"order.html")
def Payment(request):
    return render(request,"Payment.html")
def detail(request):
    data = mashalachicken.objects.all()
    return render(request,"detail.html",{"data":data})
def detail2(request):
    data = tavadhosa.objects.all()
    return render(request,"detail2.html",{"data":data})
def cod(request):
    return render(request,"cod.html")