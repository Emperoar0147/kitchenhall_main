from django.urls import path
from .views import *

urlpatterns = [
    path ('', productslist, name='listofallproducts'), # GET
    path ('products', ProductListView.as_view(), name='manageproducts'), # POST
    path ('productdetail/<str:pk>', ProductDetailView.as_view(), name='productdetails'), # GET, PUT, DELETE
    path ('product/search', searchproducts, name='searchforproduct'), # GET
    path('categories', CategoryListView.as_view(), name='listofavailablecategories'), # GET
    path('categories/<str:pk>', CategoryDetailView.as_view(), name='categorydetail'), 
]