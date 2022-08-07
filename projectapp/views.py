from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
  model = Project
  form_class = ProjectCreationForm
  template_name = 'projectapp/create.html'

  def get_success_url(self):
    return reverse('projectapp:detail', kwargs={'pk': self.object.pk})

# MultipleObjectMixin: 여러가지 Object를 다룰 수 있는 Mixin을 가져온다.
class ProjectDetailView(DetailView, MultipleObjectMixin):
  model = Project
  context_object_name = 'target_project'
  template_name = 'projectapp/detail.html'

  # MultipleObjectMixin을 가져와서 쓸 수 있게 된 paginate_by.
  paginate_by = 25

  def get_context_data(self, **kwargs):
    project = self.object
    user = self.request.user

    if user.is_authenticated:
    #   유저가 접속되어 있다면 구독 찾음
      subscription = Subscription.objects.filter(user=user, project=project)

    # 현재 Project(ProjectDetailView)의 Object와 같은 project를 가지는 Article들을 필터링
    object_list = Article.objects.filter(project=self.get_object())
    return super(ProjectDetailView, self).get_context_data(object_list=object_list,
                                                           subscription=subscription,
                                                           **kwargs)
class ProjectListView(ListView):
  model = Project
  context_object_name = 'project_list'
  template_name = 'projectapp/list.html'
  paginate_by = 25