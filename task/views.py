from django.shortcuts import render, redirect
from .forms import TaskForm

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