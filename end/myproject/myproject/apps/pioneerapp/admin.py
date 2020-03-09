from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(AuthorType)
admin.site.register(ArticleType)
admin.site.register(ThematicType)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Thematic)
admin.site.register(User)
admin.site.register(Comment)

