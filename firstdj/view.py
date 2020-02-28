from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    context  = {}
    context["hello"] = "hello swift"
    return render(request,template_name='hello.html', context=context)

def ios(request):
    return  HttpResponse("swift ")