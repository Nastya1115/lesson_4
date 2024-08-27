from django.db import models

# Create your models here.

class Group(models.Model):
    group_name = models.CharField(max_length=20)

class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    role = models.CharField(max_length=10, choices=[("User", "Admin")], default="User")
    group = models.ManyToManyField(Group, related_name="user")
