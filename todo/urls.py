from django.contrib import admin
from django.urls import path
from . import views

admin.autodiscover()

urlpatterns = [
    path('', views.todo_list),
    path('hello/', views.hello_view),

]
