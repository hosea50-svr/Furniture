from django.db import models

# Create your models here.

CATEGORY_CHOICES = [
    ("sofa", "Sofa"),
    ("bed", "Bed"),
    ("dining", "Dining"),
    ("wardrobe", "Wardrobe"),
    ("tv-stand", "TV Stand"),
    ("office", "Office Furniture"),
]

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="products/")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    color = models.CharField(max_length=50, blank=True )
    material = models.CharField(max_length=100, blank=True)

    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}'
    