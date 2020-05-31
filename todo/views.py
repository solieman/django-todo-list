from django.shortcuts import render
from django.http import HttpResponse

from .models import TodoList, Category

# Create your views here.


def index(request):
    todos = TodoList.objects.all()  # quering all todos with the object manager
    return render(request, 'hello.html')


def todo_list(request):
    text = """<h1>Building awesome to-do list!</h1>"""
    return HttpResponse(text)


def todo_task(request):
    text = """<div class="row">
                            <button class="taskDelete" name="taskDelete" formnovalidate="" type="submit"
                                    onclick="$('input#sublist').click();"><i class="fa fa-trash-o icon"></i>Delete Tasks
                            </button>
                        </div>"""
    return HttpResponse(text)


def hello_view(request):
    text = """<h1>welcome to my app !</h1>"""
    return HttpResponse(text)


def hello_parameter(request, number):
    text = "<h1>welcome to my app number %s!</h1>" % number
    return HttpResponse(text)

