# 每一个路由文件必须编写路由数组 urlpatterns
from django.conf.urls import url
from . import views

# 从视图文件views中导入所有视图函数
app_name = "polls"

# 2、将路由与视图函数绑定
urlpatterns = [
    # url(r'^$', views.polls, name='polls'),
    url(r'^$', views.polls, name='polls'),

    # url(r'^details/(\d+)/$', views.details, name='details'),
    url(r'^details/(?P<headlineid>\d+)/$', views.details, name='details'),

    # url(r'^result/(\d+)/$', views.result, name='result'),
    url(r'^result/(\d+)/$', views.result, name='result'),
    url(r'^login/$', views.login, name='login'),
    url(r'^registers/$', views.registers, name='registers'),
    url(r'^logout/$', views.logout, name='logout'),

]
