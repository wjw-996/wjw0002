from django.db import models


# Create your models here.
class Headline(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "投票表"
        verbose_name_plural = verbose_name
        # ordering = ["-create_time"]


class Option(models.Model):
    content = models.CharField(max_length=20)
    num = models.IntegerField(default=0)
    headline = models.ForeignKey(Headline, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "选项表"
        verbose_name_plural = "选项表"
        # ordering = ["-create_time"]
