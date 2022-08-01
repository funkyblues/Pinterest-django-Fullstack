from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
  # django에서 기본적으로 제공하는 TemplateView
  # template만 지정해주면 나머지는 다 정해진다.
  path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='list')
]