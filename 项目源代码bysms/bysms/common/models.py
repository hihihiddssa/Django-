#定义 数据库表 通常是在models.py里面
from django.db import models
# Create your models here.


###########
class testusers(models.Model):#用来重写登录界面的。
    name = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=200)
    password = models.CharField(max_length=200, null=True, blank=True)
###########


#django中是通过定义类来定义数据库的
class Customer(models.Model):#这个 Customer 类继承自 django.db.models.Model， 就是用来定义数据库表的
    #方法就是定义字段
    # 客户名称
    name = models.CharField(max_length=200)#CharField意思就是字符串数据类型最大长度是200个（varchar）

    # 联系电话
    phonenumber = models.CharField(max_length=200)

    # 地址
    address = models.CharField(max_length=200)

    #密码
    password = models.CharField(max_length=200,null=True,blank=True)

    # QQ号
    qq=models.CharField(max_length=30,null=True,blank=True)






