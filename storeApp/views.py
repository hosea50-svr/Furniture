from django.shortcuts import get_object_or_404, redirect, render
from . models import Product

from django.http import HttpResponseRedirect
from urllib.parse import quote

from django.core.mail import send_mail
from django.conf import settings

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

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)

    return render(request, "products/product_details.html", {
        "product": product
    })

def contact(request):
    return render(request, "contact.html")


def order_list(request):
    order = request.session.get("order", {})

    products = []
    total = 0

    for product_id, quantity in order.items():
        product = Product.objects.get(id=product_id)

        subtotal = product.price * quantity
        total += subtotal

        products.append({
            "product": product,
            "quantity": quantity,
            "subtotal": subtotal
        })

    return render(request, "products/order_list.html", {
        "products": products,
        "total": total
    })



def add_to_order(request, id):
    product = get_object_or_404(Product, id=id)

    order = request.session.get("order", {})

    product_id = str(product.id)

    if product_id in order:
        order[product_id] += 1
    else:
        order[product_id] = 1

    request.session["order"] = order

    return redirect("order_list")

def remove_item(request, id):
    order = request.session.get("order", {})

    product_id = str(id)

    if product_id in order:
        del order[product_id]

    request.session["order"] = order

    return redirect("order_list")

def increase_quantity(request, id):
    order = request.session.get("order", {})

    product_id = str(id)

    if product_id in order:
        order[product_id] += 1

    request.session["order"] = order

    return redirect("order_list")

def decrease_quantity(request, id):
    order = request.session.get("order", {})

    product_id = str(id)

    if product_id in order:
        order[product_id] -= 1

        if order[product_id] <= 0:
            del order[product_id]

    request.session["order"] = order

    return redirect("order_list")

def reset_cart(request):
    request.session.pop("order", None)
    return redirect("order_list")

# WhatsApp set-up
def order_whatsapp(request):
    order = request.session.get("order", {})

    if not order:
        return redirect("order_list")

    message = "Hello Salisu Luxury Interior,\n\n"
    message += "I would like to order the following items:\n\n"

    total = 0

    for product_id, quantity in order.items():
        product = Product.objects.get(id=product_id)

        subtotal = product.price * quantity
        total += subtotal

        message += (
            f"🪑 {product.name}\n"
            f"Quantity: {quantity}\n"
            f"Price: ₦{subtotal:,.0f}\n\n"
        )

    message += f"💰 Total: ₦{total:,.0f}\n\n"
    message += "Please let me know the availability. Thank you!"

    phone = "2348103189576" 

    whatsapp_url = f"https://wa.me/{phone}?text={quote(message)}"

    return HttpResponseRedirect(whatsapp_url)





def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]

        subject = "New Contact Form Message"

        full_message = f"""
Name: {name}
Email: {email}

Message:
{message}
"""

        send_mail(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,
            ["sm7399586@gmail.com"],
            fail_silently=False,
        )

    return render(request, "contact.html")