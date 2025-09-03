from django.contrib import admin

# Register your models here.
from .models import Profile


class myAdmin(admin.ModelAdmin):
    pass



admin.site.register(Profile,myAdmin)