from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return f"{self.user.first_name}"
