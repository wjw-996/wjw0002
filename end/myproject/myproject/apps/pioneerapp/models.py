from django.db import models
from django.contrib.auth.models import AbstractUser
from DjangoUeditor.models import UEditorField


# Create your models here.
class AuthorType(models.Model):
    type_name = models.CharField(max_length=10, blank=True, verbose_name='作者类别')

    def __str__(self):
        return self.type_name


class ArticleType(models.Model):
    type_name = models.CharField(max_length=10, blank=True, verbose_name='文章类别')

    def __str__(self):
        return self.type_name


class ThematicType(models.Model):
    type_name = models.CharField(max_length=10, blank=True, verbose_name='专题类别')

    def __str__(self):
        return self.type_name


class User(AbstractUser):
    telephone = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号')

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=10, verbose_name='分类')

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=10, verbose_name="姓名")
    introduction = models.CharField(max_length=50, null=True, blank=True, verbose_name='介绍')
    avatar = models.ImageField(upload_to='authorimg', null=True, blank=True, verbose_name="头像")
    authorType = models.ForeignKey(AuthorType, on_delete=models.CASCADE, verbose_name='作者类别',
                                   related_name='author_types')
    user = models.ManyToManyField(User, verbose_name='用户关注')
    authoruser = models.OneToOneField(User, models.CASCADE, verbose_name="作者用户", related_name="authorusers")

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    titleimg = models.ImageField(upload_to='articleimg', null=True, blank=True, verbose_name="标题图")
    introduction = models.CharField(max_length=50, null=True, blank=True, verbose_name='介绍')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='作者', related_name='articles')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类',
                                 related_name='article_categorys')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    body = UEditorField(imagePath='imgs/', width='100%', verbose_name="文章内容")
    likes = models.CharField(max_length=20, default="0", verbose_name='点赞数')
    read_num = models.CharField(max_length=20, default="0", verbose_name="阅读数")
    articleType = models.ForeignKey(ArticleType, on_delete=models.CASCADE, verbose_name='文章类别',
                                    related_name='article_types')
    user = models.ManyToManyField(User, verbose_name='文章收藏')

    def __str__(self):
        return self.title


class Thematic(models.Model):
    title = models.CharField(max_length=50, verbose_name='专题标题')
    titleimg = models.ImageField(upload_to='thematicimg', verbose_name="专题图")
    introduction = models.CharField(max_length=50, null=True, blank=True, verbose_name='介绍')
    read_num = models.CharField(max_length=20, verbose_name="阅读数")
    article = models.ManyToManyField(Article, verbose_name='专题文章')
    thematicType = models.ForeignKey(ThematicType, on_delete=models.CASCADE, verbose_name='专题类别',
                                     related_name='thematic_types')
    user = models.ManyToManyField(User, verbose_name='专题收藏')

    def __str__(self):
        return self.title


class Comment(models.Model):
    body = models.TextField(max_length=500, verbose_name='评论')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='评论用户', related_name='users')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True, verbose_name='评论文章',
                                related_name='articles')
    thematic = models.ForeignKey(Thematic, on_delete=models.CASCADE, null=True, blank=True, verbose_name='评论专题',
                                 related_name='thematics')
    agree = models.CharField(max_length=20, default="0", verbose_name='赞同数')
    Against = models.CharField(max_length=20, default="0", verbose_name='反对数')

    def __str__(self):
        return self.user.username
