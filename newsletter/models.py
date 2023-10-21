from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.email

class Newsletter(models.Model):
    subject = models.CharField(max_length=255)
    content = models.TextField()
    sent_at = models.DateTimeField(null=True, blank=True)