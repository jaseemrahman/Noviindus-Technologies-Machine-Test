#Import from the core django
from django.urls import path
#Import from local app/library
from accounts import views
urlpatterns = [
    #home page
    path('customer_list',views.customer_list,name='customer.list'),
    #login
    path('login', views.user_login, name='login'),
    #signup
    path('signup', views.user_signup, name='signup'),
    #logout
    path('logout',views.logout_user,name='logout'),
]