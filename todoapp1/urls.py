"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.task_list, name="index1"),
    path("task_list/", views.task_list1, name="task_list"),
    path("add_task/<int:id>/", views.add_task, name="add_task"),
    path("change_status/<int:id>/", views.change_post, name="change_status"),
    path("delete_post/<int:id>/", views.delete_task, name="delete_task"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("user_profile/", views.user_profile, name="user_profile"),
]
