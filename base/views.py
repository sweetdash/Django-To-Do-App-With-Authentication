from django.shortcuts import render
from .models import Task
#from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# Create your views here.
class TaskList(ListView):
    model=Task
    context_object_name='tasks'# renames Objects to tasks. We can user tasks in place of object in the application.

class TaskDetails(DetailView):
    model=Task
    template_name='base/task_detail.html'
    context_object_name='taskdetail'