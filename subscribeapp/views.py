from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

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
      # 구독 되어 있으면 삭제하고
      subscription.delete()
    else:
      # 구독이 없다면 만들어준다.
      Subscription(user=user, project=project).save()

    return super(SubscriptionView, self).get(request, *args, **kwargs)