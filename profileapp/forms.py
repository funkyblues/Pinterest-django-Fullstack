from django.forms import ModelForm

from profileapp.models import Profile

# Profile 모델을 form으로 변환하기 위해 ModelForm을 상속받고
# 어떤 fields를 입력가능하게 할 것인지만 넘겨주는 과정
class ProfileCreationForm(ModelForm):
  class Meta:
    model = Profile
    fields = ['image', 'nickname', 'message']