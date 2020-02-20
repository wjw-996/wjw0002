from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request):
    ads = Ads.objects.all()
    return render(request,"index.html",locals())
    # return HttpResponse("首页")


def detail(request, articleid):
    return render(request, "single.html")
    # return HttpResponse("detail")


def contact(request):
    return render(request, "contact.html")
    # return HttpResponse("contact")


def favicon(request):
    # 如果获取logo则重定向到一个图片资源
    return redirect(to="/static/favicon.ico")