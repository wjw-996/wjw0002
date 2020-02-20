from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator, Page


# Create your views here.

def index(request):
    ads = Ads.objects.all()
    category = Category.objects.all()
    article = Article.objects.all()
    tag = Tag.objects.all()

    paginator = Paginator(article, 2)
    num = request.GET.get("pagenumber", 1)
    page = paginator.get_page(num)
    return render(request, "index.html", {"ads": ads, "page": page})
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
