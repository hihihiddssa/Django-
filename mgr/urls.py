# -*- coding: utf-8 -*-
from django.urls import path
from mgr import customer
from mgr import sign_in_out




#这里现在是二级路由表了
urlpatterns = [
    #customer列表操作路由
    path('customers', customer.dispatcher),
    #管理员登入登出路由
    path('signin', sign_in_out.signin),
    path('signout', sign_in_out.signout),

]
