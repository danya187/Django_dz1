from datetime import date

from django.shortcuts import render

def main(request):
    return render(request, 'mainapp/index.html')

def products(request):
    return render(request, 'mainapp/products.html')

def contact(request):
    return render(request, 'mainapp/contact.html')


def temp(request):
    return render(request, 'mainapp/temp1.html', {'data': "тест"})
