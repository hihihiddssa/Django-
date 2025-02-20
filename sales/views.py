from django.http import HttpResponse
from common.models import Customer
#from django.shortcuts import render

#定义html的模板
html_template ='''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
table {
    border-collapse: collapse;
}
th, td {
    padding: 8px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}
</style>
</head>
    <body>
        <table>
        <tr>
        <th>id</th>
        <th>姓名</th>
        <th>电话号码</th>
        <th>地址</th>
        </tr>

        %s


        </table>
    </body>
</html>
'''


# Create your views here.
def listorders(request):
    #zhangsan = Customer.object.get(name='zhangsan')
    return HttpResponse("下面是系统中所有的订单信息000。。。AGCL")

#访问sales/customers/时候给出customer数据表
def listcustomers(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Customer.objects.values()

    # 检查url中是否有参数phonenumber
    ph = request.GET.get('phonenumber',None)

    # 如果有，添加过滤条件
    if ph:
        qs = qs.filter(phonenumber=ph)

    # 生成html模板中要插入的html片段内容
    tableContent = ''#初始化空字符串
    for customer in  qs:
        tableContent += '<tr>'#在每次遍历一个客户记录时，先添加一个 HTML 的表格行开始标签 <tr>，表示开始构建一个新的表格行

        for name,value in customer.items():
            tableContent += f'<td>{value}</td>'#为每个字段值创建一个 HTML 的表格数据单元格 <td>

        tableContent += '</tr>'#添加一个 HTML 的表格行结束标签 </tr>

    return HttpResponse(html_template % tableContent)#在%s处拼接tableContent
