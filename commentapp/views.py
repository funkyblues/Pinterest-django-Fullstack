from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView

from articleapp.models import Article
from commentapp.decorators import comment_ownership_required
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment

class CommentCreateView(CreateView):
  model = Comment
  form_class = CommentCreationForm
  template_name = 'commentapp/create.html'

  def form_valid(self, form):

    temp_comment = form.save(commit=False)
    # create.html의 article_pk를 넘겨주는 작업
    temp_comment.article = Article.objects.get(pk=self.request.POST['article_pk'])
    # 글 쓰는 사람은 user
    temp_comment.writer = self.request.user
    temp_comment.save()

    return super().form_valid(form)


  def get_success_url(self):
    # 현재의 object는 Comment...
    return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})

@method_decorator(comment_ownership_required, 'get')
@method_decorator(comment_ownership_required, 'post')
class CommentDeleteView(DeleteView):
  model = Comment
  context_object_name = 'target_comment'
  template_name = 'commentapp/delete.html'

  def get_success_url(self):
    # 현재의 object는 Comment...
    return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})