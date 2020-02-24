from django.contrib.syndication.views import Feed
from .models import *
from django.shortcuts import reverse

class ArticleFeed(Feed):
    title = "读书屋"
    description = "享受午后的阳光，体会万千世界"
    link = "/"

    def items(self):
        return Article.objects.all().order_by("-create_time")[:3]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.author

    def item_link(self, item):
        # return "/detail/"+item.id+"/"
        url = reverse("blogapp:detail", args=(item.id,))
        return url
