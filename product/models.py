from django.db import models
import random
import os 

availability_choices = (
    ('In-stock','In-stock'),
    ('Not-available','Not-available'),
    )

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_product(instance, filename):
    new_name = random.randint(1, 27634723542)
    name, ext = get_filename_ext(filename)
    final_name = f"product--{filename}"
    return f"Product/{final_name}"

class ProductModel(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(max_length=5000, null=True, blank=True)
    price = models.BigIntegerField(null=True, blank=True)
    show_price = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to=upload_image_product, null=True, blank=True)
    image2 = models.ImageField(upload_to=upload_image_product, null=True, blank=True)
    image3 = models.ImageField(upload_to=upload_image_product, null=True, blank=True)
    image4 = models.ImageField(upload_to=upload_image_product, null=True, blank=True)
    availability = models.CharField(choices=availability_choices,max_length=20, default='In-stock') 
    commission1 = models.FloatField(max_length=10, null=True, blank=True)
    commission2 = models.FloatField(max_length=10, null=True, blank=True)
    commission3 = models.FloatField(max_length=10, null=True, blank=True)


    def __str__(self):
        return self.name
