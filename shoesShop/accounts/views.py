from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from . forms import RegisterForm ,LoginForm
from django.contrib.auth import authenticate, logout , login
from django.contrib import messages

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
    
            
            if user is not None:
                
                if user.is_active:
                    
                    login(request, user)
                    return redirect('index')
                else:
                    messages.warning(request, 'Disable Account')
            else:
                messages.warning(request,'Check Your Username and Password')
    else:
        form = LoginForm()

    return render(request,'login.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('login')

def register(request):
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            try:
                emails = User.objects.get(email=request.POST['email'])
            except User.DoesNotExist:
                emails = None

            try:
                username = User.objects.get(username = request.POST['username'])
            except User.DoesNotExist:
                username = None
            
            if username:
                messages.warning(request, 'Bu kullanıcı adı kullanılıyor')
                return redirect('register')
            
            if emails:
                messages.warning(request, 'Bu Mail kullanılıyor')
                return redirect('register')
            
            if len(request.POST['password1']) < 8:
                messages.warning(request, 'Bu Şifreniz 8 karekterden az olamaz')
                return redirect('register')
            
            if request.POST['password1'] != request.POST['password2']:
                messages.warning(request, 'Bu Şifre girişleriniz aynı olmalı')
                return redirect('register')
            
            if form.is_valid():
                form.save()             
                return redirect('login')
            
        else:
            form = RegisterForm()

        return render(request,'register.html',{'form':form})