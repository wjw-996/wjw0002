# 每一个路由文件必须编写路由数组 urlpatterns
from django.conf.urls import url
from . import views

# 从视图文件views中导入所有视图函数
app_name = "booktest"

# 2、将路由与视图函数绑定
urlpatterns = [
    # url(r'^index/$', views.index),
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    # 使用正则分组可以向视图传递参数 同时视图函数中必须有相对应的参数 如：views中方法接受的 bookid 等
    url(r'detail/(\d+)/$', views.detail, name='detail'),
    url(r'^deletebook/(\d+)/$', views.deletebook, name='deletebook'),
    url(r'^deletehero/(\d+)/$', views.deletehero, name='deletehero'),
    url(r'^addhero/(\d+)/$', views.addhero, name='addhero'),
    url(r'^edithero/(\d+)/$', views.edithero, name='edithero'),
    url(r'^addbook/$', views.addbook, name='addbook'),
    url(r'^editbook/(\d+)/$', views.editbook, name='editbook'),
]
