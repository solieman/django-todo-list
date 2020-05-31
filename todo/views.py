from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import TodoList


# Create your views here.


def index(request):
    todos = TodoList.objects.all()  # quering all todos with the object manager

    if request.method == "POST":  # checking if the request method is a POST
        if "taskAdd" in request.POST:  # checking if there is a request to add a todo
            title = request.POST["description"]  # title
            Todo = TodoList(title=title)
            Todo.save()  # saving the todo
            return redirect("/")  # reloading the page
        if "taskDelete" in request.POST:  # checking if there is a request to delete a todo
            checkedlist = request.POST["checkedbox"]  # checked todos to be deleted
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id))  # getting todo id
                todo.delete()  # deleting todo
    return render(request, "hello.html", {"todos": todos})


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
