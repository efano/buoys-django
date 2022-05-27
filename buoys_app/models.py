from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     agency = models.CharField("agency", max_length=50, blank=True)

#     @receiver(post_save, sender=User)
#     def create_user_profile(sender, instance, created, **kwargs):
#         if created:
#             Profile.objects.create(user=instance)

#     @receiver(post_save, sender=User)
#     def save_user_profile(sender, instance, **kwargs):
#         instance.profile.save()


class Comment(models.Model):
    user = models.ForeignKey(
        User, related_name='comments', on_delete=models.CASCADE)
    agency = models.CharField(
        max_length=100, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    buoy_id = models.CharField(max_length=5, default='')
    body = models.CharField(max_length=255)

    def __str__(self):
        return '%s - %s - %s' % (self.agency, self.user, self.body)
