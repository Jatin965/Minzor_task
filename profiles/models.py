from django.db import models
from django.conf import settings

# Create your models here.

class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mobile = models.PositiveIntegerField(blank = True, null = True)
    email = models.EmailField(blank = True, null = True)

    def __str__(self):
        return str(self.user.username)