from django.contrib import admin
# from . import models
from .models import Article

# Register your models here.
# admin site에 등록하기.
admin.site.register(Article)
