from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserOrder 
from shoes.models import ShoesDetail,Category

@login_required(login_url='/accounts/login')
def myorder(request):
    user = User.objects.get(id=request.user.id)
    orders = UserOrder.objects.filter(users=user)
    categories = Category.objects.all()
    productD = []
    for order in orders:
        product = ShoesDetail.objects.get(name=order.productB)
        paycardNumber = order.paycardNumber
        
        masked_part = '*' * 6 
        masked_paycardNumber = paycardNumber[:6] + masked_part + paycardNumber[12:]

        
        chunks = [masked_paycardNumber[i:i+4] for i in range(0, len(masked_paycardNumber), 4)]

        if float(order.deliveryPrice.replace(',', '.')) < 5000:
            order.deliveryPrice = 150
            total = product.price + order.deliveryPrice
        else:
            order.deliveryPrice = "Kargo bedeli yok"
            total = product.price

        print(total)
        
        product_info = {
            'id': order.id,
            'image': product.image.url,
            'name': order.productB,
            'number': order.number,
            'price': product.price,
            'created': order.created,
            'order_number': order.random_number,
            'payName':order.payName,
            'payEmail':order.payEmail,
            'payAddress':order.payAddress,
            'paycardNumber':order.paycardNumber,
            'chunks':chunks,
            'deliveryPrice':order.deliveryPrice,
            'total':total
        }
        
        productD.append(product_info)
    context = {
        'categories':categories,
        'orders':orders,
        'productD':productD
    }
    return render(request, 'myOrders.html',context)
