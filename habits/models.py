from django.db import models
from users.models import User

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    """  Привычка """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    place = models.CharField(max_length=150, verbose_name='Место выполнения', **NULLABLE)
    time = models.TimeField(verbose_name='Время начала выполнения', **NULLABLE)
    action = models.CharField(max_length=150, verbose_name='Действие')
    is_pleasant_habit = models.BooleanField(verbose_name='Признак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Связанная привычка', **NULLABLE)
    periodicity = models.PositiveIntegerField(verbose_name='Периодичность')
    reward = models.CharField(max_length=150, verbose_name='Вознаграждение', **NULLABLE)
    duration_time = models.TimeField(verbose_name='Длительность выполнения', **NULLABLE)
    is_public = models.BooleanField(verbose_name='Признак публичности')

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'

    def __str__(self):
        return f'{self.action}'
