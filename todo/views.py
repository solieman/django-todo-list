from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return render(request, 'hello.html')


def todo_list(request):
    text = """<h1>Building awesome to-do list!</h1>"""
    return HttpResponse(text)


def hello_view(request):
    text = """<h1>welcome to my app !</h1>"""
    return HttpResponse(text)


def hello_parameter(request, number):
    text = "<h1>welcome to my app number %s!</h1>" % number
    return HttpResponse(text)


def hello_template(request):
    return render(request, "todo_list/template/hello.html", {})
