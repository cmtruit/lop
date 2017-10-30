from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import schema_view

urlpatterns = [
    url(r'^api/$', schema_view),
]

urlpatterns = format_suffix_patterns(urlpatterns)
