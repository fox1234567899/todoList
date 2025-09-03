from django.contrib import admin
from .models import MyPost


class MyAdminPost(admin.ModelAdmin):
    pass



admin.site.register(MyPost,MyAdminPost)
