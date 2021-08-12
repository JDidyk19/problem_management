from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    ''' User Model '''
    class Meta:
        ordering = ['id']
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    # TO STRING METHOD
    def __str__(self):
        return self.username
