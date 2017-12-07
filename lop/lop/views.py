from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def get_user_obj(username):
    user = User.objects.get(username=username)
    return user
        



@login_required
def index(request):
    return render(request, 'dashboard.html')

@login_required
def view_user_profile(request, username):
    current_user = request.user.username
    if current_user == username:
        user = request.user
        return render(request, 'registration/view_profile.html', {"user":user})
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
     
