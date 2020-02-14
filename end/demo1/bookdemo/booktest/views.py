from django.shortcuts import render, redirect
from django.template import loader
from .models import Book, Hero

# Create your views here.
# 3、编写需要的视图函数

from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    # return HttpResponse("<h1>这是一个首页</h1>")

    # 获取模板 需要导入 from django.template import loader
    # template = loader.get_template('index.html')
    # 渲染模板数据 数据需要导入 from .models import Book, Hero
    books = Book.objects.all()
    # context = {"books": books}
    # result = template.render(context)
    # 将渲染结果使用HttpResponse返回
    # return HttpResponse(result)

    return render(request, 'index.html', {'books': books})


def about(request):
    return HttpResponse("这是一个详情页")


def detail(request, bookid):
    # template = loader.get_template('detail.html')
    book = Book.objects.get(id=bookid)
    # context = {'book': book}
    # result = template.render(context)
    # return HttpResponse(result)
    return render(request, 'detail.html', {'book': book})


def deletebook(request, bookid):
    book = Book.objects.get(id=bookid)
    book.delete()
    # return HttpResponse("删除成功")
    # 数据交互后返回原页
    # return HttpResponseRedirect(redirect_to='/')
    return redirect(to='/')

# 使用 djang 模板
