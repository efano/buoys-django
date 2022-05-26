from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date


# Create your models here.
class Comment(models.Model):
    user = models.OneToOneField(
        User, related_name='comments', on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    buoy_id = models.CharField(max_length=5, default='')
    body = models.CharField(max_length=255)

    def __str__(self):
        return '%s - %s' % (self.user, self.body)
