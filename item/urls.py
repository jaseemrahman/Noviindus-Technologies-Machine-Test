#Import from the core django
from django.urls import path
#Import from local app/library
from item import views

urlpatterns = [
    #home page
    path('',views.item_list,name='item.list'),
    path('create',views.item_create,name='item.create'),
    path('update/<int:pk>',views.item_update,name='item.update'),
    path('delete/<int:pk>',views.item_delete,name='item.delete'),
    path('view/<int:pk>',views.item_view,name='item.view'),

    #cart
    path('cart',views.viewcart,name='cart'),
    path('addtocart',views.addtocart,name='add.to.cart'),
    path('removefromcart',views.cart_remove,name='remove.from.cart'),
    path('cart/order',views.order_create,name='cart.order'),

    # order list
    path('order_list/<int:pk>',views.order_list,name='order.list'),

    #order detail
    path('order_list/details/<int:pk>',views.order_detail_view,name='order.detail'),


    #order status
    path('order_status/<int:pk>',views.order_status,name='order.status'),

]