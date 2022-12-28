from django.db import models

class WUser(models.Model):
    closest_destination = models.CharField(max_length=40)
    user_destination = models.CharField(max_length=40)

# Create your models here.
