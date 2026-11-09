from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    BODY_TYPES = [
        ("sedan", "Sedan"),
        ("hatchback", "Hatchback"),
        ("suv", "SUV"),
        ("coupe", "Coupe"),
        ("bakkie", "Bakkie"),
        ("convertible", "Convertible"),
    ]
    CONDITIONS = [
        ("new", "New"),
        ("used", "Used"),
        ("certified pre-owned", "Certified Pre-Owned"),
    ]
    FUEL_TYPES = [
        ("petrol", "Petrol"),
        ("diesel", "Diesel"),
        ("hybrid", "Hybrid"),
        ("electric", "Electric"),
    ]
    TRANSMISSIONS = [
        ("manual", "Manual"),
        ("automatic", "Automatic"),
        ("cvt", "CVT"),
        ("dual-clutch", "Dual-Clutch"),
    ]

    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.IntegerField()
    body_type = models.CharField(max_length=200, choices=BODY_TYPES)
    color = models.CharField(max_length=200)
    mileage = models.IntegerField()
    transmission = models.CharField(max_length=200, choices=TRANSMISSIONS)
    engine = models.CharField(max_length=200)
    fuel_type = models.CharField(max_length=200, choices=FUEL_TYPES)  # fixed capital T
    condition = models.CharField(max_length=200, choices=CONDITIONS)
    price = models.FloatField()
    image = models.ImageField(upload_to='car_images/', null=True, blank=True) 

    def __str__(self):
        return f"{self.brand} {self.model}"  # fixed self.name doesn't exist, use brand

class Customer(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    id_number = models.CharField(max_length=13)
    address = models.TextField()

    def __str__(self):
        return f"{self.name} {self.surname}"
    

class Sale(models.Model):
    STATUS = [
        ("pending", "Pending"),
        ("out_for_delivery", "Out for Delivery"),
        ("delivered", "Delivered"),
        ("cancelled", "Cancelled"),
    ]

    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_sold = models.DateField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    sales_person = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    status = models.CharField(max_length=20, choices=STATUS, default='pending')

    def __str__(self):
        return f"{self.car} - {self.status}"