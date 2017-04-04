from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    price = models.IntegerField(max_length=200)
    num_in_stock = models.IntegerField(max_length=200)
    max_stock = models.IntegerField(max_length=200)

    def __str__(self):
        return self.name
