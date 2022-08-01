from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Article(models.Model):
  # SET_NULL : 회원 탈퇴를 했을 때 Article이 사라지지 않고 주인없는 게시글이 되도록
  writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)

  title = models.CharField(max_length=200, null=True)
  image = models.ImageField(upload_to='articles/', null=False)
  content = models.TextField(null=True)

  created_at = models.DateField(auto_created=True, null=True)
