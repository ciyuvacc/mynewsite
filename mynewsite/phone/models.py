from django.db import models

class Phonelist(models.Model):
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    qty = models.IntegerField()
    def __unicode__(self):
        return self.name
