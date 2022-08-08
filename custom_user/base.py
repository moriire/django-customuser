from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext as _
from django.utils import timezone
from .manager import UserManager

class CustomBaseUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_("username"), max_length=100, unique=True,)
    email = models.EmailField(_("email address"), unique=True)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = "email"

    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username
