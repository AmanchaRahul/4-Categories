from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login

from .models import *


# Create your views here.

def demo(request):
   
    return render(request,"base.html")



def login_page(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        print(email)
        print(password)

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            # Authenticate the user
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                # If user is authenticated, log them in
                login(request, user)
                return redirect("/demo/")
            else:
                # If authentication fails, display error message
                messages.error(request, "Invalid Password!")
                return redirect("/login/")
        else:
            # If email doesn't exist in the database, display error message
            messages.error(request, "Invalid Email!")
            return redirect("/login/")

    return render(request, "loginpage.html")

def register_page(request):
    if request.method=="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        
        print(first_name)
        print(last_name)
        print(username)
        print(email)
        print(password)
        
        user=User.objects.filter(email=email)
        if user.exists():
            messages.info(request,'Email already exists!')
            return redirect("/register/")
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            
        )
        
        user.set_password(password)
        user.save()
        
        messages.info(request,"Account Created Successfully!")
        return redirect("/register/")
        
        
    return render(request,"registerpage.html")



def cinema_page(request):
    return render(request,"cinema.html")


def ai_page(request):
    return render(request,"ai.html")




def cricket_page(request):
    return render(request,"cricket.html")





def gold_page(request):
    if request.method=="POST":
        data=request.POST
        date=data.get("date")
        trade_description=data.get("trade_description")
        trade_image=request.FILES.get("trade_image")
        print(date)
        print(trade_description)
        print(trade_image)
        
        
        Goldentries.objects.create(
            date=date,
            trade_description=trade_description,
            trade_image=trade_image
        )
        return redirect("/gold/")
    queryset=Goldentries.objects.all()
    context={"trades":queryset}
    return render(request,"gold.html",context)


def delete_page(request,id):
    queryset=Goldentries.objects.get(id=id)
    queryset.delete()
    return redirect("/gold/")

def update_page(request,id):
    queryset=Goldentries.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        date=data.get("date")
        trade_description=data.get("trade_description")
        trade_image=request.FILES.get("trade_image")
        print(date)
        print(trade_description)
        print(trade_image)
        
       
        queryset.trade_description=trade_description,
        
        if date:
             queryset.date=date
             queryset.save()
            
        if trade_image:
            queryset.trade_image=trade_image
            
            queryset.save()
        
        return redirect("/gold/")
   
    context={"trades":queryset}
    return render(request,"update_trade.html",context)

