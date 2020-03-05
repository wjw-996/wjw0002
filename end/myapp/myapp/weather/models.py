from django.db import models


class Weather(models.Model):
    city = models.CharField(max_length=10, verbose_name="城市")
    max_temperature = models.CharField(max_length=10, verbose_name="最高温度")
    min_temperature = models.CharField(max_length=10, verbose_name="最低温度")
    condition = models.CharField(max_length=10, verbose_name='天气')
    wind = models.CharField(max_length=20, verbose_name='风力')
    uv = models.CharField(max_length=20, verbose_name="紫外线强度")
    air = models.CharField(max_length=20, verbose_name="空气质量")

    def __str__(self):
        return self.city
