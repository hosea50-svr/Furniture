from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.hero, name="hero"),
    path('contact/', views.contact, name='contat'),
    path('about/', views.about, name='about'),
    path('category/<str:category>/', views.category_products, name='category_products'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)