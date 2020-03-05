import scrapy
from scrapy_djangoitem import DjangoItem

from microblog.models import HotSpot


class WeiboItem(DjangoItem):
    # define the fields for your item here like:
    django_model = HotSpot
