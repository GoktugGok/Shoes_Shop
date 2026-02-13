from django.shortcuts import render ,redirect
from . models import ShoesDetail, Category, Brand ,ShopBag,PayDetail,ShoeHeight,Color,Genders,ShoesNumbers,Comment
from myorder.models import UserOrder
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse 
from django.db.models import Q
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.db.models import Avg


    
def filter_shoes(request):
    if request.method == 'GET' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        category_name = request.GET.get('category_name', None)
        print(category_name)

        shoes = ShoesDetail.objects.all()

        shoes_number_filters = request.GET.getlist('shoes_number_filters')
        shoes_brand_filters = request.GET.getlist('shoes_brand_filters')
        shoes_color_filters = request.GET.getlist('shoes_color_filters')
        shoe_height_filters = request.GET.getlist('shoe_height_filters')

       # number brand color height
        if shoes_number_filters and shoes_brand_filters and shoes_color_filters and shoe_height_filters:
            q_objects = Q()
            for number in shoes_number_filters:
                q_objects |= Q(numbers__name=number)
            shoes = shoes.filter(q_objects, category__slug=category_name, product_Brand__name__in=shoes_brand_filters, color__slug__in=shoes_color_filters, shoe_Height__slug__in=shoe_height_filters)
        
       # number brand color 
        elif shoes_number_filters and shoes_brand_filters and shoes_color_filters:
            q_objects = Q()
            for number in shoes_number_filters:
                q_objects |= Q(numbers__name=number)
            shoes = shoes.filter(q_objects,category__slug=category_name, product_Brand__name__in=shoes_brand_filters, color__slug__in=shoes_color_filters)
       # number brand height
        elif shoes_number_filters and shoes_brand_filters and shoe_height_filters:
            q_objects = Q()
            for number in shoes_number_filters:
                q_objects |= Q(numbers__name=number)
            shoes = shoes.filter(q_objects,category__slug=category_name, product_Brand__name__in=shoes_brand_filters, shoe_Height__slug__in=shoe_height_filters)
       # number height color   
        elif shoes_number_filters and shoes_color_filters and shoe_height_filters:
            q_objects = Q()
            for number in shoes_number_filters:
                q_objects |= Q(numbers__name=number)
            shoes = shoes.filter(q_objects,category__slug=category_name, color__slug__in=shoes_color_filters, shoe_Height__slug__in=shoe_height_filters)
       # brand height color   
        elif shoes_brand_filters and shoes_color_filters and shoe_height_filters:
            q_objects = Q()
            for number in shoes_number_filters:
                q_objects |= Q(numbers__name=number)
            shoes = shoes.filter(q_objects,category__slug=category_name,product_Brand__name__in=shoes_brand_filters, color__slug__in=shoes_color_filters, shoe_Height__slug__in=shoe_height_filters)
       # number brand    
        elif shoes_number_filters and shoes_brand_filters:
            q_objects = Q()
            for number in shoes_number_filters:
                q_objects |= Q(numbers__name=number)
            shoes = shoes.filter(q_objects,category__slug=category_name, product_Brand__name__in=shoes_brand_filters)
       # number color 
        elif shoes_number_filters and shoes_color_filters:
            q_objects = Q()
            for number in shoes_number_filters:
                q_objects |= Q(numbers__name=number)
            shoes = shoes.filter(q_objects,category__slug=category_name, color__slug__in=shoes_color_filters)
       # number color
        
        elif shoes_brand_filters and shoe_height_filters:
            shoes = shoes.filter(category__slug=category_name,product_Brand__name__in=shoes_brand_filters, shoe_Height__slug__in=shoe_height_filters)

        elif shoes_brand_filters and shoes_color_filters:
            shoes = shoes.filter(category__slug=category_name,product_Brand__name__in=shoes_brand_filters, color__slug__in=shoes_color_filters)

        elif shoe_height_filters and shoes_color_filters:
            shoes = shoes.filter(category__slug=category_name,shoe_Height__slug__in=shoe_height_filters, color__slug__in=shoes_color_filters)

        elif shoe_height_filters:
            q_objects = Q()
            for number in shoes_number_filters:
                q_objects |= Q(numbers__name=number)
            shoes = shoes.filter(q_objects,category__slug=category_name,shoe_Height__slug__in=shoe_height_filters)

        elif shoes_number_filters:
            q_objects = Q()
            for number in shoes_number_filters:
                q_objects |= Q(numbers__name=number)
            shoes = shoes.filter(q_objects,category__slug=category_name)

        elif shoes_brand_filters:
            shoes = shoes.filter(category__slug=category_name,product_Brand__name__in=shoes_brand_filters)

        elif shoes_color_filters:
            shoes = shoes.filter(category__slug=category_name,color__slug__in=shoes_color_filters)

        elif shoe_height_filters:
            shoes = shoes.filter(category__slug=category_name,shoe_Height__slug__in=shoe_height_filters)

        elif category_name:
            shoes = shoes.filter(category__slug=category_name)

        shoes_count = shoes.count()       
        print(shoes_count)
        return JsonResponse({'shoes': list(shoes.values()),'shoes_count':shoes_count})
    else:
        return JsonResponse({'error': 'Invalid request'})

def gallery_list(request, category_slug=None, tag_slug=None):
    shoes_all = ShoesDetail.objects.all().order_by('-created')
    categories = Category.objects.all()
    brands = Brand.objects.all()
    Shoe_Heights = ShoeHeight.objects.all()
    Colors = Color.objects.all()
    genders = Genders.objects.all()
    Shoes_Numbers = ShoesNumbers.objects.all()
    
    subcategories = None
    # navbar Butun ana Category icin 
    all_categories = Category.objects.filter(level=0)

    if category_slug is not None:
        category = get_object_or_404(Category, slug=category_slug)
        if category.is_root_node():
            # Ana kategori ise
            subcategories = category.get_children()
            # Category nin ayakkabilari
            shoes_all = ShoesDetail.objects.filter(category=category)
            
            
            context = {
                'shoes_all': shoes_all, 
                'categories': categories, 
                'subcategories': subcategories,
                'category':category,
                'all_categories': all_categories,
                'genders':genders,
                'Shoe_Heights':Shoe_Heights,
                'Colors':Colors,
                'Shoes_Numbers':Shoes_Numbers,
                'brands':brands
            }
            

            return render(request, 'gallery.html', context) 
        else:
            # Alt kategori ise
            shoes_all = ShoesDetail.objects.filter(category=category)
            print("alt cate")
    context = {
                'shoes_all': shoes_all, 
                'categories': categories, 
                'subcategories': subcategories,
                'all_categories': all_categories
            }
    return render(request, 'gallery.html', context)

def product_detail(request, product_id):
    product = ShoesDetail.objects.get(id=product_id)
    all_categories = Category.objects.filter(level=0)
    product.reviewsCount += 1
    product.save()
    user = request.user.id

    # Kullanıcının satın aldığı ayakkabıları kontrol et
    purchased_shoes = UserOrder.objects.filter(users=user, productB=product.name).exists()

    print(purchased_shoes)
    comments = Comment.objects.filter(product_id=product_id).order_by('-create_at')
    average_rate = Comment.objects.filter(product_id=product_id).aggregate(Avg('rate'))['rate__avg']

    # Puan sayi ondalikli olup olmadigini kontrol ediyor
    def is_decimal(number):
        number_str = str(number)
        return '.' in number_str
    if is_decimal(average_rate):
        print("Bu sayı ondalıklı.")
    else:
        print("Bu sayı ondalıklı değil.")

    print(average_rate)
    
    if average_rate == None:
        print('sa')
        average_rate = ''
    shoesC = ShoesDetail.objects.filter(shoesC=product.shoesC)

    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.warning(request, "Sepete eklemek için giriş yapmalısınız.")
            return redirect("/accounts/login")
        name = request.POST.get("shoesName")
        number = request.POST.get("shoesNumber")
        if not number:
            messages.warning(request, 'Lütfen bir ayakkabı numarası seçmeden önce formu göndermeyi deneyin.')
            return redirect('product', product_id)

        new_product_Bag = ShopBag.objects.create(users=request.user, productB=name, number=number)
        return redirect('cart', request.user.id)

    context = {
        'product': product,
        'shoesC': shoesC,
        'comments': comments,
        'all_categories': all_categories,
        'average_rate': average_rate,
        'purchased_shoes': purchased_shoes
    }
    return render(request, 'product.html', context)

@login_required(login_url='/accounts/login')
def cart_products(request,user_id):
    products = ShopBag.objects.filter(users__id = user_id) # kullanıcının sepete ekledikleri kullanıcı ismi, ürün ismi, number 
    all_categories = Category.objects.filter(level=0)
        
    total_price = 0
    shoe = []
    for product in products:
        shoes = ShoesDetail.objects.filter(name = product.productB,numbers__name=product.number)  # ürün bilgilerini almak için
        
        for shoe_obj in shoes:
            print(product.number)
            # Her bir ayakkabı için veri yapısı oluştur
            total_price += shoe_obj.price
            shoe_data = {
                'shoe_info': shoe_obj,
                'product': product,
                'all_categories':all_categories

            }
            # Veri yapısını dizinize ekleyin
            shoe.append(shoe_data)

    Delivery_Cost = 150 if shoe else 0  # Eğer ürün yoksa kargo bedeli 0 olacak
    total_prices = total_price
    if total_prices < 5000 and Delivery_Cost != '0 ':
        total_prices += Delivery_Cost
        Total = total_prices
    else:
        Delivery_Cost = '0 '
        Total = total_prices
        
    print(Delivery_Cost)
    context = {
        'shoe':shoe,
        'total_price':total_price,
        'Delivery_Cost':Delivery_Cost,
        'Total':Total,
        'all_categories':all_categories
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
            deliveryPrice = '0'

        pay = PayDetail.objects.create(user=user,price=total,name=name,email=email,address=address,cardNumber=card_number,day=day,year=year,clv=clv)

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
        shoes_filter = ShoesDetail.objects.filter(Q(name__icontains=q))
        print(shoes_filter)

        result = {'success': True, 'message': 'Search successful', 'data': {'shoes_filter': list(shoes_filter.values())}}
    else:
        result = {'success': False, 'message': 'Search term is empty or not provided', 'data': None}

    return JsonResponse(result)

def addComment(request, product_id):
    url = request.META.get('HTTP_REFERER')  # geldiğimiz sayfanın url bilgisini verir
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if 'subject' in request.POST and 'comment' in request.POST and 'rate' in request.POST:
            if not request.POST['subject'] or not request.POST['comment'] or not request.POST['rate']:
                messages.warning(request, "Başlık, yorum ve puanlama alanları boş bırakılamaz")
                return HttpResponseRedirect(url)
        if form.is_valid():
            data = Comment()
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            current_user = request.user
            data.user_id = current_user.id
            data.product_id = product_id
            data.save()
            messages.success(request, "Yorumunuz başarıyla kaydedildi")
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)

