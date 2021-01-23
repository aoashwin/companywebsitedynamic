from django.shortcuts import render
from .models import People
from .models import Product

# Create your views here.

def home(request):
    context = {}
    return render(request, 'website/home.html', context)

def productslist(request):
    context = {}
    context['products'] = Product.objects.all()
    return render(request, 'website/products.html', context)

def peoplelist(request):
    context = {}
    context['peoples'] = People.objects.all()
    return render(request, 'website/people.html', context)

def contactus(request):
    context = {}
    return render(request, 'website/contactus.html', context)    