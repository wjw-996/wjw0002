from django.db import models


# Create your models here.
class Headline(models.Model):
    title = models.CharField(max_length=30)


class Option(models.Model):
    content = models.CharField(max_length=20)
    num = models.IntegerField(default=0)
    headline = models.ForeignKey(Headline, on_delete=models.CASCADE)
