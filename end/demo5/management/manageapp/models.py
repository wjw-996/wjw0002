from django.db import models


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=15, verbose_name="部门名")

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=15, verbose_name="员工名")
    gender = models.CharField(max_length=5, null=True, blank=True, verbose_name="性别")
    age = models.CharField(max_length=5, null=True, blank=True, verbose_name="年龄")
    position = models.CharField(max_length=20, verbose_name="职位")
    salary = models.IntegerField(verbose_name="工资")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="部门", related_name="depars")

    def __str__(self):
        return self.name
