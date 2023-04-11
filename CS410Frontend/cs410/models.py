from django.db import models
from simple_history.models import HistoricalRecords

class placeholder(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.CharField(max_length=100)
    field3 = models.CharField(max_length=100)
    field4 = models.CharField(max_length=100)
    field5 = models.CharField(max_length=100)
    history = HistoricalRecords()

    def __str__(self):
        return self.description
    

