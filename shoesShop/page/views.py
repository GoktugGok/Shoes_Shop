from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib import messages
from shoes.models import Category , ShoesDetail,Comment
from .models import Communication
from django.http import HttpResponseRedirect

from django.db.models import Avg

# Create your views here.

def index(request):
    url = request.META.get('HTTP_REFERER')
    user = request.user
    all_categories = Category.objects.filter(level=0)
    top_shoes = ShoesDetail.objects.order_by('-reviewsCount')[:6]
    comments = Comment.objects.order_by('-create_at')[:3]
    average_rating = Comment.objects.aggregate(Avg('rate'))['rate__avg'] or 0
    average_rating = round(average_rating, 1)

    if request.method == "POST":
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        phone = request.POST.get("Phone")
        message = request.POST.get("Massage")

        if not request.POST['Name'] or not request.POST['Email'] or not request.POST['Phone'] or not request.POST['Massage']:
                messages.warning(request, "Mesaj Gonderebilmek icin boş alan birakmayin")
                return HttpResponseRedirect(url)
        
        pushMessage = Communication.objects.create(name=name,email=email,phone=phone,message=message)

        if pushMessage:
            messages.success(request, "Mesajınız Gonderildi")
            return HttpResponseRedirect(url)
        else:
            messages.warning(request, "Mesajınız Gonderilmedi")

    for comment in comments:
        print(comment)
    context = {
        'top_shoes': top_shoes,
        'all_categories':all_categories,
        'comments':comments,
        'average_rating': average_rating,
        'total_reviews': Comment.objects.count(),
        'user':user
    }
    return render(request,'index.html',context)



