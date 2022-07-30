# django에서 기본적으로 제공하는 User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
# django에서 제공하는 CreateView 가져오기
from django.views.generic import CreateView

from accountapp.models import HelloWorld


def hello_world(request):
  if request.method == "POST":

    temp = request.POST.get('hello_world_input')

    # models.py의 HelloWorld 클래스로 새로운 객체 생성
    new_hello_world = HelloWorld()
    # POST로 전달한 데이터를 생성한 객체의 text에 대입
    new_hello_world.text = temp
    # save를 하여 실제 DB에 new_hello_world 객체(!!!)를 저장(!!!)하게 된다.
    new_hello_world.save()

    return HttpResponseRedirect(reverse('accountapp:hello_world'))
  else:
    # HelloWorld의 모든 데이터를 다 가져온다
    hello_world_list = HelloWorld.objects.all()
    return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})

class AccountCreateView(CreateView):
  # django에서 기본 제공하는 모델 사용
  model = User
  # django에서 기본적으로 제공하는 계정 생성 폼
  form_class = UserCreationForm
  # 계정 생성에 성공했다면 리다이렉트 할 경로 지정
  # 왜 reverse_lazy? => 함수와 클래스가 불러와지는 방식의 차이 때문...
  # 클래스 형 view에서 reverse_lazy를 사용한다.
  success_url = reverse_lazy('accountapp:hello_world')
  # 계정생성 템플릿은 만들어야 한다.
  template_name = 'accountapp/create.html'