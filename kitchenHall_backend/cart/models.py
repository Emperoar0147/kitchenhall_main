from django.db import models
from users.models import User
from products.models import Product

# Create your models here.

class CartItem(models.Model):
    """
    Model definition for a cart item
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return f"{self.product.name} - {self.quantity}"