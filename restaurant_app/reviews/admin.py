# menu/admin.py
from django.contrib import admin
from .models import Category, Dish

admin.site.register(Category)
admin.site.register(Dish)

# orders/admin.py
from django.contrib import admin
from .models import Order, OrderItem

admin.site.register(Order)
admin.site.register(OrderItem)

# reviews/admin.py
from django.contrib import admin
from .models import Review

admin.site.register(Review)

