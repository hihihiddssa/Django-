# -*- coding: utf-8 -*-
from django.urls import path
from mgr import customer
from mgr import sign_in_out
from .views import *



#这里现在是二级路由表了
urlpatterns = [
    path('process/', ocr_process),
]