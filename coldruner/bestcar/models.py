from django.db import models

class Publishing_a_trip(models.Model):
    name = models.CharField(max_length=100)
    departure = models.CharField(max_length=100)
    arrival = models.CharField(max_length=100)
    models_auto = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    seating = models.BigIntegerField()
    is_published = models.BooleanField(default=True)

