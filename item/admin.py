#Import from the core django
from django.contrib import admin
#Import from local app/library
from item.models import Product,Order,OrderDetail,Customer

# Register your models here.
admin.site.register([Product,Order,OrderDetail,Customer])
