from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



@login_required
def index(request):
    return render(request, 'dashboard.html')
