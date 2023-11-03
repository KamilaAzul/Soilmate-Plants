from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    is_confirmed = models.BooleanField(default=False)
    confirmation_code = models.CharField(max_length=64, blank=True, null=True)

    def generate_confirmation_code(self):
        self.confirmation_code = get_random_string(32)
        self.save()

    def __str__(self):
        return self.email