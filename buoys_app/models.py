from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date


# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(
        User, related_name='comments', on_delete=models.CASCADE)
    user_agency = models.CharField(max_length=100, default='')
    published_date = models.DateField(auto_now=True)
    buoy_id = models.CharField(max_length=5, default='')
    body = models.TextField()

    def __str__(self):
        return '%s - %s' % (self.user_agency, self.user)
