from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# 모델 생성
# Account 와 Profile과 1대1 매칭
class Profile(models.Model):
  # on_delete => user객체가 없어질 때 profile 객체가 하는 행동
  # CASCADE => profile도 없어진다는 뜻
  # related_name => user의 profile에 접근할 수 있도록 이름을 적어준 것
  # ex) request.user.profile
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

  # 프로필 사진!
  # upload_to => 서버 내부에 이미지가 어디에 저장될 것인지를 정해주는 경로
  # media 경로 밑에 profile 폴더가 생성된다.
  # 거기에 이미지들이 저장
  image = models.ImageField(upload_to='profile/', null=True)
  nickname = models.CharField(max_length=20, unique=True, null=True)
  message = models.CharField(max_length=100, null=True)

