import requests
from config.settings import TELEGRAM_API_KEY
from habits.models import Habit

telegram_token = TELEGRAM_API_KEY
send_message_url = f'https://api.telegram.org/bot{telegram_token}/sendMessage'


def send_telegram_message(habit_id):
    """ Функция отправки сообщения в телеграм """
    habit = Habit.objects.get(id=habit_id)
    response = requests.post(
        url=send_message_url,
        data={
            'chat_id': habit.user.telegram_id,
            'text':  (f'Привет, {habit.user}!'
                     f'Сегодня в {habit.time} в {habit.place}'
                     f'тебе надо выполнить {habit.action} в течение {habit.duration_time} секунд.')
        })
    return response
