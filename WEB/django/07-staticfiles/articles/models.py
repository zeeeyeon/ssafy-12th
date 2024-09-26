from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # pip install Pillow 설치 후 ImageField 사용 가능
    # upload_to : 미디어 루트 이후 images 공간을 만들겠음
    # image = models.ImageField(blank=True, upload_to='images/')
    image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')
