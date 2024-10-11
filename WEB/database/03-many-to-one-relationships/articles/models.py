# articles/models.py
from django.db import models
from django.conf import settings

class Article(models.Model):
    # setting.py -< installed_apps에 등록한 순서에 영향을 받음
    # 현재 활성화 된 User 모델이 무어인지는 setting.py에 적혀져 있음
    # AUTH_USER_MODEL = 'accounts.User'을 받아옴
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
