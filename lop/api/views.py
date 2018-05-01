# -*- coding: utf-8 -*-
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import response, schemas
schema_view = get_swagger_view(title='Lights-Out Patching API')

@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='Lights-Out Patching')
    return response.Response(generator.get_schema())

