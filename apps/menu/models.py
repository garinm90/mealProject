from django.db import models
from django.conf import settings


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    available = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class OrderItem(models.Model):
    item = models.ForeignKey(
        MenuItem, on_delete=models.SET_NULL, null=True, related_name="order_items"
    )
    order_item_order = models.ForeignKey("Order", on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.item} * {self.quantity} for {self.order_item_order}"


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders"
    )
    order_items = models.ManyToManyField(OrderItem, blank=True, related_name="orders")
    is_ordered = models.BooleanField(default=False)
    order_date = models.DateField(auto_now_add=True)
    order_modified_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"order # {self.pk} {self.user}"

    def confirm_order(self):
        self.is_ordered = True
        self.save(update_fields=["is_ordered"])
