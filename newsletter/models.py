from django.db import models
from django.utils import timezone

class Subscriber(models.Model):
    name = models.CharField(max_length=100, default="Subscriber name")
    email = models.EmailField(unique=True, max_length=100)
    created_date = models.DateTimeField('Date created', default=timezone.now)

    def __str__(self):
        return self.email