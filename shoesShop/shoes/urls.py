from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.gallery_list,name="gallery"),

    path('categories/<slug:category_slug>', views.gallery_list, name="gallery_by_category"),

    path('product/<int:product_id>',views.product_detail,name='product'),
    path('addcomment/<int:product_id>', views.addComment, name="addComment"),

    path('cart/<int:user_id>',views.cart_products,name='cart'),
    path('delete/<int:cart_id>',views.cart_delete,name='cart-delete'),
    path('filter_shoes/', views.filter_shoes, name='filter_shoes'),
    path('payment/<int:user_id>',views.payment_information,name="payment-information"),
    path('search',views.search,name='search'),
]
