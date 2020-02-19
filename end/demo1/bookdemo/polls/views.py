from django.shortcuts import render, redirect, reverse
from .models import Headline, Option, User
from django.views.generic import View, TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth import authenticate, login as lin, logout as lot
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *


# Create your views here.


def polls(request):
    headlines = Headline.objects.all()
    return render(request, 'polls.html', {'headlines': headlines})


# <!--{% url 'polls:details' headline.id %}-->
# class HeadlineView(ListView):
# 方法二、继承ListView
# template_name指明使用的模板
# template_name = "polls.html"
# queryset 指明返回的结果列表
# queryset = Headline.objects.all()
# context_object_name 指明返回字典参数的健
# context_object_name = "headlines"
#
# 方法一、继承的TemplateView
# template_name = "polls/index.html"
# def get_context_data(self, **kwargs):
#     return {"questions":Headline.objects.all()}


def details(request, headlineid):
    if request.user and request.user.username != "":
        headline = Headline.objects.get(id=headlineid)
        if headline in request.user.headlines.all():
            # 判断已经投过票了
            url = reverse("polls:result", args=(headlineid))
            return redirect(to=url)
        else:
            # 没投过票就是用render发起一次请求
            return render(request, "details.html", {'headline': headline})
    else:
        url = reverse("polls:login") + "?next=" + reverse("polls:details", args=(headlineid,))
        return redirect(to=url)


# class DetailsView(View):

# def get(self, request, headlineid):
#     headline = Headline.objects.get(id=headlineid)
#     return render(request, 'details.html', {'headline': headline})


def result(request, headlineid):
    headline = Headline.objects.get(id=headlineid)
    if request.method == 'POST':
        optionid = request.POST.get("content")
        option = Option.objects.get(id=optionid)
        option.num = option.num + 1
        option.save()
        request.user.headlines.add(Headline.objects.get(id=headlineid))
        url = reverse("polls:result", args=(headlineid,))
        return redirect(to=url)
    elif request.method == 'GET':
        return render(request, 'result.html', {'headline': headline})


# class ResultView(View):
#     def get(self, request, headlineid):
#         headline = Headline.objects.get(id=headlineid)
#         return render(request, 'result.html', {'headline': headline})

# def post(self, request, headlineid):
#     optionid = request.POST.get("content")
#     option = Option.objects.get(id=optionid)
# option.num = option.num + 1
# option.save()
# url = reverse("polls:result", args=(headlineid,))
# return redirect(to=url)


def login(request):
    if request.method == 'GET':
        lf = LonginForm()
        return render(request, 'login.html', {"lf": lf})
    elif request.method == 'POST':
        lf = LonginForm(request.POST)
        if lf.is_valid():
            username = lf.cleaned_data["username"]
            password = lf.cleaned_data["password"]
            # username = request.POST.get('username')
            # password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                lin(request, user)
                next = request.GET.get("next")
                print(next)
                if next:
                    url = next
                else:
                    url = reverse("polls:polls")
                return redirect(to=url)
            else:
                return render(request, 'login.html', {'err': '用户名或密码错误'})
        else:
            return HttpResponse("失败")


def registers(request):
    if request.method == 'GET':
        return render(request, 'registers.html')
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        if User.objects.filter(username=username).count() > 0:
            return render(request, 'registers.html', {'err': '用户名已存在'})
        else:
            if password == password2:
                User.objects.create_user(username=username, password=password)
                url = reverse("polls:login")
                return redirect(to=url)
            else:
                return render(request, 'registers.html', {'err': '两次密码不一致'})


def logout(request):
    lot(request)
    url = reverse('polls:polls')
    return redirect(to=url)
