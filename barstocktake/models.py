from django.db import models

class Stock(models.Model):
    DRINK_TYPE = (
        ('B', 'Beer'),
        ('S', 'Shot'),
        ('W', 'Wine'),
    )
    brand = models.CharField(max_length=50)
    volume = models.IntegerField()
    drink_type = models.CharField(max_length=1, choices=DRINK_TYPE)