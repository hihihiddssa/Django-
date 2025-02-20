# -*- coding: utf-8 -*-
'''
管理员用户的登入登出处理
'''
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout

# 登录处理
def signin( request):
    # 从 HTTP POST 请求中获取用户名、密码参数
    userName = request.POST.get('username')
    passWord = request.POST.get('password')

    # 使用 Django auth 库里面的 方法校验用户名、密码
    # authenticate 方法会根据 Django 的配置，从默认的数据库中查找用户信息。具体来说，它会查找 django.contrib.auth 应用中定义的用户表，通常是 auth_user 表
    user = authenticate(username=userName, password=passWord)

    # 如果能找到用户，并且密码正确
    if user is not None:
        if user.is_active:
            if user.is_superuser:
                login(request, user)
                # 在session中存入用户类型
                request.session['usertype'] = 'mgr'

                return JsonResponse({'ret': 0})
            else:
                return JsonResponse({'ret': 1, 'msg': '请使用管理员账户登录'})
        else:
            return JsonResponse({'ret': 0, 'msg': '用户已经被禁用'})

    # 否则就是用户名、密码有误
    else:
        return JsonResponse({'ret': 1, 'msg': '用户名或者密码错误'})


# 登出处理
def signout( request):
    # 使用登出方法
    logout(request)#logout去处理request请求中包含的参数
    return JsonResponse({'ret': 0})