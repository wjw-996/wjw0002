from rest_framework import serializers
from .models import *


class DepartmentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=10, min_length=2, error_messages={
        "max_length": "最多10个字",
        "min_length": "最少2个字"
    })

    def create(self, validated_data):
        instance = Department.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=10, min_length=2, error_messages={
        "max_length": "最多10个字",
        "min_length": "最少2个字"
    })
    gender = serializers.CharField(max_length=10)
    age = serializers.CharField(max_length=10)
    position = serializers.CharField(max_length=20, min_length=2, error_messages={
        "max_length": "最多20个字",
        "min_length": "最少2个字"
    })
    salary = serializers.IntegerField()
    department = serializers.CharField(source='department.name', read_only=True)

    def create(self, validated_data):
        instance = Employee.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.gender = validated_data.get("gender", instance.gender)
        instance.age = validated_data.get("age", instance.age)
        instance.position = validated_data.get("position", instance.position)
        instance.salary = validated_data.get("salary", instance.salary)
        instance.save()
        return instance
