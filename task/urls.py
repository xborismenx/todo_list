from django.urls import path

from task.views import TaskListView, TaskCreateView

app_name = 'task'

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task_create')
]

