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
    # 使用正则分组可以向视图传递参数
    url(r'detail/(\d+)/$', views.detail, name='detail'),
    url(r'^deletebook/(\d+)/$', views.deletebook, name='deletebook')
]
