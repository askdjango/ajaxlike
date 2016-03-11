from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    like_count = models.PositiveIntegerField(default=0)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
