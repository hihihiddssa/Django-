"""
URL configuration for bysms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

# 导入一个include函数
from django.urls import path, include

# 静态文件服务
from django.conf.urls.static import static

#一级路由
urlpatterns = [
    path('admin/', admin.site.urls),

    # 凡是 url 以 sales/  开头的，
    # 都根据 sales.urls 里面的 子路由表进行路由
    path('sales/', include('sales.urls')),

    # 凡是 url 以 api/mgr  开头的，
    # 都根据 mgr.urls 里面的 子路由表进行路由
    path('api/mgr/', include('mgr.urls')),

    path('accounts/', include('accounts.urls')),

    #path('ocr/', include('ocrdata.urls')),

    #path('qwen/', include('qwen.urls')),

]
#+  static("/", document_root="./z_dist")
