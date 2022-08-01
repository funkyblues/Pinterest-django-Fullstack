from django.http import HttpResponseForbidden
from profileapp.models import Profile

# 계정 소유권 확인 함수


def profile_ownership_required(func):
  def decorated(request, *args, **kwargs):
    # pk를 가지고 있는 User Object가 user가 된다.
    # User Object가 실제 request를 보낸 user와 같은지 아닌지를 확인하는 과정
    profile = Profile.objects.get(pk=kwargs['pk'])
    if not profile.user == request.user:
      return HttpResponseForbidden()
    return func(request, *args, **kwargs)
  return decorated