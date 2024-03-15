from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib import messages
from shoes.models import Category , ShoesDetail,Comment

# Create your views here.

def index(request):
    all_categories = Category.objects.filter(level=0)
    top_shoes = ShoesDetail.objects.order_by('-reviewsCount')[:6]  # reviewsCount'a göre azalan sırayla ilk 6 ayakkabıyı al
    comments = Comment.objects.order_by('-create_at')[:3]
    for comment in comments:
        print(comment)
    context = {
        'top_shoes': top_shoes,
        'all_categories':all_categories,
        'comments':comments
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def news(request):
    return render(request,'news.html')

def testimonial(request):
    return render(request,'testimonial.html')


