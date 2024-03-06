from django.db import models
from .store import Store
from .user import User

class StoreFavorite(models.Model):
  store = models.ForeignKey(Store, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
