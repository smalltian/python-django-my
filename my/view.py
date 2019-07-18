from django.shortcuts import render
from django.http import HttpResponse

# 页面模版
def my(request):
    context = {}
    context['my'] = 'my django'
    return render(request, 'my.html', context)

# response形式
def hello(request):
    print ("1")
    return HttpResponse("hello")
