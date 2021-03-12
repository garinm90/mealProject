from django.db import models
from django.conf import settings


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    available = models.BooleanField(default=False)
    # image = models.ImageField()


class OrderItem(models.Model):
    item = models.ForeignKey(MenuItem, on_delete=models.SET_NULL, null=True)
    order_item_order = models.ForeignKey("Order", on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=0)


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_items = models.ManyToManyField(OrderItem)
    is_ordered = models.BooleanField(default=False)
