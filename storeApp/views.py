from django.shortcuts import render
from . models import Product

# Create your views here.
def hero(request):
    return render(request, 'hero.html')

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def category_products(request, category):
    products = Product.objects.filter(category=category)
    return render(request, "products/category_products.html", {
        "products": products,
        "category": category
    })

def contact(request):
    return render(request, "contact.html")
