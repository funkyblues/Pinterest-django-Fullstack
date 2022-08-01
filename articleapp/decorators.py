from django.http import HttpResponseForbidden
from articleapp.models import Article

# 계정 소유권 확인 함수


def article_ownership_required(func):
  def decorated(request, *args, **kwargs):
    # pk를 가지고 있는 User Object가 user가 된다.
    # User Object가 실제 request를 보낸 user와 같은지 아닌지를 확인하는 과정
    article = Article.objects.get(pk=kwargs['pk'])
    if not article.writer == request.user:
      return HttpResponseForbidden()
    return func(request, *args, **kwargs)
  return decorated