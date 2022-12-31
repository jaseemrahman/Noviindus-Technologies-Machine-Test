#Import from the core django
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
#Import from the third library
#Import from local app/library
from item.models import Customer
from accounts.forms import RegistreationForm

#customer list
def customer_list(request):
    customers=Customer.objects.all()  
    context={'customers':customers,}   
    return render(request,'accounts/customer_list.html',context) 
#logout    
def logout_user(request):
    logout(request)
    messages.success(request, f'Logged out successfully!')
    return redirect('/')
#login
def user_login(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password =  request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('/')
        else:
            print("else")
            messages.info(request, f'account not exit please sign in')
    form=AuthenticationForm()
    context = {'form': form,}
    return render(request,'accounts/login.html',context)    
#signup
def user_signup(request):
    if request.method == 'POST':
        print(request.POST)
        form = RegistreationForm(request.POST)
        if form.is_valid():
            usr = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            user=User.objects.create(username=usr,first_name=first_name,last_name=last_name,email=email)  
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = RegistreationForm()
    context = {'form': form}
    return render(request,'accounts/signup.html',context)        


    

