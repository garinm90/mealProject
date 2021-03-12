from django.contrib import admin
from .models import MenuItem, Order, OrderItem

admin.site.register([MenuItem, Order, OrderItem])
