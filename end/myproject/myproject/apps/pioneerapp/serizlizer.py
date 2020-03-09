from rest_framework import serializers
from .models import *
from DjangoUeditor.models import UEditorField


class CategorySerizlizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["user_permissions", "groups", "is_staff", "is_active"]

    def validate(self, attrs):
        from django.contrib.auth import hashers
        if attrs.get("password"):
            attrs["password"] = hashers.make_password(attrs["password"])
        return attrs


class UserRegistSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20, min_length=3, error_messages={
        "required": "用户名必填"
    })
    password = serializers.CharField(max_length=20, min_length=3, error_messages={
        "required": "密码必填"
    }, write_only=True)
    password2 = serializers.CharField(max_length=20, min_length=3, error_messages={
        "required": "重复密码必填"
    }, write_only=True)

    def validate_password2(self, data):
        print("+++", data, "____")
        print("---", self.initial_data, "____")
        if data != self.initial_data["password"]:
            raise serializers.ValidationError("重复密码不一致！")
        else:
            return data

    def create(self, validated_data):
        return User.objects.create_user(username=validated_data.get("username"), email=validated_data.get("email"),
                                        password=validated_data.get("password"))


class AuthorTypeSerizlizer(serializers.ModelSerializer):
    class Meta:
        model = AuthorType
        fields = "__all__"


class ArticleTypeSerizlizer(serializers.ModelSerializer):
    class Meta:
        model = ArticleType
        fields = "__all__"


class ThematicTypeSerizlizer(serializers.ModelSerializer):
    class Meta:
        model = ThematicType
        fields = "__all__"


class AuthorSerizlizer(serializers.Serializer):
    class Meta:
        model = Author
        fields = "__all__"


class ArticleSerizlizer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class ThematicSerizlizer(serializers.ModelSerializer):
    class Meta:
        model = Thematic
        fields = "__all__"


class CommentSerizlizer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
