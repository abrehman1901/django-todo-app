from django.urls import path
from . import views

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("signup/", views.signup, name="signup"),

    path("edit/<int:pk>/", views.edit_task, name="edit_task"),
    path("toggle/<int:pk>/", views.toggle_task, name="toggle_task"),
    path("delete/<int:pk>/", views.delete_task, name="delete_task"),
    path("clear-completed/", views.clear_completed, name="clear_completed"),
]
