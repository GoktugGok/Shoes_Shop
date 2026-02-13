from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from shoes.models import Category
from . forms import RegisterForm ,LoginForm
from django.contrib.auth import authenticate, logout , login
from django.contrib import messages

# Create your views here.

def user_login(request):
    all_categories = Category.objects.filter(level=0)
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

    return render(request,'login.html',{'form':form,'all_categories':all_categories})

def user_logout(request):
    logout(request)
    return redirect('login')

def register(request):
    all_categories = Category.objects.filter(level=0)

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Kullanıcı adı kontrolü
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Bu kullanıcı adı kullanılıyor')
            return redirect('register')

        # Email kontrolü
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'Bu mail kullanılıyor')
            return redirect('register')

        # Şifre uzunluk kontrolü
        if len(password1) < 8:
            messages.warning(request, 'Şifre 8 karakterden az olamaz')
            return redirect('register')

        # Şifre eşleşme kontrolü
        if password1 != password2:
            messages.warning(request, 'Şifreler aynı olmalı')
            return redirect('register')

        # Form geçerliyse kaydet
        if form.is_valid():
            form.save()
            messages.success(request, "Hesabınız oluşturuldu")
            return redirect('login')

    else:
        form = RegisterForm()

    return render(request, 'register.html', {
        'form': form,
        'all_categories': all_categories
    })