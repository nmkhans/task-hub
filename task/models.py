from django.db import models
from category.models import Category

# Create your models here.
class Task(models.Model):
  task_title = models.CharField(max_length = 100)
  task_description = models.TextField()
  is_completed = models.BooleanField(default = False)
  category = models.ManyToManyField(Category)
  date = models.DateTimeField()

  def __str__(self):
    return f'Task: {self.task_title}'