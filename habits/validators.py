from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from habits.models import Habit


def max_time(value):
    """ Максимальное время выполнения привычки в секундах """
    if value > 120:
        raise serializers.ValidationError('Время выполнения должно быть не больше 120 секунд')


def max_periodicity(value):
    """ Максимальная периодичность привычки """
    if value > 7:
        raise serializers.ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')


def validate_pleasant_habit(related_habit, reward):
    """ Проверка связи приятной привычки с привычкой и вознаграждением """
    if related_habit is not None or reward is not None:
        raise serializers.ValidationError(
            'У приятной привычки не может быть вознаграждения или связанной привычки'
        )


def validate_useful_habit(related_habit, reward):
    """ Валидация полезной привычки """
    if not related_habit and not reward:
        raise serializers.ValidationError(
            'Полезная привычка должна иметь либо связанную приятную привычку, либо вознаграждение'
        )
    elif related_habit and reward:
        raise serializers.ValidationError(
            'Нельзя за полезную привычку получить и приятную привычку и вознаграждение'
        )
    elif related_habit and not reward:
        habit = get_object_or_404(Habit, pk=related_habit.pk)
        # Если связанная привычка полезная
        if not habit.is_pleasant_habit:
            raise serializers.ValidationError(
                'За полезную привычку можно получить приятную привычку'
            )
