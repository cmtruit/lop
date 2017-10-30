from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^', include('api.urls'))
]
