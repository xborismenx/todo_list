from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=500)
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.content}, tags - {', '.join([tag.name for tag in self.tags.all()])} - deadline: {self.deadline}"
