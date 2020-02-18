from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    telephone = models.CharField(max_length=11, verbose_name='手机号')
    headlines = models.ManyToManyField('Headline')


class Headline(models.Model):
    title = models.CharField(max_length=30, verbose_name='问题内容')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "投票表"
        verbose_name_plural = verbose_name
        ordering = ["-create_time"]


class Option(models.Model):
    content = models.CharField(max_length=20, verbose_name='选项')
    num = models.IntegerField(default=0, verbose_name='得票数')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    headline = models.ForeignKey(Headline, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "选项表"
        verbose_name_plural = "选项表"
        ordering = ["-create_time"]
