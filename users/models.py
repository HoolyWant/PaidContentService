from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    phone_number = models.CharField(unique=True, verbose_name='номер телефона')
    is_subscribed = models.BooleanField(default=True, verbose_name='по')

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

