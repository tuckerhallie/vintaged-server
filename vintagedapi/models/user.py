from django.db import models

class User(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  bio = models.CharField(max_length=200)
  uid = models.CharField(max_length=50)
