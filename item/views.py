#Import from the core django
from django.shortcuts import render
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.http import JsonResponse,HttpResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
#Import from the third library
from datetime import datetime
#Import from local app/library
from item.forms import ProductForm ,OrderForm,StatusForm
from item.models import Product,OrderDetail,Order,Customer

# Create your views here.

#list items
def item_list(request):
    items=Product.objects.all()  
    context={'items':items,
            "today":datetime.today()}   
    return render(request,'item/item_list.html',context)

#item detail view
def item_view(request,pk):
    item=Product.objects.get(pk=pk)    
    context={'item':item}   
    return render(request,'item/item_view.html',context)   

#Create Item
@login_required
def item_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("item.list")        
    else:
        form = ProductForm()

    context = {'form': form}
    return render(request,'item/item_edit.html',context) 

#edit item 
@login_required
def item_update(request,pk):
    item=Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST,files=request.FILES,instance=item)
        if form.is_valid():
            form.save()
            return redirect("item.list",)
    else:
        form = ProductForm(instance=item)
    context = {'form': form,'item': item}
    return render(request,'item/item_edit.html',context) 

#item delete
@login_required
def item_delete(request, pk):
    data = dict()
    
    if request.method == 'POST':
        item = Product.objects.get(pk=pk)
        item.delete()
        return redirect('item.list') 
    
        
    else:
        item = Product.objects.get(pk=pk)
        context = {'item': item}
        data['html_form'] = render_to_string('item/partial_item_delete.html',
                            context,request=request)
        return JsonResponse(data) 
  

#add to cart view
def addtocart(request):
    productid = request.GET['productid']
    qty = request.GET['qty']
    cartitems = {}
    if request.session.__contains__('cartdata'):
        cartitems = request.session['cartdata']
    cartitems[productid]=qty
    request.session['cartdata'] = cartitems

    items=Product.objects.all()     
    context={'items':items,
            "today":datetime.today(),
            } 
    return render(request,'item/item_list.html',context)


#to remove cart item
def cart_remove(request):
    productid = request.GET['productid']
    cartitems = {}
    if request.session.__contains__('cartdata'):
        cartitems = request.session['cartdata']
    request.session['cartdata'] = cartitems
    del cartitems[productid]
    return redirect('cart')    
     
#order create
@login_required
def order_create(request):
    data = dict()
    if request.method == 'POST':

        form = OrderForm(request.POST,files=request.FILES)
        if form.is_valid():
            # print(form.errors)
            customer=form.save()
            orderd_user=request.user
            order=Order.objects.create(customer=customer,user=orderd_user)
            order_id=Order.objects.get(pk=order.id)
            cartitems = {}
            if request.session.__contains__('cartdata'):
                cartitems = request.session['cartdata']
            request.session['cartdata'] = cartitems
            val=request.session['cartdata']
            for key,value in (zip((val.keys()), (val.values()))):
                item=Product.objects.get(pk=key)
                order_detail=OrderDetail.objects.create(order_id=order_id,product=item,qty=value,total=int(value)*item.price)
            cartitems.clear()
            messages.success(request, 'Order Placed Successfully')
            return redirect("item.list")        
    else:
        form = OrderForm()

    context = {'form': form}
    data['html_form'] = render_to_string('item/order.html',context,request=request)
    return JsonResponse(data)  
       
#cart view
def viewcart(request):
    page = loader.get_template("item/shoppingcart.html") 
    if request.session.__contains__('cartdata'):
            it = request.session['cartdata'].items()
            productdb =[]
            it = list(it)   
            for i in range(len(it)):
                productid = it[i][0]
                qty = it[i][1]
                db = Product.objects.get(id=productid)
    
                productdb.append({
                    'id':productid,
                    'title':db.title,
                    'Qty':qty,
                    'img':db.image,
                    'Price':db.price,
                    "total_price":int(qty)*db.price
                })
            fullamount = []
            for i in productdb:
                for key,value in i.items():
                    if key == "total_price":
                        fullamount.append(value)
            total_quantity = []
            for i in productdb:
                for key,value in i.items():
                    if key == "Qty":
                        total_quantity.append(int(value))      

            data = {"items":productdb,"full_amount":sum(fullamount),"total_quantity":sum(total_quantity)}
            response = page.render(data,request)
            return HttpResponse(response)
    else:
        return render(request,'item/shoppingcart.html') 

#order list
def order_list(request,pk):
    user=User.objects.get(pk=pk) 
    orders=Order.objects.filter(user=user)
    context= {'orders':orders}
    return render(request, 'item/order_list.html',context)          

#order detail
def order_detail_view(request,pk):
    order_details=OrderDetail.objects.filter(order_id=pk)
    order=Order.objects.get(pk=pk)
    form=StatusForm(instance=order)
    context={'order_details':order_details,'pk':pk,'form':form,"today":datetime.today()}

    return render(request,'item/order_detail.html',context) 

#order status
def order_status(request,pk):
    if request.method== 'POST':
        status=request.POST['order_status']
        order=Order.objects.get(pk=pk)
        order.order_status=status
        order.save()
    return HttpResponseRedirect(reverse('order.detail',args=[pk]))



