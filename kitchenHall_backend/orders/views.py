from django.shortcuts import render, get_object_or_404
from .models import Order
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .serializers import *

# Create your views here.
class AllOrdersView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ListOrdersView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = OrderSerializer
   

    def get_queryset(self):
        if self.request.user.is_authenticatd:
            user = self.request.user
            return Order.objects.filter(user=user)
        else:
            return Order.objects.none()

class OrderManagementView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)

class CreateOrderView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)

def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order_list.html', {'orders': orders})

def view_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_detail.html', {'order': order})

def create_order(request):
    # implement order creation logic after checkout
    return redirect('order-list')

def update_cart(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order_list.html', {'orders': orders})