from django.contrib import admin
from .models import *


# Register your models here.
class OptionInline(admin.StackedInline):
    model = Option
    extra = 1


class OptionAdmin(admin.ModelAdmin):
    pass


class HeadlineAdmin(admin.ModelAdmin):
    inlines = [OptionInline]


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(Headline, HeadlineAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(User, UserAdmin)
