from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accountapp.views import hello_world, AccountCreateView

app_name = "accountapp"
# 쓰는 이유? -> 개발 중에는 "127.0.0.1:8000/account/hello_world"
# 그러나 저렇게 다 치기엔 번거로움.
# django 내에서 라우팅을 편하게 해주는 함수가 있어서 저걸 쓴다고 하는군..

urlpatterns = [
  path('hello_world/', hello_world, name='hello_world'),

  # LoginView 같은 경우 템플릿이 필요함.
  path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
  path('logout/', LogoutView.as_view(), name='logout'),

  path('form/', AccountCreateView.as_view(), name='form'),
]