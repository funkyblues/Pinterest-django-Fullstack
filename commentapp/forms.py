from django.forms import ModelForm
from commentapp.models import Comment

class CommentCreationForm(ModelForm):
  class Meta:
    model = Comment
    # 사용자에게 받을 입력. 나머지는 알아서.
    fields = ['content']