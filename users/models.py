from django.contrib.auth.models import AbstractUser
from django.db import models


c


class User(AbstractUser):
    username = None
    phone_number = models.CharField(unique=True, verbose_name='номер телефона')

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

