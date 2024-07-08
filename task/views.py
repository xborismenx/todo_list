from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from task.forms import TaskCreateUpdateForm
from task.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.all().prefetch_related('tags')
    template_name = "task/task_list.html"
    context_object_name = "task_list"

    def post(self, request, *args, **kwargs):
        if "task_id" in request.POST:
            task_id = request.POST.get("task_id")
            task = Task.objects.get(id=task_id)
            task.done = not task.done
            task.save()
            return redirect("task:task_list")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreateUpdateForm
    success_url = reverse_lazy("task:task_list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskCreateUpdateForm
    success_url = reverse_lazy("task:task_list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task:task_list")


class TagListView(generic.ListView):
    model = Tag
    template_name = "task/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("task:tags_list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("task:tags_list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("task:tags_list")
    template_name = "task/tag_confirm_delete.html"
