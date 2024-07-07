from django.contrib import admin

from task.models import Tag, Task

admin.site.register(Tag)
admin.site.register(Task)
