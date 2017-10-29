from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.conf import settings

def index(request):
    return render(request, 'dashboard.html')
