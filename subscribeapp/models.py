from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Subscription(models.Model):
  # CASCADE = user가 제거되면 같이 제거
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription')
  project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='subscription')

  # user, project쌍이 가지는 구독 정보가 하나여야 하므로,
  class Meta:
    unique_together = ('user', 'project')
