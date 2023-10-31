from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customer_set',
        blank=True,
        help_text='this group belongs to',
        verbose_name='groups',)
    

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='farmers_related',
        blank=True,
        help_text='Permission to user.',
        verbose_name='user_permissions',)

USERNAME_FIELD = 'email'
REQUIRED_FIELDS = ['username']