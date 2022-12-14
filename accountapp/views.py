# django에서 기본적으로 제공하는 User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
# django에서 제공하는 CreateView 가져오기
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld

# 직접 만든 데코레이터를 배열에 집어넣음
# 이 배열만 메서드 데코레이터 에게 넘겨주면 된다
from articleapp.models import Article

has_ownership = [
  account_ownership_required,
  login_required
]

# django에서 제공하는 decorator 함수
# login했는지 안했는지를 확인해줌...!
@login_required
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

# MultipleObjectMixin : 여러가지 Object를 다룰 수 있는 Mixin을 가져온다.
class AccountDetailView(DetailView, MultipleObjectMixin):
  model = User
  # 템플릿에서 사용하는 user 객체의 이름을 다르게 설정
  # 특정 pk를 가지는 user의 url로 접속하면 그 pk의 user 정보를 보여주어야 하므로  context_object_name 에 저장
  # ex. 연예인들 페이지로 가더라도 detail은 사용자인 내 정보가 아닌 연예인 정보를 보여줘야 하니까
  # 다른사람이 와도 나의 정보를 보여줄 수 있도록...(?)

  # 템플릿 파일에서 사용할 컨텍스트 변수
  # 즉 현재 방문하고 있는 유저의 정보 = context_object_name
  context_object_name = 'target_user'
  template_name = 'accountapp/detail.html'

  paginate_by = 25
  def get_context_data(self, **kwargs):
    object_list = Article.objects.filter(writer=self.get_object())
    return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)

# Update, Delete에도 context_object_name을 넣어준다

# 일반 함수에 사용하는 decorator를 메서드에 사용할 수 있도록 변환해주는 데코레이터
# 그리고 해당 클래스에서 사용할 메서드를 추가
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
  model = User
  context_object_name = 'target_user'
  form_class = AccountUpdateForm
  success_url = reverse_lazy('accountapp:hello_world')
  template_name = 'accountapp/update.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
  model = User
  context_object_name = 'target_user'
  success_url = reverse_lazy('accountapp:login')
  template_name = 'accountapp/delete.html'