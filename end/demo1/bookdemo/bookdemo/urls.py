"""bookdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include

# 路由 网址 每一个网址均需要绑定一个视图函数
# MVT V视图函数  3个作用 接受请求 处理数据 返回响应

# from django.http import HttpResponse
#
#
# def index(request):
#     return HttpResponse("这里是首页")
#
#
# def list(request):
#     return HttpResponse("这里是列表页")
#
#
# def jsondata(request):
#     return HttpResponse("{'name':'wjw','age':'23'}")


urlpatterns = [
    # 将路由（例 admin）与视图函数绑定
    path('admin/', admin.site.urls),

    # 1、使用path将booktest中的urls.py路由文件导入绑定
    # path('', include('booktest.urls', namespace='booktest'))
    path('', include('polls.urls', namespace='polls'))
    # path('index/', index),
    # path('list/', list),
    # path('json/', jsondata),
]
