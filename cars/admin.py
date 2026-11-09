from django.contrib import admin
from .models import *

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'year', 'price', 'fuel_type', 'mileage']
    list_filter = ['fuel_type', 'body_type', 'year']
    search_fields = ['brand', 'model']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'phone', 'email', 'id_number']
    search_fields = ['name', 'surname', 'phone']

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['car', 'customer', 'price', 'status', 'date_sold', 'sales_person']
    list_filter = ['status', 'date_sold']