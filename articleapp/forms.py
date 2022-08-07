from django.forms import ModelForm
from django import forms

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):
  # WYSIWYG 사용 위한 커스터마이징
  content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable',
                                                         'style': 'height: auto; text-align: left;'}))
  project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)

  class Meta:
    model = Article
    fields = ['title', 'image', 'project', 'content']