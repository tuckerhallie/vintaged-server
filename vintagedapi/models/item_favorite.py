from django.db import models
from .user import User
from .item import Item

class ItemFavorite(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
