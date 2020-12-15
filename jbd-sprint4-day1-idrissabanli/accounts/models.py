from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    bio = models.TextField('Bio', null=True, blank=True)
    image = models.ImageField('Image', )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
