from django.contrib import admin

# Register your models here.

from .models import Article, Cpmment

admin.site.register(Article)
admin.site.register(Cpmment)