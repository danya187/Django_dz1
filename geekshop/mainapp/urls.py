from django.urls import path
from mainapp.views import product, contact

urlpatterns = [
    path('', mainapp.products, name='index'),
    path('product/<int:pk>', product, name ='product'),
    path('contact/', contact, name ='contact'),
]
