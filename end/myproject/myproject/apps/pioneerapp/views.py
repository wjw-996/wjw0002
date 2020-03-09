from django.shortcuts import render
from rest_framework import viewsets
from .serizlizer import *
from rest_framework import mixins
from rest_framework import permissions
from . import permissions as mypermissions


# Create your views here.
class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    # 1通过属性指明
    serializer_class = CategorySerizlizer

    def get_permissions(self):
        if self.action == "create" or self.action == "update" or self.action == "partial_update" or self.action == "destroy":
            return [permissions.IsAdminUser()]
        else:
            return []


class UserViewSets(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    queryset = User.objects.all()

    # serializer_class = UserSerializer
    def get_serializer_class(self):
        if self.action == "create":
            return UserRegistSerializer
        return UserSerializer


class AuthorTypeViewSets(viewsets.ModelViewSet):
    queryset = AuthorType.objects.all()
    # 1通过属性指明
    serializer_class = AuthorTypeSerizlizer

    def get_permissions(self):
        if self.action == "create" or self.action == "update" or self.action == "partial_update" or self.action == "destroy":
            return [permissions.IsAdminUser()]
        else:
            return []


class ArticleTypeViewSets(viewsets.ModelViewSet):
    queryset = ArticleType.objects.all()
    # 1通过属性指明
    serializer_class = ArticleTypeSerizlizer

    def get_permissions(self):
        if self.action == "create" or self.action == "update" or self.action == "partial_update" or self.action == "destroy":
            return [permissions.IsAdminUser()]
        else:
            return []


class ThematicTypeViewSets(viewsets.ModelViewSet):
    queryset = ThematicType.objects.all()
    # 1通过属性指明
    serializer_class = ThematicTypeSerizlizer

    def get_permissions(self):
        if self.action == "create" or self.action == "update" or self.action == "partial_update" or self.action == "destroy":
            return [permissions.IsAdminUser()]
        else:
            return []


class AuthorViewSets(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    # 1通过属性指明
    serializer_class = AuthorSerizlizer

    def get_permissions(self):
        if self.action == "create":
            return [permissions.IsAuthenticated()]
        elif self.action == "update" or self.action == "partial_update" or self.action == "retrieve" or self.action == "destroy":
            return [mypermissions.ArticlePermission()]
        else:
            return [permissions.IsAdminUser]


class ArticleViewSets(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    # 1通过属性指明
    serializer_class = ArticleSerizlizer

    def get_permissions(self):
        if self.action == "create":
            return [permissions.IsAuthenticated()]
        elif self.action == "update" or self.action == "partial_update" or self.action == "retrieve" or self.action == "destroy":
            return [mypermissions.ArticlePermission()]
        else:
            return []


class ThematicViewSets(viewsets.ModelViewSet):
    queryset = Thematic.objects.all()
    # 1通过属性指明
    serializer_class = ThematicSerizlizer

    def get_permissions(self):
        if self.action == "create":
            return [permissions.IsAuthenticated()]
        elif self.action == "update" or self.action == "partial_update" or self.action == "retrieve" or self.action == "destroy":
            return [mypermissions.ArticlePermission()]
        else:
            return []


class CommentViewSets(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    # 1通过属性指明
    serializer_class = CommentSerizlizer

    def get_permissions(self):
        if self.action == "create":
            return [permissions.IsAuthenticated()]
        elif self.action == "update" or self.action == "partial_update" or self.action == "retrieve" or self.action == "destroy":
            return [mypermissions.ArticlePermission()]
        else:
            return []
