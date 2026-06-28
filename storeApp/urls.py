from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.hero, name="hero"),
    path('contact/', views.contact, name='contat'),
    path('about/', views.about, name='about'),

    path('category/<str:category>/', views.category_products, name='category_products'),

    path("product_detail/<int:id>/", views.product_detail, name="product_detail"),

    path("add-to-order/<int:id>/", views.add_to_order, name="add_to_order"),
    path("order-list/", views.order_list, name="order_list"),

    path("remove-item/<int:id>/", views.remove_item, name="remove_item"),

    path("increase/<int:id>/", views.increase_quantity, name="increase_quantity"),
    path("decrease/<int:id>/", views.decrease_quantity, name="decrease_quantity"),

    path("order-whatsapp/", views.order_whatsapp, name="order_whatsapp"),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)