from django.db import models

class Store(models.Model):
  name = models.CharField(max_length=50)
  address = models.CharField(max_length=75)
  city = models.CharField(max_length=50)
  type = models.CharField(max_length=50)
  
