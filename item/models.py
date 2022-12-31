#Import from the core django
from django.db import models
from django.contrib.auth.models import User
#Import from the third library
import datetime

# Create your models here.

#menu
class Product(models.Model):
    title = models.CharField(max_length=300,unique=True)
    image=models.ImageField(upload_to='product', blank=True,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
 
    def __str__(self):
        return self.title

class Customer(models.Model):
    name=models.CharField(max_length=300)
    address=models.CharField(max_length=3000)
    mail_id=models.EmailField(null=True,blank=True)
 
    def __str__(self):
        return self.name


#order
class Order(models.Model):
    APPROVED = 0
    SHIPPED = 1
    DELIVERED = 2
    
    ORDER_CHOICES = (
                     (APPROVED, 'approved'),
                     (SHIPPED, 'shipped'),
                     (DELIVERED, 'delivered'),
                     )
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='customer')
    order_status=models.IntegerField(choices=ORDER_CHOICES,default=APPROVED,null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    order_date=models.DateField( default=datetime.date.today, blank=True)
    
    def __str__(self):
        return str(f"{self.id}-{self.customer}" )  

#order details
class OrderDetail(models.Model):
 
    order_id=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='order')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product')
    qty=models.IntegerField()
    total=models.DecimalField(max_digits=10, decimal_places=2)
 
    def __str__(self):
        return str(self.order_id )           
