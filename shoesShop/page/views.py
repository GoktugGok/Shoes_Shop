from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def news(request):
    return render(request,'news.html')

def testimonial(request):
    return render(request,'testimonial.html')


