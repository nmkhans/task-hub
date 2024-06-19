from django.shortcuts import render
from task.models import Task

def home(req):

  tasks = Task.objects.all()
  return render(req, 'index.html', {'tasks': tasks})