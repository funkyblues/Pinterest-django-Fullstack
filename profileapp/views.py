from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
  model = Profile
  context_object_name = 'target_profile'
  form_class = ProfileCreationForm
  success_url = reverse_lazy('accountapp:hello_world')
  template_name = 'profileapp/create.html'

  def form_valid(self, form):
    # 커스텀 하고자 하는 내용
    # form 에서 보내진 데이터가 form안에 들어가 있음.

    # 그러나 실제 DB에 저장하는게 아닌 임시로 받아들인다고 보면 된다.
    temp_profile = form.save(commit=False)
    # user라는 데이터는 받지 않았으므로, request user를 당사자로 받자
    temp_profile.user = self.request.user
    # 그 후 최종적으로 저장
    temp_profile.save()

    # 아래 코드는 기존 함수가 데이터가 잘 들어왔는지를 확인하는 코드와 같음
    return super().form_valid(form)

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
  model = Profile
  context_object_name = 'target_profile'
  form_class = ProfileCreationForm
  success_url = reverse_lazy('accountapp:hello_world')
  template_name = 'profileapp/update.html'

