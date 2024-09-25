from django.urls import path
from .views import *


urlpatterns = [
    path('me/orders', ListOrdersView.as_view(), name='orders-list'),
    path('<str:order_id>', OrderManagementView.as_view(), name='manage-order'),
    path('create', CreateOrderView.as_view(), name='create-order'),
    path('allorders', AllOrdersView.as_view(), name='all-orders'),
    path('update', update_cart, name='update-cart'),
]