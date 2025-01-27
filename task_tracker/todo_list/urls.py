"""
URL configuration for task_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import *

app_name = "todo_list"
urlpatterns = [
    path("", MainView.as_view(), name="main"),
    path("display_task/", display_task, name="display_task"),
    path("task_details/<int:pk>", DetailView.as_view(), name="task_details"),
    path("add_task", add_task, name="add_task"),
    path("update_task/<int:id>", update_task, name="update_task"),
    path("delete_task/<int:id>", delete_task, name="delete_task"),
]
