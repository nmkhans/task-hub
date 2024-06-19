from django.urls import path
from . import views

urlpatterns = [
    path('add-task/', views.add_task, name = 'add-task'),
    path('edit-task/<int:id>', views.edit_task, name = 'edit-task'),
    path('delete-task/<int:id>', views.delete_task, name = 'delete-task'),
]
