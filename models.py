from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from .base import CustomBaseUser

class CustomUser(CustomBaseUser):
    first_name = models.CharField(max_length=100)
    """
    def __str__(self):
        return self.username
    """
