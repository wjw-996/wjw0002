# Generated by Django 3.0.4 on 2020-03-09 11:22

import DjangoUeditor.models
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('telephone', models.CharField(blank=True, max_length=11, null=True, verbose_name='手机号')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('titleimg', models.ImageField(blank=True, null=True, upload_to='articleimg', verbose_name='标题图')),
                ('introduction', models.CharField(blank=True, max_length=50, null=True, verbose_name='介绍')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('body', DjangoUeditor.models.UEditorField(verbose_name='文章内容')),
                ('likes', models.CharField(default='0', max_length=20, verbose_name='点赞数')),
                ('read_num', models.CharField(default='0', max_length=20, verbose_name='阅读数')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(blank=True, max_length=10, verbose_name='文章类别')),
            ],
        ),
        migrations.CreateModel(
            name='AuthorType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(blank=True, max_length=10, verbose_name='作者类别')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='分类')),
            ],
        ),
        migrations.CreateModel(
            name='ThematicType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(blank=True, max_length=10, verbose_name='专题类别')),
            ],
        ),
        migrations.CreateModel(
            name='Thematic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='专题标题')),
                ('titleimg', models.ImageField(upload_to='thematicimg', verbose_name='专题图')),
                ('introduction', models.CharField(blank=True, max_length=50, null=True, verbose_name='介绍')),
                ('read_num', models.CharField(max_length=20, verbose_name='阅读数')),
                ('article', models.ManyToManyField(to='pioneerapp.Article', verbose_name='专题文章')),
                ('thematicType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thematic_types', to='pioneerapp.ThematicType', verbose_name='专题类别')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='专题收藏')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=500, verbose_name='评论')),
                ('agree', models.CharField(default='0', max_length=20, verbose_name='赞同数')),
                ('Against', models.CharField(default='0', max_length=20, verbose_name='反对数')),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='pioneerapp.Article', verbose_name='评论文章')),
                ('thematic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thematics', to='pioneerapp.Thematic', verbose_name='评论专题')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL, verbose_name='评论用户')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='姓名')),
                ('introduction', models.CharField(blank=True, max_length=50, null=True, verbose_name='介绍')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='authorimg', verbose_name='头像')),
                ('authorType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_types', to='pioneerapp.AuthorType', verbose_name='作者类别')),
                ('authoruser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='authorusers', to=settings.AUTH_USER_MODEL, verbose_name='作者用户')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='用户关注')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='articleType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_types', to='pioneerapp.ArticleType', verbose_name='文章类别'),
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='pioneerapp.Author', verbose_name='作者'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_categorys', to='pioneerapp.Category', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='文章收藏'),
        ),
    ]
