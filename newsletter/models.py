from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    is_confirmed = models.BooleanField(default=False)
    confirmation_code = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.email