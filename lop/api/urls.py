from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import schema_view, include_docs_urls

urlpatterns = [
    url(r'^api/$', schema_view),
    url(r'^docs/', include_docs_urls(title='Lights-Out Patching', public=False))
]

urlpatterns = format_suffix_patterns(urlpatterns)
