from django.http import HttpResponse 
from django.shortcuts import render , redirect
from django.contrib import messages
from .form import ImageForm, orderMediForm, bidForm #,RegisterForm 
from .models import Image, order, bid

from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import render, HttpResponseRedirect
from .form import signupForm, updateProfileForm, updateAdminProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        fm = signupForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Account created successfully!!")
            fm = signupForm()
    else:
        fm = signupForm()
    return render(request, 'register.html', {'form': fm})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Login Successfully!!")
                    return HttpResponseRedirect('/home/')
        else:
            fm = AuthenticationForm()
        return render(request, 'login.html', {'form': fm})
    else:
        return HttpResponseRedirect('/home/')


def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                fm = updateAdminProfileForm(
                    data=request.POST, instance=request.user)
                users = User.objects.all()
            else:
                fm = updateProfileForm(
                    data=request.POST, instance=request.user)
                users = None
            if fm.is_valid():
                fm.save()
                messages.success(request, "Profile Updated!!")
        else:
            if request.user.is_superuser == True:
                fm = updateAdminProfileForm(instance=request.user)
                users = User.objects.all()
            else:
                fm = updateProfileForm(instance=request.user)
                users = None
        return render(request, 'home.html', {'form': fm, 'users': users})
        #return render(request, 'enroll/profile.html', {'name': request.user, 'form': fm, 'users': users})
    else:
        return HttpResponseRedirect('/login/')


def user_logout(request):
    logout(request)
    print("LOGGED OUT")
    return HttpResponseRedirect('/home/')


def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, "Password Changed successfully")
                #return HttpResponseRedirect('/profile/')
                return HttpResponseRedirect('/home/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'home.html', {'form': fm})
        #return render(request, 'enroll/changepass.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')


def user_detail(request, id):
    if request.user.is_authenticated:
        user = User.objects.get(pk=id)
        fm = updateAdminProfileForm(instance=user)
        return render(request, 'home.html', {'form': fm})
        #return render(request, 'enroll/userdetail.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')


def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html')

# def UserRegistration(request):
#     if request.method == 'POST':
#             s=RegisterForm(request.POST)
            
#             first_name=request.POST.get('first_name')
#             last_name=request.POST.get('last_name')
#             email=request.POST.get('email')
#             phone=request.POST.get('phone')
            
#             password1=request.POST.get('password1')
#             password2=request.POST.get('password2')
#             gender=request.POST.get('gender')
#             if s.is_valid():
#                 if password1==password2:
#                     s.save()
#                     messages.success(request,'Registered Successfully')
#                     return HttpResponse("Registered Successfully")
#                 else:
#                     messages.success(request,'Password Mismatch')
#                     s=RegisterForm()
#                     return render(request,'register.html',{'form':s})
#             # if Register.objects.filter(email=s.email).exists():
#             #     messages.info(request,'Email taken')
#             #     return redirect('register')
#             # else:
#             #     s.save()
#             #     messages.success(request,'Registered successfully')
#             #     return render(request,'login.html')
#             else:
#                 s=RegisterForm()
            
#     else:
#         return render(request,'register.html',{'form':RegisterForm()})


# def login(request):
#     if request.method=="POST":
#         try:
#             Userdetails=Register.objects.get(email=request.POST['email'],password1=request.POST['password1'])
#             print("Username=",Userdetails)
#             request.session['email']=Userdetails.email
#             return redirect('home')
#         except Register.DoesNotExist as e:
#             messages.success(request,'Email / Password Invalid')
#     return render(request,'login.html')


# def order(request):
#     return render(request,'order.html')
    
def uploadpic(request):
    if request.method == "POST": 
        form=ImageForm(data=request.POST,files=request.FILES) 
        if form.is_valid(): 
            form.save() 
            obj=form.instance 
            return render(request,"uploadpic.html",{"obj":obj}) 
    else: 
        form=ImageForm() 
        img=Image.objects.all() 
    return render(request,"uploadpic.html",{"img":img,"form":form})

def ordermedi(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = orderMediForm(request.POST,files=request.FILES)
            if fm.is_valid():
                fm.save()
                req = fm.instance
                messages.success(request, "Request Sent!!")
                return render(request, 'session.html', {"req":req})
        else:
            fm = orderMediForm()
        return render(request, 'ordermedi.html', {'form': fm})
    messages.info(request, "Please Login First!!")
    return HttpResponseRedirect('/login/')

def session(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = bidForm(request.POST)
            if fm.is_valid():
                fm.save()
                bid = fm.instance
                messages.success(request, "Bid Sent!!")
                return render(request, 'success.html', {"bid":bid})
        orders = order.objects.all()
        
        return render(request, 'session.html', {'orders': orders, 'fm': bidForm()})

    messages.info(request, "Please Login First!!")
    return HttpResponseRedirect('/login/')

def success(request):
    return render(request, 'success.html')

def bidp(request):
    bids = bid.objects.all()
    return render(request, 'bids.html', {'bids':bids})
