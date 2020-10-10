from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.

""" Shopping cart """


class ShoppingCart(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'products/shopping_cart.html')


""" Prodcut home """


class ProductsHome(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'products/home_products.html')


""" Product only """


class ProductOnly(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'products/product_only.html')
