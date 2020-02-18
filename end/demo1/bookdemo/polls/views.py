from django.shortcuts import render, redirect, reverse
from .models import Headline, Option
from django.views.generic import View, TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView


# Create your views here.


def polls(request):
    headlines = Headline.objects.all()
    return render(request, 'polls.html', {'headlines': headlines})


# <!--{% url 'polls:details' headline.id %}-->
class HeadlineView(ListView):
    # 方法二、继承ListView
    # template_name指明使用的模板
    template_name = "polls.html"
    # queryset 指明返回的结果列表
    queryset = Headline.objects.all()
    # context_object_name 指明返回字典参数的健
    context_object_name = "headlines"

    # 方法一、继承的TemplateView
    # template_name = "polls/index.html"
    # def get_context_data(self, **kwargs):
    #     return {"questions":Headline.objects.all()}


def details(request, headlineid):
    headline = Headline.objects.get(id=headlineid)
    return render(request, 'details.html', {'headline': headline})


class DetailsView(View):

    def get(self, request, headlineid):
        headline = Headline.objects.get(id=headlineid)
        return render(request, 'details.html', {'headline': headline})


def result(request, headlineid):
    headline = Headline.objects.get(id=headlineid)
    if request.method == 'POST':
        optionid = request.POST.get("content")
        option = Option.objects.get(id=optionid)
        option.num = option.num + 1
        option.save()
        url = reverse("polls:result", args=(headlineid,))
        return redirect(to=url)
    elif request.method == 'GET':
        return render(request, 'result.html', {'headline': headline})


class ResultView(View):
    def get(self, request, headlineid):
        headline = Headline.objects.get(id=headlineid)
        return render(request, 'result.html', {'headline': headline})
    def post(self, request, headlineid):
        optionid = request.POST.get("content")
        option = Option.objects.get(id=optionid)
        option.num = option.num + 1
        option.save()
        url = reverse("polls:result", args=(headlineid,))
        return redirect(to=url)