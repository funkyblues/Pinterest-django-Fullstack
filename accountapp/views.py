from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from accountapp.models import HelloWorld


def hello_world(request):
  if request.method == "POST":

    temp = request.POST.get('hello_world_input')

    # HelloWorld 클래스로 새로운 객체 생성
    new_hello_world = HelloWorld()
    # POST로 전달한 데이터를 생성한 객체의 text에 대입
    new_hello_world.text = temp
    # save를 하여 실제 DB에 new_hello_world 객체(!!!)를 저장(!!!)하게 된다.
    new_hello_world.save()

    return HttpResponseRedirect(reverse('accountapp:hello_world'))
  else:
    # HelloWorld의 모든 데이터를 다 가져온다
    hello_world_list = HelloWorld.objects.all()
    return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})