# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

api_view = get_swagger_view(title='Lights-Out Patching API')

urlpatterns = [
    url(r'^/api', api_view)
]
