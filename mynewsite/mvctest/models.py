from django.db import models

class Product(models.Model):
    SIZES = (
        ('S','Smail'),
        ('M','Medium'),
        ('L','Large'),
    )
    sku = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    size = models.CharField(max_length=1, choices=SIZES)
    def __unicode__(self):
        return self.name
