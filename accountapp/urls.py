from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accountapp.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView

app_name = "accountapp"
# 쓰는 이유? -> 개발 중에는 "127.0.0.1:8000/account/hello_world"
# 그러나 저렇게 다 치기엔 번거로움.
# django 내에서 라우팅을 편하게 해주는 함수가 있어서 저걸 쓴다고 하는군..

urlpatterns = [
  path('hello_world/', hello_world, name='hello_world'),

  # LoginView 같은 경우 템플릿이 필요함.
  path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
  path('logout/', LogoutView.as_view(), name='logout'),

  path('create/', AccountCreateView.as_view(), name='create'),
  # 특정 유저 정보를 보기 위해 ID(Primary Key)가 필요하다.
  # 특정 유저 객체에 부여된 고유한 키.
  path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
  path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
]