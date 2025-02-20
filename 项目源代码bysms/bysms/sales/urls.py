from django.urls import path
from sales.views import *


#这里现在是二级路由表了
urlpatterns = [

    path('orders/', listorders),#当http请求是sales/orders/时，使用listorders函数处理
    path('customers/',listcustomers),

]
