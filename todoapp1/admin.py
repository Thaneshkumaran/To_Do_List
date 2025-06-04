from django.contrib import admin
from .models import task, status, CustomUser
# Register your models here.
# include('todoapp1.models')
admin.site.register(task)
admin.site.register(status)
admin.site.register(CustomUser)