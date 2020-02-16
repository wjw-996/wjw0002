from django.shortcuts import render, redirect, reverse
from .models import Headline, Option


# Create your views here.


def polls(request):
    headlines = Headline.objects.all()
    return render(request, 'polls.html', {'headlines': headlines})


def details(request, hesdlineid):
    headline = Headline.objects.get(id=hesdlineid)
    return render(request, 'details.html', {'headline': headline})


def result(request, hesdlineid):
    headline = Headline.objects.get(id=hesdlineid)
    if request.method == 'POST':
        optionid = request.POST.get("content")
        option = Option.objects.get(id=optionid)
        option.num = option.num + 1
        option.save()
        url = reverse("polls:result", args=(hesdlineid,))
        return redirect(to=url)
    elif request.method == 'GET':
        return render(request, 'result.html', {'headline': headline})
