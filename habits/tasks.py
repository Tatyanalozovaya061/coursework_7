from datetime import datetime, timezone, timedelta
from celery import shared_task
from django.db.models import F
from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def send_notification():
    """ Функция отправки уведомлений пользователям """
    current_time = datetime.now(timezone.utc)
    # получение всех полезных привычек, у которых время начала выполнения меньше либо равно текущему
    habits = Habit.objects.all().filter(time__lte=current_time, is_pleasant_habit=False)
    if habits:
        for habit in habits:
            send_telegram_message(habit)
            habit.time = F('time') + timedelta(days=habit.periodicity)
            habit.save()
