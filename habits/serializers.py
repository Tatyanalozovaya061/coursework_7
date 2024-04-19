from rest_framework import serializers
from habits.models import Habit
from habits.validators import max_time, max_periodicity, validate_pleasant_habit, validate_useful_habit


class HabitSerializer(serializers.ModelSerializer):
    """ Сериализатор модели привычки """
    duration_time = serializers.IntegerField(validators=[max_time])
    periodicity = serializers.IntegerField(validators=[max_periodicity])

    def validate(self, attrs):
        """Валидация группы полей"""
        related_habit = attrs.get('related_habit', None)
        reward = attrs.get('reward', None)
        is_pleasant_habit = attrs.get('is_pleasant_habit')
        # Если привычка приятная
        if is_pleasant_habit:
            validate_pleasant_habit(related_habit, reward)
        # Иначе если привычка полезная
        else:
            validate_useful_habit(related_habit, reward)
            if not attrs.get('place'):
                raise serializers.ValidationError('поле не может быть пустым')
            if not attrs.get('duration_time'):
                raise serializers.ValidationError('поле не может быть пустым')
        return attrs

    class Meta:
        model = Habit
        fields = '__all__'
        read_only_fields = ['user']
