from django.db import models

# Create your models here.
class Testovoe(models.Model):
    rang = models.IntegerField(blank=False)
    os = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)
    Value = models.IntegerField(blank=False)
    Alarms = models.CharField(max_length=100)

class Comments(models.Model):
    item_id = models.IntegerField(blank=False)
    comment = models.TextField(max_length=250)
    id = models.IntegerField(primary_key=True)
    
