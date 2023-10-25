from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    confirmation_token = models.CharField(max_length=255)


    def __str__(self):
        return self.email
