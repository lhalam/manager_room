from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10)
    desription = models.TextField()
    size = models.IntegerField()

    def __str__(self):
        return self.name
