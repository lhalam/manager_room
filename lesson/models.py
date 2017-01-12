from django.db import models

class Lesson(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    time = models.DateTimeField()
    place = models.CharField(max_length=15)
    timeout = models.IntegerField()

    def __str__(self):
        return self.name

