from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    agency = models.CharField('agency', max_length=50)

    def __str__(self):
        return '%s - %s' % (self.agency, self.user)


class Comment(models.Model):
    user = models.ForeignKey(
        User, related_name='comments', on_delete=models.CASCADE)
    agency = models.CharField(
        max_length=100, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    buoy_id = models.CharField(max_length=5, default='')
    body = models.CharField(max_length=255)

    def __str__(self):
        return '%s - %s - %s - %s' % (self.agency, self.user, self.buoy_id, self.body)
