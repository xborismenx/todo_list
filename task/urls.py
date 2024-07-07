from django.urls import path

from task.views import TaskListView, TaskCreateView, TagListView, TagCreateView, TagUpdateView, TagDeleteView, \
    TaskUpdateView, TaskDeleteView

app_name = 'task'

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path("tags/", TagListView.as_view(), name='tags_list'),
    path("tags/create/", TagCreateView.as_view(), name='tag_create'),
    path("tags/<int:pk>/", TagUpdateView.as_view(), name='tag_update'),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name='tag_delete'),

]
