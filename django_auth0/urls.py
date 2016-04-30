# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import auth_callback


urlpatterns = [
    url('callback$', auth_callback, name='auth_callback'),
]
