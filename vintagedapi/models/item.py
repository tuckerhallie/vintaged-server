from django.db import models
from .user import User
from .store import Store

class Item(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=50)
  color = models.CharField(max_length=100)
  image = models.CharField(max_length=200)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  store = models.ForeignKey(Store, on_delete=models.CASCADE)
  
  
