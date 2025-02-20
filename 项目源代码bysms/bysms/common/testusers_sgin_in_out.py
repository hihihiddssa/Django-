# -*- coding: utf-8 -*-
from django.http import JsonResponse
from.models import testusers, Customer

#urls路由到localhost/api/mgr/testusers，然后执行我新写的分发函数在mgr/testusers分发post/get请求。
#可以对表进行增删查改操作了
#在common/testusers_sgin_in_out中正在写校验函数


# 登录处理
def signin(request):
    # 从 HTTP POST 请求中获取用户名、密码参数
    userName = request.POST.get('username')
    passWord = request.POST.get('password')

    print('username:',userName)
    print('password:',passWord)


'''
    # 遍历 testusers 表进行校验
    user_testusers = testusers.objects.filter(name=userName, password=passWord).first()
    if user_testusers:
        return JsonResponse({'ret': 0})

    # 遍历 Customer 表进行校验
    user_customer = Customer.objects.filter(name=userName, password=passWord).first()
    if user_customer:
        return JsonResponse({'ret': 0})

    # 否则就是用户名、密码有误
    return JsonResponse({'ret': 1, 'msg': '用户名或者密码错误'})


# 登出处理
def signout(request):
    # 使用登出方法
    logout(request)
    return JsonResponse({'ret': 0})
'''