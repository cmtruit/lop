from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import SignUpForm

def get_user_obj(username):
    post_save.connect(post_save_create_or_update_profile)
    user = User.objects.get(username=username)
    return user


@login_required
def index(request):
    return render(request, 'dashboard.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def view_user_profile(request, username):
    current_user = request.user.username
    if current_user == username:
        user = request.user
        return render(request, 'registration/view_profile.html', {"user":user})
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
     
