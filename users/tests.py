from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from users.models import User


class UserTestCase(APITestCase):
    """ Тестирование пользователя """
    def setUp(self):
        self.user = User.objects.create(
            name='test',
            email='test@test.ru',
            password='12345',
            telegram_id=None
        )
        self.client.force_authenticate(user=self.user)

    def test_create_user(self):
        """ Тест создания пользователя """
        url = reverse('users:user-create')
        data = {
            'name': 'test',
            'email': 'test_create@test.ru',
            'password': '12345',
        }
        response = self.client.post(path=url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.json()['email'],
            'test_create@test.ru'
        )

    def test_list_user(self):
        """ Тест списка пользователей """

        url = reverse('users:users-list')
        response = self.client.get(path=url)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        print(response.data)
        # self.assertEquals(
        #     response.json(),
        #     [
        #         {
        #             'id': 5,
        #             'password': '12345',
        #             # 'last_login': None,
        #             # 'is_superuser': False,
        #             # 'first_name': '',
        #             # 'last_name': '',
        #             'is_staff': False,
        #             'is_active': True,
        #             # 'date_joined': '2024-04-08T11:45:54.498887+03:00',
        #             'name': 'test',
        #             'email': 'test@test.ru',
        #             # 'phone': None,
        #             # 'telegram_id': None,
        #             # 'groups': [],
        #             # 'user_permissions': []
        #         }
        #     ]
        # )

    def test_detail_user(self):
        """ Тест детализации профиля пользователя """

        url = reverse('users:user-detail', kwargs={'pk': self.user.id})
        response = self.client.get(path=url)
        # print(response.data)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json()['email'],
            'test@test.ru'
        )

    def test_update_user(self):
        """ Тест редактирования профиля пользователя """

        url = reverse('users:user-update', kwargs={'pk': self.user.id})
        response = self.client.patch(
            path=url,
            data={'first_name': 'test name'})

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json()['first_name'],
            "test name"
        )

    def test_delete_user(self):
        """ Тест удаления пользователя """

        url = reverse('users:user-delete', kwargs={'pk': self.user.id})
        response = self.client.delete(path=url)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(User.objects.get(pk=self.user.pk).is_active)
