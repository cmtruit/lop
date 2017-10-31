import os
import lop.settings
from django.contrib.auth.models import User

u = User.objects.get(username='admin')
if not u:
    user = User.objects.create_user('admin', 'admin@lop.localhost.com', 'lightsout')
    user.last_name = 'admin'
    user.save()
else:
    print("User 'admin' Exists.. Nothing to do")
