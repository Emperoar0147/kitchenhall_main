from django.urls import path
from views import *


urlpatterns = [
    path('', view_cart, name='view-cart'),
    path('add/<str:product_id>', add_to_cart, name='add-to-cart'),
    path('remove/<str:product_id>', remove_from_cart, name='remove-from-cart'),
    path('checkout', cart_checkout, name='cartcheckout'),
    path('update', update_cart, name='update-cart'),
]