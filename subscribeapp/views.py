from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from projectapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):
  def get_redirect_url(self, *args, **kwargs):
    # project_pk를 GET방식으로 받아서 해당 pk를 가지고 있는 detail로 redirect
    return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})

  def get(self, request, *args, **kwargs):

    # project_pk를 가지고 있는 project를 찾고, 없다면 404 에러 출력
    project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
    user = self.request.user

    subscription = Subscription.objects.filter(user=user,
                                               project=project)
    if subscription.exists():
      # 구독 되어 있으면 삭제하고 (토글 느낌)
      subscription.delete()
    else:
      # 구독이 없다면 만들어준다.
      Subscription(user=user, project=project).save()

    return super(SubscriptionView, self).get(request, *args, **kwargs)

# 사용자가 어떤 프로젝트들을 구독하고 있는지...
# + 로그인 하고 있는지를 파악.
@method_decorator(login_required, 'get')
class SubscriptionListView(ListView):
  model = Article
  template_name = 'subscribeapp/list.html'
  context_object_name = 'article_list'
  paginate_by = 5

  # 가지고 올 게시글들의 조건을 변경
  def get_queryset(self):
    # values_list -> 값을 list화 시킨다. (여기선 project)
    # projects 변수 안에는 project list 가 담기게 된다.
    projects = Subscription.objects.filter(user=self.request.user).values_list('project')

    # django에서 제공하는 고급 query 문. project라는 테이블 안에 어떤 값을 가지고 온다는 구문임.
    # projects라는 리스트에 해당하는 내용의 article들을 반환
    article_list = Article.objects.filter(project__in=projects)
    return article_list