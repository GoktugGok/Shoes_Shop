from django.shortcuts import render ,redirect
from . models import Shoes, Category, Tag ,ShopBag,PayDetails
from myorder.models import UserOrder
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse 
from django.db.models import Q

def gallery_list(request, category_slug=None,tag_slug=None):

    categories = Category.objects.all()
    if category_slug != None:
        category_page = get_object_or_404(Category, slug=category_slug)
        shoes_all = Shoes.objects.filter(category = category_page)
    else:
        shoes_all = Shoes.objects.all().order_by('-created')

    print(categories)
    context = {
         'shoes_all':shoes_all,
         'categories':categories
     }
    return render(request,'gallery.html',context)

def product_detail(request,product_id):
    product = Shoes.objects.get(id = product_id)
    user = request.user.id

    shoesC = Shoes.objects.filter(shoesC = product.shoesC)

    if request.method == "POST":
        user = request.user
        name = request.POST["shoesName"]
        if "shoesNumber" in request.POST:
            number = request.POST["shoesNumber"]
        else:
            messages.warning(request, 'Lütfen bir ayakkabı numarası seçmeden önce formu göndermeyi deneyin.')
            return redirect('product',product_id)
        
        new_product_Bag = ShopBag.objects.create(users = user,productB = name,number = number) 
        return redirect('cart',user.id)

    context = {
        'product': product,
        'shoesC': shoesC
    }
    return render(request,'product.html',context)

@login_required(login_url='/login/')
def cart_products(request,user_id):
    products = ShopBag.objects.filter(users__id = user_id) # kullanıcının sepete ekledikleri kullanıcı ismi, ürün ismi, number 

    total_price = 0
    shoe = []
    for product in products:
        shoes = Shoes.objects.filter(name = product.productB,numbers__name=product.number)  # ürün bilgilerini almak için
        
        for shoe_obj in shoes:
            print(product.number)
            # Her bir ayakkabı için veri yapısı oluştur
            total_price += shoe_obj.price
            shoe_data = {
                'shoe_info': shoe_obj,
                'product': product,

            }
            # Veri yapısını dizinize ekleyin
            shoe.append(shoe_data)

    Delivery_Cost = 150
    total_prices = total_price
    if total_prices < 5000:
        total_prices += Delivery_Cost
        Total = total_prices
    else:
        Delivery_Cost = 'free'
        Total = total_prices

    print(Delivery_Cost)
    context = {
        'shoe':shoe,
        'total_price':total_price,
        'Delivery_Cost':Delivery_Cost,
        'Total':Total
    }
    
    return render(request,'shop.html',context)

def cart_delete(request,cart_id):
    print(cart_id)
    shoes_cart = ShopBag.objects.get(id = cart_id)

    shoes_cart.delete()
    return redirect('cart',request.user.id)


def payment_information(request, user_id):
    total = request.GET.get('total')
    user = User.objects.get(id=user_id)
    print(user, total)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        num3 = request.POST['num3']
        num4 = request.POST['num4']

        card_number = num1 + num2 + num3 + num4

        day = request.POST['day']
        year = request.POST['year']
        clv = request.POST['clv']
        number = float(total.replace(',', ''))
        if float(number) > 4000:
            print('kargo bedeli var')
            deliveryPrice = total
        else:
            print('kargo beles')
            deliveryPrice = 'free'

        pay = PayDetails.objects.create(user=user,price=total,name=name,email=email,address=address,cardNumber=card_number,day=day,year=year,clv=clv)

        if pay:
            CartItems = ShopBag.objects.filter(users=user)
            for CartItem in CartItems:
                orderCreate = UserOrder.objects.create(users = CartItem.users, productB = CartItem.productB,number = CartItem.number,payName = pay.name,payEmail=pay.email,payAddress=pay.address,paycardNumber=pay.cardNumber,deliveryPrice=deliveryPrice)
            
            if CartItems:
                ShopBag.objects.filter(users=user).delete()

            return JsonResponse({'success': True, 'message': 'Ödeme başarılı!'})
        else:
            return JsonResponse({'error': False, 'message': 'Ödeme basarisiz!'})

    context = {
        'total':total,
    }
    return render(request, 'payment.html', context)

def search(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    if q:
        shoes_filter = Shoes.objects.filter(Q(name__icontains=q))
        print(shoes_filter)

        result = {'success': True, 'message': 'Search successful', 'data': {'shoes_filter': list(shoes_filter.values())}}
    else:
        result = {'success': False, 'message': 'Search term is empty or not provided', 'data': None}

    return JsonResponse(result)
