from django.db import models
from users.models import User
from products.models import Product


# Create your models here.


class Order(models.Model):
    """
    model definition of an order
    """
    ORDER_STATUS = [
        ('PENDING', 'pending'),
        ('PROCESSING', 'processing'),
        ('SHIPPED', 'shipped'),
        ('DELIVERED', 'delivered'),
        ('CANCELLED', 'cancelled')
    ]

    SHIPPING_METHOD = [
        ('STANDARD', {"name": "standard", "cost": 0.00}),
        ('EXPRESS', {"name": "express", "cost": 5.00})
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=50, choices=ORDER_STATUS, default=ORDER_STATUS[2][0])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    # Shipping information
    shipping_address = models.TextField()
    shipping_method = models.CharField(max_length=50, choices=SHIPPING_METHOD, default=SHIPPING_METHOD[0][0])
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    shipping_date = models.DateTimeField(null=True, blank=True)
    

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"