from django.db import models

class Item(models.Model):
    # These are each of the attributes the item will have.
    name = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    price = models.IntegerField(max_length=200)
    num_in_stock = models.IntegerField(max_length=200)
    max_stock = models.IntegerField(max_length=200)

    def __str__(self):
        return self.name
