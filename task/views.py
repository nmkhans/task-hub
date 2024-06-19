from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task
import datetime

# Create your views here.
def add_task(req):
  if req.method == 'POST':
    form = TaskForm(req.POST)

    if form.is_valid():
      form.save()
      return redirect('home')
  else:
    form = TaskForm()

  return render(req, 'task/add_task.html', {'form': form})

def edit_task(req, id):
  task = Task.objects.get(pk = id)

  if req.method == 'POST':
    form = TaskForm(req.POST, instance = task)

    if form.is_valid():
      form.cleaned_data['date'] = datetime.date.today().strftime('%Y-%m-%d')

      form.save()
      return redirect('home')
  else:
    form = TaskForm(instance = task)

  return render(req, 'task/edit_task.html', {'form': form})