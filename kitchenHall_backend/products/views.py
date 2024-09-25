from django.shortcuts import render, HttpResponse
from rest_framework import generics
from .models import Product, Category
from .serializers import *
from django.http import JsonResponse

# Create your views here.


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def productslist(request):
    all_products = Product.objects.all().values(
        'id','name', 'description', 'price', 'stock', 'image', 'category__name'
    )
    #return render(request, 'products.html', {'products': all_products})
    return JsonResponse(list(all_products), safe=False)


def manageproduct(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price', '')
        category = request.POST.get('category')
        in_stock = request.POST.get('in_stock')

        new_product = Product(name=name, description=description, price=price, in_stock=in_stock)

        new_product.save()

        if new_product.id:
            return HttpResponse(f'Your product {new_product.name} has been added')
        else:
            return HttpResponse('An error occured')
    return render(request, 'addproducts.html')


def productdetails(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})


def searchproducts(request):
    query = request.GET.get('q')
    products = Product.objects.filter(name__icontains=query)
    return render(request, 'search_result.html', {'products': products})


def availablecategories(request, category):
    categories = Product.objects.filter(category=category)
    return render(request, 'category_list.html', {'products': products})
