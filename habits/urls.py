from django.urls import path
from habits import views
from habits.apps import HabitsConfig

app_name = HabitsConfig.name

urlpatterns = [
    path('', views.HabitList.as_view(), name='habits-list'),
    path('create/', views.HabitCreate.as_view(), name='habit-create'),
    path('detail/<int:pk>', views.HabitDetail.as_view(), name='habit-detail'),
    path('update/<int:pk>', views.HabitUpdate.as_view(), name='habit-update'),
    path('delete/<int:pk>', views.HabitDelete.as_view(), name='habit-delete'),
    path('public/', views.HabitPublicList.as_view(), name='habit-public-list'),
]
