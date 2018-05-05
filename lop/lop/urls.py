from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^', include('api.urls')),
    url(r'^login/$', auth_views.login,  name='login'),
    url(r'^accounts/login/$', auth_views.login),
    url(r'^logout/$', auth_views.logout, {'template_name': 'registration/logged_out.html'}, name='logout'),
    url(r'viewprofile/(?P<username>[a-zA-Z0-9]+)$', views.view_user_profile),
    url(r'^avatar/', include('avatar.urls')),
    path('signup/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

#if settings.DEBUG is True:
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

