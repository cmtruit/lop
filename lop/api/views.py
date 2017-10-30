# -*- coding: utf-8 -*-
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls
schema_view = get_swagger_view(title='Lights-Out Patching API', url='/api')
