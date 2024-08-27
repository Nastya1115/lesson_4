import sys
import os
import django
from app_users.models import *

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

user1 = Users(name='name1', email='email@gmail.com',role='Admin')

group = Group(group_name='group1')

user1.save()
group.save()