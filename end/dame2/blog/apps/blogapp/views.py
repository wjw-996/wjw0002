from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator, Page


# Create your views here.

def index(request):
    ads = Ads.objects.all()
    # category = Category.objects.all()
    # tag = Tag.objects.all()

    typeage = request.GET.get("type")
    year = None
    month = None
    category_id = None
    if typeage == "date":
        year = request.GET.get("year")
        month = request.GET.get("month")
        article = Article.objects.filter(create_time__year=year, create_time__month=month).order_by("-create_time")
    elif typeage == "category":
        category_id = request.GET.get("category_id")
        try:
            category = Category.objects.get(id=category_id)
            article = category.article_set.all()
        except Exception as e:
            return HttpResponse("分类不合法")
    elif typeage == "tag":
        tag_id = request.GET.get("tag_id")
        try:
            tag = Tag.objects.get(id=tag_id)
            article = tag.article_set.all()
        except Exception as e:
            return HttpResponse("标签不合法")
    else:
        article = Article.objects.all().order_by("-create_time")

    paginator = Paginator(article, 2)
    num = request.GET.get("pagenumber", 1)
    page = paginator.get_page(num)
    # return render(request, "index.html", {"ads": ads, "page": page, "type": typeage, "year": year, "month": month})
    return render(request, "index.html", locals())
    # return HttpResponse("首页")


def detail(request, articleid):
    try:
        article = Article.objects.get(id=articleid)
    except Exception as e:
        print(e)
        return HttpResponse("内容不存在")
    return render(request, "single.html", {"article": article})
    # return HttpResponse("detail")


def contact(request):
    return render(request, "contact.html")
    # return HttpResponse("contact")


def favicon(request):
    # 如果获取logo则重定向到一个图片资源
    return redirect(to="/static/favicon.ico")
