from datetime import date

from mainapp.models import Products
from django.shortcuts import render

def main(request):
    title = 'Главная'
    products = Products.object.all()
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html')

def products(request):
    return render(request, 'mainapp/products.html')

def contact(request):
    return render(request, 'mainapp/contact.html')


