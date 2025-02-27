from django.shortcuts import render
from .models import Task
#from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView,DeleteView

from django.contrib.auth.views import LoginView
from django.urls import  reverse_lazy

# Create your views here.
class TaskList(ListView):
    model=Task
    context_object_name='tasks'# renames Objects to tasks. We can user tasks in place of object in the application.

class TaskDetails(DetailView):
    model=Task
    template_name='base/task_detail.html'
    context_object_name='taskdetail'

class TaskCreate(CreateView):
    model=Task
    fields = '__all__' #field=['title','description'] to individually specify
    success_url= reverse_lazy('tasks')

class TaskEdit(UpdateView):
    model=Task
    fields='__all__'
    success_url=reverse_lazy('tasks')

class TaskDelete(DeleteView):
    model=Task
    template_name='base/task_delete.html'
    success_url=reverse_lazy('tasks')
class CustomeLoginView(LoginView):
    template_name='base/login.html'
    fields='__all__'
    redirect_authenticated_user=True #redirect logged in user to home
    
    def get_success_url(self):
        return reverse_lazy('tasks')