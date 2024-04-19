from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """ Тестирование привычек """
    def setUp(self):
        self.user = User.objects.create(
            name='test',
            email='test@test.ru',
            password='test')

        self.habit = Habit.objects.create(
            user=self.user,
            place='дом',
            time='08:00:00',
            action='1 стакан воды',
            is_pleasant_habit=False,
            related_habit=None,
            reward='',
            periodicity=1,
            is_public=False,
            duration_time='00:01:00',
        )
        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        """ Тест создания привычки """
        url = reverse('habits:habit-create')
        data = {
            'place': 'дом',
            'time': '08:00:00',
            'action': '1 стакан воды',
            'reward': 'прогулка',
            'is_pleasant_habit': False,
            'is_public': False,
            'periodicity': 1,
            'duration_time': 120,
        }

        response = self.client.post(path=url, data=data)
        print(response.json())

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
#
#     def test_list_habit(self):
#         """ Тест списка привычек """
#         response = self.client.get(reverse('habits:habits-list'))
#
#         self.assertEquals(response.status_code, status.HTTP_200_OK)
#         print(response.json())
#
#         self.assertEquals(
#             response.json(),
#             {
#                 'count': 1,
#                 'next': None,
#                 'previous': None,
#                 'results': [{
#                         'id': self.habit.id,
#                         'place': self.habit.place,
#                         'time': self.habit.time,
#                         'action': self.habit.action,
#                         'is_pleasant_habit': self.habit.is_pleasant_habit,
#                         'periodicity': self.habit.periodicity,
#                         'reward': self.habit.reward,
#                         'duration_time': self.habit.duration_time,
#                         'is_public': self.habit.is_public,
#                         'user': self.user.id,
#                         'related_habit': self.habit.related_habit.id
#                 }]}
#         )
#
#     def test_detail_habit(self):
#         """ Тест просмотра привычки """
#         url = reverse('habits:habit-detail', kwargs={'pk': self.habit.id})
#         response = self.client.get(path=url)
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(
#             response.json(),
#             {
#                 'id': self.habit.id,
#                 'place': self.habit.place,
#                 'time': self.habit.time,
#                 'action': self.habit.action,
#                 'is_pleasant_habit': self.habit.is_pleasant_habit,
#                 'periodicity': self.habit.periodicity,
#                 'reward': self.habit.reward,
#                 'duration_time': self.habit.duration_time,
#                 'is_public': self.habit.is_public,
#                 'user': self.user.id,
#                 'related_habit': self.habit.related_habit.id
#             }
#         )
#
#     def test_update_habit(self):
#         """ Тест редактирования привычки """
#         url = reverse('habits:habit-update', kwargs={'pk': self.habit.id})
#         data = {
#             'time': 120,
#             'periodicity': 1,
#             'action': '2 стакана воды',
#             'reward': 'прогулка',
#         }
#         response = self.client.patch(path=url, data=data)
#         # Проверка статуса ответа
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_delete_habit(self):
#         """ Тест удаления привычки """
#         url = reverse('habits:habit-delete', kwargs={'pk': self.habit.id})
#         response = self.client.delete(path=url)
#
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
