from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    date = models.DateTimeField()
    subscribers = models.ManyToManyField(User)
    number_of_subscribers = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')

    def __str__(self):
        return self.title
