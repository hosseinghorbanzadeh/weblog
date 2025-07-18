from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from accounts.forms import CustomAuthenticationForm,CustomUserCreationForm
from django.contrib import messages

# Create your views here.

from django.contrib.auth import views as auth_views

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomAuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                login(request, form.get_user())
                return redirect('/')
            else:
                messages.error(request, 'invalid username or password')
        else:
            form = CustomAuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})
    return redirect('/')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'sucssedfuly')
                return redirect("/")
        form=CustomUserCreationForm()
        context={"form":form}
        return render(request,'accounts/signup.html',context)
    else:
        return redirect('/')
    

