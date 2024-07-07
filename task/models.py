from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Task(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
