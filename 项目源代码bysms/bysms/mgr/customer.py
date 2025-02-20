'''
这个程序是用来分发请求post/get/put等
同时处理查询/修改/添加/删除数据库中的表的
'''

from django.http import JsonResponse
import json
from common.models import Customer

#定义一个分发函数。因为django不支持从url参数直接读取方法类型
def dispatcher(request):
    # 将请求参数统一放入request 的 params 属性中，方便后续处理
    print('到达dispatch处')

    # GET请求 参数在url中，同过request 对象的 GET属性获取
    if request.method == 'GET':#request.method是一个属性，它表示客户端发送请求所使用的 HTTP 方法
        request.params = request.GET#request.GET包含了通过get方法提交的请求参数

    # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
    elif request.method in ['POST','PUT','DELETE']:
        # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
        request.params = json.loads(request.body)


    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']#从名为request.params的对象中获取键为action的值
    if action == 'list_customer':
        return listcustomers(request)
    elif action == 'add_customer':
        return addcustomer(request)
    elif action == 'modify_customer':
        return modifycustomer(request)
    elif action == 'del_customer':
        return deletecustomer(request)

    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})


def listcustomers(request):#列出客户
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Customer.objects.values()

    # 将 QuerySet 对象 转化为 list 类型
    # 否则不能 被 转化为 JSON 字符串
    retlist = list(qs)

    return JsonResponse({'ret': 0, 'retlist': retlist})

def addcustomer(request):#添加客户

    info    = request.params['data']

    # 从请求消息中 获取要添加客户的信息
    # 并且插入到数据库中
    # 返回值 就是对应插入记录的对象
    record = Customer.objects.create(name=info['name'] ,
                            phonenumber=info['phonenumber'] ,
                            address=info['address'])


    return JsonResponse({'ret': 0, 'id':record.id})

def modifycustomer(request):#修改客户

    # 从请求消息中 获取修改客户的信息
    # 找到该客户，并且进行修改操作

    customerid = request.params['id']
    newdata    = request.params['newdata']

    try:
        # 根据 id 从数据库中找到相应的客户记录
        customer = Customer.objects.get(id=customerid)#get方法是查询数据的一种方法
    except Customer.DoesNotExist:
        return  {
                'ret': 1,
                'msg': f'id 为`{customerid}`的客户不存在'
        }


    if 'name' in  newdata:
        customer.name = newdata['name']
    if 'phonenumber' in  newdata:
        customer.phonenumber = newdata['phonenumber']
    if 'address' in  newdata:
        customer.address = newdata['address']

    # 注意，一定要执行save才能将修改信息保存到数据库
    customer.save()

    return JsonResponse({'ret': 0})

def deletecustomer(request):#删除客户

    customerid = request.params['id']

    try:
        # 根据 id 从数据库中找到相应的客户记录
        customer = Customer.objects.get(id=customerid)
    except Customer.DoesNotExist:
        return  {
                'ret': 1,
                'msg': f'id 为`{customerid}`的客户不存在'
        }

    # delete 方法就将该记录从数据库中删除了
    customer.delete()

    return JsonResponse({'ret': 0})


