from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^', include('api.urls')),
    url(r'^login/$', auth_views.login,  name='login'),
    url(r'^accounts/login/$', auth_views.login),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    
]
