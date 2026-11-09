from django.urls import path
from . import views

urlpatterns = [
   path('register/', views.registerPage, name='register'), 
   path('login/', views.loginPage, name='login'),
   path('logout/', views.logoutUser, name='logout'), 
   path('', views.home, name="home"),
   path('cars/', views.cars, name="cars"),
   path('customer/', views.customer, name='customer'),
   path('sales/', views.sales, name='sales'),

   path('create_sale/<str:pk>', views.createSale, name="create_sale"),
   path('update_sale/<str:pk>', views.updateSale, name="update_sale"),
   path('delete_sale/<str:pk>', views.deleteSale, name="delete_sale"),
   path('car_view/<int:pk>', views.car_view, name="car_view" ),
   path('customer_view/<int:pk>', views.customer_view, name="customer_view" )


]