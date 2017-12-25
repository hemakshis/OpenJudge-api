# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.contrib import admin


from django.apps import apps

myapp = apps.get_app_config('problems')
for model in myapp.get_models():
    admin.site.register(model)