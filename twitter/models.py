from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text