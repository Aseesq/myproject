from django.contrib import admin
from .models import *
# Register your models here.

class info1(admin.ModelAdmin):
    list_display=('title',)

admin.site.register(category,info1)

class info2(admin.ModelAdmin):
    list_display=('name','price','stock','image',)

admin.site.register(product,info2)


class info3(admin.ModelAdmin):
    list_display=('username','password',)

admin.site.register(siginup,info3)