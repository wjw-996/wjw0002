"""myproject URL Configuration

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
from django.conf.urls import url
from django.views.static import serve
from .settings import MEDIA_ROOT
from pioneerapp.views import *
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh

from rest_framework import routers
router = routers.DefaultRouter()
router.register('categorys', CategoryViewSets)
router.register('authortypes', AuthorTypeViewSets)
router.register('articletypes', ArticleTypeViewSets)
router.register('thematictypes', ThematicTypeViewSets)
router.register('authors', AuthorViewSets)
router.register('articles', ArticleViewSets)
router.register('thematics', ThematicViewSets)
router.register('comments', CommentViewSets)
router.register('users', UserViewSets)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),
    url('media/(?P<path>.*)', serve, {'document_root': MEDIA_ROOT}),
    url(r'^login1/$', token_obtain_pair, name="login"),
    url(r'^refresh/$', token_refresh, name="refresh"),
    path('api/v1/', include(router.urls)),
    path('', include('rest_framework.urls'))
]
