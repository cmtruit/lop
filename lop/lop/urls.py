from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin 
from .views import signup
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^', include('api.urls')),
    url(r'^login/$', auth_views.login,  name='login'),
    url(r'^accounts/login/$', auth_views.login),
    url(r'^logout/$', auth_views.logout, {'template_name': 'registration/logged_out.html'}, name='logout'),
    url(r'viewprofile/(?P<username>[a-zA-Z0-9]+)$', views.view_user_profile),
    url(r'^avatar/', include('avatar.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    #url(r'^account/', include('accounts.urls')),
    url(r'^signup/$', signup, name='signup'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

#account signup
#from django.conf.urls.default import *

#urlpatterns = patterns('lop.accounts.views', (r'^signup/$', (lop.accounts.urls'))

#if settings.DEBUG is True:
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

