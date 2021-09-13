from django.urls import path
from mainapp.views import product, contact

urlpatterns = [
    path('product/<int:pk>', product, name ='product'),
    path('contact/', contact, name ='contact'),
]