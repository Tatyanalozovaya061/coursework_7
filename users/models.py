from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    """ Пользователь """
    username = None
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='E-mail', unique=True)
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    telegram_id = models.CharField(max_length=50, verbose_name='ID telegram', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.email}'
