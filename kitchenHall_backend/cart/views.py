from django.shortcuts import render, redirect, get_object_or_404
from .models import CartItem
from products.models import Product


# Create your views here.

def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'view_cart.html', {'cart_items': cart_items})


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('view-cart')


def remove_from_cart(request, product_id):
    cart_item = get_object_or_404(CartItem, user=request.user, product_id=product_id)
    cart_item.delete()
    return redirect('view-cart')


def checkout(request):
    # implement checkout process
    return render(request, 'checkout.html')


def update_cart(request):
    # implement cart update process
    return redirect('view-cart')

