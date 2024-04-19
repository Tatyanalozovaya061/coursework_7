from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitCreate(generics.CreateAPIView):
    """ Создание привычки """
    serializer_class = HabitSerializer
    # queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """ Добавление поля пользователя """
        # serializer.save(user=self.request.user)
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitList(generics.ListAPIView):
    """ Список привычек """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        habits_list = super().get_queryset()
        return habits_list.filter(user=user)


class HabitDetail(generics.RetrieveAPIView):
    """ Информация о привычке """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitUpdate(generics.UpdateAPIView):
    """ Редактирование привычки """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDelete(generics.DestroyAPIView):
    """ Удаление привычки """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitPublicList(generics.ListAPIView):
    """ Список публичных привычек """
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """ Список публичных привычек """
        return Habit.objects.filter(is_public=True)
