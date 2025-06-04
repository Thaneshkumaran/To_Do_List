from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    perity=models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.ForeignKey('status', on_delete=models.CASCADE, null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey("CustomUser", on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.title
    
class status(models.Model):
    name= models.CharField(max_length=100)
    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    USER_TYPES = [
        ('1', 'admin'),
        ('2', 'normal_user'),
    ]
    user_type = models.CharField(choices=USER_TYPES, max_length=50, default='2')
